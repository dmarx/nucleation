---
number: 438
status: Open
formerly:
- QUESTION-tmp71nlk
title: 'As a coupled oscillator system''s parameters vary, when do changes in the compatibility complex of its synchronization demands coincide with bifurcations of its locked states, and which ways of their coming apart occur?'
version: 1
tags:
- mathematics
- complex-systems
date: '2026-11-07'
line:
- formal-apparatus
- distributed-agency
summary: >-
  A's, from A12 §2.2 and §10 of the exchange "Individuation, Possibility,
  and Disposition" (2026-11-06 to 07): a change in the compatibility
  complex need not coincide with a bifurcation of the attractor structure,
  and A asks for theorems saying when they agree and counterexamples where
  they do not. It is [QUESTION-125](QUESTION-125.md)'s sibling for the complex. The wording
  is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-618 — filed from the same exchange, Proposed -->

# QUESTION-438: As a coupled oscillator system's parameters vary, when do changes in the compatibility complex of its synchronization demands coincide with bifurcations of its locked states, and which ways of their coming apart occur?

## Why it is a question

A12 §2.2, of the exchange "Individuation, Possibility, and Disposition"
(https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e): "The
mathematical payoff is that a change in the compatibility complex need not
coincide with a bifurcation of the attractor structure. One can change
without the other." A12 §10 wants "theorems specifying when those structures
agree and counterexamples where they do not".

[CLAIM-618](../claims.d/CLAIM-618.md) gives the two objects: the compatibility region of each set of
demands, and the locking region inside it. This question asks how their
boundaries relate. It is the sibling of [QUESTION-125](QUESTION-125.md), which pairs a block's
gap with a bifurcation; this one pairs the complex with a bifurcation.
[THEORY-1087](../theory.d/THEORY-1087.md) answers it once, for one seven-node motif: the locked branch
loses stability at a lag below the one at which the cycle mismatch is
greatest.

## What would answer it

For a stated family of phase dynamics, a case of each way of coming apart:
the complex gains or loses a face while the attractors are unchanged, and an
attractor bifurcates while the complex is unchanged; and, if there is one, a
condition under which the two must agree. A12 §8 proposes networks of three
to six oscillators as the first test. Candidate literature, not held by the
record and unread: Manik, Timme and Witthaut 2017, "Cycle flows and
multistability in oscillatory networks" (doi:10.1063/1.4994177); Bačić,
Schaub, Kurths and Witthaut 2026, Nature Communications
(doi:10.1038/s41467-026-75565-w).

## Note of 2026-11-15: a localized structure that is feasible where it is not attracting
<!-- inactive-ok-file: CASE-269 — Proposed; the proposed study filed from the exchange of 2026-11-15, cited in its note -->

A5 §7 of the exchange "Explain String Theory" carries the question's comparison to localized structures. 𝒦(λ) is the compatibility complex of declared demands, and 𝒯(λ) its sub-complex of demand sets met by an attracting invariant set, with 𝒯(λ) ⊆ 𝒦(λ) under a declared notion of attraction.

On a translation-invariant line, a φ⁴ kink can be required to centre in a given interval. That demand is feasible, but no particular centre is asymptotically attracting, since every translate is an equilibrium. A localized pinning potential makes one centre attract without changing the kink's charge. Varying the pinning strength is a parameter path along which 𝒯 changes while 𝒦 does not. That is the field analogue of a locking region inside its compatibility region ([CLAIM-618](../claims.d/CLAIM-618.md)), and one of the ways of coming apart this question asks about. A's construction, not run ([CASE-269](../cases.d/CASE-269.md)).

## Note of 2026-11-15: the pinned kink, run
<!-- inactive-ok-file: CASE-267 — Proposed; the run this note reports -->

The pinned kink proposed in the note above has been run ([CASE-267](../cases.d/CASE-267.md), the assistant's). A kink displaced from the centre stays displaced without the pinning bump and returns with it. The centred kink is static either way, and the charge is 1 throughout. So raising the pinning strength from zero puts the demand "centre in [−0.5, 0.5]" into the attracting subcomplex while leaving the compatibility complex unchanged. One deterministic run in one dimension, with one pinning strength. It bears on the question and does not answer it.
