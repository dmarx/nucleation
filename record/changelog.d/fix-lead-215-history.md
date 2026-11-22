### Changed

- [LEAD-215](record/leads.d/LEAD-215.md) gains the `history:` its version 4 requires ([ADR-019](record/decisions.d/ADR-019.md)): one entry for each of the three dated reading notes that raised its version. Its absence failed lint on main after the Promote run of 2026-11-22 and so skipped Promote's back-merge into staging.
