---
number: 848
status: Proposed
formerly:
- CLAIM-tmpym2vz
title: 'Participation ratio misses intrinsic dimension'
statement: >-
  A rank power-law spectrum with exponent just above 1, at the limit that
  Stringer's smoothness bound, α > 1 + 2/m on the tail of a smooth code of
  an m-dimensional stimulus manifold, allows, bounds the participation ratio
  as width grows, but the bound is approached only at widths exponential in
  m, so at realistic widths such a code has a participation ratio of about
  13 to 29 for m from 10 to 100, and neither the participation ratio nor its
  growth with width tracks intrinsic dimension or separates the regimes
  either side of α = 1
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the reading of LIT-2972 (NOTE-2257, THEORY-2174). Corrected
    in place: Stringer's bound is strict for smooth codes (λ_n =
    o(n^(−1−2/d)), Supplementary Theorem 5), so a spectrum exactly at
    α = 1 + 2/m is the limit of smooth codes, not a smooth code; and it
    constrains only the tail, so the table is for pure power laws from rank
    1, not every code the bound allows. Title and the derivation's
    paragraph changed to say so; the table's numbers rechecked and
    unchanged; LIT-2972 replaced in the grounds by its reading
    (ARG-169). The status is unchanged.
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
- CLAIM-847
bears_on:
- QUESTION-515
uses:
- TERM-136
grounds:
- THEORY-2174
summary: >-
  Fills a gap the ledger of the exchange "Rich Get Richer Power Laws"
  flagged (A30 §5, answering the owner's U19): how the participation
  ratio behaves under λ_j ∝ j^(−α) on either side of α = 1 as width grows,
  where the power-law thread meets concentration. A30's regimes are right
  asymptotically, but near α = 1 they separate only at astronomical widths;
  pure power laws at the limit of Stringer's smoothness bound, which is
  strict and on the tail only ([ARG-169](../arguments.d/ARG-169.md)), show for high-dimensional
  manifolds a participation ratio of a few tens at real widths.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CLAIM-847 TERM-136 CLAIM-822 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2174 ARG-169 — Proposed or new; the reading of Stringer and colleagues and the argument for its support, 2026-11-22 -->
<!-- inactive-ok-file: ARG-130 — new and Proposed or Rejected, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2189 — Proposed, Deferred or new; the readings of 2026-11-22 (Wang, Wu and Fan; Yang, Steinhardt and Hu; Ansuini and colleagues; Cai and colleagues; Martínez-Sánchez and colleagues), their arguments, and the entries they bear on -->

# CLAIM-848: Participation ratio misses intrinsic dimension

## The claim

**Which gap.** The ledger of the exchange asked how D_PR behaves under a
power-law spectrum on either side of α = 1 as width grows, since that is
where the exchange's power laws meet the owner's concentration of measure
(U19, [CLAIM-822](CLAIM-822.md)). A30 §5 answers it asymptotically ([CLAIM-847](CLAIM-847.md)). The answer at the
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
([LIT-2972](../literature.d/LIT-2972.md), read 2026-11-22 as [THEORY-2174](../theory.d/THEORY-2174.md)) for a smoothness bound. As
the supplement proves it (Theorem 5), a code with finite expected
derivative on an m-dimensional stimulus manifold has eigenvalues
λ_n = o(n^(−1−2/m)): strictly, and only in the tail. A pure power law at
α_c = 1 + 2/m is therefore the limit of smooth codes, not a smooth code
(the border case of the supplement's Example 2), and a smooth code may
have any head. The table below is for that limiting case, a pure power law
from rank 1; codes strictly inside the bound have smaller ratios (at
α_c + 0.05 and width 768: 11.0, 16.0 and 22.7 for m = 10, 20 and 100). At
α = α_c, 1/(α − 1) = m/2, so the participation ratio is
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
   768, codes at the limit of Stringer's bound for manifolds of intrinsic dimension 10 to
   100 have D_PR between 13 and 29; from m = 20 to m = 100 it moves from 20 to
   29. Reading D_PR as an estimate of m ([TERM-136](../terms.d/TERM-136.md)) fails for m above about 10.
2. **Width does not sharpen the shell much.** For such codes the relative
   spread of the squared norm, √(2/D_PR) ([CLAIM-847](CLAIM-847.md)), stays near 0.26 to 0.39 at
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
distinct regimes a network of real width could exhibit. [ARG-130](../arguments.d/ARG-130.md) sets
out how this qualifies [CLAIM-847](CLAIM-847.md).

## What it does not say

- Not that measured representations sit at α_c. Stringer's bound is a lower
  bound on α for smooth codes; a steeper spectrum saturates sooner.
- Not anything about non-Gaussian norms or spectra that are not pure power
  laws, for which D_PR must be computed from the measured eigenvalues.
- Not that the bound fixes D_PR. It constrains the tail only: with the
  tail at α_c and the top ten eigenvalues set equal to the tenth, the ratio
  at width 768 is 89, 112 and 137 for m = 10, 20 and 100; with the top
  eigenvalue ten times larger it is 1.8 to 2.5 (`python3 -I`,
  [ARG-169](../arguments.d/ARG-169.md)).

*Changed 2026-11-22, version 2:* the bound is stated as the reading gives
it, strict and on the tail; the sentence that called it unverified is
replaced by the reading; [LIT-2972](../literature.d/LIT-2972.md) leaves the grounds for [THEORY-2174](../theory.d/THEORY-2174.md).

## Note of 2026-11-22: Stringer and colleagues, read

Stringer and colleagues ([LIT-2972](../literature.d/LIT-2972.md)) were read ([NOTE-2257](../notes.d/NOTE-2257.md); the reading
is [THEORY-2174](../theory.d/THEORY-2174.md)). The reading **supports the premise in corrected
form** ([ARG-169](../arguments.d/ARG-169.md)):

- **Strict.** Supplementary Theorem 5: "If the expected derivative
  magnitude of φ is finite ... then λn = o(n−1−2/d)". "α ≥" is the
  weaker fractal bound of Theorem 4 in its limit. The table's row for each
  m is the limit of smooth codes.
- **Tail only.** The theorems hold as n → ∞ in an infinite-neuron limit,
  and Stringer's own fit skips ranks 1 to 10.
- **Rechecked** with `python3 -I` (direct sums against Hurwitz-zeta partial
  sums): every entry of the table reproduces (19.85 at m = 20 rounds to
  19.9). Stringer's measured exponents give D_PR at width 768 of 26.1
  (α = 1.04), 5.5 (1.49), 4.0 (1.65) and 1.3 (3.43).
- **Scope.** The arguments "apply only when the number of neurons in the
  population is substantially greater than the manifold dimension of the
  stimulus set" (SI §3.5); about 10m neurons on Stringer's heuristic, so
  the m = 100 row lies at the edge of where the bound is claimed.
- SI §3.5 makes this claim's point about the trace itself: "we observe a
  rapid increase in total variance when α becomes close to 1", a
  discontinuous "phase transition" only as N → ∞. This claim extends it
  from tr Σ to D_PR.

## Note of 2026-11-22: Ansuini and colleagues, read

Ansuini, Laio, Macke and Zoccolan ([LIT-2998](../literature.d/LIT-2998.md), [NOTE-2278](../notes.d/NOTE-2278.md), [THEORY-2189](../theory.d/THEORY-2189.md)): **a parallel;
supports the claim's last clause and runs the other way.** This claim has
the participation ratio failing to track intrinsic dimension from below:
smooth codes of m = 20 to 100 all give D_PR near 20 to 29 at width 768.
Ansuini and colleagues find the same decoupling in trained CNNs from above:
a 90%-variance PCA count "≈ 200" against a TwoNN intrinsic dimension near
18 in VGG-16's last hidden layer, and a linear count that does not tell
trained from random networks apart. So a linear count can sit above m
(curved low-dimensional manifolds) or below it (smooth high-m codes). The
paper computes no participation ratio, so it neither tests this claim's
numbers nor contradicts them. A parallel, so no relation.
