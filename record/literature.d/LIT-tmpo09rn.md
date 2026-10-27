---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmpxnucs](../notes.d/NOTE-tmpxnucs.md)) in full, from the author's own page;
  worth reading as the origin of attribution patching, for its derivation
  of the estimate and the identities that make it cheap and additive
  ([THEORY-tmpeqz27](../theory.d/THEORY-tmpeqz27.md)), for the account of where a first-order estimate
  should fail ([THEORY-tmp52c5a](../theory.d/THEORY-tmp52c5a.md)), and for its framework of what patching
  can and cannot show: sufficiency against necessity, specific against
  general understanding, and parallel against serial redundancy. Read it
  knowing that the author calls it an incomplete project, that its
  empirical evidence is one task in GPT-2 Small shown only in plots and a
  notebook, and that the systematic test is Kramár et al. ([LIT-1531](LIT-1531.md)).
title: 'Attribution Patching: Activation Patching At Industrial Scale'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("get started on
    the seven works and markov IBP"), one of the seven works the circuits
    readings of 2026-10-26 named and did not register. LIT-1531 (AtP*)
    names it as the method's origin and, in its first history item, says it
    "is not registered separately"; that is now changed at the owner's
    request. Checked on 2026-10-27 against the post's own page: by Neel
    Nanda, https://www.neelnanda.io/mechanistic-interpretability/attribution-patching,
    dated "Feb 4" on the page and 2023-02-04T22:37:34Z in its
    datePublished metadata (dateModified 2023-03-16), which gives
    `published:` (ADR-002). The post describes work done at Anthropic in
    February–March 2022, which AtP* cites as "Nanda, 2022". It has no arXiv
    record or DOI, so the URL is the source. A cross-post elsewhere was not
    searched for. The summary follows the post's own TLDR.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmpxnucs) from the post's page, fetched 2026-10-27,
    its text extracted from the HTML (about 100,000 characters with page
    furniture); the plots are images and were not seen, and the
    accompanying notebook was not opened. Status Deferred → Active. Two
    accounts filed: THEORY-tmpeqz27 (Active, re-derived and checked
    numerically) and THEORY-tmp52c5a (Proposed). The summary is checked
    against the reading and kept, with the cost made explicit.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-27'
published: '2023-02-04'
url: 'https://www.neelnanda.io/mechanistic-interpretability/attribution-patching'
first_author: 'Nanda'
keywords:
- 'attribution patching'
- 'activation patching'
- 'causal tracing'
- 'path patching'
- 'attention attribution'
- 'mechanistic interpretability'
implementations:
- 'TransformerLens'
summary: >-
  Nanda (2023), blog post, neelnanda.io. Introduces attribution patching: a
  first-order estimate of every activation-patching effect at once, the
  difference between clean and corrupted activations dotted with the
  metric's gradient on the corrupted run, from two forward passes and one
  backward pass instead of one forward pass per patch. On the IOI task in
  GPT-2 Small it approximates head-level patches well and residual-stream
  and first-MLP patches badly. The author offers it as an exploratory
  heuristic for finding what to patch, not a replacement for patching.
---
<!-- inactive-ok-file: THEORY-tmp52c5a THEORY-1000 — Proposed; the post's account of where the estimate fails, filed from this reading, and AtP*'s wider claim, cited as open -->

# LIT-tmpo09rn: Attribution Patching: Activation Patching At Industrial Scale

Nanda, N. (2023). Attribution patching: Activation patching at industrial
scale. Blog post, 4 February 2023,
https://www.neelnanda.io/mechanistic-interpretability/attribution-patching.

Read in full on 2026-10-27 ([NOTE-tmpxnucs](../notes.d/NOTE-tmpxnucs.md)). Two accounts were drawn from
it: [THEORY-tmpeqz27](../theory.d/THEORY-tmpeqz27.md) (Active) and [THEORY-tmp52c5a](../theory.d/THEORY-tmp52c5a.md) (Proposed).

## Why this is here

Registered and read at the owner's request of 2026-10-27, as one of the
works the circuits readings of 2026-10-26 named and did not register. The
record held attribution patching only through Kramár et al.'s test of it
([LIT-1531](LIT-1531.md), [NOTE-1190](../notes.d/NOTE-1190.md)), and through the work built on it: its edge version
with integrated gradients, by which [LIT-1539](LIT-1539.md) and MIB's circuit track
([LIT-1550](LIT-1550.md)) find circuits, and sparse feature circuits ([LIT-1532](LIT-1532.md)), whose
nodes are selected by linear estimates of indirect effect. This is the method's own statement: what is
estimated, why it is cheap, and where its author expected it to fail.
[LIT-1531](LIT-1531.md) was preferred as the record's entry because it tests the method
against ground truth. This post gives the derivation and the reasons for
its failure modes, which [LIT-1531](LIT-1531.md) then measured.
