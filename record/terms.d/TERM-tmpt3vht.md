---
status: Proposed
title: 'relevant, irrelevant and marginal, said of a perturbation at a fixed point of a renormalization-group map'
version: 1
tags:
- natural-sciences
- mathematics
- complex-systems
date: '2026-11-21'
line:
- formal-apparatus
complements:
- TERM-tmpyi882
draws_on:
- THEORY-777
summary: >-
  The classification the record already uses without stating it
  ([THEORY-777](../theory.d/THEORY-777.md), [THEORY-789](../theory.d/THEORY-789.md), [QUESTION-205](../questions.d/QUESTION-205.md), [QUESTION-232](../questions.d/QUESTION-232.md), [SYNTHESIS-084](../syntheses.d/SYNTHESIS-084.md) speak
  of "relevant variables" or "relevant directions"): linearize a
  renormalization-group map at a fixed point, and a perturbation is
  relevant, irrelevant or marginal as its eigenvalue grows, shrinks or
  stays one under repeated coarse-graining. Exponents are read off the
  eigenvalues, and a universality class is a fixed point's basin. Stated
  from A's exposition in A6 §4, A10 §5 and A12 §1–5 of the exchange "Rich
  Get Richer Power Laws", with A12 §3's block-variance example and A12 §4's
  ν = 1/y_t checked, and the conditions A leaves out added. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-777 THEORY-789 SYNTHESIS-084 — Proposed; the record's existing uses of "relevant" that this term states -->
<!-- inactive-ok-file: TERM-tmpyi882 CLAIM-tmpyy261 ARG-tmp92gzv — filed with this term on 2026-11-21 -->

# TERM-tmpt3vht: relevant, irrelevant and marginal, said of a perturbation at a fixed point of a renormalization-group map

## Definition

A **renormalization-group (RG) map** R_b takes a description of a system
(a Hamiltonian, a probability law, a map of an interval) to a description
of the same system observed at a scale b times coarser: coarse-grain,
rescale lengths back to the original unit, and read off the new effective
rules (A12 §1). Iterating it traces a flow. A **fixed point** S* has
R_b(S*) = S*; it is scale-invariant in the sense of [TERM-tmpyi882](TERM-tmpyi882.md)'s
sense 2.

Linearize at S*: a small perturbation along an eigendirection of the
linearized map is multiplied by b^y at each step. It is

- **relevant** if y > 0: it grows, and any nonzero amount eventually
  carries the flow away from S*. A relevant direction is a parameter that
  must be tuned to reach the fixed point. The 2D Ising critical point has
  two, temperature and field, and [THEORY-777](../theory.d/THEORY-777.md) found them as the two stiff
  directions of the coarse-grained Fisher information;
- **irrelevant** if y < 0: it shrinks, so systems that differ only along
  it flow to the same S* and share its exponents. A **universality class**
  is the set of systems whose flow reaches one fixed point once the
  relevant parameters are tuned (A10 §5, A12 §5);
- **marginal** if y = 0: the linear map does not decide it. Higher orders
  give logarithmic corrections, or a line of fixed points with exponents
  that vary along it, as in the 2D XY model's low-temperature phase
  (A12 §7, A27 §5).

## Exponents from eigenvalues

If the reduced temperature t is the only relevant thermal direction,
t' = b^(y_t) t, and the correlation length in rescaled units falls by b,
then |b^(y_t) t|^(−ν) = |t|^(−ν)/b, so ν = 1/y_t (A12 §4). Checked
symbolically. The step assumes one relevant thermal direction, the field
set to its symmetric value, and the linearized flow; the leading
irrelevant eigenvalue sets the corrections to scaling, which A12 does not
mention.

## Examples

- **The central limit theorem.** Summing pairs and rescaling by √2 is an
  RG map on probability laws, and the Gaussian is a fixed point (A12 §2).
  A finite variance puts a law in its basin. A law with a tail P(X > x) ∝ x^(−α),
  α < 2, lies outside that basin and flows instead to an α-stable fixed
  point. So whether a marginal is heavy-tailed in
  [TERM-tmpyi882](TERM-tmpyi882.md)'s sense 1 decides which fixed point summation reaches; A12
  does not say this.
- **Block averages at a critical point.** With C(r) ∝ r^(−a),
  Var(block mean) over an L × L block is L^(−4) Σ C(r_ij) ∝ L^(−a), so the
  standard deviation goes as L^(−a/2): L^(−1/8) for the 2D Ising value
  a = 1/4, against L^(−1) for independent spins (A12 §3). Checked by
  summing C(r) = r^(−1/4) over all pairs in blocks of side 8 to 512: the
  log-log slope of the variance is −0.249, and the standard deviation
  falls by 1.677 over a 64-fold change of L, against 64^(1/8) = 1.682
  (`python3 -I`). This is the finite-block integral A12 asserts without
  showing; it needs a < d.
- **Period doubling.** The doubling operator acts on unimodal maps of an
  interval, not on spatial blocks. Its fixed point has one relevant
  direction, with eigenvalue Feigenbaum's δ ≈ 4.6692 ([ARG-tmp92gzv](../arguments.d/ARG-tmp92gzv.md),
  [CLAIM-tmpyy261](../claims.d/CLAIM-tmpyy261.md)).
- **Universality across substances.** Liquid–gas critical points and
  uniaxial magnets share the 3D Ising class (A12 §5): their microscopic
  differences are irrelevant directions of one fixed point.

## What it is not

- **Not relevance to a target.** [CLAIM-152](../claims.d/CLAIM-152.md) and [CLAIM-348](../claims.d/CLAIM-348.md) make the
  adequacy of a coarse-graining relative to a declared target. RG
  relevance is relative to the fixed point and to the RG map, which is a
  choice. Whether a predictive criterion picks out the RG-relevant
  variables in general is open ([QUESTION-232](../questions.d/QUESTION-232.md), [THEORY-789](../theory.d/THEORY-789.md), [SYNTHESIS-084](../syntheses.d/SYNTHESIS-084.md));
  A13 §4 states the correspondence more strongly than the record does.
- **Not "important".** A12 §4's gloss, "Large-scale reality is determined
  by the properties that remain important under repeated changes of
  scale", holds for long-distance behaviour near a fixed point. An
  irrelevant parameter can still set non-universal amplitudes, the
  critical temperature itself, and every short-distance property.
- **Not a property of a system alone.** Whether a direction is relevant
  is fixed by the fixed point it is measured at; one perturbation can be
  relevant at one fixed point and irrelevant at another
  ([QUESTION-tmp3lkep](../questions.d/QUESTION-tmp3lkep.md)).
