---
number: 7
status: Active
formerly:
- THEORY-tmpqoglm
promote_when: >-
  Met on 2026-10-14. A close reading of Johnson, El Hanchi & Maddison
  (NOTE-tmpu7m7r) confirms Thm 3.2, Prop. 3.1 and Thm 4.1 with their
  conditions (Thm 4.1 needs d ≥ d*), and one of HaoChen et al.
  (NOTE-tmpbkfrz) confirms Lemmas 3.1–3.2.
title: 'Kernel PCA under the positive-pair density ratio recovers the eigenfunctions of the positive-pair Markov chain, and their top span is minimax-optimal for linear prediction of approximately view-invariant targets'
version: 2
history:
- version: 2
  date: '2026-10-14'
  note: >-
    Proposed to Active: promote_when is met by the close readings of LIT-258
    (NOTE-tmpu7m7r) and LIT-249 (NOTE-tmpbkfrz). Thm 4.1 now carries its
    condition d ≥ d* and the shared p(A); HaoChen et al.'s right factor is
    diag(√γ)R. Johnson et al. App. E.2 is said to apply NeuralEF, not SpIN,
    to K⁺. The "does not say" line on trained networks now cites Johnson et
    al.'s failures on real data (E.1, F.5). From NOTE-tmpdlxl6: Simon et
    al.'s "differ from ours" remark is now attributed to its real targets
    (Balestriero & LeCun, Kiani et al., Cabannes et al.), with their claim
    to complete HaoChen et al.'s account, and LIT-242 is marked as support
    by analogy. From NOTE-tmpwlhed: LIT-228 is described as giving one
    dictionary per method, all selecting the eigenvectors of G under
    constant degree, which supports the eigenvector identification on a
    finite sample only. The stale Deferred comments on LIT-249 and LIT-258
    removed, and the one on LIT-252 reworded.
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
  proved for finite augmentation spaces at the population level, Thm 4.1 for
  d at least the number of communicating classes. HaoChen et
  al.'s spectral loss is the same factorization of the normalized
  positive-pair adjacency. Whether trained networks land on these
  eigenfunctions is not shown.
extends:
- THEORY-001
extended_by:
- THEORY-005
- THEORY-009
answers:
- QUESTION-052
---
<!-- inactive-ok-file: LIT-252 — Deferred: filed and skimmed on 2026-09-26; cited as supporting only, for what Spectral Inference Networks learn, and nothing promoted here rests on it -->

# THEORY-007: Kernel PCA under the positive-pair density ratio recovers the eigenfunctions of the positive-pair Markov chain, and their top span is minimax-optimal for linear prediction of approximately view-invariant targets

## Source

Johnson, El Hanchi & Maddison (2023), [LIT-258](../literature.d/LIT-258.md), Def. 2.1, Thm 3.2, Prop. 3.1, Thm 4.1, §5 and App. C.3. Supporting: HaoChen et al. (2021), [LIT-249](../literature.d/LIT-249.md), Lemmas 3.1–3.2 and App. F; Pfau et al. (2019), [LIT-252](../literature.d/LIT-252.md), eqs. 6–8; Balestriero & LeCun, [LIT-228](../literature.d/LIT-228.md), on a finite sample; Simon et al., [LIT-242](../literature.d/LIT-242.md), by analogy only.

## What was actually shown

K⁺ is a Mercer kernel with an explicit feature map ([LIT-258](../literature.d/LIT-258.md) Def. 2.1). Population kernel PCA under K⁺ returns exactly the L²(p)-orthonormal eigenfunctions f_i of the positive-pair chain p⁺(a′|a), with h_i = λ_i^½ f_i (Thm 3.2). E_p⁺(g(a₁) − g(a₂))² = Σ(2 − 2λ_i)c_i² (Prop. 3.1), so the top eigenfunctions are the most view-invariant directions, and their span is minimax-optimal for linear prediction of approximately view-invariant targets (Thm 4.1). The optimality is for squared L²(p) error, with one p(A) shared between pretraining and the downstream task, and needs d ≥ d*, the multiplicity of eigenvalue 1 (one per communicating class); below d* every representation has unbounded worst-case error, and above it the minimax value is ε/(2(1 − λ_(d+1))) (App. D).

HaoChen et al. show the spectral contrastive loss equals ‖D^(−1/2)AD^(−1/2) − FFᵀ‖²_F plus a constant (Lemma 3.2), so its minimizers are the top eigenvectors up to a positive row scaling and a right factor diag(√γ)R with R orthonormal, invertible while γ_k > 0; Lemma 3.1 says no invertible right factor or positive row scaling changes linear-probe predictions. Johnson et al. identify these eigenvectors with their eigenfunctions scaled by p(a)^½ (§5, App. C.3). Pfau et al.'s Spectral Inference Networks learn the same objects directly (eqs. 6–7). Johnson et al. App. E.2 names SpIN and NeuralEF as ways to extract them, and applies NeuralEF, not SpIN, to K⁺.

On a finite sample, Balestriero & LeCun ([LIT-228](../literature.d/LIT-228.md)) give one spectral method per SSL loss (VICReg as Laplacian eigenmaps, SimCLR as generalized MDS, Barlow Twins as CCA) and say that all of them learn representations whose top singular vectors align with those of the pair matrix G. Under the paper's constant-degree assumption D = cI, G/c is the transition matrix of the positive-pair chain on the sample and equals HaoChen et al.'s normalized adjacency, so the three select the same eigenvectors and differ in scaling and rank. That reconciliation is the record's; the paper does not mention K⁺ or the Markov chain.

## What this does not say

- That trained networks on real data reach these eigenfunctions. Johnson et al.'s own experiments find recovery depends on parameterization and augmentation strength, on synthetic data. On real data they could not obtain a reliable estimate of the eigenfunctions from a pretrained SimCLR model, and their ImageNet spectral-loss model "does not appear to be a good approximation of K⁺" (App. E.1, F.5).
- Anything for asymmetric methods (BYOL, SimSiam, cross-modal pairs), which fall outside the self-adjoint setting.
- How this relates to Simon et al.'s kernel ([LIT-242](../literature.d/LIT-242.md)), which is built from the network's NTK and the pair structure, not from K⁺, so it supports this account by analogy only. Simon et al. say their final representations differ from those of Balestriero & LeCun, Kiani et al. and Cabannes et al.; of HaoChen et al. they say they complete the account, by identifying which of its degenerate optima training reaches in linearized models.
- Anything about population eigenfunctions or minimax optimality from Balestriero & LeCun ([LIT-228](../literature.d/LIT-228.md)). Their support is for the eigenvector identification on a finite sample, for idealized losses, and their downstream result (Theorem 9) concerns zero training-set probe loss only. Johnson et al. note an ISOMAP link without reconciling it with K⁺.
