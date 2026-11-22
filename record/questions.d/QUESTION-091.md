---
number: 91
status: Open
formerly:
- QUESTION-tmpmrm3n
title: 'Does the allocation of influence among an organization''s processes regulate how far cascades of activity propagate, holding different subsystems at different distances from criticality, as a branching ratio would show?'
version: 1
tags:
- complex-systems
- probabilistic-modeling
date: '2026-10-13'
line: distributed-agency
summary: >-
  The owner proposed Hawkes processes at U6. A6 turned them into a
  hypothesis: "the influence canvas dynamically regulates the branching
  structure". The record had no point-process material. Of the three
  sources registered, only Brémaud and Massoulié could be read. A Hawkes
  network supplies a coupling, its kernels, which [CLAIM-163](../claims.d/CLAIM-163.md) found missing
  from talk of "synchronization". Its spectral radius is a control
  parameter and, outside the linear excitatory case, only a sufficient
  bound, not an order parameter (see the note of 2026-10-13).
---
<!-- inactive-ok-file: CLAIM-163 LIT-1028 — Proposed or Unavailable; open claims, unread works and readings cited as open, nothing here rests on their being settled -->

<!-- inactive-ok-file: THEORY-tmpye6xs — Proposed or new; the reading of Azizpour and colleagues, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmps8t83 LIT-2991 — Proposed or Unavailable; the reading of the NIPS 2004 companion and the work it stands in for, 2026-11-22 -->

# QUESTION-091: Does the allocation of influence among an organization's processes regulate how far cascades of activity propagate, holding different subsystems at different distances from criticality, as a branching ratio would show?

## Why it is a question

The owner, at U6: "it feels like temporal discounting and hawkes
processes would be useful tools to integrate here." A6 §2: "The more
intriguing hypothesis is that **the influence canvas dynamically regulates
the branching structure**, changing which events can recruit others and how
far cascades can travel." Also: "I would not assume psychological systems
optimize criticality, though. Different subsystems might function
productively at different distances from criticality." A7's H4: "Influence
allocation modulates cascade sizes and recurrent activation regimes."

For a stationary linear excitatory Hawkes process the branching ratio is the
spectral radius of the integrated excitation matrix. Below one, cascades die
out, which is the Hawkes–Oakes cluster representation ([LIT-1028](../literature.d/LIT-1028.md)). The
exchange's kernels are signed and change with state. A6 and A7 granted that
these "do not inherit the simple stability guarantees", so Brémaud and
Massoulié ([LIT-1035](../literature.d/LIT-1035.md)) is where the analysis starts.

[CLAIM-163](../claims.d/CLAIM-163.md) objects that "synchronization" among an agent's interests is "an
analogy without a mechanism", with no coupling and no order parameter. A
Hawkes model of cascades has the coupling, and a control parameter, not an
order parameter. It does not rescue the synchronization
reading of Ainslie, but it shows what an answer of that kind looks like. An
answer fits a marked point process with influence-dependent kernels, to
r/place repairs ([CASE-079](../cases.d/CASE-079.md)) or to a simulation, and reports whether the
effective branching ratio moves with the allocation of influence.

## Note of 2026-10-13: what Brémaud and Massoulié prove, and do not

Brémaud and Massoulié ([LIT-1035](../literature.d/LIT-1035.md)) was read in [NOTE-728](../notes.d/NOTE-728.md), and its
result is filed as [THEORY-215](../theory.d/THEORY-215.md). Three points correct this question's
framing. The status is unchanged.

- **Their kernels are signed but fixed.** The rate is a nonlinear function
  of a fixed filter of the past. Kernels that change with the allocation of
  influence, which is what this question asks about, are outside every
  theorem in the paper.
- **The spectral radius is a branching ratio only in the linear excitatory
  case.** For Lipschitz rates and signed kernels, a spectral radius below
  one of the matrix α_i∫|h_ji| is a sufficient condition for one stable
  regime. Its distance from one measures no proved property of cascades,
  and for bounded rates no size condition is needed at all, so a model
  with saturating influence has no criticality to be near.
- **It is a control parameter, not an order parameter.** The branching
  ratio is computed from the couplings before the dynamics run. The summary's
  "the branching ratio is the coupling and order parameter" runs the two
  together. A Hawkes model has a coupling (the kernels) and this control
  parameter; an order parameter would be a collective variable of the
  state, such as the event rate, and the paper proves nothing about
  transitions.

## Note of 2026-11-22: Azizpour, Priesemann, Zierenberg and Levina, read

A parallel from neural networks, at the same transition ([NOTE-tmporpz2](../notes.d/NOTE-tmporpz2.md),
[THEORY-tmpye6xs](../theory.d/THEORY-tmpye6xs.md), which `bears_on` this question). In a random network
whose branching parameter λ is its largest eigenvalue, the best distance
from criticality for discriminating inputs is set by the readout's
integration window: subcritical for every finite window, approaching
λ = 1 as the window grows. The authors draw the control reading this
question asks about for organizations: "living systems need to adjust
their state ... depending on the specific processing tasks" (p. 4). It is
evidence that a subsystem's best distance from criticality can depend on
how it is read out; it says nothing about the allocation of influence
that the question puts as the regulator.

## Note of 2026-11-22: Natschläger, Bertschinger and Legenstein, read

**A parallel, with a distinction of what branches** ([LIT-tmpdsowv](../literature.d/LIT-tmpdsowv.md),
[NOTE-tmpi5t3r](../notes.d/NOTE-tmpi5t3r.md), [THEORY-tmps8t83](../theory.d/THEORY-tmps8t83.md), read in place of Bertschinger and
Natschläger, [LIT-2991](../literature.d/LIT-2991.md)). In driven threshold networks the order–chaos line
is K·P_bf = 1, a branching ratio of one for perturbations, not for
activity (the reader's and the filer's inference from Eq. 1, not the
paper's); this question's branching ratio is of activity. A system can
sit at one and not the other, so a measured ratio must say which it
counts. The paper's §6 also gives a local rule, each node scaling its
weights from its own margin, that holds a network at the damage line, a
mechanism of self-placement the question could set beside the allocation
of influence; it is a parallel, not evidence about organizations.
