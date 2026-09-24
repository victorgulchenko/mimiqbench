# Plan: web-opera-actions, do Mimiq's browsing personas do what real shoppers do next?

Final, 2026-09-24. Written by the web lane from 100 dev items; no model has seen any held-out item. The
commit that adds this file to the public register is its timestamp. Nothing below changes after that;
results and deviations go in RESULTS next to it.

Mimiq keeps its choice of AI models confidential, so this plan names models by role only (the browsing
persona's model, the recruiting model). Their exact identity and settings are fixed by a private
configuration file whose sha256 is below; the run refuses to start if that file differs by one byte.

## Question

Mimiq's flow mode sends simulated people through a website in a real browser. At every step each person
looks at the screen (a screenshot and the list of clickable elements), remembers what they did so far,
and decides what to do next. This plan asks whether those decisions look like a real person's: on pages
real shoppers were on, with the shopper's own history, does the simulated person do what the shopper did
next? And does giving the simulated person the shopper's own profile make its choices any more like the
shopper's?

## Hypotheses (all registered now)

- **H1 (better than a trivial guess):** on steps where the shopper clicked something visible on the
  screenshot, the simulated person with the shopper's own profile clicks within 50 pixels of the shopper's
  click more often than a fixed guess at the average click position (the mean click point of the 78 dev
  clicks, x 642.6, y 255.0 on a 1,280-pixel-wide screen). Passes if its rate is higher and a one-sided
  exact McNemar test gives p < 0.05.
- **H2 (bad news, registered as such):** the simulated person does what the shopper did next in fewer than
  one step in four: the upper end of the Wilson 95% interval of its exact next-action accuracy is below 25%.
- **H3 (profile makes no difference):** the shopper's own profile and no profile at all match the shopper's
  next action equally often: the 90% bootstrap interval of the paired difference in exact accuracy lies
  inside minus 5 to plus 5 percentage points (an equivalence test at 5% per side).
- **H4 (bad news, registered as such):** the simulated person gets the action type (click, type, or end the
  session) right less often than the rule "always click": its type accuracy is lower and a one-sided exact
  McNemar test gives p < 0.05.
- **H5 (the people move as one):** five different recruited people, shown the same step, choose the same
  action type in at least 80% of pairs of them (mean pairwise agreement over the steps).

H2, H4 and H5 state what dev showed about the product's limits; they are registered so that a held-out
confirmation of bad news carries the same weight as one of good news.

## Data

- OPeRA (Wang et al., 2025, arXiv 2506.05606; data CC BY 4.0): 51 real people shopping on a large online
  store in their own browsers in 2025, with their own survey answers; a plug-in logged each page (as
  simplified HTML), a viewport screenshot, the mouse position and every click, text entry and session end.
- Suite `opera-actions`, held-out = the dataset's own test split: 200 decision points (163 clicks, 25 text
  entries, 12 session ends, as the suite card states), from sessions no dev item comes from. 12 of the 15
  held-out shoppers also shopped in dev sessions (the dataset splits by session).
- items.jsonl sha256 `7d472d7f4a6a4b51b7ef30629061e27e6e0f2bbee9a89c5ee08210b00b976315`. The sample is
  held-out positions 1 to 200; sample ids sha256
  `766d57b7858680a2f1f230566129b0db12e2cac058055358f1d363352b957c31`.

## What the simulated person sees, and whose code decides

- The decision is production's own: the live flow loop's decision block (step message, hints, model call,
  parsing, normalization and action guards), made callable on a stored page state by a
  behaviour-preserving patch (`benchmarks/lab/patches/web-step-decision.patch`). Production code is pinned
  at a fixed commit named in the configuration; the patch's two methods are compiled onto it. Before the
  run, a check shows the requests are byte-identical to those of the patched production file.
