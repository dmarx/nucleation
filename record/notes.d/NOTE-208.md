---
number: 208
status: Skimmed
formerly:
- NOTE-tmpbnnv6
paper: LIT-235
title: 'Sun et al. 2023 — spectral theory of novel class discovery'
version: 1
date: '2026-09-26'
summary: >-
  For novel class discovery, a spectral contrastive loss over a graph of labeled and unlabeled data (NSCL) is equivalent to factorizing its adjacency matrix, and the resulting linear-probe error on novel classes is bounded — down to zero — by how far the known classes' feature span covers the unlabeled data's "ignorance space".
---
<!-- inactive-ok-file: LIT-235 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-26; the directive lapses when its status changes -->

# NOTE-208: Sun et al. 2023 — spectral theory of novel class discovery

## Contribution

Novel class discovery tries to find new classes in unlabeled data using a labeled set of known classes, but has lacked theory. The paper builds an analytical framework for when and how known classes help. It introduces a graph-theoretic representation learned by a new NCD Spectral Contrastive Loss, whose minimisation equals factorizing the graph's adjacency matrix. This yields a provable error bound and a necessary and sufficient condition for successful discovery, and empirically the loss matches or beats strong baselines on standard benchmarks.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1, Fig. 1 (pp. 1–2): motivating example — which novel cluster emerges (red mushrooms vs umbrella-shaped objects) depends on which known class is provided.
- §4.1–4.2, Thm 4.1 (pp. 3–4): vertices are all labeled and unlabeled points, with edges from augmentation and label sharing; minimizing NSCL is equivalent to a spectral decomposition of the adjacency matrix.
- §5.2, Thms 5.2–5.3, Fig. 2 (pp. 5–7): a toy 3D-object example (sphere/cube, red/blue) shows labeled data reduce residual error when it supplies information the unlabeled data lack.
- §5.3, Thm 5.5 (p. 7): residual bounded by ‖(I − P_{L♭}) U♭ᵀ y‖², i.e. error shrinks when the known samples' span covers the unlabeled "ignorance space"; Thm 5.6 follows (p. 8).
- §6, Tables 1–2 (pp. 8–9): NSCL competitive on NCD benchmarks, with a reported 10.6% gain over the best baseline on CIFAR-100-50.

## Open questions

- An application of the HaoChen-style spectral contrastive framework, showing the spectral lens gives usable guarantees for transfer from known to unknown classes.
- Check whether the bound's quantities can be estimated in practice or remain analytical.
- Peripheral to the heading's core claim; mainly an example of the framework's reach.
