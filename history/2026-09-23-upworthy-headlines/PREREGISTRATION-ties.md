# Pre-registration: near-ties (MimiqBench headlines, follow-up 1)

Written 2026-09-23, 20:35 to 20:50 UTC, before any model saw a tie pair. Nothing
below may change after the first tie call, except to add results in
RESULTS-ties.md and to list deviations there.

How this is timestamped, honestly: like commit d4fe7897, only by us. The sha256
of this file was reported to the owner before the runs, and every model call
made for it carries a digest of this file and its UTC time (`prereg`, `ts` in
runs/ties-*/calls.jsonl), but those are self-attested. Future pre-registrations
should be timestamped publicly first (see benchmarks/public-export/README.md).

## Why

The held-out benchmark scores only clear winners (p < 0.01). Real tests are
often near-ties, and that is where people most want help: the useful answer
there is "too close to call". This checks whether Mimiq says so, or whether it
sounds as sure on a near-tie as on a real winner.

## Data

- Near-tie pairs: `data/pairs_ties.jsonl`, built by `build_ties.py` from the
  same confirmatory release as the held-out pairs (Upworthy Research Archive,
  CC BY 4.0), with build_pairs.py's rules except the p-value: same test, same
  image, same excerpt, same lede; each headline shown at least 1,000 times; a
  two-proportion z-test p > 0.5; one pair per test, drawn at random (seed 2027)
  among that test's near-tie pairs; order of the two headlines random; tests
  that began between 2013-06-25 and 2014-01-10 excluded after the draw and the
  shuffle. 7,810 pairs. sha256
  `9d6a4fe8ad9636ff55aabebc6282258280bba41f13e68655ca4dda587b261488`
  (built twice, identical).
- Sample: the first 1,000 pairs in file order (a seeded shuffle).
- Comparator, no new calls: the first 1,000 pairs of `data/pairs_test.jsonl`
  (sha256 `9ae3db65cef2daf8b31b79adf3daf0190165e9cdcfc2916cdb2617880ce2e098`)
  with the forecasts of the pre-registered held-out run (runs/test-forecast),
  and the first 300 with the people (runs/test-crowd).
- What the two sets look like (computed from the data before any model call):

  | | clear winners (first 1,000) | near-ties (first 1,000) |
  |---|---|---|
  | smaller arm, median impressions | 3,225 | 3,086 |
  | observed difference, median (relative) | +125% | +8.1% |
  | observed difference, 10th to 90th percentile | +66% to +273% | +1.6% to +18.9% |

  What p > 0.5 means here: the test found no difference. At about 3,000
  impressions per headline and a 0.9% click rate, a true difference of up to
  roughly 50% either way cannot be excluded for a single near-tie, so these are
  "no detectable difference" tests, not proven equal ones. But every one of
  them is far from the clear winners, whose smallest tenth still won by 66% or
  more.
- Overlap: 109 of the 1,000 near-tie tests also gave a (different) pair to the
  first 1,000 clear-winner pairs; 76 headlines appear in both samples.
- The forecast's pick rate on the clear-winner comparator, from the held-out
  run: 82.4% (824 of 1,000; 95% interval 79.9% to 84.6%). Mimiq's tiers there,
  as published: clear 51.0%, leaning 28.3%, close 20.7% (300 tests).

## Methods (frozen)

- Forecast: identical to the held-out method 6: `backend/forecast.py`
  `forecast_prompt` (FORECAST_VERSION 2) with the Upworthy setting, the audience
  "Americans who read and share feel-good and social-issue stories on
  Facebook", thing "headline", moment "when they scroll", action "clicked";
  the forecast's model through the global inference profile, temperature 0, asked
  in both orders. Before any call, `extra.py verify` recomputes the cache keys
  (which hash the full prompt) for held-out pairs and must find them in the
  held-out caches: at writing, 50 of 50 forecast keys and 240 of 240 crowd keys
  are reproduced, so the prompts are byte-identical to the held-out run. A call
  that still fails after run.py's retries is sent once to the us. profile of
  the same model (recorded per call as `served_by`).
- People: identical to the held-out method 7: `backend/copy_test.py` `_prompt`,
  framing "This post from a stories site, with a photo and this headline,",
  the smaller model (global profile, same failover), temperature 0.9, the first
  30 people of `data/panel_real.json`, each version shown separately to the same
  people; the crowd's shift is mean stop per 100 on B minus on A; at least 10
  valid people per version.
- Tiers: `backend/forecast.py` `call_with_people` (step 1 point per 100): clear
  (the forecast is the same in both orders and the people moved the same way),
  leaning (same in both orders, the people did not agree), close (the forecast
  flipped with the order; the product makes no pick).

## Sample sizes

