# MimiqBench headlines: held-out results

Pairs file sha256 `9ae3db65cef2daf8b31b79adf3daf0190165e9cdcfc2916cdb2617880ce2e098`. Pre-registration: PREREGISTRATION.md.

| Method | Pairs | Picked the real winner | 95% interval | Cost per pair |
|---|---|---|---|---|
| Coin flip | 1000 | 50.0% | 46.9% to 53.1% |  |
| Headline written first | 1000 | 61.3% | 58.2% to 64.3% |  |
| Longer headline | 1000 | 55.9% | 52.8% to 58.9% |  |
| Plain question (the smaller model) | 1000 | 53.1% | 50.0% to 56.2% | $0.0003 |
| Old Mimiq crowd (before this work) | 100 | 49.0% | 39.4% to 58.7% | $0.0905 |
| Mimiq's people alone | 300 | 61.0% | 55.4% to 66.3% | $0.1581 |
| Mimiq forecast on the smaller model | 1000 | 72.2% | 69.3% to 74.8% | $0.0018 |
| Mimiq forecast | 1000 | 75.7% | 73.0% to 78.3% | $0.0046 |
| Mimiq's call (forecast + people) | 300 | 76.8% | 71.7% to 81.2% |  |

## How sure: Mimiq's call by tier

| Tier | Share of pairs | Right | 95% interval |
|---|---|---|---|
| clear | 51.0% (153) | 88.2% | 82.2% to 92.4% |
| leaning | 28.3% (85) | 80.0% | 70.3% to 87.1% |
| close | 20.7% (62) | 44.4% | 32.7% to 56.7% |

## Paired tests: Mimiq's call against each method (exact McNemar, same pairs)

| Against | Only the call right | Only the other right | p |
|---|---|---|---|
| Coin flip | 0 | 0 | 1 |
| Headline written first | 93 | 42 | 1.3e-05 |
| Longer headline | 98 | 28 | 2.7e-10 |
| Plain question (the smaller model) | 0 | 0 | 1 |
| Mimiq forecast | 0 | 0 | 1 |
| Mimiq forecast on the smaller model | 16 | 15 | 1 |
| Mimiq's people alone | 62 | 16 | 1.5e-07 |
| Old Mimiq crowd (before this work) | 33 | 9 | 0.00027 |

Supplementary, not pre-registered: McNemar skips half credits, so it cannot compare against a coin or a method credited on the average of two orders. A paired sign-flip permutation test on the credit differences (half credits kept, 200,000 draws):

| Against | Pairs | Call minus other | p |
|---|---|---|---|
| Coin flip | 300 | +26.8 points | 5e-06 |
| Headline written first | 300 | +16.8 points | 3e-05 |
| Longer headline | 300 | +23.7 points | 5e-06 |
| Plain question (the smaller model) | 300 | +23.8 points | 5e-06 |
| Mimiq forecast | 300 | -1.2 points | 0.4 |
| Mimiq forecast on the smaller model | 300 | +3.3 points | 0.17 |
| Mimiq's people alone | 300 | +15.8 points | 5e-06 |
| Old Mimiq crowd (before this work) | 100 | +23.0 points | 0.00046 |

## Memorization check

On 300 pairs, the forecast's model rated winners 38.01 and losers 33.14 out of 100 for "seen it word for word". Picking the more familiar headline was right 57.8% of the time (52.2% to 63.3%). That is above the pre-registered 55% line, so model-based results here, the baselines included, may be inflated by memorization.

Exploratory (not pre-registered): on the 151 probed pairs where the model rated both headlines equally familiar, so familiarity cannot tell them apart, the forecast was right 75.5% of the time (68.1% to 81.7%).
