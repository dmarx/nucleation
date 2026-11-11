---
number: 1315
status: Active
formerly:
- THEORY-tmp7q08l
title: 'As a stochastically forced system approaches a fold bifurcation its dominant eigenvalue goes to zero, so it recovers ever more slowly from small perturbations, and under ongoing perturbation this critical slowing down shows as rising lag-1 autocorrelation and rising variance; skewness and flickering are further warnings not caused by slowing; but the same signals, less pronounced, also precede thresholds that are not bifurcations, so they mark proximity to a broad class of thresholds and not which kind, nor when the shift will come'
version: 2
history:
- version: 2
  date: '2026-11-11'
  note: >-
    Reading review of 2026-11-11 (by topic, second run, part P), under
    ADR-091 and ADR-093. corroborates CLAIM-478 added. The claim's
    note of 2026-11-03: "Scheffer et al. 2009 (NOTE-1536, THEORY-1315)
    give the generic slowing down the second half uses near an
    instability"; the note's caution that slowness alone does not show new
    organization stands with it. An inactive-ok directive names the Proposed claim. No other change.
tags:
- complex-systems
- natural-sciences
date: '2026-11-03'
source:
- LIT-1956
summary: >-
  Scheffer et al. (2009), [LIT-1956](../literature.d/LIT-1956.md), read in [NOTE-1536](../notes.d/NOTE-1536.md) (Skimmed)
  from the version reprinted as chapter 2 of Dakos's 2011 thesis. Active
  for the slowing-down result, which is standard (Wissel 1984), checked in
  the chapter's Box 2.2 example, and re-derived and simulated here for
  variance σ²/(2|λ|) and autocorrelation e^{λΔ} since the chapter's Box 2.3
  was not extractable. The scope and timing caveats are the authors' (p.
  31). It does not say the signals have been shown in chaotic systems,
  which the review calls "less well studied", or that any of the reviewed
  empirical cases was checked here.
corroborates:
- CLAIM-478
---
<!-- inactive-ok-file: CLAIM-478 — Proposed; the claim this reading corroborates, nothing here rests on it -->
<!-- inactive-ok-file: NOTE-1536 — Proposed, Open, Deferred, Unfetched, Unavailable or new; cited as open -->
<!-- inactive-ok-file: LIT-720 — Unavailable; the earlier Scheffer paper, cited as context -->

# THEORY-1315: As a stochastically forced system approaches a fold bifurcation its dominant eigenvalue goes to zero, so it recovers ever more slowly from small perturbations, and under ongoing perturbation this critical slowing down shows as rising lag-1 autocorrelation and rising variance; skewness and flickering are further warnings not caused by slowing; but the same signals, less pronounced, also precede thresholds that are not bifurcations, so they mark proximity to a broad class of thresholds and not which kind, nor when the shift will come

## Source

Scheffer, Bascompte, Brock, Brovkin, Carpenter, Dakos, Held, van Nes,
Rietkerk and Sugihara (2009), [LIT-1956](../literature.d/LIT-1956.md), read in [NOTE-1536](../notes.d/NOTE-1536.md) from
chapter 2 (pp. 17–32) of V. Dakos, *Expecting the Unexpected* (Wageningen,
2011), edepot.wur.nl/168815. Earlier work: Scheffer et al. 2001 ([LIT-720](../literature.d/LIT-720.md))
and Scheffer and Carpenter 2003 ([LIT-726](../literature.d/LIT-726.md)).

## What was actually shown

**Slowing down (p. 19).** "At fold bifurcation points … the dominant
eigenvalue characterizing the rates of change around the equilibrium
becomes zero", which "can be proven" for "any continuous model approaching
a fold bifurcation" (Wissel 1984). Box 2.2's transcritical example gives
λ₁ = −γ(b − a), zero at b = a (checked).

**Autocorrelation and variance (pp. 21–22).** For the linearized stable
point dx = λx dt + σ dW, λ < 0, the stationary variance is σ²/(2|λ|) and the
lag-Δ autocorrelation e^{λΔ}; both rise without bound or to 1 as λ → 0⁻.
Simulated here at λ = −2, −1, −0.5, −0.1: variances 0.26, 0.53, 1.03, 5.16
(exact 0.25, 0.50, 1.00, 5.00), autocorrelations 0.14, 0.40, 0.62, 0.91
(exact 0.14, 0.37, 0.61, 0.90). The review grants that variance could in
principle fall as the system tracks fluctuations less well, but models show
it "usually" rises (p. 21).

**Signals without slowing (pp. 22–24).** Skewness, from the unstable point
approaching on one side; flickering, noise-driven switching once bistable.

**The scope (p. 31).** "The same signals may even occur, albeit in a less
pronounced way, as the system approaches a threshold that is not related
to catastrophic bifurcations", so they indicate "proximity to a broad class
of thresholds, where small forces can cause major changes". And
"perturbations will often trigger a transition well before a bifurcation
point is reached", so the moment "remains difficult to predict".

## What this does not say

- That the signals are reliable in real data: detection needs long series
  and filtering choices, and false positives and negatives are listed
  (p. 31).
- That they are known for chaotic systems or basin-boundary collisions:
  "we know of no explicit work" on the latter (p. 24).
- That slowing near a transition makes new organization. It marks
  proximity to a threshold, of either kind.
