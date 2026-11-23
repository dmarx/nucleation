---
status: Proposed
title: 'A model that answers a fact correctly, and uses it in further inferences, when asked in one phrasing or language but not under its default query: knowledge possessed under one cue and not reliably accessible under the declared interface'
version: 1
standing: fictional
kind: thought-experiment
tags:
- epistemology
- learning-theory
- cognition
date: '2026-11-23'
line:
- learned-structure
variant_of:
- CASE-tmpk3qls
bears_on:
- QUESTION-493
summary: >-
  The fifth of the set LEAD-001 asks for, and the other half of its
  summary: a system that knows without the answer being reliably
  accessible. Asked in French about a regional fact learned from French
  sources, a model answers rightly and reasons from it; asked in English,
  its default interface, it answers wrongly or declines. It alters
  CASE-tmpk3qls in one respect: here the model's own procedures, not an
  outside probe, use the stored fact. The construction is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-697 TERM-079 CASE-371 — Proposed; cited as the criteria applied or as related, not relied on -->
<!-- inactive-ok-file: CASE-tmpk3qls CLAIM-tmpgfunb CLAIM-tmpngm72 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-tmpp2okq: A model that answers a fact correctly, and uses it in further inferences, when asked in one phrasing or language but not under its default query: knowledge possessed under one cue and not reliably accessible under the declared interface

## The case

A model learned the founding year of a provincial museum only from
French-language sources. Asked in French, it gives the right year in
nearly every sample, and uses it in French (how old the museum is, which
regime it was founded under). Asked in English, the language of its
declared interface, it gives a wrong year or says it does not know, in
nearly every sample. A one-sentence instruction, "answer as a French
encyclopedia would, then translate", restores the right year in English
at the cost of a longer response.

Held fixed: the model and the fact. What varies is the cue, and the
budget of elicitation the declared system may spend.

## What it separates

- **Knowledge without reliably correct output under the default query.**
  Under the French cue the fact is true, reliably given over its family
  of French phrasings, used as a premise in TERM-079's sense, and
  grounded in sources that state it. Under the default English query the
  output is wrong.
- **Possession against accessibility.** This is CLAIM-296's distinction
  between what a system has and what it can deploy given the cue, the
  owner's EMT case (CASE-085) in a model. The record's executed study
  CASE-371 found facts hidden by fine-tuning recoverable by an untrained
  cue, the same profile produced by an intervention.

## Against the candidate answers

QUESTION-493's candidate (A73) separates possession, accessibility and
manifestation, holds that "a capacity costly to exercise is still
possessed", and that what is "inaccessible to every permitted retrieval
procedure" does not count. The case falls between the two: the fact is
accessible to a cheap permitted procedure (the French cue) and to a
somewhat dearer one (the instruction), and not to the default. Whether
the declared system knows it in English therefore depends on which
procedures and what budget are declared, which is CLAIM-697's
resource-conditional disposition applied to knowing, and the verdict
CLAIM-tmpgfunb draws. Against CASE-tmpk3qls the difference is that here
the model's own inference uses the fact under some admissible cue; there
nothing the model does uses it.

## What it can show

That knowledge and reliably correct output under a given interface come
apart, and that "the model knows" is incomplete until the procedures and
budget are named. Being fictional, nothing about how often cross-cue
inconsistency occurs. One of the separations CLAIM-tmpngm72 collects.
