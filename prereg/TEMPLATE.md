# Plan: <suite>, <what is tested>

Pushed: <date> (the commit that adds this file is the timestamp). Nothing below changes
after the run starts; results and deviations go in RESULTS.md next to this file.

## Question

The one question this run answers, and the hypotheses, each with its direction.

## Data

- Source, license, dates, audience, and what counted as success.
- Held-out items: file, count, sha256. How they were split from the development set
  (seed), and which positions earlier runs already used.
- Exclusions, stated before the run.

## Method (frozen)

- Code: commit and sha256 of every file that makes a call or scores one.
- Models by role (for example "the forecast's model"), with the sha256 of the private
  configuration file that names them; prompts, temperature, how many calls per item, what
  happens on an error or an unparseable answer.
- What the method is shown, and what it is never shown.

## Primary metric

How it is computed, with the interval method and the paired test against each baseline.

## Baselines

A coin, the best simple rule for this suite (named, with its development-set score),
and human forecasters where the source published them.

## Pass lines

The numbers that count as success or failure, set now.

## Secondary checks

Memorization (recall and rewording), position bias, calibration by tier, near-ties.

## Cost and stopping

Expected spend, the budget cap, and what happens if the run stops early.
