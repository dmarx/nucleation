---
status: Active
title: 'Boosting the vote: in the owner''s 2014 model, voters of fixed accuracy drawn from Beta(2, 2) vote in a weight-averaged election, and every voter''s weight is multiplied by 1 + f when their own vote was right and 1 − f when not, with a fraction replaced each round at weight 1; with full-information feedback the weighted result rises from 0.50 toward 0.98 as f grows, and churn only costs in a world that never changes; the model escapes the hive mind''s absorbing states because every voter is scored, heeded or not, and it assumes away the capture its author predicted'
version: 1
standing: stipulated
kind: executed-study
tags:
- self-governance
- learning-theory
- society-and-governance
date: '2026-10-24'
line: distributed-agency
illustrates:
- CLAIM-tmp1xoac
- QUESTION-tmpdicvf
variant_of:
- CASE-tmpw4r7u
summary: >-
  Filed at the owner's direction, 2026-10-24, after the owner suggested
  taking inspiration from the experiments in dmarx/BoostTheVote. A
  thought-experiment written in R in 2014, read at commit b5bca8f and
  re-run here through a Python port (scratch/formal/boost_the_vote.py).
  It is the full-information counterpart of the replicator construction.
  What it shows, what it assumes, and the three-axis extension it suggests
  are recorded.
---
<!-- inactive-ok-file: CASE-tmpw4r7u CLAIM-tmp1xoac QUESTION-tmpdicvf THEORY-tmp3oyxw THEORY-tmpar5jw THEORY-tmphhvqf CLAIM-tmp8z857 — Proposed or new; the construction, claim and question this bears on -->

# CASE-tmpffs67: Boosting the vote: in the owner's 2014 model, voters of fixed accuracy drawn from Beta(2, 2) vote in a weight-averaged election, and every voter's weight is multiplied by 1 + f when their own vote was right and 1 − f when not, with a fraction replaced each round at weight 1; with full-information feedback the weighted result rises from 0.50 toward 0.98 as f grows, and churn only costs in a world that never changes; the model escapes the hive mind's absorbing states because every voter is scored, heeded or not, and it assumes away the capture its author predicted

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
  where the hive mind ([THEORY-tmp3oyxw](../theory.d/THEORY-tmp3oyxw.md)) and plain Q-learning
  ([THEORY-tmpar5jw](../theory.d/THEORY-tmpar5jw.md)) get bandit feedback. Two consequences:
  - weights never reach zero, so a low-weight voter who keeps voting well
    climbs back;
  - access and authority come apart, since a voter keeps voting and being
    scored while holding little weight.

  So the model is the replicator construction's evidence-tracking regime
  ([CASE-tmpw4r7u](CASE-tmpw4r7u.md), part 1) without that regime's absorbing edges. It
  satisfies the first of [CLAIM-tmp1xoac](../claims.d/CLAIM-tmp1xoac.md)'s three conditions by design.
- **Churn is renewal.** Replacement is turnover, of the kind March found
  useful ([THEORY-142](../theory.d/THEORY-142.md)), and age-weighted replacement works like term limits.
  In a stationary world it only costs: the table's columns fall left to
  right. Its value has to show when what counts as right changes, which
  the original never tests.

## What it assumes away

- **The metric.** The model needs an objective measure of a good outcome.
  The write-up says such a metric "probably/almost certainly cannot" be
  constructed, which is [QUESTION-tmpdicvf](../questions.d/QUESTION-tmpdicvf.md)'s failure 2.
- **Capture.** The disclaimer predicts that the process "would be corrupted
  to bring about whatever outcome the people in control of the processes
  wanted". That is failure 3, and [CASE-tmpw4r7u](CASE-tmpw4r7u.md)'s self-scoring c, stated
  before the record existed.
- **Cycles.** One binary question cannot produce Condorcet cycles
  (failure 1).

## The extension it suggests (not run)

Three axes, crossed, with a world whose truth changes partway through:
1. **Feedback.** Full information, bandit (only the votes that carried the
   decision are scored), and a parameter for the fraction of unheeded votes
   still scored. That parameter is a legibility dial ([CASE-124](CASE-124.md)).
2. **Who defines the metric.** An independent metric, or one set by the
   currently highest-weight voters, which makes c endogenous.
3. **Renewal.** Churn rate, and whether it targets age or weight.

The record's anxiety, protection and legibility claims ([CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md),
[CLAIM-tmp28sti](../claims.d/CLAIM-tmp28sti.md), [CASE-tmpydmf8](CASE-tmpydmf8.md)) predict that lock-in needs both bandit-like
feedback and an endogenous metric, and that renewal pays only under change.
Lock-in under full feedback with an independent metric would count against
them. So would none under bandit feedback with an endogenous metric.
Börgers and Sarin's lock-in by reinforcement alone ([THEORY-tmphhvqf](../theory.d/THEORY-tmphhvqf.md)) is the
null to beat.

## What it cannot show

Anything about real electorates. Its author disclaimed the idea's
desirability and called it "very likely morally objectable". The case is
filed for its dynamics, not as a proposal.
