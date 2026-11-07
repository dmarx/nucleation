### Added

- ADR-tmpe7y42 (Proposed): a synthesis in a filed source is audited and, when it integrates, filed as a thesis claim with its components mapped, instead of being mapped to its source turns and left. The audit checks attribution, coverage, fidelity, standing and integration; the latest version of each distinct proposed or supposed thesis becomes one Proposed CLAIM, revised in place when the account returns.
- The `read-and-file` skill's step 9b carries it, and the curation entry gains a "Syntheses audited" section.

### Changed

- ADR codes are now minted as temporary codes and numbered at merge (`allocate: merge` in `luria.yaml`), like the record's other schemes. ADRs were the one scheme still numbered at filing, which is why this decision was first filed as ADR-075.
