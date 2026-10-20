---
number: 548
status: Active
formerly:
- THEORY-tmpimkz9
title: 'In generalised Lotka–Volterra dynamics with every interaction delayed by τ, a feasible equilibrium that is stable without delay loses stability at τ_c = min over the community eigenvalues j of arctan(|Re j|/|Im j|)/|j|, where a pair of roots crosses the imaginary axis transversally (a Hopf point), so the critical delay is set by the community spectrum; in Saeedian et al.''s strongly self-regulated setting the oscillating regime''s community-level variability falls with diversity (S = 10–70) while species-level variability rises, and the fall matches what summing independently oscillating species gives'
version: 2
history:
- version: 2
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-548 (batch 055). The delay half is re-derived (ADR-047 v2): the
    critical-delay formula with the arctan branch fixed, and transversal
    crossing. The diversity half was re-run at the paper's setting with 20
    realisations per point against a null of independently time-shifted
    species (ADR-047 v3); the pattern reproduces and matches the null, which
    the title now says. "Globally stable" and "sustained oscillation" in
    general leave the title. The weak-self-regulation, supercriticality and
    divergence requests move to QUESTION-tmpq1dzv.
tags:
- ecology
- complex-systems
date: '2026-10-16'
source:
- LIT-057
summary: >-
  Saeedian et al. (2021), [LIT-057](../literature.d/LIT-057.md), a preprint, read in [NOTE-061](../notes.d/NOTE-061.md). The
  critical delay is the linear delay result on the community matrix,
  re-derived on promotion (2026-10-20), and matched simulation at one
  strongly self-regulated setting. The variability result was re-run on
  promotion against an averaging null and matches it: the fall of
  community-level variability with diversity is what summing independent
  oscillators gives, not an ecological stabilisation.
---
<!-- inactive-ok-file: LIT-057 — Proposed; the preprint this account was read from, placed by its NOTE -->

# THEORY-548: In generalised Lotka–Volterra dynamics with every interaction delayed by τ, a feasible equilibrium that is stable without delay loses stability at τ_c = min over the community eigenvalues j of arctan(|Re j|/|Im j|)/|j|, where a pair of roots crosses the imaginary axis transversally (a Hopf point), so the critical delay is set by the community spectrum; in Saeedian et al.'s strongly self-regulated setting the oscillating regime's community-level variability falls with diversity (S = 10–70) while species-level variability rises, and the fall matches what summing independently oscillating species gives

## Source

Saeedian, Pigani, Maritan, Suweis & Azaele (2021), [LIT-057](../literature.d/LIT-057.md), the arXiv
preprint, read in full in [NOTE-061](../notes.d/NOTE-061.md). The published version in *Phil. Trans.
R. Soc. A* 380(2227) was not read, and its abstract is reworded.

## What was actually shown

**The setting.** Generalised Lotka–Volterra dynamics with delayed
interactions only (A = 0, Eq. 12). Off-diagonal entries are Normal(0, σ_B)
with connectance C, the diagonal is −d_B, and growth rates are
U[0.05, 0.1]. Every delay figure uses d_B = 10, σ_B = 0.1, C = 1. Runs
start in the coexistence region, where the undelayed equilibrium is
feasible and globally stable (Appendix A).

**The critical delay (Eq. 14, Appendix C).** Each community eigenvalue j
gives λ = j e^{−λτ}. The equilibrium loses stability at τ_c, the minimum
over the spectrum, by a Hopf bifurcation. At S = 100 the community is
stable at τ = 12, oscillates at τ = 18 and diverges numerically at τ = 28
(Figs. 2–4). τ_c and the divergence threshold both fall with S (Fig. 5b).
Below τ_c, resilience falls as τ grows.

**Variability (Eq. 15, Fig. 6).** At τ = 20 and 22, the coefficient of
variation of total abundance, CV_c, falls with S over about S = 10–70,
while the species-averaged CV_s rises. In the stable phase both are zero
by construction.

**What could have come out otherwise.** The simulated onset could have
missed the analytic τ_c. It matched, at the one setting.

## What this does not say

