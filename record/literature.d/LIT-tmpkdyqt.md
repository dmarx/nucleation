---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmpt6p3g](../notes.d/NOTE-tmpt6p3g.md)) in full, from the Alignment Forum's own
  API; worth reading as the quantified test of the textbook induction
  circuit in a two-layer attention-only model, pathway by pathway, and
  for what the refinements found: three-token matching, layer-0 heads that
  attend to copies of the current token, and a previous-token head that
  deviates on quotes, articles and punctuation ([THEORY-tmp3gl09](../theory.d/THEORY-tmp3gl09.md)). Read it
  knowing that its percentages are of the 0.053 nats the induction heads
  contribute on a filtered token subset, not of a label-shuffled loss
  like the paren post's, that its headline 89% is the bonus hypothesis
  and the main post's 86% the fourth, and that the model is not
  published.
title: 'Causal scrubbing: results on induction heads'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("get started on
    the seven works and markov IBP"): one of causal scrubbing's three
    companion posts, named by the readings of 2026-10-26 and held only
    through the main post's summary (LIT-1549, NOTE-1168). Checked on
    2026-10-27 against the Alignment Forum's record (post
    j6s9H9SHrEhEfuJnq, in the sequence "[Redwood Research] Causal
    Scrubbing"): "Causal scrubbing: results on induction heads", posted
    2022-12-03 (00:59 UTC) by Lawrence Chan with co-authors Adrià
    Garriga-Alonso, Nicholas Goldowsky-Dill, Ryan Greenblatt, Tao Lin,
    Jenny Nitishinskaya, Ansh Radhakrishnan, Buck Shlegeris and Nate
    Thomas (authors sorted alphabetically). No arXiv or DOI version
    exists; the post is the publication, so `published:` is 2022-12-03
    and the source is its URL (ADR-002). Registered as its own work, not
    folded into LIT-1549, for the reasons given in LIT-tmpnbrst's first
    history item; it `extends` the main post. The summary follows the
    post's introduction.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmpt6p3g): the whole post, its appendices and its
    three footnotes, figures from captions and text only; the
    interactive attention viewers it links were not opened. Status
    Deferred → Active. THEORY-tmp3gl09 filed (Active). The summary is
    checked against the reading and given the hypotheses' figures.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-27'
published: '2022-12-03'
url: 'https://www.alignmentforum.org/posts/j6s9H9SHrEhEfuJnq/causal-scrubbing-results-on-induction-heads'
first_author: 'Chan'
keywords:
- 'causal scrubbing'
- 'induction heads'
- 'previous-token head'
- 'attention-only transformer'
- 'mechanistic interpretability'
extends:
- LIT-1549
implementations: []
summary: >-
  Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Lin et al. (2022),
  Alignment Forum (Redwood Research). In a two-layer attention-only
  language model with two induction heads, the standard induction story
  (queries and values from the token embedding, keys from the
  previous-token head) recovers 35% of the loss the induction heads
  contribute on tokens where induction helps. Letting the heads match the
  last three tokens, read layer 0's average effect, and treat three
  layer-0 heads that attend to copies of the current token as attending
  to itself raises it to 86%, and to 89% with a crude model of where the
  previous-token head deviates.
---
<!-- inactive-ok-file: THEORY-990 — Proposed; the wider induction thesis this bears on, cited as open -->

# LIT-tmpkdyqt: Causal scrubbing: results on induction heads

Chan, L., Garriga-Alonso, A., Goldowsky-Dill, N., Greenblatt, R., Lin, T.,
Nitishinskaya, J., Radhakrishnan, A., Shlegeris, B. & Thomas, N. (2022).
Causal scrubbing: results on induction heads. *AI Alignment Forum*,
3 December 2022.

Read in full on 2026-10-27 ([NOTE-tmpt6p3g](../notes.d/NOTE-tmpt6p3g.md)). One account was drawn from
it: [THEORY-tmp3gl09](../theory.d/THEORY-tmp3gl09.md).

## Why this is here

The owner asked on 2026-10-27 to "get started on the seven works and
markov IBP" that the circuits readings of 2026-10-26 had named without
registering. The record's induction line holds the circuit's discovery
([LIT-1534](LIT-1534.md), [LIT-1538](LIT-1538.md)) and its causal case in small attention-only models
([THEORY-973](../theory.d/THEORY-973.md)), and the causal-scrubbing reading ([NOTE-1168](../notes.d/NOTE-1168.md)) said that the
model, filter and details of the 35% and 86% figures were in this post,
unread. This is the only quantified test in the record of how much of
the induction heads' contribution the textbook circuit accounts for, and
it finds the circuit to be the core of a wider computation, not the
whole of it.
