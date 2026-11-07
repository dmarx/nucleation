---
number: 182
status: Active
formerly:
- CASE-tmpasrij
title: 'Two operators under one update rule, grants moving toward observed outcomes: scored every round, the more accurate one holds the lead durably whatever the start; scored only when it acts, under sharp selection, whichever gained influence early keeps it'
version: 2
history:
- version: 2
  date: '2026-11-04'
  note: >-
    Vocabulary only, under ADR-070: "endorse" in TERM-053's sense now
    reads conferral (TERM-103) or grant (TERM-101). The
    content is unchanged.
standing: fictional
kind: construction
tags:
- self-governance
- social-ontology
line: distributed-agency
date: '2026-10-28'
summary: >-
  Filed by the fourth status review ([ADR-057](../decisions.d/ADR-057.md)) for [CLAIM-277](../claims.d/CLAIM-277.md), whose two
  loops the record had stated and not constructed. Two operators share one
  rule, with accuracies 0.8 and 0.6. Each round one acts, chosen with
  probability softmax(β·E), and the grant moves toward observed outcomes,
  E ← E + η(outcome − E). Nothing marks either one as an authority. Scored
  every round, the more accurate one ends with the larger grant in 200 of 200
  seeds, even after a head start for the other (E0 = 0.3 against 0.9). With
  η = 0.01 the lead never changes hands in the second half. Scored only
  when it acts, with that same head start, the worse one is never
  displaced in 200 of 200 seeds at β = 30 or 100. At β = 8 the better one
  recovers, after a median of 460 rounds. The scored control at β = 100
  entrenches no one. Code: scratch/formal/trust_loop.py.
---
<!-- inactive-ok-file: TERM-053 — Superseded by ADR-070 (conferral, TERM-103; grant, TERM-101); cited as the term of its time -->

# CASE-182: Two operators under one update rule, grants moving toward observed outcomes: scored every round, the more accurate one holds the lead durably whatever the start; scored only when it acts, under sharp selection, whichever gained influence early keeps it

## What happens

Two operators share one update rule and differ only in accuracy (p = 0.8
and 0.6) and in their starting grant. Each round one operator acts,
chosen with probability softmax(β·E). The grant moves toward observed
outcomes, E_i ← E_i + η(outcome − E_i), which is A5's
Ė_ji = η_j[Q_ji − E_ji] in discrete time. η sets the memory kernel A6 §1B
named. Run with `python3 scratch/formal/trust_loop.py`: 200 seeds and
4,000 rounds per regime.

| Regime | Start (E0) | β | Result |
|---|---|---|---|
| scored every round | 0.5, 0.5 | 8 | better ends with the larger grant 200/200; acts in 82% of late rounds |
| scored every round | 0.3, 0.9 | 8 | head start undone; better acts in 83% of late rounds |
| scored when acting | 0.3, 0.9 | 8 | better recovers in 200/200, median round 460 |
| scored when acting | 0.3, 0.9 | 30, 100 | worse operator never displaced, 200/200 |
| scored when acting | 0.5, 0.5 | 100 | worse operator holds most late rounds in 6/200 |
| scored every round (control) | 0.3, 0.9 | 100 | worse operator holds most late rounds in 0/200 |

Durability, under scoring every round with a fair start, is set by the
memory kernel. With η = 0.01 the lead changes hands 0.0000 times per round
in the second half. With η = 0.3 it changes 0.137 times per round.

## What it shows

- **Durable, differentiated authority with no authority primitive.**
  Persistent precedence of the more accurate operator emerges from the
  grant rule alone. Its durability is a property of η, not of a
  second kind of authority. That is [CLAIM-277](../claims.d/CLAIM-277.md)'s first clause and A5's
  "different dynamical regimes, not different ontological primitives".
- **The same loop entrenches.** When influence is what buys the chance to
  be scored, as in A5's chain of early advantage, then greater influence,
  then more visibility, an early leader keeps influence it would lose
  under scoring. The difference between the regimes is what is observed,
  not the rule.

## What it cannot show

It is two operators with fixed accuracies. Niches, where competence shows
only in rare contexts, and mutual regulation among many processes are
not in it: [QUESTION-083](../questions.d/QUESTION-083.md) keeps both. That real organizations score as the
second regime does is A46's niche-exclusion observation, not something this
construction establishes.
