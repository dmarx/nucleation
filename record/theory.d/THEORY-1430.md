---
number: 1430
status: Active
formerly:
- THEORY-tmpwe5km
title: 'Vipond shows that the persistence landscape extends to multiparameter persistence modules as a function that is stable with respect to the interleaving distance and whose weighted versions together determine the rank invariant of a finitely presented module, although no complete discrete invariant exists for such modules'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Narrowed (kind 3) and promoted at the status review's ruling (the owner
    delegated these rulings), the thirtieth status review (ADR-065).
    Proposition 36 holds for finitely presented modules only, which the
    title did not say. Old title, verbatim: "Vipond shows that the
    persistence landscape extends to multiparameter persistence modules as
    a function that is stable with respect to the interleaving distance and
    whose weighted versions together determine the rank invariant,
    although no complete discrete invariant exists for such modules". Old
    promote_when, verbatim: "A reading that includes the appendices
    confirms that the paper proves the multiparameter landscape's
    ∞-distance is bounded by the interleaving distance (Theorem 30), proves
    that the weighted landscapes of a finitely presented module determine
    its rank invariant (Proposition 36), and states, with a source, that
    multiparameter modules lack a complete discrete invariant."
    NOTE-1609 v2 read the paper with its proofs and Appendix A and is Read.
    Theorem 30's proof is complete. Proposition 36's printed proof needs
    repairs, recorded in NOTE-1609: Proposition 28's identity swaps w and
    w⁻¹, Corollary 33's interleaving needs the corrected pullback, and
    pairs equal in a coordinate need the right-continuity of finitely
    presented modules. Second check (ADR-065 point 5), by the status
    review's coordinator, 2026-11-06: (1) Definition 25 defines ‖h‖w∞ =
    ‖(wᵢhᵢ)ᵢ‖∞; (2) with h = w⁻¹ ⊙ t, x ± h = w⁻¹ ⊙ (w ⊙ x ± t), so
    λw(M)(k, x) = λ1(M ∘ ϕ_{w⁻¹})(k, w ⊙ x), and the printed identity
    fails; (3) the right-continuity step (finitely many grades, supports
    {x ≥ g}, so M_x ≅ M_{x+δ1} for small δ) closes the gap in Proposition
    36 and covers Proposition 24's converse; (4)
    scratch/formal/vipond_checks.py re-run: all checks pass and both
    controls fail as they should. Status Proposed → Active; promote_when
    removed on promotion.
tags:
- mathematics
date: '2026-11-05'
source:
- LIT-2036
summary: >-
  Vipond (2018; JMLR 2020), [LIT-2036](../literature.d/LIT-2036.md), read in [NOTE-1609](../notes.d/NOTE-1609.md),
  proofs and Appendix A included. Active: Theorem 30's proof is complete,
  and Proposition 36's holds once its slips are repaired (a w ↔ w⁻¹ swap
  in Proposition 28, and pairs equal in a coordinate), repairs a second
  checker has gone through. The landscape sees only the rank invariant; it does not say
  anything about features born at incomparable parameter values, about
  direction or paths, or about recovering a Pareto frontier of budgets.
---
# THEORY-1430: Vipond shows that the persistence landscape extends to multiparameter persistence modules as a function that is stable with respect to the interleaving distance and whose weighted versions together determine the rank invariant of a finitely presented module, although no complete discrete invariant exists for such modules

## Source

Vipond (2018; 2020), [LIT-2036](../literature.d/LIT-2036.md); read in [NOTE-1609](../notes.d/NOTE-1609.md).

## What was actually shown

- **The landscape** (Definition 19) and its line-by-line characterization
  (§1).
- **Stability** (Theorem 30; Corollary 31 for sublevel-set modules): proof
  complete, checked step by step.
- **Injectivity on rank-invariant classes** (Proposition 36, §4.2), for
  finitely presented modules. The paper's proof, repaired (NOTE-1609):
  Proposition 28's identity is λw(M)(k, x) = λ1(M ∘ ϕ_{w⁻¹})(k, w ⊙ x),
  not the printed λ1(M ∘ ϕw)(k, w⁻¹x); Corollary 33's interleaving holds
  for that pullback; and a pair a ≤ b equal in some coordinate is reduced
  to a strict one by β^{a,b} = β^{a,b+δ1}, since a finitely presented
  module has M_x ≅ M_{x+δ1} for small δ > 0. Checks:
  scratch/formal/vipond_checks.py.
- **No complete discrete invariant** (§1): stated with citations to the
  literature, not proved here.
- **Statistics** (§5, stated; proofs in Appendix B, not read): law of large
  numbers, central limit theorem, confidence intervals in a separable
  Banach space.

## What this does not say

- That the landscape is a complete invariant: it is bounded by what the
  rank invariant sees (§7).
- Anything about features born at incomparable parameter values.
- Anything about direction, paths, reachability or the cost of traversal.
- That the interleaving distance is computable in practice: it is NP-hard
  (§2).
