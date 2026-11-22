---
number: 814
status: Proposed
formerly:
- CLAIM-tmpd1shn
title: 'In the scalar linear reservoir x(t+1) = a x(t) + u(t) + η(t), the gain a does not trade memory against noise: the state''s signal-to-noise ratio and its total linear memory capacity s²/(s²+σ²) do not depend on a, which only spreads that capacity over lags; recalling the input k steps back is best at a = √(k/(k+1)), and noise added at the readout makes capacity rise monotonically toward a = 1'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation for white input of variance s² and white
  state noise of variance σ², independent, with |a| < 1: that the squared
  correlation between x(t) and u(t−1−k) is a^(2k)(1−a²)s²/(s²+σ²), that
  its sum over k ≥ 0 is s²/(s²+σ²), that a^(2k)(1−a²) is maximized at
  a² = k/(k+1), or that with independent readout noise of variance ρ the
  sum is s²/(s²+σ²+ρ(1−a²)). A nonlinear or multivariate reservoir in
  which the gain does trade memory against noise is outside the claim.
tags:
- complex-systems
- information-theory
- control-theory
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  A correction to A15 §2 of the exchange "Rich Get Richer Power Laws",
  and the gap it leaves. A illustrates a memory–noise tradeoff with
  x(t+1) = a x(t) + u(t) + η(t): as a → 1 memory half-life and noise
  variance both diverge, so "criticality amplifies both information and
  uncertainty". Input and noise enter through the same filter, so the
  state's signal-to-noise ratio is s²/σ² at every a, and the total linear
  memory capacity, summed over lags, is s²/(s²+σ²) at every a: the gain
  redistributes a fixed capacity across lags and trades nothing against
  noise. An interior optimum appears only for a task that weights lags:
  for recall k steps back it is a = √(k/(k+1)). With readout noise,
  capacity rises toward a = 1. Checked analytically and by simulation.
  The wording is the assistant's (Claude, in this session); adopting it
  is the owner's call.
bears_on:
- QUESTION-507
grounds:
- THEORY-2158
---
<!-- inactive-ok-file: THEORY-2158 ARG-146 — Proposed; the reading of Dambre and colleagues and its argument, 2026-11-21 -->

<!-- inactive-ok-file: THEORY-tmpye6xs CLAIM-809 — Proposed or new; the reading of Azizpour and colleagues, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-tmps8t83 LIT-2991 — Proposed or Unavailable; the reading of the NIPS 2004 companion and the work it stands in for, 2026-11-22 -->

# CLAIM-814: In the scalar linear reservoir x(t+1) = a x(t) + u(t) + η(t), the gain a does not trade memory against noise: the state's signal-to-noise ratio and its total linear memory capacity s²/(s²+σ²) do not depend on a, which only spreads that capacity over lags; recalling the input k steps back is best at a = √(k/(k+1)), and noise added at the readout makes capacity rise monotonically toward a = 1

## The gap it fills

A15 §2: "The same feedback that helps the network remember useful
signals also makes it retain unwanted disturbances … This gives us the
central tension: Long memory (benefit) ↔ Accumulated noise (cost).
Criticality amplifies both information and uncertainty. The optimal
setting therefore depends on what the system is trying to compute." The
half-life and the variance σ²/(1 − a²) are right. The tension is not
there: the model has no step from "both diverge" to "there is an
optimum", and in this model none exists for the measure A has in mind.

## The derivation

Let u and η be independent white sequences of variance s² and σ², and
|a| < 1. Then x(t) = Σ_{j≥0} a^j (u(t−1−j) + η(t−1−j)).

- **Signal-to-noise.** The input's share of Var x is s²/(1 − a²), the
  noise's σ²/(1 − a²); their ratio is s²/σ² at every a.
- **Memory function.** The best linear readout of u(t−1−k) from the
  scalar x(t) recovers a fraction
  m_k = Cov(x, u_{t−1−k})² / (Var x · s²) = a^(2k)(1 − a²) s²/(s² + σ²)
  of its variance.
- **Total capacity.** Σ_{k≥0} m_k = s²/(s² + σ²), independent of a. At
  σ = 0 it is 1, the number of state variables: the scalar case of the
  bound A attributes to Dambre and colleagues ([LIT-2971](../literature.d/LIT-2971.md), read 2026-11-21:
  the equality case of their Theorem 7, see the dated note), and
  of Jaeger's earlier bound on linear memory capacity, not registered.
- **Where the gain matters.** It moves capacity between lags: at a = 0.5,
  m_0 = 0.75 and m_10 ≈ 0 (σ = 0); at a = 0.99, m_0 = 0.020 and
  m_10 = 0.016. A task that needs the input k steps back is served best
  at a² = k/(k + 1), from maximizing a^(2k)(1 − a²): a = 0.71 for k = 1,
  0.91 for k = 5, 0.95 for k = 10, 0.995 for k = 100. Long-lag tasks push
  the optimum toward the stability edge without reaching it.
- **Readout noise.** If the readout sees y = x + ν with ν of variance ρ,
  independent, Σ m_k = s²/(s² + σ² + ρ(1 − a²)), which rises
  monotonically toward a = 1: amplification beats a fixed readout noise.
  Here nearness to the edge helps and nothing trades against it.

