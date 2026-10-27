---
status: Active
title: 'In angular synchronization from m pairwise offsets, each exact with probability p and otherwise uniform over L values, no estimator of any computational cost can recover all n angles with small error when p is below about √((n/m)·2 log₂ L/(L − 1)), nor an angle of average degree below about √((n/m)·log₂ L/(L − 1)), because each offset carries at most I(L, p) ≈ ½(L − 1)p² bits; below these thresholds a global configuration that exists is not determined by the pairwise evidence, whatever the resources spent on finding it'
version: 1
tags:
- information-theory
- mathematics
date: '2026-10-27'
source:
- LIT-tmpjnkzw
summary: >-
  Singer (2011), [LIT-tmpjnkzw](../literature.d/LIT-tmpjnkzw.md), §5, read in [NOTE-tmplhrxg](../notes.d/NOTE-tmplhrxg.md) from arXiv v2.
  Active as mathematics: Fano's inequality applied to an explicit entropy
  count, asymptotic in m, n → ∞, p → 0 with L fixed. The bound is loose
  (it ignores the dependencies among offsets) and covers exact recovery and
  per-angle recovery, not partial correlation, which the eigenvector method
  achieves below it. It says nothing of what a bounded algorithm can do
  above it.
---
<!-- inactive-ok-file: CLAIM-tmpi1bjh CLAIM-tmpdjt64 THEORY-tmp24sxe — Proposed; the claims this bears on and the companion account of the cheap method, cited as open -->

# THEORY-tmpco2va: In angular synchronization from m pairwise offsets, each exact with probability p and otherwise uniform over L values, no estimator of any computational cost can recover all n angles with small error when p is below about √((n/m)·2 log₂ L/(L − 1)), nor an angle of average degree below about √((n/m)·log₂ L/(L − 1)), because each offset carries at most I(L, p) ≈ ½(L − 1)p² bits; below these thresholds a global configuration that exists is not determined by the pairwise evidence, whatever the resources spent on finding it

## Source

Singer (2011), [LIT-tmpjnkzw](../literature.d/LIT-tmpjnkzw.md), §5, pp. 14–20 of arXiv 0905.3174v2; read in
[NOTE-tmplhrxg](../notes.d/NOTE-tmplhrxg.md).

## What was actually shown

**The model.** Angles and offsets take L values (resolution 2π/L). The n
angles are independent and uniform, so H(θⁿ) = n log₂ L (5.2). Each measured
offset equals θᵢ − θⱼ mod L with probability p and is otherwise uniform
(5.3), so it carries mutual information
I(L, p) = log₂ L − H(L, p) (5.4–5.8), with
I(L, p) = ½(L − 1)p² + O(p³) near p = 0 (5.20).

**All angles.** Given the angles the offsets are independent, so
H(δᵐ|θⁿ) = mH(L, p) (5.13), and H(δᵐ) ≤ m log₂ L (5.14), hence
H(θⁿ|δᵐ) ≥ n log₂ L − mI(L, p) (5.16): "each of the m offset measurements
can decrease the conditional entropy by at most I(L, p), the information that
it carries" (p. 17). Fano's inequality then gives
P_e ≥ 1 − mI(L, p)/(n log₂ L) − 1/(n log₂ L) (5.18), "applicable to all
decoding algorithms, not just for the eigenvector method" (p. 18). So
p = √((n/m)·2 log₂ L/(L − 1))·√β forces P_e ≥ 1 − β + o(1) (5.21), and the
threshold is p_c^inf = √((n/m)·2 log₂ L/(L − 1)) (5.22).

**One angle.** Conditioning on all other angles can only lower the entropy
(5.23), and then only the dᵢ offsets at vertex i inform θᵢ (5.24), so
dᵢI(L, p) > log₂ L is necessary for a small error on θᵢ (5.30). At the
average degree 2m/n this is p > p_c^ind = √((n/m)·log₂ L/(L − 1)) (5.33).
Between p_c^ind and p_c^inf "it is impossible to successfully decode all
angles, it may still be possible to decode some angles" (p. 20).

**What could have come out otherwise.** The bound is a count, and a
different measurement model would give a different count. The point it
makes is structural: the limit is set by the evidence per unknown (m/n and
p), and it binds every procedure, so below it no amount of computation
recovers the configuration, though the configuration exists by
construction.

## What this does not say

- **That recovery succeeds above the threshold.** The bound is a necessary
  condition only. Whether a feasible algorithm reaches it is a separate
  question ([THEORY-tmp24sxe](THEORY-tmp24sxe.md)).
- **That nothing can be learned below it.** The eigenvector method gets an
  above-random correlation below p_c^inf for L = 2, which the paper notes is
  "not a violation of information theory" because correlation is not exact
  decoding (pp. 18–19).
- **That the constant is tight.** H(δᵐ) ≤ m log₂ L ignores the dependencies
  among offsets, such as the triangle relation, and the paper calls the bound
  "certainly not a tight bound" (p. 17). The exponential form of the error
  (Wolfowitz's strong converse) is asserted, not shown (p. 18).
- **Anything outside the model.** Exact-or-uniform offsets, independent
  angles, fixed L, m and n large, p small. Correlated or adversarial errors
  and continuous noise are not covered.
- **That the configuration exists in general.** Existence is assumed by
  the model, so the result separates "exists but is not determined by the
  evidence" from "determined but expensive to find", and has nothing to say
  about a configuration that fails to exist ([CLAIM-tmpdjt64](../claims.d/CLAIM-tmpdjt64.md)'s
  obstructions). It bears on [CLAIM-tmpi1bjh](../claims.d/CLAIM-tmpi1bjh.md)'s "recovering a global
  structure from pairwise evidence" as the case where the bound is on
  evidence, not on resources.
