# Plan: twin2k-ask, a stated estimate against ask the room's tally, on held-out survey questions

Final, 2026-09-24. This is Part B of the engine lane's plan, made its own plan and finalized by the proof
lane; built from dev results only. No model has seen any held-out item of this suite. The commit that
adds this file to the public register is its timestamp. Nothing below changes after that; results and
deviations go in RESULTS next to it.

Mimiq keeps its choice of AI models confidential, so this plan names models by role only (the
estimate's model, the people's model). Their exact identities and settings are fixed by a private
configuration file whose sha256 is below; the run refuses to start if that file differs by one byte.

## Question and hypotheses

On dev (63 survey items asked of everyone), the tally of Mimiq's "ask the room" (25 simulated people
answering in character) was no closer to the real answer shares than a uniform guess (error 0.225
against 0.206), while one call asking a model to state the audience's distribution scored 0.130. Does
that hold on held-out questions?

- H-B1 (primary): on the held-out items asked of everyone, the stated estimate's mean error is lower
  than the room's: the paired difference is below 0 and the upper end of its 95% cluster-bootstrap
  interval is below 0.
- H-B2: on all held-out distribution items (subgroups included), the stated estimate's mean error is at
  least 0.05 below a uniform guess's.

Scope: the room is a follow-up tool; its prompt treats the question as a follow-up to something the
person was shown. It is the closest production instrument that tallies options. H-B1 is about the
room's tally, not about a survey product Mimiq does not have.

## Data

- Suite `twin2k-ask` (Twin-2K-500, Toubia et al. 2025, CC BY 4.0): real answers of 2,058 US adults, early
  2025. Held-out split as fixed in the suite's split.json.
- items.jsonl sha256 `d9c83e9cb5acc6c45df0c51e1640c4ddda856e474468160805ce145b11001fb1`. The sample is
  held-out positions 1 to 682, all distribution items (the suite's framing pairs are not part of this
  plan); sample ids sha256 `697eed80eedcc020a61cbcd5aa3451ac3a39b1a989c3197cf5f9b5425ce65394`.
- "Asked of everyone" = the items whose group is everyone: 188 held-out items (38 attitude questions and
  150 pricing items, 30 products at 5 prices).
- Error: Wasserstein distance divided by (options - 1) on ordered scales, total variation otherwise
  (`benchmarks/mimiqbench/score.py`, as `confirm.py` applies it).
- Clusters for the bootstrap: the item's question or product (`unit`); 68 among the 188 items.

## Method

- The stated estimate: `room.stated_distribution` exactly as `benchmarks/lab/patches/engine-stated-room.patch`
  adds it to production's `room.py`. The patch is not applied to production; the harness compiles the
  function the patch adds, in `room.py`'s own namespace, and the patch file's sha256 is one of the frozen
  code units. It is called as the engine lane validated it on dev: the question without its option list,
  the options, the item's audience text, no content; the estimate's model. It runs on all 682 items. An
  unparsable answer is asked once more (the same prompt as a new request), then counted as missing.
- The room: production `room.ask_room` with the item's options and the item's context as the content,
  25 people from `benchmarks/engine_lab/panels/us-adults-25.json` (built the app's way on dev; its sha256
  is a frozen code unit), the people's model. It runs on the 188 items asked of everyone.
- A missing distribution (no parsable estimate after the retry, or a room with no parsable answer) is
  scored as a uniform guess and counted. An item a method never ran on (for example after a budget stop)
  is left out of that comparison and reported, never scored as uniform.

## Primary metric

H-B1: over the 188 items, the mean of (stated error minus room error), with a 95% cluster-bootstrap
interval (`benchmarks/mimiqbench/stats.py cluster_bootstrap`: resample the 68 clusters, 5,000 draws, seed
11). H-B2: the stated estimate's mean error over the 682 items against a uniform guess's mean error on the
same items.

## Pass lines (set now)

- H-B1 passes if the mean difference is below 0 and the upper end of its interval is below 0.
- H-B2 passes if the stated estimate's mean error is at most the uniform guess's minus 0.05.

What dev showed (exploratory; engine lane files): on 63 items asked of everyone, the patched stated
estimate 0.130, the room 0.225, a uniform guess 0.206. The engine lane's earlier plugin version of the
estimate (a prompt that differs slightly from the patch's) scored a paired difference of -0.091 against
the room (95% cluster interval -0.122 to -0.059, 23 clusters). On all 232 dev items the patched estimate
scored 0.109 against a uniform guess's 0.197.

## Secondary checks (no pass lines)

- Subgroup gaps: for ordered attitude items, the gap between a subgroup's mean answer and everyone's (on a
  0 to 1 scale), predicted against real: the correlation and the least-squares slope of real on predicted
  (dev: +0.77 and 0.66).
- Both methods' mean distances next to the same people answering again two weeks later (the retest
  floor), and next to everyone's real shares used for each subgroup.
- How many answers were missing, per method.

## Configuration, code and the gate

- Private configuration: `benchmarks/mimiqbench/configs/stated-room.json`, sha256
  `4b82ee77c17a455e7fdfb7921b755ce9cfce790be0372909563bc449d89af2f5`.
- Code hash `680021428274c121d9d236838da5bde22e584220be32e6053bd3a3be15a0f0dc` (36 code units, including the
  patch file and the panel file).
- The runner (`benchmarks/mimiqbench/plans.py`, `check`, called by `runner.run` for every held-out
  step) refuses to run unless the GO line names this file's sha256 and the public commit, the
  configuration's sha256 matches, the items and sample hash as above, no sample id appears in any earlier
  cache, and every code unit is unchanged (or a deviation is declared and reported).

## Cost and stopping

About $8 in all: the stated estimate about $0.72 (measured on dev at $0.001 an item), the room about $6.60
(about $0.035 an item). Cap $8.00, charged to the engine lane, whose plan this is. The estimate runs first,
so a budget stop can only shorten the room's run; the analysis then uses the items both methods ran on
and reports the shortfall.

## Deviations before the run (clarifications made at finalization)

- The engine lane's draft defined "asked of everyone" as `extra.group_key == "all"`, which matches only
  the 38 attitude items; its own count, 188, matches the definition used here (the group is everyone,
  which also covers the 150 pricing items). This plan uses the definition that gives the count the draft
  stated.
- Added at finalization: the rule for a room with no parsable answer (scored as uniform, like a missing
  estimate), and the rule for items a method never ran on (left out and reported).
- Part B is its own plan; Part A (a model trained on past headline tests) is not part of this run.

## What we publish whatever happens

Every number above with its interval, including those against the estimate; the sample and its hashes;
every deviation.
