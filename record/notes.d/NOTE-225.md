---
number: 225
status: Skimmed
formerly:
- NOTE-tmpfq8cv
paper: LIT-257
title: 'What Similarity Measures Imply about Decodability'
version: 1
date: '2026-09-26'
summary: >-
  For linear readouts regularised by w ↦ wᵀG(X)w, the optimal decoded signal is K_X z with K_X = X G(X)⁻¹ Xᵀ / M. The expected alignment of two networks' optimal readouts is therefore Tr(K_X K_z K_Y), which recovers linear CKA, CCA, GULP and ENSD as average decoding similarities. Procrustes distance bounds the average decoding distance from both sides, with constants set by a participation ratio.
---
<!-- inactive-ok-file: LIT-257 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-225: What Similarity Measures Imply about Decodability

## Contribution

Similarity measures such as CKA, CCA and Procrustes shape distance are usually motivated by their geometric invariances. The authors show that many of them can instead be derived from decoding: CKA and CCA measure the average alignment of optimal linear readouts over a distribution of decoding tasks. They further show that Procrustes distance upper-bounds the distance between optimal readouts, and that the converse holds when the representations have low participation ratio. The upshot is a tight link between representational geometry and linearly decodable information.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.1, eqs. (1)–(2): a readout maximises z·Xw/M − ½wᵀG(X)w, so w* = G(X)⁻¹Xᵀz/M. Ridge regression is the case G = C_X + λI.
- §2.2, eq. (7): ⟨Xw*, Yv*⟩ = zᵀK_X K_Y z with K_X := X G(X)⁻¹ Xᵀ/M. Proposition 1 gives the best and worst case over tasks as extreme eigenvalues of ½(K_X K_Y + K_Y K_X). Proposition 2 gives the average case, E⟨Xw*, Yv*⟩ = Tr(K_X K_z K_Y).
- §3, Corollary 1 and Table 1: with K_z = I, the expected readout similarity is Tr[K_X K_Y] and the expected squared readout distance is ‖K_X − K_Y‖²_F. G = bI gives linear CKA, G = C_X + λI gives GULP, G = C_X gives the mean squared canonical correlation, and a trace-scaled identity gives ENSD.
- §4, eqs. (22)–(23): G(XR)⁻¹ = RᵀG(X)⁻¹R for orthogonal R, so K_X is unchanged under X ↦ XR. Proposition 3 (eqs. 25–26) bounds the Procrustes distance of the normalised representations by the average decoding distance, from both sides, with constants depending on the participation ratio R_Δ of K_X − K_Y. The proof uses the Procrustes–Bures equivalence.
- §5: the framework is for finite M. The authors name the population (M → ∞) version and linear classifiers as future work.

## Open questions

- It turns "the kernel is what matters" into an operational statement: everything a regularised linear probe can read out is a function of the (normalised) kernel K_X. That is the practical content of "the representation is determined by its kernel up to rotation", and it connects to Riesz, since a probe is a functional and hence a vector.
- A deeper reading should check appendix A.3 (the M → ∞ and non-identity K_z case), where the Gram matrix becomes an operator on L²(data). That is where the GNS/L²(P) reading would live.
- It is a workshop paper; check the appendix proofs of Proposition 3 before relying on the bounds.
