---
status: Rejected
title: 'Freeman and Pfenning''s split between inferred refinements and annotations checked against them, by analogy, shows that the direction of fit is the split between inferring a type from a term and checking a term against a type given'
version: 1
form: analogy
grounds:
- THEORY-tmp1mruk
concludes:
- CLAIM-tmpnookt
uses:
- TERM-tmp8b1yl
tags:
- logic
- philosophy-of-language
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
summary: >-
  Rejected as a route: in Freeman and Pfenning's system ([THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md)) checking
  an annotation accepts it only when the inferred refinement already lies
  below it, and no rule moves a term, so checking is word to world as
  inference is, and the paper is not a bidirectional system. Standing of
  the conclusion apart from this route: [CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md) holds it, from the
  assistant's knowledge, untested until [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md) reads Dunfield and
  Krishnaswami; [CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md) tells against it for this system. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-tmp1mruk CLAIM-tmp764wb CLAIM-tmpnookt TERM-tmp8b1yl CLAIM-tmpmk056 — Proposed; the reading, the counter filed from it, the claim and term this is about, and the claim that holds performative update -->

# ARG-tmp5r67s: Freeman and Pfenning's split between inferred refinements and annotations checked against them, by analogy, shows that the direction of fit is the split between inferring a type from a term and checking a term against a type given

## The inference

[CLAIM-tmpnookt](../claims.d/CLAIM-tmpnookt.md): inference reads a type off a term, word to world, a
descriptor; checking holds a term to a type given in advance, world to
word, a requirement; the move that makes a term fit is elaboration or
coercion. Freeman and Pfenning's system has both modes: refinement types
"will be inferred and printed by type inference, or can be used by the
programmer to annotate expressions" (p. 3).

## Critical questions

- **Are the two alike in the respect the conclusion needs?** No. The
  conclusion needs checking to be world to word. In the paper the only
  rule for an annotation, RESTRICT (p. 8), accepts (e : D′) when the
  inferred D already satisfies D ≤ D′: the term passes when the type is
  written, which is [TERM-tmp8b1yl](../terms.d/TERM-tmp8b1yl.md)'s word-to-world direction, the same as
  inference.
- **Is the move that fits a term present?** No. "we do not extend the
  language of programs for ML (only the language of types)" (p. 1), and no
  rule inserts or changes anything. A term that fails an annotation is
  left for the programmer: the performative update of [CLAIM-tmpmk056](../claims.d/CLAIM-tmpmk056.md) lies
  outside the system.
- **Is the source the right one?** No. The paper is inference with
  optional annotations, not a bidirectional system; it can show that
  checking need not impose, not what checking does where it is a mode of
  its own.

## Verdict

Rejected as a route to the correspondence; [CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md) files what the paper
does show.
