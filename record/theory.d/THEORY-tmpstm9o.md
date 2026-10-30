---
status: Proposed
title: 'Ill structured problems can be handled by an alternation between a solver working on a problem that is well structured at each moment and a recognition and retrieval system that keeps modifying the problem space from memory or the environment, a serial solver gains nothing by assembling the problem space at the outset, and nothing but the size of the knowledge base may separate ill from well structured problems, so that no qualitatively new mechanisms are needed'
version: 1
tags:
- cognition
- epistemology
date: '2026-10-30'
source:
- LIT-1634
extends:
- THEORY-1084
promote_when: >-
  A system built only from the components Simon names, a solver working in a
  locally well structured problem space and a recognition-driven retrieval
  mechanism that keeps modifying that space from a large memory or from the
  environment, shown to perform on problems of the ill structured kind
  (design under requirements that arrive during the work, with no fixed
  initial solution test) comparably to a system or expert given the full
  specification at the outset, with the gap traced to the size or content of
  its memory and not to a missing mechanism. The converse settles it the
  other way: a class of such problems on which that architecture fails at
  any memory size and a qualitatively different mechanism succeeds. A system
  that solves a problem once someone has formalized it does not count, since
  that is the preparation the claim is about.
summary: >-
  The thesis Simon (1973), [LIT-1634](../literature.d/LIT-1634.md), proposes, kept here when the
  twenty-second status review promoted [THEORY-1084](THEORY-1084.md) as a report of the
  proposal ([ADR-065](../decisions.d/ADR-065.md); [ADR-047](../decisions.d/ADR-047.md), kind 1). The paper describes the architecture,
  matches it to an architect, to battleship design and to a chess program,
  and argues from the seriality of the solver; nothing is built or tested,
  and Simon states the last part as what his analysis "suggests".
---

# THEORY-tmpstm9o: Ill structured problems can be handled by an alternation between a solver working on a problem that is well structured at each moment and a recognition and retrieval system that keeps modifying the problem space from memory or the environment, a serial solver gains nothing by assembling the problem space at the outset, and nothing but the size of the knowledge base may separate ill from well structured problems, so that no qualitatively new mechanisms are needed

## Source

Simon (1973), [LIT-1634](../literature.d/LIT-1634.md), §§3–5 (pp. 187–200); read in [NOTE-1232](../notes.d/NOTE-1232.md). What the
paper argues is [THEORY-1084](THEORY-1084.md), which this entry extends.

## Why it is Proposed

No system of this design is built or run in the paper. Whether the thesis
holds needs such a system to perform on ill structured problems about as
well as one given the full specification, or to fail on them at any memory
size while a different mechanism succeeds.
