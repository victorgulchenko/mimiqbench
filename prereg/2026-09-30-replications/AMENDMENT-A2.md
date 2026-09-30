# R1 amendment A2: R06 not run, scored as a direction miss

Prepared 2026-09-30; approved by Victor in chat (“13”). Effective only after
publication in the public register and a separate coordinator GO-A2 receipt
naming A2, this document's SHA-256 and its public commit. This amendment changes
only the handling of R06. The original registration and A1 remain historical
records; no other frozen decision changes.

## Facts before exposure

Both paid attempts stopped at R06 recruitment with
`StopRun: Recruitment returned too few unique people or unparsed criteria`.
Each returned exactly 70 of the required 80 people. The original audience was
“German-speaking CS undergraduates”; A1 widened it to technical-subject
undergraduates. Neither attempt reached R07 or R08 recruitment.

The population audit supplied with the A2 brief found **no student occupation in
the 5.5-million-person skeleton pool**. Among 6,603 Austria/Germany skeletons
aged 18–22, occupations include nurse, shopkeeper, sales and driver; 1,915 (29%)
hold a Master's, MBA or PhD. The 70 apparent “students” came from hydration
narratives, not student occupations in the population. Changing recruitment
wording cannot honestly fill this university-student panel. A2 does not repair
or regenerate the population, invent eligibility, or use either partial panel.

**no page was shown to anyone before this amendment**: both attempts have zero
simulation sessions and no recall probes. Earlier local browser QA involved no
participants or model calls. This is a pre-exposure feasibility amendment;
there are no behavioral outcomes on which to select a change.

| Attempt | UTC start → stop on 2026-09-30 | Recruitment spend USD |
|---|---|---:|
| Original R1 | 15:58:37 → 16:29:17 | 0.875806 |
| A1 | 17:01:07 → 17:05:55 | 0.135288 |
| Cumulative | Both stopped before exposure | **1.011094** |

All reservations settled. The charges include the ledger safety margin and
remain against the unchanged $15 lane and $2 recruitment subcap. Before A2,
$13.988906 remains in the lane and $0.988906 in recruitment; the shared lab cap
also binds. The recall subcap remains $0.50. Stop records are zero-dollar
metadata and do not recharge these amounts.

## Exact scoring amendment

- R06 is **not run**. It gets **direction MISS (0)** in the primary R1.1 suite
  metric. It is retained in the denominator of **eight**. The **7/8** pass bar
  is unchanged: all seven remaining studies must match direction.
- Every required outcome in those seven studies must still be resolved, with
  valid recall classifications, to produce PASS or FAIL. Other missing outcomes,
  failed recruitment or interrupted execution remain INCOMPLETE. R06 alone does
  not make the suite INCOMPLETE under A2.
- R06's human reference stays byte-for-byte unchanged in `human.json`. Its report
  row reads **“not run: the simulated population contains no university
  students”**. No synthetic persona IDs, choices, rates, effect estimates or
  recall replies are manufactured for it. Its simulated effect and magnitude
  error remain null. Its per-study `complete` flag remains false; it is resolved
  administratively only for the primary suite metric.
- R1.2 magnitude and R1.3 contamination use the seven studies that run. R06 is
  explicitly absent from both, including the fame/recall splits and R1.3's
  overall comparison share. R1.3 retains its minimum of three recall-negative
  studies and 15-percentage-point tolerance; unknown probes are not negative.
- Primary descriptive intervals and coin-tail calculations retain n=8. Primary
  source-group summaries retain R06 as a zero. All per-study statistics for the
  remaining studies use the unchanged original scorer.

## Execution and retained evidence

R01–R05 reuse their original hashed panels, byte-for-byte and in their original
order, after verification of both stopped attempts and every retained artifact.
R06 is skipped in recruitment, recall and exposure, with the reason above.
R07 and R08 are recruited once as registered. Filtering only R06 from the
registered schedule leaves 520 sessions and 560 scheduled outcome records
(R07 contributes a pair per session), with seven recall probes. Audiences,
stimuli, assignment, metrics outside this amendment, model roles, settings,
budget and subcaps do not change.

