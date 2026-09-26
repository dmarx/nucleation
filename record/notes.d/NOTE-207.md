---
number: 207
status: Skimmed
formerly:
- NOTE-tmpbn154
paper: LIT-245
title: 'MDL generalization guarantees for representation learning'
version: 1
date: '2026-09-26'
summary: >-
  Generalization of representation learning is bounded not by I(X;U) but by the minimum description length of the latent variables (or predicted labels) under a symmetric prior — a multi-letter relative entropy that reflects the encoder's structure and is non-vacuous for deterministic encoders.
---
<!-- inactive-ok-file: LIT-245 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-207: MDL generalization guarantees for representation learning

## Contribution

Theoretical guarantees for representation learning are scarce. The authors build a compressibility framework that bounds the generalization error of a representation learning algorithm by the MDL of the labels or of the latent representations. Instead of the mutual information between input and representation, which they argue does not actually reflect generalization, the bounds use a multi-letter relative entropy between the train-and-test distribution of representations and a fixed prior, so they reflect the encoder's structure and remain non-vacuous for deterministic algorithms. The approach extends Blum–Langford PAC-MDL bounds with block coding and lossy compression (the latter subsuming geometrical compression), gives what the authors believe are the first such bounds for IB-type encoders, and motivates a data-dependent prior that beats classical VIB priors in simulations.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 (p. 2): the covering lemma shows a latent U can be described with about I(U;X) bits per symbol, which is why I(U;X) has been read as the MDL of the latent variables (citing Vera et al. 2018 = k08, and Grünwald–Roos 2019 = k12, for the MDL–generalization link).
- §1 (p. 2), "Critics to IB": four objections to I(U;X) as a generalization measure — existing bounds (k08; Kawaguchi et al. 2023) hold only for finite alphabets and their constant term dominates, making them vacuous; experiments show dependence on geometrical compression rather than I(U;X) (Geiger & Koch 2019); I(U;X) is invariant to bijections so ignores encoder simplicity; it is infinite for deterministic encoders on continuous data.
- Contents: §2 bounds via predicted-label complexity with type-I and type-II symmetric priors; §3 bounds via latent-variable complexity (type-III symmetry, the main result); §4 experiments.
- Conclusion (App. C.4, p. 22): type-I symmetry connects Blum–Langford to conditional mutual information (Steinke–Zakynthinou) bounds; the MDL of latents "captures the simplicity and structure of the encoder" unlike mutual information, which captures "information leakage"; data-dependent priors outperform VIB's classical priors in simulation.

## Open questions

- The sharpest statement in the batch that the IB quantity I(X;U) is the wrong complexity and a description-length quantity is the right one — directly on the heading's question of how compression/K-complexity relates to minimal sufficiency.
- Contradicts k08 on the role of I(X;U); if both are filed, the relation should be recorded explicitly.
- Check what the "symmetric prior" requirement costs in practice and how the proposed data-dependent prior is actually used as a regularizer (practice candidate).
