---
number: 7
status: Proposed
formerly:
- THEORY-tmpqoglm
promote_when: >-
  A close reading of Johnson, El Hanchi & Maddison confirming Thm 3.2, Prop.
  3.1 and Thm 4.1 with their conditions, and of HaoChen et al.'s Lemmas
  3.1–3.2. The results are proved in the sources; this record has so far only
  skimmed them.
title: 'Kernel PCA under the positive-pair density ratio recovers the eigenfunctions of the positive-pair Markov chain, and their top span is minimax-optimal for linear prediction of approximately view-invariant targets'
version: 1
tags:
- representation-learning
- mathematics
date: '2026-09-26'
source:
- LIT-258
- LIT-249
- LIT-252
- LIT-228
- LIT-242
summary: >-
  Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), Thm 3.2 and Thm 4.1 —
  proved for finite augmentation spaces at the population level. HaoChen et
  al.'s spectral loss is the same factorization of the normalized
  positive-pair adjacency. Whether trained networks land on these
  eigenfunctions is not shown.
extends:
- THEORY-001
extended_by:
- THEORY-005
- THEORY-009
---
<!-- inactive-ok-file: LIT-252 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-258 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->
<!-- inactive-ok-file: LIT-249 — Deferred: filed and skimmed on 2026-09-26 while pursuing the owner's Riesz/Radon–Nikodym/GNS question; the theories citing it are Proposed until it is read closely -->

# THEORY-007: Kernel PCA under the positive-pair density ratio recovers the eigenfunctions of the positive-pair Markov chain, and their top span is minimax-optimal for linear prediction of approximately view-invariant targets

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), Def. 2.1, Thm 3.2, Prop. 3.1, Thm 4.1, §5 and App. C.3. Supporting: HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), Lemmas 3.1–3.2 and App. F; Pfau et al. (2019), [LIT-252](../literature.d/LIT-252.md), eqs. 6–8; Balestriero & LeCun, [LIT-228](../literature.d/LIT-228.md); Simon et al., [LIT-242](../literature.d/LIT-242.md).

## What was actually shown

K⁺ is a Mercer kernel with an explicit feature map ([LIT-258](../literature.d/LIT-258.md) Def. 2.1). Population kernel PCA under K⁺ returns exactly the L²(p)-orthonormal eigenfunctions f_i of the positive-pair chain p⁺(a′|a), with h_i = λ_i^½ f_i (Thm 3.2). E_p⁺(g(a₁) − g(a₂))² = Σ(2 − 2λ_i)c_i² (Prop. 3.1), so the top eigenfunctions are the most view-invariant directions, and their span is minimax-optimal for linear prediction of approximately view-invariant targets (Thm 4.1).

HaoChen et al. show the spectral contrastive loss equals ‖D^(−1/2)AD^(−1/2) − FFᵀ‖²_F plus a constant (Lemma 3.2), so its minimizers are the top eigenvectors up to a positive row scaling and an invertible right factor, neither of which changes linear-probe predictions (Lemma 3.1). Johnson et al. identify these eigenvectors with their eigenfunctions scaled by p(a)^½ (§5, App. C.3). Pfau et al.'s Spectral Inference Networks learn the same objects directly (eqs. 6–7), and Johnson et al. App. E.2 applies them to K⁺.

## What this does not say

- That trained networks on real data reach these eigenfunctions. Johnson et al.'s own experiments find recovery depends on parameterization and augmentation strength, on synthetic data.
- Anything for asymmetric methods (BYOL, SimSiam, cross-modal pairs), which fall outside the self-adjoint setting.
- How this relates to Simon et al.'s kernel ([LIT-242](../literature.d/LIT-242.md)), which is built from the network's NTK and the pair structure, not from K⁺. Simon et al. say their final representations differ from those of the optimum-based accounts.
- Which of Balestriero & LeCun's dictionaries ([LIT-228](../literature.d/LIT-228.md): Laplacian eigenmaps, ISOMAP, CCA) is the right one for a given method; Johnson et al. note the ISOMAP link without reconciling it with K⁺.
