---
status: Proposed
title: 'A text supports a distribution over possible communicative situations, and a translation can be faithful by preserving that distribution and its response to further evidence'
version: 1
role: thesis
defeated_if: >-
  Renderings whose inferred-situation posteriors match those of the
  source, including after added evidence, are judged no more faithful
  than renderings whose posteriors differ.
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
answers:
- QUESTION-tmpt7lzm
uses:
- TERM-tmpa0fi1
grounds:
- THEORY-tmprknoj
summary: >-
  A45 §6, recovered: fidelity as P_o(z | c_o, u_o) ≈ P_t(τ_z(z) | c_t,
  u_t), "an interesting middle position between our original
  relativistic account and the later dynamical account". Dropped at
  outline v3 without critique.
---
<!-- inactive-ok-file: THEORY-tmprknoj — Proposed; rational speech acts, cited as a worked model of this claim, not as settled -->
<!-- inactive-ok-file: CLAIM-tmpd81nk — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-tmpw9mi0: A text supports a distribution over possible communicative situations, and a translation can be faithful by preserving that distribution and its response to further evidence

## The claim

A45 §6: P_o(z | c_o, u_o) ≈ P_t(τ_z(z) | c_t, u_t), "where τ_z maps corresponding
latent communicative frames across linguistic environments. This suggests an
interesting middle position between our original relativistic account and the
later dynamical account. Rather than assuming that the text has one fully
specified communicative identity, we represent it as supporting a distribution
over possible communicative situations. Different wording and delivery contexts
change that distribution. The translator's objective can be framed as preserving
some relevant structure of the distribution, perhaps including its response to
further evidence."

It answers [QUESTION-tmpt7lzm](../questions.d/QUESTION-tmpt7lzm.md) between its horns. There is no single act, and identity is not
merely a family of realizations either: it is a distribution over acts.

## Where it went

A48 §4.2 kept the factorization as a "candidate explanatory model" but not as a
fidelity criterion, and A52 did the same. Nothing argued against it. The
mechanistic-interpretability programme A45 attached to it went at the same time:
"Can one identify internal representations that systematically track inferred
speaker footing or audience alignment? Can interventions on those
representations reproduce the effects of changing the linguistic framing
context?"

## What it does not say

That z exists: "a modeling assumption. In an arbitrary neural network, no
unique, identifiable latent variable z need exist." It is compatible with
[CLAIM-tmpd81nk](CLAIM-tmpd81nk.md) if the posterior is read as a summary of observations.

## A worked model

Rational speech act models ([THEORY-tmprknoj](../theory.d/THEORY-tmprknoj.md)) treat the listener's output as
exactly this: a posterior over what the speaker meant, given the utterance
and its alternatives. Frank and Goodman ([LIT-tmpkwn2g](../literature.d/LIT-tmpkwn2g.md)) give it for
referents. Goodman and Frank's extended model ([LIT-tmphavsf](../literature.d/LIT-tmphavsf.md)) gives a joint
posterior over the world and the speaker's topic, knowledge or lexicon,
which is an utterance supporting a distribution over the situation of its
saying.
