---
number: 157
status: Active
formerly:
- CASE-tmpffs67
title: 'Boosting the vote: in the owner''s 2014 model, voters of fixed accuracy drawn from Beta(2, 2) vote in a weight-averaged election, and every voter''s weight is multiplied by 1 + f when their own vote was right and 1 − f when not, with a fraction replaced each round at weight 1; with full-information feedback the weighted result rises from 0.50 toward 0.98 as f grows, and churn only costs in a world that never changes; the model escapes the hive mind''s absorbing states because every voter is scored, heeded or not, and it assumes away the capture its author predicted'
version: 2
history:
- version: 2
  date: '2026-10-25'
  note: >-
    A dated note added: A47 found two of the extension's outcomes
    independently (CASE-158). The case is unchanged.
standing: stipulated
kind: executed-study
tags:
- self-governance
- learning-theory
- society-and-governance
date: '2026-10-24'
line: distributed-agency
illustrates:
- CLAIM-444
variant_of:
- CASE-155
summary: >-
  Filed at the owner's direction, 2026-10-24, after the owner suggested
  taking inspiration from the experiments in dmarx/BoostTheVote. A
  thought-experiment written in R in 2014, read at commit b5bca8f and
  re-run here through a Python port (scratch/formal/boost_the_vote.py).
  It is the full-information counterpart of the replicator construction.
  What it shows, what it assumes, and the three-axis extension it suggests
  are recorded, and the extension was run on 2026-10-25.
---
<!-- inactive-ok-file: CASE-155 CLAIM-444 QUESTION-271 THEORY-938 CLAIM-446 — Proposed or new; the construction, claim and question this bears on -->

# CASE-157: Boosting the vote: in the owner's 2014 model, voters of fixed accuracy drawn from Beta(2, 2) vote in a weight-averaged election, and every voter's weight is multiplied by 1 + f when their own vote was right and 1 − f when not, with a fraction replaced each round at weight 1; with full-information feedback the weighted result rises from 0.50 toward 0.98 as f grows, and churn only costs in a world that never changes; the model escapes the hive mind's absorbing states because every voter is scored, heeded or not, and it assumes away the capture its author predicted

## The case

**The model** (dmarx/BoostTheVote, `boost_the_vote.R` and `writeup.Rmd`,
November 2014).
- *Voters.* Each voter has a fixed accuracy, the probability that their
  vote contributes to a good outcome, drawn from Beta(a, b).
- *Election.* The result is the weight-averaged vote.
- *Update.* After each election every voter's weight is multiplied by
  1 + f if their own vote was right and by 1 − f if not: multiplicative
  weights, in the weighted-majority family.
- *Churn.* Each round a fraction of voters is replaced, the older more
  likely, by fresh voters at weight 1.

The write-up treats each voter as a classifier and the election as an
ensemble to be reweighted.

**Re-run.** A Python port, scratch/formal/boost_the_vote.py: 1000 voters,
Beta(2, 2), 30 elections, 50 runs per cell. Median weighted result after
the 30th election:

| f | churn 0 | churn 0.1 | churn 0.3 |
|---|---|---|---|
| 0 | 0.50 | 0.50 | 0.50 |
| 0.2 | 0.82 | 0.62 | 0.53 |
| 0.5 | 0.91 | 0.85 | 0.58 |
| 0.8 | 0.98 | 0.92 | 0.62 |

The spread widens with f, as weight concentrates. The port differs from the
R code in one respect, as its header says. The R code never resets a
replaced voter's age, so newcomers inherit their predecessor's risk of
being replaced. That looks unintended.

## What it shows

- **Full-information feedback.** Every voter's vote is scored against the
  outcome, whether or not it decided anything. That is the experts setting,
  where the hive mind ([THEORY-899](../theory.d/THEORY-899.md)) and plain Q-learning
  ([THEORY-932](../theory.d/THEORY-932.md)) get bandit feedback. Two consequences:
  - weights never reach zero, so a low-weight voter who keeps voting well
    climbs back;
  - access and authority come apart, since a voter keeps voting and being
    scored while holding little weight.

  So the model is the replicator construction's evidence-tracking regime
  ([CASE-155](CASE-155.md), part 1) without that regime's absorbing edges. It
  satisfies the first of [CLAIM-444](../claims.d/CLAIM-444.md)'s three conditions by design.
- **Churn is renewal.** Replacement is turnover, of the kind March found
  useful ([THEORY-142](../theory.d/THEORY-142.md)), and age-weighted replacement works like term limits.
  In a stationary world it only costs: the table's columns fall left to
  right. Its value has to show when what counts as right changes, which
  the original never tests.

## What it assumes away

- **The metric.** The model needs an objective measure of a good outcome.
  The write-up says such a metric "probably/almost certainly cannot" be
  constructed, which is [QUESTION-271](../questions.d/QUESTION-271.md)'s failure 2.
- **Capture.** The disclaimer predicts that the process "would be corrupted
  to bring about whatever outcome the people in control of the processes
  wanted". That is failure 3, and [CASE-155](CASE-155.md)'s self-scoring c, stated
  before the record existed.
- **Cycles.** One binary question cannot produce Condorcet cycles
  (failure 1).

## The extension it suggests

