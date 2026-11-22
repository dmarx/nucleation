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
title: 'Dunfield and Krishnaswami show that bidirectional typing splits typing into checking a term against a type given as input and synthesizing a type from the term as output, a split of information flow, which part of a judgment is known, assigned rule by rule so that no type is guessed (introductions checked and eliminations synthesized in the Pfenning recipe), with the two meeting where a synthesized type is tested against a required one, and with the term an input in both'
version: 1
tags:
- logic
date: '2026-11-22'
source:
- LIT-tmpqagik
corroborates:
- CLAIM-tmpnookt
summary: >-
  From the reading of LIT-tmpqagik in NOTE-tmpbrc1z, for LEAD-tmp3xevc. The modes are
  information flow (§1, §3.1, §8.4); the recipe assigns them (§4); the
  change of direction is a test, subsumption, of the synthesized "fact"
  against the checked "requirement" (§4.4). It corroborates the
  fact-and-requirement reading of the two modes in CLAIM-tmpnookt, which
  ARG-tmpcpo8g narrows. Proposed until its promote_when is met.
---
<!-- inactive-ok-file: CLAIM-tmpnookt — Proposed; the claim this reading bears on -->

# THEORY-tmptsz1u: Dunfield and Krishnaswami show that bidirectional typing splits typing into checking a term against a type given as input and synthesizing a type from the term as output, a split of information flow, which part of a judgment is known, assigned rule by rule so that no type is guessed (introductions checked and eliminations synthesized in the Pfenning recipe), with the two meeting where a synthesized type is tested against a required one, and with the term an input in both

## Source

Dunfield and Krishnaswami (2021), LIT-tmpqagik, read in NOTE-tmpbrc1z.

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
