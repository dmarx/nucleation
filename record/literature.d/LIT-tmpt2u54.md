---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmpymmuh](../notes.d/NOTE-tmpymmuh.md)) in full, from the Alignment Forum's own
  API; worth reading for the details the main post defers: the
  definition of the metric, the full case against zero and mean
  ablation, how unimportant inputs are grouped, a proof that the
  scrubbed inputs are the maximum-entropy distribution consistent with
  the hypothesis ([THEORY-tmpgikxe](../theory.d/THEORY-tmpgikxe.md)), how superposition is handled, and a
  second constructed false hypothesis that scores above the model. Read
  it knowing that its Lemma 1 says "product distribution" where its
  proof shows the joint, and that it says both results posts use a
  randomized-loss baseline when the induction post does not.
title: 'Causal scrubbing: Appendix'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("get started on
    the seven works and markov IBP"): one of causal scrubbing's three
    companion posts, named by the readings of 2026-10-26 and held only
    through the main post's references to it (LIT-1549, NOTE-1168).
    Checked on 2026-10-27 against the Alignment Forum's record (post
    kcZZAsEjwrbczxN2i, in the sequence "[Redwood Research] Causal
    Scrubbing"): "Causal scrubbing: Appendix", posted 2022-12-03 (00:58
    UTC) by Lawrence Chan with co-authors Adrià Garriga-Alonso, Nicholas
    Goldowsky-Dill, Ryan Greenblatt, Jenny Nitishinskaya, Ansh
    Radhakrishnan, Buck Shlegeris and Nate Thomas (authors sorted
    alphabetically), the main post's author list. No arXiv or DOI version
    exists; the post is the publication, so `published:` is 2022-12-03
    and the source is its URL (ADR-002). The title is the post's own,
    capitalized as the Forum gives it. Registered as its own work, not
    folded into LIT-1549: it is a separate post at its own address, and
    the record files one LIT per work (LIT-tmpnbrst's first history
    item). It `extends` the main post. The summary follows the post's
    section headings.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmpymmuh): §§1–8 and all four footnotes, figures
    from captions and text only. Status Deferred → Active.
    THEORY-tmpgikxe filed (Active). The summary is checked against the
    reading.
tags:
- causality
- representation-learning
- anthology-candidate
date: '2026-10-27'
published: '2022-12-03'
url: 'https://www.alignmentforum.org/posts/kcZZAsEjwrbczxN2i/causal-scrubbing-appendix'
first_author: 'Chan'
keywords:
- 'causal scrubbing'
- 'resampling ablation'
- 'maximum entropy'
- 'polysemanticity'
- 'adversarial validation'
extends:
- LIT-1549
implementations: []
summary: >-
  Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt et al. (2022),
  Alignment Forum (Redwood Research). The technical appendix to causal
  scrubbing. It defines "% loss recovered" against a label-shuffled
  baseline and argues against zero and mean ablation with three
  examples. It proves that the inputs the algorithm samples are the
  maximum-entropy distribution preserving the joint inputs of every
  interpretation node, shows how a superposed toy model is explained as
  monosemantic terms plus an unexplained interference term, and builds a
  false hypothesis that scores far above the model. It proposes, without
  solving, adversarial validation.
---
<!-- inactive-ok-file: THEORY-802 CLAIM-454 — Proposed; the account and claim this work bears on, cited as open -->

# LIT-tmpt2u54: Causal scrubbing: Appendix

Chan, L., Garriga-Alonso, A., Goldowsky-Dill, N., Greenblatt, R.,
Nitishinskaya, J., Radhakrishnan, A., Shlegeris, B. & Thomas, N. (2022).
Causal scrubbing: Appendix. *AI Alignment Forum*, 3 December 2022.

Read in full on 2026-10-27 ([NOTE-tmpymmuh](../notes.d/NOTE-tmpymmuh.md)). One account was drawn from
it: [THEORY-tmpgikxe](../theory.d/THEORY-tmpgikxe.md).

## Why this is here

The owner asked on 2026-10-27 to "get started on the seven works and
markov IBP" that the circuits readings of 2026-10-26 had named without
registering. The causal-scrubbing reading ([NOTE-1168](../notes.d/NOTE-1168.md)) took its case for
resampling ablation, the field's standing convention ([LIT-1547](LIT-1547.md),
[LIT-1531](LIT-1531.md)), from the main post's summary, "details deferred to the
appendix post". This is that appendix. Its maximum-entropy result says
precisely what a scrubbed run assumes about everything a hypothesis
leaves unsaid, which bears on [THEORY-978](../theory.d/THEORY-978.md) and on what a passing hypothesis
certifies ([CLAIM-454](../claims.d/CLAIM-454.md)).
