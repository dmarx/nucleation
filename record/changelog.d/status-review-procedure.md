### Changed

- **Status-review worklist reordered ([ADR-057](record/decisions.d/ADR-057.md) version 6).** The sections that
  must be empty come first, now including stale converses (a Proposed reading
  still supporting an Active claim). Then the work: claims ready for a ruling
  (unblocked and not held by a recent blocker note), grouped by line; sole
  blockers, the unheld premises ranked by how many claims each alone holds
  back; blocker notes a premise has changed since; and readings no source of
  which is read in full. Reach, which had flattened to 1, is printed last.

### Added

- `record/status-review/README.md`: how a pass is run, from building the
  worklist to landing the pull request, including [ADR-047](record/decisions.d/ADR-047.md)'s routing of a
  narrowing's dropped clauses. It replaces briefs kept outside the record.
