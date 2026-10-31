---
status: Active
title: 'In a nonequilibrium steady state of a thermodynamically consistent Markov jump network, the entropy produced while a current is counted, times the squared relative uncertainty of that count, is at least 2k_B, independent of the counting time, so a current precise to ε costs at least 2k_BT/ε² of dissipation; the 2015 letter proves this within linear response and for single-cycle networks at any affinity, and for many-cycle networks far from equilibrium shows it numerically and states it as a conjecture'
version: 1
tags:
- thermodynamics
- natural-sciences
date: '2026-10-31'
source:
- LIT-tmpejle0
summary: >-
  Barato & Seifert (2015), LIT-tmpejle0, read in full in NOTE-tmpxh170.
  Active for the scope stated in the title: the biased walk, the
  unicyclic formula (A/N) coth(A/2N) and the bound on random four-state
  networks were checked numerically. It bounds the precision of currents,
  not of occupations, so it does not price how long a maintained state
  lasts, and the general multicyclic proof is not in this paper.
---
<!-- inactive-ok-file: THEORY-671 — Proposed; named as a principle this bound does not bear out -->

# THEORY-tmpnaoak: In a nonequilibrium steady state of a thermodynamically consistent Markov jump network, the entropy produced while a current is counted, times the squared relative uncertainty of that count, is at least 2k_B, independent of the counting time, so a current precise to ε costs at least 2k_BT/ε² of dissipation; the 2015 letter proves this within linear response and for single-cycle networks at any affinity, and for many-cycle networks far from equilibrium shows it numerically and states it as a conjecture

## Source

Barato & Seifert (2015), LIT-tmpejle0, letter eqs. (1)–(24) and
Supplemental Material §§I–IV, read in full in NOTE-tmpxh170 from arXiv
1502.05944v2.

## What was actually shown

**The quantity.** For a current X_α (a count of transitions with
antisymmetric increments dᵢⱼ) in a steady state with entropy production
rate σ, Q_α ≡ σtε²_α = 2σD_α/J_α², with J the mean rate and D the
diffusion coefficient of X_α (eqs. 6–10). Both σt and 1/ε² grow linearly
in t, so Q is time-independent.

**Three results.**

- Biased walk: Q = A coth(A/2) ≥ 2, increasing in the affinity A (eq. 4).
- Linear response, any network: Q_α = 2[1 + (positive semidefinite
  form)/(J_α)²] ≥ 2, equality when only A_α ≠ 0 (eq. 13, supplement §I).
- Unicyclic network with N states and affinity A, any distance from
  equilibrium: Q ≥ (A/N) coth(A/2N) ≥ 2, the minimum at uniform rates
  (eq. 20, supplement §III, with a uniqueness step the authors say they
  could not prove).

For multicyclic networks far from equilibrium: numerical minimisation
and random sampling on seven networks, all ≥ 2, minima reached in linear
response; "we conjecture that Q_α ≥ 2 also for general multicyclic
networks" (p. 4).

**My check.** Computing J and D from the top eigenvalue of the tilted
generator: Q matches A coth(A/2) and (A/N) coth(A/2N) at N = 3, 5 to six
digits; over 2,998 random complete four-state graphs with rates
10^{U(−3,3)}, min Q = 2.08.

**What could have failed.** A strongly driven, many-cycle network might
have bought precision cheaply through cycle interference. None of the
sampled networks did.

## What this does not say

- **Anything about occupation observables.** The time spent in a state
  has finite uncertainty even at equilibrium (p. 1). The bound does not
  say that keeping a system in a maintained state reliably costs
  dissipation. It says that a reliable *flux*, such as a production rate
  counted over time, does. How long a maintained state lasts is the
  escape-rate question (THEORY-tmpjzj2n).
- **That the general case is proved here.** Proofs for general networks
  came later and are not held.
- **That systems sit at the bound.** Q = 2 is reached only near
  equilibrium with a single affinity, where output is slow.
- **That dissipation selects anything.** The bound constrains
  fluctuations at a given state; it is not an extremum principle
  (contrast THEORY-671).
- **For irreversible models.** With one-way reactions the affinity is
  infinite and the bound is trivially met. A model like CASE-tmpwxags's
  must be made reversible before the bound bites.
