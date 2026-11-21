---
status: Proposed
title: 'A model has no single practical dimension: the number of parameter directions a data set resolves grows with the data, as a power of the sample size when the Fisher spectrum falls as a power of rank and as its logarithm when it falls exponentially, so zooming out and demanding precision move effective dimension in opposite directions'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  A model whose Fisher information grows in proportion to the number of
  independent observations, with a fixed eigenbasis, in which the number
  of eigendirections with nλ_j ≥ 1 does not grow as (nC)^(1/p) for a
  spectrum λ_j = C j^(−p), or as ln(nC)/a for λ_j = C e^(−aj); or a
  showing that the resolvability threshold nλ_j ≳ 1 does not track which
  directions a data set of size n constrains, so the count it gives is not
  an effective dimension. A model whose Fisher information does not scale
  with n, or whose eigenbasis turns with the data, is outside the claim.
tags:
- information-geometry
- mathematical-statistics
- learning-theory
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
grounds:
- THEORY-774
- THEORY-777
uses:
- TERM-tmp5z2du
summary: >-
  A's toy derivation at A21 §5 and the opposition at A21 §7 of the
  exchange "Rich Get Richer Power Laws": with n observations a direction
  of Fisher eigenvalue λ_j is resolved roughly when nλ_j ≥ 1, so a
  power-law spectrum C j^(−p) resolves about (nC)^(1/p) directions and an
  exponential one about ln(nC)/a; "a model does not necessarily possess
  one fixed practical dimensionality". Coarse-graining, which the record
  holds as compressing parameter space ([THEORY-777](../theory.d/THEORY-777.md), [THEORY-742](../theory.d/THEORY-742.md)), moves the
  count down; more data move it up. The assistant checked both counts.
  The wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A21); adopting it is the owner's call.
bears_on:
- QUESTION-tmpzlagu
---
<!-- inactive-ok-file: THEORY-777 — Proposed reading, the compression half -->
<!-- inactive-ok-file: TERM-tmp5z2du CLAIM-tmpyxiwv — filed with this claim from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-tmpu5yj6 THEORY-tmpd7a4j — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# CLAIM-tmpj0k4q: A model has no single practical dimension: the number of parameter directions a data set resolves grows with the data, as a power of the sample size when the Fisher spectrum falls as a power of rank and as its logarithm when it falls exponentially, so zooming out and demanding precision move effective dimension in opposite directions

## The claim

A21 §5: with n independent observations "the Fisher information
typically grows approximately in proportion to n", so "under a simple
normalized noise convention, a rough distinguishability criterion is
nλ_j ≳ 1". Then

- for λ_j = C j^(−p), the resolved count is d_eff(n) ~ (nC)^(1/p);
- for λ_j = C e^(−aj), it is d_eff(n) ~ ln(nC)/a.

"**A model does not necessarily possess one fixed practical
dimensionality. Its effective dimension can depend on observational
resolution.** With limited data, it may look like a three-parameter
model. With much more data, previously invisible parameter combinations
become detectable."

A21 §7 sets this against coarse-graining: "**Zooming out** More
microscopic distinctions become irrelevant. We may need fewer effective
parameters … **Demanding more precision** Previously negligible
differences become detectable." Both can hold of one system: "The number
of parameters required to specify the statistical law can decrease, while
the amount of information needed to specify a particular realization
remains enormous."

## Check

The assistant counted the directions with nλ_j ≥ 1 on a million-term
spectrum. For λ_j = j^(−2) the count is 10, 31, 100, 316 and 1000 at
n = 10², 10³, 10⁴, 10⁵, 10⁶, a log–log slope of 0.501 against 1/p = 0.5;
for λ_j = j^(−3), 4, 10, 21, 46 and 100, slope 0.346 against 0.333 (the
floor of a small count biases it up). For λ_j = e^(−0.5 j) the count is
9, 18, 27, 36 and 55 at n = 10², 10⁴, 10⁶, 10⁸ and 10¹², against
ln n/a = 9.2, 18.4, 27.6, 36.8 and 55.3. (A numpy script of this session,
not kept; the method is as stated.)

