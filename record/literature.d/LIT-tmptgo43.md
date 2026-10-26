---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpbsp9v) in full, from the arXiv copy (v2, the
  NeurIPS 2024 version); worth reading as the source of transcoder circuit
  analysis, for the factorization of a feature-to-feature attribution into
  an input-dependent activation times an input-invariant weight
  (THEORY-tmp9ii0y), on which the attribution graphs of LIT-tmpsuo6l are
  built, and for its blind case studies, which grade the method against
  hidden prompts and report the failures. Read it knowing that the
  comparison with SAEs is one learning rate, one seed and three models
  (THEORY-tmptjiep), that Gemma Scope found the reverse on Gemma 2 2B
  (NOTE-482), that attention patterns are frozen and QK circuits are not
  explained, and that its counts of case studies disagree between sections.
title: 'Transcoders Find Interpretable LLM Feature Circuits'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read, at the owner's request of 2026-10-26 to register and
    read the core circuits literature the record lacked. Checked on
    2026-10-26 against the arXiv record: Jacob Dunefsky, Philippe Chlenski
    and Neel Nanda, arXiv 2406.11944, v1 submitted 17 June 2024, which is
    `published:` (ADR-002); v2 of 6 November 2024 carries the comment
    "NeurIPS 2024". The summary follows the arXiv abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full (NOTE-tmpbsp9v) from the arXiv PDF of 2406.11944v2, 29
    pages, fetched 2026-10-26: the main text, Appendices A–H and the
    references. Status Deferred → Active. Two accounts filed:
    THEORY-tmp9ii0y (Active, re-derived) and THEORY-tmptjiep (Active, one
    study, narrowed to the models measured). The summary is checked against
    the reading and kept, with the three models named.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-26'
published: '2024-06-17'
arxiv: '2406.11944'
first_author: 'Dunefsky'
keywords:
- 'transcoders'
- 'circuit analysis'
- 'sparse autoencoders'
- 'mechanistic interpretability'
- 'greater-than circuit'
- 'GPT-2'
implementations: []
extended_by:
- LIT-tmpsuo6l
summary: >-
  Dunefsky, Chlenski and Nanda (2024), arXiv:2406.11944, NeurIPS 2024.
  A transcoder is a wide, sparsely activating ReLU MLP trained to imitate
  one MLP sublayer's input–output map. With attention patterns frozen, the
  attribution of one transcoder feature to a later one factors into the
  earlier feature's activation times an input-invariant dot product of
  decoder and encoder vectors, which allows weights-based circuit analysis
  through MLPs. On GPT2-small, Pythia-410M and Pythia-1.4B transcoders are
  at least on par with MLP SAEs in sparsity, faithfulness and
  human-rated interpretability, and they give a sparse account of MLP10 in
  GPT2-small's greater-than circuit.
---
<!-- inactive-ok-file: THEORY-022 CLAIM-tmpwr001 — Proposed; neighbouring accounts and the record's own claim, named, nothing here rests on them -->

# LIT-tmptgo43: Transcoders Find Interpretable LLM Feature Circuits

Dunefsky, J., Chlenski, P., & Nanda, N. (2024). Transcoders find
interpretable LLM feature circuits. *NeurIPS 2024*. arXiv:2406.11944.

Read in full on 2026-10-26 (NOTE-tmpbsp9v). Two accounts were drawn
from it: THEORY-tmp9ii0y and THEORY-tmptjiep.

## Why this is here

Registered and read at the owner's request of 2026-10-26, after the
question "how's the record on neural circuit theory?" found that the
record held almost none of the core circuits literature. The record's
circuits line had reverse-engineered circuits in small or algorithmic
models (LIT-345, LIT-tmpe7b5o), sparse dictionaries as units (LIT-323,
LIT-611) and a benchmark for localization (LIT-tmprlq7z), but no method
for tracing a circuit through MLP layers in terms of features. This is
that method's source, and the direct ancestor of the attribution graphs of
LIT-tmpsuo6l. It bears on CLAIM-tmpwr001 (a feature recovered from activity
is not yet the variable that does the work) and on QUESTION-tmpivbso
(what a circuit-only description over checkpoints could be).
