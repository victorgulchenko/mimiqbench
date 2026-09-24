# Plan: wikimedia-banners, which donation banner raises more money

Final, 2026-09-24. Written by the proof lane from 34 dev pairs; no model has seen any held-out item. The
commit that adds this file to the public register is its timestamp. Nothing below changes after that;
results and deviations go in RESULTS next to it.

Mimiq keeps its choice of AI models confidential, so this plan names models by role only (the
forecast's model). Its exact identity and settings are fixed by a private configuration file whose
sha256 is below; the run refuses to start if that file differs by one byte.

## Question and hypothesis

For real fundraising banners on German Wikipedia (Wikimedia Deutschland, 2012 to 2014), does Mimiq's
forecast pick the banner that raised more donations per impression? This is the only `ad` suite so
far; the banners are text (no images).

- H1 (primary): Mimiq's forecast picks the banner that raised more more often than not: the lower end of
  the Wilson 95% interval on the winner pairs is above 50%.

## Data

- Source: Wikimedia Deutschland's public test reports on Wikimedia's project coordination wiki (2012,
  2013, 2014) and each banner's source page; CC BY-SA 4.0.
- Suite `wikimedia-banners`, split by test, seeded (20260924). Held-out: 66 pairs (28 clear, 9 likely,
  17 unclear, 12 ties); 37 with a winner.
- items.jsonl sha256 `16ca52d3730cdf228682f160671844641333aa7b62b330d8a27270644ec651a7`. The sample is
  held-out positions 1 to 66; sample ids sha256
  `1d4adbbca5c8599442be02483fc10084c823b8f4920e6d6e2b79f6ae3c8cce58`.
- Exclusions, fixed now: a pair whose forecast cannot be parsed in either order, after production's
  retries, is left out and counted.

## Method

Mimiq's forecast on the 66 held-out pairs, exactly as the app's compare call makes it for an ad without
an image (the banner text is the content; kind `ad`, the item's audience, both orders; a pick when both
orders agree), the forecast's model. No simulated people in this plan.

## Primary metric

Accuracy on the 37 winner pairs, a no-pick counting half; Wilson 95% interval. Pairs from the same test
share a banner, so the pairs are not fully independent and the Wilson interval is somewhat too narrow;
the report says so next to it. Code: `benchmarks/mimiqbench/confirm.py`, `score.py`.

## Baselines

A coin (50%), and the rule of thumb named now from the 34 dev pairs: "the shorter banner text" (60.7% on
the 14 dev winner pairs, chosen on them). No human forecasts exist.

## Pass line (set now)

H1 passes if the lower end of the Wilson 95% interval is above 50%.

What dev showed (exploratory): 60.7% (35.6 to 81.2) on 14 winner pairs; it still picked on 60.0% of 10
near-ties. Power is low: with 37 winners, H1 needs a true accuracy near 75% to pass reliably. A fail
here means "not shown", not "shown wrong".

## Secondary checks

How often it still picks on the 12 ties; accuracy by the strength of the real difference; position
bias.

## Configuration, code and the gate

- Private configuration: `benchmarks/mimiqbench/configs/wikimedia-banners.json`, sha256
  `17f10657856b2dda2700145e9e2c8d38eb5fe35132b2204893835e7a40b26962`.
- Code hash `6da3ec99b24026c35b235ced532a2d65910009e876a22203b8a850f5ff06eeaf` (32 code units).
- The runner (`benchmarks/mimiqbench/plans.py`, `check`, called by `runner.run` for every held-out
  step) refuses to run unless the GO line names this file's sha256 and the public commit, the
  configuration's sha256 matches, the items and sample hash as above, no sample id appears in any earlier
  cache, and every code unit is unchanged (or a deviation is declared and reported).

## Cost and stopping

About $0.55; cap $1.00. If the cap stops the run, the analysis uses every completed pair and reports the
shortfall.

## What we publish whatever happens

Every number above with its interval, including those against Mimiq; the sample and its hashes; every
deviation.
