---
status: Read
paper: LIT-2962
title: 'Beck and Cohen, Superstatistics, read for how a spread of an intensive parameter turns Boltzmann factors into other statistics'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Read on 2026-11-22 by a delegated reader from arXiv cond-mat/0205097v2
    (https://arxiv.org/pdf/cond-mat/0205097, the authors' manuscript,
    stamped 14 Nov 2002, 12 pages): the whole text, pp. 1–10, and the
    reference list. Nothing skipped. The published text (Physica A 322,
    267–275, 2003; checked on Crossref) was not compared. Every quotation
    below rechecked by the filer by script against the extracted text; the
    gamma, uniform and small-variance formulas checked numerically with
    python3 -I by the reader, and the gamma and uniform tails again by the
    filer (CLAIM-tmpf9qt9).
date: '2026-11-22'
summary: >-
  A letter defining superstatistics: the long-run statistics of a system
  whose inverse temperature fluctuates slowly is the Laplace transform of
  that temperature's density. A gamma density gives Tsallis's q-exponential
  exactly; all densities agree at small variance and differ at third order
  and at large energy. It never says "power law"; only some densities give
  one.
---
<!-- inactive-ok-file: CLAIM-795 CLAIM-769 CLAIM-781 CLAIM-840 CLAIM-829 CLAIM-803 CLAIM-841 THEORY-2131 THEORY-tmpczldx CLAIM-tmpf9qt9 ARG-tmpa8ghr ARG-tmp3ppjy — Proposed or new; the entries this reading bears on, its own reading, and the claim and argument filed with it -->

# NOTE-tmpj8ro5: Beck and Cohen, Superstatistics, read for how a spread of an intensive parameter turns Boltzmann factors into other statistics

## Contribution

It names and generalizes a construction Beck had for one case (a Langevin
particle with χ²-distributed β, PRL 87, 180601, 2001, the paper's ref. 5):
"after averaging over the fluctuations one can obtain as an effective
description not only Tsallis statistics but an infinite set of more
general statistics, which we will call 'superstatistics'" (p. 1). It adds
a general small-variance universality result, a definition of the
entropic index q for every superstatistics, and the distinction between
averaging Boltzmann factors (type A) and normalized densities (type B).

## Key results

1. **The effective Boltzmann factor is a Laplace transform** (eq. 2,
   p. 3): B(E) = ∫ f(β) e^(−βE) dβ, so "the generalized Boltzmann factor
   of superstatistics is given by the Laplace transform of the probability
   density f(β)". Ordinary statistics for f = δ(β − β₀). Criteria: f a
   normalized density, B normalizable, and reduction to Boltzmann–Gibbs
   without fluctuations.
2. **Gamma gives Tsallis** (eqs. 11–13, pp. 5–6). With
   f(β) = (1/(bΓ(c)))(β/b)^(c−1) e^(−β/b), B = (1 + bE)^(−c), the
   q-exponential with c = 1/(q − 1) and bc = β₀. "It is normalizable for
   c > 1" (with ρ(E) = 1). 2c is read "as the effective number of degrees
   of freedom contributing to the fluctuating β" (p. 5): β is a sum of
   2c squared Gaussians (eq. 12).
3. **Other densities** (pp. 4–7). Uniform on [a, a + b] gives eq. 5, a
   difference of exponentials over bE, so an exponential tail when a > 0;
   two-level gives a sum of two exponentials (eq. 9; eq. 7 misprints δ(a)
   for δ(β − a)); lognormal and F only as series (eqs. 16, 20). The F with
   v = 2 "is a Tsallis distribution in β-space, not in E-space" (p. 6).
4. **Universality at small variance** (eqs. 21–22, pp. 7–8): "one always
   obtains the same result for small σ", B = e^(−β₀E)(1 + ½σ²E² +
   O(σ³E³)), from expanding ⟨e^(−(β−β₀)E)⟩ in central moments.
5. **A q for every superstatistics** (eqs. 24–25, p. 8): (q − 1)β₀² = σ²,
   q = ⟨β²⟩/⟨β⟩²; √(q − 1) = σ/β₀ "is just the coefficient of variation
   of the distribution f(β)".
6. **Maximum entropy only to first order** (p. 8): at larger σE "the
   densities given by B(E) do not extremize the Tsallis entropies in
   general".
7. **Third order discriminates** (eqs. 26–30, pp. 8–9): the coefficient
   g(q) of β₀³E³ is 0 for uniform and two-level, −⅓(q − 1)² for gamma,
   −⅙(q³ − 3q + 2) for lognormal: "one can distinguish between Tsallis
   statistics and other superstatistics by the third-order term" (p. 9).
