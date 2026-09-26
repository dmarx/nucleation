---
status: Deferred
status_note: seeded from the abstract and a skim on 2026-09-26; not read in full
title: 'What Representational Similarity Measures Imply about Decodable Information'
version: 1
tags:
- representation-learning
- neuroscience
- anthology-candidate
date: '2026-09-26'
published: '2024-11-12'
arxiv: '2411.08197'
first_author: 'Harvey'
keywords:
- 'representational similarity'
- 'linear decoding'
- 'CKA'
- 'CCA'
- 'Procrustes distance'
- 'participation ratio'
implementations: []
summary: >-
  Harvey et al. (2024), [ARXIV-2411.08197](https://arxiv.org/abs/2411.08197). For linear readouts regularised by w ↦ wᵀG(X)w, the optimal decoded signal is K_X z with K_X = X G(X)⁻¹ Xᵀ / M. The expected alignment of two networks' optimal readouts is therefore Tr(K_X K_z K_Y), which recovers linear CKA, CCA, GULP and ENSD as average decoding similarities. Procrustes distance bounds the average decoding distance from both sides, with constants set by a participation ratio.
---

# LIT-tmptlaw2: What Representational Similarity Measures Imply about Decodable Information

Sarah E. Harvey, David Lipshutz, Alex H. Williams (2024), *Proceedings of the II edition of the Workshop on Unifying Representations in Neural Models (UniReps 2024), as printed on the arXiv PDF; first appeared as arXiv preprint (proceedings volume and pages unverified)* — [ARXIV-2411.08197](https://arxiv.org/abs/2411.08197)

## Key takeaways

- For linear readouts regularised by w ↦ wᵀG(X)w, the optimal decoded signal is K_X z with K_X = X G(X)⁻¹ Xᵀ / M. The expected alignment of two networks' optimal readouts is therefore Tr(K_X K_z K_Y), which recovers linear CKA, CCA, GULP and ENSD as average decoding similarities. Procrustes distance bounds the average decoding distance from both sides, with constants set by a participation ratio.

*Seeded from the abstract and a skim, not a reading. What follows is what the work says about itself.*

Similarity measures such as CKA, CCA and Procrustes shape distance are usually motivated by their geometric invariances. The authors show that many of them can instead be derived from decoding: CKA and CCA measure the average alignment of optimal linear readouts over a distribution of decoding tasks. They further show that Procrustes distance upper-bounds the distance between optimal readouts, and that the converse holds when the representations have low participation ratio. The upshot is a tight link between representational geometry and linearly decodable information.

## Standing in the record

Filed on 2026-09-26 while pursuing, at the owner's request, the connection *GNS, unitary equivalence and the convergence of representations* (see the curation entry of that date). `Deferred` because nobody has read it closely here yet, not on merit.

Tagged `anthology-candidate` ([ADR-005](../decisions.d/ADR-005.md)): the seed judged it chiefly about machine-learning practice. It is kept here by the owner's decision of 2026-09-26 that new work stays in nucleation until a transfer is judged appropriate ([ADR-010](../decisions.d/ADR-010.md)).

**Priority for a deeper reading: medium — the main identities are simple and already captured; the value of a full read is appendix A.3 and the Proposition 3 proof.**

What a deeper reading should check:

- It turns "the kernel is what matters" into an operational statement: everything a regularised linear probe can read out is a function of the (normalised) kernel K_X. That is the practical content of "the representation is determined by its kernel up to rotation", and it connects to Riesz, since a probe is a functional and hence a vector.
- A deeper reading should check appendix A.3 (the M → ∞ and non-identity K_z case), where the Gram matrix becomes an operator on L²(data). That is where the GNS/L²(P) reading would live.
- It is a workshop paper; check the appendix proofs of Proposition 3 before relying on the bounds.

Access when seeded: Read the arXiv abstract page (v1 submitted 2024-11-12) and the full v1 PDF text (21 pp.): §§1–4 and the discussion (§5) in full; the appendix proofs were not read. The venue line comes from the PDF's own header.
