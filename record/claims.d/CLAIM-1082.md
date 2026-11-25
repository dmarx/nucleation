---
number: 1082
status: Proposed
formerly:
- CLAIM-tmpdrkvl
title: "Where an organization's operation relaxes at rate γ toward a governed configuration h(θ) and can also be pushed directly, ẋ = −γ(x − h(θ)) + bu, a smaller γ makes a direct push cheaper and a change of the configuration slower: the least effort to push x by Δ within H, 2γΔ²/(b²(1 − e^{−2γH})), rises with γ, while moving the configuration by D with operation kept within ε of it throughout needs H ≥ (D/ε − 2)/γ, so an organization whose operation has slowed is easier to redirect by intervention and slower to govern by changing its rules"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation or the check; or, in the model, a schedule
  that moves the configuration by D within H with |x − h(θ)| ≤ ε
  throughout and D > ε(γH + 2). As a reading of organizations: organizations
  whose operation slows, with the input channel b fixed, and whose
  tolerance-keeping rule changes then become faster, or whose direct
  interventions through that channel become costlier.
tags:
- control-theory
- mathematics
- society-and-governance
date: '2026-11-23'
line:
- realizability
- will-organization
rests_on:
- CLAIM-1192
- CLAIM-1051
summary: >-
  The manuscript governance-of-possibility's join JB10 (§7.3), filed at the
  owner's ruling of 2026-11-23 that joins a manuscript makes and no entry
  maps are filed rather than thrown away. It puts [CLAIM-1192](CLAIM-1192.md)'s push and
  [CLAIM-1051](CLAIM-1051.md)'s retuning in one system and adds the necessary half of
  the retuning bound, which [CLAIM-1051](CLAIM-1051.md) says it lacks. Checked with
  python3 -I. Integrated by the account [SYNTHESIS-123](../syntheses.d/SYNTHESIS-123.md). The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

<!-- inactive-ok-file: SYNTHESIS-123 — Proposed; the account filed with this claim -->

# CLAIM-1082: Where an organization's operation relaxes at rate γ toward a governed configuration h(θ) and can also be pushed directly, ẋ = −γ(x − h(θ)) + bu, a smaller γ makes a direct push cheaper and a change of the configuration slower: the least effort to push x by Δ within H, 2γΔ²/(b²(1 − e^{−2γH})), rises with γ, while moving the configuration by D with operation kept within ε of it throughout needs H ≥ (D/ε − 2)/γ, so an organization whose operation has slowed is easier to redirect by intervention and slower to govern by changing its rules

## The derivation

One system: ẋ = −γ(x − h(θ)) + bu, with h Lipschitz with constant L. It
is [CLAIM-1051](CLAIM-1051.md)'s model with a direct input added. With θ fixed and
a = x − h(θ), it is [CLAIM-1192](CLAIM-1192.md)'s ȧ = −γa + bu.

1. **Pushing.** Hold θ fixed. The least ∫u² that moves x by Δ within H is
   2γΔ²/(b²(1 − e^{−2γH})), strictly increasing in γ, with limit Δ²/(b²H)
   as γ → 0 ([CLAIM-1192](CLAIM-1192.md)).
2. **Retuning, a necessary bound.** Set u = 0 and e = x − h(θ). Then
   ẋ = −γe, so x(H) − x(0) = −γ∫₀ᴴ e dt. The configuration moves by
   D = h(θ(H)) − h(θ(0)) = [x(H) − e(H)] − [x(0) − e(0)]
   = −γ∫₀ᴴ e dt − e(H) + e(0). If |e| ≤ ε throughout, |D| ≤ ε(γH + 2),
   so H ≥ (|D|/ε − 2)/γ. The bound is tight. Start with e(0) = +ε, step h
   up by 2ε, then raise it at rate γε, which holds e at −ε.
3. **Retuning, the sufficient bound.** A change Δθ at a constant rate keeps
   |e| ≤ ε if LΔθ/(γH) ≤ ε, that is, if H ≥ LΔθ/(γε) ([CLAIM-1051](CLAIM-1051.md)).

So the least time for a change of the configuration that keeps operation
within tolerance lies between (D/ε − 2)/γ and LΔθ/(γε), where D = LΔθ
for linear h. Both bounds scale as 1/γ. Lowering γ makes the push of step
1 cheaper and the retuning of steps 2 and 3 slower, at once.

## The check

With python3 -I:

- A quadrature of the Gramian matches the closed form at γ = 0.1, 1 and 5
  (1.10333, 2.31304 and 10.00045, with b = Δ = H = 1). The effort is
  strictly increasing on a grid of 500 values of γ. The minimum-energy
  input, simulated in the system at γ = 0.5 and H = 2, reaches
  x(H) = 1.0000 at an effort of 1.1565, equal to the closed form.
- 3,000 random piecewise-constant schedules of h that kept |e| ≤ ε moved
  the configuration by at most 0.9175 of ε(γH + 2). The extremal schedule
  of step 2 reaches the bound exactly at three settings, with max |e| = ε.
- With L = Δθ = 1 and ε = 0.1, the least tolerance-keeping retuning time
  lies in [80, 100] at γ = 0.1, in [16, 20] at γ = 0.5 and in [4, 5] at
  γ = 2. The least effort to push by 1 within H = 1 is 1.103, 1.582 and
  4.075 at the same γ.

## Admission ([ADR-075](../decisions.d/ADR-075.md), step 5)

**Route: a derivation, with a discriminating prediction.**

- **The derivation.** No claim holds step 2. [CLAIM-1051](CLAIM-1051.md) gives a
  sufficient condition and calls it "sufficient, not necessary". From it
  alone, a small γ only fails to guarantee a fast retuning; it does not
  rule one out. Step 2 makes slow retuning a consequence of slow
  operation, and puts it in the same system as [CLAIM-1192](CLAIM-1192.md)'s push.
  The record holds each half in its own model. No entry says that one
  parameter moves them in opposite directions.
- **The discriminating prediction.** Where operation slows (γ falls) and
  the input channel b stays fixed, direct interventions through that
  channel get cheaper, and changes of the governing configuration that keep
  operation within tolerance take longer, in proportion to 1/γ. Neither
  component predicts the pair. A case where both get harder, or both
  easier, with b fixed, defeats the reading.

## What it does not say

- Not that a regulator has both channels. Which channel it has is
  [CLAIM-589](CLAIM-589.md)'s question: a permitted direction need not be actuated, nor
  an actuated one affordable.
- Nothing outside the tolerance. If operation may leave the band, the
  configuration can be moved at once, and operation comes within ε of it
  after ln(D/ε)/γ, which is also slower as γ falls. A configuration set
  far past its target acts as a push through h. That is not retuning in
  [CLAIM-1051](CLAIM-1051.md)'s sense.
- Nothing about feedback through maintained states ([CLAIM-400](CLAIM-400.md)). The model
  is open-loop, as [CLAIM-1192](CLAIM-1192.md)'s is.
- Not a law of organizations. The model is [CLAIM-1051](CLAIM-1051.md)'s relaxation
  toward a governed configuration. That claim's defeater says this can
  misdescribe how operation follows governance.

## The join

The manuscript governance-of-possibility, §7.3, join JB10: "An
organization whose operation has slowed is easier to redirect by
intervention and harder to govern by changing its rules." It was filed
at the owner's ruling of 2026-11-23, and the account [SYNTHESIS-123](../syntheses.d/SYNTHESIS-123.md)
integrates it.
