---
status: Skimmed
paper: LIT-tmpprh4p
title: 'Simon et al. 2023 — stepwise nature of SSL'
version: 1
date: '2026-09-26'
summary: >-
  Joint-embedding SSL learns its embedding one dimension at a time in discrete, well-separated steps — in a linearized Barlow Twins model it provably learns the top eigenmodes of a contrastive kernel in order, so SSL is to kernel PCA what supervised learning is to kernel regression — and the same stepwise rank growth appears in ResNets trained with Barlow Twins, SimCLR and VICReg.
---
<!-- inactive-ok-file: LIT-tmpprh4p — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-tmpu1tza: Simon et al. 2023 — stepwise nature of SSL

## Contribution

The paper offers a simple picture of how joint-embedding self-supervised methods train: their high-dimensional embeddings are acquired one dimension at a time in a sequence of separated steps. The picture comes from exactly solving the training dynamics of a linearized Barlow Twins model, applicable to infinitely wide networks, from small initialization; the model learns the top eigenmodes of a particular contrastive kernel in stepwise fashion, and the final representation has a closed form. The same stepwise behaviour is then observed in deep ResNets trained with Barlow Twins, SimCLR and VICReg. The authors suggest kernel PCA as a model of SSL in the way kernel regression models supervised learning.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1, Fig. 1 (pp. 1–2): embeddings start low-rank and gain rank one by one; loss curves show discrete drops aligned with eigenvalue growth.
- §4.2, Prop. 4.1 & 4.3 (pp. 4–5): exact trajectories from aligned initialization; the "top spectral" solutions are exactly the minimum-Frobenius-norm zero-loss solutions, linking to the implicit low-norm bias of gradient descent.
- §4.3, Result 4.6 (p. 5): as initialization scale → 0, generic trajectories converge to the aligned solution — stated as a Result because the derivation is informal (footnote 8).
- §5.1–5.2, Prop. 5.1 (pp. 6–7): the kernelized solution makes infinite-width SSL equivalent to kernel PCA on a matrix K_Γ; with identical views the model learns the top eigenmodes of its NTK; the result extends to multimodal SSL.
- §6, Figs. 2–4 (pp. 8–9): stepwise learning is clearest from small init but persists with standard init and learning rates (bimodal eigenvalue histograms), and also shows in hidden representations; not immediately seen for BYOL (footnote 16).
- §7 (p. 9): limitations — real networks are not kernel machines (NTK evolves) and downstream probes use hidden layers; suggests optimizers that focus updates on near-zero eigendirections could speed SSL training (App. G).

## Open questions

- Supplies the dynamical side of the spectral reading (k17, k21): not only is the optimum a spectral embedding, training reaches it eigenmode by eigenmode.
- Candidate practice lead: slow SSL convergence attributed to low-eigenvalue modes; check whether App. G's speedup proposals were tested.
- Check the gap between the NTK-regime theory and realistic runs, and the BYOL exception.
