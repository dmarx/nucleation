---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmphsgtx](../notes.d/NOTE-tmphsgtx.md)); worth reading as the short foundational argument for Contextuality-by-Default. The paper argues that the traditional reading of a Kochen–Specker or Bell-type contradiction (no joint distribution exists) cannot be right within Kolmogorovian probability, because being jointly distributed is transitive, so overlapping contexts already force one. The assumption a reductio refutes is "Noncontextual Identification", that a content is the same random variable in every context. The paper then restates contextuality as the impossibility of a coupling with a specified property C. It gives multimaximality as C for binary measurements, with the pairwise characterization (Theorem II.3) that CbD 2.0 ([LIT-tmpsa1qj](LIT-tmpsa1qj.md)) cites. It ends with Specker''s three boxes treated without assuming consistent connectedness.'
title: 'Probabilistic Foundations of Contextuality'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmphsgtx) from arXiv 1604.08412v4
    (7 Nov 2016, 10 pages, comment "To be published in Fortschritte der
    Physik - Progress of Physics. The last version corrects a typo"),
    text extracted with pdftotext. Details checked against arXiv (v1
    submitted 28 April 2016; journal ref Fortschr. Phys. 65, 1600040,
    2017) and Crossref (DOI 10.1002/prop.201600040, Fortschritte der
    Physik 65(6–8), published online 7 September 2016, print June 2017).
    `published:` is the arXiv v1 date. It is the second of the two arXiv
    ids LIT-777's footnote 10 gives for the multimaximal version; the
    paper titled "Contextuality-by-Default 2.0" is 1604.04799
    (LIT-tmpsa1qj). Not held in the Anthology of the SOTA: a grep of its
    record/ (clone of 2026-10-09, commit d8b5ba5) for the authors, the
    identifiers and the title found nothing.
tags:
- contextuality
- quantum-foundations
- mathematics
date: '2026-10-09'
published: '2016-04-28'
arxiv: '1604.08412'
doi: '10.1002/prop.201600040'
first_author: 'Dzhafarov'
keywords:
- 'contextuality'
- 'consistent connectedness'
- 'coupling'
- 'cyclic system'
- 'inconsistent connectedness'
- 'multimaximal coupling'
implementations: []
summary: >-
  Dzhafarov & Kujala (2017), Fortschr. Phys. 65:1600040. Being jointly
  distributed is transitive in Kolmogorovian probability. So if a
  measurement were the same random variable in every context, overlapping
  contexts would force a joint distribution, and Kochen–Specker and Bell
  contradictions would show that such variables do not exist. The
  assumption to drop is "Noncontextual Identification". Contextuality
  becomes the impossibility of a coupling of context-indexed variables in
  which same-content copies satisfy a property C. For inconsistently
  connected binary systems, C is multimaximality (Definition II.1).
extends:
- LIT-777
---

# LIT-tmpuzf4t: Probabilistic Foundations of Contextuality

Ehtibar N. Dzhafarov and Janne V. Kujala (2017), *Fortschritte der Physik –
Progress of Physics* 65(6–8), 1600040 — [ARXIV-1604.08412](https://arxiv.org/abs/1604.08412)

## Key takeaways

- **The transitivity argument** (Section I.3). Two random variables are
  jointly distributed exactly when they share a domain probability space,
  and that relation is transitive. In the traditional reading of KCBS,
  KS-4D or KS-3D, each observable is one random variable shared by
  overlapping contexts. Any path through the contexts then makes all of
  them jointly distributed. "No overall joint distribution exists" cannot
  be the conclusion of the contradiction.
- **The culprit is Noncontextual Identification** (Section I.4). Treating
  a measurement as the same random variable in every context is what the
  reductio refutes. Its replacement, Contextual Identification, indexes
  each variable by content and context. Stochastic Unrelatedness makes
  variables in different contexts have no joint distribution.
- **Contextuality as a coupling question** (S2, Definition I.1). A system
  is noncontextual if it has a coupling in which same-content variables
  satisfy C. Traditionally C is "equal with probability 1". For
  inconsistently connected binary systems, C is "equal with maximal
  possible probability" for every subset of a connection (Definition
  II.1).
- **The multimaximal coupling of a binary connection** is unique, with
  the staircase form, and it is characterized by maximal coupling of the
  adjacent pairs in the order of the means (Theorems II.2–II.3; II.2
  cited to [LIT-tmpsa1qj](LIT-tmpsa1qj.md), II.3 derived here). The cyclic criterion is
  restated (Theorem II.4, cited to Kujala & Dzhafarov 2016).
- **Specker's magic boxes** (Section III). Without consistent
  connectedness, the three-box system of Eq. (39) is noncontextual if and
  only if |⟨R_a^ab⟩ − ⟨R_a^ca⟩| + |⟨R_b^ab⟩ − ⟨R_b^bc⟩| + |⟨R_c^bc⟩ −
  ⟨R_c^ca⟩| ≥ 2 (Eq. 42). The absolute-value bars were lost in text
  extraction. The reading restored them because the condition is Theorem
  II.4 at n = 3 with all three correlations −1. Deterministic boxes are
  noncontextual.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request: a work the manuscript
considered and dropped from its final reference list. The bibliography
names CbD 2.0 by the pair of arXiv ids that [LIT-777](LIT-777.md)'s footnote 10 gives;
this is the second of them. See the curation entry of that day.

Read on 2026-10-09 ([NOTE-tmphsgtx](../notes.d/NOTE-tmphsgtx.md)). It is the record's statement of why CbD
indexes variables by context. It is also the place where the pairwise form
of multimaximality is derived, which CbD 2.0 ([LIT-tmpsa1qj](LIT-tmpsa1qj.md)) and the
canonical-systems paper ([LIT-tmp1kfuc](LIT-tmp1kfuc.md)) both cite.
