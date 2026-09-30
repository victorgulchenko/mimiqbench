# Replication candidates

Evidence checked 2026-09-30, before any simulation. This is a purposive screen-reconstruction
suite, not a random sample of interface research. Eleven experiments were screened; eight are
selected. A paper, an experiment, a condition, and a person are different units. Each selected
experiment contributes ONE comparison. Related experiments remain grouped by paper in reporting.

## Selection rule

Include an experiment if a primary publication or its authors' archive specifies the visible
decision, provides behavior rates (or recoverable counts), identifies the recruited population,
and has at least 50 observed people in each selected condition. Large field experiments whose
paper gives only total N and rounded device-specific rates are eligible, but their missing
cell denominators and human intervals stay explicitly unavailable. Reconstruct the decision
structure, preserve costs/defaults/extra steps, and change brand, product example and prose.
Selection is outcome-informed: the published results were known, and the follow-up portfolio
was preferred to its near-ceiling predecessor to include a privacy-protective mechanism.
This is not a literature-wide, outcome-blind or publication-bias-free sample. No simulated
results informed selection. Exclude OPeRA and previously used page-tests/organ-donation
stimuli. No substitution after publication.

The fame line is qualitative and fixed now: **high** = foundational default research or one of
the three widely cited papers named in the brief; **lower** = the other specialized papers.
Lower does not mean unseen in training. Every selected experiment gets a separate recall probe.

## Selected experiments

