### Added

- [QUESTION-147](record/questions.d/QUESTION-147.md): whether symmetry-cluster stability predictions hold
  in a second system of near-identical units, formerly [THEORY-276](record/theory.d/THEORY-276.md)'s
  promotion condition.
- [QUESTION-148](record/questions.d/QUESTION-148.md): whether bilinear knowledge-graph scores admit a
  sheaf-coboundary representation, formerly part of [THEORY-299](record/theory.d/THEORY-299.md)'s
  promotion condition.

### Changed

- [THEORY-276](record/theory.d/THEORY-276.md) (symmetry orbits as synchronization clusters, and isolated
  desynchronization) is promoted to Active. The invariance is derived
  through fixed-point subspaces, and the hypothesis that the cluster's
  factor moves nothing else is made explicit.
- [THEORY-299](record/theory.d/THEORY-299.md) (knowledge-graph embeddings as sheaf 0-cochains) is narrowed:
  each triple is scored by a norm of its coboundary, and the summed score
  is the Laplacian form only in the squared-Euclidean variant. It is
  promoted to Active.
- [THEORY-301](record/theory.d/THEORY-301.md) (Procrustes against decoding distance, through the
  participation ratio) is promoted to Active, with eqs. 25–26 derived
  directly for real matrices.
- Each carries out the promotion audit's batch-013 decisions ([ADR-047](record/decisions.d/ADR-047.md)),
  under the owner's rule that a checked re-derivation meets a promotion
  condition that asks for a proof.
