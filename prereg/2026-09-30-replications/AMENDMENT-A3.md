# R1 amendment A3: English eligibility evidence and unexposed panel reuse

Prepared 2026-09-30; approved by Victor in chat ("18 yea"). This document
takes effect only after publication in the public register and a separate
coordinator GO-A3 receipt naming this document's
SHA-256, the A3 manifest and its public commit. Earlier receipts cannot authorize
A3 or another execution of A2. The original registration, A1 and A2 remain
historical records.

## Facts before exposure

The original attempt and A1 stopped at R06 recruitment, each with 70 of the
required 80 people. A2 retained R06 as a direction miss and then stopped at R07:
`StopRun: R07: English-language eligibility is not evidenced` for the first
saved person. R08 recruitment was not reached.

**All three attempts have zero simulation sessions and zero recall probes.**
No page was shown to any recruited participant. Earlier local control QA had
no participants or model calls. This amendment follows a recruitment feasibility
failure before exposure; it is not selected from behavioral outcomes.

The English check accepted only an explicit mention of English or en-GB/en-US
in a persona's narrative, demographics or language field. The population has no
language attribute: its demographics contain age, city, education, gender,
generation, income tier, location, occupation and region. **Zero of the 40
saved R07 records contain the required English evidence.** Thus the population
does not provide evidence for the registered R07/R08 language test. German
studies passed because their narratives explicitly name the language.

An offline, zero-cost check of the saved R07 draw confirmed that all 40 people
meet the other rules: age 18–65, UK residence, unique IDs, parsed criteria and
hydration. The panel was drawn once and never exposed. No person is replaced,
relabeled or given an invented language field.

| Attempt | UTC start → stop on 2026-09-30 | Recruitment spend USD |
|---|---|---:|
| Original R1 | 15:58:37 → 16:29:17 | 0.875806 |
| A1 | 17:01:07 → 17:05:55 | 0.135288 |
| A2 | 18:46:43 → 18:49:32 | 0.075287 |
| Cumulative | All stopped before exposure | **1.086381** |

All reservations are settled. Charges include the ledger safety margin and
remain against the same **$15** lane and **$2** recruitment subcap. Before A3,
the remaining allowances are **$13.913619** and **$0.913619**, respectively.
The **$0.50** recall subcap and shared lab cap still bind. Zero-dollar stop
metadata never charges prior spend again.

## Exact eligibility amendment

Only R07 and R08 change their accepted English evidence under A3:

| Study | Required residence evidence | Required registered browser locale |
|---|---|---|
| R07 | Persona location country GB or UK | en-GB |
| R08 | Persona location country US or USA | en-US |

Both residence and the exact registered locale are required. A mention of
English cannot bypass either requirement. The locale is the frozen audience
locale passed to the session's browser context. Residence plus that locale is
the operational English-evidence rule; it is not a claim of individually
verified language proficiency. The validator does not write any language label
or modify persona bytes. Historical R1/A1/A2 checks retain their original rule.

German-language evidence for R03–R06 is unchanged. Adult age, R07's upper age
limit of 65, country, hydration, unique panel size, parsed recruitment criteria
and every other eligibility rule remain unchanged. Audiences, seeds, assignment,
stimuli, session settings, recall prompts and human references remain frozen.

## Restart and zero-cost pre-flight

- R01–R05 reuse the original attempt's exact panels in their original order.
- R07 reuses the exact saved A2 panel, pinned below. It is not redrawn. No
  language label or demographic file is invented to repair the failed check.
- R08 is recruited once, with its registered audience, n=80 and seed. The A3
  English-evidence rule applies. A recruitment failure stops the run.
- R06 remains not run. Neither failed partial R06 panel is used.

A3's restart source is the stopped A2 attempt, which chains to A1 and the
original. All state and artifact hashes, complete artifact sets, no-exposure and
no-recall conditions, panel bytes and historical ledger charges are verified.
The three original evidence directories stay immutable. A new output directory
retains all three prior state files, artifact manifests and reports in order.

**Before any paid call or ledger `execution_start`, an offline pre-flight calls
`validate_panel` on every reused panel: R01–R05 and R07.** Failure aborts at $0
with a clear pre-flight message and does not consume A3's execution claim.
The copied panel bytes, eligibility and unchanged skeleton pool also pass
before the claim. Fresh dry and QA receipts must match the A3 gate and runtime.
There is one execution for A3 across output directories. After that claim, a
later stop cannot authorize another draw or exposure under A3. A2 cannot
authorize another start.

The report retains all three stops and their individual spend, A3 spend and the
cumulative total. Ledger reconciliation includes every prior charge exactly
once; all spend remains inside the unchanged lane and subcaps.

## Scoring unchanged from A2

R06 is **direction MISS (0)** in the denominator of **eight**, and the pass bar
remains **7/8**. Its report reason stays “not run: the simulated population
contains no university students”. There are no invented R06 outcomes, rates,
persona IDs or recall replies; its simulated effect and magnitude error remain
null. All seven other studies must have resolved outcomes and valid recall
classifications. Other missing data or an interrupted execution is INCOMPLETE.

R1.2 magnitude and R1.3 contamination, including their splits and comparison
share, retain A2's seven-study calculations. Primary intervals, coin-tail and
source-group calculations retain A2's eight-study denominator and R06 zero.
The original scorer and A2 scorer are byte-for-byte unchanged; the report
adapter passes A3 data through the exact A2 scoring contract. The schedule
still has 520 sessions, 560 outcome records and seven isolated recall probes.
Every other A2 rule remains in force.

