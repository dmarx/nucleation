---
number: 408
status: Proposed
formerly:
- CASE-tmpk3qls
title: 'Probe-decodable fact the model contradicts'
statement: >-
  A fact a linear probe reads from a model's activations almost without
  error, while the model's answers and its further inferences use a contrary
  value: information stored and decodable, neither believed nor delivered
version: 1
standing: fictional
kind: thought-experiment
tags:
- epistemology
- learning-theory
- representation-learning
date: '2026-11-23'
line:
- learned-structure
bears_on:
- QUESTION-493
draws_on:
- THEORY-1024
summary: >-
  The first of the set [LEAD-001](../leads.d/LEAD-001.md) asks for, separating stored information
  from belief, correct output and knowledge. A linear probe trained on a
  model's activations reads a fact (a city's country) correctly almost
  every time, while the model answers with another country and reasons
  from that one. The information is in the weights; the system does not
  use it. The construction is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-371 CASE-357 CASE-271 TERM-079 — Proposed; cited as related or as the criterion applied, not relied on -->
<!-- inactive-ok-file: CASE-413 CLAIM-1100 CLAIM-1142 — Proposed; filed by the lead run of 2026-11-23 -->

# CASE-408: Probe-decodable fact the model contradicts

## The case

A language model has seen, in training, many documents placing the city
Ardel in country P, and a smaller number, from one prolific source,
placing it in country Q. Asked "Which country is Ardel in?", it answers Q
in nearly every sample. Asked questions whose answers depend on it (the
currency used in Ardel, the language of its street signs, the flight
time from Ardel to P's capital), it answers as if Ardel were in Q.

A linear probe is fitted on the model's middle-layer activations at the
token "Ardel", using other cities whose countries are known as training
data. On Ardel it reads P, with the probe's held-out accuracy on other
cities above 99%. Ablating the direction the probe uses changes nothing
in the model's answers about Ardel. P is true.

Held fixed: the model, its weights, its default decoding. What varies is
only who reads the activations: the model's own downstream computation or
the outside probe.

## What it separates

- **Stored information without belief.** The information that Ardel is in
  P is present and recoverable. By [TERM-079](../terms.d/TERM-079.md)'s probes (anticipation,
  inferential generalization, epistemic intervention) the model believes
  Q: Q is what it uses as a premise.
- **Stored true information without correct output or knowledge.** The
  true content is stored; the output is wrong; nothing the system does
  depends on what it stores.

## Against the candidate answers

[QUESTION-493](../questions.d/QUESTION-493.md)'s candidate (A73) says that "a fact buried in a gigantic
database and inaccessible to every permitted retrieval procedure should
not automatically count". The case agrees, and sharpens it: the fact here
is not buried in the sense of costly to find. A cheap procedure finds it.
What makes it not known is that no procedure of the declared system uses
it. If the probe is declared part of the system, the composite model plus
probe outputs P reliably, while the model's own inferences still run on
Q, so the composite's answer and its inferences disagree. That is the
point [CLAIM-1100](../claims.d/CLAIM-1100.md) makes: knowing is relative to the declared system
and budget, and decodability alone makes information stored, not known.
A73's fourth test, intervention on the supposed mechanism, is what shows
the direction is not used: ablating it changes nothing.

## Related held cases

The record's executed toy studies hold real versions of the same split:
[CASE-371](CASE-371.md) (facts fine-tuned away stay recoverable by a probe, a cue or
the runner-up answer), [CASE-357](CASE-357.md) (a trigger decodable and recruited
after its behaviour is never expressed) and [CASE-271](CASE-271.md) (readout
suppression and deletion that read alike at the original query).
[THEORY-1024](../theory.d/THEORY-1024.md) is the caution on the other side: where causal tracing
localizes a fact barely predicts where editing it succeeds, so a located
representation is not thereby the one the system uses.

## What it can show

That stored information and belief come apart coherently, as one of the
separations [CLAIM-1142](../claims.d/CLAIM-1142.md) collects. Being fictional, nothing about how
often real models are in this state. [CASE-413](CASE-413.md) is the contrast: there
the model's own procedures do use the stored fact, under one cue.
