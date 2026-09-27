---
status: Active
status_note: 'read in full 2026-09-27 ([NOTE-tmp92a59](../notes.d/NOTE-tmp92a59.md)); worth reading as the place where the cohomological witness is shown complete for a named, large class (every All-vs-Nothing model, over any ring). It is also where the obstruction is defined as a connecting homomorphism. It does not supersede [LIT-277](LIT-277.md). It re-derives none of [LIT-277](LIT-277.md)''s computations, and it drops its negative results: the Hardy false positive and the strongly contextual cover with γ = 0. Its "paradox" title-word is supported by about one page of analogy and one worked identification.'
title: 'Contextuality, Cohomology and Paradox'
version: 2
history:
- version: 2
  date: '2026-09-27'
  note: >-
    Read in full (The full text of arXiv 1502.03097 v2, from the arXiv PDF,
    18 pp.: abstract, §§1–6, the Discussion, the acknowledgements and all 33
    references. There are no appendices. The arXiv abstract page lists two
    versions: v1 (10 Feb 2015, 33 KB, 21 pp. in the authors' own article
    format) and v2 (5 Mar 2017, 88 KB, comment "18 pages, 4 figures", in the
    LIPIcs format). I also read v1 in full (21 pp., §§1–6, the Discussion
    and 53 references), because v2 defers the proof of Prop 16 to "the full
    version of the paper [2]". That reference is arXiv 1502.03097 itself,
    and the proof survives only in v1 (Prop 5.7). I downloaded the published
    LIPIcs PDF from Dagstuhl DROPS and compared it word by word with v2. The
    two are identical apart from template metadata (the v2 PDF still carries
    LIPIcs placeholders: "John Q. Open and Joan R. Access", "ACM Subject
    Classification ddd", "LIPIcs.xxx.yyy.p"), page layout and the
    spelled-out forenames in the references. So v2 is the published text.
    `pdftotext` was not available, so I extracted the text with PyMuPDF. The
    equations and diagrams came through legibly, except the snake-lemma
    diagrams, which I read from their structure. Nothing was skipped. I
    re-ran the paper's checkable claims myself (details under Key
    results).); the first NOTE on it, since it was seeded from the abstract
    alone. Status set from the reading: Active.
tags:
- contextuality
- quantum-foundations
- mathematics
- logic
date: '2026-09-27'
published: '2015-02-10'
arxiv: '1502.03097'
doi: '10.4230/LIPIcs.CSL.2015.211'
first_author: 'Abramsky'
keywords:
- 'All-vs-Nothing arguments'
- 'strong contextuality'
- 'Čech cohomology'
- 'stabiliser quantum mechanics'
- 'Liar paradox'
implementations: []
summary: >-
  Abramsky et al. (2015), [ARXIV-1502.03097](https://arxiv.org/abs/1502.03097). For a model whose outcomes
  live in a commutative ring R, "All-vs-Nothing" (AvN_R) means the
  R-linear equations satisfied by every support section of every context
  have no global solution. Theorem 21 proves AvN_R(S) ⇒ SC(Aff S) ⇒
  CSC_R(S) ⇒ CSC_ℤ(S) ⇒ SC(S), so every AvN model is strongly contextual
  with a non-vanishing Čech obstruction on every section. Theorem 4 shows
  that every state stabilised by an "AvN triple" of n-qubit Pauli
  operators yields such a model. The "paradox" half proves much less: an
  informal identification of Liar cycles with strongly contextual support
  tables, one exact case (the length-4 Liar cycle is the PR box), and the
  cohomology of paradox deferred to future work.
extends:
- LIT-277
---

# LIT-tmp5bjvi: Contextuality, Cohomology and Paradox

Abramsky, Barbosa, Kishida, Lal & Mansfield (2015), *CSL 2015, LIPIcs 41, 211–228* — DOI-10.4230/LIPIcs.CSL.2015.211

## Standing in the record

Filed on 2026-09-27 at the owner's request, as the follow-up to [LIT-277](LIT-277.md)
(Abramsky, Mansfield & Barbosa 2011). `published:` is the arXiv v1 date
([ADR-002](../decisions.d/ADR-002.md)).

It was filed `Deferred`, unread. [NOTE-tmp92a59](../notes.d/NOTE-tmp92a59.md) is the close reading of 2026-09-27, and it placed the work: **Active** — worth reading as the place where the cohomological witness is shown complete for a named, large class (every All-vs-Nothing model, over any ring). It is also where the obstruction is defined as a connecting homomorphism. It does not supersede [LIT-277](LIT-277.md). It re-derives none of [LIT-277](LIT-277.md)'s computations, and it drops its negative results: the Hardy false positive and the strongly contextual cover with γ = 0. Its "paradox" title-word is supported by about one page of analogy and one worked identification.
