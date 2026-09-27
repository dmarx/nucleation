---
status: Active
status_note: 'read in full 2026-09-27 ([NOTE-tmp1umwm](../notes.d/NOTE-tmp1umwm.md)); worth reading as the founding statement of DisCoCat, whose ε/η composition, S-for-every-sentence design and "not"-as-swap every later paper in the programme starts from. Read it as a specification, not a result. It proves nothing, runs no experiment, leaves S and the verb tensors unbuilt, and its categorical framing (a product with a posetal pregroup) cannot tell apart the parse ambiguities it says it can reason about.'
title: 'Mathematical Foundations for a Compositional Distributional Model of Meaning'
version: 2
history:
- version: 2
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 1003.4394 v1 (the only version;
    submitted 23 Mar 2010, 118 KB), from the arXiv PDF, 34 pp. I read the
    abstract, §§1–7, the acknowledgements, footnotes 1–7 and the 41
    references. `pdftotext` was not available in this session, so I
    extracted the text with PyMuPDF. The string diagrams of §§2–4 (the
    reduction "under-links", the cups and caps, and the does/not diagrams)
    do not survive extraction. Each one sits next to its symbolic form, so I
    reconstructed them from the algebra; the one diagrammatic step I relied
    on, eq. (7), I checked through the paper's own symbolic computation (p.
    24). I checked the §5 similarity numbers and the basis-invariance of the
    ε/η composition numerically myself. I did not see the published
    Linguistic Analysis text. The arXiv record calls v1 "to appear", and I
    have not checked it against print.); the first NOTE on it, since it was
    seeded from the abstract alone. Status set from the reading: Active.
tags:
- linguistics
- mathematics
- logic
- philosophy-of-language
date: '2026-09-27'
published: '2010-03-23'
arxiv: '1003.4394'
first_author: 'Coecke'
keywords:
- 'DisCoCat'
- 'compositional distributional semantics'
- 'pregroup grammar'
- 'compact closed categories'
- 'tensor product'
implementations: []
summary: >-
  Coecke et al. (2010), [ARXIV-1003.4394](https://arxiv.org/abs/1003.4394). The paper builds DisCoCat as a
  product category FVect × P of vector spaces and a free pregroup. A
  sentence's meaning is f(w₁⊗…⊗wₙ), where f is the linear map got by
  putting vector spaces in place of the pregroup types in the reduction
  p₁…pₙ ≤ s. The ε maps become inner products and the η maps become Σᵢ
  eᵢ⊗eᵢ. So "John likes Mary" is Σ_ijk c_ijk⟨v|vᵢ⟩⟨w_k|w⟩ sⱼ ∈ S, and
  "not" is the 2×2 swap matrix placed on the sentence wire. There is no
  theorem and no experiment. The sentence space S is shown only as 1- or
  2-dimensional truth values, over a toy model with one basis vector per
  individual, and the paper says how neither S nor the verb tensors are to
  be built from data. Its headline similarity numbers (3/4, 1/4, 3/8) are
  unnormalised inner products. Under its own Definition 5.1 they are
  0.949, 0.316 and 0.6.
extended_by:
- LIT-tmp26v1l
---

# LIT-tmpunb3l: Mathematical Foundations for a Compositional Distributional Model of Meaning

Coecke, Sadrzadeh & Clark (2010), *Linguistic Analysis 36 (Lambek Festschrift), pp. 345–384* — [ARXIV-1003.4394](https://arxiv.org/abs/1003.4394)

## Standing in the record

Filed on 2026-09-27 at the owner's request, as the foundational paper for
Kartsaklis, Sadrzadeh, Pulman & Coecke ([LIT-tmp26v1l](LIT-tmp26v1l.md)), filed in the same
contribution. It is held here rather than in the anthology because it is a
formal account of linguistic meaning, not a practice. The journal volume and
pages come from the authors' own later citation; the journal carries no DOI.

It was filed `Deferred`, unread. [NOTE-tmp1umwm](../notes.d/NOTE-tmp1umwm.md) is the close reading of 2026-09-27, and it placed the work: **Active** — worth reading as the founding statement of DisCoCat, whose ε/η composition, S-for-every-sentence design and "not"-as-swap every later paper in the programme starts from. Read it as a specification, not a result. It proves nothing, runs no experiment, leaves S and the verb tensors unbuilt, and its categorical framing (a product with a posetal pregroup) cannot tell apart the parse ambiguities it says it can reason about.
