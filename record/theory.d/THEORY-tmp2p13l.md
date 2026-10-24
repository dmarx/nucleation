---
status: Proposed
promote_when: >-
  A study that tracks gate weights over training in a sparsely-gated
  mixture of experts without balancing losses and shows the concentration
  arising by the stated route, experts that are selected more being trained
  more and so selected still more, for example by showing that it depends
  on early selection and not on differences in initial competence, or that
  it disappears when experts are trained equally while allocation is left
  free; and the ICLR 2017 version read and found to report Table 6 as v1
  does. It is refuted if the concentration proves to track a real
  difference in what the experts can do, or does not recur across seeds.
  Whether the balancing losses produce competent specialists, rather than
  equally used ones, is a separate question.
title: 'In a sparsely-gated mixture-of-experts layer trained without balancing losses, the gate came to give large weights to the same few experts, which the authors attribute to self-reinforcement, favoured experts being trained more and so selected more; in one 256-expert language model, the squared coefficient of variation of expert importance or load as an auxiliary loss reduced the peak-to-mean load from 17.8 to at most 1.47 and test perplexity from 39.8 to 35.6–35.7'
version: 1
tags:
- learning-theory
- complex-systems
date: '2026-10-24'
source:
- LIT-tmp95a3g
summary: >-
  Shazeer et al. (2017), section 4 and Appendix A, read in full in
  NOTE-tmpa8fuv from arXiv v1. The imbalance is reported in one paragraph,
  with Table 6's no-loss row as its evidence: one architecture, ten epochs,
  no variance. The mechanism is the authors' explanation, not a tested
  result. The fix penalizes unequal use regardless of competence.
---
<!-- inactive-ok-file: NOTE-tmpa8fuv — the reading this is filed from -->

# THEORY-tmp2p13l: In a sparsely-gated mixture-of-experts layer trained without balancing losses, the gate came to give large weights to the same few experts, which the authors attribute to self-reinforcement, favoured experts being trained more and so selected more; in one 256-expert language model, the squared coefficient of variation of expert importance or load as an auxiliary loss reduced the peak-to-mean load from 17.8 to at most 1.47 and test perplexity from 39.8 to 35.6–35.7

## Source

Shazeer, Mirhoseini, Maziarz, Davis, Le, Hinton & Dean (2017),
LIT-tmp95a3g, read in NOTE-tmpa8fuv from arXiv:1701.06538v1: section 4
(pp. 5–6), Appendix A and Table 6 (pp. 13–14).

## What was actually shown

- **The imbalance.** With no balancing loss, CV of importance 3.04, CV of
  load 3.01, and the most loaded expert at 17.80 times the mean, in
  MoE-256 after 10 epochs on 1 billion words.
- **The fix.** Any of five settings of the importance and load losses
  gives CVs of 0.02–0.48, peak-to-mean load 1.07–1.47 and test perplexity
  35.6–35.7, against 39.8 with neither.
- **The mechanism**, stated and not tested: "the favored experts are
  trained more rapidly and thus are selected even more by the gating
  network" (p. 5). Eigen et al. (2013) report the same phenomenon.

## What this does not say

That the concentration was caused as the authors say: no trajectories,
seeds or initializations are compared. That the starved experts lost
competence rather than never gaining it. That balanced experts are
equally competent; the losses equalize use, not merit, so they keep
diversity in place from outside rather than letting a specialist earn
its share. Or that the same holds for other architectures or longer
training.
