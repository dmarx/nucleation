---
status: Active
status_note: >-
  read in full 2026-10-15 from the publisher's typeset PDF of the version of record
  (Cognition 178, 67–81), posted by Gershman on his lab's publication page (gershmanlab.com/pubs/Dasgupta18_remembrance.pdf);
  Unpaywall and OpenAlex list it as bronze open access at the publisher, whose site
  refused requests from this environment, and the bioRxiv preprint was not used.
  Worth reading as the empirical case for amortized inference in people, defined
  as reuse of past computation that gains efficiency at a cost in bias: in three
  experiments (N = 84, 80, 100) an unpacking bias in one probability judgment carried
  over into a later related one, only where the queries shared hypotheses, more
  strongly under load at the first query (read as reuse of a summary statistic rather
  than stored samples), and somewhat selectively for similar cues. It measures no
  response times, so the speed gain is assumed, and the filed summary's "biased
  toward earlier answers" should read "carrying over the earlier computation's error",
  since numerical anchoring was ruled out. For [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md) it shows that the
  paper itself frames amortization as a time-for-space trade akin to a look-up table,
  for results kept in the reasoner's memory only, with free retrieval, no break-even
  account, and an error cost that is propagated approximation and interference rather
  than staleness; for [CLAIM-tmpygqjz](../claims.d/CLAIM-tmpygqjz.md) it is consistent but measures neither side
  of the cost; for [CLAIM-tmp7t44x](../claims.d/CLAIM-tmp7t44x.md) its sample-versus-summary contrast is a clean
  instance of keeping more to answer a wider family of queries at a memory cost.
title: 'Remembrance of inferences past: Amortization in human hypothesis generation'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: 'Filed, not read. Citation checked against Crossref on 2026-10-15: Crossref
    gives September 2018, so `published:` is the first of the month. Not held in
    the Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit
    d1573d2) for the authors and the title found nothing. Read the same day (NOTE-tmpoczb2).'
tags:
- cognition
- probabilistic-modeling
date: '2026-10-15'
published: '2018-09-01'
doi: 10.1016/j.cognition.2018.04.017
first_author: Dasgupta
keywords:
- amortized inference
- hypothesis generation
- memory
- Monte Carlo
implementations: []
summary: >-
  Dasgupta, Schulz, Goodman and Gershman (2018), Cognition 178. In three online
  experiments (N = 84, 80 and 100, before exclusions), a sub- or superadditivity
  bias induced in a first probability judgment carried over into a second, always-packed
  judgment about the same scene distribution, and errors on the two queries were
  correlated trial by trial (r ≈ 0.34–0.67). The carry-over appeared only when the
  second query shared part of its hypothesis space with the first, which rules out
  simple numerical anchoring; it was larger when cognitive load fell on the first
  query, which the authors' simulations read as reuse of a summary statistic rather
  than of the stored samples; and with a new cue it appeared (for subadditivity
  only, and weakly) when the cue's posterior was similar to the first. The paper
  defines amortization as reuse of past computation bought at a cost in bias, and
  itself places it in the time-for-space trade. It measures no response times, so
  the speed benefit is assumed, not shown; efficiency is shown only by better secondary-task
  accuracy on reusable trials; and it gives no account of when reuse pays.
---

# LIT-tmpt2ql7: Remembrance of inferences past: Amortization in human hypothesis generation

Dasgupta, I., Schulz, E., Goodman, N. D. and Gershman, S. J. (2018). Remembrance of inferences past: Amortization in human hypothesis generation. *Cognition* 178, 67–81. DOI 10.1016/j.cognition.2018.04.017

## Key takeaways

Read in full ([NOTE-tmpoczb2](../notes.d/NOTE-tmpoczb2.md)). In three online experiments (N = 84, 80 and 100, before exclusions), a sub- or superadditivity bias induced in a first probability judgment carried over into a second, always-packed judgment about the same scene distribution, and errors on the two queries were correlated trial by trial (r ≈ 0.34–0.67). The carry-over appeared only when the second query shared part of its hypothesis space with the first, which rules out simple numerical anchoring; it was larger when cognitive load fell on the first query, which the authors' simulations read as reuse of a summary statistic rather than of the stored samples; and with a new cue it appeared (for subadditivity only, and weakly) when the cue's posterior was similar to the first. The paper defines amortization as reuse of past computation bought at a cost in bias, and itself places it in the time-for-space trade. It measures no response times, so the speed benefit is assumed, not shown; efficiency is shown only by better secondary-task accuracy on reusable trials; and it gives no account of when reuse pays.

## Why this is here

The owner, after the cockpit reading ([LIT-tmpn2s1p](LIT-tmpn2s1p.md)): "amortized retrieval is actually a kind of amortized computation. there's probably a clearer relationship here that I imagine has likely been clarified/formalized at some point in the 30 years since the cockpit essay was published." Registered with six others for [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md).

Amortization made empirical in human inference: stored results of computation reused at a cost in bias. The closest formal reading of the owner's point.
