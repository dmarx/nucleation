### Changed

- Docs runs on pushes to the default branch now wait for one another
  ([ADR-tmp095uh](record/decisions.d/ADR-tmp095uh.md)): two merges minutes apart no longer start
  two generate runs that race and leave main's views stale.
