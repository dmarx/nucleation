---
status: Proposed
title: 'Indexed by a system''s control parameters, the compatibility complex of its synchronization demands gives each set of demands a region where they can be met together; an Arnold tongue is a locking region, where a demand is met by an attracting state, and each locking region lies inside the compatibility region of the same demands without needing to equal it'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A parameter value at which an attracting state meets a set of demands
  that no admissible configuration meets, under the same admissible state
  space; or a proof that for the stated phase dynamics every jointly
  feasible demand set is met by an attracting state wherever it is
  feasible, so that the regions always coincide. Also defeated as a
  contribution if it says nothing beyond CLAIM-567's split between a
  feasible and a reliably reached configuration, that is, if indexing by
  control parameters adds no region, boundary or comparison that
  CLAIM-567 lacks.
tags:
- mathematics
- complex-systems
- network-science
date: '2026-11-07'
line:
- distributed-agency
- formal-apparatus
rests_on:
- CLAIM-347
complements:
- CLAIM-567
- CLAIM-555
- CLAIM-153
grounds:
- THEORY-1082
- THEORY-1087
bears_on:
- QUESTION-tmp71nlk
summary: >-
  From the exchange "Individuation, Possibility, and Disposition"
  (2026-11-06 to 07). The conjecture is the owner's U4: the compatibility
  complex as a generalization of an Arnold tongue. The construction is
  A's, in A9 §1 and A12 §2.1–2.2: a parameter-indexed complex, a
  compatibility region and a locking region for each set of demands, with
  the locking region inside the compatibility region and not always equal
  to it. The strictness witness and the degenerate case of the ordinary
  tongue are the reader's. The conjecture is the owner's; the wording of
  the construction is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-555 — Proposed; cited as the parameter-space nerve this claim is set beside -->

# CLAIM-tmpk1015: Indexed by a system's control parameters, the compatibility complex of its synchronization demands gives each set of demands a region where they can be met together; an Arnold tongue is a locking region, where a demand is met by an attracting state, and each locking region lies inside the compatibility region of the same demands without needing to equal it

## The claim

**The owner's conjecture.** U4: "the compatibility complex seems likely to be
a generalization of an Arnold Tongue". A9 §1 replies: "Your Arnold-tongue
intuition is productive, but I would formulate it a little differently." The
ordinary Arnold tongue "is a **dynamical locking region**, whereas the
compatibility complex is a **feasibility structure**", and "The tongue is
not simply one face of the complex".

**The construction (A12 §2.1–2.2).** Phases live on S¹. Each demand d_e on an
edge e = (i, j) has a preferred offset a_e and a tolerance δ_e, and its
acceptance set is A_e = {θ : d_S¹(θ_j − θ_i, a_e) ≤ δ_e}. For a parameter
vector λ with admissible configurations Q(λ):

- K(λ) = {S : Q(λ) ∩ ⋂_{e∈S} A_e ≠ ∅}, [CLAIM-347](CLAIM-347.md)'s complex at each λ;
- the compatibility region of S is C_S = {λ : S ∈ K(λ)};
- the locking region T_S is the set of λ at which the dynamics admit an
  attracting phase-locked trajectory meeting every demand in S.

For the same admissible state space and fixed dynamics, T_S ⊆ C_S, since an
attracting state meeting S is a configuration meeting S. A12: "But
inclusion need not be equality." And: "An ordinary Arnold tongue is a
special case of the second kind."

**Strictness (the reader's witness).** Two attractively coupled phase
oscillators with the demand "antiphase": the demand is feasible, and the
configuration meeting it is an unstable equilibrium. [THEORY-1087](../theory.d/THEORY-1087.md) is a held
instance of the two coming apart in a seven-node motif: the locked branch
loses stability before the cycle mismatch is greatest.

**Two observations of the reader's.** For fixed dynamics and fixed λ, an
attracting state that meets S meets every subset of S, so {S : λ ∈ T_S} is
downward closed: a locking subcomplex of K(λ). And for the ordinary 1:1
tongue, with the single demand of locking to the drive, every feasible
point of the Adler model φ̇ = Δω − K sin φ has a stable branch, so there
C_S = T_S. The tongue is the degenerate case in which feasibility and
locking coincide. The gap opens with several demands, or with demands met
only on an unstable branch. In that sense the owner's "generalization"
holds.

**Where it sits.** This is [CLAIM-567](CLAIM-567.md)'s feasible/reliably-reached split
carried over a space of control parameters. [CLAIM-555](CLAIM-555.md) indexes the complex by
the parameters being trained, which is a different space. The circle-valued
obstruction is [CLAIM-153](CLAIM-153.md)'s, and its spectral form is [THEORY-1082](../theory.d/THEORY-1082.md). [CLAIM-538](CLAIM-538.md)
gives tolerances only for real offsets; A12 §2.4 is right that its convex
test "cannot simply be transferred unchanged" to the circle.

## What it does not say

- That locking regions are the only realization geometry. Reachability and
  basin size are further conditions, [CLAIM-567](CLAIM-567.md)'s.
- When changes in the complex coincide with bifurcations of the locked
  states. That is [QUESTION-tmp71nlk](../questions.d/QUESTION-tmp71nlk.md).
