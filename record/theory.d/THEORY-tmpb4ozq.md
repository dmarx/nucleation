---
status: Proposed
promote_when: >-
  A step-by-step re-derivation, recorded under ADR-047 v2, of the upper
  bound of Lattimore and Szepesvári's Theorem 3 (their Lemmas 7 and 8 and
  the decreasing-rate exponential-weights argument of Appendix C), or a
  reading of a later source that restates the bound with its proof. The
  lower bound in F is already re-derived below and does not settle it, nor
  does a citation of the bound by others.
title: 'For a finite partial-monitoring game in which every two actions whose cells meet can estimate their loss difference from their own two signals, RelExp3''s expected regret satisfies lim sup E[R_n]/√n ≤ 8√(2K_loc(1+F)(2+F) log K), with K_loc the most actions whose cells share a point and F the number of feedback symbols, and no other game-dependent constant; a two-action game shows that a factor linear in F cannot be avoided in general'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Proposed from NOTE-tmpkgxba, as Lattimore and Szepesvári's
    Theorem 3 and Theorem 5 state them. The lower bound (Theorem 5) is
    re-derived below, and its game checked numerically to be point-locally
    observable. The upper bound's proof (Appendix C) was read at the level
    of its main steps and not checked line by line. Hence Proposed.
tags:
- learning-theory
- game-theory
date: '2026-10-25'
source:
- LIT-tmpfjv79
summary: >-
  Lattimore and Szepesvári (2019), [LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md), read in [NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md). For
  the class of games Bartók (2013) studied, the leading constant of the √n
  regret depends only on K_loc, F and log K, asymptotically. It is the
  first such result against adversaries. The constant reached before the
  asymptotics set in still depends on large game constants. It is a bound
  for one algorithm in a sub-class of the easy games, not a
  characterisation of the constant.
---
# THEORY-tmpb4ozq: For a finite partial-monitoring game in which every two actions whose cells meet can estimate their loss difference from their own two signals, RelExp3's expected regret satisfies lim sup E[R_n]/√n ≤ 8√(2K_loc(1+F)(2+F) log K), with K_loc the most actions whose cells share a point and F the number of feedback symbols, and no other game-dependent constant; a two-action game shows that a factor linear in F cannot be avoided in general

## Source

Lattimore and Szepesvári (2019), [LIT-tmpfjv79](../literature.d/LIT-tmpfjv79.md), §4, Theorem 3, Appendix C
(upper bound), Appendix E, Theorem 5 (lower bound) and Appendix G, Lemma 9
(V_loc ≤ 1 + F), in the arXiv numbering. They are Theorems 8 and 14 in the
ALT text. Read in [NOTE-tmpkgxba](../notes.d/NOTE-tmpkgxba.md).

## What was actually shown

**Setting.** Weak neighbours are actions whose cells meet. A game is
point-locally observable if every pair of weak neighbours is pairwise
observable: ℓ_a − ℓ_b ∈ Im S_aᵀ + Im S_bᵀ. Dominated and degenerate actions
are removed first, which can only raise the minimax regret. K_loc is the
size of the largest set of actions whose cells share a point.

**RelExp3** runs exponential weights on cumulative estimates of each
action's loss relative to an anchor B_t, the action of largest weight. It
uses decreasing rates η_t, forced exploration α_t = min(1/(4K), t^{−1/2−ε}),
and extra exploration γ_t on the actions needed to estimate the
differences of the plausible actions M_t. The proof's idea, read and not
checked line by line: after polylog(n) rounds, the actions with
non-negligible weight lie in one point-local game around the empirical
optimum (their Lemmas 7 and 8). There the estimators use only the two
actions involved, with ‖v‖_∞ ≤ V_loc ≤ 1 + F (Lemma 9). The variance
term becomes 2V_loc²K_loc Σ_t η_t.

**The lower bound, re-derived.** Take K = 2, E = 2F − 2,
L = ((1, 0, 1, 0, …), (0, 1, 0, 1, …)), and Φ as in Appendix E. Computed for
F = 3, 4 and 6: the pair is pairwise observable, but neither action's
signals alone suffice. Take u₁ = p + Δ, u_E = p − Δ, u_i = 2Δ for odd middle
i and 0 for even, and u′_i = u_i + 2(−1)^iΔ. Then
⟨ℓ₁ − ℓ₂, u⟩ = 2Δ(F − 1) = −⟨ℓ₁ − ℓ₂, u′⟩. Action 2's symbols pool the outcome
pairs (2j − 1, 2j), whose masses agree under u and u′, so action 2 cannot
tell them apart. Action 1's differ only on outcomes 1 and E, with KL at
most 17Δ². With Δ = (17n)^{−1/2}, R(u) + R(u′) ≥ n(F − 1)Δ/2 · e^{−1}, so
max ≥ (F − 1)√n/(4e√17) ≈ (F − 1)√n/44.8. That is the paper's
(F − 1)√n/45. Checked numerically at n = 10⁶.

The arXiv text defines p = ½ − (E − 2)Δ/4. For u to sum to 1 it must be
½ − (E − 2)Δ/2. This is a typo and does not affect the bound.

## What this does not say

- **Not that the constant is the minimax one.** It is an upper bound for
  one algorithm, and the lower bound shows only that linear dependence on
  F is needed in some game.
- **Not for all easy games.** Point-local observability is stronger than
  local observability. The paper's Exhibit 3 is locally but not
  point-locally observable.
- **Not a finite-horizon statement.** The constant hidden by the
  asymptotics "does depend on arbitrarily large game-dependent constants".

## Connections

- **[THEORY-tmpyulw1](THEORY-tmpyulw1.md)** gives the class. This entry is about the constant in
  part of the easy class.
- **[QUESTION-271](../questions.d/QUESTION-271.md).** In the lower-bound game, the loss gap between the two
  environments grows with F, while what the signals reveal about them
  does not. Feedback can be informative enough to place a game in the
  easy class and still cost a factor of F within it.
