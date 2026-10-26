---
status: Active
title: 'On ten corpora simulated from three-level hierarchical LDA itself (100 documents of 250 words, a vocabulary of 100, sparse topics with η = 0.005, γ = 1), the highest-probability state of the collapsed Gibbs sampler recovered the generating tree exactly in eight; in one of the other two a wrong tree had higher posterior probability than the true one'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpcuo7o, under ADR-047 v3: the title claims no
    more than §6.1 measured, the reading was in full, and nothing in the
    record contradicts it. The paper's own caveat on identifiability is
    kept in the body.
tags:
- probabilistic-modeling
- mathematical-statistics
date: '2026-10-26'
source:
- LIT-tmpk69gp
summary: >-
  Blei, Griffiths and Jordan (2010), LIT-tmpk69gp, §6.1 and Fig. 6, read in
  NOTE-tmpcuo7o. It shows that the sampler can invert hLDA on data hLDA
  generated, with sparse, well-separated topics. It does not show that the
  tree is identified in general, or that a tree found in real data was
  there to be found. One failure is a posterior that prefers the wrong
  tree, which no better sampler would fix.
---
<!-- inactive-ok-file: CASE-tmplcm41 CLAIM-135 — Proposed; the case and claim this result is set against, open -->

# THEORY-tmpvs18m: On ten corpora simulated from three-level hierarchical LDA itself (100 documents of 250 words, a vocabulary of 100, sparse topics with η = 0.005, γ = 1), the highest-probability state of the collapsed Gibbs sampler recovered the generating tree exactly in eight; in one of the other two a wrong tree had higher posterior probability than the true one

## Source

Blei, Griffiths and Jordan (2010), LIT-tmpk69gp, §6.1 and Fig. 6, read in
full in NOTE-tmpcuo7o from arXiv 0710.0845v3.

## What was actually shown

Ten data sets were drawn from hLDA, each with 100 documents of 250 words,
a vocabulary of 100, η = 0.005 and γ = 1, with the levels truncated at
three and a Dirichlet over the three level proportions. For each, the
posterior mode over trees and allocations was approximated by the
highest-probability state of the collapsed Gibbs sampler (§5.5). In the
paper's words: "We exactly recover the correct hierarchies, with only two
errors. In one case, the error is a single wrongly allocated path. In the
other case, the inferred mode has higher posterior probability than the
true tree structure (due to finite data)."

What could have come out otherwise: the sampler could have stuck in local
modes, merged or split branches, or misallocated documents widely. In
eight of ten it did none of these.

The second failure is of a different kind from the first. A sampler that
finds a state of higher posterior probability than the truth has done its
job. The posterior itself prefers the wrong tree, so with 100 documents
the tree is not identified by the posterior mode in that case.

The authors give the condition in words: "In general we cannot expect to
always find the exact tree. This is dependent on the size of the data set,
and how identifiable the topics are. Our choice of small η yields topics
that are relatively sparse and (probably) very different from each other.
Trees will not be as easy to identify in data sets which exhibit polysemy
and similarity between topics."

## What this does not say

- **Not that hLDA's trees are identified in general.** The test used
  sparse, well-separated topics chosen to make recovery easy, and three
  levels. No condition is stated under which the tree is unique.
- **Not that a tree found in real data is real.** Data generated under the
  model's own prior test the inference, not whether the structure exists
  in data the model did not generate.
- **Not about deep trees, other hyperparameters, or larger corpora.** One
  setting was run, ten times.
- **Not a rate.** Two errors in ten is a count, not an error rate with an
  interval.

## Connections

- **QUESTION-tmpixgs8.** Its list of what would not answer it includes
  "Recovering the prior's structure from data generated under that prior,
  which tests the inference, not the structure". This is that test, carried
  out well. The question needs a world that did not assume the prior,
  which is T23's "Option A" (CASE-tmplcm41).
- **CLAIM-203.** Its note of 2026-10-26 draws the same lesson for
  latent-structure recovery.
- **CLAIM-135.** This is evidence for the first achievement on simulated
  data, and for the second only within the model and at this size. The
  case where the posterior prefers a wrong tree shows the second can fail
  while the sampler succeeds.
