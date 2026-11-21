---
status: Proposed
title: 'The scalar linear reservoir is an exactly solved instance of nearness to a transition redistributing a bounded computational capacity rather than raising it, though not by the memory-noise tradeoff the exchange gives'
version: 1
form: existence
rests_on:
- CLAIM-tmpd1shn
concludes:
- CLAIM-tmpask80
tags:
- complex-systems
- information-theory
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  Whether [CLAIM-tmpd1shn](../claims.d/CLAIM-tmpd1shn.md) supports A's [CLAIM-tmpask80](../claims.d/CLAIM-tmpask80.md) from the exchange
  "Rich Get Richer Power Laws" (A15), and how far. It is an existence
  proof: one coherent system in which moving toward the stability edge
  leaves total capacity fixed and only reallocates it across lags, with a
  task-dependent optimum. That shows the "redistribute, not raise"
  reading can hold; it does not show it holds generally, and it removes
  the memory–noise tradeoff A gave as the mechanism. Proposed, as support
  for the possibility clause only. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
grounds:
- THEORY-tmpr5fuq
---
<!-- inactive-ok-file: CLAIM-tmpd1shn CLAIM-tmpask80 — filed with this argument from the same exchange, Proposed -->
<!-- inactive-ok-file: THEORY-tmpr5fuq ARG-tmpr04sw ARG-tmp53559 — Proposed; the reading of Dambre and colleagues and the arguments of 2026-11-21 -->

# ARG-tmpubyzo: The scalar linear reservoir is an exactly solved instance of nearness to a transition redistributing a bounded computational capacity rather than raising it, though not by the memory-noise tradeoff the exchange gives

## The inference

[CLAIM-tmpask80](../claims.d/CLAIM-tmpask80.md) says, after A15, that nearness to a dynamical transition
"may change what kinds of computations a system is good at, rather than
universally increasing all computational abilities". [CLAIM-tmpd1shn](../claims.d/CLAIM-tmpd1shn.md)
solves A's own illustrative model, x(t+1) = a x(t) + u(t) + η(t): as
a → 1 the total linear memory capacity stays s²/(s²+σ²), the capacity at
long lags rises and at short lags falls, and the best gain for recalling
the input k steps back is √(k/(k+1)). So in this system, moving toward
the edge changes what the system remembers well and raises nothing in
total. That is one case where the conclusion's possibility holds.

## Critical questions (existence)

**Is the case coherent?** Yes. The model is A's, the derivation is
closed-form, and the assistant checked it by simulation
([CLAIM-tmpd1shn](../claims.d/CLAIM-tmpd1shn.md), Check).

**Does it separate the very things the conclusion says can come apart?**
It separates nearness to the transition from total capacity: the first
varies, the second does not. It does so for linear memory only, in one
dimension. [CLAIM-tmpask80](../claims.d/CLAIM-tmpask80.md)'s wider strands, the trade of linear memory for
nonlinear transformation, the sensitivity–reliability–speed tradeoff and
the finite-window shift, are not touched. And a = 1 here is marginal
stability, not a collective critical point.

## What it does not show

- **Not the generality.** One linear scalar case cannot show that every
  system near every transition redistributes rather than raises. That
  rests on Dambre and colleagues' bound ([LIT-tmp7sbn6](../literature.d/LIT-tmp7sbn6.md)), whose conditions
  were unchecked when this argument was filed. (Revised 2026-11-21, after
  the reading: see the note of that date below. The generality holds for
  the total, not for how the allocation moves with distance from the
  edge.)
- **Not A's mechanism.** A gives the reason as a memory–noise tradeoff.
  In this model there is none: noise and input share one filter, and with
  readout noise capacity rises monotonically toward the edge. The
  task-dependence comes from the allocation across lags. If [CLAIM-tmpask80](../claims.d/CLAIM-tmpask80.md)
  is adopted, its reason should be that one.

## Note of 2026-11-21: Dambre, Verstraeten, Schrauwen and Massar, read

Dambre and colleagues' paper ([LIT-tmp7sbn6](../literature.d/LIT-tmp7sbn6.md)) was read in full with its
supplement ([NOTE-tmpkp5gf](../notes.d/NOTE-tmpkp5gf.md); the reading is [THEORY-tmpr5fuq](../theory.d/THEORY-tmpr5fuq.md)). It **supports**
this argument and **closes the gap** its "What it does not show" named.

- **The conditions, checked.** The bound (Theorem 4) needs only i.i.d.
  input, a linear readout, finite fourth moments and infinite data; it
  holds without fading memory. Fading memory, with N linearly independent
  variables and a complete basis, is the condition for **equality**
  (Theorem 7). Noise is counted as a further input: the theorem holds over
  functions of all inputs, and the capacities for the signal alone sum to
  less. As first filed, this argument named the conditions "(fading
  memory, i.i.d. input)", which ran the two together.
- **Not merely analogous.** [CLAIM-tmpd1shn](../claims.d/CLAIM-tmpd1shn.md) is a case of Theorem 7, with N =
  1 and η as the second input ([ARG-tmpr04sw](ARG-tmpr04sw.md)).
- **How general.** "Raises nothing in total" holds for every fading-memory
  system with N independent observed variables: their total is N
  throughout that regime, and the paper finds it falling past the
  undriven system's stability edge (Fig. 1). How the allocation moves with
  distance from the edge is not studied: the paper sweeps input scaling at
  a fixed spectral radius. So the argument's conclusion is general for the
  total and still rests on the scalar case for the allocation.
- **Which edge.** The paper's edge is linear stability, as this argument
  already says of a = 1.

[THEORY-tmpr5fuq](../theory.d/THEORY-tmpr5fuq.md) replaces [LIT-tmp7sbn6](../literature.d/LIT-tmp7sbn6.md) in `grounds`. [ARG-tmp53559](ARG-tmp53559.md) gives the
paper's direct bearing on [CLAIM-tmpask80](../claims.d/CLAIM-tmpask80.md). Status unchanged.
