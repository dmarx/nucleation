---
status: Deferred
status_note: 'unread, registered 2026-10-14 for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md) from Crossref metadata and the standard statement of its result. No attempt to read it is recorded.'
title: 'Extensions of Lipschitz mappings into a Hilbert space'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Filed, not read, at the owner's request after a survey found the record
    meets random projections from three directions without holding the
    result they share. Citation checked against Crossref on 2026-10-14. Not held in the Anthology of the SOTA: a grep of its record/ (clone at commit d1573d2) for the title, the identifier and the result's name found nothing.
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
implementations: []
summary: >-
  Johnson & Lindenstrauss (1984), *Contemporary Mathematics* 26: 189–206. The lemma: any n points in a Hilbert space map into O(ε⁻² log n) dimensions with every pairwise distance kept within a factor 1 ± ε, by a scaled projection onto a random subspace. The lemma was a step towards a Lipschitz-extension theorem; it is now cited for itself. Unread.
extended_by:
- LIT-tmp8s1wj
- LIT-tmpcfdvm
- LIT-tmpjy3gf
- LIT-tmppzjx6
---

# LIT-tmp7skui: Extensions of Lipschitz mappings into a Hilbert space

William B. Johnson and Joram Lindenstrauss (1984), "Extensions of Lipschitz mappings into a Hilbert space", in *Conference in Modern Analysis and Probability*, Contemporary Mathematics 26: 189–206 — [doi:10.1090/conm/026/737400](https://doi.org/10.1090/conm/026/737400)

## Key takeaways

*Unread. From the result as it is standardly stated, to be checked against the text.*

- **The lemma.** For n points in ℓ₂ and 0 < ε < 1, a projection onto a
  uniformly random k-dimensional subspace, rescaled, keeps every pairwise
  distance within 1 ± ε with positive probability once k = O(ε⁻² log n).
  The dimension does not depend on the ambient dimension.
- **Why it holds.** The squared length of a fixed vector's projection
  concentrates sharply around its mean (concentration of measure on the
  sphere), so a union bound over the n² pairs costs only log n.
- **What it was for.** It is a lemma in a paper about extending Lipschitz
  maps from subsets of metric spaces into Hilbert space, where it bounds
  an extension constant.

## Standing in the record

Filed on 2026-10-14 as the anchor for [QUESTION-tmpa0dq9](../questions.d/QUESTION-tmpa0dq9.md). The
record held three uses of random projections and not the theorem that
says why they work: random features for kernels ([LIT-679](LIT-679.md), [THEORY-106](../theory.d/THEORY-106.md)),
the compressed-sensing bound in Toy Models of Superposition ([NOTE-278](../notes.d/NOTE-278.md)),
and the thresholded random projections of sparse distributed memory
([NOTE-242](../notes.d/NOTE-242.md)) and the insect olfactory code ([NOTE-670](../notes.d/NOTE-670.md)). Its later proofs
are [LIT-tmpjy3gf](LIT-tmpjy3gf.md) and [LIT-tmppzjx6](LIT-tmppzjx6.md), and its bound is shown tight in [LIT-tmp8s1wj](LIT-tmp8s1wj.md).

In the anthology the lemma appears without a LIT of its own, inside
Linformer's low-rank argument ([ANTH-LIT-529](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-529.md)). The subject is
mathematics, which no anthology topic holds.
