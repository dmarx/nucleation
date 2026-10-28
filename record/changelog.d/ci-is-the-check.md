### Changed

- Work is pushed to its pull request as it is made, and the pull request's `docs-check` job does the repair and the lint ([ADR-054](record/decisions.d/ADR-054.md), Active, at the owner's direction). Contributors no longer run `luria repair`, `link --fix`, `index` or `lint` as a gate before pushing; `luria new` stays local, a red check is fixed on the branch, and a narrow local command is still fine for diagnosing. CLAUDE.md's "Working" section and its rule on link targets say so.
