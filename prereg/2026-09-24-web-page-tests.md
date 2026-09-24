# Plan: web-page-tests, does Mimiq pick the sign-up, giving and page versions that really did better?

Final, 2026-09-24. Written by the web lane from the suite's 4 dev items and dev runs on another page suite;
no model has seen any held-out item, and no held-out picture has been opened. The commit that adds this
file to the public register is its timestamp. Nothing below changes after that; results and deviations go
in RESULTS next to it.

Mimiq keeps its choice of AI models confidential, so this plan names models by role only (the forecast's
model, the people's model, the browsing persona's model, the recruiting model). Their exact identity and
settings are fixed by a private configuration file whose sha256 is below; the run refuses to start if that
file differs by one byte.

## Question

Real, randomized tests of web pages where every version is pictured and the per-version counts are
published: Wikipedia's mobile account-creation form (June 2026) and its post-edit account prompt (July
2026), its 2012 sign-up page redesigns, 2011 donation forms and a banner photo, the 2016 wikipedia.org
language links, and a charity's pledge page (2021). Does Mimiq pick the version that really did better,
checked three ways: the forecast (the compare call), the call as the app shows it (the forecast with the
simulated crowd), and flow mode (simulated people going through a copy of each version in a real
browser)?

## Hypotheses (registered now)

- **H1:** Mimiq's forecast picks the version that really did better on the pictured pairs with a winner
  more often than not: the lower end of the Wilson 95% interval is above 50% (a no-pick counts half).
- **H2:** the same for Mimiq's call (the forecast with the simulated crowd of 25 per version).

Power is very low: the card lists 6 winner pairs in the whole held-out set and 5 or 6 of them have both
versions pictured. With 5, H1 or H2 passes only if all 5 are right. A fail means "not shown", not "shown
wrong". Flow mode has no pass line (below).

## Data

- Suite `page-tests-oa` (CC BY-SA, CC BY and CC0 sources; see its card), held-out: 15 items (13 pairs, 2
  three-version rankings). items.jsonl sha256
  `30791f9e4bb40aa5c84c17c4a602b9e3a70bbe5f69d75c5dc94068721ecc649d`. The sample is held-out positions 1
  to 15; sample ids sha256 `d50585df27283beed941646af4a30ef6541b2b9231052ba25798cb33116a01a9`.
- The page test runs on every held-out pair whose two versions are both pictured (9 pairs by the card's
  count). Left out, and counted: the two rankings and the four pairs with a version the source only
  describes in words (a customer cannot give Mimiq a page as a description).

## Method

- The forecast: the app's compare call on the two pictured versions, both orders, a pick when both orders
  agree, the item's audience line; the call: the same forecast with the simulated people's shift, as the
  app shows it, 25 people per version recruited the app's way from each item's audience line after the GO
  line. Page items go through the page path with the published screenshot as the captured page; the banner
  photo goes through the ad path. Production code is pinned at a fixed commit named in the configuration.
- Flow mode (descriptive; no pass line). Production's flow mode, whole sessions, one browser at a time, on
  local copies of the two pictured versions of these four tests:
  - `wmf2012-acux1-signup-redesign` (the 2012 sign-up page against its redesign), goal line: "You want to
    create a Wikipedia account so that you can edit articles."
  - `wmf2011-donation-form-vs-2010` and the pictured pair of `wmf2011-donation-form-colour-box`, goal line:
    "You clicked a Wikipedia fundraising banner and this page opened. Carry on the way you naturally would."
  - the pictured pair of `gwwc2021-pledge-page`, goal line: "You are reading about Giving What We Can's
    pledge to give part of your income to effective charities. Carry on the way you naturally would."

  Left out of flow mode, and why: the two 2026 tests were mobile screens and flow mode only browses at
  desktop size; the 2012 test with live field checks differs by behaviour a picture cannot show; the
  portal and the banner photo are not flows.
- How a copy is built (after the GO line, by the web lane, from the published picture alone; no outcome is
  read): the picture is the page, pixel for pixel (scaled down to 1,280 pixels wide if wider), with real
  controls laid exactly over the pictured ones: text fields over pictured fields, choices over pictured
  choices, the pictured submit, donate or pledge button as a real submit, other pictured links and buttons
  leading to a plain stand-in page that says it is outside the test. Submitting leads to a stand-in
  conversion page, the same for both versions. The browser may open nothing but the local copy (no real
  site, no real sign-up, no real payment). Each copy's sha256 is reported. If a faithful copy cannot be built
  for a test (for example, the picture does not show the controls), that test is left out of flow mode and
  reported.
- Flow mode people: the first 6 of each item's recruited panel (the product's own flow runs default to 5),
  the same 6 on both versions, up to 10 steps each; a version starts only if its budget covers all 6
  sessions. A version's score is how many reached the conversion page; flow mode picks the version with
  more (equal counts: no pick). Reported with production's own outcome labels for each person.

## Primary metric

Accuracy on the pictured winner pairs, a no-pick counting half; Wilson 95% interval. Code:
`benchmarks/mimiqbench/score.py`, through `benchmarks/web_lab/plan_results.py`.

## Baselines

A coin. No human forecasts exist. The card's base rates: of 17 pairs, 6 winners, 5 unclear, 6 ties.

## Secondary checks

On pictured pairs without a winner: how often the forecast and the call still pick, and how often the call
says "clear"; position bias; for flow mode, conversions per version, production's own outcomes, and each
pick against the real result.

## What dev showed (exploratory)

On the suite's dev banners the forecast made no pick on 3 pairs without a winner and the call said "close"
on all 3 (calibration fine; there is no dev winner). On the 8 GOV.UK organ-donation pages (another suite,
dev only, a famous test that models may remember), the first step of flow mode on local copies ranked the
versions at Spearman 0.86 against real registrations and was right on 83% of 18 winner pairs, while
simulated join rates (10 to 85%) were nothing like the real 2 to 3%; whole sessions ran end to end on the
copies.

## Configuration, code and the gate

- Private configuration: `benchmarks/mimiqbench/configs/web-page-tests.json`, sha256
  `893aed768b01e6bde579114f3e4681cbbcd5d60164a62b6ebe64b281a918787f`.
- Code hash `1c025dd93ac110f86811225ca1088200d652534c5742ed3823dfffee0451e765` (24 code units: the harness
  files the run uses and the web lane's files); production is pinned by commit in the configuration.
- The runner (`benchmarks/web_lab/plan_run.py`, through `benchmarks/mimiqbench/plans.py check`) refuses to
  run unless the GO line names this file's sha256 and the public commit, the configuration's sha256
  matches, the items and sample hash as above, no sample id appears in any earlier cache, and every code
  unit is unchanged (or a deviation is declared and reported).

## Cost and stopping

About $9; cap $11.50, recruiting included (forecast $0.30, call $4.50, flow mode $5.20 at most). If a cap stops a
step, the analysis uses every completed item and reports the shortfall; a flow pair missing a version makes no pick.

## What we publish whatever happens

Every number above with its interval, including those against Mimiq; the sample and its hashes; each
copy's hash; every deviation.
