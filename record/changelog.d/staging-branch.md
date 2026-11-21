<!-- inactive-ok-file: ADR-tmpwe08z — Proposed; this contribution of 2026-11-21 -->
### Added

- A `staging` branch and a Promote workflow (ADR-tmpwe08z, at the owner's
  request): work merges into staging through pull requests, and Promote
  merges staging into main nightly or on demand, concretizing the batch's
  temporary codes at once and merging main back into staging.

### Changed

- ADR-071: branches are cut from staging and pull requests target it.
  CLAUDE.md's working section says so. The stack of pull requests 558 to 563
  folded into staging as the first application.
