---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmpg0dnu](../notes.d/NOTE-tmpg0dnu.md)) in full, from the arXiv copy (v2, the
  NeurIPS 2023 version); worth reading as the direct test of whether causal
  tracing tells where to edit a fact: in GPT-J, fact by fact, it does not.
  The tracing effect at a layer adds at most 3.2 points of explained
  variance in edit success once the edit layer is known, and ROME's
  rewrite score is above 96% at every layer but the last
  ([THEORY-tmpg87ki](../theory.d/THEORY-tmpg87ki.md)). Read it knowing that its own account of why, that
  tracing and editing answer different questions, is offered and not
  tested ([THEORY-tmpiz2n7](../theory.d/THEORY-tmpiz2n7.md)), that "where a fact is stored" means where
  causal tracing peaks, and that its Table 3 and Figure 6 disagree on one
  cell.
title: 'Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("get started
    on the seven works and markov IBP"): one of the works the circuits
    readings named without registering (curation entry of 2026-10-27,
    "Named by the readings, not registered"). Checked as not held: a
    search of literature.d and notes.d for the identifier, the title
    and the first author found only the mentions in NOTE-1166 and
    NOTE-782. Checked on 2026-10-27 against the arXiv record: Peter
    Hase, Mohit Bansal, Been Kim and Asma Ghandeharioun, arXiv
    2301.04213, v1 submitted 10 January 2023, which is `published:`
    (ADR-002); v2 of 16 October 2023 carries the comment "NeurIPS 2023
    (Spotlight)". The summary follows the arXiv abstract.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmpg0dnu) from the arXiv PDF of 2301.04213v2,
    fetched 2026-10-27. v1 was not compared. Status Deferred → Active.
    Two accounts filed: THEORY-tmpg87ki (Active) and THEORY-tmpiz2n7
    (Proposed). The summary is checked against the reading and kept,
    with the measured quantities added.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-27'
published: '2023-01-10'
arxiv: '2301.04213'
first_author: 'Hase'
keywords:
- 'causal tracing'
- 'localization'
- 'model editing'
- 'ROME'
- 'MEMIT'
- 'CounterFact'
- 'representation denoising'
implementations: []
summary: >-
  Hase et al. (2023), arXiv:2301.04213, NeurIPS 2023. On 652 CounterFact
  facts GPT-J knows, the layer where causal tracing places a fact does not
  predict at which MLP layer an edit of that fact succeeds: regressing edit
  success on the edit layer explains most of its variance, and adding the
  tracing effect adds at most 3.2 points of R², across ROME, MEMIT,
  constrained fine-tuning and five editing problems, and again on GPT-2 XL,
  zsRE and representation zeroing. Only Fact Forcing, which edits on the
  same noised input tracing uses, shows a small reliable relation.
---
<!-- inactive-ok-file: THEORY-tmpiz2n7 THEORY-1011 — Proposed; the account filed from this reading and the storage hypothesis it tests, cited as open -->

# LIT-tmpg22tp: Does Localization Inform Editing? Surprising Differences in Causality-Based Localization vs. Knowledge Editing in Language Models

Hase, P., Bansal, M., Kim, B. and Ghandeharioun, A. (2023). Does
localization inform editing? Surprising differences in causality-based
localization vs. knowledge editing in language models. *NeurIPS 2023*.
arXiv:2301.04213.

Read in full on 2026-10-27 ([NOTE-tmpg0dnu](../notes.d/NOTE-tmpg0dnu.md)). Two accounts were drawn
from it: [THEORY-tmpg87ki](../theory.d/THEORY-tmpg87ki.md) and [THEORY-tmpiz2n7](../theory.d/THEORY-tmpiz2n7.md).

## Why this is here

Registered and read at the owner's request of 2026-10-27, to fill a gap
the circuits readings of 2026-10-26 named. The reading of ROME
([LIT-1536](LIT-1536.md), [NOTE-1166](../notes.d/NOTE-1166.md)) filed the storage hypothesis [THEORY-1011](../theory.d/THEORY-1011.md)
Proposed, and its promote_when asks for exactly this test: whether the
layer where causal tracing finds a fact predicts, fact by fact, where an
edit of that fact succeeds. [NOTE-782](../notes.d/NOTE-782.md), the reading of Makelov et al.
([LIT-968](LIT-968.md)), already cited the finding without the record holding it. It
is the empirical half of the argument whose formal half is Makelov et
al.'s Lemma D.2: a successful edit at a layer does not show that the
fact is there.
