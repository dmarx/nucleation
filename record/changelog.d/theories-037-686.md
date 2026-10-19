### Changed

- [THEORY-037](record/theory.d/THEORY-037.md) is promoted to Active. The record re-derives that the clopen
  sub-objects of the spectral presheaf form a complete Heyting algebra,
  that its negation is the source's pseudo-complement, and that excluded
  middle fails in the ℂ² case. This carries out the promotion audit's
  batch-009 decision under [ADR-047](record/decisions.d/ADR-047.md) v2.

### Fixed

- [THEORY-686](record/theory.d/THEORY-686.md) said the observations without generative effects are exactly
  the left adjoints. Having no generative effect is weaker than preserving
  all joins: the constant map to the top has none, and is not a left
  adjoint. The title now says "preserve all joins", with two
  counterexamples. With the record's re-derivations of Prop. 1.111 and
  Thm 1.115, the corrected account is promoted to Active (batch 009,
  [ADR-047](record/decisions.d/ADR-047.md) v2).
