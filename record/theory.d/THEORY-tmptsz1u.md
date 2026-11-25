---
status: Proposed
promote_when: >-
  Checked against one primary source the survey summarizes, Dunfield and
  Pfenning (2004) or Pierce and Turner (2000): that checking takes the
  type as an input and synthesis returns it as an output, that the
  recipe's assignment (introductions checked, eliminations synthesized)
  is mode-correct, and that subsumption and annotation are the only rules
  that change direction. Restatements in other surveys or textbooks do
  not count.
title: 'Bidirectional typing splits checking and synthesis'
statement: >-
  Dunfield and Krishnaswami show that bidirectional typing splits typing
  into checking a term against a type given as input and synthesizing a type
  from the term as output, a split of information flow, which part of a
  judgment is known, assigned rule by rule so that no type is guessed
  (introductions checked and eliminations synthesized in the Pfenning
  recipe), with the two meeting where a synthesized type is tested against a
  required one, and with the term an input in both
version: 1
tags:
- logic
date: '2026-11-22'
source:
- LIT-tmpqagik
corroborates:
- CLAIM-949
summary: >-
  From the reading of [LIT-tmpqagik](../literature.d/LIT-tmpqagik.md) in [NOTE-tmpbrc1z](../notes.d/NOTE-tmpbrc1z.md), for [LEAD-215](../leads.d/LEAD-215.md). The modes are
  information flow (§1, §3.1, §8.4); the recipe assigns them (§4); the
  change of direction is a test, subsumption, of the synthesized "fact"
  against the checked "requirement" (§4.4). It corroborates the
  fact-and-requirement reading of the two modes in [CLAIM-949](../claims.d/CLAIM-949.md), which
  [ARG-tmpcpo8g](../arguments.d/ARG-tmpcpo8g.md) narrows. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: CLAIM-949 — Proposed; the claim this reading bears on -->
<!-- inactive-ok-file: ARG-tmpcpo8g — Proposed; the reading of Dunfield and Krishnaswami (2021) and the entries filed from it, or the entries it bears on -->

# THEORY-tmptsz1u: Bidirectional typing splits checking and synthesis

## Source

Dunfield and Krishnaswami (2021), [LIT-tmpqagik](../literature.d/LIT-tmpqagik.md), read in [NOTE-tmpbrc1z](../notes.d/NOTE-tmpbrc1z.md).

## What was actually shown

A survey's synthesis, with small worked results of its own: the eight
direction assignments of →-elimination and which four are mode-correct
(§3), the recipe applied to the simply typed λ-calculus (§2, §4), its
size and annotatability argued (§4.5), and a backwards system for linear
logic with a substitution theorem (§6.5). The rest restates the cited
literature.

## What this does not say

- Not what a checker does on failure beyond rejecting, nor that
  bidirectional typing improves error messages, which is asserted
  (abstract, §10) and not shown.
- Not how elaboration or coercion relate to checking; the survey cites
  them and does not treat them.
- Not that the recipe is the only design: the survey shows mixed,
  combined and reversed modes (§6).
