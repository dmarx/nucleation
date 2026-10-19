### Changed

- [CLAIM-267](record/claims.d/CLAIM-267.md) (per-step errors compound through later sensitivity) and
  [CLAIM-270](record/claims.d/CLAIM-270.md) (retention and drift are different properties) are promoted
  to Active, carrying out the promotion audit's batch-001 decisions
  (ADR-047). [CLAIM-267](record/claims.d/CLAIM-267.md)'s indices are pinned to one map, with exact
  witnesses for each regime. [CLAIM-270](record/claims.d/CLAIM-270.md) gains two-state constructions for
  all four combinations of retention and drift.
