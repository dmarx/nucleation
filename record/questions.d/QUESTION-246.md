---
number: 246
status: Answered
formerly:
- QUESTION-tmp62dpv
title: 'In quantum theory, what does a failure of Kochen–Specker noncontextuality refute, as against a failure of Spekkens''s generalized noncontextuality, and which of the two notions is broader?'
version: 1
tags:
- contextuality
- quantum-foundations
date: '2026-10-21'
line: pragmatic-transport
refines:
- QUESTION-067
summary: >-
  The conceptual part of [QUESTION-067](QUESTION-067.md), split off under [ADR-049](../decisions.d/ADR-049.md) and
  answered by [THEORY-011](../theory.d/THEORY-011.md), [THEORY-015](../theory.d/THEORY-015.md), [THEORY-016](../theory.d/THEORY-016.md), [THEORY-231](../theory.d/THEORY-231.md) and
  [THEORY-559](../theory.d/THEORY-559.md). A Kochen–Specker proof refutes measurement noncontextuality
  together with outcome determinism, and so universal generalized
  noncontextuality. A generalized no-go refutes a positive quasiprobability
  representation, and Leibnizian representations within classical
  realism. The generalized notion is strictly broader. Which notion a
  test of pragmatic judgements can reach stays with [QUESTION-067](QUESTION-067.md).
answered_by:
- THEORY-011
- THEORY-015
- THEORY-016
- THEORY-231
- THEORY-559
---

# QUESTION-246: In quantum theory, what does a failure of Kochen–Specker noncontextuality refute, as against a failure of Spekkens's generalized noncontextuality, and which of the two notions is broader?

## Answer

This is the part of [QUESTION-067](QUESTION-067.md) that asks "what each would show if it
failed", split off on 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)). Five Active THEORYs answer
it.

- **What a Kochen–Specker failure refutes.** [THEORY-015](../theory.d/THEORY-015.md), from Spekkens
  2005 ([LIT-266](../literature.d/LIT-266.md)). Kochen–Specker noncontextuality is measurement
  noncontextuality plus outcome determinism for sharp measurements, and
  preparation noncontextuality implies that determinism. So every
  Kochen–Specker proof refutes universal generalized noncontextuality,
  that is, preparation and measurement noncontextuality together.
  Measurement noncontextuality alone is consistent with quantum theory.
- **The same failure, read as random variables.** [THEORY-559](../theory.d/THEORY-559.md). If each
  measurement is one random variable in every context, all of them
  already sit on one probability space. A Kochen–Specker or Bell
  contradiction then refutes that context-independent identification,
  not the existence of a joint distribution.
- **What a generalized failure refutes.** [THEORY-016](../theory.d/THEORY-016.md): a generalized
  noncontextual model exists exactly when the theory's GPT has a positive
  quasiprobability representation, so a failure rules that out.
  [THEORY-231](../theory.d/THEORY-231.md): within classical realism, such a no-go refutes Leibnizian
  representations, not realist ones as such.
- **Which is broader.** The generalized notion, strictly. [THEORY-011](../theory.d/THEORY-011.md): a
  qubit has no preparation-noncontextual model, though no
  Kochen–Specker argument with sharp measurements exists in dimension
  two. [THEORY-231](../theory.d/THEORY-231.md) adds that a generalized no-go applies where no
  Bell-like one exists, as in prepare-measure scenarios.

## Limits

[THEORY-015](../theory.d/THEORY-015.md)'s implication uses quantum theory's full preparation set, and
must be re-checked in a fragment. Its statement for the sheaf form is the
record's own join, not a source's. [THEORY-559](../theory.d/THEORY-559.md) notes that the sheaf
account and the random-variable one agree under consistent
connectedness. [THEORY-011](../theory.d/THEORY-011.md)'s qubit proof assumes exact operational
equivalence and perfectly distinguishable pairs. [THEORY-231](../theory.d/THEORY-231.md) rests on a
Skimmed reading, and proves only that Leibnizian implies noncontextual.

## What it leaves to [QUESTION-067](QUESTION-067.md)

The answer is about the notions. It does not say which one a test of
pragmatic judgements would reach. That turns on whether the record's
probe families make two renderings operationally equivalent, which needs
them to be tomographically complete for the renderings. [THEORY-315](../theory.d/THEORY-315.md)'s
witness, which needs exact equivalence over every probe, stays with the
parent.
