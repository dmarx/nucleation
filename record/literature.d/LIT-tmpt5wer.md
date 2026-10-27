---
status: Active
status_note: >-
  read 2026-10-26 ([NOTE-tmphwzim](../notes.d/NOTE-tmphwzim.md)) in full, from the typeset JMLR copy;
  worth reading for the mixed membership stochastic blockmodel, in which a
  node takes one block per interaction drawn from its own membership
  vector, for the variational EM that fits it, and as the relational
  baseline a model of members' perspectives must beat. Read it knowing
  that its §5 claim that the blockmodel and the memberships do not compete
  is asserted and fails for the likelihood given memberships, that its
  sparsity parameter is confounded with the blockmodel's scale and its
  printed estimator is the fraction of zeros ([THEORY-tmplo0xb](../theory.d/THEORY-tmplo0xb.md)), that K is
  chosen by criterion, that it cannot generate hubs, and that its protein-function check is against a weak baseline ([THEORY-tmpuvkbn](../theory.d/THEORY-tmpuvkbn.md), Proposed).
title: 'Mixed Membership Stochastic Blockmodels'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T21 the reply says "mixed-membership stochastic
    blockmodels similarly permit people to participate in different latent
    interaction roles rather than belong exclusively to one community",
    linking "jmlr.org" with no author or title. Checked on 2026-10-26
    against the JMLR abstract page and the arXiv record: Edoardo M. Airoldi,
    David M. Blei, Stephen E. Fienberg and Eric P. Xing, JMLR 9(65):
    1981–2014 (2008); arXiv 0705.4485, v1 submitted 30 May 2007, which is
    `published:` (ADR-002). JMLR gives no DOI. The summary follows the JMLR
    abstract.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full at the owner's request (NOTE-tmphwzim), from the
    typeset JMLR PDF
    (https://jmlr.org/papers/volume9/airoldi08a/airoldi08a.pdf); the
    arXiv copy was fetched and not compared. Status Deferred → Active.
    Two THEORYs filed: THEORY-tmplo0xb Active, THEORY-tmpuvkbn Proposed.
    The summary is checked against the reading and kept, without its
    "(abstract)" marker.
tags:
- network-science
- probabilistic-modeling
date: '2026-10-26'
published: '2007-05-30'
arxiv: '0705.4485'
url: 'https://jmlr.org/papers/v9/airoldi08a.html'
first_author: 'Airoldi'
keywords:
- 'mixed membership'
- 'stochastic blockmodel'
- 'relational data'
- 'variational inference'
- 'social networks'
implementations: []
summary: >-
  Airoldi, Blei, Fienberg & Xing (2008), JMLR 9: 1981–2014. For pairwise
  measurements such as links between objects, where the usual
  exchangeability assumptions fail, mixed membership stochastic blockmodels
  combine global parameters for dense patches of connectivity (the
  blockmodel) with node-specific mixed memberships. A variational algorithm
  gives fast approximate inference, applied to social and
  protein-interaction networks.
---
<!-- inactive-ok-file: THEORY-tmpuvkbn — Proposed; filed from this reading, cited as open -->

# LIT-tmpt5wer: Mixed Membership Stochastic Blockmodels

Airoldi, E. M., Blei, D. M., Fienberg, S. E. & Xing, E. P. (2008). Mixed
membership stochastic blockmodels. *Journal of Machine Learning Research* 9:
1981–2014. arXiv:0705.4485.

Read in full on 2026-10-26 from the typeset JMLR copy ([NOTE-tmphwzim](../notes.d/NOTE-tmphwzim.md)). The
summary is checked against the reading.

## Why this is here

Cited at T21 for the relational component of the reply's combined model:
members occupying several latent roles in their interactions. The record
held no blockmodel. It bears on [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md), whose last clause asks whether
inferred higher-level structure predicts responses to interventions beyond
what the communication and authority graph already gives; a mixed-membership
blockmodel of that graph is the baseline such inference must beat.
