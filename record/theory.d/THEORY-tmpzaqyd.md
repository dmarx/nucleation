---
status: Active
title: "Under multiplicative noise, members that pool their resources and split them equally every step each grow faster in the long run than they would alone, with no complementarity, relatedness or reciprocity: N independent geometric Brownian motions that share keep their drift μ and cut their volatility to σ/√N, raising each one's time-average growth rate from μ − σ²/2 to μ − σ²/(2N); the gain vanishes as their noise becomes perfectly correlated, and a sufficiently superior member does better alone"
version: 1
tags:
- complex-systems
- probabilistic-modeling
date: '2026-10-16'
source:
- LIT-035
summary: >-
  Peters & Adamou (2022), [LIT-035](../literature.d/LIT-035.md), read in [NOTE-059](../notes.d/NOTE-059.md). The mathematics is
  correct and self-contained, and the paper's own citations show the
  pooled-variance result was known (McCloskey, Winterhalder, Uitdehaag,
  Kennedy et al.). Sharing leaves the ensemble rate μ unchanged, so an
  analysis built on expectations sees no reason to share, and the time
  average does. It holds with zero cost, perfect pooling, unbreakable
  pacts and unconstrained growth. It is a sufficient mechanism in that
  model, not a solution of the cooperation puzzle, and not a showing that
  cooperation is the default.
---
<!-- inactive-ok-file: THEORY-141 THEORY-tmp8vbpr — Proposed; accounts of cooperation named for contrast, nothing here rests on their being settled -->

# THEORY-tmpzaqyd: Under multiplicative noise, members that pool their resources and split them equally every step each grow faster in the long run than they would alone, with no complementarity, relatedness or reciprocity: N independent geometric Brownian motions that share keep their drift μ and cut their volatility to σ/√N, raising each one's time-average growth rate from μ − σ²/2 to μ − σ²/(2N); the gain vanishes as their noise becomes perfectly correlated, and a sufficiently superior member does better alone

## Source

Peters & Adamou (2022), [LIT-035](../literature.d/LIT-035.md), "The ergodicity solution of the
cooperation puzzle", *Phil. Trans. R. Soc. A* 380(2227), read in full in
[NOTE-059](../notes.d/NOTE-059.md).

## What was actually shown

**The drag (§2).** A geometric Brownian motion dx = x(μ dt + σ dW) has
ensemble growth rate μ (Eq. 2.7), but a single trajectory grows at
μ − σ²/2 almost surely (Eq. 2.8). Fluctuations cost growth.

**Pooling (§§3–4).** N members grow, pool and split equally each step.
The shared process is again a GBM with the same drift and volatility
σ/√N (Eq. 3.9). Each member's time-average rate is μ − σ²/(2N) (Eq. 4.1),
a premium of (σ²/2)(1 − 1/N) (Eq. 4.2) that is largest per added member
at small N and tends to μ as N → ∞. Members out-grow even the arithmetic
mean of the same number of non-sharers (Fig. 2; μ = 0.15, σ² = 0.2,
giving 0.05 for a loner and 0.10 for a pair member by [NOTE-059](../notes.d/NOTE-059.md)'s
arithmetic).

**Correlation (§5b).** With equal pairwise correlation ρ, the effective
volatility is σ√((1 + (N−1)ρ)/N) (Eq. 5.12). There is a benefit iff ρ < 1,
and with many members it caps at μ − σ²ρ/2 (Eq. 5.13). Perfect
anticorrelation is possible only for N = 2, which gives the full rate μ.

**Unequal members (§5a).** The cooperative's rate is (1/N)Σ(μ_i −
σ_i²/(2N)) (Eq. 5.5). Member j gains by joining iff that exceeds μ_j −
σ_j²/2 (Eq. 5.6), and the group gains by admitting j iff it exceeds the
(N−1)-member rate (Eq. 5.7). A member skilled enough does better alone.

**What could have come out otherwise.** Nothing, given the model: it is a
derivation. What could fail is the model's fit to any system.

## What this does not say

- **That this solves the cooperation puzzle.** The puzzle is why
  cooperators are not exploited. Defection, walk-away and invasion are set
  aside (§4a), and the "ignore-for-tat" remedy is sketched with no
  stability analysis.
- **That cooperation is the behavioural default.** That follows only with
  zero sharing cost, perfect continuous pooling, no defection and
  unconstrained growth. The authors grant that coordination costs "may …
  make cooperation disadvantageous" (§3), and no cost is analysed.
- **That it is new.** The paper itself says McCloskey and Winterhalder
  obtain "the same expression for the variance", and that Kennedy et al.
  treat it as a special case. The novelty is the time-average framing.
- **That it explains the move to multicellularity.** That is a suggestion
  with no model (§1, §6).
- **That growth-limited populations behave the same.** GBM is unconstrained
  self-reproduction, and the authors say resource-limited growth "would be
  poorly described" by it (§2).

## Connections

- **Morality as cooperation ([THEORY-tmp8vbpr](THEORY-tmp8vbpr.md))** and **Nowak's five
  mechanisms ([THEORY-tmpkifk7](THEORY-tmpkifk7.md))** explain cooperation by the structure of
  the game: kinship, reciprocity, partner choice. This needs none of them.
  The two are not rivals: variance pooling is a payoff to sharing, and
  those mechanisms are about keeping sharers from being exploited, which
  this model assumes away.
- **Major transitions ([THEORY-141](THEORY-141.md)).** The paper's unicellular-to-multicellular
  remark points at the stability of collectives. It supplies a reason
  collectives would pay, not the policing or alignment that [THEORY-141](THEORY-141.md)
  holds they need.
