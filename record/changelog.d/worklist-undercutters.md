### Fixed

- The status-review worklist reads an argument's undercutters from the
  claims that carry `undercuts`. It had read `undercut_by`, which is
  derived and never stored, so a sound argument a held claim undercuts
  (ARG-006, undercut by CLAIM-011 and CLAIM-253) stayed listed in a section
  that must be empty. A test fires the case.
