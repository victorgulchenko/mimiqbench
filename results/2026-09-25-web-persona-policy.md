# Results: web-persona-policy, after the persona fix, do flow personas act more like real shoppers, and does the profile matter?

Plan `benchmarks/mimiqbench/prereg/final/web-persona-policy.md` (sha256 `f2dbfc3d6307b7acdfc94355979e2c1055a1428bebd863071ba12ad8ddf8dd2e`), opened by the GO line with public commit https://github.com/victorgulchenko/mimiqbench/commit/598ba831adf210044ae66d729619e059914c9c2d. Configuration sha256 `4c509b5f23f418bf1335fc2d5f558635f56594167aabaf35689a0fff076f8c4d`; code hash `54b5be2ba9249c23e79d7b786a7008032c0ab1d3bf23a549aeff56df76efc850`; production pinned at commit `ed311627` with the two registered patches (its backend is identical, file for file, to production at `1155c1d0`, where the two patches went live).

Deviations: none declared. The gate passed before every step. Sample: 200 steps, sha256 of their action ids (one per line) `0c5d9fcff07b40437ce42d8d11ce937eec12ffa983f1b620f6625db9fa98e9d1`.

## Read this first

Of the six registered lines, two passed (H2, H5) and four failed (H1, H3a, H3b, H4). Development had predicted that H3a and H4
would fail; it had predicted that H1 and H3b would pass, and they failed.

- **H1 failed: the revised decision (v2) did not match real shoppers more often than today's decision.** Both did what
  the shopper did next on 9.5% of 200 fresh steps (19 each; 14 against 14 discordant steps; difference 0.0 points, 90%
  interval -3.3 to +3.6). Development had shown +8.5 points (95% interval +2.8 to +14.7); that gain did not survive a
  fresh test. By kind of action, v2 gained where carrying on matters (typing into the search box, 0 to 5 of 20; product
  options, 0 to 2 of 17) and lost where committing matters (submitting a search, 7 to 2 of 31; adding to the cart, 7 to
  2 of 15). This split is read after the run, not registered.
- **H2 passed: v2 typed no web address** on any of the 200 steps (Wilson upper bound 1.9%), against 12.0% (24 of 200)
  for today's decision. Real shoppers in these logs never do.
- **The profile did not help and may slightly hurt (H3a and H3b failed).** Under v2 the shopper's own profile matched
  9.5% against 12.0% with no profile (-2.5 points; 5 against 10 discordant; 90% interval -5.4 to +0.6). The interval
  crosses the registered -5 point bound, so "no harm" is not shown either. Development had predicted H3a would fail.
- **People still act alike (H4 failed):** five people on the same step, when both acted, chose a different kind of
  action 20.7% of the time (line: 30%). Real shoppers of the held-out sessions in the same kind of situation differ 69.9%
  of the time. Development had predicted this failure.
- **Flows keep their usability value (H5 passed), with a shortfall:** on the sign-up test page 4 of 5 people finished and
  3 of 5 named the dead "Go to Dashboard" button; on the GOV.UK copy both people who pressed Join completed the register
  form. The sign-up page's budget stopped the run before one person's first answer and before another's summary (below).
- **A simple rule beat every simulated arm:** repeating the shopper's previous action matches their next action on 17.0%
  (12.4 to 22.8) of the same 200 steps (not registered as a line; listed in the plan as context). The same happened in the
  earlier plan on different sessions (13.5% against 8.0%).

## Verdicts

