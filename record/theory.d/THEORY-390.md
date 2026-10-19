---
number: 390
status: Active
formerly:
- THEORY-tmp4mezl
title: 'Any distribution of n × N matrices whose norms concentrate as Johnson–Lindenstrauss proofs require gives the restricted isometry property of order k with probability at least 1 − 2e^{−c₂n} for k ≤ c₁n/log(N/k), by a union bound over (12/δ)^k net points on each of the (eN/k)^k sparse supports; this makes k log(N/k) measurements sufficient for Gaussian, ±1 and sparse three-valued matrices, and does not show they are necessary'
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-1156
presupposes:
- THEORY-397
answers:
- QUESTION-120
summary: >-
  Baraniuk, Davenport, DeVore and Wakin (2008), [LIT-1156](../literature.d/LIT-1156.md), read in
  [NOTE-931](../notes.d/NOTE-931.md) from the author-posted copy. The only assumption is the
  concentration inequality Pr(|‖Φx‖² − ‖x‖²| ≥ ε‖x‖²) ≤ 2e^{−nc₀(ε)}, met
  with Achlioptas's c₀(ε) = ε²/4 − ε³/6. The proof is the JL argument run
  over a net on every sparse support, plus a step from the net to the whole
  subspace. Necessity of k log(N/k) is recalled from Gelfand widths, not
  derived from concentration, and constants are implicit.
---

# THEORY-390: Any distribution of n × N matrices whose norms concentrate as Johnson–Lindenstrauss proofs require gives the restricted isometry property of order k with probability at least 1 − 2e^{−c₂n} for k ≤ c₁n/log(N/k), by a union bound over (12/δ)^k net points on each of the (eN/k)^k sparse supports; this makes k log(N/k) measurements sufficient for Gaussian, ±1 and sparse three-valued matrices, and does not show they are necessary

## Source

Baraniuk, Davenport, DeVore and Wakin (2008), [LIT-1156](../literature.d/LIT-1156.md), *Constructive
Approximation* 28, read in [NOTE-931](../notes.d/NOTE-931.md) from the copy on Davenport's
Georgia Tech page.

## What was actually shown

**The assumption (4.3).** For each fixed x,
Pr(|‖Φx‖² − ‖x‖²| ≥ ε‖x‖²) ≤ 2e^{−nc₀(ε)}, Φ being n × N. Gaussian, ±1 and
√3·{+1, 0, −1} entries (4.4)–(4.6) meet it with c₀(ε) = ε²/4 − ε³/6,
attributed to Achlioptas. This is the per-vector tail of
[THEORY-397](THEORY-397.md).

**One support (Lemma 5.1).** For a coordinate subspace X_T, #T = k, take a
δ/4-net of its unit sphere, at most (12/δ)^k points, and apply (4.3) at
ε = δ/2 to each. A bootstrap step carries the bound from the net to all of
X_T: (1 − δ)‖x‖ ≤ ‖Φx‖ ≤ (1 + δ)‖x‖, with probability at least
1 − 2(12/δ)^k e^{−c₀(δ/2)n}.

**All supports (Theorem 5.2).** A union bound over C(N, k) ≤ (eN/k)^k
supports gives failure at most 2e^{−c₀(δ/2)n + k[log(eN/k) + log(12/δ)]}
(5.10), so the RIP holds for k ≤ c₁n/log(N/k) with probability at least
1 − 2e^{−c₂n}, for c₂ ≤ c₀(δ/2) − c₁[1 + (1 + log(12/δ))/log(N/k)].

**§6.** Any distribution that yields JL embeddings yields RIP matrices,
with slightly worse constants. Taking the nets in the spans of a fixed
orthonormal basis Ψ gives the RIP for ΦΨ, which the authors say was new
for the ±1 and sparse ensembles.

**What could have come out otherwise.** A matrix ensemble meeting (4.3)
that fails the RIP at the stated k and probability would refute it. The
proof was checked in the reading. The last step from (5.1) to the squared
RIP is not written out, and squaring makes the constant about 2δ.

## What this does not say

- **That k log(N/k) measurements are necessary.** The paper takes that
  from Garnaev–Gluskin's Gelfand widths of the ℓ₁ ball with Candès–Tao,
  which is geometry, not concentration.
- **Why the superposition bound in [NOTE-278](../notes.d/NOTE-278.md) holds.** That bound is a
  necessity bound which assumes the RIP. This account says random
  matrices satisfy the assumption, and nothing about the bound's proof.
- **Any constants.** c₁ and c₂ are shown to exist, not computed.
- **Where recovery switches from success to failure.** That is a sharp
  location, [THEORY-391](THEORY-391.md), and a union bound gives only a sufficient
  order.
- **Anything about nonnegative {0, 1} matrices**, which are not zero-mean
  and do not meet (4.3) as stated.

## Connections

- [QUESTION-120](../questions.d/QUESTION-120.md): the superposition thread, on the side of sufficiency. The family is
  the net points on every support, (eN/k)^k(12/δ)^k, and its log over
  c₀(δ/2) ≈ δ²/16 is the threshold, so the question's proposed shape holds
  here too, with a k log(12/δ) term the JL count lacks.
- [THEORY-397](THEORY-397.md) supplies the concentration this account takes as its
  premise.
