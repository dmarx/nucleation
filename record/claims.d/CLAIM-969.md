---
number: 969
status: Proposed
formerly:
- CLAIM-tmp7stqi
title: 'In a stochastic assembly process modelled as a Markov chain, the committor of an intermediate measures its future and need not rise with how much of the target it already shows, so scoring intermediates by committor can rank a small nucleus above a more assembled trap and exhibit two separately productive nuclei combining into a trap, separations a count of formed bonds cannot register'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-116, from the
    executed study CASE-374.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the construction or the committor solve: a continuous-time
  Markov chain of the stated kind in which the reported committors are wrong,
  or in which the fully assembled misfolded state does not have a lower
  committor than the one-bond nucleus, or in which the two-seam state does not
  have a lower committor than either single seam while each single seam exceeds
  the empty state. Not defeated by assembly models in which the committor
  happens to be monotone in assembled extent, nor by the observation that a
  high committor does not by itself establish causal productivity, both of
  which the claim grants.
tags:
- complex-systems
- mathematics
- probabilistic-modeling
- natural-sciences
date: '2026-11-22'
line:
- realizability
- formal-apparatus
grounds:
- CASE-374
corroborates:
- CLAIM-567
- CLAIM-599
uses:
- TERM-117
bears_on:
- QUESTION-400
---
<!-- inactive-ok-file: CASE-374 — new; the executed study this claim is grounded in, filed with it -->

# CLAIM-969: In a stochastic assembly process modelled as a Markov chain, the committor of an intermediate measures its future and need not rise with how much of the target it already shows, so scoring intermediates by committor can rank a small nucleus above a more assembled trap and exhibit two separately productive nuclei combining into a trap, separations a count of formed bonds cannot register

## The claim

Take a stochastic assembly process as a continuous-time Markov chain whose
state is the partial structure assembled so far, with an absorbing target F
and an absorbing failure set K. The committor q(s) = Pr_s(tau_F < tau_K) scores
each intermediate s by the chance it completes before it fails. Two things
hold, demonstrated in [CASE-374](../cases.d/CASE-374.md)'s model and provable to be possible in
general:

1. **The committor measures the future, not the extent.** q need not increase
   with how much of the target the intermediate already shows. In the model a
   one-bond nucleus has q = 0.81 while the fully assembled but misfolded
   four-bond state has q = 0.05. A count of formed bonds, or any progress
   measure that rises with assembled extent, cannot register this: it ranks the
   four-bond state above the one-bond one, and the committor ranks them the
   other way.

2. **Productivity does not combine.** Establishing seam a alone, or seam b
   alone, each raises the committor from the empty state (0.19 to 0.81); the
   state with both raises it to 0.04, below the empty state. Two separately
   productive nuclei combine into a trap. This is [CLAIM-599](CLAIM-599.md)'s non-monotone V,
   here arising from assembly dynamics rather than a stipulated table.

The committor is therefore the measure [CASE-220](../cases.d/CASE-220.md) and [TERM-117](../terms.d/TERM-117.md) call for:
read as a difference under an intervention, Delta_q_N = q(do N) - q(comparator),
it gives a productive nucleus a positive sign and a trap a negative one, and it
separates a nucleus from an advanced structure that a progress count would rate
higher.

## What is demonstrated and what is granted

The demonstration is the exact committor computation on the explicit chain of
[CASE-374](../cases.d/CASE-374.md) (checked against a closed form, a Monte Carlo estimate and the
harmonic equation). It suffices to show both separations are possible in an
assembly model, which is what the claim asserts. It is not claimed that every
assembly process is non-monotone, only that the monotonicity a progress count
assumes can fail, and does in a model built from mechanisms the DNA origami
readings describe (an incompatible-seam trap after Dunn et al., an unnucleated
collapse after DeLuca et al. and Sobczak).

## What it adds and what it does not say

- **To [CLAIM-567](CLAIM-567.md):** the committor is the quantitative form of "reachable is
  not reliably reached" over intermediate states, and its disagreement with a
  progress count is the separation made measurable.
- **To [CLAIM-599](CLAIM-599.md):** an assembly-dynamics instance of the non-monotonicity the
  claim proved from a stipulated table.
- **To [QUESTION-400](../questions.d/QUESTION-400.md):** the same chain shows a fixed stock's allocation
  selecting the realised form ([CASE-374](../cases.d/CASE-374.md)), which the committor to one
  form before the other tracks.
- **It does not say** that a high committor establishes causal productivity:
  [TERM-117](../terms.d/TERM-117.md) warns it does not, and the interventional Delta_q_N, not the
  committor of an observed intermediate, is what carries the causal claim.
- **It does not say** anything about real DNA origami or about organizations.
  The model is stipulated with invented rates.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
