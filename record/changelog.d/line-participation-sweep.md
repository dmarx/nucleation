### Changed

- [ADR-085](record/decisions.d/ADR-085.md) version 2: an entry takes the first line of each entry it answers, objects to or bears on, and of each question it refines. The rule is applied in one step. A line the target carries second does not pass, nothing cascades, and a term that refines a term takes no line.
- The record-wide sweep under that rule:
  - 35 entries gain 36 lines, each with a version bump and a history note naming the relation and the entry whose first line it is.
  - [CLAIM-611](record/claims.d/CLAIM-611.md) no longer carries formal-apparatus, and [CLAIM-621](record/claims.d/CLAIM-621.md) carries learned-structure in place of distributed-agency. The first sweep, ADR-085's demonstration in [#447](https://github.com/dmarx/nucleation/issues/447), had given them lines that their questions carry second.
  - [CLAIM-534](record/claims.d/CLAIM-534.md) is left out. Its `bears_on` QUESTION-255 marks what it does not claim, and the fix is for the owner.
