---
status: Proposed
title: 'Finn, Abbeel and Levine show that training a network''s initial parameters on the loss after one or a few gradient steps on each of many tasks from a declared task distribution, rather than on the loss at those parameters, yields an initialization that adapts to new tasks from that distribution from a handful of examples where joint pretraining on the same tasks does not'
version: 1
source:
- LIT-tmphr4nm
tags:
- learning-theory
date: '2026-11-19'
bears_on:
- QUESTION-tmpwqepn
corroborates:
- CLAIM-tmp5gbzr
promote_when: >-
  The record accepts the comparison as reported: an independent
  replication, or the record's own reading of a later study, finds a post-
  adaptation (MAML-style) objective beating joint pretraining plus fine-
  tuning on few-shot adaptation within a declared task family at matched
  data.
summary: >-
  From the reading of [LIT-tmphr4nm](../literature.d/LIT-tmphr4nm.md) in [NOTE-tmp3r6eu](../notes.d/NOTE-tmp3r6eu.md). Finn, Abbeel and
  Levine (2017), ICML 2017, arXiv 1703.03400. MAML trains a network's
  initial parameters on the loss after one or a few gradient steps on each
  task drawn from a declared task distribution, so that the model is, in
  the authors' words, "easy to fine-tune"; on sinusoid regression, few-
  shot Omniglot and MiniImagenet and goal-conditioned RL it adapts from a
  handful of examples where joint pretraining on the same tasks does not.
  Here because its objective already targets future adaptability, the
  disclaimer [CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md) and [QUESTION-tmpwqepn](../questions.d/QUESTION-tmpwqepn.md) carry: the reading
  confirms it, for a declared task distribution and a declared adaptation
  budget only. It also gives an empirical instance of [CLAIM-tmp5gbzr](../claims.d/CLAIM-tmp5gbzr.md), an
  initialization ranked below joint training on present loss and above it
  once adaptation is counted. Read in its NOTE.
---
<!-- inactive-ok-file: CLAIM-tmp5gbzr CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# THEORY-tmpsw2ct: Finn, Abbeel and Levine show that training a network's initial parameters on the loss after one or a few gradient steps on each of many tasks from a declared task distribution, rather than on the loss at those parameters, yields an initialization that adapts to new tasks from that distribution from a handful of examples where joint pretraining on the same tasks does not

## The account

MAML's meta-objective is the sum over sampled tasks of the loss of the
adapted parameters, θ − α∇L(θ), optimized with respect to θ (§2.2). In the
authors' words it "trains the model to be easy to fine-tune". On sinusoid
regression a model pretrained jointly on all tasks learns the average output
and cannot adapt from five points, while the MAML model adapts and infers
the unsampled half of the curve (§5.1); on few-shot Omniglot and
MiniImagenet it matches or beats classification-specific methods (§5.2); in
policy-gradient RL it adapts within one to three steps where pretraining is
sometimes worse than random initialization (§5.3). The adapted model keeps
improving past the number of steps it was trained for.

## What it does not show

That the objective targets adaptability beyond the declared p(T) and the
declared step budget; anything about the cost of acquiring new task
families outside p(T); that the effect holds for large pretrained models.
Later work ([LIT-tmpm4bnq](../literature.d/LIT-tmpm4bnq.md), Raghu et al.) argues the gain is mostly feature
reuse rather than rapid learning, which this paper does not test.
