---
status: Active
status_note: >-
  read 2026-10-25 (NOTE-tmp5sbzm) in full, from the copy the owner
  supplied on 2026-10-25, a JSTOR scan of the published article (the
  searches of the same day had found no lawful copy). Worth reading
  as the source of the DeGroot model: repeated averaging with fixed
  weights is a Markov chain on opinions, a consensus from every start is
  reached exactly when the chain has one closed class and it is
  aperiodic, and its weights are the stationary vector, zero for members
  outside that class (THEORY-tmpvqkp6). Read it knowing that the
  theorems are cited from Markov-chain texts without proof, that the
  "if and only if" of §4 needs the quantifier "for every starting
  opinion", that its Theorems 1 and 2 are the same condition, and that
  the weights are fixed and nothing tracks the truth.
title: 'Reaching a Consensus'
version: 3
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed, not read. Registered unread from the owner's exchange of
    2026-10-24/25 (the continuation of "Review PR 327 Improvements"),
    shared at
    https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824. At
    turn U36 the reply says the left eigenvector ℓ is "an emergent summary
    of who is listened to, much as in classical consensus and DeGroot
    models", by search reference only and with no title; this is the paper
    the DeGroot model is named for. Citation checked against Crossref on
    2026-10-25: Morris H. DeGroot, Journal of the American Statistical
    Association 69(345), 118–121, issue March 1974 with no day, so
    `published:` is 1974-03-01, meaning March 1974 (ADR-002). OpenAlex
    lists it closed. The summary follows the abstract on OpenAlex.
- version: 2
  date: '2026-10-25'
  note: >-
    Status Deferred → Unavailable under ADR-041: a search for a lawful full
    text on 2026-10-25 (Unpaywall, OpenAlex, Semantic Scholar, Taylor &
    Francis, JSTOR, web searches for author or institutional copies)
    reached none. No NOTE is filed.
- version: 3
  date: '2026-10-25'
  note: >-
    The owner supplied a copy on 2026-10-25, a JSTOR scan of the
    published article (JASA 69(345): 118–121, with a JSTOR cover sheet),
    which under ADR-041 returns the work to reading. Read in full the
    same day (NOTE-tmp5sbzm), and THEORY-tmpvqkp6 filed Active from it.
    Status Unavailable → Active. The summary was checked against the
    reading and kept: it is the paper's abstract, and it is accurate. No
    open URL is added, because the copy is the owner's and JSTOR's.
tags:
- network-science
- social-science
- probabilistic-modeling
date: '2026-10-25'
published: '1974-03-01'
doi: '10.1080/01621459.1974.10480137'
first_author: 'DeGroot'
keywords:
- 'consensus'
- 'opinion pooling'
- 'subjective probability'
- 'group decision'
- 'DeGroot model'
implementations: []
summary: >-
  DeGroot (1974). Members of a group that must act together each hold a
  subjective probability distribution for an unknown parameter. A model
  describes how they might reach agreement on a common distribution by
  repeatedly pooling one another's opinions; the process and the consensus
  it reaches are given explicitly. The model also applies when each
  opinion is a point estimate rather than a distribution (abstract).
---
# LIT-tmpwlnuv: Reaching a Consensus

DeGroot, M. H. (1974). Reaching a consensus. *Journal of the American
Statistical Association* 69(345): 118–121.
doi:10.1080/01621459.1974.10480137.

Read in full on 2026-10-25 from the copy the owner supplied
(NOTE-tmp5sbzm). Each member fixes, once, the weights it gives everyone's
opinions, and the group iterates F ← PF. Theorems 1 and 2 say when that
converges to a common opinion, and Theorem 3 says the common opinion is
the opinion pool weighted by P's stationary vector. The paper also states
that two closed classes, or one periodic class, give no consensus.
THEORY-tmpvqkp6 re-derives all of it. The model is offered as a
formalization of the Delphi technique.

## Why this is here

Cited at U36 for the left eigenvector of the influence matrix as the
weight each member's opinion carries in the consensus, which is the
readout ℓ·x on which [CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md) turns the population's collective
coordinate into an Ornstein–Uhlenbeck process. The record reads the model
through later work: Golub and Jackson's naïve learning ([LIT-999](LIT-999.md),
[THEORY-321](../theory.d/THEORY-321.md)), the DeGroot–Friedkin model of Jia et al. ([LIT-1146](LIT-1146.md)) and
Friedkin, Jia and Bullo ([LIT-1482](LIT-1482.md)). The paper they all start from was
not held until the owner supplied it on 2026-10-25.
