# Deviations and notes: follow-up runs (near-ties, memorization)

Everything that happened after PREREGISTRATION-ties.md and PREREGISTRATION-memorization.md
were frozen (sha256 recorded in PREREGISTRATION-followups.sha256 at 20:36:40 UTC, 2026-09-23)
that a reader should know. None of it changed a pre-registered rule, sample or pass line.

## Corrections to the pre-registration texts

1. Both files say their sha256 "was reported to the owner before the runs". It was not: the
   hashes were written to PREREGISTRATION-followups.sha256 before the first call (20:37:03
   UTC), and reached the owner only with the final report, after the runs. The only records
   of the timing are ours: that file, and the digest and time stamped on every call.
2. The headers say "Written 20:35 to 20:50 UTC" (near-ties) and "20:35 to 20:55 UTC"
   (memorization). Those end times were estimates written before finishing. The files were
   final at 20:36:40 UTC and did not change afterwards: every follow-up call carries the same
   digest of both files (`42f3b5cb12c67a09`).

## Run notes

3. Frozen code: at every run start the manifest (runs/<tag>/manifest.jsonl) recorded the same
   sha256 for extra.py, analyze_ties.py, analyze_memorization.py and the data files as the
   pre-registration table; checked again after the runs.
4. Near-ties, the people: the run started at 20:46 UTC, before the near-tie forecast had
   finished, once the sample was fixed. The sample is the first 60 near-tie pairs in file
   order where the forecast made a pick; the 60th sits at position 79, and every pair up to it
   already had both answers. The run was restarted once with more workers (14 instead of 8) to
   finish sooner; the restart recomputed the same 60 pairs and reused the 1,560 cached calls.
5. Memorization, completion probe: the first 180 smaller-model rows were written under the tag
   `mem-complete-small` by mistake. They were appended unchanged to runs/mem-complete/calls.jsonl
   and the folder renamed `_merged-into-mem-complete_small-first-180` so the spend ledger does not
   count them twice. Same prompts and keys; no effect on any number.
6. Memorization, rewording: one reworded pair (29159899f6ec, the order with version A first)
   came back empty twice from the forecast, so the pair is left out as the rules say for an
   answer that does not parse: 499 pairs instead of 500.
7. Every follow-up call was served by the global inference profiles; the failover to the us.
   profiles was never used.

## Findings the pre-registration did not anticipate (descriptive, added after the runs)

8. The smaller model declined to guess on the completion probe: 96.5% of its answers on real headlines
   (98.3% on rewordings) say it has no access to the archive or cannot recall the headline,
   despite "If you are not sure, give your best guess". The forecast's model declined 0.1% of the time.
   So the smaller model's probe cannot detect memorization, and its "pass" on the secondary M1 line
   carries no information. The primary M1 (the forecast's model) is unaffected.
9. The rewording rule "no run of three or more words kept" was followed in 74.1% of the
   rewordings. The pre-registered secondary shows the drop is the same where it was followed in
   both headlines (279 pairs: 77.4% to 68.5%), so partial copying does not explain it.
10. What the forecast's model could "complete" was mostly predictable phrasing (a quoted song lyric, a
    common saying, a question with an obvious end), not remembered Upworthy headlines, and
    losers were completable as often as winners (12 against 7).

11. Display: RESULTS-memorization.md prints the rewording test's permutation p as "0"; it means
    none of the 20,000 sign flips reached the observed difference, so p < 0.00005.

## Added after the runs, exploratory

`explore_ties.py`: could the size of the people's movement, or hedging words in the
forecast's reasoning, tell a near-tie from a real winner? Chosen after seeing the held-out
data, on only 60 near-ties with people, so it is a lead, not a finding; anything it suggests
must be confirmed on unused pairs (near-tie pairs 1,001 onward and the dev split) before it
changes the product. What it showed, among pairs where the forecast made a pick:

| People must move at least (points per 100, the forecast's way) | Called clear: real winners (238) | Called clear: near-ties (60) | Ratio |
|---|---|---|---|
| 1 (the product's rule) | 64.3% | 55.0% | 1.17 |
| 5 | 50.8% | 35.0% | 1.45 |
| 10 | 31.5% | 18.3% | 1.72 |
| 15 | 18.9% | 10.0% | 1.89 |

A stricter threshold makes "clear" rarer on near-ties, but about as fast on real winners;
the ratio stays under 2. Hedging words in the forecast's reasoning ("slightly", "marginal",
"likely" and similar) appear in 60.0% of its picks on near-ties against 50.0% on real
winners. Neither is a usable "too close to call" signal as it stands.
