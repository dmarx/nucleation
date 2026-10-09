---
number: 20
status: Open
formerly:
- QUESTION-tmppfksp
title: 'Can improving the interpreter substitute for information transmitted in the utterance, and at what rate–distortion trade-off?'
version: 1
tags:
- information-theory
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
refines:
- QUESTION-002
summary: >-
  A86 §6, "an experimental question we have not yet investigated". The
  manuscript narrows it to a distinction, improving the signal versus
  improving the interpreter (§5), and an implication (§11); the trade-
  off itself was dropped without critique.
---
<!-- inactive-ok-file: CLAIM-118 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: LIT-767 — Deferred; unread here or set aside, cited as what the exchange or manuscript names and not leaned on -->

# QUESTION-020: Can improving the interpreter substitute for information transmitted in the utterance, and at what rate–distortion trade-off?

## Why it is a question

A86 §6 gave three ways to improve a translation: a better translation (the
transmitted representation V; improved coding), better context (receiver
information K; decoder side information), and interpreter adaptation (the
effective decoder). Then: "This creates an experimental question we have not
yet investigated: **Can improving the interpreter substitute for increasing the
information transmitted in the utterance?** A highly adapted reader may
correctly reconstruct speaker footing from relatively sparse cues. An unfamiliar
reader might require explicit explanatory material." With it came a
context-dependent rate–distortion function R_K(D), and A86's own correction:
when only the decoder has K, it is a Wyner–Ziv problem ([LIT-767](../literature.d/LIT-767.md)).

## Where it stands

The manuscript keeps the distinction ([CLAIM-118](../claims.d/CLAIM-118.md)) and one consequence (§11: "an
adapted receiver may recover an implicit relation without additional message
bits"). It states no trade-off and proposes no experiment for it. A86 §10 had
named "how much decoder adaptation compensates for lower rate" as one of three
target results.

## Evidence since

Akyürek et al. ([LIT-796](../literature.d/LIT-796.md)) get more from the same demonstrations by
improving the interpreter (test-time training) than by conditioning alone.
That is direct evidence that adaptation can stand in for transmitted
information. Min et al. ([LIT-814](../literature.d/LIT-814.md)) find that the correctness of the
labels carries little of what a context transmits.
