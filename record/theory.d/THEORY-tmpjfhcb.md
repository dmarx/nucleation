---
status: Active
title: 'In an acyclic structural equation model, marginalising a variable that no declared intervention sets is an exact transformation, provided the coarse model''s exogenous noises may be dependent; so exactness does not require the dropped variable to be causally idle, and it can drop a variable that decides how its children respond to an intervention that is declared'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Filed Active from NOTE-tmp6b7dr. The first clause is Rubenstein et
    al.'s Theorem 10, proved in their Appendix B and re-derived below. The
    second is the record's corollary, with CASE-tmpdc0tl's hidden bit as
    the example, checked below step by step, which meets the condition
    for Active under ADR-047 v2.
tags:
- causality
date: '2026-10-21'
source:
- LIT-tmptzsyg
summary: >-
  Rubenstein et al. (2017), LIT-tmptzsyg, read in NOTE-tmp6b7dr. Exact
  transformation asks only that the coarse model reproduce the push-forward
  of each declared interventional law, so a never-intervened variable can
  be substituted out and its randomness folded into noise, whatever it
  does. Applied to the hidden governance bit, the coarse-graining that
  CLAIM-tmppi0xf shows to lose the response to h is exact. It does not say
  that the coarse model keeps any one system's response.
---
<!-- inactive-ok-file: TERM-tmpf5k7x — Proposed; the governance-response profile, filed from the same exchange, named for the contrast, nothing here rests on it -->

# THEORY-tmpjfhcb: In an acyclic structural equation model, marginalising a variable that no declared intervention sets is an exact transformation, provided the coarse model's exogenous noises may be dependent; so exactness does not require the dropped variable to be causally idle, and it can drop a variable that decides how its children respond to an intervention that is declared

## Source

Rubenstein et al. (2017), LIT-tmptzsyg, read in full in NOTE-tmp6b7dr:
Theorem 10 and its proof in Appendix B. Exact transformation is their
Definition 3: a map τ on states and a surjective, order-preserving ω on the
declared interventions with τ(ℙ_X^{do(i)}) = ℙ_Y^{do(ω(i))} for every i. The
corollary and the example are the record's.

## What was actually shown

**Theorem 10, re-derived.** Let M_X be acyclic, and let X₁ be set by no
declared intervention. By acyclicity its equation is X₁ = f₁(X_pa(1), E₁)
and X₁ is not an ancestor of its own parents. Build M_Y by deleting X₁'s
equation and, in each child Xᵢ's equation, replacing X₁ by f₁(X_pa(1), E₁),
so that Xᵢ = fᵢ(f₁(X_pa(1), E₁), X_pa(i)∖{1}, Eᵢ); give each child the noise
(Eᵢ, E₁), jointly distributed as under ℙ_E. Keep the declared interventions,
with X₁ deleted from none of them because it appears in none, and take ω the
identity and τ the projection that drops X₁. Under any declared i, the
solution of M_Y is the solution of M_X with X₁ removed, since every
occurrence of X₁ has been replaced by the expression that M_X^{do(i)} would
give it (X₁ is not intervened on, so that expression is in force). So
τ(ℙ_X^{do(i)}) = ℙ_Y^{do(i)}. Iterating removes any set of such variables.
The noises of two children of X₁ now share E₁: "marginalising out a common
parent node will in general result in its children having dependent
exogenous variables". Definition 1 allows it, and the theorem fails without
it.

**The corollary.** Nothing in the proof asks what X₁ does. It may be the
variable that decides how its children respond to a declared intervention.
The hidden bit (CASE-tmpdc0tl) is an instance. Its SEM: K = E_K,
Y_t = E_t, H = E_H, Y_{t+1} = (1 − H)E_{t+1} + HK, with E_K, E_t, E_{t+1} fair
bits, independent, and declared interventions ∅, do(H = 0), do(H = 1).

- K is never intervened on, so marginalising it is exact. The coarse SEM is
  Y_{t+1} = (1 − H)E′₁ + HE′₂, with E′₁ = E_{t+1} and E′₂ = K. Under do(H = 1),
  (Y_t, Y_{t+1}) is a pair of independent fair bits at both levels; under
  do(H = 0) likewise.
- Over a held do(H = 1) at several steps, Y_{t+1} = Y_{t+2} = K: the coarse
  model reproduces it with one noise E′₂ shared across the steps, which is the
  dependent noise the theorem needs.
- Yet the coarse state Y_t determines nothing of the response to h:
  Γ(Y_t) = ρ(h = 1) bits (CLAIM-tmppi0xf), since P(Y_{t+1} | S = (k, y),
  do(H = 1)) is the point mass at k, which differs between states with the
  same Y_t.

What could have failed: exactness could have required the dropped variable
to be causally idle, as Theorem 9 requires it to be childless. Theorem 10
shows that being unintervened is enough.

## What this does not say

- **Not that marginalising an intervened variable is exact.** Declaring
  do(K = 1) breaks it: under it H stays a fair bit and
  P(Y_{t+1} = 1) = ½ · ½ + ½ · 1 = ¾, while the marginalised model gives ½
  under ∅ and fixes H or Y_{t+1} under any intervention it has. Beckers and
  Halpern's strong abstraction rejects the coarse-graining for this reason
  (NOTE-tmp1bdcu, Bearing on the record, item 4).
- **Not that the coarse model keeps the response of a given system.**
  Exactness is about push-forward laws. Governance-response sufficiency
  (TERM-tmpf5k7x) is about the response kernels of individual states, and it
  fails here.
- **Not cyclic models.** Theorem 10 assumes acyclicity; the paper points to
  Bongers et al. for the cyclic case, with further conditions.
- **Not independent-noise SEMs.** With the usual requirement of independent
  exogenous variables, the theorem is false.

## Connections

- **CLAIM-tmppi0xf and CLAIM-350.** The distributional criterion this
  theorem satisfies is not the fibre-wise factorization they state; the
  hidden bit separates them.
- **THEORY-tmpj5zq1.** The other exact transformation in the same paper,
  with the opposite lesson: there, enlarging the declared interventions
  breaks exactness; here, the declared interventions are what let the
  dropped variable be anything.
- **THEORY-820.** Under h = 0, Y_t is informationally closed; this theorem
  adds that dropping K is exact as a causal model for interventions on H.
  Neither keeps the response of a given state.
