# Plan: megaoath-copy, which honesty oath makes people report their income more honestly

Final, 2026-09-24. Written by the proof lane; no model has seen any item of this suite. The commit
that adds this file to the public register is its timestamp. Nothing below changes after that;
results and deviations go in RESULTS next to it.

Mimiq keeps its choice of AI models confidential, so this plan names models by role only (the
forecast's model, the people's model, the recruiting model). Their exact identities and settings are
fixed by a private configuration file whose sha256 is below; the run refuses to start if that file
differs by one byte.

## Question and hypotheses

Can Mimiq order 21 one-sentence oaths by how honestly real people then reported their income, as well
as lay people, finance experts, behavioural scientists and the study's own collaborators did?

- H1 (primary): Mimiq's forecast ranks the 21 oaths in the real order: Spearman above 0, one-sided p
  below 0.05.
- H2: on the 20 oaths the forecasters rated, it ranks at least as well as lay people (the best human
  group): Spearman at least 0.4045.
- H3: on pairs with a significant winner, it picks the winner more often than not: the lower end of the
  95% interval that resamples oaths is above 50%.
- H4: Mimiq's simulated people alone rank the oaths positively: Spearman above 0, one-sided p below 0.05.

## Data

- Source: Zickfeld et al. (2025), "Effectiveness of ex-ante honesty oaths in reducing dishonesty
  depends on content", *Nature Human Behaviour*; data Zenodo 13329833, materials OSF t3sm4; CC BY 4.0.
  About 1,000 people per oath in a paid tax game; outcome: declared income as a share of earned income,
  minus the no-oath control. Forecasts from five groups, from the source's files.
- Suite `megaoath-copy`, all 211 items held-out (one study): 1 ranking over 21 oaths and 210 pairs (41
  clear, 26 likely, 87 unclear, 56 ties). Kind `copy`.
- items.jsonl sha256 `8b233e8ce3ac19fd42b8ded14126f593d8f08b7cb0dd4204849fda6e2717b7d1`. The sample is
  held-out positions 1 to 211; sample ids sha256
  `8a14c4daeb99fd69ebc96c9a8dce98e44c3710cb8babb948848fe42ded513c84`.
- Exclusions, fixed now: a pair whose forecast cannot be parsed in either order, after production's
  retries, is left out of pair accuracy and counted, and counts 0.5 in the ranking.

## Method

1. After the GO, recruit 25 simulated people for the items' audience the way the app does (seed
   20260924, the recruiting model); its sha256 goes in the results.
2. Mimiq's forecast on the 210 pairs, exactly as the app's compare call makes it (kind `copy`, the
   default setting, both orders; a pick when both orders agree), the forecast's model.
3. The ranking: each oath's Copeland score over those 210 forecasts. No new call.
4. Mimiq's people on each of the 21 oaths (the app's copy test, `copy_test.run_copy_batch`, the 25
   people, the people's model); an oath's score is the people's mean stated "stop to read" per 100, the
   number the app's comparison moves on. The people's pair picks and Mimiq's call on the 210 pairs come
   from these same answers.
5. The memory probe on the first 20 winner pairs in split order (the forecast's model, with and without
   the study named, both orders).

## Primary metric

Spearman between the 21 Copeland scores and the real effects; one-sided p from 100,000 random
permutations (seed 7); 95% interval by resampling oaths (3,000 draws, seed 11). H2 uses the same
computation on the 20 oaths the forecasters rated (one oath has no forecasts). H3 uses the 95% interval
that resamples oaths (2,000 draws, seed 11), because the 210 pairs share oaths. Code:
`benchmarks/mimiqbench/confirm.py`, `score.py`, `stats.py`.

## Baselines (the source's forecasts)

Spearman with the real effects over the 20 rated oaths: lay people 0.4045 (card: 0.41), finance experts
0.42, collaborators 0.29, behavioural scientists 0.25, language models run by the study's authors 0.06.
A coin: 0 and 50%. No rule of thumb is named for this suite.

## Pass lines (set now)

- H1: Spearman > 0 and one-sided p < 0.05.
- H2: Spearman on the 20 rated oaths at least 0.4045.
- H3: lower end of the oath-resampling 95% interval on winner-pair accuracy above 50%.
- H4: the people's Spearman > 0 and one-sided p < 0.05.

Expected: the copy forecast is strong on headlines (dev 72.7%, held-out 75.7%), but this is a different
behaviour (honesty, not clicks), and the study's own language-model forecasts were at chance. No
prediction is made.

## Secondary checks

Pair accuracy by the strength of the real difference; how often it still picks on the 56 ties; the
call's tiers; position bias; the probe (the winning idea is in the paper's abstract, so a lift from
naming the study is plausible).

## Configuration, code and the gate

- Private configuration: `benchmarks/mimiqbench/configs/megaoath-copy.json`, sha256
  `80ddabaf1d3a33d8167c891681c606a680d8dcb4454e829792b306959ba92118`.
- Code hash `90709a28d8cc771b05dd897ac413beee2e23e090072886c4f43250f432bd8e3f` (51 code units).
- The runner (`benchmarks/mimiqbench/plans.py`, `check`, called by `runner.run` for every held-out
  step) refuses to run unless the GO line names this file's sha256 and the public commit, the
  configuration's sha256 matches, the items and sample hash as above, no sample id appears in any earlier
  cache, and every code unit is unchanged (or a deviation is declared and reported).

## Cost and stopping

About $3.05 (forecast $1.10, people $1.30, panel $0.05, probe $0.60); cap $4.00. If a cap stops the run,
the analysis uses every completed item and reports the shortfall.

## Deviations before the run

- The suite was rebuilt before any run (evidence lane, 2026-09-24): one oath's text had picked up text
  from the source's supplement. The draft plan named the earlier file (`11812c8c...36a1`); this plan
  names the corrected one.
- While computing the forecasters' exact Spearman values for these pass lines, the proof lane's script
  also printed the simple text rules' accuracy on this suite's winner pairs. No model saw any item, and
  no rule is named as a baseline here.

## What we publish whatever happens

Every number above with its interval, including those against Mimiq; the sample and its hashes; every
deviation.
