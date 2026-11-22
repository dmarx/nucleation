---
status: Proposed
title: 'A non-abelian group learned from one-hot composition with no matrix representation imposed yields its irreducibles to a blind recovery that is given only the operation the network itself computes, exactly when the network has learned the group, and a group-supplied control recovers the same irreducibles, so the gate is the network''s competence and not the method'
version: 1
role: thesis
warrant: empirical
defeated_if: >-
  A network that has learned the group — it generalises to held-out
  products and the operation it computes by argmax is a valid group table
  equal to the true one — yet whose irreducibles the blind recovery fails to
  return or returns differently from the group-supplied control on the same
  table; or a demonstration that the blind path was in fact handed the true
  group, its Cayley table or its representations rather than the network's own
  reconstructed operation.
tags:
- representation-learning
- learning-theory
- mathematics
date: '2026-11-22'
line:
- learned-structure
answers:
- QUESTION-058
grounds:
- CASE-tmpjgjtj
---

<!-- inactive-ok-file: THEORY-022 — Proposed; cited in prose for the contrast with the abelian case -->
<!-- inactive-ok-file: CASE-tmpjgjtj — Proposed; the study this claim is grounded in, filed in the same batch -->

# CLAIM-tmpie2v3: A non-abelian group learned from one-hot composition with no matrix representation imposed yields its irreducibles to a blind recovery that is given only the operation the network itself computes, exactly when the network has learned the group, and a group-supplied control recovers the same irreducibles, so the gate is the network's competence and not the method

## The claim

[QUESTION-058](../questions.d/QUESTION-058.md) asks how much of a group's structure in a trained
representation can be read off the weights without the group being supplied.
[CASE-tmpjgjtj](../cases.d/CASE-tmpjgjtj.md) settles this for a non-abelian task where no matrix
representation is imposed: elements are one-hot indices over arbitrary labels
and the network learns the multiplication by softmax classification.

The recovery is blind in a precise sense. The only operation it uses is the
one the network itself computes — the table `T_net[g,h] = argmax` of the
logits, a forward pass through the weights, never the true group. From
`T_net` alone it derives the conjugacy classes, the class-sum operators of the
group algebra, their Peter–Weyl isotypic blocks, and hence the number of
irreducibles, their dimensions and the full character table. On the networks
that learned the group (S4 generalising to held-out products; S3 fit on the
whole table), `T_net` is a valid group equal to the true table, and the blind
recovery returns S4's `[1,1,2,3,3]` and S3's `[1,1,2]` with their exact
character tables, matching the group-supplied control to an orthogonality
residual near 10⁻¹⁴. On the network that only memorised (S3 at a 25% holdout,
test accuracy ≈ 0), `T_net` is not a group — associativity fails — and the
blind path refuses. The control, run on the true table, recovers the
irreducibles regardless, so the failure is the network's, not the method's:
the irreducibles are recoverable blind precisely when the network has learned
the group.

This is recovery up to isomorphism — characters, dimensions and the isotypic
projectors — not a canonical matrix `ρ(g)` per element, which is fixed only up
to a basis within each isotypic block ([CLAIM-135](CLAIM-135.md), [CLAIM-148](CLAIM-148.md)). It also
sharpens the abelian reading [THEORY-022](../theory.d/THEORY-022.md), whose spectral test saw the
irreducibles "only as pairs": that pairing is an artifact of ℤ/p's complex
one-dimensional characters, and does not arise here, where real non-abelian
irreducibles of dimension up to three are separated individually.

## What it does not say

It does not say every group-composition network develops recoverable
irreducibles, nor that recovery needs no information from the network: it needs
the network to have *learned the group*, which is read off the network's own
behaviour, not assumed. It does not claim canonical per-element matrices, only
identification up to equivalence. The evidence is three small groups at a few
seeds; the mechanism by which a generalising network comes to compute a valid
group is not addressed here.

The wording is the assistant's (Claude, in this session); adopting it is the
owner's call.
