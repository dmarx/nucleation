---
number: 809
status: Proposed
formerly:
- CLAIM-tmpask80
title: 'Nearness to a dynamical transition changes what a system computes well rather than raising every computational ability: memory and separation, sensitivity, reliability and speed pull apart, total capacity is bounded by the number of independent state variables, and the best distance from the transition depends on the task, the integration window and the correlations of the environment'
version: 3
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Revised in place after the reading of LIT-2980 (Azizpour, Priesemann,
    Zierenberg & Levina 2026, NOTE-tmporpz2). Its reading, THEORY-tmpye6xs,
    replaces the unread LIT in the grounds (ARG-tmp5sgtm). Strand 3 now
    states what the paper shows and its narrow scope (one branching
    transition, one task family, the optimum subcritical and approaching
    the transition as the window grows); a section sets its mechanism
    against CLAIM-814's. The title, the thesis and the status are
    unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    Revised in place after the reading of Bertschinger and Natschläger's
    NIPS companion (LIT-tmpdsowv, Natschläger, Bertschinger & Legenstein
    2004, NOTE-tmpi5t3r) in place of the unreachable LIT-2991 (now
    Unavailable), with a passage of Calvet, Reulet & Rouat (LIT-tmpahs2x,
    NOTE-tmpt3dxa). THEORY-tmps8t83 and LIT-tmpahs2x join the grounds
    (ARG-tmp2zz6k, ARG-tmps7n0g). Strand 1 now cites what was read; the
    "Misattribution" bullet names the companion paper, whose authors are
    the three A named; the section on mechanisms now holds three cases.
    The title, the thesis and the status are unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  A class of dynamical systems, with a named transition and a capacity
  measure covering memory, nonlinear transformation and discrimination,
  in which every component of that measure is maximized at the
  transition for every task in a stated family and every finite
  integration window, so that nearness to the transition raises all
  computational abilities at once; or a showing that the
  information-processing capacity of a reservoir with fading memory is
  not bounded by its number of independent state variables. A single task
  whose optimum sits at the transition does not defeat it.
tags:
- complex-systems
- information-theory
- neuroscience
- learning-theory
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
answers:
- QUESTION-507
grounds:
- THEORY-tmpye6xs
- THEORY-tmps8t83
- LIT-tmpahs2x
- LIT-2991
- THEORY-2041
- THEORY-1431
- THEORY-2158
summary: >-
  A's answer, at A15 §1–§9 of the exchange "Rich Get Richer Power Laws",
  to whether criticality is good for computation: it "may change what
  kinds of computations a system is good at, rather than universally
  increasing all computational abilities". A rests it on Dambre and
  colleagues' capacity bound, a finite-window study, and a three-way
  tradeoff of sensitivity, reliability and speed; scale-free memory helps
  only if the environment has correlations across scales, and large
  cascades help only if they keep inputs distinguishable. Dambre and
  colleagues' paper was read on 2026-11-21 and the finite-window study on
  2026-11-22 (see the dated notes); the edge-of-chaos paper could not be
  reached, and its NIPS companion (LIT-tmpdsowv) was read in its place on
  2026-11-22. A's illustrative mechanism, a memory–noise tradeoff in a scalar
  linear model, does not hold as stated ([CLAIM-814](CLAIM-814.md)), though the
  conclusion survives. The wording is A's (the other assistant in the
  exchange "Rich Get Richer Power Laws", A15); adopting it is the owner's
  call.
rests_on:
- CLAIM-814
bears_on:
- QUESTION-507
---
<!-- inactive-ok-file: THEORY-tmpehudh — Proposed; the reading of Bak, Tang and Wiesenfeld cited in the note of 2026-11-22 -->
<!-- inactive-ok-file: CLAIM-814 ARG-148 — filed with this claim from the same exchange, Open or Proposed -->
<!-- inactive-ok-file: LIT-2991 — Unavailable since 2026-11-22, registered 2026-11-21 from the exchange; read through its companion -->
<!-- inactive-ok-file: THEORY-tmps8t83 ARG-tmp2zz6k ARG-tmps7n0g — Proposed or new; the companion's reading, the supplement and their arguments, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmpye6xs ARG-tmp5sgtm LIT-tmpfn6b8 — Proposed, Deferred or new; the finite-window reading, its argument and the work it names, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-2158 ARG-128 — Proposed; the reading of Dambre and colleagues and its argument, 2026-11-21 -->
<!-- inactive-ok-file: CLAIM-769 CLAIM-626 — Proposed, bearing on the claim -->
<!-- inactive-ok-file: NOTE-tmpt3dxa — Skimmed; the passage of Calvet, Reulet and Rouat read 2026-11-22 -->

