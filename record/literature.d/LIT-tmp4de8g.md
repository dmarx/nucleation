---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmpz2cvc](../notes.d/NOTE-tmpz2cvc.md)) in full, from arXiv v1, with the
  comparison figures read from page renderings; worth reading as the
  systematic test of attribution patching against exhaustive activation
  patching on models up to 12B, for the two named causes of its misses
  (saturated attention, cancelling direct and indirect effects) and their
  fixes, and for the statistical bound on what is still missed
  ([THEORY-tmpo1u9l](../theory.d/THEORY-tmpo1u9l.md)). Read it knowing that the ground truth is single-node
  noising on one model family and five settings, that only ranks are
  scored, that the numbers are only in charts, and that AtP* is not the
  cheapest variant on its two distributions.
title: 'AtP*: An efficient and scalable method for localizing LLM behaviour to components'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 to register and
    read the core circuits literature the record lacked; registered as the
    record's entry for attribution patching. Checked on 2026-10-26 against
    the arXiv record: János Kramár, Tom Lieberum, Rohin Shah and Neel
    Nanda (Google DeepMind), arXiv 2403.00745, v1 submitted 1 March 2024
    and the only version, which is `published:`. The method's origin is
    Neel Nanda's post "Attribution Patching: Activation Patching At
    Industrial Scale" (https://www.neelnanda.io/mechanistic-interpretability/attribution-patching),
    published 4 February 2023 by the page's own metadata and describing
    work done at Anthropic in February–March 2022; it is not registered
    separately. The summary follows the arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpz2cvc) from arXiv v1: §§1–6, Appendices A, B and
    C.1; Figures 1, 2 and 9 from page renderings. Status Deferred → Active.
    Two accounts filed: THEORY-tmpo1u9l (Active) and THEORY-tmpq26u7
    (Proposed). The summary is checked against the reading and given the
    settings and the distributional exception.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-26'
published: '2024-03-01'
arxiv: '2403.00745'
first_author: 'Kramár'
keywords:
- 'attribution patching'
- 'activation patching'
- 'causal attribution'
- 'mechanistic interpretability'
- 'localization'
implementations: []
summary: >-
  Kramár, Lieberum, Shah & Nanda (2024), arXiv:2403.00745. Attribution
  patching (AtP; Nanda 2023), a first-order gradient estimate of every
  node's activation-patching effect, is tested against exhaustive patching
  on Pythia models from 410M to 12B. Verifying nodes in AtP's order finds
  the largest-effect nodes far more cheaply than unordered or
  sampling-based search. Its false negatives come from saturated attention
  and from cancelling direct and indirect effects; AtP* adds an exact
  softmax for queries and keys and layer-wise gradient dropout, and a
  subsampling test bounds the size of nodes still missed. On the two prompt
  distributions, simpler variants are cheaper than AtP*.
---
<!-- inactive-ok-file: THEORY-tmpq26u7 THEORY-tmpoirdq — Proposed; the wider thesis filed from this reading and a neighbouring account, cited as open -->

# LIT-tmp4de8g: AtP*: An efficient and scalable method for localizing LLM behaviour to components

Kramár, J., Lieberum, T., Shah, R. & Nanda, N. (2024). AtP\*: An efficient
and scalable method for localizing LLM behaviour to components.
arXiv:2403.00745.

The method it studies is from Nanda, N. (2023). Attribution patching:
Activation patching at industrial scale. Blog post, 4 February 2023,
https://www.neelnanda.io/mechanistic-interpretability/attribution-patching
(cited in the paper as "Nanda, 2022", the year of the underlying work).

Read in full on 2026-10-26 ([NOTE-tmpz2cvc](../notes.d/NOTE-tmpz2cvc.md)). Two accounts were drawn from
it: [THEORY-tmpo1u9l](../theory.d/THEORY-tmpo1u9l.md) and [THEORY-tmpq26u7](../theory.d/THEORY-tmpq26u7.md).

## Why this is here

The owner asked on 2026-10-26 how the record stood on neural circuit
theory; the answer found it held almost none of the core circuits
literature, and the owner said "go ahead and register and read those".
Attribution patching is the cheap estimate that made circuit search scale
to large models; its edge version with integrated gradients is how
[LIT-tmpf4hwb](LIT-tmpf4hwb.md) ([THEORY-tmpoirdq](../theory.d/THEORY-tmpoirdq.md)) and MIB's circuit track ([LIT-tmprlq7z](LIT-tmprlq7z.md))
find circuits, so the record held results built on it without the method
or its failure modes. This paper is registered for it, rather than
Nanda's post, because it tests the method against ground truth.
