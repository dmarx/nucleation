---
status: Proposed
title: 'A power simulation of a Contextuality-by-Default test on a four-context cyclic system with free binary answers: the plug-in signalling estimate keeps detection valid but costs most power when true signalling is small, a violation the size of Lo et al.''s then needs over 2,500 respondents a context, and no absence verdict that leans on estimated signalling is valid'
version: 1
standing: documented
kind: executed-study
tags:
- contextuality
- mathematical-statistics
- pragmatics
date: '2026-11-22'
line: pragmatic-transport
draws_on:
- THEORY-tmpdcw35
- THEORY-177
summary: >-
  Run in session for LEAD-182 on 2026-11-22 (scratch/studies/lead-182,
  power.py and absence.py; seeds fixed; 184 cells of 800 replications with
  799 bootstrap resamples, and 144 cells of 4,000 for the absence bound).
  Between-subjects respondents give two free binary answers in one of four
  contexts; true models are Lo et al.'s Table 1 and a symmetric family
  with Δ_C from −0.3 to 0.3 and signalling from 0 to 0.6. The plug-in
  test is valid, but at Δ_C = 0.19 and no true signalling its power is
  0.24 at 2,500 respondents a context and 0.65 at 4,000; with signalling
  of 0.3, 0.80 at 1,600. Absence by the plug-in bound is invalid (84% on
  the boundary); a Bonferroni bound is valid and can show absence only
  where signalling is small. Nothing here is a finding about judgements.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpdcw35 CLAIM-tmpalxab CASE-tmpl2va4 — new; the reading, the finding and the design this run belongs to -->

# CASE-tmpjp6vg: A power simulation of a Contextuality-by-Default test on a four-context cyclic system with free binary answers: the plug-in signalling estimate keeps detection valid but costs most power when true signalling is small, a violation the size of Lo et al.'s then needs over 2,500 respondents a context, and no absence verdict that leans on estimated signalling is valid

## What was run

For LEAD-182, the power analysis of the design in CASE-tmpl2va4, by
simulation, on 2026-11-22. No human data. Code, results and tables are in
scratch/studies/lead-182 (cbd.py, power.py, absence.py, results.jsonl,
absence.jsonl, summary.md); test_cbd.py's 15 tests pass, among them the
reproduction of Lo, Sadrzadeh and Mansfield's violation and spread
(THEORY-tmpdcw35).

**The simulated study.** An item is a rank-4 cyclic system: contents q0
to q3, context k measuring q_k and q_(k+1). Each respondent sees one
context and gives two free binary answers. n is the number of
respondents a context after exclusions, so an item takes 4n.

**The statistic.** Δ_C = σ·E − 2 − Δ, with the odd sign pattern σ fixed in
advance, E_k the mean product of the two answers in context k, and Δ the
plug-in signalling, the summed absolute differences of each content's two
marginal means (THEORY-177). Alternatives run beside it: σ maximised over
the eight odd patterns in each resample; each content's difference
soft-thresholded by one standard error; a delta-method bound.

**Tests.** Detection: the 5% percentile-bootstrap lower bound above 0
(resampling respondents within contexts), and at 0.05/8 for an
eight-item family. Absence: the 95% upper bound below 0, by the bootstrap
and by a Bonferroni bound built to be valid whatever the signalling
(cbd.absence_upper_bound).

**True models.** Lo et al.'s Table 1, with its correlations kept and
marginal shifts added; and a symmetric family with every |E_k| equal,
signalling spread equally over the four contents, true Δ_C of −0.3,
−0.15, 0, 0.1, 0.19 and 0.3, signalling 0, 0.1, 0.3 and 0.6, at n from 100
to 4,000. A base marginal of 0.15 is a robustness check; it changes
nothing material.

## What it found

**1. The plug-in estimate of signalling is biased upward when true
signalling is small, and the bias shrinks only as fast as the standard
error.** With no true signalling the mean of Δ̂ is 0.226 at n = 400 and
0.112 at 1,600, as the folded-normal formula 4·√(2/π)·√(2/n) predicts.
So Δ_C is underestimated by the same amount: a true 0.19 is estimated at
−0.04 at n = 400. At signalling 0.3 or more the bias is gone by n = 1,000.

