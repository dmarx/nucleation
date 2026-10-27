---
status: Active
status_note: >-
  read 2026-10-27 (NOTE-tmpoa8l3) in full, from the Alignment Forum's
  own API; worth reading as the worked case of causal scrubbing on a model
  whose algorithm is known, with the full table of hypotheses, their
  losses and standard errors, and for the authors' own finding that two
  more specific hypotheses scored higher for reasons they judge
  illegitimate (THEORY-tmpnu6ih). Read it knowing that the model and the
  prior dissection are unpublished, that every number is one run of 2,000
  scrubbed samples, and that its prose states the horizon test backwards
  in two places.
title: 'Causal scrubbing: results on a paren balance checker'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("get started on
    the seven works and markov IBP"): one of causal scrubbing's three
    companion posts, which the readings of 2026-10-26 named without
    registering, since the record held their results only through the
    main post's summaries (LIT-1549, NOTE-1168). Checked on 2026-10-27
    against the Alignment Forum's record (post kjudfaQazMmC74SbF, in the
    sequence "[Redwood Research] Causal Scrubbing", h95ayYYwMebGEYN5y):
    "Causal scrubbing: results on a paren balance checker", posted
    2022-12-03 (00:59 UTC) by Lawrence Chan with co-authors Adrià
    Garriga-Alonso, Nicholas Goldowsky-Dill, Ryan Greenblatt, Tao Lin,
    Jenny Nitishinskaya, Ansh Radhakrishnan, Buck Shlegeris and Nate
    Thomas (authors sorted alphabetically). Tao Lin is not an author of
    the main post. No arXiv or DOI version exists; the post is the
    publication, so `published:` is 2022-12-03 and the source is its URL
    (ADR-002). Registered as its own work rather than folded into LIT-1549:
    it is a separate post with its own address and author list, and the
    record files one LIT per work, so it `extends` the main post. The
    summary follows the post's introduction.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmpoa8l3): the whole post, its appendix sections and
    all eleven footnotes, figures from captions and text only. Status
    Deferred → Active. THEORY-tmpnu6ih filed (Active). The summary is
    checked against the reading and given the table's figures.
tags:
- representation-learning
- causality
- anthology-candidate
date: '2026-10-27'
published: '2022-12-03'
url: 'https://www.alignmentforum.org/posts/kjudfaQazMmC74SbF/causal-scrubbing-results-on-a-paren-balance-checker'
first_author: 'Chan'
keywords:
- 'causal scrubbing'
- 'balanced parentheses'
- 'algorithmic task'
- 'mechanistic interpretability'
- 'hypothesis testing'
extends:
- LIT-1549
implementations: []
summary: >-
  Chan, Garriga-Alonso, Goldowsky-Dill, Greenblatt, Lin et al. (2022),
  Alignment Forum (Redwood Research). Causal scrubbing applied to a
  three-layer, two-head bidirectional transformer that classifies
  parenthesis strings as balanced. The high-level hypothesis (two heads
  carry an equal-count-and-starts-open test, one head the horizon test)
  recovers 88–93% of the loss; making it specific about how the heads
  compute their tests brings it to 72%. Two still more specific
  hypotheses score higher than the one they refine, which the authors
  judge illegitimate.
---
<!-- inactive-ok-file: THEORY-802 CLAIM-454 — Proposed; the account and claim this work bears on, cited as open -->

# LIT-tmpnbrst: Causal scrubbing: results on a paren balance checker

Chan, L., Garriga-Alonso, A., Goldowsky-Dill, N., Greenblatt, R., Lin, T.,
Nitishinskaya, J., Radhakrishnan, A., Shlegeris, B. & Thomas, N. (2022).
Causal scrubbing: results on a paren balance checker. *AI Alignment
Forum*, 3 December 2022.

Read in full on 2026-10-27 (NOTE-tmpoa8l3). One account was drawn
from it: THEORY-tmpnu6ih.

## Why this is here

The owner asked on 2026-10-27 to "get started on the seven works and
markov IBP" that the circuits readings of 2026-10-26 had named without
registering. The causal-scrubbing reading (LIT-1549, NOTE-1168) held
this post's results only as the main post's four-row summary. This is
where the method meets a model whose algorithm is known, with standard
errors, and where the authors find their own score rewarding a
hypothesis for the wrong reason. It bears on THEORY-978 (the
count-test result is the authors' own case of a correlated feature
passing), on THEORY-802 and on CLAIM-454.
