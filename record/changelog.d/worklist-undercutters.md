### Fixed

- The status-review worklist reads an argument's undercutters from the
  claims that carry `undercuts`. It had read `undercut_by`, which is
  derived and never stored, so a sound argument a held claim undercuts
  ([ARG-006](record/arguments.d/ARG-006.md), undercut by [CLAIM-011](record/claims.d/CLAIM-011.md) and [CLAIM-253](record/claims.d/CLAIM-253.md)) stayed listed in a section
  that must be empty. A test fires the case.
