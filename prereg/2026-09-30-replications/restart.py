"""Reviewed pre-exposure A1/A2/A3 restarts. Validation and copying are offline."""
from __future__ import annotations

from decimal import Decimal
from pathlib import Path
import shutil

from runtime import A1_MANIFEST_SHA, A2_MANIFEST_SHA, MANIFEST_SHA, StopRun, digest, read_json, verify_entries
from outcomes import validate_panel
from score_a2 import NOT_RUN

A1_DOCUMENT_SHA = "ba2a64d18a5bc452a112f05cac5ed268564b14980de8fe566ab1d60eadab63aa"
PRIOR_STATE_SHA = "1caf2b953e5532923ae05d7af090c412dae07780613adeefc232a17eabdb3955"
PRIOR_ARTIFACTS_SHA = "0327d7fc92b66d0a7c254074d72dbfabfc35ab1d99b671cb51577dceec0e832d"
A1_STATE_SHA = "2206a2458cec8d15d5ec5189bf3e13c5c34739183dbb89c053a64f7265b95732"
A1_ARTIFACTS_SHA = "878a6d20b0115e6e787d1be29c76b69d68ed7cece7fa43bb2b41554c5f7656ec"
A2_STATE_SHA = "30751c515ea688dea5ea8a2e461538541e2adc02c52a26f6f1bf22f517e71acc"
A2_ARTIFACTS_SHA = "a644dd961367540ab1cb005e031cf259f41ca6edaf341dc4496cf3544f3f3f12"
A2_R07_PANEL_SHA = "6454cc269e9c4fa4c1e053bfe599a883bb1b4c54ffdb873d8e293e7c4aa7e4c5"
REUSE_STUDIES = ("R01", "R02", "R03", "R04", "R05")
A3_REUSE_STUDIES = REUSE_STUDIES + ("R07",)
PRIOR_STOP = "StopRun: Recruitment returned too few unique people or unparsed criteria"
A2_STOP_PREFIX = "StopRun: R07: English-language eligibility is not evidenced for "


def verified_prior_state(prior):
    path = Path(prior["output"]) / "state.json"
    expected = {None: PRIOR_STATE_SHA, "A1": A1_STATE_SHA, "A2": A2_STATE_SHA}.get(prior.get("amendment"))
    if prior["state_sha256"] != expected or digest(path) != expected:
        raise StopRun("Prior-attempt state hash mismatch")
    return read_json(path)


def attempt_history(prior):
    """Original first, then amendments; each attempt appears exactly once."""
    return (attempt_history(prior["prior_attempt"]) if prior.get("prior_attempt") else []) + [prior]


