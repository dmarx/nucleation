---
status: Proposed
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
supports:
- CLAIM-tmpask80
grounds:
- LIT-tmp7sbn6
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
---
<!-- inactive-ok-file: CLAIM-tmpask80 ARG-tmpubyzo QUESTION-tmp2hhlc — filed with this claim from the same exchange, Proposed or Open -->
<!-- inactive-ok-file: LIT-tmp7sbn6 — Deferred, registered 2026-11-21 from the exchange, unread -->

# CLAIM-tmpd1shn: In the scalar linear reservoir x(t+1) = a x(t) + u(t) + η(t), the gain a does not trade memory against noise: the state's signal-to-noise ratio and its total linear memory capacity s²/(s²+σ²) do not depend on a, which only spreads that capacity over lags; recalling the input k steps back is best at a = √(k/(k+1)), and noise added at the readout makes capacity rise monotonically toward a = 1

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
  bound A attributes to Dambre and colleagues (LIT-tmp7sbn6, unread), and
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