A2 requires a fresh output directory and fresh dry/QA receipts. Its restart
source is the stopped A1 attempt, which identifies the original attempt; panels
are copied from the original. The original and A1 evidence remain immutable.
Both stops, their spend and A2 spend appear in the new report. All ledger rows
must reconcile to both pinned states before A2 can claim its single execution.
There is **one execution per amendment across all output directories**. A2 is
not permission for another draw or exposure after a later stop.

| Retained private evidence (hashes only) | SHA-256 |
|---|---|
| Original state.json | `1caf2b953e5532923ae05d7af090c412dae07780613adeefc232a17eabdb3955` |
| Original artifacts.sha256.json | `0327d7fc92b66d0a7c254074d72dbfabfc35ab1d99b671cb51577dceec0e832d` |
| A1 state.json | `2206a2458cec8d15d5ec5189bf3e13c5c34739183dbb89c053a64f7265b95732` |
| A1 artifacts.sha256.json | `878a6d20b0115e6e787d1be29c76b69d68ed7cece7fa43bb2b41554c5f7656ec` |
| R01 panel | `db2ecb49e117a33d421b7b3687f6e6ca2afab375ace2235f8e948949ab946c94` |
| R02 panel | `a5620a6c910be53e28db0cae0f23d3b21d186cb34638cb577e8fb3cb4b237209` |
| R03 panel | `54b6687d74a8f6c2f7a11796431ed3b29279d342f44a933d7f12e0675270bb05` |
| R04 panel | `6e1c6628dbfda6a3dd0a7b615f80e3a3bb207ea558b7135b9a1770484a4b48a6` |
| R05 panel | `afc86350e90ebda53a7c8bc2c8358aacffadb6a37c1c7b432b771e8f80c53cf6` |

## Updated freeze

`FROZEN.pre-A2.sha256` preserves the A1 manifest byte-for-byte. Every one of its
20 entries remains unchanged in `FROZEN.sha256`; five new entries pin the A2
executor, report adapter, restart and ledger guards, and versioned scorer.
`score.py` is unchanged. `score_a2.py` applies only the rule above and calls the
original scorer for outcome validation and per-study statistics. This document
is hashed separately in GO-A2 to avoid a self-referential document digest.
The offline authorization module holds the exact new manifest/document hashes;
dry and QA receipts also fingerprint the full executor Python file set.

<!-- A2-HASHES-START -->
| File | SHA-256 |
|---|---|
| FROZEN.pre-A2.sha256 | `7477959c71b4a94ff94e775c66d29961ab8e8ffc78614dee450598bcf7033cf6` |
| FROZEN.sha256 | `dadd7c599de35ded0889be04a58c469153dd59599d00f22cdee65664d184971b` |
| executor.py | `d53132ca6a39f5545ab276c2a14fe5691215d031969d5a5aef1cb170f0c71b04` |
| outcomes.py | `9f845a7009298ea88bc79dc292593a98189550901b2893918602795a8168ff5c` |
| restart.py | `f237564c1fc54d6a2e8f9b4ebfc0d76e062bc5b2a01c064f733fe55d3a28b1e1` |
| reservations.py | `a9746f17ce5f697accf28b1a665b18ae254c5fbdb553ecdaa5dcbbdce0fa66dc` |
| score_a2.py | `ea2cb75fc0e1c5807a457e87b367ddd2b06a2a2043b87f2c79877315e8dc4d22` |
| score.py | `6c246bb714dcfa5b1c0dd14c5e2a824ba21a832934eb1280dd8be4eccabda27f` |
| human.json | `37d53d9680782baa9a05eaf7f5f18e5cf6bcdcc8e0e1d75bf3a53b67a22d73e5` |
| audiences.json | `b89c0f54fdc371eaea8437af4ee02f9eba4a4dd9b84a1efc187eadd63f661267` |
| REGISTRATION.md | `2a866051834de205904fad91fd9281dcf7b08e783dd06eab27e774d5b04b2ca0` |
<!-- A2-HASHES-END -->

Public files belong in `prereg/2026-09-30-replications/` in the register. Publish
this document, the updated manifest, and the three newly pinned files that
contain no infrastructure details: `score_a2.py`, `outcomes.py` and `restart.py`.
`executor.py` and `reservations.py` name infrastructure, so like the private
configuration and engine files they are represented only by their hashes above
and in the manifest. Do not publish persona data, run artifacts, local
paths, source downloads or credentials.
