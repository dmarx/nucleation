---
number: 364
status: Proposed
formerly:
- CASE-tmprcg71
title: 'A numpy model of the competence-restriction loop: capacity dynamics where competence is learned by doing and decays with disuse, with reinstatement made a threshold on capacity, in which a restriction justified by a lack of competence causes the very decay that withholds reinstatement, so that with no route to practice or training the bar never lifts; the trap has a recoverability deadline past which even release no longer restores capacity; and it is escaped only by a route strong enough to restore practice or by training that adds capacity directly and so ignites from zero'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant carrying out LEAD-104. The model was
    written, run and tested in this session; scripts and small results are
    committed under scratch/studies/lead-104/, with a README that reruns
    them. No external data: the parameters are invented to show a
    mechanism.
standing: documented
kind: executed-study
tags:
- society-and-governance
- learning-and-conditioning
- agency
- mathematics
date: '2026-11-22'
line:
- dependence-and-domination
- transient-support
- rightful-power
bears_on:
- QUESTION-478
illustrates:
- CLAIM-721
- CLAIM-605
summary: >-
  [LEAD-104](../leads.d/LEAD-104.md) asked for the model [CLAIM-721](../claims.d/CLAIM-721.md) names: [CLAIM-605](../claims.d/CLAIM-605.md)'s
  capacity dynamics with reinstatement made a threshold on capacity, to
  make the restriction-induced capability trap demonstrable. Instead of
  outside support doing the work, a restriction removes the doing, and the
  restriction lifts when capacity reaches a reinstatement threshold C_r.
  With [CLAIM-605](../claims.d/CLAIM-605.md)'s parameters (λ = 1, μ = 0.3, τ = 1.5), C_r = 0.6 and a
  party restricted at C = 0.5: with no route the capacity decays as
  e^(−μt), so it never reaches C_r and the restriction never lifts, the
  decay being the evidence that extends it; a recoverability deadline of
  1.98 time units, past which even releasing the party by hand no longer
  restores capacity; a practice route must restore exercise above a
  critical fraction (ρ ≥ 0.8) and even then cannot ignite a party below
  threshold, whereas a training route that adds capacity directly ignites
  from C = 0 once its rate reaches μ·C_r = 0.18. Each of [CLAIM-721](../claims.d/CLAIM-721.md)'s three
  conditions is shown necessary. The modelling choices and the finding are
  in [CLAIM-950](../claims.d/CLAIM-950.md). The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-721 CLAIM-950 — Proposed or new; the claim this study makes demonstrable and the finding it grounds -->

# CASE-364: A numpy model of the competence-restriction loop: capacity dynamics where competence is learned by doing and decays with disuse, with reinstatement made a threshold on capacity, in which a restriction justified by a lack of competence causes the very decay that withholds reinstatement, so that with no route to practice or training the bar never lifts; the trap has a recoverability deadline past which even release no longer restores capacity; and it is escaped only by a route strong enough to restore practice or by training that adds capacity directly and so ignites from zero

## The model

The study builds the model [CLAIM-721](../claims.d/CLAIM-721.md) names in prose and says "no one has
written": [CLAIM-605](../claims.d/CLAIM-605.md)'s model "with reinstatement made a threshold on
capacity". [CLAIM-605](../claims.d/CLAIM-605.md)'s capacity dynamics are kept unchanged,

  dC/dt = λ·P·C·(1 − C) − μ·C,

capacity C ∈ [0, 1] learned by doing (the factor C), decaying with disuse
(−μC). The modification is in what sets P and in how the restriction ends.

- A **restriction** removes the doing: while restricted the party may
  exercise only at a fraction ρ ∈ [0, 1] of what it could, and the
  restricting party may run a training program adding capacity directly at
  rate g ≥ 0:
  P = ρ·min(τC, 1), dC/dt = λ·P·C·(1 − C) − μC + g.
  ρ = 0, g = 0 is the bare restriction: no route to practice or training.
- **Reinstatement is a threshold on capacity**: the restriction lifts
  (one-way) the instant C ≥ C_r. Once free, P = min(τC, 1) and g = 0 —
  [CLAIM-605](../claims.d/CLAIM-605.md)'s free party, whose steady states are C = 0 (stable),
  C_LOW = 0.276 (unstable) and C_HIGH = 0.7 (stable).

