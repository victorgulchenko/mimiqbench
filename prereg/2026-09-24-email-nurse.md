# Plan: email-megastudies (nurse), which recruiter message gets more nurses to engage

Final, 2026-09-24. Written by the proof lane from dev results only; no model has seen any item of this
sample. The commit that adds this file to the public register is its timestamp. Nothing below changes
after that; results and deviations go in RESULTS next to it.

Mimiq keeps its choice of AI models confidential, so this plan names models by role only (the
forecast's model, the people's model, the recruiting model). Their exact identities and settings are
fixed by a private configuration file whose sha256 is below; the run refuses to start if that file
differs by one byte.

## Why this one first

It is the cleanest test of memorization we have: the study's results were first public on 29 June
2026, after the training data of every model Mimiq can use was collected. A pass here cannot come
from memory. It also has an expert panel that did no better than chance.

## Question and hypotheses

Can Mimiq order ten real LinkedIn recruiter messages by how many European nurses engaged with them,
better than the study's expert panel?

- H1 (primary): Mimiq's forecast ranks the ten messages in the real order: Spearman above 0, one-sided
  p below 0.05.
- H2: it ranks them better than the expert panel: Spearman above 0.0244 (the panel's pooled forecasts
  against the real rates; the suite card rounds it to 0.02).
- H3: on the 11 pairs with a significant winner it is right more often than the experts (59.1%, the
  suite card's figure, a tie in the experts' forecasts counted half).
- H4: Mimiq's simulated people alone rank the messages positively: Spearman above 0, one-sided p below
  0.05.

## Data

- Source: "What works in international health worker recruitment: a megastudy", OSF preprint v2,
  doi 10.31219/osf.io/6pwxe_v2 (29 June 2026), CC BY 4.0. 110,000 nurses in 28 European countries,
  one LinkedIn message each (or none), 27 January to 14 April 2025. Outcome: engaged within four weeks
  (accepted, declined, replied or clicked), 20.5% to 22.5% by message.
- Suite `email-megastudies`, study `nurse`, all 46 of its items: 1 ranking over 10 messages and 45 pairs
  (4 clear, 7 likely, 19 unclear, 15 ties); held-out by study, fixed when the study was added.
- items.jsonl sha256 `fabaa9d75bf1e2176fabe8e599394a408287c95cb4a29a8b35e8be98974b738f`. The sample is
  held-out positions 23 to 68 of the suite's split; sample ids sha256
  `13f6eeefc0af0c75a651dd48f81cb54e2fae80146b30736c98a72312a9ebb37c`.
- Exclusions, fixed now: a pair whose forecast cannot be parsed in either order, after production's
  retries, is left out of pair accuracy and counted, and counts 0.5 in the ranking. Nothing else is
  excluded.

## Method

1. After the GO, recruit 25 simulated people for the items' audience the way the app does (the audience
   endpoint's steps, seed 20260924, the recruiting model). The panel is built only then, so no held-out
   text reaches a model earlier; its sha256 goes in the results.
2. Mimiq's forecast on the 45 pairs, exactly as the app's compare call makes it (`forecast_pair`, kind
   `email`, the item's audience, both orders; a pick when both orders agree), the forecast's model.
3. The ranking: each message's Copeland score over those 45 forecasts (1 for a pick in both orders, 0.5
   each when the orders disagree). No new call.
4. Mimiq's people on each of the 10 messages (the app's email test, `copy_test.run_copy_batch`, the 25
   people, the people's model). A message's score is the people's mean stated "open and read" per 100,
   the number the app's comparison moves on. The people's pair picks and Mimiq's call on the 45 pairs
   are then computed from these same answers, with no new call.
5. The memory probe on the 11 winner pairs: the forecast's model is asked which message won, with and
   without the study named, both orders, and whether it remembers the result. Expected to show no memory
   (a control for the probe).

The model sees the message texts and the audience line only: never the outcome, the dates, the study,
or the messages' labels (except the study's name in the probe).

## Primary metric

Spearman correlation between the ten Copeland scores and the real engagement rates; one-sided p from
100,000 random permutations of the messages (seed 7); 95% interval by resampling messages (3,000 draws,
seed 11). Code: `benchmarks/mimiqbench/confirm.py` and `score.py`.

## Baselines

The expert panel (about 218 academics, HR practitioners and nurses): Spearman 0.0244 (card: 0.02),
59.1% of the 11 winner pairs. A coin: Spearman 0 and 50%. The rule of thumb named now, from the dev
emails: "the longer message" (66.7% on the dev email-open pairs).

## Pass lines (set now)

- H1 passes if Spearman > 0 and one-sided p < 0.05.
- H2 passes if Spearman > 0.0244.
- H3 passes if accuracy on the 11 winner pairs is above 59.1% (point estimate; its interval is reported
  and will be wide).
- H4 passes if the people's Spearman > 0 and one-sided p < 0.05.

Expected from dev: email opens (a teacher-email study, dev) went well (forecast ranking 0.78); flu
vaccination texts (dev) did not. Engaging with a job message is closer to opening than to getting a
shot, but these messages differ by two points at most. No prediction is made.

## Secondary checks (reported, no pass lines)

Pair accuracy by the strength of the real difference; how often it still picks on the 15 ties; the
call's tiers; position bias; the probe's result.

## Configuration, code and the gate

- Private configuration: `benchmarks/mimiqbench/configs/email-nurse.json`, sha256
  `8d1a8d5c206f9c4718afebaf270d247d79ffd95c68130ae87ac16311df654c8a`. It fixes the model for each role
  and its settings, the sample, the steps and budgets, and the pass lines in machine form.
- Code hash `90709a28d8cc771b05dd897ac413beee2e23e090072886c4f43250f432bd8e3f`: the sha256 over the
  sha256 of the 51 code units the run executes (the harness files and each production function it
  calls, listed in the configuration).
- The runner (`benchmarks/mimiqbench/plans.py`, `check`, called by `runner.run` for every held-out
  step) refuses to run unless the GO line names this file's sha256 and the public commit, the
  configuration's sha256 matches the one above, the items and sample hash as above, no sample id
  appears in any earlier cache, and every code unit still has its recorded hash. A changed unit stops
  the run unless a deviation is declared, which is then reported with the results.

## Cost and stopping

About $1.15 (forecast $0.25, people $0.75, panel $0.05, probe $0.10); cap $2.00. If a cap stops the
run, the analysis uses every completed item and reports the shortfall; nothing is re-run to change a
result.

## Deviations before the run

- While computing the forecasters' exact Spearman values for these pass lines (2026-09-24), the proof
  lane's script also printed the simple text rules' accuracy on this sample's 11 winner pairs. No
  model saw any item. The rule baseline named above was chosen on dev before that and is unchanged.

## What we publish whatever happens

Every number above with its interval, including those against Mimiq; the sample and its hashes; every
deviation.
