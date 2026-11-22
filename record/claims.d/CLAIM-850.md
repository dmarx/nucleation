---
number: 850
status: Proposed
formerly:
- CLAIM-tmpyy261
title: 'Chaos, criticality and a cascade through scales are distinct properties, and each can occur without either of the others; they meet only through particular mechanisms, such as the period-doubling accumulation point, which is critical in the renormalization-group sense and not chaotic'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A proof that one of the three entails another in a class of systems
  where all three definitions below apply (for instance, that a positive
  Lyapunov exponent forces a diverging correlation length or time, or that
  a sustained flux through a range of scales forces one); or a showing that
  one of the six separating constructions below does not meet the
  definition it is offered for, with no other construction to replace it.
  Not defeated by systems in which two or three co-occur, such as
  turbulence: the claim is that co-occurrence comes from mechanism, not
  from entailment.
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-21'
line:
- formal-apparatus
answers:
- QUESTION-516
uses:
- TERM-142
- TERM-139
complements:
- CLAIM-810
grounds:
- THEORY-1332
- THEORY-754
summary: >-
  Answers the chaos half of the owner's U4 ([QUESTION-516](../questions.d/QUESTION-516.md)). A6 §1 gave
  chaos, criticality and self-similarity as distinct with "none
  automatically implies the others"; A23 §8 gave critical correlation and
  dynamical cascade as distinct, "neither logically requires the other";
  A12 §9 that "microscopic unpredictability and macroscopic mathematical
  regularity ... can coexist". This claim joins the three and supplies a
  checked separating construction for each of the six implications, and
  the checked mechanisms where they meet: the period-doubling accumulation
  point (Lyapunov exponent zero, δ = 4.669201), type-I intermittency (mean
  laminar length ∝ ε^(−1/2)) and turbulence. Fills the ledger gap that the
  record had no claim relating them. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-142 TERM-139 CLAIM-810 CLAIM-846 ARG-129 — filed with this claim on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2041 — Proposed; the order-to-chaos transition in random deep networks -->
<!-- inactive-ok-file: THEORY-2158 CLAIM-809 — Proposed; the reading of 2026-11-21 and the claim it bears on -->

<!-- inactive-ok-file: NOTE-tmporpz2 THEORY-tmpye6xs LIT-tmpfn6b8 — Proposed or new; the reading of Azizpour and colleagues, 2026-11-22, and the Deferred work it names -->

# CLAIM-850: Chaos, criticality and a cascade through scales are distinct properties, and each can occur without either of the others; they meet only through particular mechanisms, such as the period-doubling accumulation point, which is critical in the renormalization-group sense and not chaotic

## Definitions

- **Chaos**: deterministic dynamics with a positive largest Lyapunov
  exponent on a set of positive measure (A6 §1; [THEORY-1332](../theory.d/THEORY-1332.md) on chaos as a
  property of deterministic dynamics).
- **Criticality**: a diverging correlation length or time, at a fixed
  point of a renormalization-group map ([TERM-139](../terms.d/TERM-139.md)), reached by tuning
  or otherwise (A6 §2, A8 §1).
- **Cascade**: a sustained net transfer of a conserved quantity through a
  range of scales, at a rate independent of scale across that range
  (A23 §2, §8); [THEORY-754](../theory.d/THEORY-754.md) holds the locality of such transfer in
  turbulence.

## The six separations

Each was checked with `python3 -I`.

| Has | Lacks | Construction | Check |
|---|---|---|---|
| chaos | criticality, cascade | logistic map at r = 4 (A6 §5) | Lyapunov exponent 0.693147 over 10⁶ iterates (ln 2 = 0.693147); invariant density 1/(π√(x(1−x))), KS distance 0.0004; autocorrelation within ±0.002 at lags 1–5. The correlation time is one step, and there are no scales to transfer between. |
| criticality | chaos | the period-doubling accumulation point r_∞ | superstable parameters to period 2¹² give r_∞ = 3.5699457; Lyapunov exponent there 3 × 10⁻⁶, against −0.87 at r = 3.5 and +0.18 at 3.6; the period, the orbit's correlation time, diverges as (r_∞ − r)^(−ln 2/ln δ) = (r_∞ − r)^(−0.4498). Also the critical Galton–Watson process and the Ising model at T_c, which are stochastic and have no deterministic Lyapunov exponent at all. |
| criticality | cascade | equilibrium 2D Ising at T_c | detailed balance makes every probability current zero (A24 §1), so nothing is transferred through scales although C(r) ∝ r^(−1/4). Equally the scale-free Gaussian field of [CLAIM-846](CLAIM-846.md), which has no flux, for the reason [CLAIM-810](CLAIM-810.md) gives. |
| cascade | criticality | turbulent inertial range (A23 §2, §8) | generic at high Reynolds number, with no parameter tuned to a point: "scale invariance can emerge from a sustained nonequilibrium flux rather than conventional critical tuning". |
| cascade | chaos | a linear chain of 20 shells, k_n = 2ⁿ, transfer rate k_n^(2/3) from shell n to n+1, dissipation νk_n², injection into shell 0 | steady flux 1.000 through every shell of the range; shell energy ∝ k^(−2/3), so E(k) ∝ k^(−1.667); every eigenvalue of the linear dynamics has real part ≤ −1, so no chaos and no tuning. |
| chaos | cascade | the logistic map again | one variable, no scales. |

