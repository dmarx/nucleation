---
status: Active
status_note: >-
  read 2026-11-12 ([NOTE-tmpc56d2](../notes.d/NOTE-tmpc56d2.md)) in full from arXiv v2. Worth reading as a primary source that reference conditioning was offered in 2025 in place of LoRA training, at 3–5 s per 1024² image, and for its own genealogy of training-free personalization back to IP-Adapter. It does not compare against a character LoRA.
title: 'FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). The record held no LIT with arXiv
    2506.15742, this title or this first author with this subject,
    checked on 2026-11-12. Checked against the arXiv API the same day:
    Black Forest Labs, Stephen Batifol, Andreas Blattmann, Frederic Boesel and others (the arXiv record lists the laboratory as the first author), arXiv 2506.15742, v1 submitted 2025-06-17,
    which is `published:`. The summary follows the arXiv abstract and what
    A says of the work; a reading should check both.
- version: 2
  date: '2026-11-12'
  note: >-
    Read (NOTE-tmpc56d2) from arXiv v2 (2506.15742, 24 June 2025; v1 of 17 June 2025). Read in full: abstract, §§1–5; appendix A skimmed; references skimmed. Fig. 8's bar values are not in the text extraction, so the evaluation is as the authors' prose states it. Status Deferred to Active. THEORY-tmpdzbq1 filed. Venue or type: company report on arXiv (cs.GR); no venue. Corrections: None. The paper asks to be cited as "Black Forest Labs (2025)", which matches first_author. The summary is rewritten from the reading.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2025-06-17'
arxiv: '2506.15742'
first_author: 'Black Forest Labs'
keywords:
- 'FLUX.1 Kontext'
- 'flow matching'
- 'in-context image editing'
- 'character reference'
implementations: []
summary: >-
  Black Forest Labs (2025), arXiv 2506.15742, read in [NOTE-tmpc56d2](../notes.d/NOTE-tmpc56d2.md). A 12B flow-matching transformer, fine-tuned from a FLUX.1 checkpoint to condition on a context image by sequence concatenation, renders a character from that image in new scenes and across edits "without the need for finetuning [43] or LoRA training", at 3–5 s per image; on the authors' KontextBench it leads on character reference. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). It bears on [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), [CASE-tmp3isyl](../cases.d/CASE-tmp3isyl.md) and [QUESTION-095](../questions.d/QUESTION-095.md).
---
<!-- inactive-ok-file: THEORY-tmpdzbq1 CASE-tmp40vka CASE-tmp3isyl — Proposed; the reading's account and the entries it bears on, filed on the same branch -->

# LIT-tmp4meti: FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space

Black Forest Labs, with Stephen Batifol and 22 others (2025). "FLUX.1 Kontext: Flow Matching for In-Context Image Generation and Editing in Latent Space." arXiv 2506.15742; company report on arXiv (cs.GR); no venue.

## Key takeaways

Read in [NOTE-tmpc56d2](../notes.d/NOTE-tmpc56d2.md); the account is [THEORY-tmpdzbq1](../theory.d/THEORY-tmpdzbq1.md). One in-context image model for generation and editing, in which character consistency comes from the context image at inference, fast enough for iterative work, with a crowd-sourced benchmark.

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image
generators keep a character's identity ([CASE-tmp40vka](../cases.d/CASE-tmp40vka.md)), and read the same
day at the owner's request. It is machine-learning method, read here for
the economics of amortization ([QUESTION-095](../questions.d/QUESTION-095.md)), not for practice.
