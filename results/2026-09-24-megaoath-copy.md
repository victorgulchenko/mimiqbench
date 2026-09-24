# Results: megaoath-copy: which honesty oath makes people report their income more honestly

Plan: `benchmarks/mimiqbench/prereg/final/megaoath-copy.md` (public register: https://github.com/victorgulchenko/mimiqbench/commit/28fb756829d77c71c5d2171e751fd0472057a4d5). Config sha256 `80ddabaf1d3a33d8167c891681c606a680d8dcb4454e829792b306959ba92118`. Suite `megaoath-copy`, items sha256 `8b233e8ce3ac19fd42b8ded14126f593d8f08b7cb0dd4204849fda6e2717b7d1`. Sample: 211 held-out items. Analyzed 2026-09-24T11:22:56+00:00 by `benchmarks/mimiqbench/confirm.py`.

## Hypotheses (pass lines fixed in the plan)

- **H1: FAIL.** Mimiq's forecast ranks the 21 oaths in the real order: Spearman above 0, one-sided p below 0.05. Result: Spearman -0.11 (95% interval -0.58 to 0.36), one-sided p 0.6801, 21 arms.
- **H2: FAIL.** On the 20 oaths the forecasters rated, it ranks at least as well as lay people (Spearman 0.4045). Result: Spearman -0.04 (95% interval -0.56 to 0.45), one-sided p 0.5690, 20 arms; line 0.405.
- **H3: FAIL.** On pairs with a significant winner, the lower end of the 95% interval that resamples oaths is above 50%. Result: 47.8% of 67 winner pairs (Wilson 36.3% to 59.5%; resampling arms 21.5% to 72.1%); line 50.0%.
- **H4: FAIL.** Mimiq's simulated people alone rank the oaths positively: Spearman above 0, one-sided p below 0.05. Result: Spearman -0.33 (95% interval -0.68 to 0.10), one-sided p 0.9257, 21 arms.

## Secondary checks (no pass lines)

- Mimiq's forecast, winner pairs: 47.8% of 67; makes a pick 64.2%, right when it picks 46.5%; right in both orders 29.9% (chance 25%).
  - real difference clear: 51.2% of 41.
  - real difference likely: 42.3% of 26.
  - near-ties: still picks 64.3% of 56.
  - picked the version shown first 47.9%; orders disagreed 34.8%.
- Mimiq's people, winner pairs: 26.9% of 67; makes a pick 100.0%, right when it picks 26.9%.
  - real difference clear: 24.4% of 41.
  - real difference likely: 30.8% of 26.
  - near-ties: still picks 98.2% of 56.
- Mimiq's call, winner pairs: 47.8% of 67; makes a pick 64.2%, right when it picks 46.5%; right in both orders 29.9% (chance 25%).
  - real difference clear: 51.2% of 41.
  - real difference likely: 42.3% of 26.
  - Mimiq's tier clear: 17.9% of winner pairs, right 25.0%.
  - Mimiq's tier leaning: 46.3% of winner pairs, right 54.8%.
  - Mimiq's tier close: 35.8% of winner pairs, right 50.0%.
  - near-ties: still picks 64.3% of 56, calls clear 17.9%.
  - picked the version shown first 47.9%; orders disagreed 34.8%.
- Other simple rules on the same winner pairs, for context only (not named in the plan): "longer text" 59.7%, "shorter text" 40.3%, "has a number" 49.3%, "asks a question" 50.0%, "says you" 50.0%.
- Forecasters "collaborators" on the same winner pairs: 75.0% of 64.
- Forecasters "behavioural_scientists" on the same winner pairs: 64.1% of 64.
- Forecasters "lay_people" on the same winner pairs: 79.7% of 64.
- Forecasters "finance_experts" on the same winner pairs: 76.6% of 64.
- Forecasters "llms" on the same winner pairs: 42.9% of 63.
- Mimiq's forecast, as a ranking: Spearman -0.11 over 21 arms; top version picked: no.
- Mimiq's people, as a ranking: Spearman -0.33 over 21 arms; top version picked: no.
- Memory probe on 20 winner pairs: 47.5% with the source named, 57.5% without (difference -0.100); claims of remembering: 0.

## Counts and spend

- Mimiq's forecast: {"written": 210}; spend $1.05.
- Mimiq's forecast, as a ranking: {"written": 1}; spend $0.00.
- Mimiq's people, as a ranking: {"written": 1}; spend $1.47.
- Mimiq's people: {"written": 210}; spend $0.00.
- Mimiq's call: {"written": 210}; spend $0.00.
- the memory probe: {"written": 20}; spend $0.15.

## Deviations

- None recorded by the harness. Anything else is listed here by hand below this line.

## Notes by hand (proof lane, after the run)

- Added after the run by the proof lane. Every number is from this run's files; nothing was re-run.
- Run 2026-09-24, 13:16 to 13:23 CEST; $2.72 of the plan's $4.00 cap. Every sampled item ran; none failed or was left incomplete. No step stopped. No deviation.
- Panel: 25 simulated people, `benchmarks/mimiqbench/panels/confirm-megaoath-copy.json`, sha256 `35ae1be80aa79b0e0ebbe80087fb7e8a7c6e94d0445ba3c66da5e024bafe5ff9`, built after the GO with the app's audience steps (seed 20260924). The app's audience reader turned "adults in the UK (64%) and the US (36%)" into a UK-only panel. That is what a customer would have got; it is recorded, not changed.
- The forecasters' Spearman over the 20 oaths they rated, from the plan: lay people 0.4045, finance experts 0.42, collaborators 0.29, behavioural scientists 0.25, language models run by the study's authors 0.06. Mimiq's forecast on the same 20 oaths: -0.04 (on all 21: -0.11). The secondary list above prints no forecaster correlation for this suite because they rated 20 of the 21 oaths; H2 uses those 20.
- On the same winner pairs, lay people's forecasts were right 79.7% of the time (64 pairs) and the study's own language-model forecasters 42.9% (63 pairs). Mimiq's forecast was right on 47.8% of 67.
- Mimiq's people alone ran backwards: Spearman -0.33, right on 26.9% of 67 winner pairs.
- The memory probe found no memory: no answer claimed to remember, and 47.5% with the study named against 57.5% without on 20 pairs.
- Integrity check after the run: all 1,025 prompts this run sent (the held-out cache) were scanned for every value in the items' stimulus fields and extra labels (text values, and numbers of three digits or more); none reached a model.
- What the people read about themselves: the app's audience steps join the audience line and its parsed parts with semicolons, and the persona builder (`backend/persona_generator/lazy_hydrator.py`) splits them again on semicolons. This audience line has a semicolon of its own, so the parts shifted: 2 of the 25 people were told, with every message, that they were "actively looking into this area: 21,506 in all, about 950 per statement.", and 8 more that they cared about that "area" in general (42 and 168 of the 525 people prompts). That is how the app builds people today; it is recorded, not changed.