# CLAIM-809: Nearness to a dynamical transition changes what a system computes well rather than raising every computational ability: memory and separation, sensitivity, reliability and speed pull apart, total capacity is bounded by the number of independent state variables, and the best distance from the transition depends on the task, the integration window and the correlations of the environment

## The claim

A15 gives five strands, each A's unless a work is named.

1. **Memory against separation.** A reservoir, x_{t+1} = φ(Wx_t + Bu_t)
   with a trained linear readout, needs "**Memory:** The current network
   state retains information about past inputs" and "**Separation:**
   Different input histories produce sufficiently distinguishable internal
   states" (A15 §3). An ordered network forgets; a chaotic one separates
   but cannot be read reliably; near the transition both can hold, the
   edge-of-chaos result ([LIT-2991](../literature.d/LIT-2991.md), Unavailable; read through its NIPS
   companion, THEORY-tmps8t83). There, order is fading memory, and chaos
   fails because the state "contains “spurious” information about the
   initial conditions", not because of readout noise.
2. **A bound on capacity.** "Dambre and colleagues showed that, under
   specified conditions, a reservoir's total information-processing
   capacity is bounded by its number of independent state variables.
   Different dynamical regimes can redistribute that capacity between
   linear memory and nonlinear transformations" (A15 §3; [LIT-2971](../literature.d/LIT-2971.md),
   read 2026-11-21, [THEORY-2158](../theory.d/THEORY-2158.md); see the dated note).
3. **Sensitivity, reliability, speed.** Near criticality susceptibility,
   fluctuations and relaxation time all grow, so "exactly critical may not
   be exactly optimal" (A15 §6). A finite integration window moves the
   best discrimination of inputs away from the critical point. Azizpour
   and colleagues show it for one system ([THEORY-tmpye6xs](../theory.d/THEORY-tmpye6xs.md), read
   2026-11-22): in a branching network of stochastic spiking neurons with
   a leaky readout, "every finite integration time will have an optimal
   0 < λ < 1", the optimum moving "closer to the critical point" as the
   window T grows, and the dynamic range peaking at a different λ from the
   count of discriminable inputs. The scope is narrow: one transition
   (absorbing-to-active branching, not the edge of chaos), one task family
   (discriminating stationary input rates), and the shift is to the
   subcritical side and vanishes as T → ∞. The paper states the thesis's
   last clause itself, for side as well as distance: "On which side of the
   transition this optimum lies will, however, depend on both the task and
   the type of phase transition" ([ARG-tmp5sgtm](../arguments.d/ARG-tmp5sgtm.md)).
4. **The environment sets the value of multiscale memory.** A superposition
   of exponential relaxations with rates spread as λ^(α−1) gives power-law
   memory without criticality (A15 §4; the record's [CLAIM-769](CLAIM-769.md)), but "the
   computational value depends on whether the environment itself contains
   meaningful correlations across those timescales" (A15 §4, §8).
5. **Magnitude is not discriminability.** Rare large cascades may carry
   much of the global transfer, "but … if they saturate the network, they
   may erase distinctions between different inputs. Useful computation
   depends on the *structure and discriminability of responses*, not
   merely their magnitude" (A15 §9).

Hence: "**Near-critical may be useful, but the optimal distance from
criticality depends on what the system needs to accomplish.**"

## Where the turn needs correcting

- **The scalar model's tradeoff.** A15 §2 illustrates the tension with
  x_{t+1} = a x_t + u_t + η_t: memory half-life ln(½)/ln a diverges as
  a → 1 (A's table is right: 1, 3.1, 6.6, 69 and 693 steps at a = 0.5,
  0.8, 0.9, 0.99 and 0.999, which the assistant recomputed), and so does
  the noise variance σ²/(1 − a²), whence "Criticality amplifies both
  information and uncertainty." But input and noise pass through the same
  filter, so their ratio in the state does not depend on a, and nor does
  the total memory capacity. The gain only spreads capacity over lags.
  The conclusion A wants survives, by a different route: [CLAIM-814](CLAIM-814.md),
  and [ARG-148](../arguments.d/ARG-148.md) for how far it carries.
- **Marginal stability is not criticality.** The scalar model at a → 1 is
  at the edge of linear stability, which A rightly says "resembles
  critical slowing down"; it is not a collective transition. [CLAIM-626](CLAIM-626.md)
  holds that slowing has no single organizational meaning.
- **Misattribution, a conflation.** A15 §3 names "Bertschinger,
  Natschläger, and Legenstein" for the 2004 study. The 2004 Neural
  Computation paper is by Bertschinger and Natschläger ([LIT-2991](../literature.d/LIT-2991.md)). The
  three A names wrote its NIPS 2004 companion, "At the Edge of Chaos:
  Real-time Computations and Self-Organized Criticality in Recurrent
  Neural Networks" (LIT-tmpdsowv; the title page orders them Natschläger,
  Bertschinger, Legenstein), which generalizes the journal paper's model
  and restates its headline. A ran the two 2004 papers together.
  Legenstein is also an author of a separate paper with Maass (2007), not
  registered. Corrected 2026-11-22 (version 3).
