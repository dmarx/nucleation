### Changed

- [ADR-079](record/decisions.d/ADR-079.md) (Proposed): each directed relation is stored on one side only, the side a filer writes, and its converse is derived when the record is read. `luria.yaml` marks 32 converse fields `derived` across the nineteen directed pairs. Symmetric relations are unchanged. CI's `luria repair` on this pull request removes the stored converses and moves onto the primary side the 129 values that existed only on the converse side.
- The TERM template points supersession at `superseded_by` on the replaced term. The `synthesis-review` skill no longer asks for `corroborated_by` to be carried.

### Fixed

- [LIT-862](record/literature.d/LIT-862.md), [LIT-863](record/literature.d/LIT-863.md), [LIT-1542](record/literature.d/LIT-1542.md) and [LIT-1171](record/literature.d/LIT-1171.md) named old-style codes in `extended_by` for [LIT-860](record/literature.d/LIT-860.md), [LIT-002](record/literature.d/LIT-002.md) and [LIT-048](record/literature.d/LIT-048.md).
