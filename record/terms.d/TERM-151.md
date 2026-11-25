---
number: 151
status: Proposed
formerly:
- TERM-tmp8b1yl
title: 'direction of fit, of a test or predicate: whether it is written to fit what it is applied to, describing it, or what it is applied to must be made to fit it, requiring it; formally, informative against performative update'
version: 1
tags:
- philosophy-of-language
- epistemology
- logic
date: '2026-11-22'
line:
- record-as-apparatus
- formal-apparatus
complements:
- TERM-152
- TERM-134
draws_on:
- THEORY-162
summary: >-
  Filed beside [TERM-152](TERM-152.md) at the owner's "could we maybe benefit from a term?",
  as the second reading of which term was meant. Searle's notion, made
  formal in Krifka's performative updates ([LIT-835](../literature.d/LIT-835.md), [THEORY-162](../theory.d/THEORY-162.md)), and the
  record's descriptor and imposition ([TERM-134](TERM-134.md), [CLAIM-943](../claims.d/CLAIM-943.md)). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: TERM-152 TERM-134 THEORY-162 CLAIM-943 CLAIM-942 — Proposed; the term filed with this, and the entries it is stated against -->

# TERM-151: direction of fit, of a test or predicate: whether it is written to fit what it is applied to, describing it, or what it is applied to must be made to fit it, requiring it; formally, informative against performative update

## Definition

A test applied to something has a **direction of fit**:

- **word to world**: the test is written to fit the thing, so the thing
  passes it when it is added. Applied, it narrows what the thing may be
  taken to be and moves nothing: informative update, the record's
  descriptor.
- **world to word**: the thing must be made to fit the test, which it does
  not yet pass. Applied, it moves the thing to the nearest version that
  passes: performative update, the record's imposition ([CLAIM-943](../claims.d/CLAIM-943.md)).

Which direction a test has is settled by the thing as it stands when the
test is applied, not by the test's wording: the same sentence describes
one entry and imposes on another. A test can change direction: a
requirement that building shows cannot be met is rewritten to describe what
can ([CLAIM-942](../claims.d/CLAIM-942.md)).

## Not to be confused with

- **Hard against soft.** That is how strongly a test is enforced
  ([TERM-134](TERM-134.md)); either direction can be enforced hard or soft.
- **Descriptive against normative content.** A descriptor can state a norm
  the entry already meets; direction of fit is about the relation of a test
  to its object, not about what the test says.

## Note of 2026-11-22: Freeman and Pfenning, read
<!-- inactive-ok-file: THEORY-2259 CLAIM-965 — Proposed; filed for LEAD-215 -->

A case for this term's criterion that the thing as it stands, not the
test's wording, sets the direction. In Freeman and Pfenning's refinement
types ([THEORY-2259](../theory.d/THEORY-2259.md); [NOTE-2350](../notes.d/NOTE-2350.md)) a type the programmer writes in advance is
checked by accepting it only when the term's inferred refinement already
lies below it (p. 8): checked, and still word to world. The world-to-word
direction appears only when a term fails and the programmer changes it,
outside the type system. So the direction does not divide inferred from
checked types there ([CLAIM-965](../claims.d/CLAIM-965.md)). The definition stands.

## Note of 2026-11-22: Davies and Pfenning, read
<!-- inactive-ok-file: THEORY-2260 ARG-211 CLAIM-974 — Proposed; filed for LEAD-215 -->

Two cases from Davies and Pfenning's bidirectional checker
([THEORY-2260](../theory.d/THEORY-2260.md); [NOTE-2351](../notes.d/NOTE-2351.md)). A failing ascription is world to word
on any reading: double fails its type, the type stands, and the term is to
be changed by the programmer, outside the checker (p. 10; [CLAIM-974](../claims.d/CLAIM-974.md)).
A met one (inc) is the hard case: the paper does not say whether the type
was written before the code, so this term's criterion, that the thing as
it stands settles the direction, and the reading that a type given in
advance requires whether or not it is met, both fit it ([ARG-211](../arguments.d/ARG-211.md), two
alternatives). The paper adds a distinction this term does not draw: the
same ascription is checked against its term and then relied on by the
term's uses, so one test can be world to word toward the thing it is
applied to and word to world toward those who read it. The definition
stands; whether to add that distinction is the owner's call.

## Note of 2026-11-22: Rondon, Kawaguchi and Jhala, read
<!-- inactive-ok-file: THEORY-2262 CLAIM-975 — Proposed; filed for LEAD-215 -->

Two cases for this term (case and qualification; no edge). Liquid type
inference ([THEORY-2262](../theory.d/THEORY-2262.md); [NOTE-2353](../notes.d/NOTE-2353.md)) is informative update in the
plain sense: it starts from "a trivial assignment, in which each liquid
type variable is assigned the conjunction of all logical qualifiers" and
weakens it until the program passes (p. 166). Descriptions the program
fails are passed through and dropped; the program never moves. Where a
test fails, the description gives way: the word-to-world direction. The
result is the strongest description the vocabulary and the check allow.

The qualification ([CLAIM-975](../claims.d/CLAIM-975.md)): where tests are checked by a
conservative procedure, "passes" and "is verified to pass" come apart.
The paper's failures may lie in the program, the qualifier set or the
checker (pp. 160, 169), so a test that fails to check is not thereby world
to word. The criterion here, the thing as it stands, reads best as the
thing as it stands *and is checked*. The definition stands; the
distinction is the claim's.

## Note of 2026-11-25: Martin-Löf, read
<!-- inactive-ok-file: THEORY-tmp62cvo NOTE-tmp60upv — Proposed or Skimmed; filed for LEAD-215 -->

A parallel (no edge). Martin-Löf's table of readings (THEORY-tmp62cvo;
NOTE-tmp60upv) reads one form of judgement, a ∈ A, both as "a is an
element of the set A" and as "a is a method of fulfilling (realizing) the
intention (expectation) A" (p. 5), Heyting's reading, in which the
judgement is world to word. The direction belongs to the reading of the
judgement, not to its form, which agrees with this term's criterion that
the thing and its test, not the sentence's wording, settle it. The book
has no inference or checking algorithm and says nothing on the
bidirectional correspondence. The definition stands.
