---
status: Active
status_note: 'read 2026-10-14 ([NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md)) in full; worth reading as the source of the dimension-reduction lemma, in the form its authors gave it: n points of ℓ₂ⁿ go into [K(τ) log n] dimensions with Lipschitz distortion (1+τ)/(1−τ), by a Haar-random orthogonal projection, proved by concentrating one projected norm about its median and taking a union bound over the normalized differences. Read it knowing that the τ⁻² dependence is in the proof (K ≥ (10/τ)²), not the statement; that the paper shows only that log n cannot be improved, not the τ-dependence; and that the lemma is a tool for the paper''s real subject, L(X, n) ≤ C(log n)^{1/2} for extending Lipschitz maps into ℓ₂.'
title: 'Extensions of Lipschitz mappings into a Hilbert space'
version: 3
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Filed, not read, at the owner's request after a survey found the record
    meets random projections from three directions without holding the
    result they share. Citation checked against Crossref on 2026-10-14. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d1573d2) for the title, the identifier and the result's name found nothing.
- version: 2
  date: '2026-10-14'
  note: >-
    Read in full (NOTE-tmpmv42v) from a scan of the published article,
    Contemporary Mathematics 26 (1984), pp. 189–206, hosted at
    web.stanford.edu/class/cs114/readings/JL-Johnson.pdf, extracted with
    pdftotext -layout and read from the page images where equations were
    lost. The copy confirms the authors, volume, year, pages and DOI. It
    gives only the year, so the `published:` day is a placeholder, and it
    does not print the proceedings title, which stays as Crossref gives
    it. The status moved from Deferred to Active; the summary and
    takeaways are rewritten from the text, correcting the standard
    statement in three places: the dimension is K(τ) log n with τ⁻² only
    in the proof, distortion is bounded as a product of Lipschitz
    constants, and the proof concentrates the norm about its median by
    Lévy's isoperimetric inequality, not the squared length about its
    mean. Standing in the record names the NOTE and qualifies the
    tightness claim. Keywords from the paper's own terms were added.
- version: 3
  date: '2026-10-16'
  note: >-
    Standing in the record names Indyk and Motwani's JL-type proof, which
    the record has held since 2026-10-15 (LIT-1106, NOTE-905), and no
    longer calls Larsen and Nelson unread.
tags:
- mathematics
date: '2026-10-14'
published: '1984-01-01'
doi: '10.1090/conm/026/737400'
first_author: 'Johnson'
keywords:
- 'Lipschitz extension'
- 'Hilbert space'
- 'finite metric spaces'
- 'random projection'
- 'Kirszbraun theorem'
- 'isoperimetric inequality'
- 'random rank k projection'
implementations: []
summary: >-
  Johnson & Lindenstrauss (1984), *Contemporary Mathematics* 26: 189–206. Lemma 1: for 1 > τ > 0 there is K(τ) such that any n points of ℓ₂ⁿ map into ℓ₂ᵏ, k = [K log n], with ‖f‖_lip‖f⁻¹‖_lip ≤ (1+τ)/(1−τ), by a Haar-random rank-k orthogonal projection with positive probability; the proof takes K ≥ (10/τ)². The lemma is the tool for Theorem 1, that a Lipschitz map from any n-point subset of a metric space into ℓ₂ extends to the whole space with constant at most C(log n)^{1/2}, verifying a Marcus–Pisier conjecture. A lower bound of order (Log n / Log Log n)^{1/p−1/2} for L_p, 1 ≤ p < 2, and an extension theorem for separated sets complete it.
extended_by:
- LIT-tmp8s1wj
- LIT-tmpcfdvm
- LIT-tmpjy3gf
- LIT-tmppzjx6
---

# LIT-tmp7skui: Extensions of Lipschitz mappings into a Hilbert space

