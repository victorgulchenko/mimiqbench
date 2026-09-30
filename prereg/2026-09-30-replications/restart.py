"""Reviewed pre-exposure A1/A2 restarts. Validation and copying are offline."""
from __future__ import annotations

from decimal import Decimal
from pathlib import Path
import shutil

from runtime import A1_MANIFEST_SHA, MANIFEST_SHA, StopRun, digest, read_json, verify_entries
from outcomes import validate_panel

A1_DOCUMENT_SHA = "ba2a64d18a5bc452a112f05cac5ed268564b14980de8fe566ab1d60eadab63aa"
PRIOR_STATE_SHA = "1caf2b953e5532923ae05d7af090c412dae07780613adeefc232a17eabdb3955"
PRIOR_ARTIFACTS_SHA = "0327d7fc92b66d0a7c254074d72dbfabfc35ab1d99b671cb51577dceec0e832d"
A1_STATE_SHA = "2206a2458cec8d15d5ec5189bf3e13c5c34739183dbb89c053a64f7265b95732"
A1_ARTIFACTS_SHA = "878a6d20b0115e6e787d1be29c76b69d68ed7cece7fa43bb2b41554c5f7656ec"
REUSE_STUDIES = ("R01", "R02", "R03", "R04", "R05")
PRIOR_STOP = "StopRun: Recruitment returned too few unique people or unparsed criteria"


def verified_prior_state(prior):
    path = Path(prior["output"]) / "state.json"
    expected = A1_STATE_SHA if prior.get("amendment") == "A1" else PRIOR_STATE_SHA
    if prior["state_sha256"] != expected or digest(path) != expected:
        raise StopRun("Prior-attempt state hash mismatch")
    return read_json(path)


def attempt_history(prior):
    """Original first, then A1; each attempt appears exactly once."""
    return (attempt_history(prior["prior_attempt"]) if prior.get("prior_attempt") else []) + [prior]


def verify_prior_attempt(output, audiences, amendment="A1"):
    """Pin the actual failed attempt, not an arbitrary user-selected panel cache."""
    if amendment not in ("A1", "A2"):
        raise StopRun("Unsupported restart amendment")
    a2 = amendment == "A2"
    state_sha = A1_STATE_SHA if a2 else PRIOR_STATE_SHA
    artifacts_sha = A1_ARTIFACTS_SHA if a2 else PRIOR_ARTIFACTS_SHA
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
    if (state.get("gate", {}).get("manifest_sha256") != (A1_MANIFEST_SHA if a2 else MANIFEST_SHA) or
            state.get("gate", {}).get("amendment") != ("A1" if a2 else None) or
            state.get("attempted_sessions") != [] or state.get("stop_reason") != PRIOR_STOP or
            not state.get("ended_at") or set(state.get("panels", {})) != set(REUSE_STUDIES) or
            state.get("unrecruited_studies") != ["R06", "R07", "R08"]):
        raise StopRun(f"{amendment} requires the pinned recruitment stop with zero exposures")
    observations = read_json(output / "observations.json")
    if ((output / "recall.jsonl").exists() or any((output / "traces").rglob("*")) or
            any(r.get("status") != "not_run" or r.get("value") is not None for r in observations["records"]) or
            any(r.get("status") != "unknown" for r in observations["recall"])):
        raise StopRun(f"{amendment} cannot restart after page exposure or recall")
    prior = None
    if a2:
        if not state.get("prior_attempt"):
            raise StopRun("A2 requires both original and A1 stopped attempts")
        prior = verify_prior_attempt(state["prior_attempt"]["output"], audiences)
        if prior != state["prior_attempt"] or state.get("skeleton_sha256") != verified_prior_state(prior).get("skeleton_sha256"):
            raise StopRun("A1 history or skeleton pool differs from the original attempt")
        for name in ("state.json", "artifacts.sha256.json", "RESULTS.md"):
            if digest(output / "prior-attempt" / name) != digest(Path(prior["output"]) / name):
                raise StopRun("A1 retained original evidence differs")
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
    if a2 and panels != prior["panels"]:
        raise StopRun("A1 panels differ from the original hashed panels")
    spent = sum((Decimal(str(e["usd"])) for e in events), Decimal(0))
    if spent != sum((Decimal(str(e["charged_usd"])) for e in events if e["event"] == "settle"), Decimal(0)):
        raise StopRun("First-attempt settlements do not reconcile")
    summary = {"output": str(output), "state_sha256": state_sha,
            "artifacts_sha256": artifacts_sha, "stop_reason": state["stop_reason"],
            "started_at": state["started_at"], "ended_at": state["ended_at"],
            "attempted_sessions": 0, "spent_usd": float(spent), "panels": panels}
    if a2:
        summary.update(amendment="A1", prior_attempt=prior)
    return summary


def reuse_panels(prior, out, audiences, state):
    """Copy verified bytes, preserve order, and never invoke the panel builder."""
    amendment = "A2" if prior.get("amendment") == "A1" else "A1"
    if verify_prior_attempt(prior["output"], audiences, amendment) != prior:
        raise StopRun("First-attempt evidence changed since the gate")
    history = attempt_history(prior)
    out = Path(out).resolve()
    for attempt in history:
        source = Path(attempt["output"])
        if out == source or out.is_relative_to(source) or source.is_relative_to(out):
            raise StopRun("Amended output must be separate from both prior attempts")
    by_id = {a["id"]: a for a in audiences["studies"]}
    panels = {}
    # Keep the first stop/cost record with the new evidence, without altering it.
    retained = out
    for attempt in reversed(history):
        retained = retained / "prior-attempt"
        retained.mkdir()
        for name in ("state.json", "artifacts.sha256.json", "RESULTS.md"):
            shutil.copyfile(Path(attempt["output"]) / name, retained / name)
    source = Path(history[0]["output"])
    for study in REUSE_STUDIES:
        for suffix in (".json", ".started.json", ".demographics.json"):
            shutil.copyfile(source / "panels" / (study + suffix), out / "panels" / (study + suffix))
        path = out / "panels" / f"{study}.json"
        entry = prior["panels"][study]
        if digest(path) != entry["sha256"]:
            raise StopRun(f"Copied {study} panel hash mismatch")
        panels[study] = validate_panel(read_json(path), by_id[study])
        state["panels"][study] = {**entry, "path": str(path), "reused_from": str(source)}
    state["prior_attempt"] = prior
    return panels
