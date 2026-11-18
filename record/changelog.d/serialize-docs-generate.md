### Changed

- Docs runs on pushes to the default branch now wait for one another
  ([ADR-105](record/decisions.d/ADR-105.md)): two merges minutes apart no longer start
  two generate runs that race and leave main's views stale.
