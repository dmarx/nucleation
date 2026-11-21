### Changed

- ADR-127 version 3, at the owner's request: a scheduled check-in that finds
  nothing doubles the next interval and stops after three empty, saying
  nothing; an alternative reading applies the back-off to quiet event
  turns.
