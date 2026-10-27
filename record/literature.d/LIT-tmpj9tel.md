---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmp1iis8](../notes.d/NOTE-tmp1iis8.md)) in full, from the arXiv copy; worth
  reading as the first end-to-end circuit for a natural behaviour in a
  pretrained language model, for path patching, for the backup heads that
  take over when the main ones are knocked out, and for its three tests of
  a circuit explanation, which its own circuit passes on average and fails
  under a greedy search ([THEORY-tmpccb5u](../theory.d/THEORY-tmpccb5u.md)). Read it knowing that the
  behaviour is fifteen templates in one model, that MLPs are left out of
  the circuit though removing them breaks the task, that the dropout
  explanation of the backups is a hypothesis ([THEORY-tmpmd4za](../theory.d/THEORY-tmpmd4za.md)), and that a
  few of its numbers and its greedy algorithm do not match their
  descriptions.
title: 'Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26: asked "how's
    the record on neural circuit theory?", the answer found the record held
    almost none of the core circuits literature, and the owner said "go
    ahead and register and read those". Checked on 2026-10-26 against the
    arXiv record: Kevin Wang, Alexandre Variengien, Arthur Conmy, Buck
    Shlegeris and Jacob Steinhardt (Redwood Research and UC Berkeley),
    arXiv 2211.00593, v1 submitted 1 November 2022, the only version,
    which is `published:`. The arXiv record names no venue. The summary
    follows the arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmp1iis8) from the arXiv PDF of 2211.00593v1,
    fetched 2026-10-26: §§1–6 and Appendices A–M. Status Deferred →
    Active. Two accounts filed: THEORY-tmpccb5u (Active) and
    THEORY-tmpmd4za (Proposed). The summary is checked against the reading
    and extended with the faithfulness and completeness results.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-26'
published: '2022-11-01'
arxiv: '2211.00593'
first_author: 'Wang'
keywords:
- 'indirect object identification'
- 'circuit analysis'
- 'path patching'
- 'GPT-2 small'
- 'backup name mover heads'
- 'faithfulness, completeness, minimality'
- 'mechanistic interpretability'
implementations: []
summary: >-
  Wang et al. (2022), arXiv:2211.00593. On sentences like "When Mary and
  John went to the store, John gave a drink to", GPT-2 small predicts the
  indirect object through 26 attention heads in seven classes, found by
  path patching: duplicate-token and induction heads mark the repeated
  name, S-inhibition heads pass that on, and name mover heads copy the
  remaining name. Mean-ablating every other head keeps 87% of the logit
  difference. Knocking out the name movers costs only 5%, because backup
  heads take over, and a greedy search finds knockouts under which circuit
  and model differ by up to 87%.
---
<!-- inactive-ok-file: THEORY-tmpmd4za — Proposed; the hypothesis filed from this reading, cited as open -->

# LIT-tmpj9tel: Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small

Wang, K., Variengien, A., Conmy, A., Shlegeris, B. and Steinhardt, J.
(2022). Interpretability in the wild: a circuit for indirect object
identification in GPT-2 small. arXiv:2211.00593.

Read in full on 2026-10-26 ([NOTE-tmp1iis8](../notes.d/NOTE-tmp1iis8.md)). Two accounts were drawn from
it: [THEORY-tmpccb5u](../theory.d/THEORY-tmpccb5u.md) and [THEORY-tmpmd4za](../theory.d/THEORY-tmpmd4za.md).

## Why this is here

Registered and read at the owner's request of 2026-10-26, after an answer to
"how's the record on neural circuit theory?" found that the record held
almost none of the core circuits literature. The record already relied on
its circuit second-hand. The Mechanistic Interpretability Benchmark's
circuit track and its causal-variable IOI task are built on it
([LIT-tmprlq7z](LIT-tmprlq7z.md)), and Makelov et al.'s interpretability illusion ([LIT-968](LIT-968.md),
[THEORY-282](../theory.d/THEORY-282.md)) is shown on its MLP8, with the faithful residual direction
written only by its S-inhibition heads. It is the record's first full
circuit for a natural behaviour in a pretrained model, as against the toy
and attention-only models of [LIT-tmp9dono](LIT-tmp9dono.md) and [LIT-tmpe7b5o](LIT-tmpe7b5o.md).
