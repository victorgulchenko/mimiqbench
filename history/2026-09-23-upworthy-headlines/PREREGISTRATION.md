# Pre-registration: MimiqBench headlines, held-out run

Written 2026-09-23, before any method saw a held-out pair. Committed to git
before the held-out run; the commit hash is the timestamp. Nothing below may
change after the held-out run starts, except to add results in RESULTS.md.

## Data

- Held-out pairs: `data/pairs_test.jsonl`, built by `build_pairs.py` from the
  Upworthy Research Archive confirmatory release (CC BY 4.0). 4,578 pairs, one
  per experiment: same story, same image, same excerpt, same lede; each
  headline shown at least 1,000 times; a two-proportion z-test p < 0.01; tests
  that began between 2013-06-25 and 2014-01-10 excluded (the archive authors'
  randomization-problem window). The winner is version `a` in 49.2% of pairs.
- The file's sha256 at pre-registration: 9ae3db65cef2daf8b31b79adf3daf0190165e9cdcfc2916cdb2617880ce2e098 (RESULTS.md repeats it).
- Sample: the first N pairs of the file, in file order (the order is a seeded
  shuffle). N = 1,000 for methods that make one or two calls per pair;
  the first 300 of those for crowd methods (one call per person per version).
- Nothing was tuned on these pairs. All method choices were made on
  `data/pairs_dev.jsonl` (exploratory release, 941 pairs).

## Primary outcome

Accuracy: the share of pairs where the method's pick is the headline with the
higher real click-through rate. A method that declines to pick gets half
credit (a coin). 95% Wilson intervals. Paired comparisons between methods on
the same pairs with an exact McNemar test.

## Methods (all frozen at the pre-registration commit)

Models run through global inference endpoints (the same models the product calls, about 9% cheaper).

Baselines
1. Coin: 50% by construction (the pair order is random).
2. Written first: the headline Upworthy created first (their `created_at`).
3. Longer: the longer headline.
4. Plain question: the smaller model, `run.py` `forecast_prompt` ("which headline got the higher click-through rate? Reply with exactly one letter"), temperature 0, both orders, credit averaged over the orders (`--method forecast --model small-model`).
5. Old Mimiq crowd: the production copy prompt as it was before this work, kept verbatim as `variants.prompt_legacy` (verified byte-identical to what the old product sent), the smaller model, temperature 0.9, the first 20 people of `data/panel_real.json`, each version shown separately to the same people; pick = higher mean (stop + click) per 100, as the old compare decided. First 100 pairs only (`--variant legacy`).

Mimiq
6. Forecast: `backend/forecast.py` (FORECAST_VERSION 2) `forecast_prompt` with the setting "A stories site tested two headlines for the same article on its own website in 2014. Each visitor was randomly shown one of them, with the same photo and teaser, and the site counted clicks.", the audience "Americans who read and share feel-good and social-issue stories on Facebook", thing "headline", moment "when they scroll", action "clicked"; the forecast's model, temperature 0, both orders. Pick when both orders agree; otherwise no pick (half credit) (`--method prodforecast --model forecast-model`).
7. Crowd: `backend/copy_test.py` `_prompt` at this commit, framing "This post from a stories site, with a photo and this headline,", the smaller model, temperature 0.9, the first 30 people of `data/panel_real.json`, each version shown separately to the same people; crowd pick = higher mean stop per 100 (`--variant prod`).
8. Mimiq's call: `forecast.call_with_people` on 6 and 7 (step 1 point per 100): the forecast's pick when both orders agree, otherwise the crowd's; tiers `clear` (forecast consistent and the crowd moved the same way), `leaning` (forecast consistent, crowd did not agree), `close` (forecast flipped with the order).

Also reported, not primary: the production forecast on the smaller model (cost), accuracy by tier, and accuracy by the size of the real difference.

## What dev showed (so readers can see what we expected)

On the exploratory split: plain question 49 to 51%; old crowd 51 to 53%; new crowd 64 to 66%; forecast 73 to 75% (the forecast's model), 70 to 73% (the smaller model); Mimiq's call 70%, with `clear` calls (about half) right 77 to 83% of the time, `leaning` 61 to 65%, `close` 56 to 61%. Dev samples were 50 to 300 pairs, so each of these carries several points of uncertainty.

## Hypotheses, stated before the run

- H1: Mimiq's call (8) beats the coin, the heuristics (2, 3) and the plain question (4).
- H2: Mimiq's call (8) beats the old crowd (5) on the pairs both ran.
- H3: `clear` calls are right more often than `leaning`, and `leaning` more often than `close`.

## Memorization check

Upworthy published winning headlines, so a model trained on the web may have
seen winners more often than losers. Before scoring, the forecast's model rates how familiar
each headline in 300 held-out pairs is (0 to 100, "have you seen this exact
headline before?"). Reported: mean familiarity of winners vs losers, and the
accuracy of "pick the more familiar headline". If that rule beats 55%, the
write-up says model-based results may be inflated by memorization, for every
model-based method including the baselines.

## What we publish whatever happens

All accuracies with intervals, including the ones that go against us; the
exclusions; the memorization check; the cost per pair; the code and the pair
files. If H1 fails, the site stops claiming Mimiq picks winners.
