### Changed

- **Worklist: concessions** ([ADR-057](record/decisions.d/ADR-057.md) v4). The section now reads every Active
  objection, not only `role: granted` ones, so counters that went Active when
  conceded ([CLAIM-222](record/claims.d/CLAIM-222.md), [CLAIM-226](record/claims.d/CLAIM-226.md), [CLAIM-243](record/claims.d/CLAIM-243.md), [CLAIM-071](record/claims.d/CLAIM-071.md)) are listed. A target
  filed with the concession already in its text says so under a fixed note
  heading, "filed with its concessions", instead of a version bump.
- **Worklist: live objections.** An Active objection written into its target
  no longer counts as live, so a narrowed claim can show as unblocked.
