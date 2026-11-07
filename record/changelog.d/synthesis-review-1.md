### Added

- A periodic synthesis review, [ADR-078](record/decisions.d/ADR-078.md) (Proposed), carried by the new `synthesis-review` skill. Its first stage is mechanical: `scratch/formal/synthesis_candidates.py` ranks CLAIMs that may be syntheses filed as claims, and integrations the record holds only as parts (`complements` clusters, open questions with several answers, deep `rests_on` chains), and decides nothing. A reviewer then shortlists, audits each candidate with [ADR-075](record/decisions.d/ADR-075.md)'s checks and routes, and files only what is admitted. No synthesis is set Current.
- The first review, its demonstration. It audited twelve candidates:
  - [CLAIM-545](record/claims.d/CLAIM-545.md), A's freedom-of-will synthesis, is moved into the scheme as [SYNTHESIS-007](record/syntheses.d/SYNTHESIS-007.md) (admitted by hypothesis, four corrections marked), and [SYNTHESIS-002](record/syntheses.d/SYNTHESIS-002.md) and [SYNTHESIS-004](record/syntheses.d/SYNTHESIS-004.md) are repointed to it.
  - [SYNTHESIS-008](record/syntheses.d/SYNTHESIS-008.md), in the assistant's voice, answers part of [QUESTION-131](record/questions.d/QUESTION-131.md) by derivation: a met-or-quiet complex, which is neither the requirement complex nor the quiescent complex, decides when structural frustration forces a member that is unmet and acting.
  - [CLAIM-474](record/claims.d/CLAIM-474.md) is admitted, but stays an Active CLAIM until the owner decides whether to move it.
  - Nine candidates were not admitted, each with its reason.

  The curation entry "Synthesis review of 2026-11-07" holds the ranking, the verdicts and the lines still without a synthesis.

### Changed

- The current-account template keeps the blank line after a synthesis's status line.
- [CLAIM-545](record/claims.d/CLAIM-545.md) is Superseded by [SYNTHESIS-007](record/syntheses.d/SYNTHESIS-007.md).
