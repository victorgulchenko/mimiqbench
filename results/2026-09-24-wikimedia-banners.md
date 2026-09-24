# Results: wikimedia-banners: which donation banner raises more money

Plan: `benchmarks/mimiqbench/prereg/final/wikimedia-banners.md` (public register: https://github.com/victorgulchenko/mimiqbench/commit/28fb756829d77c71c5d2171e751fd0472057a4d5). Config sha256 `17f10657856b2dda2700145e9e2c8d38eb5fe35132b2204893835e7a40b26962`. Suite `wikimedia-banners`, items sha256 `16ca52d3730cdf228682f160671844641333aa7b62b330d8a27270644ec651a7`. Sample: 66 held-out items. Analyzed 2026-09-24T11:32:04+00:00 by `benchmarks/mimiqbench/confirm.py`.

## Hypotheses (pass lines fixed in the plan)

- **H1: FAIL.** Mimiq's forecast picks the banner that raised more more often than not: the Wilson 95% interval's lower end is above 50%. Result: 54.1% of 37 winner pairs (Wilson 38.4% to 69.0%); line 50.0%.

## Secondary checks (no pass lines)

- Mimiq's forecast, winner pairs: 54.1% of 37; makes a pick 78.4%, right when it picks 55.2%; right in both orders 43.2% (chance 25%).
  - real difference clear: 55.4% of 28.
  - real difference likely: 50.0% of 9.
  - near-ties: still picks 75.0% of 12.
  - picked the version shown first 47.7%; orders disagreed 22.7%.
- The rule named in the plan, "shorter text", on the same winner pairs: 63.5%.
- Other simple rules on the same winner pairs, for context only (not named in the plan): "longer text" 36.5%, "has a number" 50.0%, "asks a question" 47.3%, "says you" 50.0%.

## Counts and spend

- Mimiq's forecast: {"written": 66}; spend $0.45.

## Deviations

- None recorded by the harness. Anything else is listed here by hand below this line.

## Notes by hand (proof lane, after the run)

- Added after the run by the proof lane. Every number is from this run's files; nothing was re-run.
- Run 2026-09-24, 13:31 to 13:32 CEST; $0.45 of the plan's $1.00 cap. All 66 sampled items ran; none failed or was left incomplete. No deviation. The plan has no panel (forecast only).
- The rule named in the plan, the shorter banner, was right on 63.5% of the 37 winner pairs. Mimiq's forecast was right on 54.1%.
- Integrity check after the run: all 104 prompts this run sent (the held-out cache) were scanned for every value in the items' stimulus fields and extra labels (text values, and numbers of three digits or more); no outcome field reached a model. The only matches were the names of the people who signed the appeals (kept in the items' `extra` labels), and those names are in the banner texts themselves.
