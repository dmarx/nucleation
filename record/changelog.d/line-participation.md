### Added

- ADR-tmpk61vy (Proposed): an entry carries every line whose argument it takes part in, meaning a line it answers, refines, objects to or bears on through one of that line's entries. Resting on or using another line's entry is a dependency, still reported as a crossing, and `complements` alone adds no line. ADR-082's rule for the nucleating-argument split is this rule applied to a split.

### Changed

- Eleven claims that bear on a question of another line now carry that line, each with a history note: CLAIM-532, 544, 549, 553, 554, 586, 611, 613, 615, 619 and 621. This clears 12 of the 79 `rests_on` crossings the lint reported; the other 67 are dependencies across lines.
