---
number: 347
status: Proposed
formerly:
- CASE-tmprsqvj
title: 'Three simulated populations with matched turnover and aggregate statistics, run through a priced lagged block test and an information profile: the transmitting population is found with its lag, the commonly driven and the institutional populations are each joined to their external variable alike, and the common input is rejected only while it is observed'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-026. Scripts,
    tests and results are under scratch/studies/lead-026/.
standing: documented
kind: executed-study
tags:
- individuation
- information-theory
- complex-systems
- causality
date: '2026-11-22'
line:
- distributed-agency
variant_of:
- CASE-101
bears_on:
- QUESTION-115
- QUESTION-116
draws_on:
- THEORY-424
- THEORY-257
- THEORY-1163
summary: >-
  [LEAD-026](../leads.d/LEAD-026.md) asked for [CASE-101](CASE-101.md)'s three populations to be run through
  [QUESTION-115](../questions.d/QUESTION-115.md)'s search and a lagged block criterion ([QUESTION-116](../questions.d/QUESTION-116.md)). Four
  populations of six member slots with the same turnover were simulated,
  matched in member variance, member correlation and the aggregate's lag-1
  autocorrelation: common input (A), norms transmitted at a lag of eight
  steps (B), an institution that trains, selects and answers to its members
  (C), and the same institution deaf to them (C0). A block test priced by
  [CLAIM-154](../claims.d/CLAIM-154.md)'s rule, over all subsets and windows of 1 to 16 steps, finds
  B's members alone, with the strongest support at the transmission lag. It
  joins A's members to their driver and C's and C0's to their institution,
  the same verdict for all three. C differs only by a feedback the price
  removes beyond four steps, and A and C0 get the same verdict on every measure. With the
  external variable unobserved, every arm's members pass. Retention
  conditioned on the environment survives turnover only in B; Bourrat's
  interventional retention of B's members does not, since intervening on
  the present misses the stored norms. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-157 CLAIM-167 THEORY-257 LIT-005 — Proposed; the block criterion tested, the claim on one-way drive it is read with, the dynamical-independence reading, and Bourrat's paper -->
<!-- inactive-ok-file: CLAIM-926 — new, filed with this case -->

# CASE-347: Three simulated populations with matched turnover and aggregate statistics, run through a priced lagged block test and an information profile: the transmitting population is found with its lag, the commonly driven and the institutional populations are each joined to their external variable alike, and the common input is rejected only while it is observed

## What was done

[CASE-101](CASE-101.md) proposed three populations "with the same turnover and the
same aggregate statistics" as the place where criteria of individuality
should disagree. [LEAD-026](../leads.d/LEAD-026.md) asked for them to be run, with [QUESTION-115](../questions.d/QUESTION-115.md)'s
search procedure and a lagged block criterion ([QUESTION-116](../questions.d/QUESTION-116.md)) applied to
each. Nothing here is data about any real population; the case is
documented as a computation on a stated model.

**The populations.** Every arm has eight observed variables: six member
slots, one environmental variable e and an unrelated persistent distractor
z. Each step, each slot's occupant is replaced with probability 0.02, the
same in every arm. A slot's value is its occupant's norm.

- *A, common input.* e is an exogenous driver that every member responds
  to. Members do not interact. Newcomers arrive naive.
- *B, reproducing organization.* Members learn from the others' norms of
  eight steps earlier, and a newcomer copies a random member's norm of eight
  steps earlier. No coupling between members is synchronous. e is inert.
- *C, institutionally maintained.* e is an institution that trains members,
  selects newcomers near its standard, and shifts with the members' mean.
- *C0.* Arm C with an institution that does not answer to its members, so
  its coupling to them is one-way, as A's driver is.

For each arm, three parameters were calibrated so that member variance
(1.00), mean member correlation (0.40) and the aggregate's lag-1
autocorrelation (0.90) match, to three decimals in the simulated runs.
[CASE-101](CASE-101.md)'s note of 2026-10-29 asks the study to state which variables
are in E. E is every observed variable outside the candidate, and each
measure was also run with e removed from the observed set.

**The search, as [QUESTION-115](../questions.d/QUESTION-115.md) and A12 state it.** Information measures
find candidates, a priced block decides, and the result is a profile across
criteria rather than one score.

- *Retention.* Krakauer et al.'s A*, A and nC ([LIT-1137](../literature.d/LIT-1137.md)), with A11's
  lagged form A(Δ) for Δ from 1 to 64 steps.
- *Interventional retention.* Bourrat's Â ([LIT-005](../literature.d/LIT-005.md)), by [NOTE-027](../notes.d/NOTE-027.md)'s route:
  intervene on the candidate in the simulator, leaving E at its own
  distribution. The input distribution, which Bourrat leaves open, is the
  candidate's population marginal.
- *Dynamical independence* ([THEORY-257](../theory.d/THEORY-257.md)). Read as zero transfer entropy
  into the candidate from the rest, with histories of 1 and 16 steps.
- *The priced lagged block* ([CLAIM-157](../claims.d/CLAIM-157.md), lagged as [QUESTION-116](../questions.d/QUESTION-116.md) asks).
  - Fit a linear autoregression of window W, 1 to 16 steps, to all observed
    variables.
  - Price each group of couplings by [CLAIM-154](../claims.d/CLAIM-154.md)'s rule, ln BF(keep) =
    ½(d′² − Occam). d′² is the likelihood-ratio statistic, and the Occam
    cost is ln n per coefficient, from a unit-information prior. That prior
    is a choice made here, not the record's.
  - A candidate passes when the couplings across every cut inside it are
    kept and those across its edge are pruned.
  - The test was run on all 255 subsets at every window.

