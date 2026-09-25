# Plan: web-persona-policy, after the persona fix, do flow personas act more like real shoppers, and does the profile matter?

Draft, 2026-09-24, persona lane. Written from 400 development steps only; no model has seen any held-out step,
and the held-out sessions were set aside by their ids before any page, action or outcome of theirs was read. The
commit that adds this file to the public register is its timestamp. Nothing below changes after that; results and
deviations go in RESULTS next to it.

Mimiq keeps its choice of AI models confidential, so this plan names models by role only (the browsing persona's
model, the recruiting model). Their identity and settings are fixed by a private configuration file whose sha256 is
below; the run refuses to start if that file differs by one byte.

## Question

Mimiq's flow mode sends simulated people through a website in a real browser. An earlier plan (W1, same data
source, different sessions) found that at each step the simulated person did what the real shopper did next only
8.0% of the time, typed a web address on about one step in five (real shoppers never do), and that giving the person
the shopper's own profile changed nothing. A revised decision prompt ("policy v2") drops the rules that caused the
typed addresses, states what recorded sessions show people do, and asks for the person's current intent before the
action. This plan asks, on fresh held-out steps: does v2 do what real shoppers do next more often than today's
decision; does it stop typing addresses; does the person's own profile make it match the shopper more often; do
different simulated people differ the way real people do; and do flows still finish tasks and still find a broken
button?

## Hypotheses (all registered now)

- **H1 (the fix works):** on the same steps, v2 with the shopper's own profile does what the shopper did next more
  often than today's decision with the same profile. Passes if its rate is higher, a one-sided exact test on the
  steps where only one of them matches gives p < 0.05, and the lower end of the 90% bootstrap interval of the
  difference (resampling shoppers) is above 0.
- **H2 (no typed addresses):** v2 types a web address on almost no step: the upper end of the Wilson 95% interval of
  its rate is below 3%. Real shoppers in these logs never do.
