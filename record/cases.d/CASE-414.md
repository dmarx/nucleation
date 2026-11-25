---
number: 414
status: Proposed
formerly:
- CASE-tmppqt0f
title: 'A generator that reaches the right answer in about one sample of a hundred, paired with a verifier that checks answers but cannot produce them: under a budget of a few hundred samples the composite answers reliably and neither part does'
version: 1
standing: fictional
kind: thought-experiment
tags:
- epistemology
- learning-theory
- agency
date: '2026-11-23'
line:
- learned-structure
- distributed-agency
variant_of:
- CASE-400
bears_on:
- QUESTION-493
draws_on:
- THEORY-1894
summary: >-
  The eighth of the set [LEAD-001](../leads.d/LEAD-001.md) asks for, on where the knowing sits. A
  model proposes factorizations of twelve-digit numbers and is right about
  one time in a hundred; a checker multiplies the factors back and accepts
  or rejects, but cannot propose any. Sampled up to 460 times and filtered
  by the checker, the pair is right 99% of the time. It alters
  [CASE-400](CASE-400.md) in two respects: the task has an exact cheap check, and
  the check is added. The construction is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-697 TERM-079 — Proposed; cited as the criteria applied, not relied on -->
<!-- inactive-ok-file: CASE-400 CLAIM-1109 CLAIM-1142 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-414: A generator that reaches the right answer in about one sample of a hundred, paired with a verifier that checks answers but cannot produce them: under a budget of a few hundred samples the composite answers reliably and neither part does

## The case

The task: given a twelve-digit number that is the product of two six-digit
primes, name the primes.

- **G**, a language model, proposes a pair per sample. About one sample
  in a hundred is the right pair, the rest scattered as in [CASE-400](CASE-400.md).
- **V**, a checker, multiplies a proposed pair and accepts it if the
  product matches and both factors pass a primality test. It is exact,
  and it has no way to propose a pair.
- **G+V**, the declared composite with a budget of N samples: sample from
  G until V accepts or N is spent, and answer with the accepted pair.

With per-sample success p = 0.01, the composite succeeds with probability
1 − (1 − p)^N, which passes 99% at N = 459. Its answers are then right
whenever it gives one, since V is exact.

## What it separates

- **G**: correct output without reliability, generative reach.
- **V**: a capacity to check without a capacity to answer. It knows of a
  pair whether it is right; it cannot produce the answer to the question.
- **G+V under budget N**: reliable correct output, grounded by V's
  check, which depends on what makes the answer true (the product) and on
  nothing else. On A73's criteria it knows the factors, and neither part
  does.

## Against the candidate answers

[QUESTION-493](../questions.d/QUESTION-493.md)'s candidate (A73) says one correct response among many
samples is generative reach and that knowledge "may belong to the
composite of generator and verifier or of model and tool". The case
agrees and fixes the condition: the composite knows only under a declared
budget, since below a few dozen samples it is unreliable. That is
[CLAIM-697](../claims.d/CLAIM-697.md)'s resource-conditional disposition, with V converting coverage
into delivered success. [THEORY-1894](../theory.d/THEORY-1894.md) is the documented pattern: with
automatic verification, coverage turns into solved problems as samples
grow; without it, majority voting and reward-model selection plateau far
below coverage. Whether the composite believes, in [TERM-079](../terms.d/TERM-079.md)'s sense, is
left open: it uses the accepted pair as its answer, but draws no further
inferences from it in this setup.

## What it can show

That knowledge can sit in a declared composite under a budget and in
neither part, which [CLAIM-1109](../claims.d/CLAIM-1109.md) states. Being fictional, nothing about
any real system's p. One of the separations [CLAIM-1142](../claims.d/CLAIM-1142.md) collects.
