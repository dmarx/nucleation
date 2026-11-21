---
status: Proposed
title: 'Gradient flow into a degenerate minimum relaxes algebraically, not exponentially, and how slowly is not fixed by the learning coefficient: on the balanced line of a k-fold product loss the decay is t^(−1/(2k−2)) while the real log canonical threshold stays ½ and only its multiplicity grows to k'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation: gradient flow on K = (a₁⋯a_k)² from a
  balanced start not decaying as t^(−1/(2k−2)), or the evidence integral
  of that K with a smooth positive prior not scaling as
  n^(−1/2)(log n)^(k−1). The restriction to the balanced line is part of
  the claim; that off-line trajectories relax exponentially (stated
  below) does not defeat it.
tags:
- learning-theory
- loss-landscapes
- mathematics
date: '2026-11-21'
line:
- learned-structure
- formal-apparatus
grounds:
- THEORY-087
- THEORY-1253
- CASE-152
- THEORY-740
- LIT-tmp0z602
- LIT-tmpv9upr
summary: >-
  A39 §5 and A42 §6 of the exchange "Rich Get Richer Power Laws"
  (2026-11-21): a quartic direction relaxes as t^(−1/2), "algebraically
  slow optimization even without thermodynamic criticality", and for a
  k-fold product "the degree of dynamical slowing and the RLCT are not
  interchangeable measures of singularity". Checked by the assistant,
  who adds that the algebraic decay needs a balanced approach: off the
  balanced line the flow relaxes exponentially at a rate set by the
  conserved imbalance. The wording is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A39, A42); adopting it is the
  owner's call.
---

<!-- inactive-ok-file: LIT-tmp0z602 LIT-tmpv9upr CLAIM-tmpuc8ro CLAIM-tmpv5asv — Deferred works registered from the exchange and not yet read, or claims filed with this one -->

# CLAIM-tmpcbfdj: Gradient flow into a degenerate minimum relaxes algebraically, not exponentially, and how slowly is not fixed by the learning coefficient: on the balanced line of a k-fold product loss the decay is t^(−1/(2k−2)) while the real log canonical threshold stays ½ and only its multiplicity grows to k

## The claim

**Algebraic relaxation (A39 §5).** On K(v) = v⁴, gradient flow
v̇ = −4v³ gives v(t) = v₀/√(1 + 8v₀²t), so |v| ∝ t^(−1/2). On K = v² it gives
v₀e^(−2t). "A singular loss landscape can produce algebraically slow
optimization even without thermodynamic criticality or interacting-particle
collective modes."

**Slowing and the learning coefficient part ways (A42 §6).** For
K = (a₁⋯a_k)² on the balanced line a₁ = ⋯ = a_k = x, K = x^(2k), and each
coordinate obeys ẋ = −2x^(2k−1), so x ∝ t^(−1/(2k−2)): t^(−1/2), t^(−1/4),
t^(−1/6) for k = 2, 3, 4. The same loss with a smooth positive prior has
Z_n ≍ n^(−1/2)(log n)^(k−1): λ = ½ and m = k for every k ([THEORY-087](../theory.d/THEORY-087.md)'s
normal-crossing case; [CASE-152](../cases.d/CASE-152.md) for k = 2). Adding factors slows the flow
without changing λ, only the multiplicity. "A hierarchy of slow learning
modes does not automatically imply a hierarchy of RLCT values."

**The assistant's checks** (`python3 -I`, `t5/check2.py`): the closed
forms agree with numerical integration of the flows to five digits at
t = 1, 10, 100. The fitted decay exponent for k = 3 is −0.2500. The free
energy slope of (a₁a₂a₃)² on [−1, 1]³ is 0.288, 0.356, 0.391, 0.413 at
n = 10³, 10⁵, 10⁷, 10⁹. That is λ = ½ approached as ½ − (m − 1)/log n with
m = 3 (0.210, 0.326, 0.376, 0.403), as [THEORY-1253](../theory.d/THEORY-1253.md) states for m > 1.

## A qualification: the algebraic decay needs a balanced approach

The assistant's addition. For K = a²b², gradient flow conserves
D = a² − b². Off the balanced line (D ≠ 0) the flow does not reach the
most degenerate point, the origin. It reaches a generic point of the
zero set, a = √D, b = 0, and b decays exponentially at rate 2D. The check:
from (0.3, 0.2), b's log-rate is −0.1002 against −2D = −0.1000. So a
single factored mode relaxes algebraically only when started balanced,
or so close to balanced that the run ends before t ≈ 1/D. Balanced small
starts are the regime of [THEORY-740](../theory.d/THEORY-740.md)'s stagewise linear networks, so the
case is not idle. But the t^(−1/2) of one quartic direction is not what a
generic start sees. What a population of such modes from a random start
sees is [CLAIM-tmpuc8ro](CLAIM-tmpuc8ro.md).

## What it does not say

That observed slow relaxation in a network is singular. That reading is
A's further claim, [CLAIM-tmpv5asv](CLAIM-tmpv5asv.md). Amari's and Wei's analyses of plateaus
at and near singularities ([LIT-tmp0z602](../literature.d/LIT-tmp0z602.md), [LIT-tmpv9upr](../literature.d/LIT-tmpv9upr.md)) are cited in the
exchange and not yet read, so the record does not yet hold their
distinction between the two kinds of plateau.
