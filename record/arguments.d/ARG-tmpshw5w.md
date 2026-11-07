---
status: Proposed
title: "A hidden mode fixed for a run, whose observations over two overlapping periods agree on the overlap and do not paste into a realizable history, shows that a presheaf of realizable observations can fail to glue"
version: 1
form: existence
grounds:
- CASE-tmpdwka1
concludes:
- CLAIM-tmprmy7a
tags:
- mathematics
- causality
date: '2026-11-07'
line:
- realizability
- formal-apparatus
summary: >-
  From A29 §4 of the exchange "Individuation, Possibility, and
  Disposition" (2026-11-06 to 07), with A27 §2, answering the owner's U12
  and U13. The inference from the hidden-mode construction of
  [CASE-tmpdwka1](../cases.d/CASE-tmpdwka1.md) to [CLAIM-tmprmy7a](../claims.d/CLAIM-tmprmy7a.md). Proposed. The case is coherent, and an
  enumeration rerun for this argument confirms it. It separates what the
  claim says comes apart: sections that agree on an overlap, and a
  realization of their union. It shows that [CLAIM-197](../claims.d/CLAIM-197.md)'s "a failure needs
  an overlap carrying sections that disagree" holds only under the sheaf
  hypothesis, and on the same enumeration so does its first clause, that
  sections over contexts that do not overlap always glue. It leaves
  [CLAIM-197](../claims.d/CLAIM-197.md) standing for sheaves, and leaves its clause on covers alone.
  Filed at the owner's review of the filing, which asked for the ARGs it
  omitted. The construction is A's (ChatGPT's). The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmprmy7a CASE-tmpdwka1 — filed from the same exchange, Proposed -->

# A hidden mode fixed for a run, whose observations over two overlapping periods agree on the overlap and do not paste into a realizable history, shows that a presheaf of realizable observations can fail to glue

## The inference

1. [CASE-tmpdwka1](../cases.d/CASE-tmpdwka1.md): "Imagine a system with one hidden organizational mode,
   \(m\in\{\alpha,\beta\}\), that cannot change during the experiment."
   Mode α produces 1, 0, 0 over periods 1–3 and mode β produces 0, 0, 1.
2. The realizable observations of periods 1–2 are {(1, 0), (0, 0)}, and
   of periods 2–3 are {(0, 1), (0, 0)}. The observations (1, 0) and
   (0, 1) agree on period 2.
3. Their pasting (1, 0, 1) is realized by no run: "Neither \(\alpha\) nor
   \(\beta\) produces it." The union, periods 1–3, is itself an observed
   context.
4. So the presheaf of realizable observations fails the gluing axiom on a
   cover whose overlap carries agreeing sections, while the sheaf of full
   histories, mode included, glues ([CLAIM-tmprmy7a](../claims.d/CLAIM-tmprmy7a.md)).

## Critical questions

- **Is the case coherent?** Yes. An enumeration rerun for this argument
  over every two-member cover of an interval by subintervals confirms
  steps 2 and 3. The presheaf is separated, since it is a subpresheaf of
  the sheaf of observed strings, so it is gluing that fails, as the claim
  says. The enumeration also finds a failure the case does not mention:
  (0, 0) on periods 1–2 and (0, 0) on periods 2–3 agree on period 2, and
  (0, 0, 0) is realized by neither mode.
- **Does it separate the very things the conclusion says can come
  apart?** Yes. The claim says two observed histories "can each be
  realizable and agree on their overlap with no realization of their
  union", where the union is observed. The case has exactly that, on the
  cover {1–2, 2–3} of 1–3. It is not [CLAIM-131](../claims.d/CLAIM-131.md)'s kind of obstruction,
  where the union of the contexts is never measured. There a compatible
  family glues by definition, and what fails is extension past the
  observed contexts.
- **What it shows about [CLAIM-197](../claims.d/CLAIM-197.md)'s wording.** [CLAIM-197](../claims.d/CLAIM-197.md)'s "a failure
  needs an overlap carrying sections that disagree" is, for a sheaf, the
  contrapositive of the gluing axiom, and [CLAIM-197](../claims.d/CLAIM-197.md) states it of sheaves.
  The case shows that the sheaf hypothesis carries it. Read as a statement
  about any family of realizable observations, the clause is false: here
  the overlap carries sections that agree and they fail to glue. The case
  reaches [CLAIM-197](../claims.d/CLAIM-197.md)'s first clause as well. On the same enumeration,
  (1) on period 1 and (0, 1) on periods 2–3 cover 1–3 with no overlap at
  all and paste to (1, 0, 1), which neither mode produces. So "Sections
  over contexts that do not overlap always glue" also fails for this
  presheaf. That disjoint cover is available only because the periods are
  discrete. With open intervals of continuous time, a connected interval
  has no cover by two disjoint members. The overlapping failure does not
  depend on discreteness. A two-period variant, one mode producing 1, 1
  and the other 0, 0, has failures only on the disjoint cover {1}, {2}.
  The claim's title says less than the case shows: a gluing failure need
  not show a disagreement on an overlap, and need not have an overlap.
- **What it does not touch.** [CLAIM-197](../claims.d/CLAIM-197.md) as a theorem about sheaves. Its
  argument, that for a cover with empty overlap "the compatibility
  hypothesis has nothing to compare, and the sheaf condition gives a
  unique section", stands. Its verdict on "tall", one global section with
  the comparison class part of the meaning, is about a sheaf model of
  meaning and is untouched. Its last clause, that "which families count
  as covers decides whether anything glues", is borne out: the failure
  here exists because {1–2, 2–3} counts as a cover of 1–3. What the case
  bears on is the scope of a reading. Where the record models
  observations of a system with a hidden mechanism, the object is the
  image presheaf. [CLAIM-197](../claims.d/CLAIM-197.md) does not reach it, nor does [CLAIM-153](../claims.d/CLAIM-153.md)'s
  "two locally consistent personas that agree on their overlap always
  glue", until a sheaf is shown.

Proposed. The case is coherent and separates what the claim says comes
apart. If the claim is adopted, it could also say that the disjoint
failure holds on discrete periods.

## What it does not show

- How often such failures occur in systems that are not stipulated.
- Whether a given failure reveals an omitted capacity or a modelling
  error ([QUESTION-tmp2p196](../questions.d/QUESTION-tmp2p196.md)). A: "inconsistency can also come from modeling
  errors or an incorrect assumption that two observations belong to the
  same system".
