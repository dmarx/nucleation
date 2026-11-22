---
number: 841
status: Proposed
formerly:
- CLAIM-tmpsr8r4
title: 'A power law or a scale-invariant law does not by itself indicate criticality: symmetry, flux, growth, coarsening, geometry and broad relaxation spectra each remove a characteristic scale without a tuned transition'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Broido and Clauset (LIT-2963)
    was read: the folded-in bullet "Many reported scale-free networks
    are not" is reworded to what the paper shows, a lack of statistical
    evidence, and marked as background to the thesis, since the paper
    never mentions criticality (ARG-tmp38kft). The thesis and status are
    unchanged.
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
- TERM-142
- TERM-139
bears_on:
- QUESTION-508
grounds:
- THEORY-543
- THEORY-1085
- LIT-2978
- LIT-2982
- LIT-2969
- LIT-2985
- LIT-2970
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
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmpw4qgu THEORY-tmphcnj3 ARG-tmp38kft — Proposed; the readings of 2026-11-22 and the argument on this claim's network bullet -->
<!-- inactive-ok-file: LIT-tmpvmrkv — Deferred; the reply disputing Broido and Clauset, registered and unread -->
<!-- inactive-ok-file: TERM-139 CLAIM-846 — filed with this claim on 2026-11-21 -->
<!-- inactive-ok-file: LIT-2978 LIT-2982 LIT-2969 LIT-2985 LIT-2970 LIT-2992 — registered 2026-11-21, Deferred, unread -->
<!-- inactive-ok-file: CLAIM-769 — Proposed; power-law relaxation from a spread of rates -->
<!-- inactive-ok-file: CLAIM-803 CLAIM-795 — filed from the same exchange on 2026-11-21, Proposed -->

# CLAIM-841: A power law or a scale-invariant law does not by itself indicate criticality: symmetry, flux, growth, coarsening, geometry and broad relaxation spectra each remove a characteristic scale without a tuned transition

## The routes

A27 §8's table, with the routes A adds in A10, A24 and A26. "Criticality"
here is a transition reached by tuning a control parameter
([TERM-139](../terms.d/TERM-139.md): a fixed point with relevant directions).

| Route | Why no intrinsic scale | Tuned? | Where |
|---|---|---|---|
| Criticality | correlation length diverges at a transition | yes | A6 §2, A8 §1 |
| Broken continuous symmetry | no θ² restoring term, so long-wavelength cost ∝ k²; transverse C(r) ∝ r^(−(d−2)) through the ordered phase | no | A27 §2–3 |
| Line of fixed points (2D XY) | marginal direction; C(r) ∝ r^(−η(T)), η = T/2πρ_s, over a range of T | no | A12 §7, A27 §5; [LIT-2969](../literature.d/LIT-2969.md) |
| Nonequilibrium growth (KPZ) | W(L, t) = L^α F(t/L^z), α = ½, z = 3/2 in 1D, generically | no | A24 §3; [LIT-2978](../literature.d/LIT-2978.md), [LIT-2982](../literature.d/LIT-2982.md) |
| Sustained flux (turbulence) | constant transfer rate across the inertial range | no | A23 §2 |
| Ordered active matter | giant number fluctuations, ΔN ∝ ⟨N⟩^φ with φ > ½, in the ordered phase | no | A26 §4, A27 §7; [THEORY-1085](../theory.d/THEORY-1085.md), [LIT-2970](../literature.d/LIT-2970.md) |
| Coarsening | L(t) ∝ t^(1/2) (nonconserved) or t^(1/3) (conserved), well below T_c | no | A26 §3 |
| Cumulative advantage | growth with attachment ∝ size | no | A1, A27 §8 |
| Geometric recursion | a fractal; Sierpiński D = log 3/log 2 = 1.585 | no | A10 §3 |
| Broad relaxation spectra | a superposition of exponentials over a wide spread of rates | no | A23 §7, A27 §8; [CLAIM-769](CLAIM-769.md) |
| Brownian motion | B(at) =d √a B(t) | no | A10 §6 |

