### Added

- ADR-057 (Proposed): status review is ranked by reliance, derived from
  the record on each pass, covers relations as well as statuses, and makes
  its changes in the pull request that decides them. It proposes five lint
  forcing functions against a repeat of the backlog.
- `record/status-review/worklist.py`, with tests: load-bearing Proposed
  entries, credence inversions, retired premises, Open questions with an
  Active answer, and unblocked Proposed claims.
- CLAIM-tmpnp8w6: a reply to CLAIM-089 on CLAIM-434's result.
- TERM-tmppwzer: inquiry, as (Σ, A, 𝓘, 𝓞, 𝓚, 𝓑).

### Changed

- `stale_days: 14`. The default of 90 could not name a stale document in
  a record a month old.
- CLAIM-365 `complements` CLAIM-347 instead of resting on it.
  CLAIM-159 `objects_to` CLAIM-024. CLAIM-470 and CLAIM-475 use the new
  TERM.
- The workbench entry of 2026-10-27 records the pass.
