---
status: Active
status_note: >-
  read in full 2026-10-29 ([NOTE-tmpruw1i](../notes.d/NOTE-tmpruw1i.md)) from the Findings of EMNLP 2026
  PDF, with the released items counted; worth reading for its
  native-authored, culturally specific pragmatic items in four Indic
  languages and its evidence that LLM errors lean literal. Its translation
  and inference tasks use different items, and no agreement between people
  is reported.
title: 'VakyArth: Evaluating Pragmatic Competence in LLMs across Indic Languages'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A5 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2026-09-01 (Findings of
    EMNLP 2026, pp. 43027–43041) (ADR-002).
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from the Findings of EMNLP 2026 PDF (ACL Anthology
    2026.findings-emnlp.2022); the arXiv v1 text is the same. The
    released data were counted: the 578 items are 204 translation and
    374 MCQ and NLI items, and only one translation source overlaps an
    inference item, which corrects the description in Why this is here.
    Tagged anthology-candidate for its advice on MT evaluation
    (ADR-005). The summary is rewritten from the text. Status Deferred
    to Active.
tags:
- pragmatics
- translation
- anthology-candidate
date: '2026-10-29'
published: '2026-09-01'
arxiv: '2609.01788'
first_author: 'Singh'
keywords:
- 'pragmatics'
- 'Indic languages'
- 'benchmark'
- 'implicature'
- 'deixis'
- 'speech acts'
implementations: []
summary: >-
  Singh et al. (2026). 578 items written by four native speakers, one per
  language, in Hindi, Punjabi, Tamil and Malayalam, over deixis, speech
  acts, implicature, social pragmatics and coherence, as disjoint MCQ, NLI
  and translation sets. Five LLMs score higher on MCQ than NLI in every
  model–language pair, and when wrong they pick the literal reading 59.1%
  of the time against 33.3% by chance. On 416 model translations, COMET
  correlates with one native rater per language at r = 0.81, better than
  XCOMET or MetricX, though hand-picked inverted translations score
  highly. The finding that translation "does not track" pragmatic
  understanding compares different items, and no inter-rater agreement is
  given.
---

# LIT-tmpog7aw: VakyArth: Evaluating Pragmatic Competence in LLMs across Indic Languages

Singh, U., Veera Balaji Kumar, P., Nanda, P., Madhusoodanan, A., Guo, G., Xu, W., & Li, J. J. (2026). VakyArth: Evaluating pragmatic competence in LLMs across Indic languages. *Findings of EMNLP 2026*, 43027–43041.

Read in full in [NOTE-tmpruw1i](../notes.d/NOTE-tmpruw1i.md).

## Why this is here

A5's reason: it sets translation tasks and pragmatic inference on related material, which is the separation [CLAIM-202](../claims.d/CLAIM-202.md) wants measured, and A5 reported its finding that fluent translations can miss pragmatic meaning. Its subject is model evaluation; [CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md) would need its items read by human receivers.

Correction from the reading: the material is related by phenomenon only. VakyArth's 204 translation items and 374 MCQ and NLI items are separate, so it cannot supply the item-level separation [CLAIM-202](../claims.d/CLAIM-202.md) wants, and the finding A5 reported rests on four hand-picked examples ([NOTE-tmpruw1i](../notes.d/NOTE-tmpruw1i.md)).

## Key takeaways

- Translation items and inference items are different utterances (1 of 204 overlaps), so no item-level dissociation can be read from it ([NOTE-tmpruw1i](../notes.d/NOTE-tmpruw1i.md)).
- Every gold label and every human rating comes from one native speaker per language; cells hold 5–16 items.
- Models' errors lean to the literal reading; MCQ beats NLI in 20 of 20 model–language pairs.
