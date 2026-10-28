---
status: Rejected
title: 'The signalling counts read off Wang et al.''s appendix show that signalling is typical of language data'
version: 1
form: evidence
tags:
- mathematical-statistics
- contextuality
date: '2026-10-28'
line: pragmatic-transport
grounds:
- LIT-851
concludes:
- CLAIM-125
summary: >-
  CLAIM-125's version 1 read LIT-851's appendix, "69 of the 90 systems
  signal", as showing that signalling is the typical case for language data
  and that an extension to signalling data is not optional. The counts are
  plug-in estimates from one or a few occurrences per context, which signal
  in expectation even when the true marginals agree. CLAIM-235 undercuts
  the inference; CLAIM-125's version 2 already re-grounded the point.
---
<!-- inactive-ok-file: ADR-061 — Proposed; the decision under whose migration this entry was filed or revised -->
<!-- inactive-ok-file: CLAIM-125 CLAIM-127 — Proposed; the conclusion this argument fails to reach and the claim that repeats the count, open -->

# ARG-tmpwp2hn: The signalling counts read off Wang et al.'s appendix show that signalling is typical of language data

## The inference

Wang, Sadrzadeh, Abramsky and Cervantes (LIT-851) report signalling
measures for 90 systems of ambiguous nouns and verbs. CLAIM-125's version
1: "69 of the 90 systems signal" and "34 signal enough that they cannot be
contextual at all". "So for language data signalling is the typical case,
not an edge case, and an extension to signalling data is not optional."
CLAIM-127 repeats the count.

## Critical questions

- **Would the evidence be expected if the hypothesis were false?** Yes,
  and this is the question that fails. The plug-in signalling Δ̂ is
  "positive in expectation even when the true marginals are equal"
  (CLAIM-235). In a rank-2 system with no signalling and one occurrence
  per context, Δ̂ takes only the values 0, 2 and 4, with expectation 2.
  NOTE-654: "51 of 90 systems have Δ exactly 0, 2 or 4, and 18 have
  err(Δ) = 1.41. Both patterns suggest one or a few occurrences per
  context."
- **Does it tell the hypothesis apart from its rivals?** No. Sampling
  noise from one or a few occurrences predicts the same counts as
  signalling in the population.
- **Does the measure measure what it is said to?** Not for the
  conclusion's population. NOTE-654: the probabilities "are relative
  frequencies of interpretations that the authors assigned by hand to BNC
  and ukWaC occurrences. No annotation protocol or agreement is
  reported." CLAIM-125 spoke of "language data", and the pragmatic thesis
  is about judgements.

## Verdict

Rejected. CLAIM-235: "CLAIM-125's 'not optional' may well be right. Its
stated evidence does not carry it." CLAIM-235 undercuts the inference: the
upward bias of plug-in signalling from few occurrences is a claim about
the subject matter. The argument does not say signalling is rare, nor that
LIT-851's Proposition 1 is wrong (THEORY-177); it is about the counts read
off the appendix.

CLAIM-125's version 2 already conceded the point. It reads the counts as
weak and rests "not optional" on NOTE-235's reading of LIT-264 and on
CLAIM-127's routes to signalling. This argument records the version 1
inference that failed.

Filed 2026-10-28 by the ADR-061 migration, from CLAIM-235.
