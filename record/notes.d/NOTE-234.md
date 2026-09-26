---
number: 234
status: Skimmed
formerly:
- NOTE-tmpy1qgp
paper: LIT-248
title: 'SSL-HSIC (kernel dependence maximization)'
version: 1
date: '2026-09-26'
summary: >-
  With image identity as the label, the SSL-HSIC loss −HSIC(Z,Y) + γ√HSIC(Z,Z) has a dependence term that is proportional to the average squared MMD between the per-image distributions of augmented-view representations (App. B.2). InfoNCE approximates the same term plus a variance penalty (eq. 7), so contrastive SSL separates the kernel mean embeddings of each image's view distribution.
---
<!-- inactive-ok-file: LIT-248 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-234: SSL-HSIC (kernel dependence maximization)

## Contribution

The paper treats self-supervised learning as dependence maximization. It proposes SSL-HSIC, which maximizes the Hilbert–Schmidt Independence Criterion between representations of transformed images and the image's identity while penalizing the kernelized variance of the representations. This reframes InfoNCE, usually read as a mutual-information bound, as implicitly approximating SSL-HSIC with a slightly different regularizer. It also sheds light on negative-free BYOL. The loss is estimated directly from mini-batches in time linear in batch size via random Fourier features, and it matches the state of the art on ImageNet linear evaluation and on transfer tasks.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §2.2, eqs. 1–2: HSIC(X,Y) = ‖E[φ(X)⊗ψ(Y)] − E[φ(X)]⊗E[ψ(Y)]‖²_HS. It is the squared Hilbert–Schmidt norm of the centred cross-covariance, written in kernel form as E[kl] − 2E[kl″] + E[k]E[l].
- §3, eqs. 4–5: L = −HSIC(Z,Y) + γ√HSIC(Z,Z). With one-hot identity labels, HSIC(Z,Y) ∝ E_pos[k(z₁,z₂)] − E_{z₁}E_{z₂}[k(z₁,z₂)]: pull positive pairs together, push the overall mean apart.
- §3.1, eqs. 6–8: a Taylor expansion of InfoNCE's log-sum-exp gives −HSIC(Z,Y) + ½E_{z₁}[Var_{z₂}k(z₁,z₂)], and in the small-variance regime −HSIC(Z,Y) + γHSIC(Z,Z) ≤ L_InfoNCE + o(variance).
- App. B.2: with μ_i the RKHS mean embedding of image i's view distribution, (1/2N²)Σ_{ij}MMD²(i,j) = NΔ_l·HSIC(Z,Y). The derivation uses E_{Z|i}⟨φ(Z),φ(Z′)⟩ = ⟨μ_i,μ_i⟩ and ⟨Σ_iμ_i, Σ_jμ_j⟩ for the second term.
- §3.2, eq. 10: with linear kernels and centred unit-norm features, −HSIC(Z,Y) is the within-image scatter Σ‖z_i^p − z̄_i‖², i.e. a clustering objective.

## Open questions

- It is the published statement that makes an SSL objective literally a function of kernel mean embeddings, closing the loop from Riesz via Lemma 3.1 of ra4 to "SSL spreads distributions".
- The InfoNCE ≈ HSIC link is a Taylor approximation in a small-variance regime, not an identity. A deeper read of App. B.1 should state its conditions before anyone cites it as an equivalence.
- The paper's kernels act on the learned representation Z (a fixed kernel on features), not on inputs. Compare this with Johnson et al. (ra2), where the kernel learned is the positive-pair kernel on inputs.
