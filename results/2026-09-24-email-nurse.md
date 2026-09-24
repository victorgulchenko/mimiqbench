# Results: email-megastudies (nurse): which recruiter message gets more nurses to engage

Plan: `benchmarks/mimiqbench/prereg/final/email-nurse.md` (public register: https://github.com/victorgulchenko/mimiqbench/commit/28fb756829d77c71c5d2171e751fd0472057a4d5). Config sha256 `8d1a8d5c206f9c4718afebaf270d247d79ffd95c68130ae87ac16311df654c8a`. Suite `email-megastudies`, items sha256 `fabaa9d75bf1e2176fabe8e599394a408287c95cb4a29a8b35e8be98974b738f`. Sample: 46 held-out items. Analyzed 2026-09-24T11:16:15+00:00 by `benchmarks/mimiqbench/confirm.py`.

## Hypotheses (pass lines fixed in the plan)

- **H1: FAIL.** Mimiq's forecast ranks the ten messages in the real order: Spearman above 0, one-sided p below 0.05. Result: Spearman -0.09 (95% interval -0.78 to 0.71), one-sided p 0.6000, 10 arms.
- **H2: FAIL.** It ranks them better than the expert panel: Spearman above 0.0244. Result: Spearman -0.09 (95% interval -0.78 to 0.71), one-sided p 0.6000, 10 arms; line 0.024.
- **H3: FAIL.** On the 11 pairs with a significant winner it is right more often than the experts (59.1%). Result: 45.5% of 11 winner pairs (Wilson 21.3% to 72.0%; resampling arms 0.0% to 100.0%); line 59.1%.
- **H4: FAIL.** Mimiq's simulated people alone rank the messages positively: Spearman above 0, one-sided p below 0.05. Result: Spearman -0.10 (95% interval -0.78 to 0.62), one-sided p 0.6253, 10 arms.

## Secondary checks (no pass lines)

- Mimiq's forecast, winner pairs: 45.5% of 11; makes a pick 81.8%, right when it picks 44.4%; right in both orders 36.4% (chance 25%).
  - real difference clear: 12.5% of 4.
  - real difference likely: 64.3% of 7.
  - near-ties: still picks 73.3% of 15.
  - picked the version shown first 54.4%; orders disagreed 17.8%.
- Mimiq's people, winner pairs: 45.5% of 11; makes a pick 100.0%, right when it picks 45.5%.
  - real difference clear: 25.0% of 4.
  - real difference likely: 57.1% of 7.
  - near-ties: still picks 100.0% of 15.
- Mimiq's call, winner pairs: 45.5% of 11; makes a pick 81.8%, right when it picks 44.4%; right in both orders 36.4% (chance 25%).
  - real difference clear: 12.5% of 4.
  - real difference likely: 64.3% of 7.
  - Mimiq's tier clear: 81.8% of winner pairs, right 44.4%.
  - Mimiq's tier close: 18.2% of winner pairs, right 50.0%.
  - near-ties: still picks 73.3% of 15, calls clear 53.3%.
  - picked the version shown first 54.4%; orders disagreed 17.8%.
- The rule named in the plan, "longer text", on the same winner pairs: 63.6%.
- Other simple rules on the same winner pairs, for context only (not named in the plan): "shorter text" 36.4%, "has a number" 36.4%, "asks a question" 50.0%, "says you" 50.0%.
- Forecasters "experts_pooled" on the same winner pairs: 60.0% of 10.
- Mimiq's forecast, as a ranking: Spearman -0.09 over 10 arms; top version picked: no.
- Mimiq's people, as a ranking: Spearman -0.10 over 10 arms; top version picked: no.
- Forecasters' Spearman (email-megastudies:nurse:engaged:rank): experts_pooled 0.02.
- Memory probe on 11 winner pairs: 59.1% with the source named, 45.5% without (difference 0.136); claims of remembering: 0.

## Counts and spend

- Mimiq's forecast: {"written": 45}; spend $0.26.
- Mimiq's forecast, as a ranking: {"written": 1}; spend $0.00.
- Mimiq's people, as a ranking: {"written": 1}; spend $0.75.
- Mimiq's people: {"written": 45}; spend $0.00.
- Mimiq's call: {"written": 45}; spend $0.00.
- the memory probe: {"written": 11}; spend $0.10.

## Deviations

- None recorded by the harness. Anything else is listed here by hand below this line.

## Notes by hand (proof lane, after the run)

- Added after the run by the proof lane. Every number is from this run's files; nothing was re-run.
- Run 2026-09-24, 13:13 to 13:16 CEST; $1.17 of the plan's $2.00 cap. Every sampled item ran; none failed or was left incomplete. No step stopped. No deviation.
- Panel: 25 simulated people, `benchmarks/mimiqbench/panels/confirm-email-nurse.json`, sha256 `e95ae204a061a68cd91f7e9b1877e857ce53d441a312afd65ce48e3aa73fb97e`, built after the GO with the app's audience steps (seed 20260924). The app's audience reader turned the study's audience (nurses in 28 European countries: the EU except Denmark, plus Norway and Switzerland) into a UK-only panel, and the UK was not in the study. That is what a customer would have got, so it stands; it is a finding about recruiting, not a deviation.
- Expert baseline: the plan's 59.1% counts the experts' one tied pooled forecast as half over the 11 winner pairs. The secondary line above (60.0% of 10) leaves that pair out. H3's pass line is the plan's 59.1%.
- H2's line prints as 0.024; the line tested is 0.0244 (rounded in print only).
- The rule named in the plan, the longer message, was right on 63.6% of the 11 winner pairs. Mimiq's forecast was right on 45.5%.
- Mimiq's call labelled 81.8% of the winner pairs clear and was right on 44.4% of those. It also called 53.3% of the 15 near-ties clear. These messages differ by two points of engagement at most, and the call's confidence was not earned.
- The memory probe found no memory, as expected for a study published after the models' training data was collected: no answer claimed to remember, and 59.1% with the study named against 45.5% without on 11 pairs (difference +13.6 points, sign-flip p 0.25).
- Integrity check after the run: all 384 prompts this run sent (the held-out cache) were scanned for every value in the items' stimulus fields and extra labels (text values, and numbers of three digits or more); none reached a model. The nurse items carry a secondary outcome in `fields.registered` (two-digit counts, too small to scan for); no prompt contains the word. The forecast saw the message texts and the audience line only, as the plan says; the people saw the message text with their own persona.
- What the people read about themselves: the app's audience steps join the audience line and its parsed parts with semicolons, and the persona builder (`backend/persona_generator/lazy_hydrator.py`) splits them again on semicolons. This audience line has a semicolon of its own, so the parts shifted: 6 of the 25 people were told, with every message, that they were "actively looking into this area: about 10,000 per message.", and 8 more that they cared about that "area" in general (60 and 80 of the 250 people prompts). That is how the app builds people today; it is recorded, not changed.
