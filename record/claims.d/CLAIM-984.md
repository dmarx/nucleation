---
number: 984
status: Proposed
formerly:
- CLAIM-tmpmp7w2
title: 'Closed vocabulary lets description be inferred'
statement: >-
  Whether a specification can be read off what it specifies or must be
  stated in advance depends on whether its vocabulary of tests is closed:
  over a finite declared vocabulary the strongest description an object
  passes is computable, so describing can be left to inference, while over
  an open one no strongest description need exist and what the object is to
  satisfy must be written down
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A system whose refinement vocabulary is open, predicates formed freely,
  in which the strongest refinement a term passes is nonetheless inferred
  without annotation; or one whose vocabulary is finite and declared in
  which annotations are still needed for something other than choosing
  among refinements the term already passes.
tags:
- logic
- epistemology
- software-engineering
date: '2026-11-22'
line:
- formal-apparatus
- record-as-apparatus
grounds:
- THEORY-2259
- THEORY-2260
complements:
- CLAIM-949
- CLAIM-974
uses:
- TERM-151
summary: >-
  Offered by the Davies and Pfenning reader as something only the two
  readings together show, and filed under the dialectic regime,
  2026-11-22. Freeman and Pfenning declare a finite lattice of refinements
  and infer everything ([THEORY-2259](../theory.d/THEORY-2259.md)); Davies and Pfenning let
  refinements combine freely, find inference "most likely undecidable",
  and have the programmer state types ([THEORY-2260](../theory.d/THEORY-2260.md)). Two systems are a
  contrast, not a test; the Liquid Types reading under [LEAD-215](../leads.d/LEAD-215.md), whose
  qualifiers are a finite set chosen to keep inference decidable, is the
  third. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-2259 THEORY-2260 — Proposed; the readings and claims this is stated against -->

# CLAIM-984: Closed vocabulary lets description be inferred

## The claim

Freeman and Pfenning's refinements come from a finite lattice the
programmer declares, and finiteness is "necessary for the decidability
of refinement type inference": every refinement a term passes is
computed, and an annotation only picks among them. Davies and Pfenning
let refinements combine by intersection without that bound, find
inference "most likely undecidable, and principal types do not exist",
and so have the programmer ascribe types, mostly to functions. Read
together: when the tests a specification may use are closed and finite,
the strongest description an object passes is a function of the object,
and nothing need be stated; when they are open, the object does not
determine which of its true descriptions matters, and someone must say.

## Bearing on the record

The record's predicates are open: a claim's title, a term's definition,
any test written in prose. On this claim that is why the record's
descriptors are filed rather than computed, and why the filer, not the
tooling, writes them. The record's closed vocabularies (statuses, tags,
roles, warrants) are the part a tool can check and in principle infer.

## Admission ([ADR-075](../decisions.d/ADR-075.md))

A discriminating prediction: a third system, Liquid Types, whose
qualifiers are a finite set, should infer refinements without
annotation over that set and need annotations only beyond it. An outcome
in which it needs annotations over its own qualifiers goes against this.

## Note of 2026-11-22: Rondon, Kawaguchi and Jhala, read
<!-- inactive-ok-file: THEORY-2262 — Proposed; the reading noted here -->

The discriminating prediction is met. Liquid types infer refinements over
the finite qualifier set Q with no annotation, the restriction to Q being
what makes inference "efficiently decidable" ([THEORY-2262](../theory.d/THEORY-2262.md)). The
failures the paper reports trace to the qualifiers chosen or to the
conservative check, not to a need for annotation over Q. One system
agrees; the claim stays Proposed. The note names the reading as evidence,
so [THEORY-2262](../theory.d/THEORY-2262.md) gains a `corroborates` edge to this claim ([ADR-093](../decisions.d/ADR-093.md)).

## Note of 2026-11-25: Martin-Löf, read
<!-- inactive-ok-file: THEORY-2307 NOTE-2419 CLAIM-1289 — Proposed or Skimmed; filed for LEAD-215 -->

A parallel on another axis (no edge), from Martin-Löf ([THEORY-2307](../theory.d/THEORY-2307.md);
[NOTE-2419](../notes.d/NOTE-2419.md)). The book separates a set, given by rules that form its
elements, from a category, "grasped" without "exhaustive rules for forming
its objects" (p. 21). This claim asks whether the vocabulary of tests is
closed; [CLAIM-1289](CLAIM-1289.md), filed from the reading, asks whether the
candidates come from a set already given. Each marks where something must
be stated rather than generated. The book bears on neither inference nor
annotation, so it does not test the prediction. No change.
