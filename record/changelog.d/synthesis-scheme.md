### Added

- [ADR-tmptu1vn](record/decisions.d/ADR-tmptu1vn.md) (Proposed): a SYNTHESIS scheme for the record's integrations of its own entries. Its statuses (Current, Proposed, Unadmitted, Rejected, Superseded) are about the integration, not its components. It has a required admission `route` (hypothesis, derived, integration), and `integrates` and `premises` relations whose targets' standing is derived, never copied.
- A generated current-account view, `docs/current-account.md`, from `record/views.d/current-account.md.j2`. It sets out every Current or Proposed synthesis by line, with each component's live status.
- The five syntheses admitted from "Individuation, Possibility, and Disposition" are moved into the scheme as the demonstration ([SYNTHESIS-tmpg2eh2](record/syntheses.d/SYNTHESIS-tmpg2eh2.md), [SYNTHESIS-tmpj2lnj](record/syntheses.d/SYNTHESIS-tmpj2lnj.md), [SYNTHESIS-tmp46moy](record/syntheses.d/SYNTHESIS-tmp46moy.md), [SYNTHESIS-tmprmcy0](record/syntheses.d/SYNTHESIS-tmprmcy0.md), [SYNTHESIS-tmp73anp](record/syntheses.d/SYNTHESIS-tmp73anp.md)); their CLAIMs are Superseded by them.

### Changed

- CLAIM's `superseded_by` accepts a SYNTHESIS, and ARG's `concludes` does too, with `argued_by` as its converse. The two ARGs that concluded the moved claims now conclude their syntheses.
- The `read-and-file` skill's step 9b files an admitted synthesis as a SYNTHESIS.
