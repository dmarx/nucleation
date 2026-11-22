---
status: Open
title: 'Read an elaborating type system to test whether elaboration or coercion insertion is the update that moves a term to fit the type it is checked against, as the record''s account of specification says'
version: 1
stage: idea
priority: low
method:
- reading
tags:
- logic
date: '2026-11-22'
line:
- formal-apparatus
advances:
- CLAIM-tmpnookt
summary: >-
  Filed from the reading of Dunfield and Krishnaswami (NOTE-tmpbrc1z) for
  LEAD-tmp3xevc. CLAIM-tmpnookt places the performative half of typing in
  elaboration or coercion; the survey only cites the elaboration
  literature, and the one change to a term it treats is the programmer's
  annotation, which changes no behaviour. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpnookt — Proposed; the claim this lead tests -->

# LEAD-tmp7mkn0: Read an elaborating type system to test whether elaboration or coercion insertion is the update that moves a term to fit the type it is checked against, as the record's account of specification says

## What to do

Register and read one elaborating bidirectional system the survey cites:
Dunfield, "Elaborating intersection and union types" (ICFP 2012; Journal
of Functional Programming 24(2–3), 2014), or Dunfield, "Elaborating
evaluation-order polymorphism" (ICFP 2015, arXiv 1504.07680). Ask:

- does elaboration take a source term that checks against a type to a
  target term that differs from it, and is that difference the least the
  type requires, in some order on terms;
- does a coercion inserted at subsumption change what the term does, or
  only its representation;
- is anything in the system moved to fit a type it fails, or does
  elaboration apply only to terms that already check.

## What would count

CLAIM-tmpnookt's elaboration clause confirmed if elaboration moves a term
it applies to, minimally in a stated sense, to fit its type; narrowed if
it applies only to terms that already check, so that it translates rather
than repairs.
