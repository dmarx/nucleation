---
number: 709
status: Active
formerly:
- THEORY-tmpj670e
title: "Mutual information between continuous variables can be estimated from k-nearest-neighbour statistics, with the joint k-th-neighbour distance in the maximum norm fixing the scale at which marginal neighbours are counted, so that the biases of the three entropy estimates largely cancel; the one approximation is a locally constant density, the systematic error scales with k/N, and exactness for independent variables is observed in every tested case but not proved"
version: 1
tags:
- information-theory
- mathematical-statistics
date: '2026-10-16'
source:
- LIT-1163
summary: >-
  Kraskov, Stögbauer & Grassberger (2004), [LIT-1163](../literature.d/LIT-1163.md), read in [NOTE-938](../notes.d/NOTE-938.md)
  (formal sections in full, numerics at lower resolution). The estimators
  are derived up to one approximation and one neglected correction; the
  rest is numerical. Checked by simulation on correlated Gaussians.
---

# THEORY-709: Mutual information between continuous variables can be estimated from k-nearest-neighbour statistics, with the joint k-th-neighbour distance in the maximum norm fixing the scale at which marginal neighbours are counted, so that the biases of the three entropy estimates largely cancel; the one approximation is a locally constant density, the systematic error scales with k/N, and exactness for independent variables is observed in every tested case but not proved

## Source

Kraskov, Stögbauer & Grassberger (2004), "Estimating Mutual Information",
arXiv cond-mat/0305641v1 (Phys. Rev. E 69, 066138), [LIT-1163](../literature.d/LIT-1163.md), read in
[NOTE-938](../notes.d/NOTE-938.md).

## What was actually shown

**Derived.** From E(log p_i) = ψ(k) − ψ(N) for the mass of the k-th
neighbour ball (Eq. 17), and a constant density inside it (Eq. 18), the
Kozachenko–Leonenko entropy estimate (Eq. 20). Counting marginal
neighbours at the joint distance gives I⁽¹⁾ = ψ(k) − ⟨ψ(n_x + 1) +
ψ(n_y + 1)⟩ + ψ(N) (Eq. 8); using rectangles gives I⁽²⁾ = ψ(k) − 1/k −
⟨ψ(n_x) + ψ(n_y)⟩ + ψ(N) (Eq. 9), with one correction neglected.

**Observed numerically.** Systematic errors scale as Φ(k/N) or
Φ((k − ½)/N) (Eq. 32), are an order of magnitude below Darbellay–Vajda's
on Gaussians, and vanish for every independent pair tested.

**Checked.** I⁽¹⁾, k = 3, on unit Gaussians with r = 0, 0.3, 0.6, 0.9 at
N = 200 and 2000: within one standard deviation of −½log(1 − r²)
throughout, with a small positive bias at r = 0.9 (0.839 against 0.830 at
N = 2000), as the paper's Fig. 4 shows.

What could have come out otherwise: the estimate at r = 0 could have
carried a k/N bias like the r ≠ 0 cases. In every case tested it did not.

## What this does not say

- **That the estimator is unbiased or consistent with a known rate.** No
  bound is proved; the rate is fitted (N^{−0.85} at r = 0.9).
- **That exactness for independence is a theorem.** It is a conjecture, and
  the stronger ratio conjecture fails for the ordered Weinman exponential.
- **Anything about conditional mutual information or transfer entropy.**
  The paper does not estimate them. Nearest-neighbour transfer-entropy
  estimators are later extensions, not held.
- **That it is invariant under reparametrization.** MI is; the estimates
  are not, and the paper transforms variables case by case.

## Connections

- A transfer-entropy estimate built this way ([TERM-057](../terms.d/TERM-057.md)) needs a
  null other than [THEORY-641](THEORY-641.md)'s χ², which is for parametric and plug-in
  estimators.
- [NOTE-788](../notes.d/NOTE-788.md)'s mutual-information estimates use an implementation of this
  estimator; its transfer entropy uses another.