## Retained evidence and updated freeze

<!-- A3-EVIDENCE-START -->
| File | SHA-256 |
|---|---|
| Original state.json | `1caf2b953e5532923ae05d7af090c412dae07780613adeefc232a17eabdb3955` |
| Original artifacts.sha256.json | `0327d7fc92b66d0a7c254074d72dbfabfc35ab1d99b671cb51577dceec0e832d` |
| A1 state.json | `2206a2458cec8d15d5ec5189bf3e13c5c34739183dbb89c053a64f7265b95732` |
| A1 artifacts.sha256.json | `878a6d20b0115e6e787d1be29c76b69d68ed7cece7fa43bb2b41554c5f7656ec` |
| A2 state.json | `30751c515ea688dea5ea8a2e461538541e2adc02c52a26f6f1bf22f517e71acc` |
| A2 artifacts.sha256.json | `a644dd961367540ab1cb005e031cf259f41ca6edaf341dc4496cf3544f3f3f12` |
| R01 panel | `db2ecb49e117a33d421b7b3687f6e6ca2afab375ace2235f8e948949ab946c94` |
| R02 panel | `a5620a6c910be53e28db0cae0f23d3b21d186cb34638cb577e8fb3cb4b237209` |
| R03 panel | `54b6687d74a8f6c2f7a11796431ed3b29279d342f44a933d7f12e0675270bb05` |
| R04 panel | `6e1c6628dbfda6a3dd0a7b615f80e3a3bb207ea558b7135b9a1770484a4b48a6` |
| R05 panel | `afc86350e90ebda53a7c8bc2c8358aacffadb6a37c1c7b432b771e8f80c53cf6` |
| R07 panel | `6454cc269e9c4fa4c1e053bfe599a883bb1b4c54ffdb873d8e293e7c4aa7e4c5` |
<!-- A3-EVIDENCE-END -->

`FROZEN.pre-A3.sha256` preserves the A2 manifest byte-for-byte. The updated
`FROZEN.sha256` retains all 25 paths and changes only four implementation pins:
`executor.py`, `outcomes.py`, `restart.py` and `reservations.py`. All other
entries, including `score.py`, `score_a2.py`, `human.json` and `audiences.json`,
are unchanged. The original registration and both earlier amendments remain
unchanged. This document is hashed separately in GO-A3 to avoid a
self-referential digest. The offline authorization module pins the exact A3
manifest and document hashes; dry/QA receipts fingerprint all executor Python
files, including that module and the tests.

<!-- A3-HASHES-START -->
| File | SHA-256 |
|---|---|
| FROZEN.pre-A3.sha256 | `dadd7c599de35ded0889be04a58c469153dd59599d00f22cdee65664d184971b` |
| FROZEN.sha256 | `dc87d4c8334aeeac73ca9d0d11ae9359bff9a6297ee635878c78953c20b0134a` |
| executor.py | `47ed1c911e2450a118c26f41eaf92783032984e2aae8e44b9cdbab1d06a061bd` |
| outcomes.py | `98bff48ce9575502357eea1fb360eb4e7df08f9ec12c065ffa55faaa18e57eb9` |
| restart.py | `8af9f3c6b199d2b603bcd7e73d30fcf05b0615a359f87d46c54d9d14947efa09` |
| reservations.py | `0e248df0818dbf735a4605d256c7f1c0bd9f2075bbe1d472743f398c7c6db311` |
| score_a2.py | `ea2cb75fc0e1c5807a457e87b367ddd2b06a2a2043b87f2c79877315e8dc4d22` |
| score.py | `6c246bb714dcfa5b1c0dd14c5e2a824ba21a832934eb1280dd8be4eccabda27f` |
| human.json | `37d53d9680782baa9a05eaf7f5f18e5cf6bcdcc8e0e1d75bf3a53b67a22d73e5` |
| audiences.json | `b89c0f54fdc371eaea8437af4ee02f9eba4a4dd9b84a1efc187eadd63f661267` |
| REGISTRATION.md | `2a866051834de205904fad91fd9281dcf7b08e783dd06eab27e774d5b04b2ca0` |
<!-- A3-HASHES-END -->

## Exact public-file list

Publish only these six files under `prereg/2026-09-30-replications/`:

| Local repository filename | Public register filename |
|---|---|
| AMENDMENT-A3.md | AMENDMENT-A3.md |
| FROZEN.pre-A3.sha256 | FROZEN.pre-A3.sha256 |
| FROZEN.sha256 | FROZEN-A3.sha256 |
| outcomes.py | outcomes.py |
| restart.py | restart.py |
| score_a2.py | score_a2.py |

The register keeps one manifest per amendment. **Do not replace its
`FROZEN.sha256` or earlier amendment manifests.** The A3 manifest retains
repository-relative source paths; only its publication filename changes.
The unchanged A2 scorer is included for the public analysis contract.

These six files contain no vendor or model names, absolute local paths,
credentials or persona records. `executor.py` and `reservations.py` name
infrastructure, so they are **hash-only**, as are private configuration and
engine manifests. Runtime configuration, tests, briefs, this operator's
runbook, GO receipts, downloads, panels and raw run artifacts are not public
files. Publication and execution await approval and coordinator review.
