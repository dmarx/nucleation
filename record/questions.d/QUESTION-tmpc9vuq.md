---
status: Open
title: 'Is the latent-variable MDL bound of Theorem 4 in Sefidgaran et al. non-vacuous for a trained encoder, with a type-III symmetric prior that does not use the ghost data?'
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-19'
line: 'learned-structure'
summary: >-
  Filed when the promotion audit (batch 038, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-238](../theory.d/THEORY-238.md). The constant in Theorem 4 was re-derived and the
  bound holds as stated. The former promote_when also asked whether the
  bound is small for a real network, which the account does not claim.
  This question holds that request.
---

# QUESTION-tmpc9vuq: Is the latent-variable MDL bound of Theorem 4 in Sefidgaran et al. non-vacuous for a trained encoder, with a type-III symmetric prior that does not use the ghost data?

## Why it is a question

[THEORY-238](../theory.d/THEORY-238.md) states Theorem 4 of [LIT-245](../literature.d/LIT-245.md): the expected generalization error
of an encoder–decoder learner is at most 2√((2B + K + 2)/n) + ε, where B
is the KL divergence of the encoder's train-and-ghost latents to a prior
symmetric under label-preserving permutations. The theorem holds for any
decoder, and its constants were re-checked in the audit. Nobody has
computed it. The paper lists evaluating it "analytically in simple
setups" as future work. The prior it allows may depend on the ghost set,
which a learner never sees, and the experiment approximates it by moving
averages that are only approximately symmetric. A floor of 2√((K+2)/n)
remains however compressible the latents are.

So whether this quantity accounts for generalization in practice, rather
than only in principle, is open.

## What would answer it

A numerical evaluation of the bound for a trained encoder, with a prior
built without the ghost data and checked to be type-III symmetric, showing
whether the bound is below 1 for 0–1 loss, and how close it is to the
measured gap. A bound that is vacuous at realistic n and K would answer it
no for that setting. Test accuracies of regularizers built from the bound,
such as CDVIB, cannot settle it: a better regularizer does not show that
the bound is tight.