- **H3a (the profile helps, the founder's criterion):** under v2, the shopper's own profile does what the shopper did
  next more often than no profile: one-sided exact test on the discordant steps, p < 0.05. The margin is 0 on
  purpose: on development data even a perfect record of each shopper's own habits, taken from their other sessions,
  added nothing to predicting the next kind of action once the page and the previous action were known (-0.1
  points, 95% interval -1.8 to +1.6), so any reliable gain would count. Development predicts this fails.
- **H3b (the profile does no harm):** under v2, own profile and no profile match the shopper equally often: the 90%
  bootstrap interval of the paired difference (resampling shoppers) lies inside minus 5 to plus 5 points.
- **H4 (people differ like real people, the founder's criterion):** five different recruited people under v2, on
  the same step, when two of them both act (click, type or leave), choose a different kind of action at least 30%
  of the time. Real shoppers in the same kind of situation (same page type, same previous kind of action) choose a
  different kind 60.5% of the time on development data (53.4% when the previous element clicked is also the same);
  that is an upper bound for the same page, so the line is set at about half of it. Development predicts this fails:
  11% for five people under today's decision, 13% under v2 with explicit habits (a variant not adopted), and a person
  with and without their profile under v2 differed in 16% of the steps where both acted.
- **H5 (flows keep their usability value):** whole live sessions under v2 on two local test pages: (a) a three-screen
  sign-up whose final "Go to Dashboard" button does nothing: at least 4 of 5 people finish the sign-up (reach the
  final screen and press that button) and at least 3 of 5 name the dead button in their own end-of-session summary;
  (b) a local copy of the GOV.UK organ-donation "Thank you" page (version C) with a working register form: of the
  people who press Join, at least 80% complete the form.

## Data

- OPeRA (Wang et al., 2025, arXiv 2506.05606; data CC BY 4.0): 51 real people shopping on a large online store in
  their own browsers in 2025, with their own survey answers; a plug-in logged each page (as simplified HTML), a
  viewport screenshot, the mouse position and every click, text entry and session end. 527 sessions, 5,856 actions.
- W1 used 200 steps from 75 sessions; those sessions are spent and appear nowhere in this plan, dev or held-out.
- **Held-out pool, set aside from session and user ids only, before any of its pages, actions or outcomes was
  read:** every session of the 12 users who had no step in any earlier run (40 sessions, 402 actions) plus a seeded
  30% of the other sessions that held no earlier step (ranked by sha256 of the seed and the session id): 140
  sessions, 1,148 actions, 41 users. Session list sha256
  `f4d595038a839e4d4b028ce5b078194184b4a46186e4021de161edf8d9e111ef` (the ids sorted, one per line); the split
  file (`benchmarks/persona_lab/data/split.json`) sha256 `703ab30b56b0b0af41fdb882e055fd25b56527a82bf4d3c860707f5de14f8771`.
- **The sample, by rule:** every action of the held-out sessions, ranked by sha256 of `persona-w3-20260924|sample|`
  followed by its action id; the first 200. H4 uses the first 20 of those. The sample's action ids and their
  sha256 are computed by the runner right after the gate passes, from the registered session list only, and printed
  in the results.
- Development data (never the held-out pool): the other 312 sessions (3,799 actions, 38 users), split by user into
  a tuning half and a checking half; 400 development steps were run.

## What the simulated person sees, and whose code decides

- The decision is production's own: the live flow loop's decision (step message, hints, model call, parsing,
  normalization and action guards) made callable on a stored page state by a behaviour-preserving patch, with the
  policy patch on top. Production is pinned at the commit named in the configuration with the two patches (sha256
  in the configuration) applied; that snapshot is what the run imports. Today's decision is the same snapshot with
  the policy switch set to v1, which a test shows sends byte-identical requests to the code before the patches.
- The page state, as in W1: the page's address; the real screenshot resized to the flow browser's width, cut at its
  height and encoded as production encodes its own screenshots (steps without a screenshot are decided without one);
  the list of clickable elements emulated on the stored page with production's own rules; the shopper's earlier
  actions in the session as production's journey; the step number and the time since the session began.
- The goal line, the same for every step and person: shopping on that store for themselves, continuing the session
  the way they normally would (exact words in the configuration).
- People: (1) **own profile**: one person recruited the app's way from the shopper's own survey answers (people
  already recruited from the same survey text with the same seed are reused; the others are recruited after the
  GO line); (2) **no profile**: production's defaults; (3) **panel**: the five people W1 recruited from a one-line
  description of the dataset's population.
- Arms on the same 200 steps: **A** today's decision, own profile; **B** v2, own profile; **C** v2, no profile.
  **D** v2, the panel of five, first 20 steps. **E** whole live sessions under v2 on the two local test pages
  (5 people each, from the panels named in the configuration), in a real browser that may open only the local copy.
- Scoring, as in W1 with one registered correction. A click counts as the shopper's click when it lands within 50
  pixels of the shopper's click point. Correction: a click the log records at the screen's corner (0, 0) is a
  keyboard submit (pressing Enter in the search box), not a pointer; it is scored as W1 scores clicks without a
  screenshot, by the element (the simulated person must pick the shopper's element). This affects 9% of development
  clicks and 9 of W1's 163; W1's rule is reported as a secondary. Text entries are right if they go into the element
  the shopper typed into; ending the session is right if the shopper ended it; scroll, back, typed address, wait and
  checking email never appear next in the log, so they count as wrong.
- Kind of action, for H4: the element's name in the log, mapped to the dataset's own kinds of click (reviews,
  product options, search, cart, and so on) by a map learned on development logs only; typing and leaving are kinds
  of their own.

## Primary metrics and pass lines

As in the hypotheses. H1 and H3: exact next-action match, paired over the same steps, exact one-sided test on the
discordant steps, and a bootstrap over shoppers (5,000 rounds, seed 11) for intervals. H2: Wilson interval. H4: mean
over steps of the share of pairs of the five people, both acting, with different kinds. H5: counts.

## Baselines

Today's decision on the same steps (arm A); for context, "always click" for the action type, and the rule "repeat
the shopper's previous action" (13.5% on W1's held-out steps, 17% on the dataset's development items).

## Secondary checks (reported, no pass line)

W1's scoring rule for H1; action-type accuracy; how often each arm scrolls (development: v2 scrolls on 35% of steps
against 17.5% for today's decision, registered here as bad news); clicks within 25 and 100 pixels; exact match by the
shopper's kind of action; H1 and H3 on the 12 never-seen users' steps alone; H4's share with scrolls counted as a kind;
the real between-shopper variety of H4 recomputed on the held-out pool; the text of every end-of-session summary in E.

## What development showed (exploratory, 400 steps, 37 users)

- Today's decision matched the shopper's next action on 8.0% of 200 development steps; v2 on 16.5% (paired difference
  +8.5 points, 95% interval +2.8 to +14.7, 23 against 6 discordant steps). On the checking half, never used for tuning:
  8.0% against 20.0% (+12.0, +2.3 to +20.8).
- Typed web addresses: today's decision 20.5% of steps, v2 0 of 300 decisions.
- Own profile against no profile under v2 (checking half): -2.0 points (95% interval -7.6 to +3.3).
- On real shoppers, who the person is barely predicts the next action once the situation is known: the kind of action
  is predicted equally well with or without each shopper's own habits from their other sessions; survey answers
  predict habits only weakly (for example "I usually research a lot" against the share of review clicks: rank
  correlation 0.13).
- Five recruited people on the same step, when both act, chose a different kind of action 11% of the time under
  today's decision and 13% under v2 with explicit habits (v2 as registered here was not run with five people on
  development). Tried and not adopted: explicit habits from the profile (no gain, and they did not make
  people differ); drawing each move from the person's own list of likely moves (more variety, mostly between
  scrolling and clicking; 17% when both act; per-person accuracy lower).
- Live sessions under v2 (development): on the sign-up page 2 of 2 people finished and both named the dead button (under
  today's decision 2 of 2 finished, and the one person whose session reached its summary named it; both also typed a
  web address after the dead button); on the GOV.UK copy 2 of 2 pressed Join and completed the form.

## Configuration, code and the gate

- Private configuration: `benchmarks/mimiqbench/configs/web-persona-policy.json`, sha256
  `4c509b5f23f418bf1335fc2d5f558635f56594167aabaf35689a0fff076f8c4d`.
- Code hash `54b5be2ba9249c23e79d7b786a7008032c0ab1d3bf23a549aeff56df76efc850` (29 files: the runner and scorer, the
  harness files it imports, the two patches, the people files and the local test pages).
- The runner (`benchmarks/persona_lab/w3.py`) refuses to read any held-out row unless the GO line
  `opera-persona-w3 <this file> <its sha256> <public commit URL>` is present, this file and the configuration are
  committed and unchanged, the configuration's sha256 and the session-list sha256 match the ones above, every frozen
  file is unchanged (or a deviation is declared and reported), and this file names no model.
- Disclosed: before any GO line, while its analysis code was tested on development steps, the runner computed one
  secondary statistic (the real between-shopper variety of H4) over the held-out pool's logged kinds of action. The
  value was not printed, saved or seen, no model saw any held-out row, and no pass line depends on it; that code now
  runs on held-out rows only after the GO line.

## Cost and stopping

About $15; cap $17, recruiting included (arm caps A $4.80, B $4.40, C $4.20, D $2.10, E $1.50). If a cap stops an arm,
the analysis uses every completed step present in all three of A, B and C and reports the shortfall.

## What we publish whatever happens

Every number above with its interval, including those against Mimiq; the sample's ids and their hash; every
end-of-session summary from E; every deviation.
