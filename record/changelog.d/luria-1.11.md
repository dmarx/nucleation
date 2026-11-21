### Changed

- CI pins luria 1.11.0, up from 1.10.0, at the owner's go of 2026-11-21 on the first recommendation of the retrospective of that day. 1.11.0's `luria new` refuses a title that cites a code, with a message saying why. A code in a title had failed docs-check four times that day, because the repair links the code in the body heading and not in `title:`. A code in backticks is a mention and passes. Nothing else changed between the two releases, apart from a commented-out note in luria's CLAUDE.md template, so the record's checks are otherwise unchanged.
