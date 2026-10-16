---
status: Proposed
promote_when: >-
  Two results. For the delay half: the same analysis with weak
  self-regulation, where interactions rather than growth rates set the
  leading eigenvalue, showing whether the critical delay still falls with
  diversity, and a stiff delay-equation solver showing whether the
  "divergent" phase past it is real. For the diversity half: community
  variability compared against a null of independent or phase-randomised
  species trajectories, with the number of realisations stated, showing
  whether it falls faster than the √S averaging such a null gives. If it
  does not, the "positive diversity–stability" result is statistical, not
  ecological. More runs at the one parameter setting cannot settle either
  half.
title: "A delay in the interactions of a large random Lotka–Volterra community whose undelayed equilibrium is feasible and globally stable destabilises it through a Hopf bifurcation at a critical delay set by the community spectrum, giving sustained oscillation with no external forcing; whether diversity then stabilises depends on the measure, since in the oscillating regime community-level variability falls with diversity while species-level variability rises"
version: 1
tags:
- ecology
- complex-systems
date: '2026-10-16'
source:
- LIT-057
summary: >-
  Saeedian et al. (2021), [LIT-057](../literature.d/LIT-057.md), a preprint, read in [NOTE-061](../notes.d/NOTE-061.md). The
  critical delay is the standard linear delay result applied to a random
  community matrix, and matched simulation at one parameter setting
  (strong self-regulation, d_B = 10, σ_B = 0.1, C = 1). It falls with
  diversity S, which [NOTE-061](../notes.d/NOTE-061.md) suggests may be an extreme-value effect of
  the growth rates rather than of interactions. The diversity result rests
  on two delays and S ≲ 70, with no test against the averaging null the
  paper itself cites.
---
<!-- inactive-ok-file: LIT-057 — Proposed; the preprint this account was read from, placed by its NOTE -->

# THEORY-tmpimkz9: A delay in the interactions of a large random Lotka–Volterra community whose undelayed equilibrium is feasible and globally stable destabilises it through a Hopf bifurcation at a critical delay set by the community spectrum, giving sustained oscillation with no external forcing; whether diversity then stabilises depends on the measure, since in the oscillating regime community-level variability falls with diversity while species-level variability rises

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

- **Non-reciprocal metabolic cycles ([THEORY-tmpsuuh4](THEORY-tmpsuuh4.md))** is the other case
  in this group where oscillation comes from the structure of an
  interaction matrix: a cycle's parity removes the real mode, as a delay
  here rotates a stable pair across the axis.
- **The BZ reaction ([THEORY-tmpe57v7](THEORY-tmpe57v7.md))** oscillates by a relaxation cycle
  in a chemical medium. Here the oscillation needs no autocatalysis, only
  a lag in the response.
