---
number: 224
status: Proposed
formerly:
- CASE-tmpdwka1
title: 'One hidden mode fixed for a run, producing 1, 0, 0 over three periods in one setting and 0, 0, 1 in the other: the realizable observations of periods 1–2 and 2–3 include (1, 0) and (0, 1), which agree on period 2, and no run realizes their pasting (1, 0, 1)'
version: 1
standing: stipulated
kind: construction
tags:
- mathematics
- causality
date: '2026-11-07'
line:
- formal-apparatus
illustrates:
- CLAIM-623
summary: >-
  A29 §4 of the exchange "Individuation, Possibility, and Disposition"
  (2026-11-06 to 07), answering the owner's U13, "flesh this out further".
  A finite system with a hidden mode that cannot change during a run,
  whose observable histories over overlapping periods agree and do not
  paste into a realizable one. A27 §2 gives the same shape with a one-use
  resource. The reader checked it by enumeration. The wording is A's;
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-623 — filed from the same exchange, Proposed -->

# CASE-224: One hidden mode fixed for a run, producing 1, 0, 0 over three periods in one setting and 0, 0, 1 in the other: the realizable observations of periods 1–2 and 2–3 include (1, 0) and (0, 1), which agree on period 2, and no run realizes their pasting (1, 0, 1)

## The case

A29 §4 of the exchange "Individuation, Possibility, and Disposition"
(https://chatgpt.com/share/6aee7a9b-f13c-83e9-a865-6a29c2c3ff7e): "Imagine
a system with one hidden organizational mode, \(m\in\{\alpha,\beta\}\),
that cannot change during the experiment." Mode α produces 1, 0, 0 over
periods 1–3, and mode β produces 0, 0, 1.

- The realizable observations of periods 1–2 are {(1, 0), (0, 0)}, and of
  periods 2–3 are {(0, 1), (0, 0)}.
- (1, 0) and (0, 1) agree on period 2, where both are 0.
- Their pasting (1, 0, 1) is produced by neither mode. "Neither \(\alpha\)
  nor \(\beta\) produces it."

The full histories, mode included, still glue: "full histories cannot be
glued unless their hidden states also agree." What fails is gluing for the
observations once the mode is forgotten. A: "Technically, the pointwise
image of a morphism of sheaves need not itself satisfy the sheaf
condition."

A27 §2 gives the same shape with a consumable resource that suffices for
one performance: "Each is individually feasible, and their visible
histories may agree during a shared idle interval. But the two
performances together may be impossible without replenishing the hidden
resource."

The reader enumerated both modes and confirmed every set above.

## What it can show

That a presheaf of realizable observations can fail to glue over two
overlapping intervals whose union is itself observed ([CLAIM-623](../claims.d/CLAIM-623.md)). It
is a worked instance of [QUESTION-379](../questions.d/QUESTION-379.md): locally realizable, compatible on
the overlap, a coherent string globally, and no realization.

It cannot show how often such failures occur in systems that are not
stipulated, or tell an omitted capacity from a modelling error
([QUESTION-437](../questions.d/QUESTION-437.md)).
