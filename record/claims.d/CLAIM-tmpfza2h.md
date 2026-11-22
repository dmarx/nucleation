---
status: Proposed
title: 'Graded predicates on a measure space, identified almost everywhere and ordered pointwise, form a distributive lattice under minimum and maximum whose L¹ distance is the metric of the valuation p ↦ ∫p dμ, while the concept lattice of a thresholded incidence can be any complete lattice and need not be distributive, so the two lattices a theory of overlapping perspectives might use are different objects'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from A29 §4 of the exchange "Explain
    First Contact RL" (ChatGPT, shared 2026-11-22), with the assistant's
    fill that the metric is a valuation metric; checked with python3 -I.
role: thesis
warrant: demonstrated
defeated_if: >-
  A failure of distributivity of pointwise min and max on [0, 1]-valued
  functions; a failure of v(p ∨ q) − v(p ∧ q) = ∫|p − q| dμ for
  v(p) = ∫p dμ; or a proof that every concept lattice is distributive.
  That some recovered concept lattice happens to be distributive does not
  defeat it.
tags:
- mathematics
- logic
- representation-learning
date: '2026-11-22'
line:
- formal-apparatus
- learned-structure
rests_on:
- CLAIM-tmprq9q5
summary: >-
  A29 §4 of the exchange "Explain First Contact RL" (2026-11-22). Keep
  graded predicates instead of thresholding them: P_μ = L¹(X, μ; [0, 1]),
  with p ∧ q = min(p, q), p ∨ q = max(p, q) and d_μ(p, q) = ∫|p − q| dμ,
  "a metric lattice of graded predicates" that keeps overlap and does not
  force a partition. A29: it is distributive, and formal concept lattices
  "need not be distributive". The assistant's fill: "metric lattice" is
  exact in Birkhoff's sense, since v(p) = ∫p dμ is a strictly positive
  valuation and d_μ = v(p ∨ q) − v(p ∧ q); and every complete lattice,
  the non-distributive M₃ among them, is the concept lattice of some
  incidence. Xiong's soft meet and join (min and max of profiles, NOTE-240) are this
  lattice's operations, unremarked by A29. The wording is A's (ChatGPT, in the exchange of 2026-11-22),
  except the fill, which is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmprq9q5 LIT-267 — Proposed; the graded perspectives this lattice orders, filed with it on 2026-11-22, and the paper whose lattice it is compared with -->

# CLAIM-tmpfza2h: Graded predicates on a measure space, identified almost everywhere and ordered pointwise, form a distributive lattice under minimum and maximum whose L¹ distance is the metric of the valuation p ↦ ∫p dμ, while the concept lattice of a thresholded incidence can be any complete lattice and need not be distributive, so the two lattices a theory of overlapping perspectives might use are different objects

## The claim

Let P_μ be the measurable functions X → [0, 1], identified when equal
μ-almost everywhere, read as graded participation or dispositional
predicates. Under pointwise minimum and maximum P_μ is a lattice, and
d_μ(p, q) = ∫|p − q| dμ is a metric on it (A29 §4). A29: "The
graded-function lattice is distributive under pointwise minimum and
maximum. Formal concept lattices need not be distributive." The
thresholded construction of Xiong (LIT-267, THEORY-698) and this one "are
not the same lattice".

## Proof and fill (the assistant's)

- **Distributive.** [0, 1] is a chain, so a distributive lattice, and a
  pointwise product of distributive lattices is distributive; identifying
  functions equal a.e. respects min and max.
- **A valuation metric.** v(p) = ∫p dμ is modular, since
  max(p, q) + min(p, q) = p + q gives v(p ∨ q) + v(p ∧ q) = v(p) + v(q),
  and strictly monotone on a.e.-classes. Then
  v(p ∨ q) − v(p ∧ q) = ∫(max − min) dμ = ∫|p − q| dμ = d_μ(p, q), so
  (P_μ, d_μ) is a metric lattice in Birkhoff's sense, not by analogy. The
  overlap of CLAIM-tmprq9q5 is v(p ∧ q).
- **Concept lattices.** Every complete lattice L is the concept lattice
  of the context (L, L, ≤) (the basic theorem of formal concept analysis),
  so concept lattices include M₃, where a ∧ (b ∨ c) = a and
  (a ∧ b) ∨ (a ∧ c) = 0.

## Check

python3 -I on random [0, 1] vectors: distributivity, max + min = p + q
and max − min = |p − q| hold to rounding; the M₃ computation gives a and
0.

## Where Xiong already has it

Xiong's paper has a soft algebra beside the thresholded one: the meet and
join profiles of two concepts are the pointwise min and max of their
attribute-projection profiles (Eq. 6; NOTE-240, claim C4, which finds that
under the paper's Eq. 5 the min profile behaves as an upper bound of A,
not a lower one). A29's graded lattice is that operation taken over a
measure, with its distributivity and metric stated. A29 did not say so.

## What it does not say

Which lattice a theory of perspectives should use. The graded lattice
keeps degree and overlap; the concept lattice keeps implications among
attributes, which A29 §3 calls the part that is "empirically meaningful".
