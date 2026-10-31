---
number: 1258
status: Active
formerly:
- THEORY-tmpe0idn
title: "The steady state of Hennick and De Baerdemacker's fractional Fokker–Planck model of SGD is a tempered posterior only within a region of constant effective diffusion; the weights between regions, where accessibility would act, are not derived"
version: 1
tags:
- learning-theory
- probabilistic-modeling
date: '2026-10-31'
source:
- LIT-1879
summary: >-
  Hennick and De Baerdemacker (2025; ICLR 2026), [LIT-1879](../literature.d/LIT-1879.md), read in
  [NOTE-1467](../notes.d/NOTE-1467.md). Their Lemma 3.3 and Corollary 3.2 show that where a scalar
  effective diffusion D_ξ is constant, the steady state is exp(−L_m/D_ξ),
  the posterior at effective sample size 1/D_ξ. That is a temperature, and
  inside such a region it leaves no room for an accessibility correction.
  Across regions their own equation's zero-flux state is ∝ exp(−∫∇L/D),
  set by D along the paths between regions; checked on a double well.
  Active: the algebra and the counterexample are elementary and checked.
  It does not say SGD is far from Bayesian across regions, only that the
  paper does not show it is close.
---
<!-- inactive-ok-file: QUESTION-363 THEORY-1272 — Open or Proposed; the question this bears on, and the sibling filed from the same reading -->

# THEORY-1258: The steady state of Hennick and De Baerdemacker's fractional Fokker–Planck model of SGD is a tempered posterior only within a region of constant effective diffusion; the weights between regions, where accessibility would act, are not derived

## Source

Hennick and De Baerdemacker (2025), [LIT-1879](../literature.d/LIT-1879.md), §3.4 (Lemma 3.3,
Corollary 3.2), §4.2 (Figs. 3–4, Table 2) and App. D.3 of arXiv
2503.22478v2; read in [NOTE-1467](../notes.d/NOTE-1467.md).

## What was actually shown

**The paper's result.** For the Fokker–Planck equation
∂p/∂t = ∇·(D∇p − γp∇L_m) (Eq. 2, with a Caputo time derivative in Eq. 4),
on a subset W where the effective diffusion is a constant D_ξ and a steady
state exists, p_s ∝ exp(−γL_m/D_ξ) (Lemma 3.3). With γ = 1 and log loss,
p_s^(mD_ξ) ∝ p(X_m|w) (Corollary 3.2). That is the identity
(e^(−L_m/D_ξ))^(mD_ξ) = e^(−mL_m): inside W, SGD's steady state is the
posterior with a flat prior at effective sample size 1/D_ξ, a tempered
posterior. The fractional derivative plays no part at steady state.

**What it leaves out.** "Accessibility" in the abstract would have to
change how mass is shared between regions, since inside one region of
constant D_ξ the steady state is exactly a tempered posterior. Between
regions D differs (D_ξ = ξ^(2 − 2λ/d_s), Corollary 3.1, and λ changes).
For the paper's own equation with a scalar D(w) that varies, the zero-flux
steady state solves D∇p = −p∇L, so p ∝ exp(−∫∇L/D), which depends on D
along the paths that join regions and is not exp(−L/D(w)) region by
region. Checked on a one-dimensional double well L = (w² − 1)² with
D = 0.3 + 0.1 tanh(5w): the left basin holds 0.87 of the zero-flux mass
and 0.41 of exp(−L/D(w)); inside the right basin, where D is nearly
constant, the two agree in shape to 2%.

**The experiment.** In §4.2 the cross-cluster masses of SGD solutions on
a moons classifier are compared with an SGLD posterior after "tempering"
with ξ = 0.5, chosen by the KL between the empirical and theoretical SGD
distributions (Fig. 3), with good agreement (Table 2: KL 0.009). The
untempered SGD distribution prefers another cluster (Fig. 4b). So the
cross-region agreement is obtained with a fitted scale, and the
"posterior" is SGLD seeded at SGD's own lowest-loss, lowest-LLC solutions.

**What could have failed.** The steady state could have depended on D
only through each region's own value. For an equation of this form it
cannot.

## What this does not say

- **That SGD's cross-region weights are far from the posterior's.** Only
  that the paper derives no correction for them, and its one test fits ξ.
- **Anything about training time.** The correspondence is temperature to
  sample size, 1/D_ξ against n, of the same kind as Mandt et al.'s ε/S
  against 1/N ([THEORY-1255](THEORY-1255.md)). The paper ties its steady state to
  regions where λ is "locally constant ... away from phase transitions"
  (p. 7), so it says nothing about the order of transitions over training.
- **That the Fokker–Planck form is the right one for SGD.** Other
  conventions for a position-dependent D (Itô, Stratonovich) give other
  steady states; all of them depend on D between regions.
- **That a steady state exists.** The paper assumes it and allows that it
  may not (§5.1, Prop. D.1).
