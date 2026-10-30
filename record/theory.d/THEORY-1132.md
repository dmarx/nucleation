---
number: 1132
status: Active
formerly:
- THEORY-tmp9mvg2
title: 'For K networks compared under square loss, the multi-marginal fused Gromov–Wasserstein objective of a joint coupling tensor is exactly the sum of the pairwise fused GW objectives of its two-way marginals, so the joint optimum is at least the sum of the pairwise optima, with equality exactly when some choice of pairwise optimal couplings is jointly realizable as the marginals of one tensor; a joint alignment is consistent in that sense by construction, which for deterministic couplings means the pairwise maps compose and for soft ones does not'
version: 1
tags:
- network-science
- mathematics
date: '2026-10-29'
source:
- LIT-1814
summary: >-
  Zeng et al. (2024), [LIT-1814](../literature.d/LIT-1814.md), Theorem 1 and its proof (pp. 5, 12),
  read in [NOTE-1334](../notes.d/NOTE-1334.md). The identity was checked numerically; the
  equality condition and the remark on composition are the record's,
  short consequences of it. Active. The edge: "consistent by
  construction" means jointly realizable, not composable, once couplings
  are soft; and the paper never reports the gap that measures how far
  independent pairwise optima are from joint realizability.
---

# THEORY-1132: For K networks compared under square loss, the multi-marginal fused Gromov–Wasserstein objective of a joint coupling tensor is exactly the sum of the pairwise fused GW objectives of its two-way marginals, so the joint optimum is at least the sum of the pairwise optima, with equality exactly when some choice of pairwise optimal couplings is jointly realizable as the marginals of one tensor; a joint alignment is consistent in that sense by construction, which for deterministic couplings means the pairwise maps compose and for soft ones does not

## Source

Zeng, Du, Zhang, Xia, Liu and Tong (2024), [LIT-1814](../literature.d/LIT-1814.md), Definition 2
(pp. 2–3), Proposition 1 and Theorem 1 (pp. 3, 5; proofs pp. 11–12 of arXiv
2310.04470v2); read in [NOTE-1334](../notes.d/NOTE-1334.md).

## What was actually shown

**The identity.** For a coupling tensor S with marginals µ₁, …, µ_K and q =
2, both terms of the MFGW objective depend on S only through its two-way
marginals P_{j,k}(S): the Wasserstein term because the cost tensor is a
sum of pairwise costs (eq. 14, p. 12), the GW term because each pair's
distortion integrates out the other coordinates (eq. 15). So the
objective is Σ_{j<k} FGW(G_j, G_k; P_{j,k}(S)) (p. 12). Each marginal is a
feasible pairwise coupling, hence Theorem 1: Σ_{j<k} FGW(G_j, G_k) ≤
MFGW(G₁, …, G_K) (p. 5).

**Checked.** For K = 3 random 4-node structures with random embeddings,
the objective at a random feasible tensor equalled the sum of pairwise
objectives at its marginals to machine precision, and the tensor form of
Proposition 1 matched the direct sum over j < k (numpy; my script). The
sums must run over j < k: Definition 2 prints 1 ≤ j, k ≤ K, which would
double both terms.

**The equality condition (the record's).** MFGW = min over S of
Σ F_{jk}(P_{jk}(S)) and the right side is Σ min F_{jk}, so they are equal
iff some tensor has every two-way marginal pairwise optimal. Pairwise
couplings fitted independently need not be the marginals of any tensor;
the gap is a measure of that failure.

**Composition (the record's).** If S is supported on tuples given by
bijections, its marginals are permutations and P₁₃ is P₂₃ after P₁₂. For
soft couplings the marginals are jointly realizable but need not compose.
With two nodes per network and S = ¼ on (1,1,1), (1,2,1), (2,1,2), (2,2,2),
P₁₂ and P₂₃ are uniform, so their composition is uniform, while P₁₃ is the
identity.

**What could have failed.** The joint objective could have contained
genuinely K-way terms, coupling three networks at once. Under square
loss with a pairwise-sum cost it does not; all its content is pairwise
plus the constraint of joint realizability.

## What this does not say

- **That joint alignment is more accurate.** That is the empirical claim
  of [THEORY-1159](THEORY-1159.md), and the inequality is silent on it.
- **That consistency is free.** Joint realizability is bought by a higher
  objective whenever the pairwise optima conflict; whether the conflict is
  noise or a true non-transitivity is not settled by the mathematics.
- **That HOT's output composes.** Its tensors are entropic and soft (eqs.
  11–13), so composition holds only in the deterministic limit.
- **That the gap was measured.** The paper reports no value of
  MFGW − Σ FGW on any data.
- **Anything for a K-way cost.** With a cost tensor that is not a sum of
  pairwise terms, the identity does not hold.
