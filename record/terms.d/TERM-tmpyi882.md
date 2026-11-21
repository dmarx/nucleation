---
status: Proposed
title: 'scale-free, said of an observable: a heavy-tailed marginal, a scale-covariant law of correlation or dynamics, or a power-law spectrum'
version: 1
tags:
- complex-systems
- mathematics
- natural-sciences
date: '2026-11-21'
line:
- formal-apparatus
complements:
- TERM-tmpt3vht
summary: >-
  Three things the exchange "Rich Get Richer Power Laws" calls scale-free,
  kept apart: a one-point distribution whose tail is a power law, a law of
  correlation, geometry or dynamics that is unchanged by a change of scale
  up to a rescaling (self-similarity proper), and a power spectrum. For a
  stationary field the third is the second stated in Fourier coordinates;
  otherwise none implies another (CLAIM-tmpwl8y8). Fills the gap the ledgers
  name, that the record had no word separating these, and answers the
  self-similarity half of the owner's U4. The distinctions are A's, spread
  over A6 §6, A10 §1–2, A23 §2, A24 §3, A26 §9 and A27 §9; the definition,
  the Fourier relation and the stated regularity condition are the
  assistant's. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpwl8y8 CLAIM-tmpsr8r4 CLAIM-tmpyy261 CLAIM-tmpbe2gh — filed with this term on 2026-11-21, Proposed -->
<!-- inactive-ok-file: THEORY-803 — Proposed; the record's one reading of statistical self-similarity, named as an instance -->

# TERM-tmpyi882: scale-free, said of an observable: a heavy-tailed marginal, a scale-covariant law of correlation or dynamics, or a power-law spectrum

## Definition

An observable is **scale-free** over a stated range x_min ≪ x ≪ x_c
(no physical system has more; A10 §7) in one of three senses. Which one
is meant must be said, because they come apart.

1. **Heavy-tailed marginal** (distributional). A one-point law, of an
   event size, a degree, a wealth, has a regularly varying tail:
   P(X > x) = x^(−α) L(x) with L slowly varying, so that
   P(X > bx | X > x) → b^(−α) whatever x is (A8 §4, A10 §7). This is the
   sense the exchange opened with (A1), and the sense of "scale-free
   network". It says how often large values occur and nothing about how
   values at different places, times or scales are related.
2. **Scale-covariant law** (self-similarity proper). A law relating
   values across positions, times or resolutions is unchanged by x → bx up
   to a rescaling of the observable: a correlation function
   C(br) = b^(−a) C(r); the law of a process, B(at) =d a^H B(t) (A10 §6);
   a geometric measure M(br) = b^D M(r), the fractal case (A10 §3); a
   dynamic law C(br, b^z t) = b^(−2Δ) C(r, t), in which space and time
   rescale together (A24 §6); or a family of moments whose exponents ζ(q)
   are nonlinear in q, the multifractal case (A23 §4–5). A23 §4's binomial
   cascade with p = 0.8 has local exponents from α_min = −log₂ 0.8 = 0.322
   to α_max = −log₂ 0.2 = 2.322, and τ(q) = −log₂(p^q + (1 − p)^q) is
   linear, q − 1, only at p = ½ (checked). A6 §6's
   "geometric" and "statistical" self-similarity are this sense, and its
   "distributional scale invariance" is sense 1.
3. **Power-law spectrum**. Power per unit frequency or wavenumber falls as
   S(f) ∝ f^(−β), so with β = 1 every octave carries the same power,
   ∫_f^2f C/u du = C ln 2 (A10 §4). A spectrum says how variance is shared
   among scales; it is not the distribution of event sizes (A23 §2).

## How the senses are related

- **Sense 3 is sense 2 for the two-point function, when the field is
  stationary.** The power spectrum is the Fourier transform of the
  two-point correlation, so C(r) ∝ r^(−a) with 0 < a < d corresponds to
  S(k) ∝ k^(a−d). The Gaussian field of CLAIM-tmpwl8y8 has S(k) ∝ k^(−2)
  and C(r) ∝ 1/r in d = 3. Treating a power-law spectrum and power-law
  correlations as two findings about one stationary signal double-counts
  one fact. The spectrum says nothing about higher-order statistics, which
  is where multifractality (A23 §5) and flux (CLAIM-tmpbe2gh) live.
- **Neither sense 2 nor sense 3 implies sense 1, and sense 1 implies
  neither.** A Gaussian field can have power-law correlations and
  Gaussian values; independent Pareto draws have a power-law tail and no
  correlations at all, so a flat spectrum (CLAIM-tmpwl8y8, checked there).
- **The power law is the form of exact scale covariance.** If a positive
  measurable f satisfies f(bx) = g(b) f(x) for every b, x > 0, then
  g(ab) = g(a) g(b), a measurable multiplicative function, so g(b) = b^(−α)
  and f(x) = f(1) x^(−α). Measurability, or monotonicity, is the "mild
  regularity" A10 §1 leaves unstated; without it the Cauchy equation has
  pathological solutions. Regular variation (A10 §7) is the asymptotic
  version, which is why sense 1 is stated with L(x).
- **Geometry and distribution can be one organization measured twice**,
  as A10 §3 says of critical percolation, but the link is a scaling
  relation, not an identity. For percolation clusters the size exponent
  and the fractal dimension satisfy τ = 1 + d/D_f. With the exact 2D value
  D_f = 91/48 this gives τ = 1 + 96/91 = 187/91, the value A5 quotes
  (checked in exact fractions, `python3 -I`). A10 does not give the
  relation; it is the step its "two measurements of the same underlying
  scale-invariant organization" needs.
- **A rank spectrum is a fourth object.** The eigenvalues of a covariance
  matrix ordered by rank, λ_j ∝ j^(−α), are a power-law spectrum in sense 3
  only when the eigenbasis is the Fourier basis, that is, for a stationary
  field. Otherwise a power-law rank spectrum is not a statement about
  scales in space or time.

## What it is not

- **Not "critical".** Each sense can hold far from any tuned transition
  (CLAIM-tmpsr8r4). Criticality is one mechanism for sense 2.
- **Not "heavy-tailed" by default.** The exchange slides between "power
  law", "scale-free" and "heavy tail" from A1 to A10; A27 §9 is where it
  separates them: "Are unusually large outcomes disproportionately
  common?" against "Are fluctuations at widely different spatial or
  temporal scales related by the same mathematical law?"
- **Not one relation to chaos.** The owner's U4 heard self-similarity in
  scale-free behaviour. That hearing is right for sense 2 and does not
  follow for sense 1; how either bears on chaos is CLAIM-tmpyy261's
  question (QUESTION-tmpyqohh).
- **Not the record's earlier usage.** THEORY-803 (statistical
  self-similarity of networks under geometric renormalization) is sense 2
  applied to a network's degree law and clustering; "scale-free
  hierarchical multi-index target" in QUESTION-158 names weights a_k across
  a target's directions, a rank-spectrum usage.
