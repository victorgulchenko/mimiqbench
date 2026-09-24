# Register

One row per confirmatory run. A row is added when its plan is pushed, before the run,
and updated when the result is in. Rows are never removed.

| ID | Suite | Question | Plan pushed | Held-out items sha256 | Status | Result |
|---|---|---|---|---|---|---|
| H1 | Upworthy headlines (clear winners, p < 0.01) | Does Mimiq's forecast pick the real winner more often than the best simple rule? | 2026-09-23, private repo first (see README) | `9ae3db65...2e098` | Reported | [75.7% on 1,000](history/2026-09-23-upworthy-headlines/RESULTS.md) |
| H2 | Upworthy headlines (near-ties, p > 0.5) | Does Mimiq say "too close to call" when there is no real winner? | 2026-09-23, private repo first | `9d6a4fe8...61488` | Reported | [Check failed: 38.4% called clear](history/2026-09-23-upworthy-headlines/RESULTS-ties.md) |
| H3 | Upworthy headlines (memorization) | Does the forecast hold on headlines a model cannot have seen? | 2026-09-23, private repo first | `9ae3db65...2e098` | Reported | [Recall check passed; rewording check failed](history/2026-09-23-upworthy-headlines/RESULTS-memorization.md) |