William B. Johnson and Joram Lindenstrauss (1984), "Extensions of Lipschitz mappings into a Hilbert space", in *Conference in Modern Analysis and Probability*, Contemporary Mathematics 26: 189–206 — [doi:10.1090/conm/026/737400](https://doi.org/10.1090/conm/026/737400)

## Key takeaways

*From the reading, [NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md).*

- **Lemma 1, as stated.** For each 1 > τ > 0 there is K = K(τ) > 0 such
  that if A ⊂ ℓ₂ⁿ and card A = n, some f maps A onto a subset of ℓ₂ᵏ,
  k = [K log n], with ‖f‖_lip ‖f⁻¹‖_lip ≤ (1+τ)/(1−τ). The map is a random
  rank-k orthogonal projection U*QU, U Haar on O(n), and it works with
  positive probability, which can be pushed towards one by raising k.
- **Where τ⁻² comes from.** Only the proof. The failure probability is at
  most 2n(n+1) exp(−τ²K log n/18), "positive if, say, K ≥ (10/τ)²", so
  k = [100 τ⁻² log n] suffices.
- **How the proof works.** It concentrates the norm r(Uy) = √n‖QUy‖ of one
  projected unit vector about its median, with tail 4 exp(−nε²/2), by
  Lévy's isoperimetric inequality as used in Figiel, Lindenstrauss and
  Milman (1977). Khintchine's inequality puts the mean between √(k/2) and
  √k, and the median within a constant of it. A union bound over the at
  most n(n−1) normalized differences finishes it.
- **What is tight.** The log n: k dimensions hold at most 4ᵏ vectors at
  mutual distance ≥ 1 in a ball of radius 2, so an orthonormal set of more
  than 4ᵏ vectors cannot go into k dimensions with small distortion. The
  paper says nothing about the dependence on τ.
- **What it was for.** Theorem 1: every Lipschitz f from an n-point subset
  of a metric space into ℓ₂ extends with ‖f̃‖_lip ≤ K√(log n) ‖f‖_lip, by
  Lemma 1 with τ = 1/2, Kirszbraun's theorem, and the non-linear
  Hahn–Banach theorem in ℓ∞ᵏ, which costs √k.
- **The rest.** L(p, n) ≥ δ(Log n / Log Log n)^{1/p−1/2} for 1 ≤ p < 2
  (Theorem 3). Extensions from ε-separated sets of diameter D cost at most
  6D/ε into ℓ₂ (Theorem 2), and 4D/ε into any Banach space (Benyamini, in
  the appendix). An ε-net on the unit sphere of an n-dimensional space
  has at most (1 + 4/ε)ⁿ points (Lemma 3).

## Standing in the record

Filed on 2026-10-14 as the anchor for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md), and read
the same day in [NOTE-tmpmv42v](../notes.d/NOTE-tmpmv42v.md). The record held three uses of random
projections and not the lemma usually given for why they work: random
features for kernels ([LIT-679](LIT-679.md), [THEORY-106](../theory.d/THEORY-106.md)), the compressed-sensing
bound in Toy Models of Superposition ([NOTE-278](../notes.d/NOTE-278.md)), and the thresholded
random projections of sparse distributed memory ([NOTE-242](../notes.d/NOTE-242.md)) and the
insect olfactory code ([NOTE-670](../notes.d/NOTE-670.md)).

The reading bears on the question's distances thread. The proof has the
shape the question proposes: a threshold of order log of the family's size
over a squared tolerance, here τ⁻² log n from a union bound over point
pairs. It says nothing about random features or expand-and-threshold maps.
Its Lemma 3 net is the other ingredient a union bound over sparse supports
needs, which bears on the superposition thread. Its later proofs are
[LIT-tmpjy3gf](LIT-tmpjy3gf.md) and [LIT-tmppzjx6](LIT-tmppzjx6.md), and Indyk and Motwani's Gaussian proof of
a JL-type lemma, read for nearest-neighbour search ([LIT-1106](LIT-1106.md), [NOTE-905](../notes.d/NOTE-905.md),
Appendix A). The order ε⁻² log n is shown necessary for some point set,
up to a constant and for ε above about 1/√min{n, d}, in [LIT-tmp8s1wj](LIT-tmp8s1wj.md)
([NOTE-tmp4mti8](../notes.d/NOTE-tmp4mti8.md)). This paper proves only that the log n cannot be
improved, and does not state the ε⁻².

In the anthology the lemma appears without a LIT of its own, inside
Linformer's low-rank argument ([ANTH-LIT-529](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-529.md)). The subject is
mathematics, which no anthology topic holds.

Filed, with [LIT-tmpjy3gf](LIT-tmpjy3gf.md) and [LIT-tmppzjx6](LIT-tmppzjx6.md), as [THEORY-tmpns5kz](../theory.d/THEORY-tmpns5kz.md).
