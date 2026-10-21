---
status: Active
title: 'In ḋ = (α − κ)d − βd³, with d the difference between two parties'' shares of authority, α their self-reinforcement and κ a constraint that bears on both alike, the equal allocation is the only equilibrium and is stable for κ > α, and for κ < α it is unstable and the unequal allocations ±√((α − κ)/β) are stable: a constraint that favours neither party can, by weakening, destabilize the equal allocation and make persistent unequal allocations stable, of any size near the threshold (|d*| → 0 as κ → α), without determining which party gains the larger share, and in this model restoring κ > α restores the equal allocation'
version: 3
history:
- version: 2
  date: '2026-10-21'
  note: >-
    From the reading of Arthur's 1983 working paper on 2026-10-21
    (THEORY-tmpxzls4): a second store of advantage beside authority over
    the rule, in a different model. The claim is unchanged.
- version: 3
  date: '2026-10-21'
  note: >-
    Title narrowed at the owner's review of 2026-10-21: "dominate" said more
    than the model gives. Near the bifurcation the stable asymmetry
    ±√((α − κ)/β) is arbitrarily small, so shares of 50.5% and 49.5% are a
    symmetry-broken state. The result is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the stability analysis: a choice of α, κ ≥ 0 and β > 0 for
  which the equilibria of ḋ = (α − κ)d − βd³ or the signs of f′ at them
  differ from those stated, or a trajectory of the model that does not go
  to the stated stable equilibrium. Its bearing on any actual rule is not
  part of the claim, so evidence about a rule cannot defeat it.
tags:
- complex-systems
- self-governance
- society-and-governance
date: '2026-10-21'
line:
- distributed-agency
- formal-apparatus
grounds:
- CASE-112
complements:
- CLAIM-330
summary: >-
  A19 of the exchange of 2026-10-20, on the owner's U19: does the account
  "capture 'deregulation' as a disguised effort to induce organizational
  symmetry breaking?" A19's model is a supercritical pitchfork, [CASE-112](../cases.d/CASE-112.md)'s
  normal form with no tilt and μ = α − κ. The stability analysis is
  checked here, algebraically and numerically. A19: "A policy can be
  neutral with respect to the identities of participants while being
  non-neutral with respect to the kinds of power distributions its
  dynamics produce." The claim is about the model. It says nothing about
  any reform, or about anyone's intent, and it does not show that a tipped
  allocation outlasts the constraint's return: in this model it does not.
---
<!-- inactive-ok-file: CLAIM-277 CLAIM-297 THEORY-470 CLAIM-tmpyxupb — Proposed; the entrenchment claims and the reading named for the mechanisms this claim leaves out, nothing here rests on them -->

# CLAIM-tmpptl3y: In ḋ = (α − κ)d − βd³, with d the difference between two parties' shares of authority, α their self-reinforcement and κ a constraint that bears on both alike, the equal allocation is the only equilibrium and is stable for κ > α, and for κ < α it is unstable and the unequal allocations ±√((α − κ)/β) are stable: a constraint that favours neither party can, by weakening, destabilize the equal allocation and make persistent unequal allocations stable, of any size near the threshold (|d*| → 0 as κ → α), without determining which party gains the larger share, and in this model restoring κ > α restores the equal allocation

## The claim

The owner, at U19 of the exchange of 2026-10-20: "does this account also
capture "deregulation" as a disguised effort to induce organizaitonal
symmetry breaking?" A19 §1 took two parties with shares of practical
authority w₁ + w₂ = 1 and d = w₁ − w₂, and wrote

  ḋ = (α − κ)d − βd³,  β > 0,

with "α represents endogenous positive feedback: existing authority makes
it easier to acquire more authority", "κ represents the stabilizing effect
of an institutional constraint" and β limiting the amplification. "The
equation is symmetric under exchange of the two participants: d ↦ −d.
Neither participant is formally favored."

Write μ = α − κ and f(d) = μd − βd³, so f′(d) = μ − 3βd².

- **κ > α (μ < 0).** μ − βd² < 0 for every d, so d = 0 is the only
  equilibrium, and f′(0) = μ < 0: it is stable, and globally attracting.
- **κ < α (μ > 0).** The equilibria are d = 0 and d = ±√(μ/β).
  f′(0) = μ > 0, so the equal allocation is unstable, and
  f′(±√(μ/β)) = μ − 3μ = −2μ < 0, so both unequal allocations are stable.
  Every start other than d = 0 goes to the one whose sign it has.
- **Restoring the constraint.** Raising κ back above α returns the first
  case. The equal allocation is again the only equilibrium, and any tipped
  state decays to it. The bifurcation is supercritical, so in κ there is no
  hysteresis.

So the rule is identity-neutral, since f is odd, and still not neutral as
to the allocation it stabilizes. Weakening it past κ = α decides that one
party will hold more authority without deciding which. A19: "A rule need
not explicitly favor a participant to stabilize or destabilize the
symmetry among participants", and "The rules of motion remain symmetric.
**The realized organization does not.**"

## The check

- **Algebra, by sampling.** 20,000 draws of α, κ ∈ [0, 2] and
  β ∈ [0.05, 3]. The real roots of f and the sign of f′ at each were
  computed and compared with the three cases above: no mismatch, and
  f′ = −2μ at both outer roots to rounding.
