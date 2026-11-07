### Added

- [ADR-tmpe7y42](record/decisions.d/ADR-tmpe7y42.md) (Proposed): a synthesis in a filed source is audited and, when it integrates, filed as a thesis claim with its components mapped, instead of being mapped to its source turns and left. The audit checks attribution, coverage, fidelity, standing and integration; the latest version of each distinct proposed or supposed thesis becomes one Proposed CLAIM, revised in place when the account returns.
- The `read-and-file` skill's step 9b carries it, and the curation entry gains a "Syntheses audited" section.

### Changed

- ADR codes are now minted as temporary codes and numbered at merge (`allocate: merge` in `luria.yaml`), like the record's other schemes. ADRs were the one scheme still numbered at filing, which is why this decision was first filed as ADR-075.
- [ADR-071](record/decisions.d/ADR-071.md), version 2: a decision goes with a demonstration of its effects, in the same pull request, so it is approved by what it does and git blame leads from it to what it changed. CLAUDE.md says so. The synthesis audit is the first instance: first opened alone as dmarx/nucleation#423, then folded into the filing that applies it.
- [ADR-tmpe7y42](record/decisions.d/ADR-tmpe7y42.md), version 2, at A's review of the pull request as the owner refined it: a synthesis is filed only if a stated case has every component hold and the integration false. Applied to the six synthesis CLAIMs: five admitted, four on narrower titles, and the dispositional reframing not admitted. The skill's ARG rule is narrowed to load-bearing or contested support.
- ADR-tmpe7y42, versions 3 and 4, at A's second review and the owner's direction: three admission routes (independent hypothesis, derived result, explanatory integration), each with its own test; a synthesis that passes none and has not merged is withdrawn before merge, its text and audit kept in the curation entry, since not admitted is not refuted. The dispositional reframing is the first so withdrawn.
