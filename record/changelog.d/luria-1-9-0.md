### Changed

- CI pins luria 1.9.0, up from 1.7.0. 1.8.0 adds an opt-in `luria repair --prune_stale` and a `repair:` table in `luria.yaml` for repair flags, both off unless set. 1.9.0 renders `docs/record.md` from a template, leaves out a section with nothing to show, and adds a warn-first `undescribed-schemes` lint class. This record's schemes all describe themselves, so the class does not fire here, and `docs/record.md` now gains its "What each family is" section.
