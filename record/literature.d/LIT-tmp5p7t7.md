---
status: Active
status_note: >-
  Read on 2026-11-12 ([NOTE-tmp56sxk](../notes.d/NOTE-tmp56sxk.md)) from
  https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11269175/fullTextXML.
title: 'AI models collapse when trained on recursively generated data'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Filed, not read. Identifier checked on 2026-11-12 with Crossref, and confirmed not held by DOI or arXiv id, exact title and first author in record/literature.d. `published:`: Crossref's online date. No email address was sent to any service.
- version: 2
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 (NOTE-tmp56sxk; THEORY-tmp5ac00). Nature 631(8022):755.
    The same work circulated as arXiv 2305.17493 from 2023-05-27 under another
    title; `published:` stays at the Nature date, the versions differing in
    title and content. The record analogues in its registration summary (loss
    of source diversity, derivative claims cited as independent evidence,
    narrowing categories) are A's (A43), not the paper's.
tags:
- learning-theory
- anthology-candidate
date: '2026-11-12'
published: '2024-07-24'
doi: '10.1038/s41586-024-07566-y'
first_author: 'Shumailov'
keywords: []
implementations: []
summary: >-
  Shumailov et al. (2024), AI models collapse when trained on recursively
  generated data. The authors define "model collapse": successive
  generations of generative models are trained on data produced by their
  predecessors, and they lose information about the true distribution.
  Low-probability tails vanish first ("early"). Later the distribution
  converges toward a low-variance point ("late"). They name three
  compounding error sources: - statistical approximation (finite samples) -
  functional expressivity - functional approximation Two simple models are
  proved to collapse when each generation uses only the previous
  generation's samples (βi = γi = 0): - a discrete distribution, which forms
  an absorbing Markov chain - a recursively fitted Gaussian (Theorem 3.1),
  where the Wasserstein distance goes to infinity and the variance goes to 0
  almost surely The language-model experiment fine-tunes OPT-125m on
  wikitext2, then trains successive generations on predecessors' outputs.
  Read for the exchange "luria experiment design".
---
<!-- inactive-ok-file: THEORY-tmp5ac00 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# LIT-tmp5p7t7: AI models collapse when trained on recursively generated data

Ilia Shumailov et al. (2024), Nature. DOI 10.1038/s41586-024-07566-y.

## Key takeaways

*Seeded from the exchange; read on 2026-11-12, below.* A cites it for compounding errors when generations train on predecessors' outputs; A treats it as a caution, testable in a record as loss of source diversity, derivative claims cited as independent evidence, and narrowing categories, and says it does not show a record will collapse.

## Standing in the record

Registered on 2026-11-12 from the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda), at A43 (§11). It bears on [QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md); [LIT-971](LIT-971.md) is held.

## Reading of 2026-11-12

Read in [NOTE-tmp56sxk](../notes.d/NOTE-tmp56sxk.md), from https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11269175/fullTextXML; its account is [THEORY-tmp5ac00](../theory.d/THEORY-tmp5ac00.md).
