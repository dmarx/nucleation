---
status: Active
status_note: >-
  read in part 2026-11-05 (NOTE-tmp6e0rl) from arXiv v2; worth reading as
  the open survey of multiparameter persistence: modules over grids are of
  wild representation type, good barcodes need not exist and the rank
  invariant is incomplete for two or more parameters, while the
  interleaving distance extends the bottleneck distance, is stable and
  universal, and is NP-hard to compute. Read beside Vipond (LIT-tmp75waa),
  which was itself read; not a stand-in. Its main limits: a survey whose
  topics follow the authors' interests, with many results cited rather
  than proved; nothing on direction or paths.
title: 'An Introduction to Multiparameter Persistence'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read in part on 2026-11-05 as an open survey read
    alongside Vipond (LIT-tmp75waa), for the owner's pasted synthesis on
    resource-bounded realizability (written by another assistant, A, in
    the same exchange as the emergency-readiness bibliography, pasted
    2026-11-04), whose Response 3 §5 says multiparameter persistence has
    "invariants and stability results" and a classification "more
    complicated than that of one-parameter persistence". The synthesis does
    not cite it; it was read because it states the classification
    difficulty and the stability results more fully. Not a stand-in:
    Vipond was read. Citation checked against Crossref and the arXiv API:
    Magnus Bakke Botnan and Michael Lesnick (Crossref gives the title in
    lower case), in Representations of Algebras and
    Related Structures (proceedings of ICRA 2020), EMS Series of Congress
    Reports, pp. 77–150, book chapter, published 2023-11-30,
    doi:10.4171/ECR/19/4. arXiv:2203.14289 [math.AT], v1 2022-03-27, which
    is `published:`. Not held before. Copy: arXiv v2 of 2023-03-13,
    https://arxiv.org/pdf/2203.14289, extracted with pdftotext; the EMS
    version was not consulted. Status set to Active.
tags:
- mathematics
date: '2026-11-05'
published: '2022-03-27'
arxiv: '2203.14289'
doi: '10.4171/ECR/19/4'
first_author: 'Botnan'
keywords:
- 'multiparameter persistence'
- 'wild representation type'
- 'good barcode'
- 'rank invariant'
- 'interleaving distance'
- 'stability'
- 'universality'
implementations: []
summary: >-
  Botnan & Lesnick (2022; EMS 2023). A survey of multiparameter persistent
  homology for data analysis. Modules decompose uniquely into
  indecomposables, but "multiparameter persistence modules have wild
  representation type", a module may have no good barcode (Example 4.6),
  and "for P = N2 , the rank invariant is incomplete." Practice uses
  incomplete invariants: Hilbert function, rank invariant, multigraded
  Betti numbers, generalized rank invariant, vectorizations such as
  Vipond's landscapes. The metrics behave well: the interleaving distance
  extends the bottleneck distance, is stable and, over prime fields,
  universal; but it is NP-hard to compute for two or more parameters.
---
<!-- inactive-ok-file: THEORY-tmprk262 NOTE-tmp6e0rl — Proposed, Skimmed or new; cited from the reading of Botnan & Lesnick (2023) as open -->

# LIT-tmp1045q: An Introduction to Multiparameter Persistence

Botnan, M. B. & Lesnick, M. (2023). An Introduction to Multiparameter Persistence. In *Representations of Algebras and Related Structures*, EMS Series of Congress Reports: 77–150. doi:10.4171/ECR/19/4. arXiv:2203.14289 (v1 2022).

## Key takeaways

*From the reading, NOTE-tmp6e0rl. Section numbers are arXiv v2's.*

- **Wild type** (§1.1, §8). "multiparameter persistence modules have wild
  representation type"; a classification "is thought to be a hopelessly
  difficult task" (§8.1), and "the representation type of a commutative
  grid is wild even for small grid sizes" (§8.2).
- **No good barcode** (§4.1, Example 4.6): "A simple argument by
  contradiction shows that M cannot have a good barcode".
- **Incomplete invariants** (§4.2): complete for one parameter; "However,
  for P = N2 , the rank invariant is incomplete."
- **Good metrics** (§1.2, §6.1): the interleaving distance is stable and
  universal over prime fields (Theorem 6.7), but "computing the
  interleaving distance on n-parameter persistence module is NP-hard for
  n ≥ 2".
- **Young** (§1.2): "applications of MPH are still in their infancy."

## Standing in the record

Read beside Vipond (LIT-tmp75waa) for the pasted synthesis on
resource-bounded realizability's sentence on multiparameter persistence,
which it shows to be accurate and understated: classification is
regarded as hopeless, and the natural distance between budget-indexed
modules is NP-hard to compute, an obstruction a programme comparing
architectures by such distances would meet. It treats only the first of A's
three levels, persistence; nothing on direction. Filed from it:
THEORY-tmprk262.
