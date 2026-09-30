# Frozen recall protocol

No probe has been sent. After public registration and coordinator GO, use the browsing
role in a fresh context, without tools or browsing, temperature 0 and at most 300 output
tokens. One attempt per study; a failed request is unknown, not a negative recall.
Keep every raw response. Never put probe answers into persona or browser contexts.
Use a request with no extra reasoning-token allowance, retry or fallback. A valid response
has the requested JSON keys: a boolean self-report, an allowed direction string, rates that
are null or finite numbers in [0,1], a null or nonnegative sample size, a string detail and
a finite confidence in [0,100]. No discretionary prose repair. A malformed response is
unknown. Parse and classify locally; do not ask another model to repair it.

Exact common prompt, with `{citation}` and `{contrast}` taken from the table below:

> Without searching or using tools, do you remember the published result of {citation},
> specifically {contrast}? Report whether you recall this particular experiment rather
> than inferring what ought to happen. If you remember, give the direction, both condition
> rates, the approximate sample size, and one distinctive procedural detail. If you do not
> remember, say so. Return JSON with keys remembers (boolean), direction (A/B/tie/unknown),
> rate_a (number between 0 and 1 or null), rate_b (number between 0 and 1 or null),
> sample_size (number or null), detail (string), and confidence (0 to 100).

| ID | citation | contrast |
|---|---|---|
| R01 | Luguri and Strahilevitz, Shining a Light on Dark Patterns (2021), Study 1 | A plain subscription offer versus B the mild dark-pattern package; acceptance among completers |
| R02 | Luguri and Strahilevitz, Shining a Light on Dark Patterns (2021), Study 2 | A content-control versus B hidden-information initial offer, pooled over form conditions |
| R03 | Utz and colleagues, (Un)informed Consent (2019), Experiment 1 | A top bar versus B bottom-left notice, any interaction among desktop visitors |
| R04 | Utz and colleagues, (Un)informed Consent (2019), Experiment 2 | A optional purpose boxes unchecked versus B prechecked, all-purpose agreement among desktop visitors |
| R05 | Utz and colleagues, (Un)informed Consent (2019), Experiment 3 | A data wording versus B cookie wording, no policy link in either; any interaction among desktop visitors |
| R06 | Machuletz and Bohme, Multiple Purposes, Multiple Problems (2020) | A control versus B deception T1, agreeing to all three purposes |
| R07 | Grassl and colleagues, Dark and Bright Patterns in Cookie Consent Requests (2021), Experiment 2 | A baseline versus B refusal-default-only condition, agreeing to tracking |
| R08 | Chandrashekar and colleagues, Defaults versus framing (2023), health survey subscription task | A positive versus B negative wording, both no-default; consent to future surveys |

Classify **positive** if `remembers=true`, even when the claimed memory is wrong; also
positive when both rates are within 0.03 absolute of the frozen reference and direction
is correct, regardless of the self-report. This second criterion alone is not proof of
memorization. Classify **negative** only for a valid response with `remembers=false`
that does not meet the rate criterion. Everything else is **unknown**. Treat unknown
as potentially contaminated in conservative reporting. The procedural detail and claimed
sample size are reported verbatim but do not trigger discretionary recoding.

R07's criterion uses the selected complete-pair rates in human.json. A recalled rate for
another archive subset may be real memory; the self-report criterion still captures it.
Use a deterministic local comparison, never a paid judge. Eight experiment prompts are
asked even where a paper is shared. Do not retry a weak recall answer or exclude an item
because the probe is positive.

This is a **guided self-report/result-recall probe inspired by H4**, not H4's verbatim
headline-completion test. A negative answer cannot establish absence of training exposure.
Report the fixed fame split independently of the observed recall split.
