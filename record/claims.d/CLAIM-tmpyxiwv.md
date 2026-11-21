---
status: Proposed
title: 'When past and future are independent given a shared parameter, the shape of the Fisher spectrum fixes how predictive information grows: in a linear-Gaussian model it grows as (d/2) ln T with d resolved directions, as T^(1/p) when the spectrum falls as j^(−p), and as (ln T)²/(4a) when it falls as e^(−aj), so the power-law regime of Bialek, Nemenman and Tishby follows from a power-law spectrum'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the identity I(past; future) = I(θ; past) + I(θ; future) −
  I(θ; past, future) for past and future independent given θ, or in
  I(θ; X_{1:T}) = ½ Σ_j ln(1 + Tλ_j) for a Gaussian prior of unit
  variance on each eigendirection of a linear-Gaussian model; or a
  computation of 2G(T) − G(2T) on those spectra that does not approach
  the stated asymptotics. A nonlinear or singular model in which the
  growth differs is outside the claim, which is stated for the
  linear-Gaussian case and offered as the mechanism elsewhere.
tags:
- information-theory
- information-geometry
- learning-theory
- mathematical-statistics
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
rests_on:
- CLAIM-tmpj0k4q
grounds:
- THEORY-087
- LIT-tmpys7v3
uses:
- TERM-tmpxml4k
- TERM-tmp5z2du
bears_on:
- QUESTION-tmpzlagu
summary: >-
  Fills a gap in the exchange "Rich Get Richer Power Laws": A21 §4 gives
  three growth regimes for predictive information (bounded, log T, T^μ)
  and A21 §5 a toy count of resolved Fisher directions, and calls the
  second "not a general law connecting the Fisher spectrum to the amount
  of predictive information", leaving the two unconnected. In a
  linear-Gaussian model with a shared parameter they connect exactly:
  I_pred(T) = 2G(T) − G(2T) with G(T) = ½ Σ ln(1 + Tλ_j), which grows as
  (d/2) ln T for d equal eigenvalues, as T^(1/p) for λ_j ∝ j^(−p) and as
  (ln T)²/(4a) for λ_j ∝ e^(−aj). Checked numerically. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpj0k4q TERM-tmpxml4k TERM-tmp5z2du QUESTION-tmpzlagu — filed with this claim from the same exchange, Proposed -->
<!-- inactive-ok-file: LIT-tmpys7v3 — Deferred, registered 2026-11-21 from the exchange, unread -->

# CLAIM-tmpyxiwv: When past and future are independent given a shared parameter, the shape of the Fisher spectrum fixes how predictive information grows: in a linear-Gaussian model it grows as (d/2) ln T with d resolved directions, as T^(1/p) when the spectrum falls as j^(−p), and as (ln T)²/(4a) when it falls as e^(−aj), so the power-law regime of Bialek, Nemenman and Tishby follows from a power-law spectrum

## The gap it fills

A21 §4 lists three regimes of growth for predictive information
(TERM-tmpxml4k), the last "I_pred(T) ∼ cT^μ, 0 < μ < 1 … as can occur in
certain infinite-dimensional learning problems". A21 §5 counts the Fisher
directions n observations resolve, (nC)^(1/p) for a power-law spectrum
(CLAIM-tmpj0k4q), and then disclaims the link: "This is a toy calculation,
not a general law connecting the Fisher spectrum to the amount of
predictive information." The regimes are asserted and the spectrum is
counted; nothing joins them. This claim joins them in the one setting
where it can be done exactly.

## The derivation

**Step 1.** If past P = X_{1:T} and future F = X_{T+1:2T} are independent
given a parameter θ, then

  I(P; F) = I(θ; P) + I(θ; F) − I(θ; P, F),

since H(P) = H(P|θ) + I(θ;P), likewise for F, and
H(P,F) = H(P|θ) + H(F|θ) + I(θ; P,F). With G(T) = I(θ; X_{1:T}) and
stationarity, I_pred(T) = 2G(T) − G(2T). This is the source A21 §3 names
for the coin, made general: what past and future share is what each says
about θ.

**Step 2.** In a linear-Gaussian model, rotated to the eigenbasis of the
per-observation Fisher matrix, with a unit-variance Gaussian prior on each
coordinate, G(T) = ½ Σ_j ln(1 + Tλ_j) exactly.

**Step 3.** The spectrum's shape then fixes the growth:

- **d equal eigenvalues λ:** G(T) ≈ (d/2) ln(Tλ), so
  I_pred(T) ≈ (d/2) ln T − (d/2) ln 2: Bialek, Nemenman and Tishby's
  logarithmic regime, with the same (d/2) coefficient the record holds as
  the Bayesian Occam penalty of a regular model (THEORY-087).
- **λ_j = C j^(−p), p > 1:** G(T) ≈ ½ (CT)^(1/p) ∫₀^∞ ln(1 + u^(−p)) du
  = ½ (CT)^(1/p) π/sin(π/p), so
  I_pred(T) ≈ ½ (π/sin(π/p)) (2 − 2^(1/p)) (CT)^(1/p): the power-law
  regime, with μ = 1/p.
- **λ_j = C e^(−aj):** G(T) ≈ (ln CT)²/(4a), and I_pred(T) has the same
  leading term: growth faster than any multiple of ln T and slower than
  any power.

So the regime of predictive information is the regime of the count of
resolved directions, d_eff(T), integrated: each resolved direction adds
about ½ ln(Tλ_j), and the sum over the (CT)^(1/p) resolved ones is of
order (p/2)(CT)^(1/p).

## Check

The assistant computed 2G(T) − G(2T) on a two-million-term spectrum
(a numpy script of this session, not kept; the method is as stated).

- d = 3, λ = 1: I_pred = 5.890, 12.776 and 19.684 nats at T = 10², 10⁴,
  10⁶, against (3/2) ln(T/2) = 5.868, 12.776 and 19.684.
- λ_j = j^(−2): I_pred = 7.30, 26.63, 88.97, 287.35 and 915.95 at
  T = 10² … 10⁶, log–log slope 0.52 against 1/p = 0.5; at T = 10⁶ the
  formula gives ½·π·(2 − √2)·1000 = 920.
- λ_j = j^(−3): slope 0.38 over the same range, falling toward 1/3 as T
  grows; G(T)/((p/2)T^(1/p)) reaches 1.18 against the limit
  π/(p sin(π/p)) = 1.21.
- λ_j = e^(−0.5 j): the ratio of I_pred to (ln T)²/(4a) is 0.74, 0.83,
  0.88, 0.91 and 0.94 at T = 10², 10⁴, 10⁶, 10⁸, 10¹², approaching 1 as
  the subleading terms fade.

## What it does not say

- **Not that every process with power-law predictive information has a
  power-law spectrum.** Long-range dependent processes with no parameter
  to learn can grow too (TERM-tmpxml4k, condition 2); this is one
  mechanism, exact in one model.
- **Not that it holds in singular models.** There the logarithmic
  coefficient is the learning coefficient, not d/2 (THEORY-087,
  THEORY-1253), and the spectrum is not the right object.
- **Not that the process is ergodic.** The mixture over θ is not, and the
  growth comes from that (TERM-tmpxml4k, condition 1).
- **Not that criticality produces it.** No transition enters; A21 §4's
  caveat that these regimes "are not a one-to-one classification of
  physical criticality" stands.
