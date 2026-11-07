### Changed

- [ADR-tmp39arf](record/decisions.d/ADR-tmp39arf.md) (Proposed): the Pages site deploys at most once every two hours. A merge still triggers the workflow. A new `gate` job skips the build when the last deploy to `github-pages` is under two hours old, or already published the commit. A scheduled run every two hours publishes what was skipped, and a manual run always builds.
