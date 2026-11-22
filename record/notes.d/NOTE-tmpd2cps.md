---
status: Skimmed
paper: LIT-2259
title: 'Bosca and Ghrist — Selective Adaptation of Beliefs and Communication on Cellular Sheaves'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Skimmed on 2026-11-22 for LEAD-023 from the arXiv copy (2601.22431v2,
    18 March 2026, 34 pages): the introduction, §2, the theorem statements
    of §3–6 (Theorems 3.2, 4.1, 4.3, 5.2; Propositions 4.8, 5.4, 6.1, 6.3;
    Corollary 6.5), the conclusion and Appendix C's corollaries read; the
    proofs and Appendices A–B skipped. Quotations checked by script.
date: '2026-11-22'
summary: >-
  Hansen and Ghrist's discourse-sheaf dynamics with selective rigidity:
  agents fixed in some directions of opinion and flexible in others, and
  some expression maps fixed while others adapt. Fixed opinions turn
  equilibrium into a sheaf Poisson equation; adapting maps follow Laplacian
  flow on an auxiliary sheaf of structures and converge to the
  Frobenius-nearest consistent sheaf. With both evolving, a conserved
  quantity excludes agreement by silence or vanishing opinions, and the
  ratio of the two rates decides which one barely moves.
---

# NOTE-tmpd2cps: Bosca and Ghrist — Selective Adaptation of Beliefs and Communication on Cellular Sheaves

## Contribution

Directional stubbornness in opinions and in expressions on discourse
sheaves, with the structure (the restriction maps) treated by a sheaf of its
own, and quantitative bounds on when beliefs or expressions are the ones
that change.

## Key results (parts read)

1. **Partial stubbornness (Theorem 3.2).** Free opinions converge
   exponentially to the solution of a sheaf Poisson equation nearest the
   initial state, forced by the fixed directions.
2. **Partial learning (Theorem 4.1).** When only some incidence maps
   adapt, gradient flow on the discrepancy converges to the sheaf
   "Frobenius-nearest to F among all sheaves minimizing discrepancy"; the
   flow is "sheaf diffusion on an auxiliary structure sheaf whose global
   sections correspond to sheaf structures making a fixed opinion profile
   publicly consistent" (abstract).
3. **Joint dynamics (Theorem 5.2).** Total disagreement is nonincreasing;
   with a precompact orbit trajectories converge to equilibria. "perfect
   agreement is achievable only when the effective Laplacian has trivial
   kernel" (conclusion).
4. **No agreement by disengagement (Proposition 5.4).** The matrix
   α(L_F)ᵥᵥ − βxᵥxᵥᵀ is conserved at a free vertex whose maps all adapt;
   "the system cannot resolve discord by either silencing communication or
   eliminating opinions."
5. **Which changes (Propositions 6.1, 6.3; Corollary 6.5).** The ratio of
   expression rate β to opinion rate α bounds the displacement of the
   other variable: "If expressions adapt faster than beliefs, agents reach
   surface harmony before private convictions have had time to evolve. The
   reverse regime produces the opposite effect: flexible individuals
   conform to rigid communication norms while the underlying discourse
   structure remains unchanged."
6. **Open (conclusion).** Fixed stalks and pairwise interactions;
   "Allowing stalks to evolve would capture how agents' opinion spaces
   change as interests shift".

## Assumptions

A finite connected graph; finite-dimensional real stalks; linear restriction
maps; gradient flows of the quadratic disagreement with rates α and β;
precompactness or regularization for the joint case.

## Concepts

Discourse sheaf; sheaf Laplacian; global sections (public consistency);
stubborn and free directions; sheaf of free opinions; sheaf of free
structures; sheaf Poisson equation; conservation law; structural and opinion
stagnation; rhetorical accommodation.

## Bearing on the record

- **[THEORY-1088](../theory.d/THEORY-1088.md).** It confirms the account (learning to lie, the
  conserved blocks) and extends it: selective rigidity, the structure flow
  as diffusion on a sheaf of its own, and rate bounds. As [THEORY-1088](../theory.d/THEORY-1088.md) says,
  nothing in either flow checks an expression against the opinion it
  expresses; the stagnation bound makes that sharper: with β ≫ α
  agreement is reached with beliefs almost unchanged.
- **[QUESTION-282](../questions.d/QUESTION-282.md).** A model in which interaction changes the correspondence
  structure (the restriction maps) and not only the states, with a
  quantitative condition, the rate ratio β/α, under which the structure is
  what changes. The adaptation rule is the modeller's gradient flow, so it
  does not show structure the system generates, and it does not separate
  change of the operator from redescription.

## Limitations

Skimmed: proofs not followed. Linear model; the rates and the energy are
posited, not derived from agents; bounds are sufficient conditions, as the
authors say.
