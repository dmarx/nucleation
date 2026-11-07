### Added

- ADR-tmptu1vn (Proposed): a SYNTHESIS scheme for the record's integrations of its own entries. Its statuses (Current, Proposed, Unadmitted, Rejected, Superseded) are about the integration, not its components. It has a required admission `route` (hypothesis, derived, integration), and `integrates` and `premises` relations whose targets' standing is derived, never copied.
- A generated current-account view, `docs/current-account.md`, from `record/views.d/current-account.md.j2`. It sets out every Current or Proposed synthesis by line, with each component's live status.
- The five syntheses admitted from "Individuation, Possibility, and Disposition" are moved into the scheme as the demonstration (SYNTHESIS-tmpg2eh2, SYNTHESIS-tmpj2lnj, SYNTHESIS-tmp46moy, SYNTHESIS-tmprmcy0, SYNTHESIS-tmp73anp); their CLAIMs are Superseded by them.

### Changed

- CLAIM's `superseded_by` accepts a SYNTHESIS.
- The `read-and-file` skill's step 9b files an admitted synthesis as a SYNTHESIS.