So none of the six implications holds. A6's table already said "none
automatically implies the others" for chaos, criticality and
self-similarity, without constructions; A23 §8 said it for critical
correlation and cascade. The cascade-without-chaos row is the
assistant's; it answers the objection that the turbulent cascade is
chaotic, so its scaling might come from chaos.

## Where they meet

They co-occur through particular mechanisms, which is why the owner's
link is apt and why it is not an identity.

- **The onset of chaos by period doubling is critical.** A6 §3–4: "the
  transition into chaos can itself be a critical phenomenon, with
  self-similarity and scaling laws." Checked: the ratios of successive
  superstable spacings converge to δ = 4.669201 by period 2¹², and the
  ratio of successive distances from x = ½ to the nearest cycle point to
  −2.50291, Feigenbaum's α. Both are fixed-point data of the doubling
  operator and are the same for unimodal maps with a quadratic maximum
  (Feigenbaum's constants, named in the exchange and not registered as a
  work). The critical point is the boundary of chaos, not chaos: its
  Lyapunov exponent is zero. [ARG-129](../arguments.d/ARG-129.md) weighs A6's analogy between this
  and a thermal critical point.
- **Intermittency near a tangent bifurcation** (A6 §5, Pomeau–Manneville,
  named and not registered). Checked on the logistic map just below the
  period-3 window, r = 1 + √8 − ε: the mean length of laminar phases grows
  from 6.3 at ε = 10⁻³ to 68 at ε = 10⁻⁵, a log-log slope of −0.515,
  against the type-I law ε^(−1/2). Here chaos carries a power law in its
  distance from a transition. A6's hedge, "power-law statistics or
  power-law scaling with distance from the transition", is right: in type
  I it is the mean that scales, not the distribution of lengths.
- **Turbulence** is chaotic and a cascade at once, and its inertial range
  is scale-free. Its scaling is attributed to the flux (A23 §2), not to the
  chaos; the linear chain above shows the flux alone suffices for the
  spectrum.
- **The order-to-chaos transition in wide random networks** ([THEORY-2041](../theory.d/THEORY-2041.md))
  is another case of the first kind: a depth scale diverges at the
  boundary of chaos.

## Self-similarity

The owner's second link holds in one sense. Self-similarity is
[TERM-142](../terms.d/TERM-142.md)'s sense 2. It comes with criticality (statistical
self-similarity at a fixed point, A6 §2) and with the onset of chaos (the
attractor at r_∞ is a Cantor set rescaled by α at each level). Chaos
itself neither needs it nor excludes it: the attractor of the logistic
map at r = 4 is the whole interval, while the attractors of the Hénon and
Lorenz systems are fractal. Chaos does not give heavy-tailed outcomes
either; at r = 4 the variable is confined to [0, 1] (A6 §5: "sensitivity
to initial conditions does not automatically produce power-law-distributed
outcomes").

## What it does not say

- That the three are unrelated. The claim is that every link between them
  runs through a mechanism, which must be named in each case.
- That "edge of chaos" is a general optimum. A6 closes on this: "an
  interesting hypothesis in some complex systems, but it is not a
  universal mathematical theorem." Whether being near such a boundary aids
  computation is the computational question filed elsewhere from this
  exchange.
- That statistical regularity needs predictable trajectories. A12 §9's
  point stands: a law can be stable under rescaling while each trajectory
  is unpredictable.

## Note of 2026-11-21: Dambre, Verstraeten, Schrauwen and Massar, read

A **contrast**, no edge. Dambre and colleagues ([LIT-2971](../literature.d/LIT-2971.md), read in
[NOTE-2244](../notes.d/NOTE-2244.md); [THEORY-2158](../theory.d/THEORY-2158.md)) put their reservoirs "close to the edge of
stability" and measure capacity up to and past the undriven system's
bifurcation. That edge is a third thing beside this claim's three: the
loss of linear stability of a fixed point (spectral radius 1 for the echo
state network), marginal stability, which is neither chaos nor
criticality in the claim's senses, though the logistic map's route
continues to the period-doubling accumulation point the claim names. The
reading's bearing on computation is filed on [CLAIM-809](CLAIM-809.md).

## Note of 2026-11-22: Azizpour, Priesemann, Zierenberg and Levina, read

Weak support, by statement (NOTE-tmporpz2, THEORY-tmpye6xs). The paper
distinguishes "absorbing-to-active, transition to chaos, or a
bifurcation" as transitions whose optimal side can differ, citing
Toyoizumi and Abbott (LIT-tmpfn6b8, registered, Deferred) for the chaos
side. It treats branching criticality only, and does not show that the
three are distinct properties; no relation is written.