def verify_prior_attempt(output, audiences, amendment="A1"):
    """Pin the actual failed attempt, not an arbitrary user-selected panel cache."""
    if amendment not in ("A1", "A2", "A3"):
        raise StopRun("Unsupported restart amendment")
    previous = {"A1": None, "A2": "A1", "A3": "A2"}[amendment]
    state_sha = {None: PRIOR_STATE_SHA, "A1": A1_STATE_SHA, "A2": A2_STATE_SHA}[previous]
    artifacts_sha = {None: PRIOR_ARTIFACTS_SHA, "A1": A1_ARTIFACTS_SHA, "A2": A2_ARTIFACTS_SHA}[previous]
    output = Path(output).resolve()
    if digest(output / "state.json") != state_sha:
        raise StopRun("First-attempt state hash mismatch")
    if digest(output / "artifacts.sha256.json") != artifacts_sha:
        raise StopRun("First-attempt artifact manifest hash mismatch")
    artifacts = read_json(output / "artifacts.sha256.json")
    verify_entries(artifacts, output)
    actual = {str(p.relative_to(output)) for p in output.rglob("*") if p.is_file()}
    if actual != set(artifacts) | {"artifacts.sha256.json"}:
        raise StopRun("First-attempt evidence contains unregistered files")
    state = read_json(output / "state.json")
    expected_manifest = {None: MANIFEST_SHA, "A1": A1_MANIFEST_SHA, "A2": A2_MANIFEST_SHA}[previous]
    valid_stop = (str(state.get("stop_reason", "")).startswith(A2_STOP_PREFIX)
                  if amendment == "A3" else state.get("stop_reason") == PRIOR_STOP)
    if (state.get("gate", {}).get("manifest_sha256") != expected_manifest or
            state.get("gate", {}).get("amendment") != previous or
            state.get("attempted_sessions") != [] or not valid_stop or
            not state.get("ended_at") or set(state.get("panels", {})) != set(REUSE_STUDIES) or
            state.get("unrecruited_studies") != (["R07", "R08"] if amendment == "A3" else ["R06", "R07", "R08"])):
        raise StopRun(f"{amendment} requires the pinned recruitment stop with zero exposures")
    observations = read_json(output / "observations.json")
    if amendment == "A3" and (state.get("not_run_studies") != NOT_RUN or
                               observations.get("amendment") != "A2" or observations.get("not_run") != NOT_RUN):
        raise StopRun("A3 requires the unchanged A2 R06 not-run rule")
    if ((output / "recall.jsonl").exists() or any((output / "traces").rglob("*")) or
            any(r.get("status") != "not_run" or r.get("value") is not None for r in observations["records"]) or
            any(r.get("status") != "unknown" for r in observations["recall"])):
        raise StopRun(f"{amendment} cannot restart after page exposure or recall")
    prior = None
    if previous:
        if not state.get("prior_attempt"):
            raise StopRun(f"{amendment} requires the complete stopped-attempt history")
        prior = verify_prior_attempt(state["prior_attempt"]["output"], audiences, previous)
        if prior != state["prior_attempt"] or state.get("skeleton_sha256") != verified_prior_state(prior).get("skeleton_sha256"):
            raise StopRun("Prior history or skeleton pool differs from the original attempt")
        for name in ("state.json", "artifacts.sha256.json", "RESULTS.md"):
            if digest(output / "prior-attempt" / name) != digest(Path(prior["output"]) / name):
                raise StopRun("Retained prior evidence differs")
    events = state["cost_events"]
    reserves = [e["reservation_id"] for e in events if e["event"] == "reserve"]
    settles = [e["reservation_id"] for e in events if e["event"] == "settle"]
    if (any(e["phase"] != "recruitment" or e["event"] not in ("reserve", "settle") for e in events) or
            len(set(reserves)) != len(reserves) or sorted(reserves) != sorted(settles)):
        raise StopRun("First-attempt costs are ambiguous or extend beyond recruitment")
    by_id = {a["id"]: a for a in audiences["studies"]}
    panels = {}
    for study in REUSE_STUDIES:
        entry = state["panels"][study]
        path = output / "panels" / f"{study}.json"
        if digest(path) != entry["sha256"]:
            raise StopRun(f"Saved {study} panel hash mismatch")
        people = validate_panel(read_json(path), by_id[study])
        if len(people) != entry["n"]:
            raise StopRun(f"Saved {study} panel count mismatch")
        panels[study] = {"sha256": entry["sha256"], "n": entry["n"]}
    if previous and panels != prior["panels"]:
        raise StopRun("Reused panels differ from the original hashed panels")
    if amendment == "A3":
        path = output / "panels/R07.json"
        if digest(path) != A2_R07_PANEL_SHA:
            raise StopRun("Saved R07 panel hash mismatch")
        people = validate_panel(read_json(path), by_id["R07"], amendment="A3")
        panels["R07"] = {"sha256": A2_R07_PANEL_SHA, "n": len(people)}
    spent = sum((Decimal(str(e["usd"])) for e in events), Decimal(0))
    if spent != sum((Decimal(str(e["charged_usd"])) for e in events if e["event"] == "settle"), Decimal(0)):
        raise StopRun("First-attempt settlements do not reconcile")
    summary = {"output": str(output), "state_sha256": state_sha,
            "artifacts_sha256": artifacts_sha, "stop_reason": state["stop_reason"],
            "started_at": state["started_at"], "ended_at": state["ended_at"],
            "attempted_sessions": 0, "spent_usd": float(spent), "panels": panels}
    if previous:
        summary.update(amendment=previous, prior_attempt=prior)
    return summary


def preflight_reused_panels(prior, audiences):
    """Revalidate all retained panels offline, before claiming an execution."""
    amendment = {None: "A1", "A1": "A2", "A2": "A3"}.get(prior.get("amendment"))
    try:
        if verify_prior_attempt(prior["output"], audiences, amendment) != prior:
            raise StopRun("Prior-attempt evidence changed since the gate")
    except (StopRun, OSError, ValueError, KeyError, TypeError) as exc:
        raise StopRun(f"Reused-panel pre-flight failed at $0 before execution_start: {exc}") from exc


def reuse_panels(prior, out, audiences, state):
    """Copy verified bytes, preserve order, and never invoke the panel builder."""
    preflight_reused_panels(prior, audiences)
    amendment = {None: "A1", "A1": "A2", "A2": "A3"}[prior.get("amendment")]
    history = attempt_history(prior)
    out = Path(out).resolve()
    for attempt in history:
        source = Path(attempt["output"])
        if out == source or out.is_relative_to(source) or source.is_relative_to(out):
            raise StopRun("Amended output must be separate from all prior attempts")
    by_id = {a["id"]: a for a in audiences["studies"]}
    panels = {}
    # Keep the first stop/cost record with the new evidence, without altering it.
    retained = out
    for attempt in reversed(history):
        retained = retained / "prior-attempt"
        retained.mkdir()
        for name in ("state.json", "artifacts.sha256.json", "RESULTS.md"):
            shutil.copyfile(Path(attempt["output"]) / name, retained / name)
    for study in (A3_REUSE_STUDIES if amendment == "A3" else REUSE_STUDIES):
        source = Path(prior["output"] if study == "R07" else history[0]["output"])
        for suffix in (".json", ".started.json", ".demographics.json"):
            if study == "R07" and suffix == ".demographics.json":
                continue  # A2 stopped before writing demographics; never invent a language label.
            shutil.copyfile(source / "panels" / (study + suffix), out / "panels" / (study + suffix))
        path = out / "panels" / f"{study}.json"
        entry = prior["panels"][study]
        if digest(path) != entry["sha256"]:
            raise StopRun(f"Copied {study} panel hash mismatch")
        panels[study] = validate_panel(read_json(path), by_id[study], amendment=amendment)
        state["panels"][study] = {**entry, "path": str(path), "reused_from": str(source)}
    state["prior_attempt"] = prior
    return panels
