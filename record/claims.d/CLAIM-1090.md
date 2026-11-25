---
number: 1090
status: Proposed
formerly:
- CLAIM-tmpf0417
title: 'Seeds are decided by what is forced at binding'
statement: >-
  Whether a seed set helps or hurts is decided by what is forced when each
  component first becomes bound, not by what the constraints force in the
  end, so a predictor of productive nuclei cannot be computed from the
  constraint architecture alone: it must take the order and threshold of
  growth as conditions, since a static closure can be constant where the
  chance of assembly varies most
version: 1
history:
- version: 1
  date: '2026-11-23'
  note: >-
    Filed by the lead run of 2026-11-23 as one of two alternative readings
    of the executed study CASE-389; the other objects to it. The
    filer leans to this one.
role: thesis
warrant: interpretive
defeated_if: >-
  A predictor computed from the constraint architecture alone, with no
  growth order, rate or threshold, that meets CASE-389's registered
  criterion of transfer in its model, or in another system where adding a
  compatible seed can lower the chance of the target. Not defeated by such a
  predictor in a system where seeds never hurt, where a monotone score
  suffices; nor by the objection that the study's system lacks coherent
  alternative branches, which limits the evidence and does not supply the
  predictor.
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-23'
line:
- realizability
- formal-apparatus
rests_on:
- CLAIM-1205
- CLAIM-1204
bears_on:
- QUESTION-380
summary: >-
  Alternative reading A of [CASE-389](../cases.d/CASE-389.md), the one the filer leans to. In
  that study a static closure of the constraints (arc consistency) forced
  the whole target from any seed, every island-based predictor failed, and
  the one that worked counted the states open when each component first
  reached the binding threshold. Read generally: [QUESTION-380](../questions.d/QUESTION-380.md)'s predictor
  "computed from a constraint architecture" needs the growth rule's order
  and threshold among the conditions the question already asks an answer
  to state. Alternative reading B ([CLAIM-1078](CLAIM-1078.md)) objects that the study
  cannot show this for systems with coherent alternative branches. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CASE-389 CLAIM-1205 CLAIM-1204 CLAIM-1078 CLAIM-1085 — new; the study, the claims this reading rests on or cites, and the alternative that objects to it, filed by the lead run of 2026-11-23 -->

# CLAIM-1090: Seeds are decided by what is forced at binding

## The claim

[QUESTION-380](../questions.d/QUESTION-380.md) asks for a predictor "computed from a constraint
architecture", and lists among the conditions an answer must state "the
possibility of backtracking, the order of formation". [CASE-389](../cases.d/CASE-389.md)
suggests the order is not a side condition but the substance:

1. **The static closure is uninformative where it matters.** When the
   constraints have the target as their only solution, arc consistency
   forces it from any seed. In the study's amended model, checked post hoc,
   single-seed arc-consistency islands are 61 to 64 of 64 components on
   every architecture checked, so a predictor built on them is nearly
   constant, while V varies across seed sets from 0 to 0.51.
2. **Islands built forward still miss it.** The forward closure, waiting
   until each component is forced, overstates what the growth forces; the
   failures fall inside islands ([CLAIM-1205](CLAIM-1205.md)).
3. **The predictor that works reads the order.** Counting what is open at
   first threshold transfers to fresh architectures ([CLAIM-1204](CLAIM-1204.md)).

So the effect of a nucleus is a property of the architecture together
with the growth rule. Stern et al.'s own island already says so: it is
what folds correctly "if that subset is cut out and actuated", a dynamic
notion that the record's description of it as "computed from the
constraint structure" ([QUESTION-380](../questions.d/QUESTION-380.md)) passes over.

## Alternatives

Two readings of the study would be filed differently, and both are:

- **A, this claim** (the filer's lean): the order and threshold of growth
  belong in any predictor of productive nuclei.
- **B, [CLAIM-1078](CLAIM-1078.md)**: the study's system lacks the coherent alternative
  branches that self-folding sheets have, so it leaves open whether a
  constraint-only race predictor works where they exist.

The filer leans to A because the study's evidence bears on it directly,
three ways, while B marks a limit of that evidence. The two are compatible
if A is read as a claim about systems like the one tested; they part if A
is read as general. Choosing is the owner's call.

## What it does not say

- That the constraint architecture does not matter: island coverage still
  beats the number of seeds ([CLAIM-1085](CLAIM-1085.md)).
- That TFF is the right predictor beyond this system.
