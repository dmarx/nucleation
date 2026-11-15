---
status: Proposed
promote_when: >-
  A run that states the null-space criterion used (exact, or the
  numerical rank threshold) shows the two things the title asserts. (a)
  On edited layers of an LLM, the common null space of two or more
  domains' preservation-key matrices is markedly smaller than the
  smaller individual one, with a positive Conflict Index for the paper's
  domain pairs. (b) Under null-space-projected sequential editing, the
  pairs or orders with higher conflict show more forgetting of earlier
  domains than those with lower conflict. Either the authors' released
  code or an independent reimplementation will do. It does not need
  MuEdit's recipe to be the best editor, which the title does not assert.
title: 'On Liang and colleagues, an edit to an LLM''s MLP projection that must leave several domains'' preserved key representations unchanged is confined to the intersection of their null spaces, which can be much smaller than any one domain''s, and this inter-domain null-space misalignment, measured as the share of the smaller null space lost in the intersection, is what makes null-space-projected editing collapse when applied sequentially across heterogeneous domains'
version: 1
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpy7s15
summary: >-
  Liang, Lin, Huang, Wu, Li, Wang & Yan (2026), [LIT-tmpy7s15](../literature.d/LIT-tmpy7s15.md), read in
  [NOTE-tmps6dyd](../notes.d/NOTE-tmps6dyd.md). The intersection bound is elementary linear algebra and
  holds; the claim that misalignment explains the collapse rests on
  results from one editor family, five to seven domains and three
  backbones, with conflict used as a surrogate for forgetting. The sharp
  edges: the Conflict Index is degenerate as defined at the paper's own
  sizes unless null spaces are thresholded, and the threshold is not
  given; and in the seven-task test, ordering by conflict does no better
  than the average random order, which weakens the link from measured
  conflict to forgetting.
---

# THEORY-tmpa60dn: On Liang and colleagues, an edit to an LLM's MLP projection that must leave several domains' preserved key representations unchanged is confined to the intersection of their null spaces, which can be much smaller than any one domain's, and this inter-domain null-space misalignment, measured as the share of the smaller null space lost in the intersection, is what makes null-space-projected editing collapse when applied sequentially across heterogeneous domains

## Source

Liang et al. (2026), [LIT-tmpy7s15](../literature.d/LIT-tmpy7s15.md), read in [NOTE-tmps6dyd](../notes.d/NOTE-tmps6dyd.md) from arXiv v1.

## What was actually shown

- **Lemma 1**: the common null space is the intersection, no larger than
  the smaller individual null space. This is true by linear algebra.
- **Order matters for AlphaEdit's final scores** across five domains on
  Llama3-8B. ZsRE specificity is 0.3009 under the default order and
  0.5506 under the best order by summed conflict.
- **MuEdit beats AlphaEdit and other editors after sequential editing**
  across domains. It does so on three backbones and with as few as 50
  reference examples.

Each of these could have come out otherwise: ordering by conflict might
not have changed AlphaEdit's scores, and relaxing preservation
constraints might have cost more in earlier domains than it gained.

## What this does not say

- **That conflict, as measured, predicts forgetting.** The paper uses
  adjacent conflict "as a tractable surrogate for editing interference,
  rather than an exact measure of cumulative forgetting". In the
  seven-task test, greedy ordering is within the 95% interval of the
  mean random order on every task.
- **What the index measures numerically.** It depends on a null-space
  criterion the text does not state.
- **Anything about where knowledge is stored.** The preservation
  argument is about a linear map's outputs on reference keys, whatever
  the layer stores.
