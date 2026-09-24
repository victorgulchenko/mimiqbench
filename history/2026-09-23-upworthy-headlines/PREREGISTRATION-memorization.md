# Pre-registration: memorization checks (MimiqBench headlines, follow-up 2)

Written 2026-09-23, 20:35 to 20:55 UTC, before any completion probe, rewording
or forecast on reworded headlines was run. Nothing below may change after the
first call, except to add results in RESULTS-memorization.md and to list
deviations there. Timestamping: as PREREGISTRATION-ties.md (self-attested
sha256, reported to the owner before the runs; every call carries a digest of
this file and its UTC time).

## Why

Upworthy published its winning headlines, and the whole archive, winners,
losers and clicks, has been public since 2020 and 2021. A model trained on the
web may have seen these headlines, and even the results. The held-out run's
check asked the model how familiar each headline looked: winners looked more
familiar, and "pick the more familiar one" was right 57.8% of the time, above
the pre-registered 55% line. The analysis suggesting the forecast survives that
(75.5% on pairs rated equally familiar) was exploratory, added after the run.
A familiarity rating is also a weak test, since winners may simply look more
like typical Upworthy headlines. The two checks below test memory directly.
Both were fixed before running, with pass lines.

## Data

The first 1,000 pairs of `data/pairs_test.jsonl` (sha256
`9ae3db65cef2daf8b31b79adf3daf0190165e9cdcfc2916cdb2617880ce2e098`), exactly
the pairs on which the forecast scored 75.7% (the forecast's model) and 72.2% (the smaller model
4.5). M2 uses the first 500 of them. The forecast's answers on the original
headlines come from the pre-registered held-out run (runs/test-forecast); no
new call is made on the original headlines except the completion probe.

## M1. Completion: can the model finish these exact headlines?

- Every headline of at least 5 words, both versions of each pair (1,999 of
  2,000; one headline is shorter), is split on spaces. The model sees the first
  max(2, floor(n/2)) words and must write the rest. A pair with a headline too
  short to probe is left out of the "neither completable" subset (the
  conservative choice) and counted.
- The prompt (`COMPLETE_PROMPT` in `extra.py`) says the headline is real, from
  Upworthy in 2013 to 2015, and in the public Upworthy Research Archive, and
  asks for the rest word for word, with a best guess if unsure. Naming the
  source makes recall easier (the "guided instruction" of Golchin and Surdeanu,
  2023), so the probe leans toward finding memorization.
- Models: the forecast's model (primary), and the smaller model, which plays the people and runs the cheaper forecast (secondary). Temperature 0,
  at most 60 tokens, global inference profiles with failover to us.
- Scoring (`analyze_memorization.py`): text lowercased, curly quotes
  straightened, apostrophes dropped, everything but letters and digits a space;
  the model's first line, minus the beginning if it repeated it. Word for word:
  its first k words equal the k missing words. Completable: the longest common
  subsequence of the k missing words and the model's first k words covers at
  least 75% of the missing words.
- Chance level: the same probe, same prompt, on the fresh rewordings from M2
  (1,000 headlines no model can have seen). Their completion rate is what
  guessing from style alone achieves.

Decision (primary): the forecast's accuracy, scored as in RESULTS.md
(the pick when both orders agree, half credit otherwise), on the pairs where
neither headline is completable by the forecast's model. PASS if at least 72.7% (the
published 75.7% minus 3 points). Secondary: the forecast on the smaller model on pairs where
neither headline is completable by the smaller model, line 69.2% (72.2% minus 3).

Also reported: completion rates, word for word and completable, on real
headlines and on the chance-level rewordings; winners against losers (pairs
where only the winner is completable against pairs where only the loser is,
exact sign test), which shows whether the model saw winners more; accuracy on
pairs with at least one completable headline; and, on the first 300 pairs, the
people alone and Mimiq's call (as pre-registered for the held-out run) on the
pairs neither model can complete.

## M2. Rewording: does the forecast read the headlines or recognize them?

