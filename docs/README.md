# Docs

- [Reading list](literature/README.md) — one note per work, with its standing in this record.
- [Readings](notes/README.md) — close readings, one per work actually read.
- [Accounts](theory/README.md) — claims about what is true, each with its evidence.
- [Lines of work](lineage.md) and [lines of explanation](theory-lines.md) — the relations between works and between accounts.
- [Curation log](curation/README.md) — why things entered this record, and why they left.
- [Decisions](decisions/README.md) — choices, with their alternatives.
- [Design principles](design-principles.md) — standing values, numbered.
- [Development log](devlog/README.md) — the narrative, one book per month.
- [The record](record.md) — what this project's record is made of and where each kind of entry is filed, generated from `luria.yaml`. Read it before assuming this record can only hold decisions: schemes, journals, fragment directories and remotes are families *this* project names.

Each of these is **generated** — run `luria index`. The list above is
[written by `luria init` from this project's own
`luria.yaml`](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-048.md),
so it names the views this record actually renders; edit it freely
afterwards, it is yours. This directory is for
*reading*; filing happens in `record/`, whose `.d`-suffixed containers hold
the sources ([LU-ADR-021](https://github.com/dmarx/luria/blob/main/record/decisions.d/ADR-021.md)).
Never edit an assembled page — the lint refuses hand edits, and anything in a
view directory the generator didn't write is an error.

Every other page in this directory must be linked from here; `luria lint`
fails otherwise, because an index that silently stops covering the directory
is worse than no index. View directories are exempt: they carry their own
generated indexes.
