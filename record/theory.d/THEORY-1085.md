---
number: 1085
status: Active
formerly:
- THEORY-tmprfjii
title: 'In Toner and Tu''s hydrodynamic theory, a flock''s ordered state is a broken continuous symmetry of a coarse-grained velocity field: speed fluctuations relax in a finite time of order 1/α and are dropped, leaving as slow degrees of freedom the transverse velocity and the conserved density, which propagate as sound at ω = ±cq⊥; no individual member appears in the description, which is offered for a universality class of microscopic rules'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11 (by topic, second run, part P), under
    ADR-091 and ADR-093. corroborates CLAIM-478 and bears_on
    QUESTION-281 added. CLAIM-478's note: "Toner and Tu 1995 (NOTE-1228;
    THEORY-1085) give a flock's case" of its first half. QUESTION-281's
    note: "Toner and Tu 1995 is a worked case of creation and
    stabilization coming apart (NOTE-1228)". No other change.
tags:
- complex-systems
- natural-sciences
date: '2026-10-27'
source:
- LIT-1670
summary: >-
  Toner and Tu (1995), [LIT-1670](../literature.d/LIT-1670.md), read in [NOTE-1228](../notes.d/NOTE-1228.md) from the arXiv
  preprint. Active as a statement of what the theory is: its variables, the
  degree of freedom it eliminates and why, and the modes that remain, all
  in the text (pp. 3–8). It does not say that the theory's exponents are
  right ([THEORY-1095](THEORY-1095.md)), that the universality claim holds, or that the
  order so described is an agent or an individual.
corroborates:
- CLAIM-478
bears_on:
- QUESTION-281
---
<!-- inactive-ok-file: THEORY-tmpdfeto NOTE-tmpcjw5n ARG-tmpdc2qe — Proposed, Skimmed or new; the reading of the long paper and its argument, 2026-11-22 -->
<!-- inactive-ok-file: THEORY-1095 CLAIM-478 CLAIM-157 — Proposed or Open; neighbours cited as open -->
<!-- inactive-ok-file: CLAIM-841 — filed 2026-11-21 from the exchange "Rich Get Richer Power Laws"; Deferred and Proposed -->

# THEORY-1085: In Toner and Tu's hydrodynamic theory, a flock's ordered state is a broken continuous symmetry of a coarse-grained velocity field: speed fluctuations relax in a finite time of order 1/α and are dropped, leaving as slow degrees of freedom the transverse velocity and the conserved density, which propagate as sound at ω = ±cq⊥; no individual member appears in the description, which is offered for a universality class of microscopic rules

## Source

Toner and Tu (1995), [LIT-1670](../literature.d/LIT-1670.md), pp. 1–8 of the arXiv preprint
adap-org/9506001; read in [NOTE-1228](../notes.d/NOTE-1228.md).

## What was actually shown

**The variables.** A coarse-grained velocity field v(r, t) obeying eq. (1)
and a number density ρ obeying ∂ρ/∂t + ∇ · (vρ) = 0, which "reflects
conservation of birds" (eq. 2, p. 3). The abstract offers it for "a large
universality class of microscopic rules, including those recently simulated
by Viscek et. al." (p. 1).

**The broken symmetry.** For α > 0 the α and β terms "simply make the local
v have a non-zero magnitude (= √(α/β)) in the ordered phase", and
v = v₀x̂∥ + δv with v₀x̂∥ = ⟨v⟩ "the spontaneous average value of v"
(p. 3). The direction is arbitrary: "the direction in which we choose to
break the symmetry of v was arbitrary" (p. 9).

**The eliminated degree of freedom.** "We will ignore fluctuations in the
magnitude |v| from its optimal value of √(α/β) since they decay in a finite
time (of order 1/α)" (pp. 3–4). The speed is thereafter fixed:
v = (v⊥, √(1 − |v⊥|²)).

**The modes that remain.** The theory is then in v⊥ and δρ (eqs. 3, 4).
"All of the correlation and response functions for this problem" have "two
sharp peaks at ω = ±cq⊥", with c = √(σ₁ρ₀) "the speed of sound" (p. 8),
and their widths D⊥ᴿq⊥² + D∥q∥² vanish as q → 0. So the long-wavelength
dynamics are propagating and slowly damped, and in d = 2 they scale
hyperdiffusively, with z = 6/5 (pp. 7, 9).