**2. Detection by the plug-in statistic is valid and, where signalling is
small, expensive.** Its false-detection rate on the boundary (true Δ_C =
0) is at most 0.068 (signalling 0.6, n = 1,000; Monte Carlo standard error
about 0.009) and near 0 at low signalling. Power at the 0.05 level:

| true Δ_C | true signalling | n = 1,000 | 1,600 | 2,500 | 4,000 |
|---|---|---|---|---|---|
| 0.196 (Lo et al.'s table) | 0 | 0.01 | 0.06 | 0.26 | 0.75 |
| 0.19 | 0 | 0.01 | 0.05 | 0.24 | 0.65 |
| 0.19 | 0.1 | 0.13 | 0.44 | 0.83 | 0.97 |
| 0.19 | 0.3 | 0.59 | 0.80 | 0.92 | 1.00 |
| 0.19 | 0.6 | 0.68 | 0.83 | 0.93 | 0.99 |
| 0.30 | 0 | 0.24 | 0.68 | 0.96 | 1.00 |
| 0.10 | 0.3 | 0.17 | 0.35 | 0.49 | 0.66 |

At 0.05/8, for a family of eight items, a 0.19 violation with signalling
0.3 is found with power 0.76 at 2,500 and 0.95 at 4,000. Maximising the
sign pattern changes nothing beyond Monte Carlo error here, because one
pattern dominates. The delta-method bound gains some power at low
signalling (0.44 against 0.24 at Δ_C = 0.19, n = 2,500) at the same size.

**3. The soft-thresholded statistic is not valid.** It buys power by
underestimating signalling, and on the boundary it detects falsely 22% of
the time at signalling 0.3 and n = 400, and up to 62% at signalling 0.6.

**4. No absence verdict that leans on estimated signalling is valid.** The
plug-in upper bound declares a boundary system noncontextual 84% of the
time when true signalling is 0, and declares a contextual system (Δ_C =
0.19) noncontextual 48% of the time at n = 100 and 17% at n = 400. The
soft-thresholded bound still errs 21% of the time on the boundary. The
Bonferroni bound, which credits only the signalling a lower confidence
bound guarantees, errs at most 3% on the boundary and under 1% for
contextual systems. Its power to show absence is high only where
signalling is small: 0.92 at n = 1,600 for Δ_C = −0.15 without
signalling, 0.21 with signalling 0.1, and near 0 with 0.3. Where the
data signal heavily, robust absence can be shown only for systems well
inside the noncontextual region (Δ_C = −0.3 with signalling 0.3: 0.77 at
4,000).

## What it can show

That the test LEAD-182 asks for is feasible but large. CASE-053's rough
figure, about 650 valid responses a context to see a 0.19 violation at
three standard deviations, assumed the signalling away, as Lo et al.'s
format does. With free answers, Δ must be estimated, and when the true
system is near-symmetric the estimate's bias, not its spread, sets the
cost: over 4,000 respondents a context for power 0.75 at Lo et al.'s
effect. When the data do signal, as LIT-842 finds language data do as a
rule, 1,600 a context give power 0.80. So the pilot's estimate of the
signalling is the main input to the sample size (CASE-tmpl2va4).

It also shows that the two verdicts need different estimators. Detection
can use the plug-in signalling, whose bias is in the safe direction.
Absence cannot, and needs the conservative bound, which can only certify
absence where signalling is small. This is the asymmetry CLAIM-tmpalxab
states.

## What it cannot show

- Anything about human judgements. The true models are stipulated; only
  Lo et al.'s table comes from data, and from a format that forced
  symmetry.
- Behaviour outside the simulated family: unequal correlations other than
  Lo et al.'s, signalling concentrated on one content, respondents
  answering several items (dependence across items), or exclusions that
  depend on the context.
- The best valid test. A likelihood-ratio test against the noncontextual
  set, or a bias-corrected signalling estimate with a guaranteed bound,
  might do better than the plug-in; neither was built here.
