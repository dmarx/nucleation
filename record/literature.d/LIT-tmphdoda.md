---
status: Active
status_note: >-
  read in full 2026-10-29 (NOTE-tmpmkero) from the LREC-COLING 2024 PDF;
  worth reading as the first collection of human pragmatic-similarity
  ratings and for its account of what lowers agreement. The 0.45 the
  record cites is one session's single-judge figure; the others are 0.72
  and 0.66.
title: 'A Collection of Pragmatic-Similarity Judgments over Spoken Dialog Utterances'
version: 2
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Filed, not read, from A5 of the exchange "Paper assessment"
    (2026-10-28 to 29). `published:` is arXiv v1 2024-03-21 (LREC-COLING
    2024, pp. 154–163) (ADR-002). A5 called it "PragSim", which is the
    name of its data repository, not of the paper.
- version: 2
  date: '2026-10-29'
  note: >-
    Read in full from the LREC-COLING 2024 PDF (ACL Anthology
    2024.lrec-main.14); the arXiv v1 text is the same. Correction: the
    summary's nine judges, 220 pairs and 0.45 describe Session 1 only;
    the collection is 693 pairs in three sessions (two English, one
    Spanish) with 6–9 judges, 5,532 ratings, and agreement 0.45, 0.72
    and 0.66. Tagged anthology-candidate for its train-and-evaluate
    advice to modelers (ADR-005). The summary is rewritten from the
    text. Status Deferred to Active.
tags:
- pragmatics
- psychometrics
- anthology-candidate
date: '2026-10-29'
published: '2024-03-21'
arxiv: '2403.14808'
first_author: 'Ward'
keywords:
- 'pragmatic similarity'
- 'spoken dialog'
- 'human judgments'
- 'prosody'
implementations: []
summary: >-
  Ward & Marco (2024). The first collection of human pragmatic-similarity
  ratings: 693 pairs of a spoken dialog utterance and a re-enactment of
  it, made under six conditions so that similarity varies, rated on a 1–5
  slider for "overall feeling, tone, and intent" by 6–9 judges in three
  sessions, two English and one Spanish, 5,532 ratings in all. Mean
  pairwise Pearson agreement between judges was 0.45, 0.72 and 0.66 by
  session, rising with experience and falling for lexically different
  pairs (0.80 in Session 2 without them). Judges discussed ratings during
  the sessions, and all pairs are within one language.
---

# LIT-tmphdoda: A Collection of Pragmatic-Similarity Judgments over Spoken Dialog Utterances

Ward, N. G., & Marco, D. (2024). A collection of pragmatic-similarity judgments over spoken dialog utterances. *Proceedings of LREC-COLING 2024*, 154–163.

Read in full in NOTE-tmpmkero.

## Why this is here

A5's warning for [CASE-055](../cases.d/CASE-055.md)'s Stage 0, kept in [CASE-tmph0fxi](../cases.d/CASE-tmph0fxi.md): if judges agree on pragmatic similarity at 0.45, a model can look weak because the target is unstable, or strong because it reproduces one panel's habits.

Correction from the reading: 0.45 is the first of three sessions and a single-judge figure (the others are 0.72 and 0.66), and a nine-judge mean at 0.45 is far more reliable. The warning holds in another form: the agreement for pairs that differ in words, as translations do, is lower and unreported (NOTE-tmpmkero).

## Key takeaways

- 0.45 is Session 1 and one judge against another; a nine-judge mean at that level has an estimated reliability near 0.88 (NOTE-tmpmkero).
- Agreement is lowest for lexically different pairs, the kind every translation is, and the paper does not report it separately.
- Within-language only; no test–retest.