So what A's conclusion needs, an optimum that depends on the task, comes
from the allocation of a fixed capacity over lags, not from a tradeoff
between memory and noise.

## Check

The assistant checked each step (a numpy script of this session, not
kept; the method is as stated). Analytic sums: total capacity 1.0000,
0.8000 and 0.5000 for σ² = 0, 0.25 and 1 (s² = 1) at each of a = 0.5,
0.9 and 0.99. Simulation of 400,000 steps at a = 0.9, σ² = 0.25: summed
squared sample correlations over 60 lags, 0.792 against 0.800. The
argmax of a^(2k)(1 − a²) on a grid of 200,001 points matched √(k/(k+1))
to four places for k = 1, 5, 10, 100. Readout noise ρ = 0.5, 600,000
steps: 0.616 against 0.615 at a = 0.5 and 0.748 against 0.743 at a = 0.9;
at a = 0.99 a run that short overshot (0.829 against 0.794), and three
runs of 4,000,000 steps summed over 1,500 lags gave 0.804, 0.795 and
0.797 against 0.794.

## What it does not say

- Not that nonlinear reservoirs behave so. A nonlinear φ converts some
  linear memory into nonlinear capacity, which is Dambre and colleagues'
  point; the scalar linear case only shows the redistribution in its
  simplest form.
- Not that a multivariate linear reservoir has no tradeoff: with N state
  variables and noise that does not share the input's direction, the
  allocation is richer. The claim is about A's model.

## Note of 2026-11-21: Dambre, Verstraeten, Schrauwen and Massar, read

Dambre and colleagues' paper ([LIT-2971](../literature.d/LIT-2971.md)) was read in full with its
supplement ([NOTE-2244](../notes.d/NOTE-2244.md); the reading is [THEORY-2158](../theory.d/THEORY-2158.md)). It **supports**
the claim, which turns out to be **a case of its Theorem 7** ([ARG-146](../arguments.d/ARG-146.md)).

- With |a| < 1 the reservoir has fading memory and N = 1. Count η as the
  paper's second i.i.d. input v: x lies in the span of the degree-one
  functions of u and η, and over the full basis the capacities sum to 1 at
  every a, u's share being s²/(s² + σ²) and η's σ²/(s² + σ²). The paper:
  "It is only over the full space that Theorem 7 holds and that the
  capacities will sum to N. However since v is unknown, the capacities
  which are measurable are those which depend only on u."
- "The scalar case of the bound" understates it: it is the equality case.
  The independence from a is the theorem's, since its conditions hold
  throughout |a| < 1 and fail at a = 1.
- At σ² = s² the u-share is ½ = N/K with K = 2, the paper's linear
  benchmark (Fig. 4).
- The paper's capacity has no bias term; with zero-mean u and η that
  changes nothing. Gaussian input is within its theory (it names Hermite
  bases for it).
- The readout-noise result is not in the paper; it is consistent with it if
  ν is a third input that enters only the observation. Nothing in the
  paper bears on the lag optimum a² = k/(k + 1).

[THEORY-2158](../theory.d/THEORY-2158.md) replaces [LIT-2971](../literature.d/LIT-2971.md) in `grounds`. Status unchanged.

## Note of 2026-11-22: Azizpour, Priesemann, Zierenberg and Levina, read

A contrast, not evidence for or against the computation here ([NOTE-tmporpz2](../notes.d/NOTE-tmporpz2.md),
[THEORY-tmpye6xs](../theory.d/THEORY-tmpye6xs.md)). In this claim's scalar reservoir input and state noise
share one filter, and noise added at the readout makes capacity rise
monotonically toward a = 1. In Azizpour and colleagues' branching network
the readout also carries Gaussian noise, but the binding obstacle is the
network's own fluctuations, which grow relative to the signal and slow
down near λ = 1 and are not averaged out within a finite window T; the
optimum is then subcritical and approaches the transition only as
T → ∞. The two cases move the optimum in opposite directions for
different reasons; [CLAIM-809](CLAIM-809.md) now says so (version 2). No relation is
written. The note is the assistant's (Claude, in this session).

## Note of 2026-11-22: Natschläger, Bertschinger and Legenstein, read

**A contrast**, no edge ([LIT-tmpdsowv](../literature.d/LIT-tmpdsowv.md), read in [NOTE-tmpi5t3r](../notes.d/NOTE-tmpi5t3r.md) in place of
Bertschinger and Natschläger, [LIT-2991](../literature.d/LIT-2991.md); [THEORY-tmps8t83](../theory.d/THEORY-tmps8t83.md)). The system is
nonlinear, high-dimensional and binary, and its edge is damage spreading,
not the marginal linear stability of a scalar map. In this claim's model
there is no chaotic side; there, what is lost past the edge is fading
memory, the state carrying "spurious" information about initial
conditions, a cost a linear model cannot show. Nothing in the reading
bears on the scalar derivation. [CLAIM-809](CLAIM-809.md) now sets the three cases side by
side (version 3). The note is the assistant's (Claude, in this session).
