---
status: Proposed
title: 'A language model agreeing with humans in direction is weak evidence, because models are trained on human text about teasing and reproach and the founding stimuli are famous, and the language-model test bed''s defeat condition fires only on a reversal'
version: 1
role: counter
tags:
- representation-learning
- philosophy-of-science
date: '2026-10-10'
line: pragmatic-transport
rests_on:
- CLAIM-085
grounds:
- LIT-833
objects_to:
- CLAIM-058
summary: >-
  Found in the record's audit of the line on 2026-10-10 (empirical lens);
  no turn of the exchange raises it. Agreement in direction is what a model
  trained on human descriptions of teasing and reproach would show anyway,
  and Villon, Henley and Hofstadter's Marot are likely in training data,
  so a model's "interpretation" of them may be recall. [ARG-008](../arguments.d/ARG-008.md) and
  [CLAIM-085](CLAIM-085.md) already bound what model results show about human pragmatics.
  What is new is that [CLAIM-058](CLAIM-058.md)'s validity bar is too low, and the
  contamination point. Minor.
---
<!-- inactive-ok-file: CLAIM-058 — Proposed; open, and cited as the claim this objection is to -->
<!-- inactive-ok-file: CLAIM-029 — Proposed; open, cited for its reading of LIT-833, not as settled -->

# CLAIM-tmpt2k3r: A language model agreeing with humans in direction is weak evidence, because models are trained on human text about teasing and reproach and the founding stimuli are famous, and the language-model test bed's defeat condition fires only on a reversal

## The objection

[CLAIM-058](CLAIM-058.md) holds that context-conditioned language models are a setting in
which the theory's effects "can be tested before human studies". It is
defeated only if "Framing and order effects found in models fail to
replicate, even in direction, in matched human studies". So it survives any
human result that has the same sign as the model's.

**The bar is low.** Agreement in direction is what a model trained on human
writing would show whatever its mechanism. Such a model has read a great deal
of text in which people describe, enact and react to teasing, reproach and
shifts of footing. [ARG-008](../arguments.d/ARG-008.md) already grants that "An LLM's context-conditioning
behavior need not correspond to human inference over communicative
situations." If that is so, matching direction is weak evidence that the
model tests anything about the theory's claims on human interpretation.

**The founding stimuli are famous.** Villon, Henley's rendering of Villon and
Hofstadter's translations of Marot are widely published and discussed. They
are likely in the training data, together with commentary on them. A model's
reading of their footing may then be recall of what has been written about
them, not interpretation. No entry in claims, cases or questions raises
training-data contamination. The word appears only as cross-condition
contamination within one conversation ([CLAIM-085](CLAIM-085.md), [CASE-032](../cases.d/CASE-032.md)).

**One model is not enough.** Lu et al. ([LIT-833](../literature.d/LIT-833.md)), as [CLAIM-029](CLAIM-029.md) reads them,
find that order alone moves accuracy from near chance to near the state of
the art, and that good orders do not transfer across model sizes. That is
order sensitivity, not a reversal of a pragmatic effect, but it shows that
what a context does to one model need not be what it does to another. A
directional agreement found in one model may not hold in the next.

What is already documented: [CLAIM-085](CLAIM-085.md) grants that a framing effect in one
model "establishes a property of that model under those prompts", and [ARG-008](../arguments.d/ARG-008.md)
does not extend "to evidence about human pragmatics". This objection adds
that [CLAIM-058](CLAIM-058.md)'s own defeat condition is too weak a test of validity, and the
contamination point.

## What it does not say

- It does not say language models are useless as a test bed. Control of
  frames and orders is real ([ARG-008](../arguments.d/ARG-008.md)).
- It does not say a directional match is no evidence, only that it is weak.

## What would answer it

- A defeat condition on magnitude or on the pattern across conditions, not
  only on sign.
- Stimuli held out from training: new texts, or texts written after the
  models' training cut-off, alongside the famous ones.
- Agreement required across several model families and sizes.
