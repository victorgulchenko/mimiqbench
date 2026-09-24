# MimiqBench headlines: near-ties

Pre-registration: PREREGISTRATION-ties.md. Tie pairs file sha256 `9d6a4fe8ad9636ff55aabebc6282258280bba41f13e68655ca4dda587b261488`; clear-winner pairs file sha256 `9ae3db65cef2daf8b31b79adf3daf0190165e9cdcfc2916cdb2617880ce2e098`.

A near-tie is a held-out Upworthy test where the two headlines' click rates were statistically indistinguishable (both shown at least 1,000 times, p > 0.5). Neither headline really won, so the right answer is "too close to call".

## How often the forecast makes a pick (same answer in both orders)

| Pairs | Tests | Makes a pick | 95% interval |
|---|---|---|---|
| Clear winners (p < 0.01), held-out run | 1000 | 82.4% | 79.9% to 84.6% |
| Near-ties (p > 0.5) | 1000 | 69.8% | 66.9% to 72.6% |

Difference (ties minus clear winners): -12.6 points (95% interval -16.3 to -8.9), two-sided p = 3.9e-11. Ratio 0.85 (0.81 to 0.89). Pre-registered reading: **discriminates somewhat**.

## How sure Mimiq says it is: clear / leaning / close

| Pairs | clear | leaning | close (no pick) |
|---|---|---|---|
| Clear winners, held-out run (300 tests, direct) | 51.0% | 28.3% | 20.7% |
| Near-ties (two-stage: 1000 + 60 tests) | 38.4% (29.6% to 47.3%) | 31.4% (22.7% to 40.3%) | 30.2% (27.4% to 33.0%) |

When the forecast made a pick, the people moved the same way on 55.0% of near-ties (42.5% to 66.9%, 60 tests), against 64.3% on clear winners (238 tests).

A clear call is 1.33 times as likely on a real winner as on a near-tie (bootstrap 95% interval 1.04 to 1.76). Pre-registered line: a calibrated tool calls at most 15% of near-ties clear. Result: **not met**.

Illustration (secondary, descriptive): in the held-out release, one random headline pair per test is a clear winner or a near-tie in the ratio 36.3% to 63.7%. Among those two kinds only, a clear call would come from a real winner 43.1% of the time. (Tests in between, 0.01 < p < 0.5, were not measured.)

## Secondary

- S1. On near-ties the forecast agreed with the headline that happened to get more clicks 52.4% of the time it picked (48.7% to 56.1%, 698 tests); with half credit for no pick, 51.7%. Near 50% is expected: the observed winner of a near-tie is mostly noise.
- S2. Pick rate by how alike the two headlines are (word overlap, thirds of both sets): least similar: clear winners 85.9% (377), near-ties 77.0% (274); middle: clear winners 82.8% (355), near-ties 70.6% (326); most similar: clear winners 76.9% (268), near-ties 64.2% (400).
- S3. The people's average movement (points per 100, pairs with a forecast pick): clear winners 9.49 (moved 1 point or more on 93.7%), near-ties 7.20 (moved on 85.0%).
- S4. How common each kind is: one random eligible headline pair per test in the held-out release (9247 tests) is a clear winner (p < 0.01) 16.7% of the time, in between 54.0%, a near-tie (p > 0.5) 29.3%.

## Run facts

- Cost: $14.04 (ties-forecast $4.53, ties-crowd $9.50).
- Calls served by profile: {'forecast-model': 2000, 'small-model': 3600}; unresolved errors: {'ties-forecast': 0, 'ties-crowd': 0}.
- Pre-registration digests stamped on the calls: 42f3b5cb12c67a09; calls ran 2026-09-23T20:37:06+00:00 to 2026-09-23T21:22:16+00:00 UTC.
- Tier rule cross-check against backend/forecast.py: identical.

## Deviations and notes

See DEVIATIONS-followups.md (written by hand after the runs; this section is not produced by the scoring script).