Effective information was not computed. It needs a discrete transition
matrix and a declared intervention distribution at each level, and the
populations here are continuous. All information figures are
linear-Gaussian estimates, in nats, from about 250,000 time points per arm
(Â from 20,000 intervened replicas).

## What it found

**The block test's verdicts.**

| arm | e observed | e hidden |
|---|---|---|
| A | {members, e}, at every window | {members} |
| B | {members}, at every window | {members} |
| C | {members, e}, at every window | {members} |
| C0 | {members, e}, at every window | {members} |

- *B is found, with its lag.* The members pass as a block at every window,
  W = 1 included. A one-step model sees the lag-8 transmission through the
  members' own persistence, although the true one-step coupling is zero.
  The support for the block peaks at the transmission lag: the internal
  ln BF is 10,909 at W = 7, 18,290 at W = 8, and 14,603 at W = 16.
- *A's members are rejected alone while the driver is observed.* Their
  internal cut is pruned, at −107 for W = 1, and their edge is kept, at
  39,531. Joined to the driver they pass, as one-way drive passes under
  [CLAIM-167](../claims.d/CLAIM-167.md). With the driver unobserved the members pass, with an internal
  ln BF of 10,256. The common input then shows up as coupling among the
  members.
- *C and C0 get A's verdict.* The members alone fail and the members with
  the institution pass. C's members-to-institution feedback is kept at
  W = 1 (ln BF 373) and W = 4 (85) and priced out from W = 6 (−50), so the
  direction that tells C from A survives only at short windows. A and C0
  get the same verdict on every measure computed here, and their figures
  agree to within a few per cent.

**The information profile.** Members are the six slots; E is the rest.

| | A | B | C | C0 |
|---|---|---|---|---|
| A*(1), members | 1.76 | 1.83 | 1.65 | 1.76 |
| A(1), members | 1.20 | 1.83 | 1.01 | 1.20 |
| A(8), members | 0.00 | 0.71 | 0.00 | 0.00 |
| A(64), members | 0.00 | 0.20 | 0.00 | 0.00 |
| A(64), members, e hidden | 0.00 | 0.20 | 0.02 | 0.00 |
| Â(1), members | 1.29 | 1.37 | 1.10 | 1.27 |
| Â(8), members | 0.00 | 0.18 | 0.00 | 0.00 |
| Â(64), members | 0.00 | 0.02 | 0.00 | 0.00 |
| transfer into members, history 16 | 0.15 | 0.00 | 0.11 | 0.16 |
| the same, e hidden | 0.00 | 0.00 | 0.00 | 0.00 |

- *Retention conditioned on E separates B.* B's norms survive turnover,
  with A(64) of 0.20 nats against zero elsewhere. That holds with e observed
  and, in these parameters, with it hidden. The lag profile also separates
  the aggregates the calibration matched only at lag 1: the aggregate's
  autocorrelation at lag 32 is 0.17 in A, 0.68 in B, 0.38 in C and 0.17
  in C0.
- *Â misses B's memory.* Â of B's members falls to 0.02 by Δ = 32, while
  A(32) is 0.31. An intervention on the present values leaves the norms of
  the last eight steps in place, and those carry the transmission. The
  state of a population that transmits at a lag includes its stored past.
- *Dynamical independence goes with the block test.* B's members are
  independent of the rest. A's, C's and C0's are not, while e is observed,
  and all are once it is hidden.
- *Unpriced, every information measure picks the largest candidate.* A*,
  A and Â are largest for members with e and z in every arm. z adds its own
  persistence without any coupling, as [THEORY-1163](../theory.d/THEORY-1163.md)'s monotonicity says.

**Against the known boundaries.** By construction, B's system is its
members, with timescale L = 8, and C's is its members with the institution.
A's members are no collective. C0's boundary includes an institution that
imposes it.

- The procedure recovers B and its lag, and C's membership.
- It returns A's members only together with their driver, which [CLAIM-167](../claims.d/CLAIM-167.md)
  counts as one system and [QUESTION-116](../questions.d/QUESTION-116.md)'s test counts as a population
  rightly rejected. That holds only while the driver is observed.
- It cannot tell C0 from A, which is [CLAIM-194](../claims.d/CLAIM-194.md)'s made-versus-imposed
  boundary in population form, with an even stronger result: here the
  imposed boundary's verdict is identical to a common input's.

## What it cannot show

- **Sensitivity.** These are four parameterizations of one linear model,
  calibrated on three statistics. The separation of B by A(Δ) with e hidden
  depends on the driver's timescale, which is about 20 steps here. A driver
  as persistent as B's tradition was not tried.
- **Nonlinear dynamics.** All information figures are linear-Gaussian, and
  turnover makes the process non-Gaussian, so the figures are lower bounds
  on the true information.
- **The price.** Occam per coefficient is ln n. A smaller prior variance
  would keep C's feedback at longer windows.
- **The macrostate.** The search covers boundary and timescale only. The
  macrostate leg and effective information were not attempted.

Results, scripts and tests: scratch/studies/lead-026/ (summary.txt).
[CLAIM-926](../claims.d/CLAIM-926.md) states the finding.
