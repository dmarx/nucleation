---
status: Proposed
title: 'A power law or a scale-invariant law does not by itself indicate criticality: symmetry, flux, growth, coarsening, geometry and broad relaxation spectra each remove a characteristic scale without a tuned transition'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A showing that one of the routes listed below needs a parameter tuned to
  a transition after all, for each route, so that the list is empty; or an
  argument that the evidence ordinarily offered for criticality (a power
  law in one observable) does in fact discriminate it from these routes.
  Not defeated by the remark that every scale-invariant state is a fixed
  point of some renormalization-group map: the claim concerns tuning to a
  transition, not the existence of a fixed point (see "What it does not
  say").
tags:
- complex-systems
- natural-sciences
- thermodynamics
date: '2026-11-21'
line:
- formal-apparatus
uses:
- TERM-tmpyi882
- TERM-tmpt3vht
bears_on:
- QUESTION-tmp3lkep
grounds:
- THEORY-543
- THEORY-1085
- LIT-tmpd6yec
- LIT-tmpecowz
- LIT-tmp6l8le
- LIT-tmph28ji
- LIT-tmp71zbs
summary: >-
  A's, stated at A10 §6 ("Scale invariance is a mathematical property that
  can be produced by many different mechanisms. Criticality is one
  particularly important mechanism for generating it") and A23 §8 ("the
  word criticality is often used too broadly"), and built up over A24 §3,
  A26 §3–4, §6, §9 and A27 §6, §8 into a list of routes: broken continuous
  symmetry, a line of fixed points, nonequilibrium growth (KPZ), sustained
  flux, coarsening, cumulative advantage, geometric recursion, and broad
  relaxation spectra. The assistant adds what would show criticality
  instead, the three-state ring check of A24 §1, and two corrections. The
  wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A10, A23, A24, A26, A27); adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-tmpt3vht CLAIM-tmpwl8y8 — filed with this claim on 2026-11-21 -->
<!-- inactive-ok-file: LIT-tmpd6yec LIT-tmpecowz LIT-tmp6l8le LIT-tmph28ji LIT-tmp71zbs LIT-tmp1cgul LIT-tmpl2b2l — registered 2026-11-21, Deferred, unread -->
<!-- inactive-ok-file: CLAIM-769 — Proposed; power-law relaxation from a spread of rates -->
<!-- inactive-ok-file: CLAIM-tmp8h6nt CLAIM-tmp1dlyp — filed from the same exchange on 2026-11-21, Proposed -->

# CLAIM-tmpsr8r4: A power law or a scale-invariant law does not by itself indicate criticality: symmetry, flux, growth, coarsening, geometry and broad relaxation spectra each remove a characteristic scale without a tuned transition

## The routes

A27 §8's table, with the routes A adds in A10, A24 and A26. "Criticality"
here is a transition reached by tuning a control parameter
([TERM-tmpt3vht](../terms.d/TERM-tmpt3vht.md): a fixed point with relevant directions).

| Route | Why no intrinsic scale | Tuned? | Where |
|---|---|---|---|
| Criticality | correlation length diverges at a transition | yes | A6 §2, A8 §1 |
| Broken continuous symmetry | no θ² restoring term, so long-wavelength cost ∝ k²; transverse C(r) ∝ r^(−(d−2)) through the ordered phase | no | A27 §2–3 |
| Line of fixed points (2D XY) | marginal direction; C(r) ∝ r^(−η(T)), η = T/2πρ_s, over a range of T | no | A12 §7, A27 §5; [LIT-tmp6l8le](../literature.d/LIT-tmp6l8le.md) |
| Nonequilibrium growth (KPZ) | W(L, t) = L^α F(t/L^z), α = ½, z = 3/2 in 1D, generically | no | A24 §3; [LIT-tmpd6yec](../literature.d/LIT-tmpd6yec.md), [LIT-tmpecowz](../literature.d/LIT-tmpecowz.md) |
| Sustained flux (turbulence) | constant transfer rate across the inertial range | no | A23 §2 |
| Ordered active matter | giant number fluctuations, ΔN ∝ ⟨N⟩^φ with φ > ½, in the ordered phase | no | A26 §4, A27 §7; [THEORY-1085](../theory.d/THEORY-1085.md), [LIT-tmp71zbs](../literature.d/LIT-tmp71zbs.md) |
| Coarsening | L(t) ∝ t^(1/2) (nonconserved) or t^(1/3) (conserved), well below T_c | no | A26 §3 |
| Cumulative advantage | growth with attachment ∝ size | no | A1, A27 §8 |
| Geometric recursion | a fractal; Sierpiński D = log 3/log 2 = 1.585 | no | A10 §3 |
| Broad relaxation spectra | a superposition of exponentials over a wide spread of rates | no | A23 §7, A27 §8; [CLAIM-769](CLAIM-769.md) |
| Brownian motion | B(at) =d √a B(t) | no | A10 §6 |

