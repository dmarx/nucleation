---
status: Proposed
title: 'Capacity resources capture with no return channel'
statement: >-
  In the two-institution meaning–influence model with the party's resources
  read as capacity, scaling the evaluator's conferral gain to
  g_E(1 + ω m_P), cutting the return channel does not prevent capture when
  the party's own reading is off symmetry: with the evaluator's evidence
  independent of the party, the evaluator is captured exactly when
  (1 + ω m_P*) g_E σ_E² > 2(1 − φ′_E), m_P* being the party's own fixed
  point, and it is then captured to either side, as its own start
  decides, not toward the party's
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below; or a rerun of its check (LEAD-015's
  model, χ = ψ = 0, θ = 0, resources as capacity, each institution stable
  alone) in which the evaluator's having two stable readings disagrees
  with the condition, or in which the two readings are not symmetric about
  zero. Not defeated by runs with θ > 0, where the claim says the condition
  is not exact, or by the directional reading of resources, which it is
  not about.
tags:
- complex-systems
- society-and-governance
- self-governance
date: '2026-11-26'
line:
- distributed-agency
rests_on:
- CLAIM-947
- CLAIM-1021
grounds:
- CASE-401
bears_on:
- QUESTION-100
complements:
- CLAIM-1202
summary: >-
  Found at the synthesis review of 2026-11-26 (Arm B3), joining CLAIM-947's
  condition for one institution to CLAIM-1021's capacity reading of
  CLAIM-404's "resources". CLAIM-1202 says that in CASE-401's model what
  prevents capture is a return channel too weak to close the loop, and
  CASE-401 cut the return channel with the party's corpus balanced, so
  that its reading sat at zero. If the party leans (its own evidence
  unbalanced) and its resources raise the evaluator's conferral gain, a
  cut return channel still leaves the evaluator's own loop pushed past its
  threshold: 395 of 395 random parameter sets agree with the condition, and
  every capture is a symmetric pair of readings. So under the capacity
  reading the remedy CLAIM-1202 names holds only for a party at symmetry,
  and the capture it leaves is the evaluator's own lock-in, not a tilt to
  the party. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-1021 CLAIM-1202 CLAIM-947 CASE-401 — Active; premises, ground and the claim this bounds -->

# CODE: Capacity resources capture with no return channel

## The claim

CASE-401 couples two of CASE-363's reduced institutions, an evaluator E and
a party P, by four nonnegative channels: θ and ω carry P's meaning into E's
evidence and conferral, χ and ψ carry E's meaning into P's. CLAIM-1021 reads
the party's resources as capacity, so that E's conferral is
a′_E = δ_E a_E + (1 − δ_E) tanh((1 + ω m_P) g_E σ_E m_E / 2). This claim
takes the return channel cut, χ = ψ = 0, and E's evidence independent of
the party, θ = 0.

## Derivation

1. With χ = ψ = 0, P's update does not involve E. P is a single
   institution on its own evidence b_P; stable alone (Δ_P > 0) it settles at
   its fixed point m_P*, which is zero only when b_P = 0.
2. Once m_P = m_P*, E's map is CASE-363's institution with its gain g_E
   replaced by g_E(1 + ω m_P*), since θ = 0 leaves its evidence at its own
   b_E = 0.
3. By CLAIM-947, that institution's symmetric state is unstable exactly
   when (1 + ω m_P*) g_E σ_E² > 2(1 − φ′_E), and its fixed points solve the
   Curie–Weiss equation a = tanh(Ja) with
   J = (1 + ω m_P*) g_E σ_E² / (2(1 − φ′_E)). With no field the nonzero
   solutions are a pair ±a, so E's captured reading is on whichever side
   its start lies, not the side of P's lean.
4. Where ω m_P* < 0 the gain is lowered and E is further from its
   threshold.

The step from 2 to 3 assumes P has settled; a transient of P on the way to
m_P* cannot strand E captured below the condition, since below it E's only
fixed point is symmetric.

## Check

With LEAD-015's `model.py` unchanged, `check_capacity_return_cut.py`
(kept by the review; to be stored beside the study) draws 400 parameter
sets with g_E, g_P in [1, 6], b_P in [−0.3, 0.3] and ω in [0, 10], keeps
those with each institution stable alone and the condition at least 2 %
from equality, and calls E captured when starts at +0.9 and −0.9 settle on
different readings. With θ = 0, 395 of 395 agree with the condition, and
every captured pair is symmetric (for example ω = 5.9, m_P* = 0.537:
E settles at ±0.513). With θ drawn from [0, 1], only 330 of 399 agree,
because P's lean then tilts E's evidence and the pitchfork is no longer
symmetric; captured readings were still found on both sides (ω = 6.6,
m_P* = 0.40: +0.568 and −0.360).

## How it stands to the record

- **CLAIM-1202.** "What does [prevent capture] is a return channel too
  weak to close the loop, the evaluator's reading not moving the party's
  standing or evidence." That holds in its directional model, and with the
  return channel cut it holds under the capacity reading too while the
  party sits at symmetry, which is CASE-401's case (θ = ω = 3, spectral
  radius 0.958). It fails under the capacity reading when the party leans.
  The directional reading with a cut return channel and a leaning party
  gives one fixed point tilted toward the party, not two.
- **CLAIM-1021.** Its one-sided captures below threshold need a push and
  a running return channel; this capture needs neither and has no side.
- **CLAIM-404.** Its first two routes govern an organization through its
  evidence or its criteria. Read as capacity, resources act on a third
  thing, the gain of the evaluator's own interpretation–authority loop.

## Admission

By ADR-075's second route, a derivation. The claim follows from CLAIM-947's
condition and CLAIM-1021's model by the steps above, and no claim holds it:
CASE-401 cut the return channel only with a balanced party, and CLAIM-1202
states its remedy without the reading of resources it depends on. It is not
trivial in what it changes, the side of the capture and the scope of a
named remedy.

## What it does not say

- That resources work as capacity in any institution, which CLAIM-1021
  also leaves open.
- Anything exact for θ > 0.
- That a party's own reading is commonly off symmetry, or by how much.
