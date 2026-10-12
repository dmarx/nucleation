---
status: Deferred
status_note: 'filed 2026-10-12 from the owner''s papers-feed, not read. Registered for [QUESTION-025](../questions.d/QUESTION-025.md), where it gives a measured case of correlated attributes yielding non-orthogonal, entangled concept directions. No NOTE is filed, and it stays Deferred until it is read, not on merit.'
title: 'Post-Hoc Concept Disentanglement: From Correlated to Isolated Concept Representations'
version: 1
history:
- version: 1
  date: '2026-10-12'
  note: >-
    Filed, not read. Found in the owner's papers-feed snapshot of 2026-10-11 by embedding
    similarity to QUESTION-025 and judged from the abstract. Citation checked against arXiv on
    2026-10-12: Eren Erogullari, Sebastian Lapuschkin, Wojciech Samek et al., arXiv:2503.05522,
    2025-03-07, which is the `published:` date. Not held in the Anthology of the SOTA: a grep of
    its record/ (clone at commit d8b5ba5) for the identifier and title found nothing.
tags:
- representation-learning
- anthology-candidate
date: '2026-10-12'
published: '2025-03-07'
arxiv: '2503.05522'
first_author: 'Erogullari'
keywords:
- 'concept activation vectors'
- 'correlated concepts'
- 'disentanglement'
- 'orthogonality'
- 'activation steering'
implementations: []
summary: >-
  Erogullari et al. (2025). The paper shows that concept activation vectors for concepts that
  co-occur in the data, such as "beard" and "necktie" in CelebA, come out similar and
  non-orthogonal. It proposes a post-hoc method with a non-orthogonality loss that finds
  orthogonal concept directions while keeping each one pointing the right way. It reports that the
  orthogonalized directions work better for activation steering, inserting or removing one concept
  with less effect on the correlated one. Not read.
---

# LIT-tmp3ad0u: Post-Hoc Concept Disentanglement: From Correlated to Isolated Concept Representations

Eren Erogullari, Sebastian Lapuschkin, Wojciech Samek, Frederik Pahde (2025), *arXiv:2503.05522*.

Filed for [QUESTION-025](../questions.d/QUESTION-025.md): it measures what happens to linear concept directions when attributes are
correlated in the data. Co-occurring attributes such as beard and necktie give entangled,
non-orthogonal directions, which is the correlated-attribute failure the question asks about.

*Seeded from the abstract, not a reading. A reading should check the claim above first.*
