---
number: 1191
status: Proposed
formerly:
- CLAIM-tmpx7oaj
title: 'Gain alone has no comfortable optimum'
statement: >-
  With the user's commands held fixed, the information between a scroll
  gesture and the displacement it produces under a gain k does not prefer a
  comfortable gain: it is the same for every nonzero gain when the mapping
  is noiseless (infinite for a continuous command), and it rises with the
  size of the gain when the displacement carries additive Gaussian noise or
  is quantized to pixels; so any interior optimum a First Contact score
  finds over gain must come from how the user's commands change with the
  gain
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: a noiseless injective gain under which
  command-to-displacement information changes with k at a fixed command
  distribution, or an additive Gaussian output noise of fixed variance
  under which it falls as the gain grows. A scroll model whose noise
  scales with the gain, or whose displacement saturates, is outside the
  stated conditions and does not defeat it.
tags:
- information-theory
- control-theory
- learning-theory
date: '2026-11-22'
line:
- will-organization
- distributed-agency
grounds:
- THEORY-2147
summary: >-
  A gap fill for A4 of the exchange "Explain First Contact RL" (ChatGPT,
  2026-11-22), which held that for Δy = kΔx "changing k does not change
  the information carried by the input", so raw input-output information
  "may not distinguish a comfortable sensitivity from a frustrating one".
  That holds in A's idealization, a noiseless mapping, and is stated here
  with its conditions and the case it misses: with display quantization or
  output noise the raw score rises with gain, a bias toward the fastest
  scrolling, not indifference. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-419 — Proposed; the reading and the case this fills a gap in -->

# CLAIM-1191: Gain alone has no comfortable optimum

## The derivation

Let the command X (finger displacement) have a fixed distribution and the
displacement be Y = kX (+ noise), k ≠ 0. This is First Contact's control
term I(X; S_{t+1} | S_t) for a scroll whose state advances by Y.

1. **Noiseless.** y = kx is injective, so Y determines X and I(X; Y) =
   H(X) for a discrete command, whatever k; for a command with a density
   the information is infinite for every k. Mutual information is
   invariant under injective maps of either variable. Checked with
   `python3 -I`: five equiprobable commands give I = 2.3219 bits at
   k = 0.5, 1 and 3.
2. **Additive Gaussian output noise.** Y = kX + ε, ε ~ N(0, σ²)
   independent. For Gaussian X with variance s², I = ½ log₂(1 + k²s²/σ²),
   strictly increasing in |k|. For any X, Y/k = X + ε/k, and for |k₂| >
   |k₁| the channel at k₁ is the channel at k₂ followed by independent
   Gaussian noise of variance σ²(1/k₁² − 1/k₂²), so by data processing the
   information at k₂ is at least that at k₁. Checked: with s = 1, σ = 0.5,
   I = 0.16, 0.50, 1.16, 2.04, 3.01 bits at k = 0.25, 0.5, 1, 2, 4.
3. **Pixel quantization.** Y = round(kX) is a deterministic function of X,
   so I(X; Y) = H(Y), which for a command with a density grows like
   log₂|k| once k is large. Checked by simulation for a standard normal
   command: H(Y) = 1.24, 2.10, 3.06, 4.05, 5.05 bits at k = 0.5, 1, 2, 4, 8.

In no case does the score at fixed behaviour have an interior maximum in k.

## What follows

A First Contact score over scroll gain can single out a comfortable gain
only through the premise the paper rests on, that "the more intuitive the
interface, the less noisy the user's commands" ([NOTE-2236](../notes.d/NOTE-2236.md), §1): the
command distribution must itself depend on k. A4 saw this ("the human's
behavior changes in response to the mapping"). What A4 did not say is that
with a realistic display the raw score is biased toward high gain. A study
of the scroll case ([CASE-419](../cases.d/CASE-419.md)) should therefore estimate the score
over the user's realized gestures under each gain, not compute it from the
physics, and should read an interior optimum as evidence about the user,
not about the mapping. The same holds for momentum and friction parameters
insofar as they act as an injective map from release velocity to coast
distance.

## Scope

The conditions are a fixed command distribution and a gain that does not
change the noise. Motor noise in the command itself does not alter the
argument, since it is part of X's distribution. A saturating or
non-injective mapping (a displacement cap, a dead zone) can lower the
information at high gain and is not covered.
