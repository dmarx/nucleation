---
number: 507
status: Open
formerly:
- QUESTION-tmp2hhlc
title: 'Do systems near a dynamical transition, or with scale-free dynamics, have a distinctive computational capacity, or does nearness to the transition only redistribute a bounded capacity among kinds of computation, by task?'
version: 3
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2980 (Azizpour, Priesemann, Zierenberg &
    Levina 2026, NOTE-tmporpz2, THEORY-tmpye6xs): the sentence calling the
    finite-window study unread is replaced; what it settles is in the dated
    note. The question and its status are unchanged.
- version: 3
  date: '2026-11-22'
  note: >-
    After the reading of Bertschinger and Natschläger's NIPS companion
    (LIT-tmpdsowv, NOTE-tmpi5t3r, THEORY-tmps8t83) in place of the
    unreachable LIT-2991: the sentence in point 1 calling the edge-of-chaos
    paper unread is replaced; what the reading adds is in the dated note.
    The question and its status are unchanged.
tags:
- complex-systems
- information-theory
- neuroscience
- learning-theory
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
summary: >-
  A's open direction at the close of A13 of the exchange "Rich Get Richer
  Power Laws", "whether scale-free systems have a distinctive
  computational capacity—whether their multiscale correlations make them
  especially capable of storing memories, propagating signals, adapting,
  or performing calculations", which A calls "considerably more subtle"
  than the edge of chaos, and which A15 takes up. The record holds the
  order-to-chaos transition in deep networks ([THEORY-2041](../theory.d/THEORY-2041.md), [THEORY-2051](../theory.d/THEORY-2051.md)), a
  reservoir ([THEORY-1431](../theory.d/THEORY-1431.md)) and 1/f in brains ([CLAIM-692](../claims.d/CLAIM-692.md)), and no question
  on criticality and computation. The wording is A's (the other assistant
  in the exchange "Rich Get Richer Power Laws", A13 and A15); adopting it
  is the owner's call.
---
<!-- inactive-ok-file: THEORY-2151 — Proposed or new; the Bialek reading of 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2041 THEORY-2051 THEORY-1431 — Proposed readings bearing on the question -->
<!-- inactive-ok-file: CLAIM-805 CLAIM-809 CLAIM-814 — filed with this question from the same exchange, Proposed -->
<!-- inactive-ok-file: LIT-2991 — Unavailable since 2026-11-22; read through its companion -->
<!-- inactive-ok-file: THEORY-tmps8t83 ARG-tmp2zz6k — Proposed or new; the companion's reading and its argument, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-2158 CLAIM-850 — Proposed; the reading of 2026-11-21 and a claim it bears on -->

<!-- inactive-ok-file: THEORY-tmpye6xs LIT-tmpfn6b8 — Proposed or new; the reading of Azizpour and colleagues, 2026-11-22, and the Deferred work it names -->
<!-- inactive-ok-file: THEORY-tmpl7rgc — Proposed; the reading of Crutchfield and Feldman, 2026-11-22 -->

# QUESTION-507: Do systems near a dynamical transition, or with scale-free dynamics, have a distinctive computational capacity, or does nearness to the transition only redistribute a bounded capacity among kinds of computation, by task?

## Why it is a question

A15 opens on the hope: "**A system near criticality may be especially
capable of preserving information about the past while remaining
sensitive to new information from its environment.**" It then gives the
reasons to doubt that it is a general advantage: a bound on total
capacity (Dambre and colleagues, [LIT-2971](../literature.d/LIT-2971.md), read 2026-11-21: see the
dated note), a three-way
tradeoff of sensitivity, reliability and speed, and a finite-window study
in which the best discrimination moves off the critical point
([LIT-2980](../literature.d/LIT-2980.md), read 2026-11-22: see the dated note). A's answer is [CLAIM-809](../claims.d/CLAIM-809.md); one exactly solved
case is [CLAIM-814](../claims.d/CLAIM-814.md).

Three things keep it open.

