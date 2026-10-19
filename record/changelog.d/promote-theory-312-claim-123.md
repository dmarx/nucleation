### Changed

- [THEORY-312](record/theory.d/THEORY-312.md) is promoted to Active. The large-batch InfoNCE loss is
  −HSIC(Z,Y) plus a nonnegative log-mean-exp, and Theorem B.1's remainder
  enters with a plus sign. Both are re-derived in a dated note, which
  settles the sign question its promotion condition asked about.
- [CLAIM-123](record/claims.d/CLAIM-123.md) is promoted to Active. It was reviewed again as demonstrated
  after its correction in [#165](https://github.com/dmarx/nucleation/issues/165): score addition composes conditions
  exactly when the conditional dependence ratio does not vary with x.
- Both carry out the promotion audit's batch-014 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
  Stale inactive-ok entries naming either code are trimmed.
