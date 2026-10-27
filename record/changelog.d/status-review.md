### Added

- [ADR-057](record/decisions.d/ADR-057.md) (Proposed): status review is ranked by reliance, derived from
  the record on each pass, covers relations as well as statuses, and makes
  its changes in the pull request that decides them. It proposes five lint
  forcing functions against a repeat of the backlog.
- `record/status-review/worklist.py`, with tests: load-bearing Proposed
  entries, credence inversions, retired premises, Open questions with an
  Active answer, and unblocked Proposed claims.
- [CLAIM-tmpnp8w6](record/claims.d/CLAIM-tmpnp8w6.md): a reply to [CLAIM-089](record/claims.d/CLAIM-089.md) on [CLAIM-434](record/claims.d/CLAIM-434.md)'s result.
- [TERM-tmppwzer](record/terms.d/TERM-tmppwzer.md): inquiry, as (Σ, A, 𝓘, 𝓞, 𝓚, 𝓑).

### Changed

- `stale_days: 14`. The default of 90 could not name a stale document in
  a record a month old.
- [CLAIM-365](record/claims.d/CLAIM-365.md) `complements` [CLAIM-347](record/claims.d/CLAIM-347.md) instead of resting on it.
  [CLAIM-159](record/claims.d/CLAIM-159.md) `objects_to` [CLAIM-024](record/claims.d/CLAIM-024.md). [CLAIM-470](record/claims.d/CLAIM-470.md) and [CLAIM-475](record/claims.d/CLAIM-475.md) use the new
  TERM.
- The workbench entry of 2026-10-27 records the pass.