1. **Which transition.** A runs together the order-to-chaos transition
   of recurrent networks, where the edge-of-chaos results live
   (Bertschinger and Natschläger, [LIT-2991](../literature.d/LIT-2991.md), Unavailable, read through
   its NIPS companion, [THEORY-tmps8t83](../theory.d/THEORY-tmps8t83.md); the record's
   [THEORY-2041](../theory.d/THEORY-2041.md) for deep networks), and branching criticality of neural
   avalanches, where a branching ratio of one separates dying from
   exploding cascades ([QUESTION-091](QUESTION-091.md)). They are different transitions: the
   first is a change in the sign of the largest Lyapunov exponent of a
   deterministic map, the second a change in the mean offspring number of
   a stochastic cascade. A network can sit at one and not the other. A
   claim that critical brains compute well because reservoirs at the edge
   of chaos do needs a step relating the two, and the record has none.
2. **Which measure.** "Different definitions of utility can have optima
   at different parameter values" (A13 §6); "sensitivity isn't the same
   as useful computation". Memory capacity, separation, discrimination in
   a finite window and predictive information each peak, if at all, at
   their own place.
3. **Which environment.** A15 §8: "If the environment has one dominant
   characteristic timescale … a much simpler system tuned to that
   timescale could be more efficient." A scale-free internal dynamics
   pays only where the input has correlations across those scales.

A15 §5 adds a methodological point worth keeping: a study that perturbs
single neurons and follows the spread is "a stronger experimental
approach than relying on a power-law fit alone". A cites a Nature
Communications study of 10 January 2026 that the registration could not
identify, so the record cannot use it.

## What would answer it

For a stated class of systems and a stated family of tasks: a capacity
measure, its bound, and how the bound's allocation moves with distance
from the transition, with the transition named. Dambre and colleagues'
result, once read, may answer the first part for reservoirs with fading
memory and i.i.d. input. An adaptive system that tunes its own distance
from the transition by task (A15 §7, quasicriticality) would make the
question one of control rather than of a fixed operating point, as
[QUESTION-091](QUESTION-091.md) asks for organizations.

## Note of 2026-11-21: Dambre, Verstraeten, Schrauwen and Massar, read

Dambre and colleagues' paper ([LIT-2971](../literature.d/LIT-2971.md), read in [NOTE-2244](../notes.d/NOTE-2244.md); the
reading is [THEORY-2158](../theory.d/THEORY-2158.md)) **answers the first part** of "What would
answer it" and **leaves the rest open**.

- **Measure and bound: given**, for systems driven by i.i.d. input with a
  linear readout: capacities for orthogonal functions of past inputs sum to
  at most N, and to N with fading memory and N independent variables.
  Nearness to the transition cannot raise the total, which is flat at N
  inside the fading-memory regime and falls past the undriven system's
  stability edge.
- **Allocation against distance from the transition: not given.** The
  paper sweeps input scaling and sampling period at a fixed spectral
  radius.
- **Point 1, which transition.** The paper's edge is the stability edge
  of a deterministic map, neither branching criticality nor, strictly,
  the onset of chaos; [CLAIM-850](../claims.d/CLAIM-850.md) separates chaos, criticality and
  cascades, and this is a further thing.
- **Point 3, which environment.** The paper takes i.i.d. input on purpose,
  "so that any measured structure will be due to the dynamical system
  itself", and calls the bound for correlated input "largely a theoretical
  insight". It cannot speak to the value of multiscale memory in a
  correlated environment.

[THEORY-2158](../theory.d/THEORY-2158.md) `bears_on` this question.

## Note of 2026-11-21: Bialek, Nemenman and Tishby, read

A weaker bearing, a claim without proof ([THEORY-2151](../theory.d/THEORY-2151.md), [NOTE-2243](../notes.d/NOTE-2243.md)). The paper asserts that predictive information diverges at critical points (§3, p. 12; §6, p. 44; its footnote 9), so that critical systems would be the most complex in its sense. It gives no derivation. On this question's first part it offers an information-theoretic measure of capacity, predictive information, that differs from Dambre's ([THEORY-2158](../theory.d/THEORY-2158.md)), and a candidate answer that is unproved and that [CLAIM-805](../claims.d/CLAIM-805.md) ("criticality is not the maximum of complexity") questions. The note is the assistant's (Claude, in this session).

## Note of 2026-11-22: Azizpour, Priesemann, Zierenberg and Levina, read