- **Trajectories.** RK4, step 0.01, to t = 200, with α = β = 1. At κ = 1.5,
  starts at ±10⁻⁶ and ±0.3 all went to 0. At κ = 0.5 they went to
  ±0.707107 = ±√0.5, with the sign of the start. A state tipped at κ = 0.5
  and then run at κ = 1.5 went back to 0 (|d| < 10⁻⁴³).
- **With a tilt.** [CASE-112](../cases.d/CASE-112.md)'s form, ẇ = μw − w³ + h, with h = 0.02 and a
  start against the tilt at w = −0.7. Sweeping μ through 0.5, 0.25, 0.1,
  −0.5, 0.1, 0.25 and 0.5 gave w = −0.686, −0.454, then +0.389 (at
  μ = 0.1 the tilt exceeds h_c = 2μ^{3/2}/(3√3) ≈ 0.012, so the lower
  branch is gone), +0.040, +0.389, +0.536, +0.726. Restoring the
  constraint brought w near zero. Weakening it again selected the side the
  tilt favours, not the side the state had held before.
- **The domain.** d is a difference of shares only while |d| ≤ 1, that is
  while α − κ ≤ β, as A19's caption says ("Valid as an authority-share
  model where the equilibria remain within d ∈ [−1, 1]"). At α = 1, κ = 0,
  β = 0.5 the stable states are ±1.414, outside it.

## Where it sits in the record

[CASE-112](../cases.d/CASE-112.md) is the same normal form, ẇ = μw − w³ + h, for the balance of
authority between two regimes within an agent. A19's equation is that case
at h = 0, with μ read as the strength of a rule. [CASE-112](../cases.d/CASE-112.md)'s tilt h is what
A19's table calls "**Explicit symmetry breaking**", "A rule change favors
identifiable actors or classes differently". [CLAIM-330](CLAIM-330.md) is the record's
other result about an unstable symmetric state, for a different model: a
loop between interpretation and authority destabilizes symmetry when
βγ > (1 − α)(1 − δ). Here a single self-reinforcing variable does so once
its damping falls.

A19 §3 separated four mechanisms, and "Actual reforms can combine these
mechanisms":

| Mechanism | A19's "What changes?" | In the record |
|---|---|---|
| Spontaneous symmetry breaking | "A symmetric arrangement becomes unstable; small differences select asymmetric outcomes" | this claim |
| Explicit symmetry breaking | "A rule change favors identifiable actors or classes differently" | [CASE-112](../cases.d/CASE-112.md)'s h |
| Release of existing asymmetry | "A constraint previously limited the effects of unequal resources or positions" | [THEORY-470](../theory.d/THEORY-470.md)'s reading, Proposed |
| Reorganization of governance | "The authority to make and revise rules changes hands" | [CLAIM-tmpyxupb](CLAIM-tmpyxupb.md) |

Only the first is demonstrated here.

## What it does not say

- **Nothing about intent.** A19 §4: "To establish *disguise*, rather than
  merely an asymmetric consequence, we'd need evidence about the
  proponents' actual aims", and "We should not infer deception simply
  because asymmetry subsequently appears." The same dynamics "could be
  favored by someone who welcomes open-ended competition and by someone
  who expects an established organization to benefit." The record holds no
  episode that would bear on the intent behind any reform, and this claim
  is not evidence about one.
- **Nothing about any actual rule.** A19's caption: "This is a constructed
  bifurcation model, not an empirical finding about deregulation
  generally." Whether a given rule enters any real dynamics as a symmetric
  damping term is an empirical question the claim does not touch.
- **Not that a tipped allocation outlasts the constraint.** In this model
  it does not: restoring κ > α restores d = 0. [CASE-112](../cases.d/CASE-112.md)'s hysteresis is in
  the tilt h at fixed μ > 0, not in μ. Persistence after a rule is restored
  would need another mechanism, such as the advantaged party acquiring
  authority over the rule itself, the last stage of A19 §6's sequence
  ("Durable authority asymmetry → Changed capacity to revise rules"). That
  is the entrenchment of [CLAIM-277](CLAIM-277.md) and [CLAIM-297](CLAIM-297.md) and the governance profile
  of [CLAIM-tmpyxupb](CLAIM-tmpyxupb.md), none of it demonstrated here. Arthur's model, read on
  2026-10-21 through its 1983 working paper ([THEORY-tmpxzls4](../theory.d/THEORY-tmpxzls4.md)), has another
  such mechanism: lock-in is absorption in accumulated adoptions, a state a
  reversal of returns does not touch. "Small subsidies to the excluded
  choice will not re-establish it; large subsidies, on the other hand,
  will swing the market and drive the dominant choice out." Accumulated
  adoptions are a second store of advantage beside authority over the
  rule; the model is a different one, and nothing of it carries over to
  this equation. A19's citation of Arthur is accurate to that paper.
- **Not that symmetry breaking is a failure.** A19 §5: "differentiation can
  be constitutive of an organization", and "We can distinguish desirable
  specialization from problematic entrenchment only after specifying
  criteria beyond the symmetry-breaking dynamics themselves." When it is
  complementary specialization and when entrenchment is [QUESTION-132](../questions.d/QUESTION-132.md)'s
  question, and whether undifferentiated processes come to hold
  differentiated authority at all is [QUESTION-083](../questions.d/QUESTION-083.md)'s. This claim shows only
  that a symmetric rule can make an unequal allocation the stable one.
