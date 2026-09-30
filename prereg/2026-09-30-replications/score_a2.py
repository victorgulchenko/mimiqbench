"""Frozen A2 analysis: R06 is an administrative direction miss, never an observation.

Uses the unchanged R1 scorer for all per-study statistics and input validation.
Offline only; no model, browser or network capability.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

import score as original
from score import newcombe

R06_REASON = "not run: the simulated population contains no university students"
NOT_RUN = {"R06": R06_REASON}
RUN_STUDIES = ("R01", "R02", "R03", "R04", "R05", "R07", "R08")


def score(data, truth):
    if data.get("amendment") != "A2" or data.get("not_run") != NOT_RUN:
        raise ValueError("A2 scoring requires the exact registered R06 not-run rule")
    if {s["id"] for s in truth["studies"]} != set(RUN_STUDIES) | {"R06"} or len(truth["studies"]) != 8:
        raise ValueError("A2 retains all eight human references")
    if any(r["study"] == "R06" for r in data["records"] + data.get("recall", [])):
        raise ValueError("A2 forbids R06 observations, invented panel slots and recall probes")
    result = original.score(data, truth)
    omitted = next(r for r in result["studies"] if r["study"] == "R06")
    omitted.update(status="not_run", reason=R06_REASON, direction_match=0,
                   primary_resolved=True, recall="not_run")
    ran = [r for r in result["studies"] if r["study"] in RUN_STUDIES]
    complete = all(r["complete"] for r in ran)
    recall_complete = all(r["recall"] != "unknown" for r in ran)
    successes = sum(r["direction_match"] or 0 for r in ran)
    groups = {}
    for group in result["source_group_shares"]:
        members = [r for r in result["studies"] if r["group"] == group]
        groups[group] = (sum(r["direction_match"] for r in members) / len(members)
                         if all(r["complete"] or r.get("primary_resolved") for r in members) else None)
    # R1.2 and R1.3 use only the seven executed studies, including the R1.3
    # overall comparison share. R06 is not an unknown or recall-negative probe.
    splits = {}
    for field, labels in (("fame", ("high", "lower")), ("recall", ("positive", "negative", "unknown"))):
        for label in labels:
            subset = [r for r in ran if r[field] == label]
            finished = [r for r in subset if r["complete"]]
            splits[f"{field}:{label}"] = {"registered": len(subset), "completed": len(finished),
                                          "matches": sum(r["direction_match"] for r in finished)}
    negative = [r for r in ran if r["recall"] == "negative"]
    survival = "UNASSESSABLE"
    if complete and recall_complete and len(negative) >= 3:
        share = sum(r["direction_match"] for r in negative) / len(negative)
        survival = "PASS" if share >= successes / len(ran) - .15 else "FAIL"
    result.update(
        amendment="A2", not_run=NOT_RUN.copy(), complete=complete, recall_complete=recall_complete,
        verdict=("PASS" if successes >= 7 else "FAIL") if complete and recall_complete else "INCOMPLETE",
        direction_matches=successes, direction_share=successes / 8 if complete else None,
        descriptive_wilson_ci95=original.wilson(successes, 8) if complete else None,
        coin_tail_probability_descriptive=sum(math.comb(8, k) for k in range(successes, 9)) / 256 if complete else None,
        source_group_shares=groups,
        source_group_equal_weight_mean=sum(groups.values()) / len(groups) if complete else None,
        splits=splits, secondary_studies=list(RUN_STUDIES), secondary_excluded_studies=["R06"],
        absolute_delta_error_mean=sum(r["absolute_error"] for r in ran) / len(ran) if complete else None,
        within_10pp=sum(r["absolute_error"] <= .10 for r in ran) if complete else None,
        recall_survival_secondary=survival)
    result["limitations"].append(
        "A2: R06 was not run and counts as a direction MISS (0) in the eight-study primary metric; "
        "it is absent from R1.2 magnitude and R1.3 contamination, including their splits and comparison share. "
        "Suite completeness means seven resolved studies plus the registered R06 administrative miss.")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("observations", type=Path)
    args = parser.parse_args()
    truth = json.loads(Path(__file__).with_name("human.json").read_text())
    print(json.dumps(score(json.loads(args.observations.read_text()), truth), indent=2))