Read in [NOTE-tmporpz2](../notes.d/NOTE-tmporpz2.md) ([THEORY-tmpye6xs](../theory.d/THEORY-tmpye6xs.md), which `bears_on` this question).
It **gives a case for point 2 and leaves points 1 and 3 open**.

- **Point 2, which measure:** the number of ε-discriminable input rates
  and a fluctuation-aware dynamic range peak at different couplings, both
  below the critical point for every finite readout window (pp. 3–4).
- **Point 1, which transition:** the paper is on branching
  (absorbing-to-active) criticality and says the result depends on the
  transition: "On which side of the transition this optimum lies will,
  however, depend on both the task and the type of phase transition", the
  transition to chaos favouring the supercritical side (Toyoizumi and
  Abbott, [LIT-tmpfn6b8](../literature.d/LIT-tmpfn6b8.md), registered, Deferred). A statement with a
  citation, not the step relating the two transitions that point 1 asks
  for.
- **"What would answer it":** the paper gives performance against
  distance from the transition, which Dambre and colleagues did not, but
  for one measure family and with no bounded total being redistributed.
- **Point 3, which environment:** silent; the input is a stationary rate.

The sentence above calling the finite-window study unread is replaced
(version 2).

## Note of 2026-11-22: Natschläger, Bertschinger and Legenstein, read

Bertschinger and Natschläger's Neural Computation paper ([LIT-2991](../literature.d/LIT-2991.md)) could
not be reached; its NIPS companion was read in its place ([LIT-tmpdsowv](../literature.d/LIT-tmpdsowv.md),
[NOTE-tmpi5t3r](../notes.d/NOTE-tmpi5t3r.md); [THEORY-tmps8t83](../theory.d/THEORY-tmps8t83.md), which `bears_on` this question). It
**supports the "distinctive capacity" side for one class and leaves the
dilemma open**, and it **adds to point 1**.

- **Point 1, which transition.** The order–chaos line of driven threshold
  networks is K·P_bf = 1 (Eq. 1), P_bf being "the probability ... that a
  node will change its output if a single out of its K input bits is
  flipped". So K·P_bf is the expected number of nodes one flipped node
  flips in the next step: the line is a branching ratio of one for
  perturbations (damage), not for activity, which "can vary considerably"
  across the parameter plane (§2, Fig. 1). That is a formal step relating
  the edge of chaos to branching criticality, by the form of their order
  parameter, not an identification of the two: a network can be at the
  damage-branching line with activity far from any critical branching of
  its own. The reading of Eq. 1 as a branching ratio is the reader's and
  the filer's inference, not the paper's; the paper does not draw it.
- **The "distinctive capacity" side.** The abstract's "only near the
  critical boundary can such networks perform complex computations on
  time series", for driven random threshold networks and short-memory
  nonlinear Boolean tasks, averaged over many tasks. No total and no
  bound, so the "redistribute a bounded capacity" side is not tested
  ([ARG-tmp2zz6k](../arguments.d/ARG-tmp2zz6k.md) on [CLAIM-809](../claims.d/CLAIM-809.md)).
- **Point 2, which measure.** One family: summed mutual information on
  Boolean tasks, with NM-separation as its predictor; both peak near the
  line.
- **Point 3, which environment.** Silent; the input is i.i.d. binary.

Calvet, Reulet and Rouat ([LIT-tmpahs2x](../literature.d/LIT-tmpahs2x.md), a passage) find the best region
aligned with the critical region for one sign of the
excitatory–inhibitory balance only. The sentence in point 1 calling the
paper unread is replaced (version 3).

## Note of 2026-11-22: Crutchfield and Feldman, read

**Background**, no edge ([LIT-3010](../literature.d/LIT-3010.md), read in [NOTE-tmpe86ty](../notes.d/NOTE-tmpe86ty.md);
[THEORY-tmpl7rgc](../theory.d/THEORY-tmpl7rgc.md)). The paper offers measures a capacity study could use
(entropy rate, excess entropy, transient information) and the split of
finitary from infinitary processes; it says nothing about transitions,
capacity or tasks. For point 2, which measure, it adds a methodological
caution: an observer working at finite block length converts unseen
memory into apparent randomness, overestimating the entropy rate by E/L
(Props. 13–15), which bears on any finite-window study such as [LIT-2980](../literature.d/LIT-2980.md).
