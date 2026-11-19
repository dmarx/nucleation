---
status: Proposed
title: 'Raghu and colleagues show that on standard few-shot image-classification and RL benchmarks, MAML''s fast adaptation comes almost entirely from reusing features already present in its meta-initialization rather than from rapid change of representations, so that freezing all layers but the head at test time, or never adapting the body during training (ANIL), leaves performance about unchanged.'
version: 1
source:
- LIT-tmpm4bnq
tags:
- learning-theory
- representation-learning
date: '2026-11-19'
bears_on:
- QUESTION-tmpwqepn
promote_when: >-
  An independent replication on Omniglot or MiniImageNet with the standard
  MAML architecture finds that freezing the whole network body at test
  time costs at most a few points of accuracy, that ANIL matches MAML
  within seed variation, and that CCA or CKA similarity of body
  representations before and after inner-loop adaptation stays near 1.
summary: >-
  From the reading of LIT-tmpm4bnq in NOTE-tmpuduuy. Raghu, Raghu, Bengio
  and Vinyals (2019), arXiv 1909.09157, ICLR 2020. On standard few-shot
  benchmarks, freezing MAML's network body at test time barely changes
  accuracy, and body representations hardly move during adaptation (CCA
  above 0.9). MAML's success is therefore "feature reuse", not "rapid
  learning", and ANIL, which adapts only the head, matches MAML. It is
  here because A54 used it to separate reusable structure from the
  capacity to acquire structure, a clause of CLAIM-tmp8ljvp. The paper
  supports that distinction between routes to fast adaptation but does not
  measure acquisition capacity over training or forgetting. It also warns
  that a low adaptation budget can measure reuse rather than plasticity
  (CASE-tmphsr99). Read in its NOTE.
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmpfhidr: Raghu and colleagues show that on standard few-shot image-classification and RL benchmarks, MAML's fast adaptation comes almost entirely from reusing features already present in its meta-initialization rather than from rapid change of representations, so that freezing all layers but the head at test time, or never adapting the body during training (ANIL), leaves performance about unchanged.

## The account

MAML trains an initialization from which a few gradient steps solve a new task. Raghu and colleagues find that on the standard benchmarks those steps barely change the body. Accuracy is about the same with the body frozen, and representations before and after adaptation have CCA similarity above 0.9, from early in training on. Removing the body's inner loop altogether (ANIL) gives the same accuracy at lower cost, and dropping the head at test time (NIL) also matches. They conclude "feature reuse is the dominant factor".

## What it does not show

- Not that capacity to acquire new structure declines, or that it moves apart from reuse over training.
- Nothing about forgetting or continual learning.
- Not that the same holds where test tasks need features the training tasks did not supply. The authors limit the claim to benchmark datasets.
