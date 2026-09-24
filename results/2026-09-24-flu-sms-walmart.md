# Results: flu-sms (Walmart): which pharmacy text gets more people a flu shot

Plan: `benchmarks/mimiqbench/prereg/final/flu-sms-walmart.md` (public register: https://github.com/victorgulchenko/mimiqbench/commit/28fb756829d77c71c5d2171e751fd0472057a4d5). Config sha256 `95235142348c2f54dc8765a83e6564d06077773aced78daa9c6d985ace40e82a`. Suite `flu-sms`, items sha256 `2e5d02a1528fabf8eb97361e84782d60cc577f97956aefc5ab42cebc10529674`. Sample: 232 held-out items. Analyzed 2026-09-24T11:30:47+00:00 by `benchmarks/mimiqbench/confirm.py`.

## Hypotheses (pass lines fixed in the plan)

- **H1: FAIL.** Mimiq's forecast ranks the 22 texts in the real order (31 December): Spearman above 0, one-sided p below 0.05. Result: Spearman 0.07 (95% interval -0.41 to 0.51), one-sided p 0.3830, 22 arms.
- **H2: FAIL.** Against the 31 October outcome the forecasters predicted, it ranks at least as well as lay people (0.5981). Result: Spearman -0.04 (95% interval -0.47 to 0.41), one-sided p 0.5686, 22 arms, second outcome window; line 0.598.
- **H3: PASS.** Against the 31 October outcome it ranks better than the scientists (above -0.1322). Result: Spearman -0.04 (95% interval -0.47 to 0.41), one-sided p 0.5686, 22 arms, second outcome window; line -0.132.
- **H4: FAIL.** On pairs with a significant winner, the lower end of the 95% interval that resamples texts is above 50%. Result: 55.3% of 94 winner pairs (Wilson 45.3% to 65.0%; resampling arms 37.9% to 73.1%); line 50.0%.
- **H5: PASS.** Mimiq's simulated people alone rank the texts positively (31 December): Spearman above 0, one-sided p below 0.05. Result: Spearman 0.42 (95% interval 0.01 to 0.72), one-sided p 0.0269, 22 arms.

## Secondary checks (no pass lines)

- Mimiq's forecast, winner pairs: 55.3% of 94; makes a pick 51.1%, right when it picks 60.4%; right in both orders 30.9% (chance 25%).
  - real difference clear: 56.5% of 62.
  - real difference likely: 53.1% of 32.
  - near-ties: still picks 70.5% of 61.
  - picked the version shown first 67.1%; orders disagreed 42.9%.
- Mimiq's people, winner pairs: 75.5% of 94; makes a pick 100.0%, right when it picks 75.5%.
  - real difference clear: 82.3% of 62.
  - real difference likely: 62.5% of 32.
  - near-ties: still picks 100.0% of 61.
- Mimiq's call, winner pairs: 55.3% of 94; makes a pick 51.1%, right when it picks 60.4%; right in both orders 30.9% (chance 25%).
  - real difference clear: 56.5% of 62.
  - real difference likely: 53.1% of 32.
  - Mimiq's tier clear: 23.4% of winner pairs, right 90.9%.
  - Mimiq's tier leaning: 27.7% of winner pairs, right 34.6%.
  - Mimiq's tier close: 48.9% of winner pairs, right 50.0%.
  - near-ties: still picks 70.5% of 61, calls clear 39.3%.
  - picked the version shown first 67.1%; orders disagreed 42.9%.
- The rule named in the plan, "more messages", on the same winner pairs: 81.4%.
- Other simple rules on the same winner pairs, for context only (not named in the plan): "longer text" 64.4%, "shorter text" 35.6%, "has a number" 50.0%, "asks a question" 18.6%, "says you" 50.0%.
- Forecasters "experts" on the same winner pairs: 44.6% of 92.
- Forecasters "lay" on the same winner pairs: 89.4% of 94.
- Mimiq's forecast, as a ranking: Spearman 0.07 over 22 arms (second window -0.04); top version picked: no.
- Mimiq's people, as a ranking: Spearman 0.42 over 22 arms (second window 0.35); top version picked: no.
- Forecasters' Spearman (flu-sms:walmart:rank): experts -0.13, experts_excluding_own 0.27, lay 0.60.
- Memory probe on 30 winner pairs: 78.3% with the source named, 76.7% without (difference 0.017); claims of remembering: 0.

## Counts and spend

- Mimiq's forecast: {"written": 231}; spend $1.55.
- Mimiq's forecast, as a ranking: {"written": 1}; spend $0.00.
- Mimiq's people, as a ranking: {"written": 1}; spend $1.66.
- Mimiq's people: {"written": 231}; spend $0.00.
- Mimiq's call: {"written": 231}; spend $0.00.
- the memory probe: {"written": 30}; spend $0.38.

## Deviations

- None recorded by the harness. Anything else is listed here by hand below this line.

## Notes by hand (proof lane, after the run)

- Added after the run by the proof lane. Every number is from this run's files; nothing was re-run.
- Run 2026-09-24, 13:23 to 13:31 CEST; $3.63 of the plan's $6.00 cap. Every sampled item ran; none failed or was left incomplete. No step stopped. No deviation.
- Panel: 25 simulated people, `benchmarks/mimiqbench/panels/confirm-flu-sms-walmart.json`, sha256 `a6a3bfacd89bd3f0f09ec1b8e42c379762a2462a9ded690596269af54e1f11d5`, built after the GO with the app's audience steps (seed 20260924). The app's audience reader turned the suite's audience line (US pharmacy customers, mean age 60, 62% of them women) into US women aged 55 to 65 only. That is what a customer would have got; it is recorded, not changed.
- H3 passes only because its line, the scientists' own correlation, is below zero (-0.1322). Mimiq's forecast against the 31 October outcome was -0.04, no better than chance. Read H3 as "not worse than the scientists", nothing more.
- H5 is a real pass: Mimiq's simulated people alone ranked the 22 texts at Spearman 0.42 (95% interval 0.01 to 0.72, one-sided p 0.027) and picked the winner in 75.5% of 94 winner pairs. On dev (another study's 19 texts) the people ran backwards. The plan set no correction for testing five hypotheses; at 0.05 / 5 = 0.01 this p would not pass.
- On the same winner pairs: the rule named in the plan, more messages, 81.4%; lay forecasters 89.4% (94 pairs); scientists 44.6% (92 pairs); Mimiq's forecast 55.3% (94 pairs).
- Exploratory, not in the plan: on the memory probe's 30 winner pairs, the probe's question without the study named (which text won the real test) was right 76.7% of the time, and Mimiq's forecast 60.0% on the same pairs. The probe asks from the outside; the forecast asks how these people would react. One suite and 30 pairs: a lead for the engine lane, not a result.
- The memory probe found no memory: no answer claimed to remember, and 78.3% with the study named against 76.7% without (difference +1.7 points).
- Integrity check after the run: all 1,132 prompts this run sent (the held-out cache) were scanned for every value in the items' stimulus fields and extra labels (text values, and numbers of three digits or more); none reached a model.
- What the people read about themselves: the app's audience steps join the audience line and its parsed parts with semicolons, and the persona builder (`backend/persona_generator/lazy_hydrator.py`) splits them again on semicolons. This audience line has a semicolon of its own, so the parts shifted: 3 of the 25 people were told, with every message, that they were "actively looking into this area: mean age 60, 62% women.", and 11 more that they cared about that "area" in general (66 and 242 of the 550 people prompts). That is how the app builds people today; it is recorded, not changed.
