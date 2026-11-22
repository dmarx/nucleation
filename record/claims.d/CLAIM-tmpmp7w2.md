---
status: Proposed
title: 'Whether a specification can be read off what it specifies or must be stated in advance depends on whether its vocabulary of tests is closed: over a finite declared vocabulary the strongest description an object passes is computable, so describing can be left to inference, while over an open one no strongest description need exist and what the object is to satisfy must be written down'
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
- THEORY-tmp1mruk
- THEORY-tmpei9b5
complements:
- CLAIM-tmpnookt
- CLAIM-tmpvq4ru
uses:
- TERM-tmp8b1yl
summary: >-
  Offered by the Davies and Pfenning reader as something only the two
  readings together show, and filed under the dialectic regime,
  2026-11-22. Freeman and Pfenning declare a finite lattice of refinements
  and infer everything ([THEORY-tmp1mruk](../theory.d/THEORY-tmp1mruk.md)); Davies and Pfenning let
  refinements combine freely, find inference "most likely undecidable",
  and have the programmer state types ([THEORY-tmpei9b5](../theory.d/THEORY-tmpei9b5.md)). Two systems are a
  contrast, not a test; the Liquid Types reading under [LEAD-tmp3xevc](../leads.d/LEAD-tmp3xevc.md), whose
  qualifiers are a finite set chosen to keep inference decidable, is the
  third. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp1mruk THEORY-tmpei9b5 — Proposed; the readings and claims this is stated against -->

# CLAIM-tmpmp7w2: Whether a specification can be read off what it specifies or must be stated in advance depends on whether its vocabulary of tests is closed: over a finite declared vocabulary the strongest description an object passes is computable, so describing can be left to inference, while over an open one no strongest description need exist and what the object is to satisfy must be written down

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
