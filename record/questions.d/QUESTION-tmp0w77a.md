---
status: Open
title: 'Measured on another game, or on Hex with a standard AlphaZero implementation or larger networks, is the iso-strength trade between training compute and tree-search compute again a straight line in log–log space ending at a one-node search, and is its slope, reported with its uncertainty and with test-time compute in a stated unit, within error of Jones''s −1.2?'
version: 1
tags:
- learning-theory
date: '2026-10-30'
line: distributed-agency
summary: >-
  The promotion condition formerly on [THEORY-342](../theory.d/THEORY-342.md), moved here when the
  status review of 2026-10-30 promoted it under [ADR-065](../decisions.d/ADR-065.md). Jones measured
  one game with one nonstandard implementation and gave no uncertainty on
  the slope, and he asks twice for the test on other games.
---

# QUESTION-tmp0w77a: Measured on another game, or on Hex with a standard AlphaZero implementation or larger networks, is the iso-strength trade between training compute and tree-search compute again a straight line in log–log space ending at a one-node search, and is its slope, reported with its uncertainty and with test-time compute in a stated unit, within error of Jones's −1.2?

## Why it is a question

[THEORY-342](../theory.d/THEORY-342.md) reports Jones's exchange rate ([LIT-1069](../literature.d/LIT-1069.md), read in [NOTE-884](../notes.d/NOTE-884.md)): on
9×9 Hex, at fixed Elo, about 15× less search for each 10× more training,
down to a one-node search. It is one game, small boards, a modified
AlphaZero with small fully connected networks, and no standard errors on
the fitted coefficients. Whether the trade is a property of search against
training in general, or of this implementation, is open.

## What would answer it

The same iso-performance measurement (training compute against search
compute at fixed strength) made on another game, or on Hex with a standard
AlphaZero implementation or larger networks, with the slope reported with
its uncertainty and the unit of test-time compute stated. A straight line in
log–log space ending at a one-node floor would generalize the trade; a
bending curve, or a slope that differs beyond the reported uncertainty,
would confine it to Hex or to this implementation. More snapshots of the
same 9×9 runs, or a refit of the same data in another functional form,
cannot settle it.