8. **Large E is not universal** (p. 7): "While in general the large-E
   behavior is different for all superstatistics (it strongly depends on
   the function f(β)), we now show that the low-E behavior is universal."
9. **Type A and type B** (p. 9): for E = ½u² and a gamma f, type A gives
   q = 1 + 1/c and type B q = 1 + 2/(2c + 1); type B with f equals type A
   with a reweighted f̃.
10. **Applications cited, not shown**: Taylor–Couette and Lagrangian
    turbulence, hadron spectra, cosmic rays, plasmas. "In the turbulence
    applications ... the fluctuating intensive quantity is related to the
    energy dissipation rate of the flow" (p. 9).

## Assumptions

- **Time-scale separation**: "This time scale T is much larger than the
  relaxation time that the single cells need to reach local equilibrium"
  (p. 2).
- β > 0; a Gaussian f is called unphysical (p. 4).
- The long-run density is the average over cells a test particle visits
  over times much longer than T.
- ρ(E) = 1 for normalizability unless stated.
- f(β) is "a priori unknown", "determined by the invariant measure of the
  underlying dynamical system" (pp. 3–4), and not derived here. "The
  central hypothesis of our paper is that generalized Boltzmann factors of
  the form (2) are physically relevant for large classes of dynamically
  complex systems" (p. 3).

## Concepts

Superstatistics ("the statistics of the statistics"); effective Boltzmann
factor; Laplace transform of the parameter density; χ² inverse
temperature with 2c degrees of freedom; Tsallis q-exponential and the
index q as a squared coefficient of variation; small-variance
universality; the third-order discriminant g(q); type-A and type-B
superstatistics.

## Bearing on the record

- **CLAIM-795, item 4: grounds it, with a qualification.** Eq. 13 is item
  4's formula with energy for time and inverse temperature for rate:
  ∫ gamma(β) e^(−βE) dβ = (1 + bE)^(−c), the survival (b′/(b′ + t))^a
  with a = c, b′ = 1/b. The paper does not treat waiting times, and its
  non-gamma cases show that a spread gives a power law only with weight
  near β = 0. The assistant's CLAIM-tmpf9qt9 states that condition and
  checks it. ARG-tmpa8ghr argues the support.
- **CLAIM-769: supports its second half by parallel.** Eq. 2 is
  THEORY-2131's s(t) = ∫p(λ)e^(−λt)dλ; the uniform with a = 0 and the gamma
  cases are THEORY-2131's. The exact hyperbola is c = 1, which Beck marks
  non-normalizable with ρ(E) = 1 ("normalizable for c > 1"). Beck's
  time-scale separation parallels CLAIM-781's separation of rates. Nothing
  on rate trees or discounting. THEORY-tmpczldx `corroborates` CLAIM-769.
- **THEORY-2131: corroborates the mathematics**, the same integral and the
  same gamma and uniform results, derived in physics, not Sozou's reading
  of discounting; its `promote_when` asks for Sozou and is not met.
- **ARG-tmp3ppjy: qualifies its routing.** Item 4 now rests on this
  reading as well as on THEORY-2131.
- **NOTE-tmpa7yd2: consistent.** Newman's "combinations of exponentials"
  is not this construction.
- **QUESTION-505: supports one row and adds a reading.** The gamma
  mixture's exponent is its shape c, half the number of squared Gaussian
  degrees of freedom summed into β (eq. 12), and type-B averaging shifts it
  (c → c + ½ for E = ½u²).
- **CLAIM-841** (filer C's file): supports its "broad relaxation spectra"
  row as a further instance with no transition; Beck's flagship
  application is turbulence, a separate row, so the two rows can be one
  system read twice. Reported, not noted there.
- **LEAD-209: qualifies its table.** The turbulence and mixture columns are
  not exclusive in Beck's account, and the third-order term g(q) is a
  discriminating observable the table lacks.
- **CLAIM-840 and CLAIM-829: support their "what it does not say"**: a
  q-exponential bulk and tail with no transition; the only knob is the
  variance.
- **CLAIM-803: supports in kind**; g(q) separates superstatistics from one
  another, not mixtures from feedback.

## Limitations

- A letter: the central hypothesis is asserted, f(β) comes from no
  dynamics, and the applications are cited, not shown.
- Universality is a small-σE expansion. Nothing is proved about tails
  beyond the closed forms; lognormal and F have none. The paper never uses
  the words "power law", "tail" or "heavy" (grep of the text).
- Read as arXiv v2, not the journal text.
- A gap the record uses: which densities give a power-law tail. Filled by
  the assistant in CLAIM-tmpf9qt9 (weight at β = 0, by the Tauberian
  correspondence), checked numerically.
