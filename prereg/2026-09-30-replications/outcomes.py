"""Deterministic extraction of submitted choices and isolated recall classification."""
from __future__ import annotations

import copy
import json
import math
import re

from runtime import HERE, StopRun, read_json


def recall_prompts():
    text = (HERE / "RECALL.md").read_text()
    common = " ".join(line[2:] for line in text.splitlines() if line.startswith("> "))
    rows = {}
    for line in text.splitlines():
        if re.match(r"\| R0[1-8] \|", line):
            study, citation, contrast = [part.strip() for part in line.split("|")[1:-1]]
            rows[study] = common.format(citation=citation, contrast=contrast)
    if len(rows) != 8:
        raise StopRun("Cannot extract all eight exact frozen recall prompts")
    return rows


def classify_recall(raw, human):
    def number(x, low, high):
        return type(x) in (int, float) and math.isfinite(x) and low <= x <= high
    try:
        data = json.loads(raw)
        if not isinstance(data, dict) or type(data.get("remembers")) is not bool:
            return "unknown"
        if data.get("direction") not in ("A", "B", "tie", "unknown"):
            return "unknown"
        if any(k not in data or (data[k] is not None and not number(data[k], 0, 1)) for k in ("rate_a", "rate_b")):
            return "unknown"
        if "sample_size" not in data or (data["sample_size"] is not None and not number(data["sample_size"], 0, float("inf"))):
            return "unknown"
        if not isinstance(data.get("detail"), str) or not number(data.get("confidence"), 0, 100):
            return "unknown"
        rates = {arm: human[arm]["x"] / human[arm]["n"] if human[arm].get("n") else human[arm]["rate"] for arm in ("a", "b")}
        direction = "B" if rates["b"] > rates["a"] else "A" if rates["b"] < rates["a"] else "tie"
        accurate = data["direction"] == direction and all(data["rate_" + arm] is not None and abs(data["rate_" + arm] - rates[arm]) <= .03 + 1e-12 for arm in ("a", "b"))
        return "positive" if data["remembers"] or accurate else "negative"
    except (ValueError, TypeError, KeyError):
        return "unknown"


def validate_panel(panel, audience, *, amendment=None):
    """Reject unverifiable eligibility; do not manufacture language/education labels."""
    seen, people = set(), []
    for person in panel.get("personas", []):
        pid = person.get("id")
        if not isinstance(pid, str) or not pid.strip():
            raise StopRun("Recruitment returned a missing persona ID")
        if pid not in seen:
            seen.add(pid)
            people.append(person)
    if len(people) != audience["n"] or not panel.get("criteria"):
        raise StopRun("Recruitment returned too few unique people or unparsed criteria")
    study = audience["id"]
    for person in people:
        demo = person.get("demographics", {})
        age = demo.get("age")
        if type(age) not in (float, int) or not math.isfinite(age) or age < 18 or (study == "R07" and age > 65):
            raise StopRun(f"{study}: failed adult/age eligibility for {person['id']}")
        country = str((demo.get("location") or {}).get("country", "")).upper()
        required = {"R01": {"US", "USA"}, "R02": {"US", "USA"}, "R06": {"AT", "DE"}, "R07": {"GB", "UK"}, "R08": {"US", "USA"}}.get(study)
        if required and country not in required:
            raise StopRun(f"{study}: country eligibility failed for {person['id']}")
        narrative = person.get("narrative")
        if not isinstance(narrative, str) or not narrative.strip() or "mock narrative" in narrative.lower() or narrative == "A person going about their daily life.":
            raise StopRun(f"{study}: failed hydration for {person['id']}")
        # Only explicit persona evidence, not the injected audience prompt/context.
        evidence = json.dumps({"narrative": narrative, "demographics": demo,
                               "languages": person.get("languages", person.get("language"))}, ensure_ascii=False).lower()
        if study in ("R03", "R04", "R05", "R06") and not re.search(r"german|deutsch|\bde-DE\b", evidence, re.I):
            raise StopRun(f"{study}: German-language eligibility is not evidenced for {person['id']}")
        if study in ("R07", "R08"):
            if amendment == "A3":
                # Residence was checked above. Use the exact registered locale
                # passed to the session; do not add a language label to a person.
                locale = {"R07": "en-GB", "R08": "en-US"}[study]
                if audience.get("locale") != locale:
                    raise StopRun(f"{study}: English evidence requires residence and registered browser locale {locale}")
            elif not re.search(r"english|\ben-(gb|us)\b", evidence):
                raise StopRun(f"{study}: English-language eligibility is not evidenced for {person['id']}")
        if study == "R06":
            subject = r"computer science|computing|informatik"
            label = "computing"
            if audience.get("hard_eligibility") == "Austria or Germany; German-speaking undergraduate in a technical subject; adult":
                subject += r"|engineering|ingenieur|mathematics|mathematik|physics|physik"
                label = "technical-subject"
            if not (re.search(subject, evidence) and re.search(r"undergraduat|bachelor|first.year|erstsemester", evidence)):
                raise StopRun(f"R06: {label} undergraduate eligibility is not evidenced for {person['id']}")
    return people


