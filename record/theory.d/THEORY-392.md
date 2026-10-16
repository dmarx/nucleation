---
number: 392
status: Active
formerly:
- THEORY-tmp7nqd6
title: 'Every map from an n-point subset of a metric space into Hilbert space extends to the whole space with Lipschitz constant at most K√(log n) times its own, by dimension reduction to K log n coordinates followed by Kirszbraun and the non-linear Hahn–Banach theorem; for L_p, 1 ≤ p < 2, the constant must be at least δ(Log n/Log Log n)^(1/p−1/2), so √(log n) is right up to a log log factor in the worst case'
version: 2
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Updated after reading the later works: sharpness still open per Lee and
    Naor (NOTE-927); Problem 4 answered by inference from Linial,
    London and Rabinovich (NOTE-928), replacing "unchecked".
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-1153
presupposes:
- THEORY-397
summary: >-
  Johnson and Lindenstrauss (1984), [LIT-1153](../literature.d/LIT-1153.md), read in [NOTE-930](../notes.d/NOTE-930.md).
  Theorem 1 proves Marcus and Pisier's conjecture L(X, n) ≤ K(Log n)^(1/2)
  for every metric space X; Theorem 3 gives L(p, n) ≥ δ(Log n/Log Log n)^(1/p−1/2)
  for 1 ≤ p < 2, hence L(∞, n) ≥ δ(Log n/Log Log n)^(1/2). The √(log n)
  comes from the √k cost of passing between ℓ₂ᵏ and ℓ∞ᵏ, with k of order
  log n. Whether the upper bound is sharp the paper leaves open, and the
  constants are loose.
---

# THEORY-392: Every map from an n-point subset of a metric space into Hilbert space extends to the whole space with Lipschitz constant at most K√(log n) times its own, by dimension reduction to K log n coordinates followed by Kirszbraun and the non-linear Hahn–Banach theorem; for L_p, 1 ≤ p < 2, the constant must be at least δ(Log n/Log Log n)^(1/p−1/2), so √(log n) is right up to a log log factor in the worst case

## Source

Johnson and Lindenstrauss (1984), [LIT-1153](../literature.d/LIT-1153.md), *Contemporary
Mathematics* 26: 189–206, read in [NOTE-930](../notes.d/NOTE-930.md) from a scan of the
published article. Filed for later use; it answers no question of the
record's yet.

## What was actually shown

**The quantity.** L(X, n) is the smallest L such that every f from an
n-point subset of X into ℓ₂ extends to all of X with ‖f̃‖_lip ≤ L‖f‖_lip.
L(p, n) is L(L_p(0, 1), n). Log x means max(1, ln x).

**Upper bound (Theorem 1).** sup_{n≥2} (Log n)^(−1/2) L(∞, n) < ∞, so
L(X, n) ≤ K√(Log n) for every metric space X. The proof takes the image
A = f[M] ⊂ ℓ₂ and applies Lemma 1, the dimension reduction of
[THEORY-397](THEORY-397.md), with τ = 1/2: a map g⁻¹ from A into ℓ₂ᵏ, k ≤ K log n,
with ‖g⁻¹‖_lip ≤ 1 and ‖g‖_lip ≤ 3. It extends g by Kirszbraun's theorem,
passes to ℓ∞ᵏ by the identity (norm 1, inverse norm √k), extends there by
the non-linear Hahn–Banach theorem, and composes back:
‖f̃‖_lip ≤ 3√k‖f‖_lip ≤ 3K√(log n)‖f‖_lip.

**Lower bound (Theorem 3).** There is δ > 0 such that for all n ≥ 2 and
1 ≤ p < 2, L(p, n) ≥ δ(Log n/Log Log n)^(1/p−1/2). Since L(∞, n) ≥ L(1, n),
L(∞, n) ≥ δ(Log n/Log Log n)^(1/2). The proof uses Lemma 4: L_p contains
subspaces E with d(E, ℓ₂ᴺ) ≤ 2 onto which every projection has norm at
least δN^(1/p−1/2), with N = Log n/(2 Log Log n), and a linearization from
Lindenstrauss (1964) with a smoothing lemma (Proposition 1, Lemma 5),
which the reading followed only in outline.

**What could have come out otherwise.** An n-point subset of some metric
space and a map into ℓ₂ with no extension of constant O(√(log n)) would
refute Theorem 1. The proof of Theorem 1 was read in full; Proposition 1
and Lemma 5, used only for Theorem 3, were followed in outline.

## What this does not say

- **That √(log n) is sharp.** The gap to the lower bound is
  (Log Log n)^(1/2), and the paper leaves sharpness open. It is still open
  in the record's later reading: Lee and Naor ([LIT-1152](../literature.d/LIT-1152.md), [NOTE-927](../notes.d/NOTE-927.md),
  §1.4) say no known lower bound beats √(log n) for any target. Their
  C log n/log log n ([THEORY-396](THEORY-396.md)) holds for every Banach target and is
  weaker than this bound for Hilbert space.
- **Anything about targets other than Hilbert space**, except through
  Theorem 3's L_p subspaces and [THEORY-398](THEORY-398.md)'s separated case.
- **Anything about embedding the metric space itself.** The paper's
  Problems 3 and 4 ask about that and leave it open. Problem 4, distortion
  K√(log n) into ℓ₂, is answered in the negative by the record's inference
  from Linial, London and Rabinovich ([THEORY-394](THEORY-394.md)): every n-point
  metric embeds with distortion O(log n), and constant-degree expanders
  need Ω(log n). That paper cites neither Problem 4 nor this one; the
  inference is the record's.
- **Explicit constants.** K is shown to exist; the steps are loose
  (Theorem 1's last step needs K ≥ 1).

## Connections

- [THEORY-397](THEORY-397.md): this account uses that one's dimension reduction as its
  first step. The extension is the purpose the lemma was proved for.
- [THEORY-398](THEORY-398.md): the paper's other extension theorem, for separated
  domains, where the constant depends on the ratio of diameter to
  separation and not on n.