The derivations A gives were rechecked: the BKT exponent from
⟨Δθ²⟩ = (T/πρ_s) ln r gives exp(−½⟨Δθ²⟩) = r^(−T/2πρ_s); the 2D
infrared integral ∫k^(d−3) dk diverges logarithmically (Mermin–Wagner,
[LIT-2985](../literature.d/LIT-2985.md)); an explicit field μ²θ² gives ξ = √ρ_s/μ; KPZ's z = α/β =
(½)/(⅓) = 3/2, so a tenfold length is 10^1.5 = 31.6-fold in time against
100-fold for diffusion (A24 §6); 1D directed percolation's
ν∥/ν⊥ = 1.7338/1.0969 = 1.581 (A24 §2). The Gaussian spin-wave route is
checked numerically in [CLAIM-846](CLAIM-846.md).

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
- **Many networks reported as scale free show little statistical
  evidence of it** (A10 §6, corrected on 2026-11-22), which A attributes
  to "rigorous studies", plainly Broido and Clauset (LIT-2963). A said
  they "are not"; the paper shows a lack of evidence, many "may in fact
  be log-normal networks", and its verdict is disputed (LIT-tmpvmrkv).
  The paper never mentions criticality, so this bullet is background to
  the thesis, not a ground of it (ARG-tmp38kft).

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
tails at all. [LEAD-209](../leads.d/LEAD-209.md) proposes making this a protocol.

Two neighbours filed from the same exchange: [CLAIM-803](CLAIM-803.md) holds that a
power-law distribution does not identify its mechanism, and [CLAIM-795](CLAIM-795.md)
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
  open part of [QUESTION-508](../questions.d/QUESTION-508.md).

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
  Wiesenfeld, [LIT-2992](../literature.d/LIT-2992.md)), and whether a given system takes it is
  [QUESTION-508](../questions.d/QUESTION-508.md).

## Change of 2026-11-22

The bullet "Many reported scale-free networks are not" now reads "Many
networks reported as scale free show little statistical evidence of it",
and is marked as background, not a ground (ARG-tmp38kft). Version 2.

## Note of 2026-11-22: Newman, read

Newman's review (LIT-2976, read in NOTE-tmpa7yd2; the reading is
THEORY-tmp6jdas) **supports the distributional half** of the thesis:
"most experimentally observed power laws are probably not the result of
phase transitions—a variety of other mechanisms produce power-law
behaviour as well" (§III.E, p. 12), and tuning "makes the divergence of
length-scales an unlikely explanation for generic power-law
distributions" (§IV.E, p. 19). It **leaves open** the routes listed here
(symmetry, a line of fixed points, KPZ, flux, coarsening), none of which
is in the review; its own routes (the Yule process, combinations of
exponentials, inverses, walks, highly optimized tolerance) touch only the
"cumulative advantage" and "broad relaxation" rows, loosely.
THEORY-tmp6jdas `corroborates` the claim.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

A **parallel** (LIT-2987, NOTE-tmphbwdu, THEORY-tmpw4qgu). The power law
with an exponential cutoff is "clearly favored" for fires, flares and
earthquakes (p. 26), the classic self-organized-criticality cases, and the
pure power law is "firmly ruled out" for earthquakes (p. 23): the shape
offered as evidence of criticality often is not a pure power law at all.
No edge.

## Note of 2026-11-22: Broido and Clauset, read

**No bearing on the thesis; qualifies the folded-in bullet** (LIT-2963,
NOTE-tmpleyjh, THEORY-tmphcnj3; ARG-tmp38kft, Rejected as a route). The
paper never mentions criticality or any route listed here; it doubts that
the power law is there at all, before any question of what it indicates.
It was never in `grounds`, and stays out. Status unchanged.
