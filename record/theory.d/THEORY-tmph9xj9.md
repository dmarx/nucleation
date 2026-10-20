---
status: 'Proposed'
promote_when: 'A reading of the analytic treatment of the same model (Amit, Gutfreund and Sompolinsky 1985 and 1987, or an equivalent) or of a later simulation at N in the thousands, confirming that random patterns stored by the outer-product rule are attractors with basins of nonzero width up to a load proportional to N, near 0.14–0.15N, and that recall then collapses for all patterns rather than degrading pattern by pattern; and, for the forgetting clause, a model with decaying or saturating couplings shown to keep recent patterns retrievable at any number stored. It is refuted if the capacity scaling fails at large N, if the large-N basins shrink to zero width at any load, or if bounded couplings fail to prevent the collapse. A further simulation at N = 30 or 100 cannot settle it.'
title: 'A network of N threshold units with symmetric Hebbian couplings stores random patterns as attractors up to a load proportional to N, about 0.15N for all large N, past which recall fails for every pattern at once, and a provision for forgetting old memories, such as couplings that saturate, keeps the most recent ones retrievable however many are added'
version: 1
tags:
- complex-systems
- neuroscience
- cognition
date: '2026-10-20'
source:
- LIT-918
summary: >-
  The large-N and forgetting clauses that [THEORY-272](THEORY-272.md)'s title carried before the promotion audit (batch 051) narrowed it to Hopfield's simulations at N = 30 and 100. Hopfield (1982), [LIT-918](../literature.d/LIT-918.md), expects the 0.15N figure "for all large N" from a crosstalk estimate, and states in words that overload makes every memory irretrievable unless old ones are forgotten, with saturating couplings as the mechanism. Filed under [ADR-047](../decisions.d/ADR-047.md) v4.
extends:
- THEORY-272
answers:
- QUESTION-201
---


# THEORY-tmph9xj9: A network of N threshold units with symmetric Hebbian couplings stores random patterns as attractors up to a load proportional to N, about 0.15N for all large N, past which recall fails for every pattern at once, and a provision for forgetting old memories, such as couplings that saturate, keeps the most recent ones retrievable however many are added

## Source

Hopfield (1982), [LIT-918](../literature.d/LIT-918.md), read in full in [NOTE-819](../notes.d/NOTE-819.md). The crosstalk on a
bit is approximately Gaussian for large nN (Eq. 10), and the retention
seen at n = 0.15N "is expected to be true for all large N". On overload
(p. 2557): "the addition of new memories beyond the capacity overloads
the system and makes all memories irretrievable unless there is a
provision for forgetting old memories"; with couplings saturating at 0,
±1, ±2, ±3, only recent memories stay stable.

## What is asserted, and by whom

Two things, both Hopfield's: that capacity scales with N at about 0.15N
for large networks, with collapse for all patterns past it; and that
forgetting, by saturating couplings, prevents that collapse for recent
memories. The first rests on an estimate, the second on a statement with
no figure.

## What the record holds toward it

- [THEORY-272](THEORY-272.md) (Active): the simulations at N = 30 and 100, with recall
  degrading near 0.15N, fusion of a pattern placed 10 bits from another at
  N = 100, and no pattern stable at 25-fold overload; the energy
  argument and the crosstalk estimate checked.
- The analytic literature the promote_when names (not read here) is
  widely cited for a capacity near 0.138N at large N. If the record reads
  it, the figure in the title may need that correction.

## What would confirm or reject it

The large-N treatment and a bounded-coupling model, as the promote_when
says. [QUESTION-201](../questions.d/QUESTION-201.md) asks the capacity half as a question.
