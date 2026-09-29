# Results: headlines, can a cheaper candidate model take over the forecast? (H4)

Plan `prereg/2026-09-29-headlines-candidate-forecast.md` (sha256
`0ba3fc25e232acf3f17b907d0017701a275b2659d84c45aff5bc402d92e5482c`), pushed in commit
https://github.com/victorgulchenko/mimiqbench/commit/1e416ec8389d77065fe43960d1c4d741e95e5054
before any held-out pair was sent to the candidate. Every held-out call carries that sha256 and its
UTC time. Models are named by role; the private configuration that names them has sha256
`7416193ae90578de690a9412a7294d8b1031b1735feaff31e20c13052edc8a2e`.

Deviations: one. 10 of the candidate's 2,000 held-out answers could not be parsed and were not
asked again (the plan's rule re-asks an order up to six times; the harness re-asks only on a second
pass, which was not run). As the plan says for an order with no answer, those pairs count as no
pick (half credit). Had all ten been answered and right, the candidate's accuracy would rise by at
most 0.5 points; no decision changes.

## Read this first

**The candidate does not replace the production forecast.** It passed three of the four lines and
failed the one that decides it.

- **H4.1 failed: the candidate is 6.0 points less accurate than the production model** on the same
  1,000 held-out pairs: 69.7% (95% interval 66.8% to 72.5%) against 75.7% (72.9% to 78.3%). Paired
  difference -6.0 points, 95% interval -8.4 to -3.7 (line: the lower end above -3.0); 124 pairs only
  the candidate got right, 216 only the production model; sign-flip p < 0.00001 (none of 200,000
  flips). Development had shown -6.2 points on 300 other pairs.
- **H4.2 passed: it beats the best simple rule.** 69.7%, lower end 66.8%, against 61.3% for the
  headline written first.
- **H4.3 passed: it does not win by remembering.** Given half a headline, it could finish 1.1% of
  1,999 (word for word 0.3%). On the 977 pairs where it could finish neither headline it scored
  69.9%, against 69.7% overall (line: at most 3 points lower).
- **H4.4 passed: rewording barely moves it.** On H3's rewordings of the first 500 pairs it scored
  66.7%, against 69.4% on the same pairs in their original words: a drop of 2.7 points (line: at
  most 5). The production model dropped 8.6 points on the same check (H3).

## Not registered: where the gap comes from

Read after the results, so it is a lead, not a finding. On the 500 reworded pairs, which no model can
have seen, the candidate scored 66.7% and the production model 68.0% (H3's cached answers): a
difference of -1.3 points, 95% interval -4.5 to +2.0, sign-flip p 0.48 (86 pairs only the candidate
right, 93 only the production model). So on headlines neither can have seen, the two are not
distinguishable here, and much of the production model's 6-point lead on the original headlines may
come from the familiarity H3 could not rule out. Headlines people test in Mimiq are new, which makes
this the case that matters in use. A registered test on fresh headlines would settle it.

## Secondary

| | Candidate | Production (H1) |
|---|---|---|
| Pairs where both orders agreed (a pick) | 77.4% | 82.4% |
| Answers naming the headline shown first | 44.3% | |
| Unparsed answers | 10 of 2,000 | |

On the development near-ties (exploratory, 300 pairs, not held out), the candidate made a pick on
218 and the production model on 214: like the production model (H2), it rarely says a real tie is too
close to call.

## Cost

Held-out calls at list price: the forecast $0.72 (2,000 calls), the recall probe $1.25 (1,999
calls; the candidate thinks at length before finishing a headline), the reworded pairs $0.32 (1,000
calls): $2.29 in all. Development runs (600 development pairs, winners and near-ties) added $0.44: $2.73
in all, under the $5 cap.
