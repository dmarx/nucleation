### Added

- [ADR-047](record/decisions.d/ADR-047.md): the promotion audit runs in small, persisted batches, ranked
  by expected yield, with decisions recorded apart from status changes.
- `record/promotion-audit/`: the audit's versioned queue with a hand-off
  block, one decision file per reviewed candidate, batch files, working
  notes, and `check.py`, which fails when the queue and the decisions
  disagree. Batch 001 reviewed five demonstrated CLAIMs. [CLAIM-267](record/claims.d/CLAIM-267.md) and
  [CLAIM-270](record/claims.d/CLAIM-270.md) are to be promoted, [CLAIM-285](record/claims.d/CLAIM-285.md) split, and [CLAIM-077](record/claims.d/CLAIM-077.md) and
  [CLAIM-098](record/claims.d/CLAIM-098.md) have misclassified warrants. No status changes here.
