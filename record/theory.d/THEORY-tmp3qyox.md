---
status: Active
title: 'When two firms each hire the best available candidate by a noisy ranking, and the ranking model makes an independent re-ranking worth more to the second mover than its own next choice and makes a weaker first mover better for it, then for every accuracy of the private rankings there is a more accurate shared algorithmic ranking that each firm strictly prefers to use whatever the other does, and with which both firms, and total welfare, do worse than if neither used it'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmp1expw. The result is Kleinberg and
    Raghavan's Theorem 1, with identity (3) and Theorem 3. The proof of
    Theorem 1 and identity (3) were re-derived below, and Mallows
    instances, including the paper's three-firm example, were recomputed
    by exact enumeration, which meets the condition for Active under
    ADR-047 v2. Theorems 2 and 3 are the paper's, the second read in its
    appendix, the first in statement.
tags:
- game-theory
- social-science
date: '2026-10-21'
source:
- LIT-tmpj9gl0
summary: >-
  Kleinberg and Raghavan (2021), LIT-tmpj9gl0, read in NOTE-tmp1expw. A
  Braess paradox for screening: the shared algorithm's accuracy helps
  whoever chooses first and its correlation hurts whoever chooses second,
  and at the right accuracy the second effect wins while adoption stays
  dominant. It holds for the Mallows model always and for some random
  utility models, and never for Plackett–Luce. It says nothing about
  shocks, dynamics or market responses.
---
<!-- inactive-ok-file: TERM-tmp5lqn0 — Proposed; filed from the same exchange, named as the entry this account bears on -->

# THEORY-tmp3qyox: When two firms each hire the best available candidate by a noisy ranking, and the ranking model makes an independent re-ranking worth more to the second mover than its own next choice and makes a weaker first mover better for it, then for every accuracy of the private rankings there is a more accurate shared algorithmic ranking that each firm strictly prefers to use whatever the other does, and with which both firms, and total welfare, do worse than if neither used it

## Source

Kleinberg and Raghavan (2021), *PNAS* 118(22), LIT-tmpj9gl0, read in
NOTE-tmp1expw from arXiv v2: Theorem 1 (§2.5), identity (3) (§2.4),
Theorem 2 (RUMs, Appendix C) and Theorem 3 (Mallows, Appendix E). The
re-derivation and recomputation below are the record's.

## What was actually shown

Firms hire in a random order. Let U_s be the first mover's expected utility
using s ∈ {A, H} (algorithm, human), and U_{s₁s₂} the second mover's when
the first used s₁ and it uses s₂. A firm's payoff is ½(U_{s} + U_{s′s}).
Using the algorithm is strictly dominant iff

(4) U_A + U_AA > U_H + U_AH and (5) U_A + U_HA > U_H + U_HH.

**(5) always holds for θ_A > θ_H**, by monotonicity (Definition 1): the
algorithm's top choice is better, and it stays better after removing the
first mover's independently chosen candidate.

**Identity (3).** U_AH = E[π₁1{π₁ ≠ σ₁} + π₂1{π₁ = σ₁}] and U_AA = E[σ₂].
Conditioned on either event, π₂ and σ₂ have the same law, so
U_AH(θ, θ) − U_AA(θ, θ) = E[(π₁ − π₂)1{π₁ ≠ σ₁}]. Definition 2 makes it
positive: at equal accuracy (4) fails.

**The crossing.** At θ_A = θ_H, (4) fails; as θ_A → ∞ the algorithm is
nearly exact and (4) holds. All U's are continuous in θ_A, so there is
θ*_A > θ_H with f(θ*_A) = g(θ*_A), where f = U_A + U_AA and
g = U_H + U_AH.

**Welfare.** W_AA = U_A + U_AA = f and W_HH = U_H + U_HH = h, a constant
in θ_A. Definition 3 says U_AH < U_HH for θ_A > θ_H, so g < h. At θ*_A,
W_AA = f = g < h = W_HH. By continuity there is θ′_A slightly above
θ*_A with g < f < h: (4) holds strictly, (5) holds, and W_AA < W_HH. By
symmetry each firm's utility is half the welfare, so each firm is worse
off too.

**Recomputed for Mallows** (Kendall tau, exact enumeration over
permutations, values the expected uniform order statistics):

- n = 3: at equal accuracy the second mover gains from independence
  (0.5379 against 0.5329 at φ = 1.5; 0.5604 against 0.5536 at φ = 2).
- n = 3, two firms: a strictly dominant algorithm with lower welfare at
  (φ_H, φ_A) = (1.5, 1.60), (2.0, 2.15) and (3.0, 3.30), for example
  welfare 1.1165 against 1.1207 at (2.0, 2.15).
- n = 4, three firms, φ_A = 2, φ_H = 1.75: all-algorithm 0.55111 each,
  all-human 0.55231, and the algorithm is a best response to every
  profile of the others, as §4 reports (≈ 0.551 and ≈ 0.552).

What could have failed: the second mover's loss from correlation could
have been outweighed by the first mover's gain at every accuracy where
adoption is dominant. Definition 3 is what rules that out at the
crossing.

## What this does not say

- **Not for every ranking model.** Plackett–Luce makes identity (3) zero,
  and the effect vanishes. Appendix B builds three-candidate models
  violating each condition, and with fifteen candidates Laplacian noise
  violates Definition 2 (Fig. 2).
- **Not that the loss is large.** About 4% in the one Gaussian instance
  quantified. Under Mallows, which ignores values, the authors warn the
  effect can be made arbitrarily large, which says more about the model.
- **Not about shocks or dynamics.** The point is that neither is needed.
- **Not about harm to particular candidates.** The paper names it and
  sets it aside. Its result concerns average quality.
- **Not a general k-firm theorem.** The three-firm case is one computed
  instance.
- **Not for n = 2.** With two candidates both firms hire both whatever
  they use. Appendix E's strict inequality needs n ≥ 3.

## Connections

- **TERM-tmp5lqn0.** A shared rule class for reading candidates is a
  common legibility regime. Each institution reads better, and together
  they read the same errors. This is A25's "loss of organizational
  diversity" with a welfare cost, in a model where it can be computed.
- **THEORY-tmpwl9bj** has the opposite structure: one learner whose
  model reshapes its own data. Here no data are reshaped, and the cost
  comes from correlation across decision-makers.