[CLAIM-721](../claims.d/CLAIM-721.md)'s three conditions become model switches: competence decays
with disuse (μ > 0); lifting depends on competence shown (the gate on
C_r); and the restricting party supplies no route (ρ = 0, g = 0).

## What was run

`scratch/studies/lead-104/restriction_trap.py` integrates the model
(forward Euler, dt = 10⁻³) and asserts every number; the parameters are
[CLAIM-605](../claims.d/CLAIM-605.md)'s (λ = 1, μ = 0.3, τ = 1.5), with C_r = 0.6 and a party
restricted at C = 0.5 < C_r ("for lack of competence"). An independent
pytest, `test_restriction_trap.py`, re-derives the facts (8 cases, all
pass). Run with `python3 -I` and one BLAS thread. No data is downloaded.

1. **The bare restriction is a self-perpetuating trap.** With no route,
   while restricted dC/dt = −μC, so C(t) = C₀e^(−μt) falls monotonically
   and never reaches C_r: the gate never opens. The restriction causes the
   very decay that withholds reinstatement. Competence reviews at a fixed
   interval read 0.50, 0.274, 0.151, 0.083 — each lower than the last and
   each below C_r — so every review extends the restriction. The decay is
   the evidence for its own continuation.
2. **A recoverability deadline.** A party restricted at C_LOW < C₀ < C_r is
   not reinstated (C below C_r and falling) yet would recover if someone
   freed it — but only until C decays past C_LOW. That window closes at
   t_dead = ln(C₀/C_LOW)/μ = 1.98. Freed at t = 1.0 or 1.5 the party
   recovers to 0.7; freed at 2.5 or 4.0 it decays to 0 even once free. This
   is the restriction twin of [CLAIM-605](../claims.d/CLAIM-605.md)'s substitution deadline.
3. **The route decides, and practice cannot ignite while training can.** A
   practice route (restoring exercise at fraction ρ, g = 0) has a positive
   restricted steady state only if ρ ≥ ρ_crit = 4μ/(λτ) = 0.8; below it
   every restricted party decays to 0, and even a sufficient route cannot
   lift a party below its shifted threshold. A training route (adding
   capacity directly at rate g, with ρ = 0, so no exercise at all) drives
   C → g/μ and reinstates once g ≥ g_crit = μ·C_r = 0.18, from any start,
   C₀ = 0 included. This is [CLAIM-605](../claims.d/CLAIM-605.md)'s result 3 — capacity-first support
   cannot ignite, a direct capacity transfer can — reached through
   restriction rather than substitution.
4. **Each condition is necessary.** Drop decay (μ = 0): C stays at C₀, a
   standing bar that makes no new evidence, not the worsening loop. Drop
   the competence gate (a fixed release date): the party is freed
   regardless and, if still above C_LOW, recovers — the loop cannot form.
   Drop no-route: result 3.

## What it can show

It makes [CLAIM-721](../claims.d/CLAIM-721.md)'s restriction-induced capability trap demonstrable in a
model, as the lead asked. The loop it describes in prose — restriction →
disuse → decay → the decay read as the reason to extend → restriction — is
the model's generic behaviour under its three conditions, not a tuned
special case. It also locates [CLAIM-721](../claims.d/CLAIM-721.md)'s "route to practice or training"
precisely: a practice route works only above a threshold and cannot
ignite, a training route that adds capacity directly can, which is exactly
[CLAIM-605](../claims.d/CLAIM-605.md)'s distinction.

## What it cannot show

It is a toy. The threshold C_r, the deadline, ρ_crit and g_crit all depend
on invented parameters; the model shows directions and the structure of
the loop, not magnitudes for any institution. It does not show that any
real restriction is of this kind — that competence here decays with
disuse, that lifting in fact waits on competence shown, and that no route
is supplied — which is [CLAIM-721](../claims.d/CLAIM-721.md)'s own `defeated_if`. And it says nothing
about whether a restriction is justified, which [CLAIM-721](../claims.d/CLAIM-721.md) sets aside.