This could have been otherwise as a description: a flock could have been
modelled with individual trajectories, or with the speed as a dynamical
variable at long wavelengths. The theory does neither.

## What this does not say

- **That the exponents are right.** That is [THEORY-1095](THEORY-1095.md)'s question.
- **That the universality claim holds.** No microscopic rule is
  coarse-grained into eqs. (1, 2) in the paper.
- **That the ordered state is an agent, an individual, or one system in the
  record's sense.** The paper's order is a phase of a field; it has no
  account of agency, and its "birds" are in scare quotes throughout. Whether
  a broken-symmetry mode is a unit is for [CLAIM-157](../claims.d/CLAIM-157.md) and
  [QUESTION-281](../questions.d/QUESTION-281.md), not this paper.
- **"Goldstone mode".** The paper does not use the term. That the transverse
  velocity is slow because the symmetry is broken is the standard reading
  of a theory of this form, and is how [CLAIM-478](../claims.d/CLAIM-478.md) would use it; the
  paper states only the modes and their dispersion.

## Note of 2026-11-21: the exchange "Rich Get Richer Power Laws"

The exchange uses this theory as a route to scale-free behaviour in an
ordered phase rather than at a transition (A26 §4, A27 §7), filed as one
of the routes of [CLAIM-841](../claims.d/CLAIM-841.md). It adds two things this reading does not
hold, both unread here:

- **Giant number fluctuations.** In ordered active matter the count in a
  region fluctuates as ΔN ∝ ⟨N⟩^φ with φ > ½, against ½ for independent
  particles, a prediction A attributes to the Toner–Tu theory; A adds that
  "some initially predicted exponents differ from those obtained in
  large-scale simulations". The long 1998 paper is registered as
  [LIT-2970](../literature.d/LIT-2970.md), unread; the simulation study is unnamed.
- **A universality class for the ordered phase.** A27 §7 cites a 2024
  Physical Review Letters paper using the functional renormalization
  group to propose one, "with scaling exponents consistent with numerical
  simulations". The paper is not named and is not registered.

A's framing, "In certain active systems, scaling is a property of the
phase itself" (A26 §4), agrees with this reading's broken-symmetry slow
modes and goes beyond it only in calling the result scale-free; the
exponents remain [THEORY-1095](THEORY-1095.md)'s question.

## Note of 2026-11-22: Toner and Tu (1998), read

The long paper (LIT-2970, read in NOTE-tmpcjw5n; the reading is
THEORY-tmpdfeto) **supports this reading and extends it.** The slaving of
the speed fluctuation is derived there in full: δv∥ = −Dρ∂∥δρ, by
neglecting ∂tδv∥ "relative to αδv∥" (eqs. 3.1–3.2, p. 19), the eliminated
degree of freedom this entry names. The universality claim is still
posited: "This approach allows us to bury our ignorance in a few
phenomenological parameters" (p. 18), as this entry says of 1995.

**A correction to "What this does not say".** Its bullet "Goldstone
mode" holds that the paper does not use the term; that is true of the
1995 letter, but the 1998 paper does: "The "Goldstone modes" associated
with this "spontaneously broken rotational symmetry" are fluctuations in
the direction of motion", and they "mix with modes associated with
conservation of bird number to produce propagating sound modes"
(abstract). So the broken-symmetry reading of the slow transverse
velocity is the authors' own by 1998.

**On the exchange's note of 2026-11-21.** The two things A added are now
checked against the long paper. Its "giant number fluctuations" are in
it as a density structure factor diverging as q → 0, "infinitely bigger
than those in a fluid or an ideal gas" (pp. 7–8), not as ΔN ∝ ⟨N⟩^φ,
which it never writes; and "some initially predicted exponents differ
from those obtained in large-scale simulations" is not in it: it reports
"good agreement" (p. 70). LIT-2970 is no longer unread; the formula and
the disagreement A reported are later work the record has not read
(ARG-tmpdc2qe). No status change.
