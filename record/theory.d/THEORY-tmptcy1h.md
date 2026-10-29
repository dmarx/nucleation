---
status: Active
title: 'Between two weighted directed networks with node measures, the Gromov–Wasserstein distance is bounded below by a hierarchy of invariants, each in an in-going and an out-going version, and the strongest of them, a transport problem whose costs are themselves transport problems, equals a transport problem whose costs are one-dimensional Wasserstein distances between the nodes'' weight profiles, so it is computed in closed form; the bounds are one-sided, and two networks can agree on all of them while being at positive distance'
version: 1
tags:
- network-science
- mathematics
date: '2026-10-29'
source:
- LIT-tmpu05fk
summary: >-
  Chowdhury and Mémoli (2019), LIT-tmpu05fk, Theorem 24 and Lemma 28 (pp.
  11–13), read in NOTE-tmp72o0n. Proved; the equalities were already known
  for discrete spaces from Schmitzer and Schnörr 2013, as the paper says.
  TLB = R-TLB and the order of the bounds were checked numerically on 25
  random asymmetric pairs. Active. The edge the paper leaves implicit: a
  zero lower bound is no evidence of sameness. A 3-node pair with every
  bound zero is at dN,2 ≥ 0.215 (the record's construction).
---

# THEORY-tmptcy1h: Between two weighted directed networks with node measures, the Gromov–Wasserstein distance is bounded below by a hierarchy of invariants, each in an in-going and an out-going version, and the strongest of them, a transport problem whose costs are themselves transport problems, equals a transport problem whose costs are one-dimensional Wasserstein distances between the nodes' weight profiles, so it is computed in closed form; the bounds are one-sided, and two networks can agree on all of them while being at positive distance

## Source

Chowdhury and Mémoli (2019), LIT-tmpu05fk, §3.1, pp. 10–13 of arXiv
1808.04337v2; read in NOTE-tmp72o0n.

## What was actually shown

**Theorem 24 (p. 12).** For measure networks X, Y and p ∈ [1, ∞], with
C(x, y) = Wp(ωX(x, ·)∗µX, ωY(y, ·)∗µY):

- 2dN,p ≥ TLB, the infimum over couplings of the Lp norm of the joint
  eccentricity, itself an infimum over couplings for each pair (x, y)
  (eq. JE, p. 11);
- TLB = R-TLB, the transport problem with cost C;
- R-TLB ≥ FLB = R-FLB, the Wasserstein distance between the distributions
  of the nodes' out-going Lp norms;
- FLB ≥ |sizep(X) − sizep(Y)|;
- separately, 2dN,p ≥ SLB = R-SLB, the Wasserstein distance between the
  distributions of all edge weights.

Each holds for the in-going profiles ωX(·, x) too (p. 12). The equalities
rest on Lemma 28 (p. 13): for measurable f, g into ℝ, the pushforward of the
set of couplings of µX and µY is exactly the set of couplings of f∗µX and
g∗µY. The proof uses analytic sets and a lemma of Varadarajan to lift any
coupling of the pushforwards. In the discrete case the equalities "follow
from [SS13, Proposition 4.5]" (p. 12); the general case is the paper's.

**Why it matters for computation.** Each entry of C is a one-dimensional
transport, solved by sorting (eqs. 5–6, pp. 16–17), so the TLB costs one
n × m transport problem after nm closed-form ones (p. 16).

**Checked.** On 25 random pairs of asymmetric networks of 3 to 5 nodes
with random non-uniform measures, the TLB computed with one linear program
per joint eccentricity matched the closed form to 3 × 10⁻¹⁵, every entry of
C included, in both directions. The best coupling found by many restarts of
a GW solver never fell below the TLB, and TLB ≥ FLB ≥ SzLB held in every
case (numpy, scipy, POT 0.9.7; my script).

**What could have failed.** The inner infimum over couplings of X × Y
could have been smaller than the one-dimensional transport between the
pushed-forward weight profiles, if some coupling of the pushforwards were
not induced by a coupling of the spaces. Lemma 28 rules it out.

## What this does not say

- **That a small bound means close networks.** Every bound is one-sided.
  Take uniform 3-node networks ωX = [[0,1,2],[2,0,1],[1,2,0]] and
  ωY = [[0,1,2],[1,2,0],[2,0,1]]. Every row and column of each is a
  permutation of {0, 1, 2}, so every weight profile has the same
  distribution and TLB, FLB, SLB and the size bound vanish in both
  directions. But ωX has zero diagonal and ωY has diagonal (0, 2, 1); the
  pairs ((x, y), (x, y)) alone give disp(µ)² ≥ Σ_y ωY(y, y)² Σ_x µ(x, y)²
  ≥ 5/27, so dN,2 ≥ 0.215. This construction is the record's, not the
  paper's.
- **That the experiments measured the distance.** They report the R-TLB
  as a dissimilarity (§4, Figs. 5–6). Their structure is real for that
  invariant; it is a lower bound on the distance, nothing more.
- **That the bound is tight on any family.** The paper gives no estimate
  of the gap between the R-TLB and dN,p.
