---
number: 111
status: Proposed
formerly:
- CLAIM-tmpw9mi0
title: 'A text supports a distribution over possible communicative situations, and a translation can be faithful by preserving that distribution and its response to further evidence'
version: 1
role: thesis
warrant: interpretive
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
- QUESTION-021
uses:
- TERM-011
grounds:
- THEORY-172
summary: >-
  A45 §6, recovered: fidelity as P_o(z | c_o, u_o) ≈ P_t(τ_z(z) | c_t,
  u_t), "an interesting middle position between our original
  relativistic account and the later dynamical account". Dropped at
  outline v3 without critique.
objected_by:
- CLAIM-236
complements:
- CLAIM-214
---
<!-- ref::uses-file: TERM-011 — stated in "frame, as inferred from evidence"; the body names the term only inside quotations of its source, which are not altered (ADR-038) -->

# CLAIM-111: A text supports a distribution over possible communicative situations, and a translation can be faithful by preserving that distribution and its response to further evidence

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

It answers [QUESTION-021](../questions.d/QUESTION-021.md) between its horns. There is no single act, and identity is not
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
[CLAIM-046](CLAIM-046.md) if the posterior is read as a summary of observations.

## A worked model

Rational speech act models ([THEORY-172](../theory.d/THEORY-172.md)) treat the listener's output as
exactly this: a posterior over what the speaker meant, given the utterance
and its alternatives. Frank and Goodman ([LIT-821](../literature.d/LIT-821.md)) give it for
referents. Goodman and Frank's extended model ([LIT-816](../literature.d/LIT-816.md)) gives a joint
posterior over the world and the speaker's topic, knowledge or lexicon,
which is an utterance supporting a distribution over the situation of its
saying.

## Note of 2026-10-10: the replies

[CLAIM-214](CLAIM-214.md) (2026-10-10): the criterion compares each language's own
posterior and needs no correspondence of alternative sets. Two consequences:
a rendering with the source's literal content can fail it, and a target
language may admit no rendering that passes.

## Note of 2026-10-30: what holds it back

It offers an answer to [QUESTION-021](../questions.d/QUESTION-021.md), which is Open with two rival offered
answers, [CLAIM-137](CLAIM-137.md) and [CLAIM-151](CLAIM-151.md), both Proposed. Promoting it would answer
that question, which needs a showing that the distribution criterion
predicts faithfulness judgements better than one act or a family of
realizations does. The comparison in its defeat condition, renderings
whose inferred-situation posteriors match the source's against renderings
whose posteriors differ, has not been run.
