---
status: Proposed
title: 'The period-doubling route to chaos and a thermal critical point share the structure of a renormalization-group fixed point with one relevant direction, so the analogy is formal, though not every row of the exchange''s table pairs like with like'
version: 1
form: analogy
grounds:
- THEORY-777
concludes:
- CLAIM-tmpyy261
uses:
- TERM-tmpt3vht
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  Weighs A6 §3–4 of the exchange "Rich Get Richer Power Laws": its table
  pairing a thermal transition with the period-doubling transition, and
  its claim that "The connection isn't merely metaphorical. The same broad
  mathematical framework—renormalization—explains both phenomena." The
  analogy holds at the level of a fixed point of a renormalization map
  with one relevant direction to tune, and supports CLAIM-tmpyy261's
  clause that the onset of chaos is critical. Two rows of the table pair
  unlike things: δ is the relevant eigenvalue, not an exponent (the
  exponent is ln 2/ln δ = 0.4498), and the self-similar bifurcation
  diagram lives in parameter space, not in the state. Proposed: supported
  with those corrections. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpyy261 TERM-tmpt3vht — filed with this argument on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-777 — Proposed; relevant directions found at the 2D Ising fixed point -->

# ARG-tmp92gzv: The period-doubling route to chaos and a thermal critical point share the structure of a renormalization-group fixed point with one relevant direction, so the analogy is formal, though not every row of the exchange's table pairs like with like

## The inference

1. A thermal critical point is a fixed point of a renormalization map on
   Hamiltonians, with relevant directions that must be tuned (temperature,
   and the field, held at zero by symmetry). Near it, quantities scale with
   exponents set by the relevant eigenvalues, ν = 1/y_t, and systems in
   its basin share them (TERM-tmpt3vht). THEORY-777 finds the two relevant
   directions of the 2D Ising point as the two stiff directions of the
   coarse-grained Fisher information.
2. The period-doubling accumulation point is a fixed point of the
   doubling operator on unimodal maps, f ↦ −α f(f(−x/α)), with one
   relevant direction; its eigenvalue is δ, and α is the rescaling of the
   state variable. Maps with a quadratic maximum lie in its basin and share
   δ and α (A6 §3–4, named as Feigenbaum's; the work is not registered).
3. So the two share a structure: a fixed point, one tuned direction,
   universal numbers read off the linearization, and a basin that is the
   universality class. The route to chaos is a critical phenomenon in
   TERM-tmpt3vht's sense, which is the clause of CLAIM-tmpyy261 this
   supports.

Checked (`python3 -I`): from superstable parameters up to period 2¹², the
spacing ratios converge to δ = 4.669201 and the scaling of the cycle near
x = ½ to α = −2.50291; r_∞ = 3.5699457, where the Lyapunov exponent is
3 × 10⁻⁶, zero to the precision of the run.

## Critical questions

- **Are they alike in the respect the conclusion needs?** Yes. The
  conclusion is that both are fixed points of a scale transformation with
  relevant directions, and that holds of both.
- **What relevant differences are there?**
  - The renormalization acts on a space of one-dimensional maps by
    composition and rescaling of x, not on spatial blocks of a many-body
    system. There is no spatial dimension, no thermodynamic limit, and no
    thermal noise; noise added to the map is a further perturbation of the
    fixed point.
  - The universality class is set by the order of the map's maximum, not
    by dimension and symmetry.
  - The period of the stable orbit is the map's correlation time, so
    A6's second row ("Correlation length becomes very large | Period of
    the stable orbit doubles repeatedly") pairs like with like.
- **Does the table pair corresponding items?** Not in two rows.
  - "Universal critical exponents emerge | Universal Feigenbaum constants
    emerge" pairs an exponent with an eigenvalue. δ corresponds to b^(y_t),
    the factor by which the relevant perturbation grows per step. The
    corresponding exponent is the divergence of the period as r → r_∞,
    (r_∞ − r)^(−ln 2/ln δ) = (r_∞ − r)^(−0.4498), the analogue of ν with
    b = 2.
  - "Fluctuations show scale invariance | Bifurcations show self-similar
    scaling" pairs a property of the state at the fixed point with the
    geometry of the bifurcation diagram, a property of the parameter
    space. The state-side analogue is the attractor at r_∞, a Cantor set
    self-similar under rescaling by α.
- **Is there a counter-analogy?** The thermal critical point has
  fluctuations at every scale in a stationary ensemble; at r_∞ there is
  one deterministic orbit and nothing fluctuates. So "critical" carries
  over as a statement about the renormalization map, not about
  fluctuations. That is why CLAIM-tmpyy261 places the meeting of chaos and
  criticality at a fixed point, and does not say that chaos produces
  critical fluctuations.

Proposed: A6's "not merely metaphorical" is supported at the level of the
renormalization map, with the two rows corrected as above.
