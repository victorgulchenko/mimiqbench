# R1 amendment A1: R06 recruitment eligibility

Prepared 2026-09-30; approved by Victor in chat (“11 yes”). This document takes
effect only after publication in the public register and a separate coordinator
GO-A1 receipt naming its SHA-256 and public commit. The original R1 registration
remains unchanged; this amendment supersedes only its R06 audience restriction.

## Why this amendment is needed

The first paid attempt stopped during recruitment with
`StopRun: Recruitment returned too few unique people or unparsed criteria`.
R01–R05 were recruited and saved with hashes. R06 returned 70 people against the
required 80; R07 and R08 were not reached. The Austria pool has approximately
3,844 personas in total, and the narrow computing-undergraduate audience could
not fill the panel with explicit eligibility evidence.

**No page was shown to any recruited participant before this amendment: zero
simulation sessions were attempted.** No recall probes were sent. Prior local
browser QA exercised controls without participants or model calls; it is not
experimental exposure. This is a feasibility amendment before exposure, not a
change prompted by behavioral outcomes.

The attempt ran from 2026-09-30 15:58:37 UTC to 16:29:17 UTC and incurred
**$0.875806** in recorded recruitment charges (including the ledger safety
margin), approximately $0.88. All reservations were settled. These charges
remain in the shared ledger and count against the unchanged $15 lane and $2
recruitment subcap. A zero-dollar stop entry records the failure without charging
that spend again. The final amended report must retain this stop and spend.

## Exact R06 text before and after

Before — `audience`:

> German-speaking undergraduate computer science students, mostly in their first year, taking part in a classroom study of flight-search user experience. Approximately 60 percent attend university in Austria and 40 percent in Germany.

After — `audience`:

> German-speaking undergraduate students in technical subjects (computer science, engineering, mathematics, physics) at universities in Austria or Germany, mostly in their first year, taking part in a classroom study of flight-search user experience. Approximately 60 percent attend university in Austria and 40 percent in Germany; this is a preference, not a hard rule.

Before — `hard_eligibility`:

> Austria or Germany; German-speaking computing undergraduate; adult

After — `hard_eligibility`:

> Austria or Germany; German-speaking undergraduate in a technical subject; adult

The 60/40 Austria/Germany mix is a preference, never a rejection quota. The
subject expansion is limited to computer science, engineering, mathematics and
physics. Adult age, German language, undergraduate status and country remain
hard requirements, supported by explicit persona evidence.

`audiences.json` now carries version `R1-A1`. R06's stimulus, goal, context,
locale, timezone, n=80, seed=20260936 and scoring stay as registered. All other
studies, the 7/8 pass bar, metrics, $15 total lane, $2 recruitment and $0.50 recall
subcaps are unchanged. No other frozen input changes.

## Restart and evidence retention

R01–R05 must reuse their exact saved panels, in their original order, after
verifying the state and artifact hashes below and each panel hash. They are
not recruited again. The failed R06 draw is retained as evidence; a new R06
draw uses A1. R07 and R08 are recruited for the first time. No partial R06 panel
is topped up, relabeled or substituted for the registered n.

The original failed attempt and its artifacts remain immutable. A1 writes to a
new output directory, requires fresh dry and browser-QA receipts, and permits
one paid execution only, enforced in the shared ledger across output directories.
It is not a general resume facility. Any later interruption or recruitment
failure stops the run; A1 cannot authorize another draw or re-exposure.

| Retained private evidence (hashes only) | SHA-256 |
|---|---|
| First attempt state.json | `1caf2b953e5532923ae05d7af090c412dae07780613adeefc232a17eabdb3955` |
| First attempt artifacts.sha256.json | `0327d7fc92b66d0a7c254074d72dbfabfc35ab1d99b671cb51577dceec0e832d` |
| R01 panel | `db2ecb49e117a33d421b7b3687f6e6ca2afab375ace2235f8e948949ab946c94` |
| R02 panel | `a5620a6c910be53e28db0cae0f23d3b21d186cb34638cb577e8fb3cb4b237209` |
| R03 panel | `54b6687d74a8f6c2f7a11796431ed3b29279d342f44a933d7f12e0675270bb05` |
| R04 panel | `6e1c6628dbfda6a3dd0a7b615f80e3a3bb207ea558b7135b9a1770484a4b48a6` |
| R05 panel | `afc86350e90ebda53a7c8bc2c8358aacffadb6a37c1c7b432b771e8f80c53cf6` |

## Updated freeze

The original manifest is preserved byte for byte as `FROZEN.pre-A1.sha256`.
The new `FROZEN.sha256` changes only the `audiences.json` entry; every other
entry and frozen file is identical. It lists all 20 frozen inputs, including
hashes only of the two private files. This document is separately hashed in
GO-A1, avoiding a self-referential manifest/document digest.

| File | SHA-256 |
|---|---|
| FROZEN.pre-A1.sha256 (original manifest) | `1ed4cb753d3fe8d5cb8e9aab9298702fee55ff075983fa252534afb327ceee6c` |
| FROZEN.sha256 (A1 manifest) | `7477959c71b4a94ff94e775c66d29961ab8e8ffc78614dee450598bcf7033cf6` |
| audiences.json before A1 | `433b54f15b397c102cd24b1d22a0735ad38ed9f5bfc4860a3db8839890146cf6` |
| audiences.json version R1-A1 | `b89c0f54fdc371eaea8437af4ee02f9eba4a4dd9b84a1efc187eadd63f661267` |
| REGISTRATION.md (unchanged) | `2a866051834de205904fad91fd9281dcf7b08e783dd06eab27e774d5b04b2ca0` |

Public publication includes this document, the two manifests and the new
audience file. Private configuration, engine manifests, personas, raw run
artifacts, local paths and credentials are excluded.
