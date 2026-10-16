---
status: Active
title: 'A metric space that admits, at every scale, random partitions into small pieces with each point padded away from piece boundaries with constant probability is absolutely Lipschitz extendable: maps from it into any Banach space extend to any containing space at O(1/padding), which gives C log λ for doubling constant λ, C r² for K_r-minor-free graph metrics, C(g+1) on genus-g surfaces and C√d from ℓ₂ᵈ; the bounds are upper bounds only, and the method needs a decomposition the domain may not have'
version: 1
tags:
- mathematics
date: '2026-10-16'
source:
- LIT-tmp2k8rj
summary: >-
  Lee and Naor (2005), [LIT-tmp2k8rj](../literature.d/LIT-tmp2k8rj.md), read in [NOTE-tmpd7vjw](../notes.d/NOTE-tmpd7vjw.md) from the authors'
  January 2004 preprint. Theorem 4.1 turns (ε, δ)-padded random partitions of
  the domain at every scale into a C/(εδ)-gentle partition of unity, and Lemma
  2.1 turns that into extensions of constant 3C/(εδ) into any Banach space;
  Lemma 3.8 carries the partitions from X to any superspace. Theorem 5.1 gives
  ae(X) ≤ C log λ(X), ≤ C r² for K_r-minor-free graph metrics, ≤ C(g+1) on
  surfaces of genus g, and e(ℓ₂ᵈ, Z) ≤ C√d, generalizing Johnson, Lindenstrauss
  and Schechtman's Cd and Matoušek's trees. No lower bound shows any of them
  tight.
---

# THEORY-tmpvy222: A metric space that admits, at every scale, random partitions into small pieces with each point padded away from piece boundaries with constant probability is absolutely Lipschitz extendable: maps from it into any Banach space extend to any containing space at O(1/padding), which gives C log λ for doubling constant λ, C r² for K_r-minor-free graph metrics, C(g+1) on genus-g surfaces and C√d from ℓ₂ᵈ; the bounds are upper bounds only, and the method needs a decomposition the domain may not have

## Source

Lee and Naor (2005), [LIT-tmp2k8rj](../literature.d/LIT-tmp2k8rj.md), *Inventiones Mathematicae* 160(1):
59–95, read in [NOTE-tmpd7vjw](../notes.d/NOTE-tmpd7vjw.md) from the authors' preprint of January 2004.
Theorem numbers are the preprint's. Filed for later use; it answers no
question of the record's yet.

## What was actually shown

**Absolute extendability.** ae(X) is the sup of the extension constant
e(X, Y, Z) over every Y ⊇ X and every Banach space Z. The paper's claim is
that for many X it is finite, and depends on X alone.

**From partitions to extensions.** A ∆-bounded decomposition is
(ε, δ)-padded if each point within ε∆ of X lies at distance at least ε∆
from the boundary of its piece with probability at least δ. Given such
decompositions at every scale 2ⁿ, Theorem 4.1 builds a C/(εδ)-gentle
partition of unity (C/(εδ)-thick likewise; (ε, δ)-separating ones give
C(1/ε + 1/δ)), and Lemma 2.1 gives extensions of constant 3K into any
closed convex subset of a Banach space, linear in the map. Lemma 3.8
turns an (ε, δ)-padded decomposition of X into an
(ε/(16+8ε), δ)-padded one of any Y ⊇ X, which is why the bound does not
depend on Y. In the appendix the same holds, multiplied by β, for
β-barycentric targets such as Hadamard spaces (Lemma 6.1, Theorem 6.2).

**The decompositions and the bounds (Theorem 5.1).**
- Every metric space is (1/(256 log C(X; 2∆, ∆/4)), ½)-padded (Lemma
  3.11, after Gupta, Krauthgamer and Lee), so doubling X is
  (C/log λ(X), ½)-padded and **ae(X) ≤ C log λ(X)** (Theorem 1.6).
- K_r-minor-free graph metrics are (c/r², ½)-padded (Lemma 3.14, a sketch
  after Klein–Plotkin–Rao and Fakcharoenphol–Talwar), so
  **ae(⟨G⟩) ≤ C r²** (Theorem 1.7). With Robertson and Seymour, a family
  of finite graphs has ae(⟨F⟩) < ∞ if and only if ⟨F⟩ does not contain
  all finite metrics (Corollary 1.8).
- Subsets of a surface of genus g: **ae(X) ≤ C(g+1)** (Corollary 1.9).
- ℓ₂ᵈ has (ε, 1/(2√d))-separating decompositions (Lemma 3.16), so
  **e(ℓ₂ᵈ, Z) ≤ C√d** for every Banach Z (Theorem 1.11), and
  e(Y, Z) ≤ C√d · dist(Y, ℓ₂ᵈ) for normed Y.
- Neighbourhoods in manifolds with Ricci(g) ≥ −(n−1)rg:
  e(X, Y, Z) ≤ C · n(1 + √(r∆)) when X is ∆-dense in Y (Proposition 5.2).

Since log λ(X) = O(log n) for n points and O(d) inside a d-dimensional
normed space, Theorem 1.6 recovers Johnson, Lindenstrauss and
Schechtman's C log n and Cd, with the superspace now arbitrary. Theorem
1.7 with r = 3 recovers Matoušek's bounded constant for trees, in the
separable case, without needing the superspace to be a tree.

**What could have come out otherwise.** A doubling space X, a superspace
Y and a Banach Z with no extension of constant O(log λ(X)) would refute
Theorem 1.6; a planar graph metric with unbounded extension constant
would refute Theorem 1.7 at r = 5. The chain Lemma 3.11 → Lemma 3.8 →
Theorem 4.1 → Lemma 2.1 was read in full; Lemma 3.14 and Corollary 3.15
only in the paper's sketch.

## What this does not say

- **That any of these bounds is tight.** The paper proves no matching
  lower bound for log λ, r², g + 1 or √d. It notes only that ae must grow
  with genus, since every n-point metric embeds isometrically in a surface
  of genus O(n³).
- **That every absolutely extendable space has a padded decomposition.**
  The method is sufficient. Sets of bounded D/ε, which Benyamini's
  appendix to Johnson and Lindenstrauss ([THEORY-tmpub08y](THEORY-tmpub08y.md)) extends at 4D/ε
  into any Banach space, can have unbounded doubling constant: an
  equilateral n-point set has λ = n (my observation). The paper's §1.2
  says the only previously known absolutely extendable families were
  absolute Lipschitz retracts or of bounded cardinality; that appendix is
  another case it does not mention (my observation).
- **Anything about maps into Hilbert space in particular.** No bound here
  uses the target's geometry beyond barycentres.
- **Explicit constants**, beyond the 256, 340, 36, 680 and 160 in the
  lemmas.

## Connections

- [THEORY-tmpi8kfq](THEORY-tmpi8kfq.md): the same paper's bound for n-point domains, which needs
  a different partition (random balls with the log-ratio analysis) and
  holds for Banach targets only.
- [THEORY-tmpub08y](THEORY-tmpub08y.md): another bound that depends on the domain alone, in
  terms of diameter over separation. The two are incomparable: an
  equilateral set favours that one, a geometric sequence 2⁰, …, 2ⁿ on a
  line favours this one (my observation).
- [THEORY-388](THEORY-388.md): random partitions appear there too, as hash buckets for
  near-neighbour search, chosen so near points rarely separate. Here the
  partitions are not stored or queried; they are averaged over (my
  observation).
