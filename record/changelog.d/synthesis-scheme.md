### Added

- [ADR-076](record/decisions.d/ADR-076.md) (Proposed): a SYNTHESIS scheme for the record's integrations of its own entries. Its status (Current, Proposed, Rejected, Superseded) is about the integrating account; whether it earned an entry is a separate `admission` field (admitted, unadmitted). It has a required admission `route` (hypothesis, derived, integration), and `integrates` and `premises` relations whose targets' standing is derived, never copied.
- A generated current-account view, `docs/current-account.md`, from `record/views.d/current-account.md.j2`. It sets out every Current or Proposed synthesis by line, with each component's live status.
- The five syntheses admitted from "Individuation, Possibility, and Disposition" are moved into the scheme as the demonstration ([SYNTHESIS-003](record/syntheses.d/SYNTHESIS-003.md), [SYNTHESIS-004](record/syntheses.d/SYNTHESIS-004.md), [SYNTHESIS-001](record/syntheses.d/SYNTHESIS-001.md), [SYNTHESIS-005](record/syntheses.d/SYNTHESIS-005.md), [SYNTHESIS-002](record/syntheses.d/SYNTHESIS-002.md)); their CLAIMs are Superseded by them.

### Changed

- CLAIM's `superseded_by` accepts a SYNTHESIS, and ARG's `concludes` does too, with `argued_by` as its converse. The two ARGs that concluded the moved claims now conclude their syntheses.
- The `read-and-file` skill's step 9b files an admitted synthesis as a SYNTHESIS.
- Five lint rules, in `lint.fail_on`, enforce what the SYNTHESIS fields cannot say:
  - premises within integrates, for claim and synthesis premises;
  - a Current synthesis resting only on what is in force or adopted;
  - derived meaning demonstrated.

  `scratch/formal/synthesis_fixture.py` fires each rule on a throwaway record and checks the view.
- The view gives each component's kind, and shows only admitted syntheses. CASE's `illustrates` accepts a SYNTHESIS. The ARGs and the case that described the current account now point to the syntheses.
- [ADR-076](record/decisions.d/ADR-076.md), version 3: a Current synthesis must be admitted, and an unadmitted one may not keep a `route`. A `supposed` synthesis, whose adoption adopts a conditional account, is exempt from the premise-status rules and labelled conditional in the view. The fixture covers all three.