- The page state, built only from what the dataset logged before the action: the page's address; the
  real screenshot, resized to 1,280 pixels wide, cut at 720 pixels high and encoded as production encodes
  its own screenshots (when the dataset has no screenshot for a step, which is usual for text entries and
  session ends, the person decides without one, as production does when a capture fails); the list of
  clickable elements, emulated on the stored page with production's own rules (its selectors in page
  order, its text rule, the first 50; positions are unknown and left out); the shopper's earlier actions in
  the session as production's journey; the step number and the time since the session began.
- The goal line, the same for every step and person: shopping on that store for themselves, continuing the
  session the way they normally would (exact words in the configuration).
- Three ways, on the same steps: (1) **own profile**: one person recruited the app's way from the shopper's
  own survey answers; (2) **no profile**: production's defaults for every field; (3) **panel**: five people
  recruited the app's way from a one-line description of the dataset's population, on the first 30 sample
  steps only (cost).
- Scoring. A click counts as the shopper's click when it lands within 50 pixels of the shopper's click
  point (a radius fixed on dev from the dataset's own training clicks: two clicks on the same element fall
  within 50 pixels 87.5% of the time, clicks on different elements of the same screen 4.3%). Production's
  click and press-and-hold are clicks; type and fill-form are text entries (right if they go into the
  element the shopper typed into); done and give-up end the session; scroll, back, navigate, wait and
  check-email are actions the dataset's log never shows next, so they count as wrong.

## Primary metrics and pass lines

As in the hypotheses: H1 hit rate within 50 pixels against the fixed point (paired, exact McNemar); H2
exact next-action accuracy, Wilson upper end below 25%; H3 paired bootstrap (items resampled, 5,000
rounds, seed 11), 90% interval inside plus or minus 5 points; H4 type accuracy against "always click"
(paired, exact McNemar); H5 mean pairwise type agreement at least 80%.

## Baselines

"Always click"; a random point on the screen; the average click point of the other held-out steps; a
random element from production's list; and, for context only, the dataset paper's own text-only language
model baselines on the full test split (not the same protocol).

## Secondary checks (reported, no pass line)

Hits within 25 and 100 pixels; the share of scrolls and typed addresses; accuracy by the shopper's kind of
click; how often the shopper's target was in production's element list at all; the text typed against
the shopper's search words; the panel's click agreement and how often any of the five did what the shopper
did (1 to 5 people).

## Exclusions, fixed now

A step whose model call fails after production's retries (an API error, not a bad answer) is left out and
counted. An answer that cannot be parsed is kept: production turns it into a scroll, and so does the
score.

## What dev showed (exploratory, 100 dev steps)

Own profile: 10.0% (5.5 to 17.4) of next actions matched; clicks within 50 pixels 10.3% (5.3 to 19.0) of
78, against 1.3% for the average click point and 0.9% for a random point; action type 60% against 92% for
"always click" (34% of the steps were scrolls or typed addresses). No profile: 10.0%, paired difference
0.0 (-5 to +5). Five recruited people agreed on the action type 92% of the time (30 steps). A variant
without production's anti-loop rules (not part of this plan) changed nothing (11%).

## Configuration, code and the gate

- Private configuration: `benchmarks/mimiqbench/configs/web-opera-actions.json`, sha256
  `d1f22aaab570ef4bbc300fa3225ab0bedb12e84d3e43fc1bee2988ba1f4169db`.
- Code hash `f39b3ebe6e179f474f97793e8b74ba5ef5f2c3be13296bbb510d721fd063a1b6` (25 code units: the harness
  files the run uses, the web lane's files, the patch and the panel file); production is pinned by commit
  in the configuration.
- The runner (`benchmarks/web_lab/plan_run.py`, through `benchmarks/mimiqbench/plans.py check`) refuses to
  run unless the GO line names this file's sha256 and the public commit, the configuration's sha256
  matches, the items and sample hash as above, no sample id appears in any earlier cache, and every code
  unit is unchanged (or a deviation is declared and reported).

## Cost and stopping

About $11; cap $12.50, recruiting included. If a cap stops a step, the analysis uses every completed step and reports the
shortfall.

## What we publish whatever happens

Every number above with its interval, including those against Mimiq; the sample and its hashes; every
deviation.
