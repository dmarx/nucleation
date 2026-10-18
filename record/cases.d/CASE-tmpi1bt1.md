---
status: Active
title: 'A fold in boundary maintenance: in ḃ = μb + κb² − b³ with cooperative repair (κ > 0), an unmaintained and a maintained state are both stable for −κ²/4 < μ < 0, so maintenance lost past the fold is not restored by returning the parameter, and recovery slows to zero as the fold nears'
version: 1
standing: fictional
kind: construction
tags:
- complex-systems
- individuation
date: '2026-10-18'
line: distributed-agency
illustrates:
- CLAIM-099
- CLAIM-025
summary: >-
  A7 §4 of the exchange of 2026-10-17, after the owner's "flesh this out
  further": a normal form for the activity b that maintains a boundary,
  in which repair processes reinforce one another. Its equilibria, the
  bistable range, the hysteresis loop and the slowing of recovery at the
  fold are derived and rechecked here. It shows a capacity to maintain,
  and not only a state, being lost and not coming back when conditions
  do, which is CLAIM-099's distinction in a model. A7's own caveat: "This
  is a proposed minimal model, not an empirical fit." THEORY-136 and
  THEORY-214 say why its early-warning consequence is weak evidence.
  Fictional by construction.
---

# CASE-tmpi1bt1: A fold in boundary maintenance: in ḃ = μb + κb² − b³ with cooperative repair (κ > 0), an unmaintained and a maintained state are both stable for −κ²/4 < μ < 0, so maintenance lost past the fold is not restored by returning the parameter, and recovery slows to zero as the fold nears

## The construction

A7 §4: "Suppose repair has a cooperative, self-amplifying component":

  ḃ = μb + κb² − b³ + d,  κ > 0,

where b ≥ 0 "measures boundary-maintenance activity, μ changes the linear
ability to sustain it, and κb² models positive feedback among repair
processes. The cubic term saturates growth." Take d = 0.

Write ḃ = f(b) = b·g(b) with g(b) = μ + κb − b².

- **Equilibria.** b = 0, and the roots of b² − κb − μ = 0,
  b± = (κ ± √(κ² + 4μ))/2, real when μ ≥ −κ²/4. They collide at
  μ_fold = −κ²/4.
- **Stability.** f′(0) = μ, so b = 0 is stable for μ < 0. At b±, g = 0, so
  f′(b±) = b±·g′(b±) = b±(κ − 2b±) = ∓ b±√(κ² + 4μ). The upper branch b₊
  is stable, the lower b₋ unstable.
- **Bistable range.** For −κ²/4 < μ < 0 both roots are positive (their
  sum is κ, their product −μ > 0). Then 0 and b₊ are both stable, and b₋
  is the threshold between them. For μ > 0, b₋ < 0 lies outside b ≥ 0,
  b = 0 is unstable, and b₊ is the only stable state. For μ < −κ²/4 only
  b = 0 remains.
- **Hysteresis.** Lower μ from the maintained state: b follows b₊ until μ
  passes −κ²/4, then collapses to 0. Raise μ back to any value in
  (−κ²/4, 0): b = 0 is still stable and b stays there. Maintenance returns
  only when μ passes 0, or when something outside the dynamics lifts b
  above b₋(μ) = (κ − √(κ² + 4μ))/2.
- **Slowing at the fold.** The recovery rate at b₊ is |f′(b₊)| =
  b₊√(κ² + 4μ), which goes to 0 as μ → −κ²/4.

A7's chart values for κ = 1 check: (b₊, b₋) = (0.724, 0.276) at μ = −0.2,
(0.816, 0.184) at μ = −0.15, and b₊ = 1.048 at μ = 0.05 and 1.171 at
μ = 0.2. The derivation was redone by hand and the values numerically
for this filing.

## What it can show

A7's four consequences, each now a property of the normal form:

- "**Boundary maintenance can have a threshold.** An organization may
  require a minimum existing stock of maintenance capacity to sustain
  itself." The stock is b₋.
- "**Recovery can depend on history.** Two systems with the same current
  external conditions may differ because one has retained sufficient
  repair organization and the other has lost it." In the bistable range,
  μ does not fix the state.
- "**Restoration can cost more than preservation.** Once the maintained
  state collapses, returning the external parameter to its previous value
  may not regenerate maintenance without an additional intervention." The
  additional intervention is μ past 0 or a lift above b₋.
- "**Critical slowing can warn of approaching failure.** Near the fold,
  local recovery rates approach zero, though noise, rate-dependent
  effects, and nonstationarity can make empirical early-warning signals
  unreliable."

And A7's use of it: "A will-organization can change what gets done without
changing the underlying capacity to govern. In a deeper transition, it can
lose or regain that capacity itself." That is CLAIM-099 (maintaining a
regime of action is not maintaining the capacity to govern) and CLAIM-025
(the two fail separately), with a mechanism for the loss of the second.

It is also the kind of model CLAIM-330 says it lacks: CLAIM-330 does not
say "That the bounded nonlinear system has two captured attractors, or how
far it hysteretically holds one." This case is a different variable, the
maintenance of a boundary, not the meaning–authority loop. It shows what a
nonlinear half would look like. It does not supply CLAIM-330's.

## What it cannot show

- **That any boundary obeys it.** A7: "This is a proposed minimal model,
  not an empirical fit." Nothing measures μ or κ.
- **That an abrupt collapse shows a fold.** THEORY-136: jumps also come
  from a stepwise driver or a simple threshold, and only hysteresis,
  initial-state dependence or a lasting shift after a temporary
  disturbance comes close to showing alternative stable states. A field
  test of this case is the hysteresis loop, not the collapse.
- **That slowing will warn.** On r/place, a boundary of attack and repair,
  THEORY-214 finds several distinct precursors rather than one generic
  warning signal, and many overthrows with no warning.
- **Who maintains b.** The equation does not say whether repair is the
  organization's own or supplied from outside. That is QUESTION-086's
  question, and A7 §1's caveat: "writing G and H into an equation does not
  establish self-maintenance."
