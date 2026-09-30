# Stimulus and outcome contract

Authored 2026-09-30. These are complete static HTML/CSS/JavaScript sources, with no build,
package installation, remote fonts, external images, analytics, account creation or payment.
They have **not been opened, served, browser-tested, or run**. Source review is not browser QA.
Only `sites/` may later be served; the surrounding directory contains the human answers.

## Addresses and assignments

All addresses are relative to a future loopback-only `sites/` origin. There is no public host.
Use `/s01/index.html?v=a&i=0`, etc. `v` must be `a` or `b`; `i` is a condition-local integer
0–39. Invalid or missing parameters show an error, never a silently chosen control. No page
contains citations, experiment names, winners, human rates or a link to another condition.

| Study | Entry | A | B | Captured value |
|---|---|---|---|---|
| R01 | s01 | One plain offer | Preselected suggested plan; alternatives; shame-framed refusal; reasons with reconsideration | `primary`: 1 only if a participant explicitly submits enrollment at any branch; 0 final refusal |
| R02 | s02 | Renewal price prominent | Same price as small gray footnote after controls | `primary`: 1 initial acceptance; 0 initial decline/alternatives |
| R03 | s03 | Binary top bar | Same binary bottom-left box | `primary`: 1 either banner decision; 0 no action |
| R04 | s04 | Optional purposes unchecked | Same purposes checked | `primary`: 1 submission with all four optional purposes on; 0 partial/none/no action |
| R05 | s05 | “Ihre Daten” | “Cookies” | `primary`: 1 any submitted settings; 0 no action |
| R06 | s06 | Three purposes + subdued confirm | Same plus orange bulk-allow button | `primary`: 1 all three allowed; 0 partial/none |
| R07 | s07 | Order schedule a | Reverse order schedule b | Both versions contain all 8 cells. Primary A=`cell_0`, B=`cell_1`; value 1 tracking allowed, 0 refused. `v` is NOT the treatment here. |
| R08 | s08 | Positive invitation statement | Negative invitation statement | `primary`: A Yes=1/No=0; B Yes=0/No=1 |

Independent-condition studies have different people in A and B. A visit uses the index of
that person within the condition, not the combined 80-person index. R07 has only 40 visits,
each supplying a paired observation. Blocks 0, 2 and 4 of eight people use order a; blocks
1 and 3 use order b. Its order is `(i mod 8 + j) mod 8` for a and
`(i mod 8 + 7 − j) mod 8` for b, j=0..7. Every cell occupies every position five times.

R02 form distribution in **each** content arm: indices 0–13 plain, 14–21 recommended,
22–31 preselected, 32–39 obstructed. Each form stratum balances the two prices by index
parity. This 35/20/25/20% allocation approximates the source's marginal 34.26/22.80/22.53/20.41%.
Source cross-cell counts are unavailable; do not portray Table 3 as a plain-form comparison.
The endpoint is recorded before obstruction follow-up or trick question, which are outside
this measured screen. Both prices and trial lengths are preserved exactly. R01 alternates
low/high price by index parity. There is no actual enrollment or charge.

R04/R05: the necessary checkbox is checked and disabled. Four optional categories rotate
by `i mod 4`, with the same rotation schedule in A and B. There is no accept-all shortcut.
R05 omits the policy link in both arms and retains its blank space. R03/R04 have a functioning
local policy dialog. A policy-link click alone is not a submitted choice.

R07: cell number bits 1/2/4 represent refusal default, refusal emphasis, and obstruction
of agreement. Refusal stays left; agreement stays right. A separate Continue submits the
radio state. In obstructed cells, Review choices reveals the agreement radio. Eight invented
news identities and articles replace the source brands and content. All eight exposures are
kept to preserve a repeated-choice task. Identity is `(cell + i) mod 8`: every cell appears
with every news identity five times, avoiding a fixed brand/treatment confound. Only cells
0 and 1 enter the primary score.

## Trace contract

`window.replicationExport()` returns an independent JSON copy of:

