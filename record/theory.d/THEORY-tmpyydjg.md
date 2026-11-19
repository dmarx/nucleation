---
status: Proposed
title: 'Larremore, Clauset and Jacobs show that a degree-corrected stochastic block model restricted to pure-type groups of a bipartite network finds higher-likelihood partitions faster than the unrestricted model and recovers planted groups that one-mode projections hide, and that on an IMDb actor–movie network its movie blocks track language for most groups and genre for one'
version: 1
source:
- LIT-tmpc7kaa
tags:
- network-science
- probabilistic-modeling
date: '2026-11-19'
promote_when: >-
  The record checks the objective (Eq. 16), the SBM comparison (§III, Fig.
  2) and the synthetic recovery result (Fig. 3B) against the paper, and
  confirms the IMDb block descriptions from the Fig. 8 caption and text
summary: >-
  From the reading of LIT-tmpc7kaa in NOTE-tmp823hg. Larremore, Clauset
  and Jacobs (2014), arXiv 1403.2933. They formulate a degree-corrected
  bipartite stochastic block model, in which communities are pure-type
  groups with the same expected connection pattern to the other side's
  groups. It finds better partitions faster than the unconstrained SBM and
  recovers planted structure that one-mode projections hide. In their
  actor–movie example (IMDb, 1995–2000), five of six movie blocks were
  language groups and one was a genre (Adult), and the authors read the
  blocks as traces of "multiple mechanisms responsible for the existence
  of edges". Here because it is the standard method behind the owner's U10
  genres example, CASE-tmpsjjgx: it supplies the joint people-and-items
  identification, but its own film blocks are mostly not genres, which
  bears on the case's confounds. Read in its NOTE.
---
<!-- inactive-ok-file: CASE-tmpsjjgx — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmpyydjg: Larremore, Clauset and Jacobs show that a degree-corrected stochastic block model restricted to pure-type groups of a bipartite network finds higher-likelihood partitions faster than the unrestricted model and recovers planted groups that one-mode projections hide, and that on an IMDb actor–movie network its movie blocks track language for most groups and genre for one

## The account

In a bipartite network with known vertex types, assign each vertex to one of Ka groups of its own type or Kb of the other. Model edge counts as Poisson with mean θiθjωgigj, with no edges between same-type groups. The maximum-likelihood partition maximizes Σ mrs ln(mrs/κrκs) (Eq. 16). A community is then a set of vertices with the same expected pattern of connections to the other side's groups. The biSBM is the SBM with the bipartite constraints imposed. Because it searches only pure-type partitions, on the malaria data it reached higher likelihoods 3.25 times faster, while the SBM found pure-type partitions in 8 of 2000 runs. On synthetic networks with an ambiguous projection, only the degree-corrected biSBM recovered the planted groups, above λ ≈ 0.33. On 53,158 actors and 39,768 movies from IMDb, five of six movie blocks were language groups and one was the Adult genre.

## What it does not show

- That blocks in engagement or rating data are genres. Its film example uses co-appearance, and the blocks were mostly languages.
- How many groups to use. Model selection is left open.
- Mixed membership, weighted edges or dynamics, including any feedback from using the blocks.
