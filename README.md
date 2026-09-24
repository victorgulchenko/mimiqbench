# MimiqBench

Pre-registered benchmarks for [Mimiq](https://www.mimiqai.com), which shows pages, ads,
emails, copy and video to simulated people and calls which version will do better.

This repository is the public register. Every confirmatory run is planned here first:
the plan, the frozen list of test items (by sha256), the analysis code (by sha256) and
the pass lines are pushed before any held-out item is sent to a model. GitHub records
when each commit was pushed, so a plan's date cannot be moved after the fact. Results
are added afterwards, next to the plan they answer, whatever they show.

## How a run works

1. **Build.** A suite of real tests with known outcomes (A/B tests, message
   megastudies, survey results) is split into a development set and a held-out set,
   from a seed, before any model sees it.
2. **Develop.** Methods are tuned on the development set only. Those numbers are
   exploratory and always labelled so.
3. **Register.** The plan is pushed here: hypotheses, the sha256 of the held-out item
   list, of the analysis code and of the model configuration, the primary metric, the
   baselines, and the pass lines. Which AI models Mimiq uses is confidential, so plans
   name models by their role and fix the exact configuration by its hash.
4. **Run once.** The frozen method runs on the held-out set.
5. **Report.** Results are pushed next to the plan, including failed checks and every
   deviation from the plan.

Each plan is scored against a coin, the best simple rule for that kind of test, and
human forecasters wherever the source published their predictions.

## What has been measured so far

**Headlines** (the Upworthy Research Archive, real click-through tests from 2013 to 2015):

- Mimiq's forecast picked the headline that really won in **75.7%** of 1,000 held-out
  tests (95% interval 73.0% to 78.3%). A coin gets 50%; the best simple rule, picking
  the headline written first, gets 61.3%. Mimiq's simulated people on their own got 61.0%.
- When the call said "clear" (51% of tests) it was right 88.2% of the time.
- **Reworded headlines:** when each headline was reworded, so a model could not have
  seen it before, accuracy fell from 76.7% to 68.0% (499 tests). The plan allowed at
  most a 5-point drop, so this check failed.
- **Tests with no real difference:** the forecast still picked a side in 69.8% of them
  and called 38.4% clear. The plan allowed at most 15% clear, so this check failed too.
  A clear call says which way a difference would go, not whether one exists.

**Beyond headlines** (five runs registered here on 2026-09-24 before any held-out item
was sent to a model; [REGISTER.md](REGISTER.md) has each plan and result):

- Ranking real message variants by real behaviour, Mimiq's forecast was no better than
  chance in four studies: recruiter emails to nurses (Spearman -0.09), honesty oaths
  (-0.11), flu-vaccine text messages (0.07) and fundraising banners (54% of 37 winner
  pairs, interval 38% to 69%). Simple rules and lay forecasters did better where the
  studies measured them. Mimiq's simulated people alone ranked the flu texts at 0.42,
  the one pass for the people.
- Survey answers: one stated estimate of an audience's answer shares came much closer
  to real shares than the tally of simulated people (error 0.114 against 0.232; a
  uniform guess scores 0.209).

**Web pages and flows** (two runs registered here on 2026-09-24 before any held-out item
was sent to a model):

- Picking the page version that really did better (Wikipedia sign-up, account and
  donation pages, a charity pledge page): the forecast and the app's call each picked
  4 of 5 real winners, 80% (interval 38% to 96%). The plan needed all five, so it
  failed. The miss was the most recent test (July 2026). On these five tests, "pick the
  new version" was right every time.
- Flow mode (simulated people using copies of the pages in a real browser) showed both
  versions working on a sign-up test and a donation test, every person finished each,
  but it could not tell the versions apart.
- Next steps of real shoppers (200 held-out steps from recorded shopping sessions): the
  browsing persona did what the shopper did next 8.0% of the time (5.0% to 12.6%), and
  its action type lost to always guessing "click" (55.5% against 81.5%). Its clicks
  were no closer than the average click point of other steps (9.4% against 7.8% within
  50 px). Giving it the shopper's own profile changed nothing, and five different people
  chose the same action type 92% of the time.

So far the forecast has held up on headlines, and not on subtle wording changes in
messages or on web page versions. Flows show whether people can get through a site and
where they stall; they do not predict which version converts better or what a real
visitor clicks next. Video has no confirmatory result yet.

Details: [history/2026-09-23-upworthy-headlines](history/2026-09-23-upworthy-headlines).

## A note on the first benchmark

The headline benchmark's plans were committed to Mimiq's private repository before its
runs (2026-09-23, commits `d4fe7897` at 19:40 and `585f8fb9` at 23:39, Berlin time) and
are published here afterwards, so their timing rests on our word. Every plan from now
on is pushed here first.

## Files

- [REGISTER.md](REGISTER.md): every registered plan, its status and its result.
- [prereg/](prereg): plans, one folder per run.
- [history/](history): runs registered before this repository existed.
- [ledger/](ledger): daily anchors of Mimiq's sealed prediction ledger (live A/B tests
  called before their results existed).

Text in this repository is licensed CC BY 4.0. Test data keeps its source's license;
suites whose sources do not allow redistribution are identified by sha256 only.