- **Two transitions.** A runs the order-to-chaos transition and branching
  criticality together ([QUESTION-507](../questions.d/QUESTION-507.md), point 1).
- **Power-law memory's range.** The Γ(α) integral converges for α > 0,
  and with rates confined to [λ_min, λ_max] the power law holds for
  1/λ_max ≪ t ≪ 1/λ_min; the long-time end, where memory matters, is set
  by the slowest rates. A says only "an intermediate range of times".

## Three cases, three outcomes

The record now holds three analysed cases (the third added 2026-11-22,
version 3), and they put the optimum in three places. The first two move
it in opposite directions. In [CLAIM-814](CLAIM-814.md)'s scalar reservoir, input and state
noise pass through one filter, so the gain trades nothing against state
noise; noise added at the readout, after the filter, makes capacity rise
monotonically toward the transition (a = 1), and [ARG-148](../arguments.d/ARG-148.md) reads the case
as redistribution, not gain. In Azizpour and colleagues' network
([THEORY-tmpye6xs](../theory.d/THEORY-tmpye6xs.md)), the obstacle is internal: near λ = 1 the population's
own fluctuations grow relative to the signal and slow down, and a leaky
readout of finite window T does not average them out, so the optimum is
pushed away from the transition, less as T grows. Readout noise favours
the transition there; unaveraged, critically slowed internal fluctuations
disfavour it here. Both fit the thesis, that the best distance depends on
the task and the readout, and neither alone says which way a given system
goes. The third case is the edge of chaos itself: in Natschläger,
Bertschinger and Legenstein's driven threshold networks (THEORY-tmps8t83),
a linear readout does best on the order–chaos line, averaged over many
nonlinear tasks of recent inputs; the paper reports no per-task optima.
So readout noise toward the transition (CLAIM-814), subcritical for every
finite window (Azizpour), and on the order–chaos line on average
(Bertschinger and colleagues), with Calvet, Reulet and Rouat
(LIT-tmpahs2x) finding the alignment with the critical region dependent
on the sign of the excitatory–inhibitory balance. Added 2026-11-22
(versions 2 and 3); the wording is the assistant's (Claude, in this
session).

## What it does not say

- Not that nearness to a transition never helps: it can shift capacity
  toward long memory, which some tasks need.
- Not that brains are critical. A15 §5 calls the evidence "contested",
  and the record holds only that 1/f structure does not discriminate
  mechanism ([CLAIM-692](CLAIM-692.md)).

## Note of 2026-11-21: Dambre, Verstraeten, Schrauwen and Massar, read

Dambre and colleagues' paper ([LIT-2971](../literature.d/LIT-2971.md)) was read in full with its
supplement ([NOTE-2244](../notes.d/NOTE-2244.md); the reading is [THEORY-2158](../theory.d/THEORY-2158.md)). It **supports
strand 2** and **qualifies the thesis** ([ARG-128](../arguments.d/ARG-128.md)).

- **Strand 2 holds, with its conditions stated.** The total is bounded by
  the number N of observed variables for i.i.d. input, a linear readout and
  infinite data (Theorem 4), and equals N when the system also has fading
  memory and N linearly independent variables (Theorem 7). Input scaling
  moves capacity between linear memory and nonlinearity (Fig. 3).
- **Stronger than the claim on the total.** C_TOT "remains close to N up
  to the bifurcation point of the undriven system and then drops off
  rapidly" (Fig. 1). For this measure nearness to the edge cannot raise
  total capacity and crossing it loses some. That is more than "does not
  raise every ability".
- **Not shown: allocation against distance from the transition.** The
  paper's redistributing "regimes" are input scalings and sampling periods
  at a fixed spectral radius near the edge, not distances from it. The
  thesis's use of strand 2 for distance rests on [CLAIM-814](CLAIM-814.md) and the
  other strands.
