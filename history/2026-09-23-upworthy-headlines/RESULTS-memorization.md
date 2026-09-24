# MimiqBench headlines: memorization checks

Pre-registration: PREREGISTRATION-memorization.md. Held-out pairs: the first 1,000 of `data/pairs_test.jsonl` (the pairs the forecast was scored on); the paraphrase check uses the first 500.

## M1. Can the model finish the headline from memory?

Each headline was cut in half; the model got the first half, was told it is a real Upworthy headline from the public archive, and was asked to finish it word for word. "Completable" means its continuation matched at least 75% of the missing words in order.

| Model | Headlines | Finished word for word | Completable | Completable, fresh paraphrases (chance level) |
|---|---|---|---|---|
| The forecast's model | 1999 | 0.4% | 1.0% | 0.1% (999) |
| The people's model (the smaller model) | 1999 | 0.1% | 0.1% | 0.0% (999) |

| Model | Forecast accuracy, neither headline completable | 95% interval | One or both completable | Pre-registered line | Result |
|---|---|---|---|---|---|
| The forecast's model | 75.6% (980 pairs) | 72.8% to 78.1% | 81.6% (19 pairs) | 72.7% | pass |
| The people's model (the smaller model) | 72.2% (998 pairs) | 69.3% to 74.9% | 100.0% (1 pairs) | 69.2% | pass |

The forecast's model: only the winner completable in 7 pairs, only the loser in 12 (sign test p = 0.36); both 0, neither 980.

The people's model (the smaller model): only the winner completable in 0 pairs, only the loser in 1 (sign test p = 1); both 0, neither 998.

Secondary (first 300 pairs, neither headline completable by either model: 293 pairs): the people alone 60.1% (all 300: 61.0%); Mimiq's call as pre-registered 76.3% (all: 76.8%).

## M2. Does the forecast still work when the headlines are reworded?

Each headline was reworded on its own by the smaller model (same meaning, hook, tone and length, no run of three words kept), without seeing the other headline or the result. The production forecast (the forecast's model, both orders) then judged the reworded pair.

| Pairs | Original wording | Reworded | Drop | 95% interval of the drop | Pre-registered line | Result |
|---|---|---|---|---|---|---|
| 499 | 76.7% | 68.0% | +8.6 points | +5.2 to +12.0 | at most 5.0 points | fail |

Paired sign-flip permutation p = 0. Makes a pick: 81.8% original, 78.6% reworded; when both made a pick, the same pick 87.5% of the time (329 pairs).

Rewording checks: 74.1% of 1000 rewordings share no run of three words with the original; median length ratio 0.92 (middle half 0.80 to 1.00); 1 pairs whose two rewordings came out identical. On the 279 pairs where both rewordings share no three-word run: original 77.4%, reworded 68.5%.

## Verdict (rule fixed in advance)

**M2 failed: rewording lowers accuracy; memorization cannot be ruled out; report the paraphrased accuracy next to the original**.

## Exploratory (not pre-registered)

The original familiarity ratings (the forecast's model, 0 to 100): headlines the forecast's model could complete averaged 32.1 (7), the rest 35.6 (593). "Pick the more familiar headline" on pairs neither model could complete: 57.8% (293 pairs).

## Run facts

- Cost: $5.36 (mem-complete $2.76, mem-paraphrase $2.60).
- Calls served by profile: {'forecast-model': 3997, 'small-model': 3998}; unresolved errors: {'mem-complete': 0, 'mem-paraphrase': 1}.
- Pre-registration digests stamped on the calls: 42f3b5cb12c67a09; calls ran 2026-09-23T20:37:03+00:00 to 2026-09-23T21:05:31+00:00 UTC.

## Deviations and notes

See DEVIATIONS-followups.md (written by hand after the runs; this section is not produced by the scoring script).
