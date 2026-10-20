---
number: 778
status: Active
formerly:
- THEORY-tmpnxcxo
title: 'In the Random Hierarchy Model with v symbols per level, m rules per symbol and s-tuples, the covariance between two tokens whose lowest common ancestor is ℓ levels up has zero mean over grammars and root-mean-square size about ((1 − m/v^(s−1))/(v³ m^(2ℓ−1)))^(1/2), falling by a factor m per level, while its estimate from P sequences carries noise of about (v²P)^(−1/2), so the two meet at P_ℓ ≈ v m^(2ℓ−1)/(1 − m/v^(s−1)); all to leading order in large v and m'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Split from THEORY-201 by the promotion audit (batch 063, ADR-040 and
    ADR-047 v2), on the pattern of THEORY-770's split from THEORY-673.
    THEORY-201 bundled these derived statistics with measured learning
    curves and an argued link between them. The derivation was re-derived
    to leading order and checked by exact computation in the review; this
    THEORY holds it, and THEORY-201 keeps the rest and extends this one.
tags:
- mathematical-statistics
- learning-theory
- compositionality
date: '2026-10-20'
source:
- LIT-883
summary: >-
  Cagnetta and Wyart (2024), [LIT-883](../literature.d/LIT-883.md), App. D–F, read in [NOTE-687](../notes.d/NOTE-687.md); re-derived
  to leading order by the promotion audit and checked against exact
  covariances of sampled grammars. A statement about the statistics of the
  generative model only: it says nothing about what a trained network
  learns, or when, and nothing about natural language.
extended_by:
- THEORY-201
---
<!-- inactive-ok-file: THEORY-201 THEORY-673 — Proposed; the account that extends this one, and the split this one follows -->

# THEORY-778: In the Random Hierarchy Model with v symbols per level, m rules per symbol and s-tuples, the covariance between two tokens whose lowest common ancestor is ℓ levels up has zero mean over grammars and root-mean-square size about ((1 − m/v^(s−1))/(v³ m^(2ℓ−1)))^(1/2), falling by a factor m per level, while its estimate from P sequences carries noise of about (v²P)^(−1/2), so the two meet at P_ℓ ≈ v m^(2ℓ−1)/(1 − m/v^(s−1)); all to leading order in large v and m

## Source

Cagnetta and Wyart (2024, NeurIPS 2024), [LIT-883](../literature.d/LIT-883.md), Appendices D–F (the
covariance, the sampling noise and the tuple correlations), read in full
in [NOTE-687](../notes.d/NOTE-687.md) from arXiv v3. The note followed the moment computations to
their large-v, large-m limits. The promotion audit re-derived the result
to leading order and checked it numerically (batch 063).

## What was actually shown

**The model.** L levels; v symbols at each; each symbol has m rules, each
an s-tuple of symbols of the level below. A level's v·m tuples are
distinct, so it uses a fraction f = m/v^(s−1) of all s-tuples. The root and
every rule choice are uniform.

**The derivation, to leading order.**

1. *Siblings.* For two positions of one tuple, the joint probability of
   the pair (x, y) is N(x, y)/(vm), where N counts the level's tuples with
   x and y in those positions. Each of the v^(s−2) such tuples is present
   with probability f, so N has mean m/v and variance v^(s−2) f(1 − f),
   the 1 − f being the correction for drawing tuples without replacement.
   The covariance therefore has mean zero over grammars and variance
   (1 − f)/(v³ m).
2. *One level further.* A level's transition matrix for one position is
   uniform plus a fluctuation Δ whose entries have variance about 1/(vm).
   A covariance has zero row and column sums, so passing it down both
   branches leaves Δ₁ᵀ C Δ₂. Each factor multiplies the variance by
   v · 1/(vm) = 1/m: a factor m per level in root-mean-square size.
3. *Level ℓ.* Hence variance (1 − f)/(v³ m^(2ℓ−1)). Two tokens t apart
   have their common ancestor about log_s t levels up, so the size decays
   roughly as t^(−ln m/ln s).
4. *Sampling noise.* Each entry of a joint estimated from P sequences has
   variance about 1/(v²P), so the estimated covariance has noise
   (v²P)^(−1/2).
5. *Threshold.* Signal equals noise at P_ℓ = v m^(2ℓ−1)/(1 − f).

**The check.** For s = 2 and L = 4, the exact covariance was computed by
multiplying transition matrices for 20 sampled grammars per setting, and
compared with the formula. The ratio for ℓ = 1 to 4 was 1.02, 1.02, 1.01
and 0.96 at v = 128, m = 16, and 1.07, 0.97, 0.91 and 0.74 at v = 16,
m = 4. The agreement improves with v and m, and degrades with depth when
they are small, as a leading-order result should. The sampling noise came
within 3% of (v²P)^(−1/2) for P from 10³ to 10⁶. The recipe is in the
audit's decision for [THEORY-201](THEORY-201.md).

## What this does not say

- **Not exact.** It is leading order in large v and m, with tuple draws
  treated as independent. At small v and m and deep levels the exact
  covariance falls below it (about a quarter below at v = 16, m = 4,
  ℓ = 4).
- **Nothing about learning.** That a trained network detects these
  correlations, represents the hidden symbols, or shows loss steps at P_ℓ
  is [THEORY-201](THEORY-201.md)'s claim, which measures some of it in small networks and
  argues the link.
- **Nothing about language.** The model's rules are uniform, unambiguous
  and of fixed shape. That real text has correlations decaying as a power
  of distance does not make it such a tree.
- **Only s = 2 was checked numerically.** The derivation covers general s;
  the exact computation did not.

## Connections

- [THEORY-201](THEORY-201.md) extends this, adding the learning curves and the
  character-level test.
- [THEORY-195](THEORY-195.md) is the classification result for the same model ([LIT-877](../literature.d/LIT-877.md)).
