---
status: Deferred
status_note: >-
  filed 2026-10-25, not read. Registered from the owner's exchange of
  2026-10-24/25 (the continuation of "Review PR 327 Improvements"), shared
  at https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824, where
  "classical consensus and DeGroot models" are cited at turn U36 without a
  title. No NOTE is filed.
title: 'Reaching a Consensus'
version: 1
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

Not read. The summary is drawn from the abstract or from what the work
is standardly cited for. A reading should check it first.

## Why this is here

Cited at U36 for the left eigenvector of the influence matrix as the
weight each member's opinion carries in the consensus, which is the
readout ℓ·x on which [CASE-tmpvmjgd](../cases.d/CASE-tmpvmjgd.md) turns the population's collective
coordinate into an Ornstein–Uhlenbeck process. The record reads the model
through later work: Golub and Jackson's naïve learning ([LIT-999](LIT-999.md),
[THEORY-321](../theory.d/THEORY-321.md)), the DeGroot–Friedkin model of Jia et al. ([LIT-1146](LIT-1146.md)) and
Friedkin, Jia and Bullo ([LIT-1482](LIT-1482.md)). The paper they all start from was
not held.
