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
<!-- inactive-ok-file: CLAIM-049 CLAIM-074 CLAIM-182 THEORY-169 — listed as material that may bear on this question, not as settled -->
<!-- inactive-ok-file: CLAIM-118 — Proposed; open, and cited as open: the claim, argument or reading is under test, not settled -->
<!-- inactive-ok-file: LIT-767 — Unavailable; unread here or set aside, cited as what the exchange or manuscript names and not leaned on -->
<!-- inactive-ok-file: CLAIM-199 CLAIM-258 — Proposed; cited in a note of 2026-10-12 as open, for what each holds, not as settled -->

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

## Note of 2026-10-11: material in the record that may bear on this

A synthesis review of 2026-10-11 found these entries bearing on this
question without being linked to it. Each is listed for what its title
says; none has yet been assessed as an answer, and none is linked by
`answers`.

- [THEORY-169](../theory.d/THEORY-169.md): In attention layers, conditioning on a context is exactly
  training a learner on it and predicting: linear…
- [CLAIM-074](../claims.d/CLAIM-074.md): Fidelity is relative to the interpreter's learning history: a
  frame given in context is transient while an…
- [CLAIM-049](../claims.d/CLAIM-049.md): An adaptive interpreter's state includes its message, context
  knowledge and learned parameters, and…
- [CASE-005](../cases.d/CASE-005.md): The language-model experiments: frame commutator, trajectory-
  preserving selection, ICL against TTT
- [CLAIM-182](../claims.d/CLAIM-182.md): Storage is not anchoring, addressability is: a structure that
  is kept but cannot be pointed at part by…

## Note of 2026-10-12: a ceiling on what a better interpreter can gain

PR [#121](https://github.com/dmarx/nucleation/issues/121) filed [CLAIM-199](../claims.d/CLAIM-199.md), a proposal, which separates what a rendering
makes possible, the best risk over all decision rules, from what a
receiver can use, the best risk over the rules it can apply. On that
account no receiver does better with a garbling than an ideal receiver
does with the source. That bears on how far improving the interpreter can
stand in for transmitted information. Its worked example has no side
information at the decoder, which is A86's Wyner–Ziv case. [CLAIM-258](../claims.d/CLAIM-258.md)
and [CLAIM-237](../claims.d/CLAIM-237.md), on side information and deficiency, bear here as on
[QUESTION-016](QUESTION-016.md).
