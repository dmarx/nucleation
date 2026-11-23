---
number: 400
status: Proposed
formerly:
- CASE-tmpd1jgy
title: 'A model that answers a question correctly once in two hundred samples and otherwise scatters its answers with no stable preference: a correct output that is generative reach, neither believed nor known'
version: 1
standing: fictional
kind: thought-experiment
tags:
- epistemology
- learning-theory
date: '2026-11-23'
line:
- learned-structure
bears_on:
- QUESTION-493
draws_on:
- THEORY-1894
summary: >-
  The second of the set [LEAD-001](../leads.d/LEAD-001.md) asks for, separating a correct output
  from belief, reliability and knowledge. Sampled two hundred times on a
  hard arithmetic question, a model gives the right answer once and
  spreads the rest over many wrong ones, none preferred. Read at the
  sample that was right, the output is correct; nothing in the system
  holds it. The construction is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-697 TERM-079 — Proposed; cited as the criteria applied, not relied on -->
<!-- inactive-ok-file: CASE-414 CLAIM-1109 CLAIM-1142 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-400: A model that answers a question correctly once in two hundred samples and otherwise scatters its answers with no stable preference: a correct output that is generative reach, neither believed nor known

## The case

A model is asked for the product of two four-digit numbers. At
temperature 1 it is sampled two hundred times. One sample gives the
correct product. The other 199 give about 150 distinct wrong products,
the most frequent of them three times. The correct product is no more
frequent than a typical wrong one; its probability under the model is
about 0.005. Asked afterwards whether the correct product is right, the
model says yes and no about equally often. An evaluator who sees only the
one correct sample would score the model correct.

Held fixed: the model and the question. What varies is which sample is
read, and whether one or all are.

## What it separates

- **Correct output without belief.** No answer is used as a premise
  across the model's further inferences in [TERM-079](../terms.d/TERM-079.md)'s sense; the correct
  one has no standing among the others.
- **Correct output without reliability, and so without knowledge.** The
  output is right by the draw. Over the declared family (this question,
  resampled) the success rate is 0.005.

## Against the candidate answers

[QUESTION-493](../questions.d/QUESTION-493.md)'s candidate (A73) says one correct response in many samples
is "evidence of generative reach", not knowledge, which is [CLAIM-697](../claims.d/CLAIM-697.md)'s
coverage against delivery. The case agrees on every criterion A73 lists:
true, but not reliable over the declared family, and not grounded, since
nothing in the model's processing distinguishes the right product from
the wrong ones (A73's first test, reliability, already fails; the others
need not be run). [THEORY-1894](../theory.d/THEORY-1894.md) is the documented pattern at scale:
coverage rises with samples while selection without a verifier plateaus
far below it.

## What it can show

That a correct output is not evidence of belief or knowledge without its
distribution. Being fictional, nothing about how common the profile is.
[CASE-414](CASE-414.md) adds a verifier to a generator like this one, and asks where
the knowing then sits ([CLAIM-1109](../claims.d/CLAIM-1109.md)). One of the separations
[CLAIM-1142](../claims.d/CLAIM-1142.md) collects.
