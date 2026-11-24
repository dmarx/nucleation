### Fixed

- SYNTHESIS-124's history listed version 3 before version 2, so lint read
  it as ending at version 2 and failed docs-lint on main after the
  promotion of 2026-11-23; that failure skipped the back-merge into
  staging. The history now runs oldest first, as elsewhere. The skipped
  back-merge was done by hand (staging fast-forwarded to main).
