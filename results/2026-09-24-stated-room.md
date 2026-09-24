# Results: twin2k-ask: a stated estimate against ask the room's tally, on held-out survey questions

Plan: `benchmarks/mimiqbench/prereg/final/stated-room.md` (public register: https://github.com/victorgulchenko/mimiqbench/commit/28fb756829d77c71c5d2171e751fd0472057a4d5). Config sha256 `4b82ee77c17a455e7fdfb7921b755ce9cfce790be0372909563bc449d89af2f5`. Suite `twin2k-ask`, items sha256 `d9c83e9cb5acc6c45df0c51e1640c4ddda856e474468160805ce145b11001fb1`. Sample: 682 held-out items. Analyzed 2026-09-24T11:42:20+00:00 by `benchmarks/mimiqbench/confirm.py`.

## Hypotheses (pass lines fixed in the plan)

- **H-B1: PASS.** On the held-out items asked of everyone, the stated estimate's mean error is lower than the room's: the paired difference is below 0 and the upper end of its 95% cluster-bootstrap interval is below 0. Result: mean error 0.114 against 0.232 on 188 items (68 clusters); difference -0.118 (95% cluster interval -0.138 to -0.098); missing scored as uniform: 0 and 0; not run: 0. (Line rewritten by hand from results.json; see the notes.)
- **H-B2: PASS.** On all held-out distribution items, the stated estimate's mean error is at least 0.05 below a uniform guess's. Result: mean error 0.110 against a uniform guess's 0.209 on 682 items; needed at most 0.159; missing scored as uniform: 0; not run: 0.

## Secondary checks (no pass lines)

- the stated estimate: mean distance 0.110 over 682 items; uniform guess 0.209; the same people two weeks later 0.016; everyone's shares used for a subgroup 0.028.
- ask the room (production tally): mean distance 0.232 over 188 items; uniform guess 0.212; the same people two weeks later 0.016.
- Subgroup gaps (ordinal items): correlation of predicted and real gaps 0.55 over 442 subgroup items; real = 0.44 x predicted.

## Counts and spend

- the stated estimate: {"written": 682}; spend $0.95.
- ask the room (production tally): {"written": 188}; spend $6.03.

## Deviations

- None recorded by the harness. Anything else is listed here by hand below this line.

## Notes by hand (proof lane, after the run)

- Added after the run by the proof lane. Every number is from this run's files; nothing was re-run.
- Run 2026-09-24, 13:32 to 13:42 CEST; $6.98 of the plan's $8.00 cap, charged to the engine lane (the stated estimate $0.95 on 682 items, the room $6.03 on 188). Every sampled item ran; none failed or was left incomplete; no distribution was missing on either side. No step stopped. No deviation.
- Display fix: the harness printed H-B1's result with the template for pairs ("n/a of 188 winner pairs"), because the hypothesis type's name, paired_less_cluster, starts with "pair" and `confirm.py` tests for that first. The verdict and the numbers were computed correctly and are in results.json; the H-B1 line above was rewritten from that file. `confirm.py` stays frozen until the coordinator ends the freeze; the one-line fix is noted for after.
- A correction to the plan's wording: it says the patch is not applied to production. It had in fact been applied to production earlier the same day (12:40 CEST, before the plan was frozen). The run used the patch's own code, as the plan says, and production's room.py now carries the same code (the same syntax tree for the prompt, the options list and the function), so the result applies to the stated estimate as ask the room returns it today.
- Panel: `benchmarks/engine_lab/panels/us-adults-25.json`, sha256 `95b9665e61c38033c9b306d6ab05aaa116469f3b851081c0541ab9b271bd762c`, as frozen.
- The stated estimate was closer than the room on 77.7% of the 188 items asked of everyone.
- The room, as production tallies it, was worse than a uniform guess on held-out items too: 0.232 against 0.212 (normalized -0.10), as on dev.
- What the pass does not show, on matched items (`score_distributions` per item over this run's predictions): on the 165 items where the same real people answered again two weeks later, the estimate's error was 0.116 against their retest's 0.016, about seven times the noise floor. On the 494 subgroup items, using everyone's real shares would have been far closer (0.028 against the estimate's 0.108), and the estimate beat that on only 9.1% of them. A customer does not have everyone's real answer, so this is not a usable rival, but it shows the estimate is far from knowing a subgroup's answer.
- Subgroup gaps (ordinal items): predicted and real gaps correlate 0.55 over 442 subgroup items, and real gaps are 0.44 times the predicted ones. The estimate gets the direction of a subgroup's difference partly right and overstates its size more than twofold. On dev these were 0.77 and 0.66.
- Integrity check after the run: all 5,382 prompts this run sent (the held-out cache) were scanned for every value in the items' stimulus fields and extra labels (text values, and numbers of three digits or more); no outcome field reached a model. The only matches were the answer options and the products' names and categories, which are part of the questions as they were asked.
