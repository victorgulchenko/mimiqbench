# Register

One row per confirmatory run. A row is added when its plan is pushed, before the run,
and updated when the result is in. Rows are never removed.

| ID | Suite | Question | Plan pushed | Held-out items sha256 | Status | Result |
|---|---|---|---|---|---|---|
| H1 | Upworthy headlines (clear winners, p < 0.01) | Does Mimiq's forecast pick the real winner more often than the best simple rule? | 2026-09-23, private repo first (see README) | `9ae3db65...2e098` | Reported | [75.7% on 1,000](history/2026-09-23-upworthy-headlines/RESULTS.md) |
| H2 | Upworthy headlines (near-ties, p > 0.5) | Does Mimiq say "too close to call" when there is no real winner? | 2026-09-23, private repo first | `9d6a4fe8...61488` | Reported | [Check failed: 38.4% called clear](history/2026-09-23-upworthy-headlines/RESULTS-ties.md) |
| H3 | Upworthy headlines (memorization) | Does the forecast hold on headlines a model cannot have seen? | 2026-09-23, private repo first | `9ae3db65...2e098` | Reported | [Recall check passed; rewording check failed](history/2026-09-23-upworthy-headlines/RESULTS-memorization.md) |
| C1 | Email: LinkedIn nurse recruitment megastudy (results public since 29 June 2026) | Does Mimiq's forecast rank ten real recruiter messages by real engagement, better than the study's expert panel? | 2026-09-24 | see [plan](prereg/2026-09-24-email-nurse.md) | Registered, not yet run | |
| C2 | Copy: honesty-oath megastudy | Does Mimiq rank 21 oaths by real honesty better than the published lay forecasters? | 2026-09-24 | see [plan](prereg/2026-09-24-megaoath-copy.md) | Registered, not yet run | |
| C3 | SMS: Walmart flu-vaccine megastudy (texts listed by sha256 only) | Does Mimiq rank 22 real text messages by real vaccinations better than scientists and lay forecasters? | 2026-09-24 | see [plan](prereg/2026-09-24-flu-sms-walmart.md) | Registered, not yet run | |
| C4 | Ads: Wikimedia fundraising banners | Does Mimiq pick the banner that raised more? | 2026-09-24 | see [plan](prereg/2026-09-24-wikimedia-banners.md) | Registered, not yet run | |
| C5 | Ask: survey answer shares (Twin-2K-500) | Does one stated estimate of an audience's answers get closer to real survey shares than the tally of simulated people? | 2026-09-24 | see [plan](prereg/2026-09-24-stated-room.md) | Registered, not yet run | |
