# Plan R1: do simulated people respond to reconstructed interfaces like people did?

Prepared 2026-09-30, before recruitment, recall probes or simulated visits. **Not yet publicly
registered and not authorized to run.** The commit that publishes this plan and its frozen
manifest in the [public register](https://github.com/victorgulchenko/mimiqbench) is the timestamp.
The coordinator must confirm that publication before any call or run. Results and deviations
will go in RESULTS.md, whatever happens. No results exist at preparation.

## Question and scope

Eight published experiments, five source-paper groups: two subscription-offer experiments,
five consent-interface experiments, and one future-survey subscription experiment. We rebuild
their decision structure with new brands, products and wording. Do the **browsing personas'
observed choices** move in the same direction, and by how many percentage points?

This tests transfer to reconstructed screens, not exact replication or never-seen live-site
usability. All original outcomes were public before this plan. There is no concealed human
holdout here, and no fitting or development runs on these targets. Engine A's production
browser path is frozen at the implementation commit in the private configuration. Before
execution, the coordinator must verify that implementation has been merged and accepted.

## Data and selection (fixed)

CANDIDATES.md contains the eleven screened experiments, primary citations, screen locators,
rates, denominators, fame labels, exclusions and reconstruction limits. The selection rule is
source/structure/population availability and at least 50 people per selected condition;
large field studies with unpublished device-cell denominators retain that limitation openly.
The selected IDs are exactly R01–R08 in human.json. No addition, deletion, replacement,
alternative contrast or direction change after publication, including after a failed probe.

| Study | Primary comparison, B minus A | Human reference | Paper group |
|---|---|---|---|
| R01 | Mild subscription friction package minus plain offer | 155/600 − 73/644; positive | LS |
| R02 | Hidden renewal price minus prominent price, initial acceptance | 183/607 − 191/1,289; positive | LS |
| R03 | Bottom-left binary notice minus top bar, any desktop decision | 32.9% − 2.2%; positive | Utz |
| R04 | Prechecked minus unchecked optional purposes, all-purpose desktop consent | 11.9% − 0.0%; positive | Utz |
| R05 | Cookie wording minus data wording, any desktop submission, no policy link | 17.0% − 11.2%; positive | Utz |
| R06 | Extra bulk-allow button minus selected-purpose confirmation only | 27/50 − 12/52; positive | MB |
| R07 | Refusal default minus no default, tracking agreement | 120/218 − 133/218; negative; paired archive subset | GSB |
| R08 | Negative minus positive future-survey wording, no default | 79/312 − 299/320; negative; counts recovered from rounding | CAF |

R03–R05 use corrected, published desktop percentages. Their condition Ns and human sampling
intervals are unavailable; total study N must not be used as a device-cell denominator.
R07's 218 complete pairs are a source-data subset fixed before simulation, not all 255
recruits. Its paired cells are included in human.json. Source and source-data hashes are in
SOURCES.sha256. Neither unavailability nor an unexpected simulated direction permits dropping
a study. Selection is outcome-informed, including the choice of the privacy-protective
portfolio follow-up over its near-ceiling predecessor; it is not an outcome-blind literature
sample. Related experiments are grouped in all summaries; they are not eight independent
research programs.

## Stimuli and audiences

STIMULI.md fixes the paths, controls, branch behavior, nuisance-factor schedules, outcome
extraction and all known adaptations. The entire sites directory is frozen. Serve **only**
that directory on a local origin after GO. The browser must not be able to retrieve this
plan, human.json, recall material or source documents. No original brand, citation, published
rate, winner or study ID appears in rendered stimulus content.

audiences.json freezes the recruitment prompt, scenario/goal, locale, timezone and eligibility
for every experiment. R01/R02 approximate the original US consumer panel; R03–R05 German
product-review visitors; R06 German-speaking computing undergraduates, 60% Austria/40% Germany;
R07 UK online-panel adults 18–65; R08 US online-panel adults. Report achieved age, gender,
education, occupation, country and language distributions beside available source summaries.
Unknown source demographics remain unknown. Desktop adaptations and abbreviated lead-ins
are reported, including R08's omitted preceding vignette.

After publication/GO, build each panel **once**, with the existing production panel builder,
the fixed prompts and seeds. Request 80 people for R01–R06/R08, 40 for R07. Deduplicate by
persona ID; alternate returned people into A and B for independent-condition studies. Save
and hash panels before any page exposure. No arm's model sees its counterpart or the human
answer. No second panel draw because behavior looks implausible. If the production builder
relaxes away a hard eligibility criterion, yields too few people, or substitutes generic
narratives for failed hydration, report a recruitment failure and stop; do not quietly
relabel it a matched audience. Soft source proportions are targets, not invented exact quotas.

## Method and sample size

- Use the production flow browser runner, not a text-only winner forecast, a new behavioral
  rule, or a calibrated conversion prior. The browsing, recall, recruiting, fallback and
  summary roles and exact settings are frozen in **private-config.json**, referenced only
  by hash publicly. This is the production browser implementation with a configured browsing
  role; it does not establish accuracy for every model configuration or the default tier.
- Forty distinct people per condition. R07 has 40 people seeing eight cells in one session,
  with a paired comparison of cells 0/1. Seven other experiments have 80 independent sessions
  each: **600 browser sessions total**, plus eight recall probes and panel creation.
- One browser at a time, fresh context per visit, 1440×900, normal production clean image
  and action list, the configured desktop browser, 40-action and 480-second server limits.
  Record browser/runtime versions and effective environment before exposure. No forced consent clicks, no
  success-directed goal, no changes to prompts, hydration, heuristics or calibration.
- Run balanced rounds: for i=0..39, R01 through R08 in numeric order. For independent arms,
  A then B when i is even, B then A when odd. R07 runs once per round, using its fixed order
  schedule. No full-study-first ordering that spends the budget only on easy studies.
- Freeze browser traces and submitted-choice exports before scoring. R03–R05 keep the
  original 30-second window in actual browser wall time. Record inference latency: this
  adaptation can confound simulated attention with computation time and must be disclosed.
- A known voluntary exit is a non-action, never success. Technical/model errors, engine
  cutoffs, automated `engine_consent` events and unavailable traces are unknown, not refusal.
  No replacement participant or rerun after exposure. Internal production retries/fallbacks
  remain bounded, recorded and charged. Do not pool fallback observations invisibly.

Precision is deliberately modest: with 40 independent people/arm, the worst-case normal
95% half-width of a rate difference is about **21.9 pp**. The conservative worst-case paired
normal approximation is about **31.0 pp**; actual R07 uncertainty uses the paired discordance
interval below. This is not powered for a 5.8 pp effect or narrow absolute conversion forecasts.
Report intervals even on a correct direction. Do not reduce n to obtain a verdict if the
budget cannot complete it. Larger precision studies need their own prior registration.

## Primary metrics and pass lines

For study j, human effect `dh = pB − pA`, simulated effect `ds = qB − qA`, measured in
percentage points. A direction match is 1 exactly when `dh × ds > 0`, otherwise 0. An exact
simulated tie counts 0. The primary suite metric is the unweighted share of the eight
experiments with a direction match. **PASS requires at least 7/8 (87.5%), all 40 people in
both conditions of every experiment with resolved outcomes, and all eight valid recall
classifications. Otherwise a finished suite is FAIL; an unfinished suite is INCOMPLETE.**

R1.2 (secondary magnitude line): report signed and absolute effect error for every study,
mean absolute error, and the fraction with absolute error ≤10 pp. This line does not turn
a primary direction pass into a claim of numerical accuracy. R1.3 (secondary contamination
line): if at least three studies are recall-negative, their direction share must be at least
the overall share minus 15 pp to say the suite survives the recall screen; otherwise this
line is unassessable, not passed. Source fame splits have no pooled substitute threshold.

score.py fixes the calculations: 95% Wilson condition intervals; independent differences
via Newcombe/Wilson; R07 uses Bonferroni-adjusted Wilson intervals for the two discordance
probabilities (97.5% each, z=2.241402727604947), then subtracts their opposite endpoints.
This conservative paired construction targets 95% coverage and stays nondegenerate when
no pair disagrees; Wilson coverage remains approximate. Human intervals use exact counts
where available and paired data for R07. No interval is fabricated for missing human Ns.
Effect-error intervals condition on the human point estimate and are labelled that way;
they do not account for human sampling uncertainty. Printed field-study rates have a
rounding uncertainty up to 0.05 pp each, hence up to 0.1 pp on their difference.

The descriptive suite Wilson interval and binomial coin tail probability are accompanied
by each of the five source-group shares and their equal-weight mean. With a purposive,
correlated literature set, the binomial calculation is descriptive, not proof of general
product accuracy. It is not permissible to treat eight contrasts as independent evidence
without this qualification.

Missing outcomes are bounded both ways (all unknown A positive/B negative, and vice versa).
No positive verdict is available with any missing scheduled outcome. Report available-case
rates as incomplete descriptive results. Also show completer-only R01 and results with
fallback decisions excluded; these are sensitivities, never replacements for primary.

## Baselines

A coin: expected 50%. Always choose B: 6/8. Always choose A: 2/8. A domain-informed human
rule about defaults, prominence and positive invitations can plausibly anticipate most of
these directions; this suite supplies no measured expert forecast baseline and no claim
of beating experts. The bar exceeds the fixed always-B rule, but does not by itself prove
benefit beyond such mechanism knowledge.

## Contamination

Every stimulus is re-skinned before exposure. RECALL.md fixes an isolated, guided result
recall probe per experiment using the browsing role, before the first visit and after GO.
It is inspired by [H4](https://github.com/victorgulchenko/mimiqbench/blob/main/prereg/2026-09-29-headlines-candidate-forecast.md);
it is not an identical headline-completion test. Self-reported recall, or both rates recalled
within 3 pp with the right direction, flags an experiment. Unknown/failed probes are not
negative. Report raw responses, flags and direction/magnitude scores for positive, negative
and unknown subsets. Also report the **pre-fixed** high/lower fame split (6/2), regardless
of probe answers. No probe answer changes the sample, stimulus, hydration or prompt.

## Cost and stopping

Owner-approved **$15 total** in the `replications` ledger lane, including recruitment,
hydration, recall, browser steps, summaries, retries and fallbacks. Existing lane caps are
unchanged; the overall ledger allowance increases by the approved $15. Preparation uses $0.
Recruitment has an additional $2 subcap; recall $0.50. Unused subcap money may fund visits,
but never raise the $15 lane cap. No paid pricing pilot or smoke run is authorized here.

Do not claim 600 visits are known to fit: cost on these sites is unmeasured. After GO,
reserve a conservative upper bound before **each** paid call, including fallback attempts,
and charge all returned usage with the lab's safety margin. Unknown prices, unavailable
usage or an insufficient remaining allowance stop further calls. Reconcile ambiguous failed
requests before resuming. The ledger's post-charge check alone is not hard-cap protection.
When money runs out, preserve partial traces and mark all unfinished slots not_run/unknown.
Stop; publish INCOMPLETE. Never quietly switch to a cheaper role, shorten visits, shrink n,
drop an experiment, or ask a forecast to fill missing people.

## Freeze, publication and execution gate

FROZEN.sha256 identifies this plan, candidates, truth, audiences, recall protocol, stimulus
specification, every site asset, scorer and **hash only** of the private configuration and
private engine manifest. Engine source bytes and production-panel dependencies are pinned
in that private manifest. Source documents are pinned by SOURCES.sha256. Hashing is a
read-only preparation step, not a simulation.

| Frozen input | SHA-256 |
|---|---|
| Human reference, human.json | `37d53d9680782baa9a05eaf7f5f18e5cf6bcdcc8e0e1d75bf3a53b67a22d73e5` |
| Audience specification, audiences.json | `433b54f15b397c102cd24b1d22a0735ad38ed9f5bfc4860a3db8839890146cf6` |
| Offline analysis, score.py | `6c246bb714dcfa5b1c0dd14c5e2a824ba21a832934eb1280dd8be4eccabda27f` |
| Private role/configuration file (hash only) | `e75d595575bff2f62821590ed34670b353a0e0a31f385cdd672d87129bb277c2` |
| Private engine manifest (hash only) | `6ac1c88bc682615b147f9bf0db89d7556c850f3fc5180b0e2561c7602c1224b1` |

The coordinator publishes the public-safe files and manifest, records the public commit URL,
and supplies a separate GO receipt containing `replications`, this registration's repository
path, its SHA-256 and that public commit URL. The private config, engine manifest, credentials,
personas and full run traces must not be copied into the public register. Public model names
are roles only, as in H1/H4. A date written in this file, an approved budget or a local commit
is not a public registration.

No paid runner is included in this preparation. A later executor must enforce the gate,
verify all hashes and the accepted production engine, finish local browser QA, and implement
call reservations/trace extraction without changing the frozen choices. The existing generic
held-out CLI does not automatically support these custom sites. Any needed change to frozen
code, configuration or experimental decisions requires a public amendment before exposure.
This preparation ends here; it does not create a GO receipt.

## What will be published whatever happens

All eight rows: human counts/rates and missingness, simulated counts/rates, effect intervals,
direction, error, failures, latency, role fallbacks and dollars. The primary verdict and
secondary lines, source-group summaries, fame/recall splits, raw recall responses, incomplete
slots, source-reconstruction departures and every protocol deviation. Failed or incomplete
evidence is retained. No claim beyond these observed numbers, and no Results placeholder
presented as a measured result.