- Both headlines of each of the first 500 pairs are reworded one at a time by
  the smaller model (temperature 0, `PARAPHRASE_PROMPT` in `extra.py`): the same
  meaning, facts, names and numbers; the same kind and strength of hook; the
  same tone, intensity, point of view and tense; about the same length; no run
  of three or more words kept except names and numbers. The rewording model sees
  one headline at a time, never the other one, never the result. Cleaning: the
  first non-empty line, minus a leading label and surrounding quotes
  (`clean_paraphrase`).
- The production forecast, with the same prompt, model and settings as the
  held-out run (the forecast's model, temperature 0, both orders), judges the reworded
  pair. The truth is the original pair's winner.

Decision (primary): PASS if the reworded accuracy is at most 5.0 points below
the original-wording accuracy on the same pairs (point estimates, both scored
as in RESULTS.md). Reported with a paired bootstrap 95% interval of the drop
(20,000 resamples, seed 2029) and a paired sign-flip permutation p.

Why this is fair, and where it is not: both headlines in a pair are about the
same story, with the same photo and teaser, so knowing the story cannot tell
the winner; only the wording can. Rewording removes the exact strings a
remembered answer would key on and keeps what a reader reacts to. The limit is
that rewording can also blunt what made a headline work, so a drop is
ambiguous (memory, or a weaker rewording), while holding up is strong evidence
that the forecast reads the headlines. Checks on the rewording, reported: the
share of rewordings that keep no run of three words, the length ratio, pairs
whose two rewordings came out identical; and, secondary, M2 on the pairs where
both rewordings keep no run of three words.

## Verdict rule, fixed now

- M1 (the forecast's model) and M2 both pass: the site may say that checks fixed in advance
  found no sign that the forecast's accuracy comes from remembering the
  headlines, and give the numbers.
- M1 fails: the site's headline accuracy becomes the accuracy on pairs where
  the forecast's model can complete neither headline, and says why.
- M2 fails and M1 passes: the site gives the reworded accuracy next to 75.7%
  and says memorization cannot be ruled out.

Whatever happens, RESULTS-memorization.md reports every number above with its
interval.

## Budget

About 3,000 short calls to the forecast's model and 3,000 short calls to the smaller model for the completion
probes (about $2.40), 1,000 calls to the smaller model for the rewordings (about $0.40), and
1,000 calls to the forecast's model for the forecast on reworded pairs (about $2.30), inside the
$24 cap shared with the near-tie runs.

## Exploratory, flagged as such when reported

The held-out familiarity ratings against completion (do "familiar" headlines
turn out to be completable?), and the "more familiar" rule on pairs neither
model can complete.

## Files this pre-registration freezes (sha256 at writing)

The same table as PREREGISTRATION-ties.md; the ones this check depends on:

| file | sha256 |
|---|---|
| data/pairs_test.jsonl | 9ae3db65cef2daf8b31b79adf3daf0190165e9cdcfc2916cdb2617880ce2e098 |
| extra.py (COMPLETE_PROMPT, PARAPHRASE_PROMPT, clean_paraphrase, split_headline) | 813808808e61c92252b568d3c84a69edbc144680cb72ae181313c88002b9793c |
| analyze_memorization.py (scoring and decision rules) | f4f8864eebab8f013a9411188a97c29d0916ab5506c4475a1cb17aa1e38089e1 |
| analyze_ties.py (shared helpers) | 36b441a33f3aed97a88f11d87f4111789b9ee61f26a4f0c7cb7b34b61b53816d |
| run.py (unchanged since d4fe7897) | b851d5d7dfc6f5c631b607d670a6794c5696abb1817117b31f322188f680be57 |
| ../../backend/forecast.py (forecast_prompt unchanged since d4fe7897) | 968fe6e3220f39fc673679076c104fec7dad23a7c872f51e06be555f5165a134 |

Every run start also writes these hashes to runs/<tag>/manifest.jsonl.
