---
number: 947
status: Active
formerly:
- CLAIM-tmp6f8w8
title: 'Conferral rates set capture speed, not outcome'
statement: >-
  In the coupled meaning–influence model of two hypotheses and two
  specialists, with conferral a moving average toward a softmax of agreement
  with the current meaning, the symmetric state is unstable exactly when gσ²
  > 2(1 − φ(1 − ε)): the conferral memory and the meaning rate set how fast
  capture comes, not whether it comes or where it settles
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-090, from the
    executed study CASE-363.
- version: 2
  date: '2026-11-23'
  note: >-
    Promoted to Active at the status review's ruling (the owner delegated
    these rulings; ADR-057): its ground CASE-363 went Active at this
    review on a reproduced rerun; the derivation was rechecked; no
    objection; the defeated_if is not met (spread 1e-9, 1,916 of 1,916
    sets agree).
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation in CASE-363, or a rerun of its code
  (scratch/studies/lead-090/) in which the Jacobian of the mean-field map at
  symmetry differs from α = 1 − ρ(1 − φ(1 − ε)), β = ρσ, γ = (1 − δ)gσ/2, δ,
  or in which the captured fixed point moves with ρ or δ. A different reading
  of CASE-092's conferral (a multiplicative update, or scoring against the
  argmax interpretation) does not count: the claim is stated for this
  reading, and the study reports the others.
tags:
- complex-systems
- self-governance
date: '2026-11-22'
line:
- distributed-agency
grounds:
- CASE-363
bears_on:
- QUESTION-100
summary: >-
  [CASE-363](../cases.d/CASE-363.md) builds [CASE-092](../cases.d/CASE-092.md)'s model and reduces it to its mean field.
  Its linearization is [CASE-099](../cases.d/CASE-099.md)'s J with α = 1 − ρ(1 − φ′), β = ρσ,
  γ = (1 − δ)gσ/2 and δ (φ′ = φ(1 − ε)), so [CLAIM-330](CLAIM-330.md)'s condition becomes
  gσ² > 2(1 − φ′), with the meaning rate ρ and the memory δ cancelled. The
  fixed points solve the Curie–Weiss equation a = tanh(Ja + h),
  J = gσ²/(2(1 − φ′)), so they too are independent of ρ and δ. Under a
  multiplicative (replicator) conferral authority is neutral alone and any
  positive loop destabilizes; under Regime B, γ = 0. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-317 — Proposed or new; the study this claim rests on and its companion, filed in the same batch, and LEAD-081's build, filed today -->

# CLAIM-947: Conferral rates set capture speed, not outcome

## The claim

[CLAIM-330](CLAIM-330.md) holds the threshold for [CASE-099](../cases.d/CASE-099.md)'s abstract J. [QUESTION-100](../questions.d/QUESTION-100.md) leaves open "whether [CASE-092](../cases.d/CASE-092.md)'s full model has that linearization". Built as [CASE-363](../cases.d/CASE-363.md) reads it, it does, with all four entries nonnegative and α, δ < 1 whenever φ′ < 1 and δ < 1, and the entries are

- α = 1 − ρ(1 − φ′), the persistence of meaning, raised by queries framed by the dominant interpretation;
- β = ρσ, authority's pull on meaning through the specialists' retrievals;
- γ = (1 − δ)gσ/2, meaning's pull on conferral, through scoring by agreement;
- δ, the conferral memory.

Then βγ > (1 − α)(1 − δ) reduces to gσ² > 2(1 − φ′). Both the meaning rate and the memory cancel, because each scales both sides. They set λ+ and so the time to capture, and nothing else: the fixed points solve a = tanh(Ja + h) with J = gσ²/(2(1 − φ′)) and h = gσb/(2(1 − φ′)), the mean-field Ising equation, in which neither appears. On 1,916 random parameter sets the nonlinear map left symmetry exactly when the condition held.

So in this model what decides capture is the gain of conferral on agreement (g), the specialists' difference (σ, entering twice, once in each arrow) and self-confirming framing (φ′); the conferral timescale, one of [CASE-092](../cases.d/CASE-092.md)'s controls, does not. [LEAD-081](../leads.d/LEAD-081.md)'s build found the same cancellation and fitted it roughly ([CASE-317](../cases.d/CASE-317.md)); here it is exact.

## What it does not say

- That it holds for other conferral rules. Under a multiplicative update authority is neutral alone (δ_eff = 1), so any positive loop destabilizes; under the argmax score there is no linearization. Both are in [CASE-363](../cases.d/CASE-363.md).
- That memory is idle. It sets the speed of capture and, with noise, how long a run stays near symmetry.
- That the model is new. [CLAIM-948](CLAIM-948.md) places it among known models.
