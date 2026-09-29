# Plan: Upworthy headlines, a cheaper candidate model for the forecast (H4)

Pushed: 2026-09-29 (the commit that adds this file to the public register is the timestamp).
Nothing below changes after the first held-out call; results and deviations go in
`results/2026-09-29-headlines-candidate-forecast.md`.

## Question

Can a cheaper candidate model take over Mimiq's forecast without losing accuracy on the
headlines benchmark (H1)? Four hypotheses, all on the pairs H1 used:

- **H4.1, non-inferiority.** On the same 1,000 held-out pairs, the candidate's accuracy is at
  most 3 points below the production forecast model's.
- **H4.2, better than a rule.** The candidate beats the best simple rule on these pairs (the
  headline written first, 61.3%).
- **H4.3, recall (as H3 M1).** The candidate does not win by remembering: on the pairs where it
  can finish neither headline, its accuracy is at most 3 points below its own overall accuracy.
- **H4.4, rewording (as H3 M2).** On reworded versions of the first 500 pairs, its accuracy
  drops by at most 5 points from the same pairs in their original words.

The candidate replaces the production forecast only if all four pass.

## Data

- Source: the Upworthy Research Archive (Matias, Munger, Aubin Le Quere and Ebersole,
  *Scientific Data*, 2021; CC BY 4.0), confirmatory release, as in H1. Success is the headline
  more visitors clicked; clear winners only (p < 0.01).
- Held-out items: `data/pairs_test.jsonl`, the first 1,000 pairs, sha256
  `9ae3db65cef2daf8b31b79adf3daf0190165e9cdcfc2916cdb2617880ce2e098` (H1's file and sample).
  H1 to H3 already used these pairs with the production model, whose answers are cached. The
  candidate model has never been sent any of them.
- Rewordings: H3's own rewordings of both headlines of the first 500 pairs (cached,
  `runs/mem-paraphrase/calls.jsonl`, sha256
  `5d59c44c82dc210ca4b1e81dc5c3a63f544bb91d9c42a707f378d5bb14ee6c9a`). No new rewording is made.
- Exclusions: none. An order with no answer after six attempts counts as no pick, so the pair
  gets half credit, as in H1.

## Method (frozen)

- Code, sha256 of every file that makes or scores a call:
  - `run.py` `c1ebe1c02e468e81146a83a5edc67acec4df709ad1f32e8913ae2cc29a950a59`
  - `candidate.py` (runs and scores this plan) `716e82fb258c65c4b4174b18f438cf975898f2861fbc74d162393223b0ebfc08`
  - `extra.py` (H3's recall probe) `813808808e61c92252b568d3c84a69edbc144680cb72ae181313c88002b9793c`
  - `analyze_memorization.py` (H3's completion scoring) `f4f8864eebab8f013a9411188a97c29d0916ab5506c4475a1cb17aa1e38089e1`
  - `backend/forecast.py` (the production prompt) `968fe6e3220f39fc673679076c104fec7dad23a7c872f51e06be555f5165a134`
  - `backend/simulation_engine/direct_llm.py` (the candidate's transport) `002b166c39be9b1d0f6df29fd994e96e920fd64d847ae3afe4e606cf6e2c60bc`
- Models by role, both named in the private configuration file `configs/h4-models.json`,
  sha256 `7416193ae90578de690a9412a7294d8b1031b1735feaff31e20c13052edc8a2e`:
  - the production forecast model: H1's, with its cached held-out answers
    (`runs/test-forecast/calls.jsonl`, sha256
    `d66a72bde6fb01b81c1348a38b7891b18e9c9908b1736b057fff57a79094bfb2`). No new call is made
    to it.
  - the candidate forecast model, reached through its maker's API by way of a router.
- The candidate is asked exactly what the production model was asked: the production forecast
  prompt (`backend/forecast.py`, FORECAST_VERSION 2) with H1's setting and audience line, both
  orders, one call each. Temperature 0 is requested (the model's default if the provider
  refuses it); at most 400 answer tokens plus 1,500 for thinking; the provider's default
  reasoning effort, as the product runs it today.
- The candidate sees the two headlines, the setting and the audience line. It never sees
  impressions, clicks, click rates or which headline won.
- Recall probe: H3's prompt (`COMPLETE_PROMPT`) on every headline of the 1,000 pairs that has
  at least five words, at most 60 tokens, temperature 0, scored as in H3 (completable: the
  model's continuation covers at least 75% of the missing words).
- Every held-out call carries this file's sha256 and its UTC time.

## Primary metric

Accuracy as in H1: the pick when both orders agree, half credit otherwise, with a 95% Wilson
interval. The paired difference, candidate minus production, on the same 1,000 pairs, with a
95% interval from a paired bootstrap (10,000 resamples, seed 2029) and a paired sign-flip test
(200,000 flips, seed 2029). `python candidate.py score` computes every number below.

## Baselines

A coin (50%), the headline written first (61.3%), the production forecast model (75.7%, H1).

On the development split only (exploratory; positions 300 to 599 of `data/pairs_dev.jsonl`,
never held out), run on 2026-09-29 to check that the candidate answers in the expected format
and to price it: candidate 66.7% (61.2% to 71.8%), production 72.8% (67.5% to 77.6%); 44 pairs
only the candidate got right, 73 only the production model. Development samples carry several
points of uncertainty, and nothing in this plan was changed after seeing them.

## Pass lines

- H4.1 passes if the lower end of the paired 95% interval is above -3.0 points.
- H4.2 passes if the lower end of the candidate's 95% Wilson interval is above 61.3%.
- H4.3 passes if the accuracy on pairs neither of whose headlines the candidate can complete is
  at least its overall accuracy minus 3 points.
- H4.4 passes if the drop from the original to the reworded 500 pairs is at most 5 points. If it
  fails, the reworded accuracy is the conservative figure, as in H3.

## Secondary checks

Pick rate (both orders agree), position bias (share of answers naming the headline shown first),
errors, completion rates (word for word and completable), cost per pair.

## Cost and stopping

About 4,000 calls, expected under $1, hard cap $5 (the owner's approval, 2026-09-29). If the cap
stops the run, the unanswered pairs count as no pick and the stop is listed as a deviation.
