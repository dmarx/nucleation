---
status: Read
paper: 'LIT-tmpw9g80'
title: 'Obayashi, Aoi, Tsuchiya and Kokubu — The basin of attraction of passive dynamic walking'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from the authors' arXiv v3 (11 January 2016), 17
    pp., CC BY 4.0, https://arxiv.org/pdf/1407.5720v3, extracted with
    pdftotext -layout. Read: the main text, §§1–5. Read by caption only:
    the figures. Scanned only: the references. The published version in
    Proc. R. Soc. A was not compared. Registered and read as a stand-in for
    McGeer (1990), LIT-tmpv6ctd, at the owner's request. Quotes checked by
    string match against the extracted text.
date: '2026-11-05'
summary: >-
  In the simplest passive walking model, the states that take at least one
  step form a long thin domain, and its pull-backs under the step map
  nest down to a basin of attraction that is very small, thin, V-shaped
  and fractal-like. The authors trace this to the saddle-centre upright
  equilibrium: near its stable manifold the pull-backs are thinned, and
  non-uniform deformation folds them. Past a slope of about 0.019 the
  attractor is destroyed by a boundary crisis.
---
<!-- inactive-ok-file: LIT-tmpv6ctd THEORY-tmpabuss THEORY-1052 — Unavailable or Proposed, and new or held; cited from the reading of Obayashi et al. (2016) as open -->

# NOTE-tmpescek: Obayashi, Aoi, Tsuchiya and Kokubu — The basin of attraction of passive dynamic walking

## Contribution

A dynamical-systems explanation, from the saddle-type hyperbolicity of the
upright posture, of why passive walkers' basins of attraction are small,
thin and fractal-like, which the authors take to explain why stable passive
walking is hard to produce.

## Key insight

The stance leg is an inverted pendulum, and an inverted pendulum falls.
Pulling the set of states that survive a step back through the step map
squeezes it along the saddle's stable manifold, so the states that keep
walking form an ever thinner, folded set around the gait.

## Assumptions

- **Garcia et al.'s simplest walking model** in the limit β = m/M → 0, so
  the stance-leg equation decouples (θ̈₁ = sin(θ₁ − γ)), on a slope γ, with
  no actuation or control.
- **Fully inelastic, instantaneous foot contact**; scuffing ignored by
  conditions (2.4)–(2.5).
- **Basin computed numerically**: a point counts as in the basin when 50
  and 200 steps give the same result; partial analytic support from a
  linearisation about the equilibrium.

## Key results

- **McGeer's idea** (§1, p. 2): "Passive dynamic walking, a popular dynamic
  system that is based on the inverted pendulum mechanism, was proposed by
  McGeer [13,14]. This system walks down a shallow slope without an
  actuator or controller; it does this by balancing the energy dissipation
  due to foot contact with the energy generation due to the gravitational
  potential energy."
- **The difficulty** (§1, p. 2): "Due to the properties of the saddle point
  in the governing dynamics, an inverted pendulum falls down easily."
- **The construction** (§2b, p. 4): "We define the domain D as the
  collection of initial conditions for which the model takes at least one
  step." Its inverse images: "These regions indicate the collections of
  initial conditions for which the model takes at least (n + 1) steps."
- **The basin** (abstract): "The basin of attraction is very small and
  thin, and it has a fractal-like shape"; V-shaped, with slits and stripes
  (§3).
- **The mechanism** (§4a–c): the upright equilibrium is a saddle-centre;
  by the λ-lemma, regions pulled back near its stable manifold are thinned,
  and non-uniform deformation near the centre-unstable manifold makes the V
  and, iterated, the slits and stripes.
- **Dependence on slope** (§2b, p. 4, citing Garcia et al.): they "found
  that S has an attracting fixed point at 0 < γ < 0.015, and there is a
  period-doubling cascade to chaos for 0.015 < γ < 0.019."
- **Loss of the gait** (§4d, p. 14): near γ ≈ 0.019 the attractor meets the
  basin boundary, "the attractor breaks down, and the model no longer
  continues walking."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The simplest walking model's basin is very small, thin and fractal-like | moderate to strong: numerical | §3, Figs. 5–8 |
| C2 | Its shape comes from the saddle-type hyperbolicity of the upright equilibrium | moderate: argued from a linearisation, the λ-lemma and figures, not proved | §4a–c |
| C3 | Past a slope near 0.019 the attractor is destroyed by a boundary crisis | moderate: numerical | §4d |

## Concepts

- **Domain D**, the states that take at least one step; its **inverse
  images** S⁻ⁿ(D), those that take at least n + 1; and the **basin** B,
  approximated by their intersection.
- **Centre-stable and centre-unstable manifolds** of the saddle-centre
  equilibrium (§2c).
- **Boundary (attractor) crisis**: the attractor meets the basin boundary
  and is destroyed (§4d).

## Connections

It credits McGeer (1990), [LIT-tmpv6ctd](../literature.d/LIT-tmpv6ctd.md), with proposing passive dynamic
walking and restates of his work only the idea and its energy balance,
result 1 above. The model is Garcia et al.'s 1998 simplification of a
compass walker, and the stability findings it builds on are later work's
(Garcia et al. 1998; Schwab and Wisse 2001). None of McGeer's specific
models, results or experiments is restated.

## Bearing on the record

- **The pasted synthesis on constraint architectures**, on McGeer (1990):
  "stable gait cycles driven by gravity and their own dynamics." Right as
  the idea. Missing, and important for A's use: the stable cycle's basin is
  very small and thin, and the cycle exists only in a narrow range of slope.
- **[CLAIM-079](../claims.d/CLAIM-079.md)** (stability does not entail viability): supports, with a
  sharp mechanical case. The gait is an asymptotically stable attractor,
  yet almost every nearby state falls, and a slow increase of slope destroys
  it by crisis. The fit is partial: [CLAIM-079](../claims.d/CLAIM-079.md) is about losing access to
  viable trajectories while in the regime; here states inside the basin
  keep their access, and the fragility is that the basin is thin.
- **[THEORY-134](../theory.d/THEORY-134.md)** (viability kernel): supports in method. D and its nested
  pull-backs are a discrete-time viability-kernel construction for the
  constraint of not falling, and the basin is the attracting part within it.
  The paper does not use the word viability.
- **[THEORY-1052](../theory.d/THEORY-1052.md)** (quasi-static attractors and rate-induced tipping):
  qualifies rather than supports. The crisis is parameter-induced loss of
  an attractor, not rate-induced.
- [THEORY-136](../theory.d/THEORY-136.md) and [CLAIM-463](../claims.d/CLAIM-463.md) are unrelated: no claim about abrupt change as
  evidence, and no hysteresis studied.
- Filed: [THEORY-tmpabuss](../theory.d/THEORY-tmpabuss.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **The authors'**: other walking models may have differently shaped
  basins, though the saddle mechanism should be shared (§5); control to
  enlarge the basin is left to future work.
- **One idealised model in a singular limit.**
- **Numerical basins** judged by finite numbers of steps.
- **The mechanism is argued**, from a linearisation and figures, not
  proved.

## Open questions

- Do walkers with knees, mass in the legs, or McGeer's own models share
  the thin, folded basin? The authors expect so; computing their basins
  would say.
- How much does a little control enlarge the basin, and at what cost?