| Hypothesis | Verdict | Result |
|---|---|---|
| H1 v2 with the own profile does what the shopper did next more often than today's decision (one-sided exact p < 0.05 and 90% lower bound above 0) | FAIL | 9.5% against 9.5%; 14 vs 14 discordant; one-sided p 0.57; difference 0.0, 90% interval -3.3 to +3.6 (95% -3.9 to +4.4) |
| H2 v2 types a web address on almost no step (Wilson 95% upper bound below 3%) | PASS | 0 of 200; upper bound 1.9% (today's decision: 24 of 200, 12.0%) |
| H3a under v2 the own profile matches more often than no profile (one-sided exact p < 0.05) | FAIL | 9.5% against 12.0%; 5 vs 10 discordant; one-sided p 0.94 |
| H3b under v2 own profile and no profile are equivalent (90% interval inside +/-5 points) | FAIL | difference -2.5 points, 90% interval -5.4 to +0.6 |
| H4 five people under v2, when both act, choose a different kind of action at least 30% of the time | FAIL | 20.7% over 20 steps (with scrolling counted as a kind: 23.5%) |
| H5 sign-up: at least 4 of 5 finish and at least 3 of 5 name the dead button; GOV.UK copy: at least 80% of those who press Join complete the form | PASS | 4 of 5 finished, 3 of 5 named it; 2 of 2 who pressed Join completed the form (3 of 5 left without pressing Join) |

## Every number (held-out, 200 steps; intervals Wilson 95% unless stated)

| | A: today's decision, own profile | B: v2, own profile | C: v2, no profile |
|---|---|---|---|
| did what the shopper did next (registered rule) | 9.5% (6.2% to 14.4%) | 9.5% (6.2% to 14.4%) | 12.0% (8.2% to 17.2%) |
| ... the earlier plan's rule (keyboard submits scored by point) | 9.0% | 9.5% | 12.0% |
| right action type (click, type, leave) | 55.0% | 55.5% | 59.5% |
| click within 50 px of the shopper's (135 clicks on screen) | 8.1% | 8.9% | 10.4% |
| ... within 25 px / 100 px | 6.7% / 10.4% | 5.2% / 13.3% | 8.1% / 16.3% |
| picked the shopper's element from the list (188 clicks and entries) | 8.0% | 4.3% | 6.4% |
| typed a web address | 12.0% | 0.0% | 0.0% |
| scrolled | 17.0% | 27.0% | 26.0% |

The shoppers' own actions on these steps: 168 clicks (16 of them keyboard submits), 20 text entries, 12 session ends.
Baselines on the same steps: always click 84.0% for the action type; repeat the previous action 17.0% (12.4% to 22.8%).

Did what the shopper did next, by the shopper's kind of action (A / B / C, counts): search submit 7 / 2 / 4 of 31; reviews 2 / 3
/ 5 of 24; typing a search 0 / 5 / 4 of 20; product link 1 / 1 / 2 of 18; product option 0 / 2 / 1 of 17; related items 0 / 1 / 1
of 16; add to cart or buy 7 / 2 / 3 of 15; site menu 0 / 0 / 0 of 14; leaving 0 / 1 / 2 of 12; other 1 / 1 / 1 of 12; cart 0 / 1 / 0
of 7; quantity 1 / 0 / 1 of 6; suggested search 0 / 0 / 0 of 4; filters 0 / 0 / 0 of 4.

## Secondary checks (no pass line)

- H1 and H3 on the 77 steps of the 12 shoppers no earlier run had seen: v2 own 7.8%, today's decision 10.4%, v2 no profile
  10.4% (v2 own minus today's -2.6 points, 90% interval -6.7 to +2.7).
- H4 counting every pair of the five (scrolls included as a kind): 23.5%. The real between-shopper variety recomputed on the
  held-out pool: 69.9% (1,136 steps; development 60.5%).
- Scrolling, v2 against today's: +10.0 points (95% interval +4.2 to +18.5); registered as bad news.
- The end-of-session summaries of arm E are listed below.

## Arm E: whole live sessions under v2 (one browser at a time, local pages only)

Sign-up test page (three screens; the final "Go to Dashboard" button does nothing):

| Person | Finished | Named the dead button | Steps | Typed an address |
|---|---|---|---|---|
| 1 | yes | yes | 9 | no |
| 2 | yes | yes | 14 | yes (a guessed dashboard address, after the dead button) |
| 3 | yes | yes | 14 | yes (the same) |
| 4 | yes | no summary (stopped by the budget) | 14 | no |
| 5 | no (stopped by the budget before any answer) | no summary | 14 | no |

GOV.UK organ-donation copy (version C): 2 of 5 pressed Join and both completed the register form in 3 steps; 3 of 5 ended the
visit on the "Thank you" page (the real test's registration rate was 2 to 3%).

End-of-session summaries, as written by the simulated people (dashes replaced by commas; nothing else changed):
- Sign-up 1: "I got all the way through signup feeling pretty good about TaskFlow, and then hit a wall at the finish line, the 'Go to Dashboard' button just doesn't work, which is honestly unacceptable for a product trying to onboard new users. I can't recommend something I've never actually gotten into, and I'd be hesitant to trust a tool with my team's work if the signup flow is this broken."
- Sign-up 2: "I went through the whole signup process twice and still never made it into the actual product, the 'Go to Dashboard' button is completely non-functional and there's zero feedback to tell you something went wrong. For a task management tool trying to win over new users, failing at the literal last step of onboarding is a trust-killer. I wouldn't bother coming back unless someone told me it was fixed."
- Sign-up 3: "I jumped through every hoop TaskFlow asked me to, filled out the forms twice, and still never got into my workspace because the final button just doesn't work. It's genuinely baffling, the onboarding felt polished right up until the moment it completely fell apart. I wouldn't trust this product with my actual work data if it can't even get me through the front door."
- Sign-up 4 and 5: no summary (the budget stopped their sessions).
- GOV.UK 1: "Well I came on to pay my vehicle tax and ended up on the organ donor register, which is something I'd been meaning to do for ages but never got round to. The whole thing took barely any time and everything was clear and easy to follow. I'm really glad the prompt was there - it's a clever place to put it when you've got people's attention."
- GOV.UK 2: "Really pleased with how that went - paid my car tax, saw the organ donor prompt and thought why not, and it was done in minutes. It's the kind of thing where the government has actually made it easy to do something good, which doesn't always happen. The only tiny niggle was a possible name truncation issue but it seemed to sort itself out."
- GOV.UK 3: "Did what I came to do - vehicle tax is paid, happy days. The organ donor thing at the end is a bit random but I'm already registered so it didn't bother me. GOV.UK generally does the job without too much faff, which is all you want from a government website really."
- GOV.UK 4: "Job done, road tax is paid and that's what I came for. The organ donor thing at the end was a bit random - I'm already registered I think, but even if I wasn't, I wouldn't want to deal with that straight after sorting my car tax. GOV.UK generally does what it needs to do, I'll give it that."
- GOV.UK 5: "Did what I needed to do - car tax is sorted, job done. The organ donor thing at the end was a bit random and I ignored it, I'm already registered anyway. GOV.UK generally does what it needs to, it's not pretty but it works."

## Deviations and operational notes

- No frozen file changed; no deviation was declared.
- **Shortfall (arm E):** the sign-up page's share of the arm budget ($1.20, as the runner's own commands set it) ran out
  during the fourth person's session: 24 model calls were refused. Person 4 had already pressed "Go to Dashboard" (counted as
  finished, as the registered code counts it) but got no summary; person 5 got no model answer at all (every step fell back to
  a scroll) and counts as not finished. H5's counts are over all five, as registered.
- Arm E used fresh model calls only: the development sessions' answer cache was moved aside for the run.
- Five of the twelve never-seen shoppers have no survey answers in the dataset (18 of the 200 steps). Recruited the registered
  way, all five got the same generic person from the empty description. Without those 18 steps: v2 own against today's 9.3%
  against 9.3%; own against no profile 9.3% against 11.5% (-2.2, 90% interval -5.3 to +1.4). Not registered.
- Production moved on after the plan (a later commit changed two action guards: a text box among several form fields is no
  longer taken for a chat box, and the guard's note left the person's thoughts). Replayed offline through that later code
  (same requests, answered from this run's own cache), 0 of the 700 decisions change. These results hold for production as
  deployed at the time of writing.
- Disclosed in the plan, repeated here: before any GO line, one secondary statistic (the real between-shopper variety) was
  computed in memory over the held-out pool while the analysis code was tested; it was not seen. It is reported above as
  computed after the GO line.

## Cost

$14.78 of the plan's $17 cap: recruiting $0.04; A $4.30; B $3.66; C $3.49; D $1.91; E $1.37.