Three axes, crossed, with a world whose truth changes partway through:
1. **Feedback.** Full information, bandit (only the votes that carried the
   decision are scored), and a parameter for the fraction of unheeded votes
   still scored. That parameter is a legibility dial ([CASE-124](CASE-124.md)).
2. **Who defines the metric.** An independent metric, or one set by the
   currently highest-weight voters, which makes c endogenous.
3. **Renewal.** Churn rate, and whether it targets age or weight.

The prediction, as filed before the run: the record's anxiety, protection
and legibility claims ([CLAIM-446](../claims.d/CLAIM-446.md), [CLAIM-445](../claims.d/CLAIM-445.md), [CASE-156](CASE-156.md))
predict that lock-in needs both bandit-like feedback and an endogenous
metric, and that renewal pays only under change. Lock-in under full
feedback with an independent metric would count against them. So would
none under bandit feedback with an endogenous metric. Börgers and Sarin's
lock-in by reinforcement alone ([THEORY-938](../theory.d/THEORY-938.md)) is the null to beat.

## The extension, run 2026-10-25

At the owner's direction, scratch/formal/boost_the_vote_extension.py.

**Design.**
- *Voters.* Voters now have fixed leans, voting 1 with probability
  p_i ∼ Beta(2, 2) whatever the truth, so who is right changes when the
  truth does.
- *Phases.* The truth is 1 for 30 elections and 0 for the next 60.
- *Scoring.* f = 0.2 and N = 1000. The decision is the weighted majority.
  Heeded voters are always scored; unheeded ones with probability ρ.
- *Metric.* With probability m per election, the standard voters are
  scored against is the collective's own decision. Since the decision is
  the weighted majority, that is the standard of the highest-weight voters
  taken together.
- *Renewal.* Either none, or 5% replaced each round, by age or as the
  highest-weight voters, a term limit.
- *Runs.* 100 per cell, reporting means.

Selected cells:

| ρ | m | renewal | right before switch | right after switch | right at end | delay to 5 right in a row |
|---|---|---|---|---|---|---|
| 1 | 0 | none | 0.98 | 0.49 | 1.00 | 32 |
| 1 | 0 | age | 0.98 | 0.88 | 1.00 | 7 |
| 1 | 0.25 | none | 0.97 | 0.11 | 0.59 | 55 |
| 1 | 0.5 | none | 0.88 | 0.06 | 0.07 | 57 |
| 1 | 0.5 | age | 0.88 | 0.66 | 1.00 | 21 |
| 1 | 1 | none | 0.53 | 0.47 | 0.47 | — |
| 0 | 0 | none | 0.97 | 0.58 | 1.00 | 26 |
| 0 | 0.5 | none | 0.91 | 0.02 | 0.05 | 59 |
| 1 | 0 | top-weight | 0.21 | 0.42 | 0.00 | — |

A fourth axis was added once the first run showed that bandit feedback
over voters is not the record's bandit concern. Under *observability*, the
outcome is observed only when the collective acts (decides 1); avoiding
yields no observation. The truth then switches 0 → 1, so the old answer is
avoidance. With an independent metric and no renewal, 36% of runs (ρ = 1)
and 42% (ρ = 0) were right at the end, with a delay of about 48 elections.
With age renewal, all were right, with a delay of about 8.

**Findings, against the prediction.**
1. **No lock-in with full feedback and an independent metric.** That
   falsifier was not triggered. But recovery took about as long as the
   training had: 32 elections after 30. That is weight inertia, not
   lock-in.
2. **An endogenous metric suffices for lock-in under full feedback.** At
   m = 0.5, 93% of runs were still wrong at the end; even m = 0.25 left 41%
   wrong. Bandit feedback is not needed. "Needs both" is wrong.
3. **Bandit feedback over voters changes little.** In a binary decision,
   penalizing the heeded side when it is wrong is itself informative about
   the other side. The bandit feedback that matters is over outcomes.
4. **Outcome-conditional observation suffices too.** With an independent
   metric, avoidance alone held about 60% of runs on the old answer for the
   whole second phase. Escape came only when vote noise tipped a decision
   into acting. This is [CLAIM-446](../claims.d/CLAIM-446.md)'s identifiability step reproduced.
5. **Renewal pays under change and costs little before it.** Age-targeted
   renewal rescued every case except the fully endogenous one, which is a
   coin-flip lock from the first elections: the decision never changes.
   Its cost before the switch was at most a few points. Term limits on the
   highest weights destroyed learning altogether: removing the competent
   every round is not renewal.

So two routes to lock-in each work alone: a metric partly set by those in
charge, and feedback conditional on acting. Age-like renewal defeats both
short of full endogeneity. One parameterization, binary decisions,
symmetric leans: the thresholds are illustrative, not estimates.

## What it cannot show

Anything about real electorates. Its author disclaimed the idea's
desirability and called it "very likely morally objectable". The case is
filed for its dynamics, not as a proposal.

## Note of 2026-10-25: an independent convergence

A47 of the exchange of 2026-10-24, continued, reported at 03:12 UTC on
2026-10-25, 42 minutes before this case's extension was committed, found
the same two outcomes in a different model. Full-information, independent
audits recovered after a reversal of expertise (findings 1 and 5).
Conformity scoring, an endogenous metric, held the old allocation (finding
2). The run is not held ([CASE-158](CASE-158.md)). The case is unchanged.