The work cited for the sloppy-model setting, Transtrum and colleagues'
review ([LIT-tmpm1tji](../literature.d/LIT-tmpm1tji.md)), was read on 2026-11-21 and corroborates the
compression half only ([THEORY-tmpd7a4j](../theory.d/THEORY-tmpd7a4j.md), [ARG-tmpu5yj6](../arguments.d/ARG-tmpu5yj6.md); see the note below).
The count above does not depend on it.

## What it does not say

- **Not a general law.** A calls it "a toy calculation, not a general law
  connecting the Fisher spectrum to the amount of predictive
  information". It needs Fisher information linear in n and a fixed
  eigenbasis, which a nonlinear model gives only near a point and a
  singular model not at all ([THEORY-1253](../theory.d/THEORY-1253.md)). The link to predictive
  information that A leaves out is [CLAIM-tmpyxiwv](CLAIM-tmpyxiwv.md).
- **Not that the spectrum is the same for every experiment.** The
  spectrum is that of one design ([TERM-tmp5z2du](../terms.d/TERM-tmp5z2du.md), condition 1); the
  record's cases spread only under coarse observation ([THEORY-774](../theory.d/THEORY-774.md),
  [THEORY-777](../theory.d/THEORY-777.md)).
- **Not that a fractal is the same thing.** A21 §5–6 likens the growth to
  "a fractal at increasing resolution" and reads box-counting dimension as
  bits gained per doubling of resolution (log₂ 3 ≈ 1.585 for the
  Sierpiński triangle, which the assistant confirmed). A gives no shared
  measure across the fractal, parameter and predictive settings, and its
  table of "complexity as a function of scale" is an analogy, not a
  result. Which of these dimensions agree is [QUESTION-tmpzlagu](../questions.d/QUESTION-tmpzlagu.md).

## Note of 2026-11-21: Transtrum et al. (2015), Transtrum, Machta & Sethna (2010, 2011) and Bialek, Nemenman & Tishby, read

- **The review** ([NOTE-tmphbpab](../notes.d/NOTE-tmphbpab.md)) supports the compression half: the
  hopping model's manifold is a "hyper-blob" after one step and "as time
  proceeds, the model manifold contracts onto a hyper-ribbon". It says
  nothing of resolved directions growing with data; its nearest remark is
  the EGFR figure's cut at eigenvalues below 1. It was in the grounds,
  unread; it carries less, and corroborates ([ARG-tmpu5yj6](../arguments.d/ARG-tmpu5yj6.md)).
- **The 2010 letter** ([NOTE-tmpamhd2](../notes.d/NOTE-tmpamhd2.md)) is a parallel: points added within the
  radius of convergence "supply little new information", each
  cross-section a constant factor thinner, a geometric fall, which on this
  claim's terms gives logarithmic growth.
- **The 2011 paper** ([NOTE-tmpzxtnv](../notes.d/NOTE-tmpzxtnv.md)) gives a count of the same kind in
  noise rather than n: the expected number of parameters not evaporated at
  a best fit grows as log(W₀/σ)/|log ∆| for widths W₀∆ⁿ (Eq. 37), and "the
  errors must be smaller than the narrowest width for there to be no
  evaporated parameters". Background.
- **Bialek, Nemenman and Tishby** ([NOTE-tmpilbkz](../notes.d/NOTE-tmpilbkz.md)) corroborate the power-law
  half: with K ∼ N^ν effective parameters each new sample carries
  ∼ N^(ν−1) bits (§4.5), and in their worked nonparametric case the
  predictive information is "directly proportional to the number of bins
  that can be put in the range of x", which grows as √N (§4.6). They warn
  that "If the number of parameters grows constantly, then the scenario
  where the data overwhelms all the unknowns is far from certain". Their
  count is through the density of divergences, not a Fisher threshold
  nλ ≳ 1.