- Forecast on the 1,000 near-tie pairs (2,000 calls to the forecast's model, about $4.60): the
  pick rate's 95% interval is about plus or minus 2.7 points, so a difference
  from 82.4% of about 4 points or more is detectable.
- People on the first 60 near-tie pairs, in file order, where the forecast made
  a pick (3,600 calls to the smaller model, about $9.50). The budget for all of this work
  ($25 in total) sets this number; it gives the people's agreement rate an
  interval of about plus or minus 12 points.

## Primary outcomes

P1. Pick rate: the share of near-tie pairs where the forecast gives the same
answer in both orders (so the product makes a pick), against the same share on
the clear-winner pairs (82.4%). Reported: both rates with Wilson 95%
intervals, the difference with a Newcombe 95% interval and a two-sided
two-proportion z-test, and the ratio with a log interval. Reading, fixed now:
"discriminates well" if the near-tie pick rate is at most half the clear-winner
rate; "discriminates somewhat" if it is lower with p < 0.05 but more than half;
"does not discriminate" otherwise.

P2. The share of near-ties Mimiq calls clear, leaning and close. Two stages,
because a close call needs no people: close = 1 minus the pick rate (1,000
pairs); clear = pick rate x a; leaning = pick rate x (1 - a), where a is the
share of the 60 people-sample pairs on which the people moved 1 point per 100
or more the way the forecast picked. 95% intervals by bootstrap (20,000
binomial draws of each stage, seed 2027). Compared with the published tiers on
clear winners (51.0 / 28.3 / 20.7). Also reported: how many times more likely a
clear call is on a real winner than on a near-tie (a likelihood ratio, with a
bootstrap interval).

Pass line for calibration, fixed now: a well-calibrated tool calls at most 15%
of near-ties "clear" (point estimate of the two-stage share).

## Hypotheses

- H1t: the forecast makes a pick less often on near-ties than on clear winners
  (P1, reading above).
- H2t: Mimiq calls a smaller share of near-ties clear than of clear winners, and
  at most 15% (P2).

What we expect, written down so it can be checked: the forecast judges wording
and does not know a test's size, so we expect it to pick on most near-ties
(65 to 80% would not surprise us) and the 15% line to fail. If it fails, the
site must not suggest that a clear call means the test will have a real
winner; the 88% accuracy of clear calls applies to tests that had one.

## Secondary (reported, not decisive)

- S1. On near-ties, how often the forecast's pick matches the headline that
  happened to get more clicks (expected near 50%, since that difference is
  mostly noise), and the score with half credit for no pick.
- S2. Pick rate by how alike the two headlines are (share of words in common;
  thirds cut on both sets pooled), near-ties against clear winners.
- S3. The people's movement: mean absolute shift and the share of pairs where
  they moved 1 point or more, near-ties against clear winners (pairs where the
  forecast made a pick).
- S4. How common each kind is in the held-out release: one random eligible pair
  per test (`base_rates.py`, seed 2028), the share with p < 0.01, between, and
  p > 0.5; and, as an illustration only, the share of clear calls that would
  come from real winners in a mix of just those two kinds at that ratio.

## Exclusions and failures

- A pair where either order's forecast fails to parse after retries is left out
  and counted, as in the held-out run.
- A people-sample pair with fewer than 10 valid people on either version is left
  out, not replaced, and counted.
- `extra.py` stops starting new calls past a per-run budget and a hard cap of
  $24 across every ties-* and mem-* run. If a cap stops a run, the analysis uses
  every completed pair and reports the shortfall.

## What we publish whatever happens

Every number above with its interval, including those that go against the
product; the near-tie pairs file; the code; the cost; any deviation.

## Files this pre-registration freezes (sha256 at writing)

| file | sha256 |
|---|---|
| data/pairs_ties.jsonl | 9d6a4fe8ad9636ff55aabebc6282258280bba41f13e68655ca4dda587b261488 |
| data/pairs_test.jsonl | 9ae3db65cef2daf8b31b79adf3daf0190165e9cdcfc2916cdb2617880ce2e098 |
| data/panel_real.json | 66256b73579521e873666609cf24717f489b8021b2d9ea3debdb6fc73802eac8 |
| build_ties.py | 076cae7a9b13df964bcabfbf840a1c4abe56ebf4d4fcefef4a814a9ff21e3093 |
| base_rates.py | a70d83191cc2ba951036a5119720927a5f6776272bc3a94d4ee2cac9d1b846bf |
| extra.py | 813808808e61c92252b568d3c84a69edbc144680cb72ae181313c88002b9793c |
| analyze_ties.py | 36b441a33f3aed97a88f11d87f4111789b9ee61f26a4f0c7cb7b34b61b53816d |
| analyze_memorization.py | f4f8864eebab8f013a9411188a97c29d0916ab5506c4475a1cb17aa1e38089e1 |
| run.py (unchanged since d4fe7897) | b851d5d7dfc6f5c631b607d670a6794c5696abb1817117b31f322188f680be57 |
| build_pairs.py (unchanged since d4fe7897) | de1904e4e4df1835fdfc1943e19bc97d833d0a2c033724b41904dd4d1b18c64e |
| variants.py (unchanged since d4fe7897) | f454f9510f30aace7cf1073c0a2460570dbe71d5c779da0c869b42da6d0b1ac5 |
| ../../backend/forecast.py (forecast_prompt unchanged since d4fe7897) | 968fe6e3220f39fc673679076c104fec7dad23a7c872f51e06be555f5165a134 |
| ../../backend/copy_test.py (unchanged since d4fe7897) | 7c5d418e71b60ee7c6551a7ab2e588f479de32725e8dbcd19bff21b80e70a556 |
| ../../backend/simulation_engine/web_runner.py (unchanged since d4fe7897) | 1dc2d6c19ad1ea4af16a246c3ac64d1b199c415782be0703277db42d97f1da55 |

Every run start also writes these hashes to runs/<tag>/manifest.jsonl.

Unchanged means the file's git blob in the working tree equals the one at
commit d4fe7897 (checked with `git hash-object` at writing). backend/forecast.py
changed after d4fe7897 only in `call_with_people`'s handling of close calls
(commit cb69329f), which does not affect tiers.
