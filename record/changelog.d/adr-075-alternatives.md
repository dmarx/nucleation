### Added

- Three alternative decisions, all Proposed, answering the owner's worry that [ADR-075](record/decisions.d/ADR-075.md)'s language discourages documenting useful syntheses. The owner chooses one:
  - [ADR-tmpi2grj](record/decisions.d/ADR-tmpi2grj.md) (A, the assistant's lean): the test only decides whether a synthesis also yields a claim, and a synthesis that organizes held components is filed as an account either way.
  - [ADR-tmpoxu5i](record/decisions.d/ADR-tmpoxu5i.md) (B): the same, for the owner's syntheses only.
  - [ADR-tmpkiuac](record/decisions.d/ADR-tmpkiuac.md) (C): no test at filing; the synthesis review tests it.
- The owner chose A on pull request 594. B and C are Rejected, kept as alternatives not taken. The `read-and-file` skill now files a synthesis's map as an account whether or not it yields a claim, and leaves only a recap in the curation entry. ADR-075 and ADR-084 take history notes.
