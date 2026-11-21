### Added

- Three alternative decisions, all Proposed, answering the owner's worry that [ADR-075](record/decisions.d/ADR-075.md)'s language discourages documenting useful syntheses. The owner chooses one:
  - [ADR-131](record/decisions.d/ADR-131.md) (A, the assistant's lean): the test only decides whether a synthesis also yields a claim, and a synthesis that organizes held components is filed as an account either way.
  - [ADR-134](record/decisions.d/ADR-134.md) (B): the same, for the owner's syntheses only.
  - [ADR-133](record/decisions.d/ADR-133.md) (C): no test at filing; the synthesis review tests it.
- The owner chose A on pull request 594. B and C are Rejected, kept as alternatives not taken. The `read-and-file` skill now files a synthesis's map as an account whether or not it yields a claim, and leaves only a recap in the curation entry. [ADR-075](record/decisions.d/ADR-075.md) and [ADR-084](record/decisions.d/ADR-084.md) take history notes.
