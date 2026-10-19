### Added

- [QUESTION-157](record/questions.d/QUESTION-157.md): whether factored-process results replicate on other
  generator families or objectives, and what loss gap the factored
  representation pays when noise makes it lossy. It holds [THEORY-256](record/theory.d/THEORY-256.md)'s
  former promote_when, unchanged, and refines [QUESTION-060](record/questions.d/QUESTION-060.md).

### Changed

- [THEORY-256](record/theory.d/THEORY-256.md), Active after narrowing: the lossless per-factor embedding of
  a tensor-product generator's predictive state, re-derived, together with
  what [LIT-986](record/literature.d/LIT-986.md) measured. That is 4-layer GPT-2-style transformers on five
  Mess3 and Bloch Walk factors, settling near the factored dimension in
  linearly independent subspaces that are approximately orthogonal in their
  leading components, and reaching it first under the token noise tested.
  It is promoted on one study read in full under [ADR-047](record/decisions.d/ADR-047.md) v3, carrying out
  the promotion audit's batch-019 decision.
