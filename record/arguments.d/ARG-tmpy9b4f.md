---
status: Proposed
title: "Bialek, Nemenman and Tishby ground the logarithmic case of the claim that the Fisher spectrum's shape fixes how predictive information grows, and its power-law case as to exponent only, as an instance of their annealed result; its exponential-spectrum case is not in their paper"
version: 1
form: evidence
grounds:
- THEORY-tmp3gj1j
concludes:
- CLAIM-tmpyxiwv
uses:
- TERM-tmpxml4k
tags:
- information-theory
- learning-theory
- mathematical-statistics
date: '2026-11-21'
line:
- formal-apparatus
- learned-structure
summary: >-
  What the reading of Bialek, Nemenman and Tishby (NOTE-tmpilbkz) carries
  for CLAIM-tmpyxiwv, which grounded on the unread LIT-tmpys7v3 for the
  attribution of the regimes. The logarithmic case is theirs (§4.1); the
  power-law case is an instance of their §4.5 annealed result as to
  exponent only, the annealed coefficient being too large by about 1 + 1/p;
  the exponential case is not in the paper. The claim's derivation stands
  on its own; the attribution in its title is narrowed in a dated note. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpyxiwv TERM-tmpxml4k THEORY-tmp3gj1j — Proposed or Rejected entries filed on 2026-11-21 from the exchange "Rich Get Richer Power Laws" and from the readings of its works, or Deferred works not yet read -->

# ARG-tmpy9b4f: Bialek, Nemenman and Tishby ground the logarithmic case of the claim that the Fisher spectrum's shape fixes how predictive information grows, and its power-law case as to exponent only, as an instance of their annealed result; its exponential-spectrum case is not in their paper

## The inference

CLAIM-tmpyxiwv derives, in a linear-Gaussian model with a shared
parameter, I_pred(T) = 2G(T) − G(2T), G(T) = ½ Σ ln(1 + Tλ_j), and from it three
growth laws, and says "the power-law regime of Bialek, Nemenman and Tishby
follows from a power-law spectrum". The paper (THEORY-tmp3gj1j) gives:

- §4.1, Eq. 41: linear regression with Gaussian noise, S₁(N) → (K/2) log₂ N,
  independent of the basis functions: the claim's first case, with the
  paper's infinite-future I_pred, which the claim's 2G(T) − G(2T) turns
  into (K/2) log(T/2), the same coefficient.
- §3: the data–parameter information equals I_pred with an infinite
  future: the claim's Step 1 in that form.
- §4.5: power law N^(μ/(μ+1)) from an essential singularity of ρ(D), in the
  annealed approximation, and heuristically from a parameter count growing
  as a power of N.

## Critical questions

- **Would the evidence be expected if the claim were false?** The
  logarithmic case, no: it is the same calculation. The power-law case:
  the paper's result is about a mechanism (an essential singularity), and
  the claim's model is a case of it only if its density of divergences has
  that form. The filer computed the paper's annealed quantity in the
  claim's model directly: S₁^(a) = G(N) + ½ Σ Nλ_j/(1 + Nλ_j), which for
  λ_j = j^(−p) grows as N^(1/p), the claim's exponent, with a coefficient
  larger than the exact G's by a factor tending to 1 + 1/p (1.501 at
  p = 2, 1.341 at p = 3, N = 10⁶; NOTE-tmpilbkz). So the claim's model is an
  instance of §4.5 as to exponent, and the paper's coefficients should not
  be cited for it.
- **Does it tell the claim apart from its rivals?** The rival origin of
  power-law growth is long memory with no parameter (TERM-tmpxml4k,
  condition 2; the paper's K* of Eq. 69). The paper itself says its
  measure "makes no distinction" between the two; the claim's "What it
  does not say" already grants this.
- **Does the measure measure what it is said to?** The paper's I_pred has
  an infinite future; the claim's a future of length T. For logarithmic
  growth the coefficient is the same; for power-law growth cT^μ the finite
  future multiplies it by 2 − 2^μ. The claim's computed coefficient is for
  its own convention.

The exponential case, (ln T)²/(4a), is not in the paper; it is the
claim's.

## Verdict

Grounds the logarithmic case and Step 1, and the power-law case as to
exponent; the "follows from" in the claim's title is the claim's own
mapping onto the paper's mechanism, exact in its model, and the paper had
no complete Bayesian family of power-law scalings to compare with (p. 32).
The THEORY replaces the unread LIT in the claim's grounds. Proposed.
