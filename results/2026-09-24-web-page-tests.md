# Results: web-page-tests: does Mimiq pick the sign-up, giving and page versions that really did better?

Plan `benchmarks/mimiqbench/prereg/final/web-page-tests.md` (sha256 `ddfdf1224ab2dc270b7c54adf33051d4054558ef17408925ec77c9669cd351f7`), opened by the GO line with public commit https://github.com/victorgulchenko/mimiqbench/commit/1b4920aafa114bfd0648fdc0b3e2ebf8ffec9c39. Configuration sha256 `893aed768b01e6bde579114f3e4681cbbcd5d60164a62b6ebe64b281a918787f`; code hash `1c025dd93ac110f86811225ca1088200d652534c5742ed3823dfffee0451e765`; production pinned at commit `b490cea57f90`.

Deviations: none declared.

## Read this first (added by hand after the analysis; every number from the run files)

- **H1 and H2 failed.** The forecast and the call (forecast plus crowd) each picked the real winner on 4 of the 5 pictured
  winner pairs: 80.0% (37.6 to 96.4). With 5 winners only a clean sweep could pass; read it as "not shown".
- The miss is the most recent test: Wikipedia's July 2026 post-edit account prompt, run after the models' training data. The
  forecast picked the version that lost in both orders, and the call followed it ("leaning"). The June 2026 account form, also
  recent, was right. The three other right answers are tests from 2012 and 2016 that have been public for years.
- Said as loudly: on these 5 winner pairs the new version (the redesign) won every time, so the rule "pick the new version"
  was right on 5 of 5 (a rule chosen on these same items, so it flatters itself; the harness's scorer reports it), against
  Mimiq's 4 of 5. On these tests Mimiq did not beat the simplest guess a team would make.
- On the 2 pictured pairs with no real difference (ties) the forecast still picked both times; the call said "leaning", never
  "clear". The call's "clear" was right on 3 of 3 winners.
- **Flow mode could not tell versions apart.** On the 2012 sign-up test (a clear real winner, the redesign), all 6 people reached
  the account-created page on both versions; on the donation form test (a real tie), all 6 donated on both. Flow mode showed
  that both versions work; it did not rank them.
- **Production bug found by this run:** production's own outcome labelled all 12 of those successful sign-ups "bounced", with
  the canned summary "I tried to continue, but the site blocked me with a verification step". The block detector
  (`_detect_antibot_verification_block` in e2e_heuristics.py) matches the words "captcha" and "security check" in a step's
  target text, so any sign-up form with a CAPTCHA or security-check field is reported as blocking people even when every
  person completed it. It is still in today's production commit (4b3fc019).

## Verdicts

| Hypothesis | Verdict | Result |
|---|---|---|
| H1 Mimiq's forecast picks the version that really did better on the pictured pairs with a winner (Wilson 95% lower end above 50%) | FAIL | 80.0% (37.6% to 96.4%) of 5 winner pairs; picks 100.0% |
| H2 Mimiq's call (forecast and crowd) picks the version that really did better on the pictured pairs with a winner (Wilson lower end above 50%) | FAIL | 80.0% (37.6% to 96.4%) of 5 winner pairs; picks 100.0% |

## Every number (held-out)

- forecast: items 9, excluded {}; ties {"n": 2, "pick_rate": 1.0, "pick_rate_ci95": [0.34238, 1.0], "agrees_with_leader_when_picks": 0.5}; unclear {"n": 2, "accuracy": 0.5, "ci95": [0.094531, 0.905469], "note": "agreement with the observed leader where the real difference is not significant (secondary)"}; by tier null
- call: items 9, excluded {}; ties {"n": 2, "pick_rate": 1.0, "pick_rate_ci95": [0.34238, 1.0], "clear_rate": 0.0, "clear_rate_ci95": [0.0, 0.65762], "agrees_with_leader_when_picks": 0.5}; unclear {"n": 2, "accuracy": 0.5, "ci95": [0.094531, 0.905469], "note": "agreement with the observed leader where the real difference is not significant (secondary)"}; by tier {"clear": {"n": 3, "accuracy": 1.0, "ci95": [0.438503, 1.0], "share": 0.6}, "leaning": {"n": 2, "accuracy": 0.5, "ci95": [0.094531, 0.905469], "share": 0.4}}

## Flow mode (descriptive; no pass line)

| Test | Version | People | Reached the conversion page | Production's own "converted" |
|---|---|---|---|---|
| wmf2012-acux1-signup-redesign | A | 6 | 6 | 0 |
| wmf2012-acux1-signup-redesign | B | 6 | 6 | 0 |
| wmf2011-donation-form-vs-2010 | A | not run | | |
| wmf2011-donation-form-vs-2010 | B | not run | | |
| wmf2011-donation-form-colour-box | A | 6 | 6 | 6 |
| wmf2011-donation-form-colour-box | B | 6 | 6 | 6 |
| gwwc2021-pledge-page | A | 6 | 5 | 6 |
| gwwc2021-pledge-page | B | not started | | |

- wmf2012-acux1-signup-redesign: flow mode's pick none (equal); real outcome clear, winner B: no pick.
- wmf2011-donation-form-vs-2010: **not run** (by hand: the frozen writer prints this row as if run). No faithful copy could be built: the 2010 form is pictured only as a 351 x 230 crop of the form box, while its rival is the whole page. Real outcome: tie.
- wmf2011-donation-form-colour-box: flow mode's pick none (equal); real outcome tie, winner none: no real winner.
- gwwc2021-pledge-page: no pick because version B (the original three-box page) **never started** (by hand): version A's six sessions cost $0.72, and the registered rule starts a version only if $0.10 per session for all 6 fits in the pair's $1.20. A pair missing a version makes no pick, as registered. Real outcome: unclear (no winner). On A, 5 of 6 people clicked "Take The Pledge"; its other pledges are pictured as links, which the protocol counts as leaving.

## Deviations and operational notes (added by hand)

- No frozen code unit changed; the gate passed before every step and no deviation was declared.
- The header's plan sha256 and public commit were filled in by hand: the results writer read the wrong key names from the GO
  gate and printed "?".
- Flow table versions: sign-up test A = the 2012 page, B = the redesign; donation form A = white box, B = green box; pledge page
  A = the separate block, B = the original three boxes. Copies (sha256 of each version's page, picture and control spec):
  wmf2012-acux1-signup-redesign: current `128edc2ff9be28d1...`, redesign `c3ac1f53c8262b5d...`; wmf2011-donation-form-colour-box: white_low `2b433417bccea0a4...`, green_low `78b8dc40ebadb7a7...`; gwwc2021-pledge-page: separate_block `3696df95c456f272...`, original `a3cadbbd9211e8a8...`.
- Production code was the snapshot of the pinned commit (b490cea5), as registered. Production now runs flows from a later
  commit (4b3fc019); this run does not cover those changes (the block detector above is unchanged there). The snapshot lacked
  files git does not track (the persona pool, the backend's local environment file, one context module); they were linked from
  the working tree, the same files every dev run used. The ad path and recruiting helpers the harness compiles from the server
  file were byte-identical between the pinned commit and the working tree (checked).
- Flow sessions ran one browser at a time with the local environment flag set, so production's address guard would let the
  browser open the local copy; the guard itself was replaced for these sessions by one that allows only the local copy (no real
  site could be reached).

## Spend

$6.70 of the plan's $11.50 cap (ledger lane `web`).


## Update after the run

- 2026-09-24: the block-detector bug this run found is fixed in production (a session that ends in "done" on a page that shows no block is no longer reported as blocked).
