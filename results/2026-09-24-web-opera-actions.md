# Results: web-opera-actions: do Mimiq's browsing personas do what real shoppers do next?

Plan `benchmarks/mimiqbench/prereg/final/web-opera-actions.md` (sha256 `d8af19eba2e3dd1b116e34314273055be58735e26307a5a2450dfe1ef59cdd48`), opened by the GO line with public commit https://github.com/victorgulchenko/mimiqbench/commit/1b4920aafa114bfd0648fdc0b3e2ebf8ffec9c39. Configuration sha256 `d1f22aaab570ef4bbc300fa3225ab0bedb12e84d3e43fc1bee2988ba1f4169db`; code hash `f39b3ebe6e179f474f97793e8b74ba5ef5f2c3be13296bbb510d721fd063a1b6`; production pinned at commit `b490cea57f90`.

Deviations: none declared.

## Read this first (added by hand after the analysis; every number from the run files)

- All five registered lines passed. Three of them (H2, H4, H5) are the bad news registered as such: the persona did what the
  shopper did next on 8.0% (5.0 to 12.6) of 200 held-out steps; its action type was right 55.5% against 81.5% for "always
  click"; five different recruited people chose the same action type 92% of the time.
- H1 passed against the fixed dev average point, but **not against the registered baseline that matters most**: the average
  click point of the other held-out steps lands within 50 px of the shopper's click on 7.8% of the 128 clicks, and the
  persona's 9.4% is not distinguishable from it (paired exact McNemar, 11 against 9 discordant, p 0.82). Most of that
  baseline's hits are repeated clicks in the review photo viewer. Read H1 as "better than a fixed guess made on dev", not
  "better than a trivial guess".
- Not registered (the suite card's dev baseline, reported for context): repeating the shopper's previous action matches their
  next action on 13.5% (9.4 to 18.9) of the 200 steps, more than the persona's 8.0% (16 against 27 discordant, p 0.13).
- The shopper's own profile made no difference (H3): -0.5 points against no profile (90% interval -3.0 to +2.0).

## Verdicts

| Hypothesis | Verdict | Result |
|---|---|---|
| H1 the persona's click lands on the shopper's target more often than the fixed average click point | PASS | 9.4% against 0.8% of 128 clicks; one-sided McNemar p 0.00049 (11 vs 0 discordant) |
| H2 the persona does what the shopper did next in fewer than one step in four (upper 95% bound below 25%) | PASS | 8.0% (5.0% to 12.6%) of 200 steps |
| H3 the shopper's own persona and no persona match equally often (90% interval of the difference inside +/-5 points) | PASS | difference -0.5 points, 90% interval -3.0 to +2.0, 200 steps |
| H4 the persona's action type is right less often than always saying "click" | PASS | 55.5% against 81.5%; one-sided McNemar p 3.1e-15 |
| H5 five different recruited people agree on the action type at least 80% of the time | PASS | 92.0% over 30 steps; clicks within 50 px of each other 57.1% |

## Every number (held-out)

| | Own persona | No persona | Panel of five (first 30 steps) |
|---|---|---|---|
| did what the shopper did next | 8.0% (5.0% to 12.6%) (n 200) | 8.5% (5.4% to 13.2%) (n 200) | 6.0% (1.6% to 20.4%) (n 30) |
| right action type | 55.5% (48.6% to 62.2%) (n 200) | 58.0% (51.1% to 64.6%) (n 200) | 39.3% (24.0% to 57.0%) (n 30) |
| click within 50 px of the shopper's | 9.4% (5.4% to 15.7%) (n 128) | 8.6% (4.9% to 14.7%) (n 128) | 9.5% (2.5% to 30.1%) (n 19) |
| ... when it clicked | 14.3% (8.4% to 23.3%) (n 84) | 12.4% (7.0% to 20.8%) (n 89) | 9.1% (1.6% to 37.7%) (n 11) |
| right type when it did not scroll or navigate | 82.8% (75.6% to 88.3%) (n 134) | 86.6% (79.8% to 91.3%) (n 134) | 85.7% (60.1% to 96.0%) (n 14) |
| picked the shopper's element from production's list | 4.8% (2.5% to 8.8%) (n 188) | 5.9% (3.3% to 10.2%) (n 188) | 0.0% (0.0% to 12.5%) (n 27) |
| scrolled, navigated or waited | 33.0% (26.9% to 39.8%) (n 200) | 33.0% (26.9% to 39.8%) (n 200) | 53.3% (36.1% to 69.8%) (n 30) |

Actions chosen, own persona: {'click': 129, 'navigate': 39, 'scroll_down': 19, 'scroll_up': 8, 'type': 4, 'fill_form': 1}; no persona: {'click': 132, 'navigate': 44, 'scroll_up': 11, 'scroll_down': 11, 'type': 2}; panel: {'navigate': 74, 'click': 70, 'scroll_down': 6}.
Median distance from the shopper's click: own 394 px, no persona 396 px.
Panel: any of the five did what the shopper did: {"1": "3.3%", "2": "6.7%", "3": "6.7%", "4": "6.7%", "5": "6.7%"}.

Baselines on the same steps: the shoppers' own action types {"click": 163, "terminate": 12, "input": 25}; always click 81.5%; a random point on the screen 0.9%; the average click point of the other steps 7.8%; a random listed element 1.5%; the shopper's target was in production's element list on 49.5% of clicks and inputs.

## Secondary checks (no pass line)

- Clicks within 25 px: own 8.6% (4.9% to 14.7%), no persona 7.8%; within 100 px: own 13.3% (8.5% to 20.2%), no persona 12.5%.
- Own persona, did what the shopper did, by the shopper's kind of action: review 16.3% of 43; input 4.0% of 25; product_link 0.0% of 22; product_option 9.1% of 22; search 12.5% of 16; terminate 0.0% of 12; nav_bar 0.0% of 12; suggested_term 22.2% of 9; other 0.0% of 8; quantity 12.5% of 8; purchase 14.3% of 7; filter 0.0% of 5; cart_side_bar 0.0% of 5; cart_page_select 0.0% of 4; page_related 0.0% of 2.
- Typed text against the shopper's search words (word overlap, own persona, text-entry steps): 0.0.

## Deviations and operational notes (added by hand)

- No frozen code unit changed; the gate passed before every step and no deviation was declared.
- The header's plan sha256 and public commit were filled in by hand: the results writer read the wrong key names from the GO
  gate and printed "?".
- Production code was the snapshot of the pinned commit (b490cea5), as registered. Production now runs flows from a later
  commit (4b3fc019); this run does not cover those changes. The snapshot lacked files git does not track (the persona pool the
  recruiting draws from, the backend's local environment file and one context module); they were linked from the working
  tree, the same files every dev run used. The first preparation attempt stopped at recruiting for that reason, after one
  recruiting call; the rerun recruited all 13 held-out shoppers (age and gender match their surveys in 13 of 13).
- The recruiting helpers the harness compiles from the server file were byte-identical between the pinned commit and the
  working tree (checked).
- For context only (a different protocol: text pages, the full test split): the dataset paper's text-only model baselines
  scored 8.3% to 21.5% on the exact next action.

## Spend

$11.54 of the plan's $12.50 cap (ledger lane `web`).