- **That interaction complexity sets τ_c.** In this strongly self-regulated
  regime the community eigenvalues are about −r_i, so τ_c ≈ π/(2 max r_i),
  about 16 for r ≤ 0.1, which brackets the observed onset between 12 and
  18. The fall with S may then be the largest growth rate rising with the
  number drawn. That is [NOTE-061](../notes.d/NOTE-061.md)'s inference, unverified, and the paper
  calls the trend consistent with May.
- **That diversity stabilises the community.** Summing S weakly correlated
  oscillators lowers CV_c roughly as 1/√S for statistical reasons. The
  paper cites Tilman et al. (1998) on exactly this null and does not test
  against it. Realisations and error bars for Fig. 6 are not stated.
- **That the oscillations stay bounded.** The divergence past τ_c^C
  persisted when the Euler step was refined. The Conclusion mentions
  "analytical insights" on boundedness that the paper does not contain,
  and the Introduction says it does not prove boundedness.
- **Anything with both instantaneous and delayed interactions.** No result
  combines them.
- **The arctan branch.** Eq. 14 leaves it unstated; for a nearly real
  eigenvalue it must be read so as to give the classical π/(2|α|).

## Connections

- **Non-reciprocal metabolic cycles ([THEORY-634](THEORY-634.md))** is the other case
  in this group where oscillation comes from the structure of an
  interaction matrix: a cycle's parity removes the real mode, as a delay
  here rotates a stable pair across the axis.
- **The BZ reaction ([THEORY-508](THEORY-508.md))** oscillates by a relaxation cycle
  in a chemical medium. Here the oscillation needs no autocatalysis, only
  a lag in the response.

## Note of 2026-10-20: the derivation, and a re-run against the null

**The critical delay.** With every interaction delayed, the bracket of
Eq. 12 vanishes at x* = −B⁻¹r, so δx′(t) = J δx(t − τ) with J = diag(x*)B,
and on each eigenvector λ = j e^{−λτ}. A root λ = iω needs ω = |j| and
i e^{iωτ} = j/|j|, so τ_j = (arg j − π/2)/|j| = arctan(|Re j|/|Im j|)/|j|
for Re j < 0, which is π/(2|j|) for real j and fixes the branch Eq. 14
leaves open. At τ = 0 all roots are the j; new roots of a retarded equation
enter from Re λ = −∞; so stability is first lost at τ_c = min_j τ_j. From
λ − j e^{−λτ} = 0, dλ/dτ = −λ²/(1 + λτ), and at λ = iω its real part is
ω²/(1 + ω²τ²) > 0, so the pair crosses transversally. Supercriticality is
not derived.

**The re-run.** The paper's setting (d_B = 10, σ_B = 0.1, C = 1,
r ~ U[0.05, 0.1], feasible draws only), Euler with dt = 0.05 to t = 4000,
the first 2000 discarded, S = 10, 20, …, 70, τ = 20 and 22, 20 realisations
per point. The null shifts each species' series by an independent random
circular lag and sums them.

| S | CV_c (τ=20) | CV_c/null | CV_s | CV_c (τ=22) | CV_c/null | CV_s |
|---|---|---|---|---|---|---|
| 10 | 0.174 | 0.98 | 0.39 | 0.243 | 1.02 | 0.55 |
| 30 | 0.097 | 0.82 | 0.46 | 0.136 | 0.94 | 0.63 |
| 50 | 0.082 | 0.89 | 0.48 | 0.109 | 0.93 | 0.65 |
| 70 | 0.072 | 0.87 | 0.52 | 0.103 | 0.98 | 0.70 |

Every ratio is within one standard deviation (about 0.2) of 1, and
CV_c√S stays near 0.55–0.60. Onset matched τ_c (S = 50: flat at τ = 12,
CV_c 4·10⁻⁴ at 15 against τ_c,min = 15.1, 0.055 at 18), and dt = 0.02
moved CV_c by 3%. One aside: τ_c is not the growth-rate bound π/(2 max r)
[NOTE-061](../notes.d/NOTE-061.md) suggested; from S = 40 its correlation with that bound is about
0.2, and it falls below it (13.1 against 15.8 at S = 200), so at larger S
the interactions set it.
