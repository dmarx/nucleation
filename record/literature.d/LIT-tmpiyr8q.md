---
status: Active
status_note: >-
  read 2026-11-12 ([NOTE-tmp5l4tx](../notes.d/NOTE-tmp5l4tx.md)) from arXiv v1. Worth reading as the record's plainest primary statement of personalization as amortization: one embedding learned in about two GPU-hours and re-used "for a multitude of new generations", against baselines that optimize for every creation.
title: 'An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read, from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). The record held no LIT with arXiv
    2208.01618, this title or this first author with this subject,
    checked on 2026-11-12. Checked against the arXiv API the same day:
    Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik and Daniel Cohen-Or, arXiv 2208.01618, v1 submitted 2022-08-02,
    which is `published:`. The summary follows the arXiv abstract and what
    A says of the work; a reading should check both.
- version: 2
  date: '2026-11-12'
  note: >-
    Read (NOTE-tmp5l4tx) from arXiv v1 (2208.01618, 2 August 2022, the only version). Read: abstract, §§1–7, evaluation, user study, limitations, societal impact and conclusion. Supplementary pages skimmed; references skipped. Status Deferred to Active. THEORY-tmpc6xzg filed. Venue or type: arXiv preprint (the PDF footer reads "Preprint. Under review."); no venue on the arXiv record. Corrections: None. The summary is rewritten from the reading.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-12'
published: '2022-08-02'
arxiv: '2208.01618'
first_author: 'Gal'
keywords:
- 'textual inversion'
- 'personalization'
- 'word embedding'
- 'text-to-image'
implementations: []
summary: >-
  Gal et al. (2022), arXiv 2208.01618, read in [NOTE-tmp5l4tx](../notes.d/NOTE-tmp5l4tx.md). A concept is learned from 3–5 images as one new token embedding in the text-encoder input space of a frozen latent diffusion model, in about two hours, and then re-used without further optimization, in new prompts and in downstream models "that build on the same initial LDM model"; its authors say it does not preserve a person's identity. Registered from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44). It bears on [CASE-tmp40vka](../cases.d/CASE-tmp40vka.md), [CLAIM-tmpnwq8a](../claims.d/CLAIM-tmpnwq8a.md) and [QUESTION-095](../questions.d/QUESTION-095.md).
---
<!-- inactive-ok-file: THEORY-tmpc6xzg CASE-tmp40vka CLAIM-tmpnwq8a — Proposed; the reading's account and the entries it bears on, filed on the same branch -->

# LIT-tmpiyr8q: An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion

Rinon Gal, Yuval Alaluf, Yuval Atzmon, Or Patashnik, Amit H. Bermano, Gal Chechik and Daniel Cohen-Or (2022). "An Image is Worth One Word: Personalizing Text-to-Image Generation using Textual Inversion." arXiv 2208.01618; arXiv preprint (the PDF footer reads "Preprint. Under review."); no venue on the arXiv record.

## Key takeaways

Read in [NOTE-tmp5l4tx](../notes.d/NOTE-tmp5l4tx.md); the account is [THEORY-tmpc6xzg](../theory.d/THEORY-tmpc6xzg.md). Personalization by inverting a concept into the text-embedding space of a frozen model: the learned artifact is one input vector, not new weights.

## Standing in the record

Registered on 2026-11-12 from the exchange "Identify Synthesis Opportunities" (2026-11-08, https://chatgpt.com/share/6af51819-4de8-83ea-b5aa-5edc65869c44), for the history of how image
generators keep a character's identity ([CASE-tmp40vka](../cases.d/CASE-tmp40vka.md)), and read the same
day at the owner's request. It is machine-learning method, read here for
the economics of amortization ([QUESTION-095](../questions.d/QUESTION-095.md)), not for practice.
