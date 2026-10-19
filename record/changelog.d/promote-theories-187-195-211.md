### Added

- [QUESTION-166](record/questions.d/QUESTION-166.md): whether the depth law of deep linear networks holds
  from starts off the decoupled set, such as random orthogonal weights. It
  holds [THEORY-187](record/theory.d/THEORY-187.md)'s former promote_when, unchanged, and refines
  [QUESTION-039](record/questions.d/QUESTION-039.md).
- [QUESTION-165](record/questions.d/QUESTION-165.md): whether the number of examples a deep network needs on
  the Random Hierarchy Model is set by the detectability of patch–label
  correlations or by the grammar's size. It holds [THEORY-195](record/theory.d/THEORY-195.md)'s former
  promote_when, unchanged.
- [QUESTION-164](record/questions.d/QUESTION-164.md): whether the law of balance holds in a deep network
  trained on real data. It holds [THEORY-211](record/theory.d/THEORY-211.md)'s former promote_when,
  unchanged, and refines [QUESTION-069](record/questions.d/QUESTION-069.md).

### Changed

- [THEORY-187](record/theory.d/THEORY-187.md), Active after narrowing: the depth law of deep linear networks
  is stated for whitened inputs and decoupled, balanced starts, with
  iterations counted at the stable step size. The finite-depth plateau
  exponent and the iteration count are re-derived.
- [THEORY-195](record/theory.d/THEORY-195.md), Active after narrowing under [ADR-047](record/decisions.d/ADR-047.md) v3: what the Random
  Hierarchy Model experiments measured, in the range they cover. The
  attribution of the sample size to correlation detection moves to a
  QUESTION.
- [THEORY-211](record/theory.d/THEORY-211.md), Active after narrowing: the law of balance in the SDE model
  of SGD, whenever both groups carry noise, re-derived by Itô's lemma.
  These changes carry out the promotion audit's batch-027 decisions
  ([ADR-047](record/decisions.d/ADR-047.md)).