def extract(visit, person_id, exported, result, *, transport_failure=None, fallback=False):
    keys = [("a", "cell_0"), ("b", "cell_1")] if visit["study"] == "R07" else [(visit["variant"], "primary")]
    journey = result.get("journey", [])
    reason = transport_failure or result.get("error")
    if any(step.get("action") in ("engine_consent", "test_limit", "error", "engine_event") for step in journey):
        reason = reason or "engine consent, cutoff or technical error in journey"
    if not isinstance(exported, dict) or any(exported.get(k) != value for k, value in
            (("schema", 1), ("site", "s" + visit["study"][1:]), ("variant", visit["variant"]), ("index", visit["index"]))):
        reason = reason or "missing or mismatched submitted-choice export"
    if not journey:
        reason = reason or "missing engine trace"
    export = exported if isinstance(exported, dict) else {}
    decisions = export.get("decisions", {})
    events = export.get("events", [])
    if not isinstance(decisions, dict) or not isinstance(events, list) or not all(isinstance(e, dict) for e in events):
        reason = reason or "malformed export"
        decisions, events = {}, []
    offered = [e.get("cell") for e in events if e.get("type") == "portfolio_cell"]
    voluntary = bool(journey and journey[-1].get("action") in ("done", "give_up") and not journey[-1].get("engine_note"))
    rows = []
    for arm, key in keys:
        row = {"study": visit["study"], "arm": arm, "person_id": person_id, "index": visit["index"],
               "value": None, "status": "technical_failure", "session": visit["session"],
               "fallback": fallback, "reason": reason, "decision_latency_ms": None}
        decision = decisions.get(key)
        matching = [e for e in events if e.get("type") == "decision" and e.get("key") == key]
        if not reason and isinstance(decision, dict) and type(decision.get("value")) is int and decision["value"] in (0, 1) and matching and all(e.get("value") == decision["value"] and e.get("choice") == decision.get("choice") for e in matching):
            row.update(value=decision["value"], status="observed", decision_latency_ms=matching[0].get("elapsed_ms"))
        elif not reason and decision is None and voluntary:
            if visit["study"] != "R07" or (offered and key == f"cell_{offered[-1]}"):
                row.update(value=0, status="voluntary_exit", reason="evidenced participant exit")
            else:
                row["reason"] = "portfolio cell was not offered at voluntary exit"
        elif not reason:
            row["reason"] = "no submitted decision or evidenced voluntary exit"
        rows.append(row)
    return rows


def score_observations(data):
    # This is the exact frozen scorer, not a reimplementation of its statistics.
    import importlib.util
    if data.get("amendment") not in (None, "A1", "A2", "A3"):
        raise ValueError("Unsupported scoring amendment")
    name = "score_a2.py" if data.get("amendment") in ("A2", "A3") else "score.py"
    spec = importlib.util.spec_from_file_location("r1_frozen_scorer", HERE / name)
    scorer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(scorer)
    truth = read_json(HERE / "human.json")
    def score(value):
        # A3 changes eligibility only. Feed the unchanged A2 scorer its exact
        # metadata contract, then label the result with the execution amendment.
        result = scorer.score(value | {"amendment": "A2"} if value.get("amendment") == "A3" else value, truth)
        if value.get("amendment") == "A3":
            result["amendment"] = "A3"
        return result
    scored = score(data)
    excluded = copy.deepcopy(data)
    for row in excluded["records"]:
        if row.get("fallback"):
            row.update(value=None, status="technical_failure")
    sensitivity = score(excluded)
    completers = {}
    for arm in ("a", "b"):
        rows = [r for r in data["records"] if r["study"] == "R01" and r["arm"] == arm and r["status"] == "observed"]
        completers[arm] = {"x": sum(r["value"] for r in rows), "n": len(rows),
                           "rate": sum(r["value"] for r in rows) / len(rows) if rows else None}
    complete = all(completers[arm]["n"] for arm in ("a", "b"))
    completers["sim_delta"] = completers["b"]["rate"] - completers["a"]["rate"] if complete else None
    completers["ci95"] = scorer.newcombe(completers["a"], completers["b"]) if complete else None
    completers["interpretation"] = "Available completers only; sensitivity, never a replacement for the registered denominator"
    return {"primary": scored, "fallback_excluded": sensitivity, "R01_completer_only": completers}
