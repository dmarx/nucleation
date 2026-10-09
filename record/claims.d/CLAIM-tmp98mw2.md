---
status: Proposed
title: 'A language model''s response to a context is functionally a parameterized pragmatic frame'
version: 1
role: thesis
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
- TERM-tmporf01
summary: >-
  The owner at U17, offered as a motivating example "maybe even just for
  notational purposes". The assistant made it the primary formal example
  (A43), then one running case of three (A52). Its formal statement,
  frame as a parameterized family of contexts, did not survive outline
  v4.
supports:
- ARG-tmpq5vp7
---
<!-- inactive-ok-file: CLAIM-tmpxrgp3 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->

# CLAIM-tmp98mw2: A language model's response to a context is functionally a parameterized pragmatic frame

## The claim

U17: "I'm wondering if leveraging an LLM (and how it responds to a context, i.e.
functionally a parameterized frame) as a motivating example, maybe even just for
notational purposes. there might also be valuable connections or even
experiments in the ICL/TTT literature we could draw from."

A43 made the model "the primary formal example", with Henley as "the motivating
*humanistic* example", and the model as "a **parameterized interpretive
instrument**, rather than being treated as a definitive judge of meaning".
A49's c_f = Γ(f, c_0) ([TERM-tmporf01](../terms.d/TERM-tmporf01.md)) is the claim in notation.

## Where it went

A48 kept the model as running case B, an "operational proxy". A52 kept it as
running case C. Its use as evidence is limited by [CLAIM-tmpo49t2](CLAIM-tmpo49t2.md). The manuscript keeps
language models as one kind of interpreter in its empirical programme
(Abstract, §10) and keeps one consequence ([CLAIM-tmpxrgp3](CLAIM-tmpxrgp3.md)), but no longer presents a
model's context-conditioning as a frame. C6 §6 (U32) demoted it: ICL and TTT
"are compatible with our theory but not required for its mathematical
definitions", and the notation P_θ(y | c, u) is gone from the manuscript.

## What the in-context-learning readings say

- **For the frame reading.** Min et al. ([LIT-tmpgsgpo](../literature.d/LIT-tmpgsgpo.md)) find a context's
  effect is carried by input distribution, label space and format rather
  than by correct labels. Xie et al. ([LIT-tmp6trip](../literature.d/LIT-tmp6trip.md)) give the formal sense
  in which a context fixes a posterior over a latent concept.
- **Toward the defeater.** Lu et al. ([LIT-tmpthf7j](../literature.d/LIT-tmpthf7j.md)) find that order alone,
  with content fixed, moves accuracy from near chance to near the state of
  the art. Good orders do not transfer across model sizes, so the "frame"
  is sensitive to surface form.
