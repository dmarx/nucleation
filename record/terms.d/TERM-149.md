---
number: 149
status: Proposed
formerly:
- TERM-tmpsu4df
title: 'shared perspective, of a population, as against correlated responses and socially learned norms, evidential reading: members whose interpretive structures are alike, whose interpretive states depend on one another in both directions, and whose uptake of a member''s deviation depends on whether the population''s standard of evidence warrants it'
version: 1
rivals:
- TERM-148
tags:
- social-ontology
- agency
- individuation
date: '2026-11-22'
line:
- distributed-agency
summary: >-
  Filed for [LEAD-087](../leads.d/LEAD-087.md), before any simulation, as the criterion
  [CASE-145](../cases.d/CASE-145.md)'s A4 asked for: what "additional relational
  organization distinguishes a perspective from" correlated responses or
  socially learned norms. Three conditions, each measured by perturbing
  some members and watching the rest: structural concordance (alike),
  cross-member dependence (coupled both ways), and evidential
  answerability (a warranted deviation is taken up, an unwarranted one of
  the same size corrected). Common training passes the first and fails
  the second; unconditional conformity passes two and fails the third.
  [TERM-148](TERM-148.md) is the rival reading of the third condition. The
  wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: TERM-148 — new; the rival reading, filed with this term for LEAD-087 -->
<!-- inactive-ok-file: CLAIM-417 — Proposed; its defeater is cited as the test this term must pass -->
<!-- inactive-ok-file: THEORY-1800 TERM-119 TERM-126 — Proposed; cited for the measurement constraint and to mark what this term is not, nothing here rests on their adoption -->

# TERM-149: shared perspective, of a population, as against correlated responses and socially learned norms, evidential reading: members whose interpretive structures are alike, whose interpretive states depend on one another in both directions, and whose uptake of a member's deviation depends on whether the population's standard of evidence warrants it

## Why it is needed

[CASE-145](../cases.d/CASE-145.md) proposes populations trained alike, some interacting and
some not, with and without a mechanism of collective decision. A4 set
its condition: "a shared perspective will simply mean correlated
responses or socially learned norms. The study only helps the theory if
it specifies, ahead of time, what additional relational organization
distinguishes a perspective from those simpler phenomena." This term is
that specification, written and committed before the simulation of
[LEAD-087](../leads.d/LEAD-087.md) was coded.

It is [TERM-072](TERM-072.md) sense 1 said of several members. A11: interpretations
"belong to a common organizational perspective insofar as their
significance is mutually answerable within an identifiable regime of
contextual selection, evaluation, and possible revision", and A8:
"What unifies the system is not the absence of disagreement. It is the
organization within which disagreement has consequences." Agreement,
however high, is therefore not the test; how disagreement is handled
is.

## Definition

A population of members shares a perspective, in this reading, when all
three hold.

1. **Structural concordance.** The members' interpretive structures, the
   relations among their categories and not only their answers, are
   alike beyond what members trained on different schemas show. This
   follows DeChurch and Mesmer-Magnus ([THEORY-1800](../theory.d/THEORY-1800.md)): structural measures
   of sharedness track team process where agreement measures do not.
   Necessary, not sufficient: common training gives it.
2. **Cross-member dependence, both ways.** Perturb the interpretive
   states of a subset S of members and nothing else. The interpretive
   states of the unperturbed members U then differ from those in an
   otherwise identical run without the perturbation, and S is drawn back
   faster than it would be with the members' interaction removed. This is
   what correlated responses lack: members alike by common training are
   alike without depending on one another, and members who learned their
   norms socially and no longer interact are alike in the same way.
3. **Evidential answerability.** The uptake by U of S's deviation depends
   on whether the population's standard of evidence warrants the
   deviation, not only on how many members carry it. Of two deviations of
   the same size carried by the same S, one warranted (the world the
   population answers to has changed as S changed) and one not, the
   warranted one is taken up by U more than the unwarranted one. This is
   what coordinated feedback in general lacks: a population whose members
   copy one another unconditionally carries both alike, by number.

Condition 3 is where this term and its rival differ. [TERM-148](TERM-148.md)
reads A8's "disagreement has consequences" as restoration of the shared
structure (a deviation is corrected back to the organization rather than
averaged into it), without requiring that the standard be one of
evidence. Which reading the record adopts is the owner's decision.

## How it is measured

For the simulation of [LEAD-087](../leads.d/LEAD-087.md), stated before it was coded.

- A member's interpretive state is its map from situations to
  categories; its interpretive structure is the matrix of relations
  among its categories.
- **Concordance** r is the mean correlation, over pairs of members, of
  their structures. It passes when r exceeds the value for members
  trained on different schemas by at least 0.3.
- A perturbation moves S's state (20% of members) by a fixed size δ in a
  fixed direction. Each perturbed run has a twin with the same random
  numbers and no perturbation.
- **Spillover** s is U's mean displacement from its twin in the
  perturbation's direction, as a fraction of δ, averaged over a window
  after the perturbation; s_w for the warranted perturbation, s_u for the
  unwarranted one. **Recovery** g is how much of δ S has lost, averaged
  over the same window.
- **Condition 2** passes when the larger of s_w and s_u exceeds ε = 0.05,
  and g for the unwarranted perturbation exceeds the same population's g
  with interaction removed by ε.
- **Condition 3** passes when σ = s_w − s_u exceeds ε.
- "Exceeds" means the lower end of a 95% interval over seeds exceeds it.

## What it is not

- **Not agreement.** Members can disagree on many answers and pass; they
  can agree on all and fail condition 2.
- **Not a shared mental model.** [TERM-119](TERM-119.md) is a record's publicly
  inspectable state, and a shared mental model is a property of members'
  heads ([NOTE-1804](../notes.d/NOTE-1804.md)); condition 1 alone is the second.
- **Not collective agency.** Nothing here requires a collective decision,
  a collective action or a goal-directed description of the population
  ([TERM-044](TERM-044.md)). That is the point of [CASE-145](../cases.d/CASE-145.md): the two can then be
  measured apart.
- **Not [TERM-126](TERM-126.md)'s answerability.** That is a normative relation in which
  an actor owes a party an answer. Here "answerable" is A8's
  cross-context answerability: a member's interpretation has
  consequences for the others' under a common standard.

## What would settle it

If, in the study, unconditional conformity passes condition 3, or common
training or socially learned norms pass condition 2, the term does not
make A4's distinction and, by A4's own rule, that counts against the
category. If it makes the distinction, adoption is still the owner's
call, between this reading and [TERM-148](TERM-148.md). It bears on [CLAIM-417](../claims.d/CLAIM-417.md)'s
defeater, that "organizational perspective" cannot be told from
coordinated feedback in general.
