---
number: 849
status: Proposed
formerly:
- CLAIM-tmpyxiwv
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
- CLAIM-825
grounds:
- THEORY-087
- THEORY-2151
uses:
- TERM-141
- TERM-135
bears_on:
- QUESTION-517
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
<!-- inactive-ok-file: CLAIM-825 TERM-141 — filed with this claim from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-154 THEORY-2151 — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# CLAIM-849: When past and future are independent given a shared parameter, the shape of the Fisher spectrum fixes how predictive information grows: in a linear-Gaussian model it grows as (d/2) ln T with d resolved directions, as T^(1/p) when the spectrum falls as j^(−p), and as (ln T)²/(4a) when it falls as e^(−aj), so the power-law regime of Bialek, Nemenman and Tishby follows from a power-law spectrum

## The gap it fills

A21 §4 lists three regimes of growth for predictive information
([TERM-141](../terms.d/TERM-141.md)), the last "I_pred(T) ∼ cT^μ, 0 < μ < 1 … as can occur in
certain infinite-dimensional learning problems". A21 §5 counts the Fisher
directions n observations resolve, (nC)^(1/p) for a power-law spectrum
([CLAIM-825](CLAIM-825.md)), and then disclaims the link: "This is a toy calculation,
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
  the Bayesian Occam penalty of a regular model ([THEORY-087](../theory.d/THEORY-087.md)).
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

The three regimes are Bialek, Nemenman and Tishby's ([LIT-3008](../literature.d/LIT-3008.md)), as A21
§4 states them; the work was read on 2026-11-21 ([THEORY-2151](../theory.d/THEORY-2151.md)), and
what it carries is in the note below. The derivation
and the check above do not depend on it; what does is the attribution of
the regimes, taken from A.

## What it does not say

- **Not that every process with power-law predictive information has a
  power-law spectrum.** Long-range dependent processes with no parameter
  to learn can grow too ([TERM-141](../terms.d/TERM-141.md), condition 2); this is one
  mechanism, exact in one model.
- **Not that it holds in singular models.** There the logarithmic
  coefficient is the learning coefficient, not d/2 ([THEORY-087](../theory.d/THEORY-087.md),
  [THEORY-1253](../theory.d/THEORY-1253.md)), and the spectrum is not the right object.
- **Not that the process is ergodic.** The mixture over θ is not, and the
  growth comes from that ([TERM-141](../terms.d/TERM-141.md), condition 1).
- **Not that criticality produces it.** No transition enters; A21 §4's
  caveat that these regimes "are not a one-to-one classification of
  physical criticality" stands.

## Note of 2026-11-21: Bialek, Nemenman & Tishby, read

Read in [NOTE-2243](../notes.d/NOTE-2243.md), filed as [THEORY-2151](../theory.d/THEORY-2151.md), which replaces the unread
LIT in this claim's grounds. What it carries ([ARG-154](../arguments.d/ARG-154.md)):

- **(d/2) ln T is theirs.** §4.1, Eq. 41: linear regression with Gaussian
  noise and a prior on the coefficients gives S₁(N) → (K/2) log₂ N,
  independent of the basis; §4.2 gives the same for any K-parameter family.
  Their I_pred has an infinite future and equals the data–parameter
  information, which is Step 1 in that form; with this claim's T′ = T it
  becomes (K/2) log(T/2), as stated above.
- **T^(1/p) is an instance of their §4.5 result, as to exponent only.**
  Their power law, N^(μ/(μ+1)), is derived in the annealed approximation
  from an essential singularity of the density of divergences; this
  claim's model is a case of it. The filer computed their annealed quantity
  in this model: S₁^(a) = G(N) + ½ Σ Nλ_j/(1 + Nλ_j), which for λ_j = j^(−p) grows
  as N^(1/p) with a coefficient larger than the exact G's by a factor
  tending to 1 + 1/p (1.501 at p = 2, 1.341 at p = 3, N = 10⁶; [NOTE-2243](../notes.d/NOTE-2243.md)).
  So the exponent agrees and the paper's coefficients should not be cited
  for it; the exact G above is the right object. The mapping is this
  claim's, not the paper's, which knew of no complete Bayesian family of
  power-law scalings (p. 32).
- **(ln T)²/(4a) is not in the paper.** It is this claim's.

The title's "the power-law regime of Bialek, Nemenman and Tishby follows
from a power-law spectrum" should be read with that qualification: their
regime, by their mechanism, as to exponent. Their conditions also bear: no
long-range correlations given the parameters (Eq. 65, of which this
claim's conditional independence is a stronger form), and a degenerate
Fisher matrix lowering the dimension (Eq. 64), which agrees with the
exclusion of singular models above.
