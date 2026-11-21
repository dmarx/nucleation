---
status: Proposed
title: "A rank power-law spectrum with exponent just above 1, as Stringer's smoothness bound α ≥ 1 + 2/m requires of a smooth code of an m-dimensional stimulus manifold, bounds the participation ratio as width grows, but the bound is approached only at widths exponential in m, so at realistic widths such a code has a participation ratio of about 13 to 29 for m from 10 to 100, and neither the participation ratio nor its growth with width tracks intrinsic dimension or separates the regimes either side of α = 1"
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the computation below: participation ratios of a pure rank
  power law with α = 1 + 2/m that at width 768 vary with m from 10 to 100
  by more than the stated range, or that approach their infinite-width
  limit at widths polynomial rather than exponential in m. Not met by real
  spectra that are not pure power laws, which the claim does not cover; a
  measured spectrum must be checked on its own terms.
tags:
- representation-learning
- mathematics
- neuroscience
date: '2026-11-21'
line:
- learned-structure
rests_on:
- CLAIM-tmpy688z
bears_on:
- QUESTION-tmpvu6cb
uses:
- TERM-tmplplcf
grounds:
- LIT-tmp7uzka
summary: >-
  Fills a gap the ledger of the exchange "Rich Get Richer Power Laws"
  flagged (A30 §5, answering the owner's U19): how the participation
  ratio behaves under λ_j ∝ j^(−α) on either side of α = 1 as width grows,
  where the power-law thread meets concentration. A30's regimes are right
  asymptotically, but near α = 1 they separate only at astronomical widths;
  with Stringer's smoothness bound, smooth codes of high-dimensional
  manifolds all show a participation ratio of a few tens at real widths.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpy688z TERM-tmplplcf CLAIM-tmpfwwfy LIT-tmp7uzka — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read -->

# CLAIM-tmpym2vz: A rank power-law spectrum with exponent just above 1, as Stringer's smoothness bound α ≥ 1 + 2/m requires of a smooth code of an m-dimensional stimulus manifold, bounds the participation ratio as width grows, but the bound is approached only at widths exponential in m, so at realistic widths such a code has a participation ratio of about 13 to 29 for m from 10 to 100, and neither the participation ratio nor its growth with width tracks intrinsic dimension or separates the regimes either side of α = 1

## The claim

**Which gap.** The ledger of the exchange asked how D_PR behaves under a
power-law spectrum on either side of α = 1 as width grows, since that is
where the exchange's power laws meet the owner's concentration of measure
(U19, [CLAIM-tmpfwwfy](CLAIM-tmpfwwfy.md)). A30 §5 answers it asymptotically ([CLAIM-tmpy688z](CLAIM-tmpy688z.md)). The answer at the
widths networks have is different in kind.

**The derivation.** With S_p(D) = Σ_(j≤D) j^(−p), D_PR = S_α(D)²/S_(2α)(D).
For α > 1, S_α(D) = ζ(α) − D^(1−α)/(α − 1) + O(D^(−α)), and (α − 1)ζ(α) → 1
as α ↓ 1, so the share of the limit reached is about

S_α(D)/ζ(α) ≈ 1 − D^(−(α−1)).

The sum S_(2α) has long converged (2α ≈ 2). So D_PR is within a fixed
fraction of its limit only once D^(α−1) is a fixed number, that is at
D ≈ e^(c/(α−1)): exponential in 1/(α − 1). Just above α = 1 the bounded regime
is real but unreachable, and just below it the D^(2(1−α)) growth is too slow
to see; both look like the (log D)² of α = 1.

**With Stringer's bound.** A29 §7 cites Stringer and colleagues
([LIT-tmp7uzka](../literature.d/LIT-tmp7uzka.md), Deferred: registered, not read) for a smoothness bound: a
differentiable code of an m-dimensional stimulus manifold has
α ≥ α_c = 1 + 2/m. At α = α_c, 1/(α − 1) = m/2, so the participation ratio is
bounded in width with limit ζ(1 + 2/m)²/ζ(2 + 4/m), but is approached only at
widths exponential in m. Computed in this session (python3 -I, scipy, with
Hurwitz zeta for the partial sums, checked against direct summation):

| m | α_c | limit of D_PR | D_PR at width 768 | share of limit | width for half the limit |
|---|---|---|---|---|---|
| 2 | 2.00 | 2.50 | 2.50 | 1.00 | under 2 |
| 5 | 1.40 | 7.73 | 6.89 | 0.89 | 12 |
| 10 | 1.20 | 22.6 | 13.2 | 0.58 | 264 |
| 20 | 1.10 | 75.2 | 19.9 | 0.26 | 1.2 × 10⁵ |
| 50 | 1.04 | 415 | 26.1 | 0.06 | 1.2 × 10¹³ |
| 100 | 1.02 | 1,590 | 28.8 | 0.02 | 2.6 × 10²⁶ |

Three consequences:

1. **The participation ratio does not track intrinsic dimension.** At width
   768, codes at Stringer's bound for manifolds of intrinsic dimension 10 to
   100 have D_PR between 13 and 29; from m = 20 to m = 100 it moves from 20 to
   29. Reading D_PR as an estimate of m ([TERM-tmplplcf](../terms.d/TERM-tmplplcf.md)) fails for m above about 10.
2. **Width does not sharpen the shell much.** For such codes the relative
   spread of the squared norm, √(2/D_PR) ([CLAIM-tmpy688z](CLAIM-tmpy688z.md)), stays near 0.26 to 0.39 at
   width 768 and falls only logarithmically with width, against 1/√D for an
   isotropic code. Smooth high-dimensional codes are far from the thin
   annulus however wide the layer.
3. **The regime is not identifiable from width scaling.** Between widths
   10⁴ and 10⁶ the local slope d ln D_PR/d ln D is 0.29 at α = 0.9 (asymptote
   0.2), 0.17 at α = 1 (asymptote 0) and 0.09 at α = 1.1 (asymptote 0).
   Fitting D_PR against width cannot place α either side of 1; the
   spectrum's exponent has to be fitted directly.

So the exchange's bridge holds in a narrower form: a power-law spectrum
governs concentration, but near α = 1 it does so through slowly varying,
nearly m-independent participation ratios of a few tens, not through
distinct regimes a network of real width could exhibit.

## What it does not say

- Not that measured representations sit at α_c. Stringer's bound is a lower
  bound on α for smooth codes; a steeper spectrum saturates sooner.
- Not anything about non-Gaussian norms or spectra that are not pure power
  laws, for which D_PR must be computed from the measured eigenvalues.
- That Stringer's bound is as A29 states it is unverified here: the work is
  registered and not read.
