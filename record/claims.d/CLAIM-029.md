---
number: 29
status: Proposed
formerly:
- CLAIM-tmp98mw2
title: 'A language model''s response to a context is functionally a parameterized pragmatic frame'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  Prompt effects on a model's interpretations fail paraphrase invariance
  and transfer, so that what a context does to the model is not a
  function of the frame it describes but of its surface form.
tags:
- philosophy-of-language
- representation-learning
date: '2026-10-08'
line: pragmatic-transport
uses:
- TERM-025
grounds:
- LIT-460
summary: >-
  The owner at U17, offered as a motivating example "maybe even just for
  notational purposes". The assistant made it the primary formal example
  (A43), then one running case of three (A52). Its formal statement,
  frame as a parameterized family of contexts, did not survive outline
  v4.
supports:
- ARG-008
---
<!-- inactive-ok-file: CLAIM-118 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: THEORY-251 — Proposed; filed today, cited as a qualification of the defeater, not leaned on -->

# CLAIM-029: A language model's response to a context is functionally a parameterized pragmatic frame

## The claim

U17: "I'm wondering if leveraging an LLM (and how it responds to a context, i.e.
functionally a parameterized frame) as a motivating example, maybe even just for
notational purposes. there might also be valuable connections or even
experiments in the ICL/TTT literature we could draw from."

A43 made the model "the primary formal example", with Henley as "the motivating
*humanistic* example", and the model as "a **parameterized interpretive
instrument**, rather than being treated as a definitive judge of meaning".
A49's c_f = Γ(f, c_0) ([TERM-025](../terms.d/TERM-025.md)) is the claim in notation.

## Where it went

A48 kept the model as running case B, an "operational proxy". A52 kept it as
running case C. Its use as evidence is limited by [CLAIM-085](CLAIM-085.md). The manuscript keeps
language models as one kind of interpreter in its empirical programme
(Abstract, §10) and keeps one consequence ([CLAIM-118](CLAIM-118.md)), but no longer presents a
model's context-conditioning as a frame. C6 §6 (U32) demoted it: ICL and TTT
"are compatible with our theory but not required for its mathematical
definitions", and the notation P_θ(y | c, u) is gone from the manuscript.

## What the in-context-learning readings say

- **For the frame reading.** Min et al. ([LIT-814](../literature.d/LIT-814.md)) find a context's
  effect is carried by input distribution, label space and format rather
  than by correct labels. Xie et al. ([LIT-797](../literature.d/LIT-797.md)) give the formal sense
  in which a context fixes a posterior over a latent concept.
- **Toward the defeater.** Lu et al. ([LIT-833](../literature.d/LIT-833.md)) find that order alone,
  with content fixed, moves accuracy from near chance to near the state of
  the art. Good orders do not transfer across model sizes, so the "frame"
  is sensitive to surface form.
- **A qualification of that defeater.** Kirsanov et al. ([LIT-946](../literature.d/LIT-946.md), read in
  [NOTE-789](../notes.d/NOTE-789.md); [THEORY-251](../theory.d/THEORY-251.md)) find that across draws of examples the
  class representations barely move while accuracy swings widely: the
  sensitivity to example selection sits in the vocabulary readout. If the
  frame is the representation a context sets, it is more stable than the
  accuracy suggests. Order was not varied, only which examples were drawn,
  so this qualifies Lu et al.'s point without settling their case.

## Prior statement

Shanahan, McDonell and Reynolds's role play ([LIT-460](../literature.d/LIT-460.md), read in [NOTE-370](../notes.d/NOTE-370.md))
states this idea most clearly before the manuscript. The prompt selects a
role from a superposition of characters, and each reply narrows the set.

## Note of 2026-10-15: three observations the defeater runs together

A3 of the exchange of 2026-10-14 (workbench entry of 2026-10-15) found
this claim and separated three observations: a prompt changes the output
distribution; a prompt changes an internal task or interpretive
representation; two prompts, or a prompt and an activation intervention,
induce equivalent pragmatic behaviour over a stated family of contexts.
"The first does not entail the second, and neither entails the third."

Its point about `defeated_if` is right. Failure of paraphrase invariance
and transfer would defeat a stronger hypothesis, that the model's
representation is invariant to surface form, not the reading of a
model's response as a parameterized frame. Kirsanov et al.'s stable class
representations, above, already pull the two apart. The defeater is left
as it stands; restating it is the owner's call. A3's prompt-equivalence
claim, equivalence over decision consequences, is [CLAIM-050](CLAIM-050.md) applied to
prompts and is not filed. Its question about activation steering is
[QUESTION-106](../questions.d/QUESTION-106.md).
