# Plan: flu-sms (Walmart), which pharmacy text gets more people a flu shot

Final, 2026-09-24. Written by the proof lane from dev results (the Penn/Geisinger study); no model has
seen any item of this sample. The commit that adds this file to the public register is its timestamp.
Nothing below changes after that; results and deviations go in RESULTS next to it.

The suite's message texts may not be redistributed (CC BY-NC-ND article, unlicensed OSF files), so this
plan names the items by sha256 only. Mimiq keeps its choice of AI models confidential, so models appear
by role only (the forecast's model, the people's model, the recruiting model); their exact identities
and settings are fixed by a private configuration file whose sha256 is below.

## Question and hypotheses

Can Mimiq tell which of 22 real text messages got more Walmart pharmacy customers vaccinated, and does
it do better than the 24 behavioural scientists and 406 lay people who forecast the same messages
before the results were known?

- H1 (primary): Mimiq's forecast ranks the 22 texts in the real order (31 December outcome): Spearman
  above 0, one-sided p below 0.05.
- H2: against the 31 October outcome, the window the forecasters predicted, it ranks at least as well as
  the lay people: Spearman at least 0.5981.
- H3: against the 31 October outcome it ranks better than the scientists: Spearman above -0.1322.
- H4: on pairs with a significant winner, it picks the winner more often than not: the lower end of the
  95% interval that resamples texts is above 50%.
- H5: Mimiq's simulated people alone rank the texts positively (31 December): Spearman above 0, one-sided
  p below 0.05.

## Data

- Source: Milkman et al. (2022), "A 680,000-person megastudy of nudges to encourage vaccination in
  pharmacies", *PNAS* 119(6):e2115126119; per-arm counts from the authors' OSF files; message texts from
  the supplement. 689,693 customers, 22 text arms and a no-text control, from 25 September 2020.
  Outcome: a flu shot at a Walmart pharmacy by 31 December 2020 (primary); by 31 October 2020 (the
  forecasters' window).
- Suite `flu-sms`, held-out = the Walmart study, all 232 items (split by study before any model call):
  1 ranking over 22 texts and 231 pairs (94 with p < 0.05: 62 clear, 32 likely; 61 ties; 76 unclear).
- items.jsonl sha256 `2e5d02a1528fabf8eb97361e84782d60cc577f97956aefc5ab42cebc10529674`. The sample is
  held-out positions 1 to 232; sample ids sha256
  `49d62252ac20210c5fe708f0da4ab41624362cd175dca62adfab000d4f3a6528`.
- Exclusions, fixed now: a pair whose forecast cannot be parsed in either order, after production's
  retries, is left out of pair accuracy and counted, and counts 0.5 in the ranking.

## Method

1. After the GO, recruit 25 simulated people for the items' audience the way the app does (seed
   20260924, the recruiting model); its sha256 goes in the results.
2. Mimiq's forecast on the 231 pairs, exactly as the app's compare call makes it (kind `email`, the
   item's audience, both orders), the forecast's model.
3. The ranking: each text's Copeland score over those 231 forecasts. No new call.
4. Mimiq's people on each of the 22 texts (the app's email test, `copy_test.run_copy_batch`, the 25
   people, the people's model); a text's score is the people's mean stated "open and read" per 100. The
   people's pair picks and Mimiq's call on the pairs come from these same answers.
5. The memory probe on the first 30 winner pairs in split order (the forecast's model, with and without
   the study named, both orders).

The model sees the texts (with the suite's stand-ins for names and dates) and the audience line only.

## Primary metric

Spearman between the 22 Copeland scores and the real 31 December effects; one-sided p from 100,000
random permutations (seed 7); 95% interval by resampling texts (3,000 draws, seed 11). H2 and H3 use the
31 October effects. H4 uses the interval that resamples texts (2,000 draws, seed 11). Code:
`benchmarks/mimiqbench/confirm.py`, `score.py`, `stats.py`.

## Baselines (the source's own forecasts and a rule)

| | Spearman, 31 Oct | Right on the 94 winner pairs |
|---|---|---|
| Lay people (406, mean forecast) | 0.5981 | 89.4% (card) |
| Scientists (24, mean forecast) | -0.1322 | 44.7% (card) |
| A coin | 0 | 50% |

The rule of thumb named now, from dev: "the arm with more messages" (87.5% on 12 dev winner pairs).

## Pass lines (set now)

- H1: Spearman (31 Dec) > 0 and one-sided p < 0.05.
- H2: Spearman (31 Oct) at least 0.5981.
- H3: Spearman (31 Oct) above -0.1322.
- H4: lower end of the text-resampling 95% interval on winner-pair accuracy above 50%.
- H5: the people's Spearman (31 Dec) > 0 and one-sided p < 0.05.

Expected from dev (19 Penn texts): forecast Spearman -0.09, 45.8% on 12 winner pairs; the people
Spearman -0.32 and 0 of 12 winner pairs (they punish length and a second text, which real patients
rewarded). H1, H2, H4 and H5 are expected to fail. The top arms were widely quoted from 2021 on, so
memorization is possible for them; the probe checks.

## Secondary checks

Pair accuracy by the strength of the real difference; how often it still picks on the 61 ties; the
call's tiers; position bias; the probe (with and without the study named, and any claim of remembering).

## Configuration, code and the gate

- Private configuration: `benchmarks/mimiqbench/configs/flu-sms-walmart.json`, sha256
  `95235142348c2f54dc8765a83e6564d06077773aced78daa9c6d985ace40e82a`.
- Code hash `90709a28d8cc771b05dd897ac413beee2e23e090072886c4f43250f432bd8e3f` (51 code units).
- The runner (`benchmarks/mimiqbench/plans.py`, `check`, called by `runner.run` for every held-out
  step) refuses to run unless the GO line names this file's sha256 and the public commit, the
  configuration's sha256 matches, the items and sample hash as above, no sample id appears in any earlier
  cache, and every code unit is unchanged (or a deviation is declared and reported).

## Cost and stopping

About $4.75 (forecast $2.00, people $1.80, panel $0.05, probe $0.90); cap $6.00. If a cap stops the run,
the analysis uses every completed item and reports the shortfall.

## Deviations before the run

- While computing the forecasters' exact Spearman values for these pass lines, the proof lane's script
  also printed the simple text rules' accuracy on this sample's winner pairs. No model saw any item. The
  rule named above was chosen on dev before that and is unchanged.

## What we publish whatever happens

Every number above with its interval and the verdict on each hypothesis. Not the texts (license).
