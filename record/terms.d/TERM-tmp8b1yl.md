---
status: Proposed
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
- TERM-tmp94y6v
- TERM-134
draws_on:
- THEORY-162
summary: >-
  Filed beside [TERM-tmp94y6v](TERM-tmp94y6v.md) at the owner's "could we maybe benefit from a term?",
  as the second reading of which term was meant. Searle's notion, made
  formal in Krifka's performative updates ([LIT-835](../literature.d/LIT-835.md), [THEORY-162](../theory.d/THEORY-162.md)), and the
  record's descriptor and imposition ([TERM-134](TERM-134.md), [CLAIM-tmpmk056](../claims.d/CLAIM-tmpmk056.md)). The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: TERM-tmp94y6v TERM-134 THEORY-162 CLAIM-tmpmk056 CLAIM-tmp5rv9x — Proposed; the term filed with this, and the entries it is stated against -->

# TERM-tmp8b1yl: direction of fit, of a test or predicate: whether it is written to fit what it is applied to, describing it, or what it is applied to must be made to fit it, requiring it; formally, informative against performative update

## Definition

A test applied to something has a **direction of fit**:

- **word to world**: the test is written to fit the thing, so the thing
  passes it when it is added. Applied, it narrows what the thing may be
  taken to be and moves nothing: informative update, the record's
  descriptor.
- **world to word**: the thing must be made to fit the test, which it does
  not yet pass. Applied, it moves the thing to the nearest version that
  passes: performative update, the record's imposition ([CLAIM-tmpmk056](../claims.d/CLAIM-tmpmk056.md)).

Which direction a test has is settled by the thing as it stands when the
test is applied, not by the test's wording: the same sentence describes
one entry and imposes on another. A test can change direction: a
requirement that building shows cannot be met is rewritten to describe what
can ([CLAIM-tmp5rv9x](../claims.d/CLAIM-tmp5rv9x.md)).

## Not to be confused with

- **Hard against soft.** That is how strongly a test is enforced
  ([TERM-134](TERM-134.md)); either direction can be enforced hard or soft.
- **Descriptive against normative content.** A descriptor can state a norm
  the entry already meets; direction of fit is about the relation of a test
  to its object, not about what the test says.

## Note of 2026-11-22: Freeman and Pfenning, read
<!-- inactive-ok-file: THEORY-tmp1mruk CLAIM-tmp764wb — Proposed; filed for LEAD-tmp3xevc -->

A case for this term's criterion that the thing as it stands, not the
test's wording, sets the direction. In Freeman and Pfenning's refinement
types ([THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md); [NOTE-tmpew427](../notes.d/NOTE-tmpew427.md)) a type the programmer writes in advance is
checked by accepting it only when the term's inferred refinement already
lies below it (p. 8): checked, and still word to world. The world-to-word
direction appears only when a term fails and the programmer changes it,
outside the type system. So the direction does not divide inferred from
checked types there ([CLAIM-tmp764wb](../claims.d/CLAIM-tmp764wb.md)). The definition stands.

## Note of 2026-11-22: Davies and Pfenning, read
<!-- inactive-ok-file: THEORY-tmpei9b5 ARG-tmp7pf1t CLAIM-tmpvq4ru — Proposed; filed for LEAD-tmp3xevc -->

Two cases from Davies and Pfenning's bidirectional checker
(THEORY-tmpei9b5; NOTE-tmpaiy4v). A failing ascription is world to word
on any reading: double fails its type, the type stands, and the term is to
be changed by the programmer, outside the checker (p. 10; CLAIM-tmpvq4ru).
A met one (inc) is the hard case: the paper does not say whether the type
was written before the code, so this term's criterion, that the thing as
it stands settles the direction, and the reading that a type given in
advance requires whether or not it is met, both fit it (ARG-tmp7pf1t, two
alternatives). The paper adds a distinction this term does not draw: the
same ascription is checked against its term and then relied on by the
term's uses, so one test can be world to word toward the thing it is
applied to and word to world toward those who read it. The definition
stands; whether to add that distinction is the owner's call.