The derivations A gives were rechecked: the BKT exponent from
⟨Δθ²⟩ = (T/πρ_s) ln r gives exp(−½⟨Δθ²⟩) = r^(−T/2πρ_s); the 2D
infrared integral ∫k^(d−3) dk diverges logarithmically (Mermin–Wagner,
[LIT-tmph28ji](../literature.d/LIT-tmph28ji.md)); an explicit field μ²θ² gives ξ = √ρ_s/μ; KPZ's z = α/β =
(½)/(⅓) = 3/2, so a tenfold length is 10^1.5 = 31.6-fold in time against
100-fold for diffusion (A24 §6); 1D directed percolation's
ν∥/ν⊥ = 1.7338/1.0969 = 1.581 (A24 §2). The Gaussian spin-wave route is
checked numerically in [CLAIM-tmpwl8y8](CLAIM-tmpwl8y8.md).

## A's further distinctions folded in

- **Structure is not scaling.** A Turing instability selects a band of
  wavenumbers and so a characteristic wavelength ℓ* = 2π/k* (A26 §2;
  [THEORY-543](../theory.d/THEORY-543.md)): "the emergence of structure and the emergence of scaling
  symmetry are two distinct phenomena." A26 §6 sorts the cases as scale
  selection (Turing), scale evolution (coarsening, whose dynamic scaling
  C(r, t) = F(r/L(t)) is "self-similar transformation, rather than a
  permanently scale-invariant state") and persistent multiscale
  organization (critical, turbulent, active). A26 §7 reads which case from
  the dispersion relation λ(k): negative everywhere, positive near some
  k* > 0, vanishing as k → 0, or positive over a broad band.
- **A histogram cannot name its mechanism** (A24 §1). Two processes can
  share a stationary distribution and differ in their currents. Checked: a
  three-state ring with rotation-symmetric rates 2 one way and 1 the other
  has stationary probabilities ⅓ each and a net current ⅓ on every edge;
  with equal rates the same distribution has none. "The same power-law
  distribution could be generated by an equilibrium critical system, a
  driven cascade, or an entirely different stochastic mechanism."
- **Order can be the reason for scale-free fluctuations** (A27 §10):
  "A particular kind of order can be the reason a system supports
  scale-free fluctuations"; and "A symmetry can protect scale-free
  fluctuations, and explicitly breaking that symmetry can introduce a
  characteristic scale" (A27 §6).
- **Many reported scale-free networks are not** (A10 §6), which A
  attributes to "rigorous studies", plainly Broido and Clauset
  ([LIT-tmp1cgul](../literature.d/LIT-tmp1cgul.md), unread).

## What would show criticality instead

A12 §8: "A heavy-tailed distribution alone doesn't tell us whether a system
is critical. But a set of consistent scaling relationships—across event
sizes, system sizes, correlations, and control parameters—can provide much
stronger evidence." The discriminating observations are a cutoff that
grows as a control parameter is moved (and not only with system size), a
data collapse P(s, L) = s^(−τ) f(s/L^D) across sizes, and exponents that
satisfy the scaling relations among several observables. A24 §9 adds that
the cutoff behaves differently by route: near criticality it grows on
approach, in turbulence it is set by the injection and dissipation
scales, and a KPZ interface has universal scaling without power-law
tails at all. [LEAD-tmpng7or](../leads.d/LEAD-tmpng7or.md) proposes making this a protocol.

Two neighbours filed from the same exchange: [CLAIM-tmp8h6nt](CLAIM-tmp8h6nt.md) holds that a
power-law distribution does not identify its mechanism, and [CLAIM-tmp1dlyp](CLAIM-tmp1dlyp.md)
lists mechanisms with no positive feedback. This claim is narrower in one
way and wider in another: it concerns criticality in particular, and
scale-covariant laws (correlations, spectra, dynamic scaling) as well as
distributions.

## Corrections to A's turns

- A24 §5 is headed "Three ways nonequilibrium systems produce universal
  scaling" and its table has four rows (directed percolation, KPZ,
  turbulent cascade, self-organized criticality).
- A12 §8's third row, "Stable scale-free dynamics", is not defined beyond
  the BKT example and as written cannot be told from "critical scaling".
  This claim reads it as scaling with no tuned direction, which is the
  open part of [QUESTION-tmp3lkep](../questions.d/QUESTION-tmp3lkep.md).

## What it does not say

- That these routes are outside renormalization theory. In RG terms every
  scale-invariant law sits at or near some fixed point; the Goldstone
  phase and the XY phase are fixed points, and KPZ is a nonequilibrium
  one. What separates them from a critical point is that nothing has to be
  tuned to reach them. So "critical" in the broad sense of "at an RG fixed
  point" is not what this claim denies; it denies that a power law shows
  a tuned transition.
- That self-organized criticality is ruled out. It is a route that ends at
  a critical point without outside tuning (A24 §4; Bak, Tang and
  Wiesenfeld, [LIT-tmpl2b2l](../literature.d/LIT-tmpl2b2l.md)), and whether a given system takes it is
  [QUESTION-tmp3lkep](../questions.d/QUESTION-tmp3lkep.md).
