---
status: Proposed
promote_when: >-
  The proofs the survey cites are read and confirm its statements: the
  Wentzell–Freidlin exit-time theorem fixing only the exponential order of
  the mean exit time; the first full proof of the Eyring–Kramers prefactor
  by potential theory (Bovier, Eckhoff, Gayrard and Klein 2004); the
  failure of that prefactor at degenerate saddles; and the absence of a
  limiting prefactor for irreversible dynamics (cycling).
title: 'Berglund holds that large-deviation theory fixes only the exponential order of the mean time for a small-noise diffusion to leave a potential well, while the Eyring–Kramers prefactor needs other methods, fails at degenerate saddles, and can fail to have a limit for irreversible dynamics'
version: 1
tags:
- mathematics
- probabilistic-modeling
- complex-systems
date: '2026-11-04'
source:
- LIT-tmp76lym
summary: >-
  Berglund (2011), LIT-tmp76lym, read in NOTE-tmpke9h3, a review
  registered as a stand-in for Freidlin and Wentzell (LIT-tmp6rglf).
  Proposed: the survey sketches and cites the proofs rather than giving
  them. It does not say the prefactor is unknowable for non-gradient
  systems in general, only that large deviations do not deliver it and
  that in the cycling case it has no limit.
---
<!-- inactive-ok-file: NOTE-tmp4cwdr — Skimmed and new; the front-matter reading of the book this survey stands in for, cited as open -->

# THEORY-tmp2rxfm: Berglund holds that large-deviation theory fixes only the exponential order of the mean time for a small-noise diffusion to leave a potential well, while the Eyring–Kramers prefactor needs other methods, fails at degenerate saddles, and can fail to have a limit for irreversible dynamics

## Source

Berglund, "Kramers' law: Validity, derivations and generalisations"
(arXiv 2011; Markov Processes Relat. Fields 2013), LIT-tmp76lym; read in
NOTE-tmpke9h3. The book it stands in for, LIT-tmp6rglf, was read only in
its front matter (NOTE-tmp4cwdr).

## What was actually shown

- **The exponent (Theorem 2.2, credited to Wentzell and Freidlin).**
  lim 2ε log E τ = inf over ∂D of the quasi-potential, which in the
  gradient case is twice the barrier height (eqs. 2.11–2.13). It holds
  "only true in the sense of logarithmic equivalence (2.5)."
- **Not the prefactor (§1; Remark 2.5).** The approach proves Arrhenius'
  law "for more general than gradient systems, but fails to control the
  prefactor."; "However, to our knowledge a rigorous computation of the
  prefactor by this" approach has not been achieved.
- **Other methods (§1, §3).** The Eyring–Kramers formula had "a full proof
  of (1.9) having been obtained only in" 2004, by potential theory and
  capacities (Theorem 3.3); the Witten Laplacian gives the full expansion.
- **Degenerate saddles (§4.1).** "Kramers’ law (1.9) cannot be true in the
  presence of" singular Hessians; at a pitchfork the prefactor scales as
  ε^{1/4}.
- **Irreversible dynamics (§4.3).** "In general, the answer is negative."
  The prefactor "need not even converge to a limiting value as ε → 0."
  (cycling, Theorem 4.3).

## What this does not say

- That the exponent is wrong anywhere: Arrhenius' law survives in every
  case the survey treats, including the irreversible one.
- That every non-gradient system lacks a limiting prefactor; the
  survey's negative case is the cycling one.
- Anything checked here against the cited proofs, which were not read.