- **Which edge.** The paper's edge is the undriven system's loss of linear
  stability, marginal stability, not a collective critical point, as the
  section "Marginal stability is not criticality" already says of the
  scalar model. The paper's one remark about the edge's value is an
  assumption carried in from Langton.
- **The defeater is safe.** `defeated_if`'s second clause, a reservoir with
  fading memory whose capacity is not bounded by its state variables,
  cannot be met: Theorem 4 bounds every system.

[THEORY-2158](../theory.d/THEORY-2158.md) replaces [LIT-2971](../literature.d/LIT-2971.md) in `grounds`. Status unchanged.

## Note of 2026-11-22: Azizpour, Priesemann, Zierenberg and Levina, read

Read in [NOTE-tmporpz2](../notes.d/NOTE-tmporpz2.md) ([THEORY-tmpye6xs](../theory.d/THEORY-tmpye6xs.md)). It **supports strand 3 and the
window- and task-dependence of the thesis**, narrowly ([ARG-tmp5sgtm](../arguments.d/ARG-tmp5sgtm.md)); the
revisions are made in place above (version 2).

- **Window:** subcritical optimum for every finite T, approaching
  criticality as T grows (pp. 3–4, Fig. 2).
- **Task, weakly:** the number of discriminable inputs and the dynamic
  range peak at different λ; both are measures of one task family.
- **Scope:** branching transition only; the paper cites Toyoizumi and
  Abbott ([LIT-tmpfn6b8](../literature.d/LIT-tmpfn6b8.md), registered, Deferred) for the transition to chaos,
  where "deviations toward the supercritical side ... are thus beneficial
  in the presence of noise".
- **Silent** on strands 1, 2, 4 and 5.
- **The defeater** is not met: no finite window has its optimum at the
  transition; the critical optimum returns only as T → ∞.
- **No Fisher information.** The record does not attribute one to the
  paper, and the paper does not use it: its measure is ideal-observer
  overlap error.

## Note of 2026-11-22: Bak, Tang and Wiesenfeld, read

**Background, by contrast of senses.** Bak, Tang and Wiesenfeld
([LIT-2992](../literature.d/LIT-2992.md), read in [NOTE-tmpnl00y](../notes.d/NOTE-tmpnl00y.md); the reading is [THEORY-tmpehudh](../theory.d/THEORY-tmpehudh.md)) build
criticality out of minimal stability: the pile stops "precisely at the
point when the network of minimally stable states has been broken down
to the level where the noise signal cannot be communicated through
infinite distances" (p. 382). That does not touch the bullet "Marginal
stability is not criticality", whose marginal stability is a scalar map
at a → 1; theirs is a spatial percolation threshold of many marginally
stable sites, a collective state. The two senses should not be run
together. No edge. Status unchanged.

## Note of 2026-11-22: Bertschinger and Natschläger, sought; Natschläger, Bertschinger and Legenstein, and Calvet, Reulet and Rouat, read

Bertschinger and Natschläger's Neural Computation paper (LIT-2991) could
not be reached and is now Unavailable; its abstract was read. Its NIPS
2004 companion was read in its place (LIT-tmpdsowv, NOTE-tmpi5t3r; the
reading is THEORY-tmps8t83), and a passage of Calvet, Reulet and Rouat
(LIT-tmpahs2x, NOTE-tmpt3dxa). The revisions are made in place above
(version 3).

- **Strand 1: supported** (ARG-tmp2zz6k). Order is fading memory; chaos
  carries "spurious" information about initial conditions, which the
  paper's NM-separation subtracts.
- **The headline qualifies the thesis and does not defeat it.** The
  abstract's "only near the critical boundary can such networks perform
  complex computations on time series" is the universal reading the claim
  rejects. But the companion averages over "many different tasks" and
  warns that a network "specifically designed for a single task will not
  show a good performance in this setup"; it reports no per-task optima
  and no total. The defeater asks for every component maximized at the
  transition for every task, which is not shown.
- **"The best distance depends": supported, weakly** (ARG-tmps7n0g).
  Calvet and colleagues find "the edge of chaos, or the critical region,
  does not consistently align with the peak performance region",
  depending on the sign of the excitatory–inhibitory balance, and present
  this as refining the 2004 result.
- **The attribution** is corrected in place: A's three authors are the
  companion's.
- **Silent** on strands 2 to 5.

THEORY-tmps8t83 and LIT-tmpahs2x join the grounds; LIT-2991 stays there
as the work the strand names. Status unchanged.
