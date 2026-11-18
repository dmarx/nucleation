### Changed

- Docs runs on pushes to the default branch now wait for one another
  (ADR-tmp095uh): two merges minutes apart no longer start
  two generate runs that race and leave main's views stale.
