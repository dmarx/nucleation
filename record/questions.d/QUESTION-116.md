---
number: 116
status: Open
formerly:
- QUESTION-tmp6neu8
title: 'What is the time-lagged form of the block criterion, for a collective whose members are weakly coupled at every instant but strongly connected through time-respecting paths of transmission, across generations and through stored artifacts?'
version: 3
history:
- version: 2
  date: '2026-11-11'
  note: >-
    A dated note added citing QUESTION-222, which holds the same gap
    (CLAIM-157's time-lagged block test) from the side of reduced
    dynamics. Reported by the synthesis review of 2026-11-11
    (seventh round). No other change.
- version: 3
  date: '2026-11-22'
  note: >-
    Note of 2026-11-22 added: a lagged, priced block test built and run
    on CASE-101's populations (CASE-tmprsqvj, CLAIM-tmp2jbb1, LEAD-026).
    The question is unchanged.
tags:
- individuation
- network-science
date: '2026-10-16'
line: distributed-agency
refines:
- QUESTION-035
summary: >-
  [CLAIM-157](../claims.d/CLAIM-157.md) already says its block test on synchronous dynamics will not
  see Otto's notebook, whose coupling "is a write and a later read", and
  that a time-lagged version "is not built". A9 §2 of the exchange of
  2026-10-16 met the same gap from the other side: "A collective can be
  weakly connected synchronically but strongly connected diachronically."
  The second time it turns up. An answer is a criterion on temporal
  networks or lagged dynamics that finds such a collective and still
  rejects mere common input.
---
<!-- inactive-ok-file: CASE-tmprsqvj CLAIM-tmp2jbb1 — new, filed 2026-11-22 from LEAD-026's study -->

# QUESTION-116: What is the time-lagged form of the block criterion, for a collective whose members are weakly coupled at every instant but strongly connected through time-respecting paths of transmission, across generations and through stored artifacts?

## Why it is a question

[CLAIM-157](../claims.d/CLAIM-157.md), on Otto's notebook: "Its coupling is a write and a later read,
and a block test on synchronous dynamics will not see it. The storage
route ([CASE-043](../cases.d/CASE-043.md)) needs a time-lagged version of the criterion, which is
not built."

A9 §2 of 2026-10-16, on 100,000 supporters of one program: an
interaction network built from a ten-minute window shows hundreds of
disconnected components, while a decade shows alumni teaching children,
donors funding the program, older fans teaching rituals to newer ones.
"The members are not simultaneously interacting. But they participate in
causal pathways connecting the organization's earlier and later states."
So "a snapshot interaction network may therefore be the wrong
mathematical object for historical social individuation", and A9 proposed
a temporal network, where paths respect time, with books, archives,
recorded games and places as carriers: "a **distributed memory system**,
with both human and nonhuman carriers". The rivalry ([CASE-098](../cases.d/CASE-098.md)) is held
together this way.

A5 §1 named the methodological point: such a case is not yet a failure of
[CLAIM-157](../claims.d/CLAIM-157.md), only of an operationalization that uses the wrong timescale or
state variables. [CLAIM-331](../claims.d/CLAIM-331.md) says the timescale belongs to the level.

## What would count as an answer

A criterion stated on lagged dynamics or a temporal network, priced as
[CLAIM-154](../claims.d/CLAIM-154.md) prices a block, that finds the notebook's and the fandom's
coupling, says over what window, and rejects a population whose members
are correlated only because they receive the same input ([CASE-101](../cases.d/CASE-101.md),
arm A). A time-respecting path, A9 warned, "indicates possible historical
transmission, not by itself collective individuality."

## Note of 2026-11-11: the same gap from reduced dynamics

[QUESTION-222](QUESTION-222.md) holds the same gap from the side of reduced dynamics: a
coarse variable whose reduced dynamics carry memory of eliminated
variables, and whether a level whose history does the predicting is
still a level. It cites [CLAIM-157](../claims.d/CLAIM-157.md)'s missing time-lagged block test, which
is this question. Neither is a part of the other, so they are not
related by `refines`.

## Note of 2026-11-22: a lagged block test, run on [CASE-101](../cases.d/CASE-101.md)'s populations

[CASE-tmprsqvj](../cases.d/CASE-tmprsqvj.md) builds one candidate form of the criterion this question asks
for, and runs it on [CASE-101](../cases.d/CASE-101.md)'s populations ([LEAD-026](../leads.d/LEAD-026.md)). The test:

- fits a linear autoregression of window W over the observed variables;
- prices every group of couplings by [CLAIM-154](../claims.d/CLAIM-154.md)'s rule, with an Occam cost
  of ln n per coefficient;
- passes a candidate when every cut inside it is kept and its edge is
  pruned.

[CLAIM-tmp2jbb1](../claims.d/CLAIM-tmp2jbb1.md) states the result.

- **It finds the collective this question describes.** The members of the
  transmitting population have no synchronous coupling, only coupling at a
  lag of eight steps. They pass as a block, and the block's support peaks
  at W = 8, which says over what window.
- **It rejects common input only while the input is observed.** The
  commonly driven members fail alone and pass joined to their driver. With
  the driver unobserved they pass alone.
- **A one-step model is not blind to the lag.** Fitted to data, it sees the
  transmission through the members' own persistence. The window decides
  where the support peaks, not whether the block is seen.

The answer this question asks for must reject common input. This test does
so only relative to an observed set that contains the input. Whether that
counts as an answer for the model is the owner's call. The question is
unchanged and stays Open.
