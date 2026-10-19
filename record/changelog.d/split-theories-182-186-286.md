### Added

- [THEORY-739](record/theory.d/THEORY-739.md), Active: for word2vec's quartic proxy with tied weights
  and symmetric reweighting, the rank-d minimisers are the top eigenvectors
  of M*, and from an aligned start each is acquired in a logistic rise, in
  order of eigenvalue. Split from [THEORY-182](record/theory.d/THEORY-182.md), re-derived.
- [THEORY-740](record/theory.d/THEORY-740.md), Active: a two-layer linear network from a decoupled,
  balanced start learns its correlation's singular modes one at a time in
  order of strength, while one layer learns them all on one timescale.
  Split from [THEORY-186](record/theory.d/THEORY-186.md), re-derived.
- [THEORY-738](record/theory.d/THEORY-738.md), Active: the unconstrained-features max-margin geometry
  under step imbalance is simplex-encoded-label interpolation, and the
  simplex ETF only for balanced or binary data. Split from [THEORY-286](record/theory.d/THEORY-286.md),
  re-derived by a dual certificate.

### Changed

- [THEORY-182](record/theory.d/THEORY-182.md), [THEORY-186](record/theory.d/THEORY-186.md) and [THEORY-286](record/theory.d/THEORY-286.md) extend the new entries and keep
  their unproved parts, Proposed, with their promote_whens unchanged. These
  changes carry out the promotion audit's batch-024 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