| ID | Primary evidence and screen locator | Frozen A / B and human outcome | Human N and denominator | Fame; fidelity |
|---|---|---|---|---|
| R01 | Luguri & Strahilevitz (2021), *Shining a Light on Dark Patterns*, Journal of Legal Analysis 13:43–109, [doi:10.1093/jla/laaa006](https://doi.org/10.1093/jla/laaa006). [Final paper mirror](https://content.naic.org/sites/default/files/national_meeting/Shining%20Light%20on%20Dark%20Patterns.pdf), Study 1 pp. 60–65, Table 2, Appendix B. | Plain offer / mild package (default + recommendation + extra refusal screens). Subscription acceptance: 73/644 = 11.34% / 155/600 = 25.83%; B−A +14.50 pp. | Study recruited analytic sample 1,963; selected completed-condition Ns 644/600. These are the completer rates, not Table 2's dropout-as-refusal rates. | High. Procedural description is sufficient for the three-screen mild branch, but not pixel-exact original layout. Six free months; $2.99/$8.99 afterward, balanced. |
| R02 | Same citation, **separately recruited Study 2**, pp. 71–76, Table 3. | Visible renewal price / renewal price in small gray footnote. Acceptance on the **initial offer screen**: 191/1,289 = 14.82% / 183/607 = 30.15%; +15.33 pp. | Analytic N=3,777. Table 3 pools the independently assigned form, price and consent-cover factors. It is not the plain-button cell alone. | High. One free month; $8.99/$38.99 afterward. Both sites implement four form backgrounds and both prices. Standardization and abbreviated lead-in are explicit adaptations. Later trick-question decisions are not this endpoint. |
| R03 | Utz, Degeling, Fahl, Schaub & Holz (2019), *(Un)informed Consent*, CCS, [doi:10.1145/3319535.3354212](https://doi.org/10.1145/3319535.3354212), [corrected author paper](https://arxiv.org/pdf/1909.02638), Experiment 1, Figs. 1–3, §§3.2,4.2; [screen archive and erratum](https://github.com/RUB-SysSec/uninformed-consent). | Desktop top bar / bottom-left box, same binary buttons. **Any decision** (accept or decline), not acceptance alone: 2.2% / 32.9%; +30.7 pp. | Experiment N=14,135 across six positions and two device strata. Desktop-by-position Ns are not published in the inspected materials. Do not divide total N by 12 or invent event counts. | High. German product-review visitors arriving from search. Desktop-only reconstruction; original endpoint window 30 seconds. Exact host page is unavailable. |
| R04 | Same Utz citation, **Experiment 2**, Fig. 1(d), corrected Fig. 4, §§3.3,4.3. | Desktop purpose checkboxes optional-off / optional-on. Submission allowing every optional purpose: 0.0% / 11.9%; +11.9 pp. | §4.1 says 36,530, §4.3 says 36,395 and about 4,044/condition across devices. Preserve this source discrepancy. Desktop cell Ns unavailable. 0.0% is a rounded value, not a verified zero count. | High. Same five purposes, necessary fixed on, one submit, bottom-left placement. Checkbox order counterbalanced. Timing and host limitations as R03. |
| R05 | Same Utz citation, **Experiment 3**, corrected Fig. 6, §3.4 and §4.4; archived NT-NP and TE-NP screens. | Desktop “your data” / “cookies”, neither with a policy link. Any submitted purpose decision: 11.2% / 17.0%; +5.8 pp (1 − no-action share). | §4.1 N=32,225; §4.4's mean 6,032 per condition does not reconcile with four conditions. Desktop cell Ns unavailable. Do not silently repair the paper. | High. Same category controls and empty policy-link space in both versions. Small effect is retained, not screened out. |
| R06 | Machuletz & Böhme (2020), *Multiple Purposes, Multiple Problems*, PoPETs 2020(2):481–498, [doi:10.2478/popets-2020-0037](https://doi.org/10.2478/popets-2020-0037), [paper](https://petsymposium.org/popets/2020/popets-2020-0037.pdf), Figs. 2,8; Table 5. | Three unchecked purposes + confirm selection / same plus prominent select-everything button. All-three consent: 12/52 = 23.08% / 27/50 = 54.0%; +30.92 pp. | N=150 after exclusions; unused reduced-choice arm n=48. Only control and T1 enter primary. | Lower. German-speaking first-year computing undergraduates, Austria/Germany. Blocking dialog before a flight search. Preserve small gray confirmation action and orange bulk action. Desktop-only is a device adaptation. |
| R07 | Graßl, Schraffenberger, Zuiderveen Borgesius & Buijzen (2021), *Dark and Bright Patterns in Cookie Consent Requests*, JDSR 3(1):1–38, [doi:10.33621/jdsr.v3i1.54](https://doi.org/10.33621/jdsr.v3i1.54), [paper](https://arxiv.org/pdf/2509.18210), Experiment 2, Fig. 6, Appendix B; [author archive](https://osf.io/bfdvy/). | Neutral radio choices / refusal preselected. Primary outcome is tracking agreement. Published archive's **complete baseline/default pairs**: 133/218 = 61.01% / 120/218 = 55.05%; −5.96 pp. | Published recruitment N=255, not 255 complete pairs in `fu_full_data.csv`. Paired cells (A,B): 00=79, 01=6, 10=19, 11=114; n=218. Single-condition observed counts differ (baseline 140/226, default 121/221). | Lower. UK residents 18–65. Eight news designs in one portfolio, randomized order, retained in the site; only the baseline/default pair is scored. Counts are an explicitly selected archive subset, not a falsely attributed paper table. |
| R08 | Chandrashekar et al. (2023), *Defaults versus framing*, Meta-Psychology 7, [doi:10.15626/MP.2022.3108](https://doi.org/10.15626/MP.2022.3108), [paper](https://open.lnu.se/index.php/metapsychology/article/view/3108/3438), Part 2 survey subscription, Tables 2,5. | Positive / negative notification wording, both with **no preselection**. Consent to future health surveys: 93.4% / 25.3%; −68.1 pp. | Pooled recruitment samples N=1,920; selected cells n=320/312. Rounded rates uniquely imply counts 299/79, identified as reconstructed counts. | High because it directly reprises a famous default/framing paradigm. US online panel participants; mean age 38, 52% female. Preserve radio yes/no and invert the meaning of yes in B. Preceding organ-donation scenario is omitted and disclosed. |

## Excluded experiments (not reserves)

| Candidate | Evidence, screens, rates and N | Decision |
|---|---|---|
| Nouwens et al. (2020), *Dark Patterns after the GDPR*, CHI, [doi:10.1145/3313831.3376321](https://doi.org/10.1145/3313831.3376321), [paper](https://arxiv.org/pdf/2001.02479), Fig. 3, Tables 1–2. | Eight pictured interfaces; 40 people, 1,280 repeated choices. Overall 707/1,280 accept-all; hiding rejection changes acceptance by about 22–23 pp. These are not 1,280 independent people or per-condition rates. High fame; reconstructable. | Exclude: below 50 distinct people, repeated-visit carryover, and regression effects alone are insufficient for the required condition-rate table. |
| Graßl et al. (2021), **Experiment 1** (same citation), Fig. 1, Appendix B, [archive](https://osf.io/c7qza/). | Eight within-person news designs, n=228; 93.8% agreement overall; the paper finds no substantial default/aesthetic/obstruction effect. Per-condition rates are graphed; supplied merged archive has incomplete condition records. Lower fame; reconstructable. | Exclude from v1: prioritize the independent privacy-protective follow-up to cover the opposite direction; do not count both near-identical portfolios as broad product coverage. The null finding remains visible here. |
| Wroblewski & Etre (2009), [*Inline Validation in Web Forms*](https://alistapart.com/article/inline-validation-in-web-forms/), Figure 1 and videos. | Six registration forms; n=22 people, ages 21–49. Reported best-arm success improvement 22%, but absolute success rates and per-arm event counts are absent. High practitioner fame; interactions reproducible. | Exclude: too few people and relative improvement is not an absolute behavioral rate. Never reinterpret “22%” as 22 percentage points. |

## Extraction and limitations

- Source figures were visually inspected. Use Utz's corrected 2019-10-22 paper, not the
  camera-ready charts: the authors explicitly corrected Figures 3, 4 and 6.
- R07 data: [fu_full_data.csv](https://osf.io/download/ep3uy/) and
  [data dictionary](https://osf.io/download/4zg38/). `consent`: 1 agreement, 0 refusal.
  Join `avision` and `quitelight` on `participantId`; retain one finite 0/1 observation
  in both conditions; never convert `NA` into refusal. The archived file's SHA-256 is
  recorded in SOURCES.sha256. No raw participant data is redistributed here.
- R08's Table 2 prints an affirmative sentence in the row labelled negative/no-default.
  The original [Group A survey](https://osf.io/download/jqckg/) (`health-nodef-neg`)
  and [Group B survey](https://osf.io/download/5qrct/) (`Negative-NoDefault`) both
  contain the negation and explicitly recode Yes=0, No=1. The reconstruction follows
  those original instruments. The [authors' analysis source](https://osf.io/download/vqxpu/)
  was read, not executed. One sample randomized answer order; the other kept Yes first.
  Our fixed order and required response are adaptations, not purported exact copies.
- Re-skinning is a deliberate transfer test. It cannot both change product/wording and
  be an exact replication. We preserve each treatment mechanism and list departures in
  STIMULI.md; human rates are reference targets, not guaranteed truths for the new brands.
- The five source-paper groups are LS, Utz, MB, GSB, and CAF. Three Utz experiments on
  one host do not establish coverage of three unrelated products. Pricing, checkout,
  trust ratings and inline validation are not independently validated by this suite.
- No original images or long passages are embedded in the sites. Sources remain linked
  for verification. The author CSV is CC BY 4.0; the other papers' individual reuse
  terms apply to their contents. Our screens and wording are newly authored.
