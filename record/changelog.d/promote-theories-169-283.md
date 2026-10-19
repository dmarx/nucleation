### Added

- [QUESTION-159](record/questions.d/QUESTION-159.md): whether an exact train-then-predict identity holds
  for further sequence-layer classes, or is bounded by some standard
  attention layer. It holds [THEORY-169](record/theory.d/THEORY-169.md)'s former scope test, unchanged.
- [QUESTION-158](record/questions.d/QUESTION-158.md): whether gradient descent, without a spectral
  initialization, reaches the hierarchical multi-index thresholds, and
  whether they survive a second input law. It holds [THEORY-283](record/theory.d/THEORY-283.md)'s former
  promote_when, unchanged, and refines [QUESTION-039](record/questions.d/QUESTION-039.md).

### Changed

- [THEORY-169](record/theory.d/THEORY-169.md), Active after narrowing: for unnormalized causal linear
  attention and for softmax attention, conditioning on a context is a
  learner's train-then-predict step. The three identities are re-derived.
- [THEORY-283](record/theory.d/THEORY-283.md), Active after narrowing: the sample-size thresholds and rates
  are stated for the Bayes-optimal and spectral estimators and for a
  network with a spectral first layer, not for gradient descent. These
  changes carry out the promotion audit's batch-024 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