```
{schema: 1, site, variant, index, events: [...], decisions: {...}, terminal: boolean}
```

Events include relative milliseconds, loads, each submitted decision, purpose selections,
alternative/refusal branches, policy opens, portfolio reviews and terminal state. Decisions
are first-write-wins. A checkbox or radio click alone is not a submission. A summary's prose,
a claimed task completion, or clicking the largest button is never a conversion proxy.
State is kept in memory and session storage; a fresh browser context is mandatory. Capture
the trace before closing the context. Do not infer refusal from a missing export.

For R03–R05, a 30,000 ms browser timer begins when the notice is inserted; at expiry an
undecided notice records `no_action=0` and disappears. A participant who voluntarily leaves
before deciding is also 0. A browser crash, engine budget cutoff or lost trace is unknown.
Record decision latency and model-call latency separately: the source's 30-second window
was human viewing time, while inference consumes our wall time. Do not pause this timer,
extend it after seeing results, or claim it is a clean measure of human attention.

For other studies, voluntary exit before a choice is recorded separately and scored 0 in
the intention-to-expose simulated rate. Show a completer-only sensitivity for R01, whose
published reference excludes dropouts. Technical cutoffs/errors remain null, not 0.
For R07 a voluntary exit makes **unseen** cells unknown, not recorded refusals; a cell that
was visibly offered and deliberately abandoned can be 0. Every paired cell must be observed
or have an evidenced voluntary exit for the experiment to count as complete.

## Re-skinning and fidelity departures fixed in advance

- R01/R02: SecureNest Account Watch replaces the original identity/credit-monitoring
  offer with account-exposure/identity monitoring. The demographic/privacy lead-in is
  summarized in the goal/context instead of re-administered; geography and threat framing
  remain. R02 does not reproduce the university/corporate recruitment-cover manipulation.
- R03–R05: Werkblick's Uferlicht Mini replaces the undisclosed host and original product.
  German language, purposes, blocking status, spatial placement and outcome window remain.
  Exact host geometry is unavailable. The site retains the large difference between a bar
  and a corner notice. Fixed 1440×900 measures one desktop setup, not the source's device mix.
- R06: Weitflug, a new route and a future date replace the original search. Dialog structure,
  orange emphasis, details disclosure and purpose semantics remain. The source used both
  mobile and desktop; this is a desktop transfer. Classroom social context is summarized.
- R07: newly authored news pages and common component geometry replace varying source
  themes; a single appeal slider follows each visit instead of the original complete
  retrospective questionnaire. Preserve eight exposures, not eight independent studies.
  The reference uses only the 218 archive participants with both relevant choices.
- R08: WellSpring replaces the original panel wrapper; policy/health invitations remain.
  The prior organ-donation vignette is omitted. New wording retains affirmative versus
  negated notification statements and the opposite coding of Yes. No-default remains
  no-default; the participant must explicitly select a radio before continuing. Yes stays
  first here; one original sample randomized response order. The source instruments also
  differ in required-response validation. The original survey files resolve the apparent
  missing negation in the published Table 2; see CANDIDATES.md.

These are prespecified **structural transfers**, not pixel-perfect replicas and not new
human experiments. Departures must accompany the numeric comparisons wherever published.

## Later local QA, after publication and coordinator GO

No QA was executed in preparation. Before paying for a browser decision, an operator must
check each branch/price/background, first-write trace behavior, yes/no inversion, 30-second
expiry, all eight portfolio cells, keyboard submission, rejection paths and absence of
external requests. Check 1440×900 and record screenshots privately. A bug requiring any
frozen-file edit requires a new public amendment **before** model exposure; cosmetic and
substantive changes both get new hashes. Do not improvise repairs during scored visits.

The current production engine automatically handles a small set of exact English cookie
button labels in recognized containers. These reworded German and English controls do not
match that list. Do not change the production helper for this suite. If a trace nonetheless
contains `engine_consent`, invalidate that visit as a technical failure; it was not a
participant decision. This guard must be checked in later QA and during every run.
