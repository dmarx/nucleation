---
status: Proposed
title: 'When influence shares are a softmax of logits trained by gradient on any loss of the shares, the part of a rare operator''s growth that depends on its own performance is proportional to its share, so its recovery exponent tends, as it becomes rare, to a value that does not depend on how good it is; a multiplicative contribution rule keeps that part independent of share'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-016, from the
    derivation below and the executed study CASE-tmpnti0m.
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: that is, a softmax share
  π = softmax(z), a loss L(π) whose partial derivatives in π are bounded
  near the resident shares, and a gradient update of z under which the
  coefficient of operator i's own derivative ∂L/∂π_i in the change of
  log π_i does not vanish as π_i → 0. A router whose shares are not a
  softmax of the trained logits, or whose update adds a term not derived
  from a loss of the shares (such as a usage bias), is outside the claim
  and does not defeat it.
tags:
- learning-theory
- complex-systems
- ecology
date: '2026-11-22'
line:
- distributed-agency
bears_on:
- QUESTION-132
- QUESTION-083
grounds:
- CASE-tmpnti0m
summary: >-
  For shares π = softmax(z) and any differentiable loss L(π),
  ∂L/∂z_i = π_i(∂L/∂π_i − Σ_j π_j ∂L/∂π_j). So a gradient step on the
  logits moves a rare operator's logit, the channel through which its own
  performance acts, in proportion to its share. Its log share also moves
  with the residents' drift, which does not depend on it. As the operator
  becomes rare, its recovery exponent (QUESTION-132's λ_i) tends to a value
  that is the same for a competent and an incompetent operator. That holds
  for ordinary mixture-of-experts gating and for a load-balancing loss
  added to it. A multiplicative contribution rule, Δz_i = η(ℓ̂ − ℓ_i),
  keeps the operator's own term independent of share. In CASE-tmpnti0m, at
  matched participation, a rare specialist's growth rate fell from 0.010
  to 0.00075 per rare sample as its starting share went from 10⁻² to 10⁻⁵
  under gating, with or without the balancing loss. It stayed at 0.036 to
  0.044 under the multiplicative rule. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmpnti0m — new, filed with this claim -->

# CLAIM-tmp1u4m3: When influence shares are a softmax of logits trained by gradient on any loss of the shares, the part of a rare operator's growth that depends on its own performance is proportional to its share, so its recovery exponent tends, as it becomes rare, to a value that does not depend on how good it is; a multiplicative contribution rule keeps that part independent of share

## The derivation

Let π = softmax(z), so ∂π_j/∂z_i = π_j(δ_ij − π_i). For any differentiable
L(π), write g_j = ∂L/∂π_j and ḡ = Σ_j π_j g_j. Then

  ∂L/∂z_i = Σ_j g_j π_j(δ_ij − π_i) = π_i(g_i − ḡ).

A gradient step Δz = −η ∂L/∂z changes log π_i by

  Δ log π_i = Δz_i − Σ_j π_j Δz_j
            = −η π_i(g_i − ḡ) + η Σ_j π_j²(g_j − ḡ).

Operator i's own performance enters only through g_i. Its coefficient is
−η π_i(1 − π_i), which vanishes with π_i. The second sum is the
residents' drift. Its term in i is O(π_i²), and the rest does not depend
on i. So, with g bounded near the resident shares, the growth rate of a
rare operator tends, as π_i → 0, to the residents' drift. That rate is the
same for any operator made rare, however good it is. Recovery driven by
its competence is then algebraic, not exponential: dπ_i ∝ π_i², taking a
time of order 1/π_i.

- **Ordinary mixture-of-experts gating.** Under the mixture
  log-likelihood, g_i = −p_i/Σ_j π_j p_j, which is bounded while the
  residents' likelihoods are bounded below. The logit step is h_i − π_i,
  the posterior minus the prior, and that equals π_i times a bounded
  factor.
- **A load-balancing loss.** Added to L, it is also a function of the
  shares. Its gradient carries the same factor π_i, so it does not
  restore a rare operator either.
- **A multiplicative contribution rule.** Under Δz_ci = η(ℓ̂ − ℓ_i), the
  operator's own term is η(ℓ̂ − ℓ_i), whatever its share. Its recovery
  exponent stays at the mean of that advantage over the residents.
- **A usage bias.** Moved by usage and added to the logits, it is not the
  gradient of a loss of the shares, so it falls outside the identity. It
  restores a rare operator whether or not the operator is competent.

## The check

CASE-tmpnti0m ran the three cases at K = 4, where moe, moe_aux and rep match
on participation and performance. The rare specialist was given share ε,
frozen, with no further intervention. Medians over 6 seeds:

| rule | growth rate per rare sample, ε = 10⁻² / 10⁻³ / 10⁻⁵ | recovered from 10⁻⁵ within ~3,200 rare samples |
|---|---|---|
| moe | 0.010 / 0.0033 / 0.00075 | 0/6 |
| moe_aux | 0.0098 / 0.0034 / 0.00075 | 0/6 |
| rep | 0.036 / 0.042 / 0.044 | 6/6 |

The rate under gating does not fall exactly in proportion to ε. A residue
of about 10⁻³ per rare sample remains at ε = 10⁻⁵, and the derivation puts
it in the residents' drift. An incompetent copy made rare under moe stays
at its share (rate −2 × 10⁻⁵). Under rep it is driven out.

## What it bears on

- **QUESTION-132.** Its recovery exponent is the test of stabilizing
  coexistence. Under softmax-gradient routing, the exponent at rarity
  does not reflect whether the niche is open to the rare operator. A
  positive λ_i in such a system therefore cannot be read as the niche
  being open to it, and a near-zero one cannot be read as closure. The
  exponent has to be measured at a finite share and said so, or the
  influence rule has to be multiplicative in the operator's advantage.
- **QUESTION-083.** Ordinary mixture-of-experts routing specializes, as
  the record already holds. It does not give a rare specialist an
  exponential route back, and neither does balancing in the gradient. A
  bias outside the gradient does, without regard to competence.

## What it does not say

- It does not say that every gradient-trained router fails to recover
  rare experts. At a finite share, recovery happens, as it did here from
  10⁻² and 10⁻³.
- It does not say that the multiplicative rule is better overall. It also
  let a spare duplicate the rare specialist when there was room (see
  CLAIM-tmp1jz5w).
- Mixtures that use top-k routing, noise or temperature are not covered,
  beyond what the identity itself implies.
