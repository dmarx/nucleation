### Added

- ADR-tmpkc4c4: an entry's title is a short address (30 to 50 characters as a
  target, no code), and its full assertion lives in a new `statement:`
  field on CLAIM, THEORY, ARG, SYNTHESIS, CASE and TERM.

### Changed

- 162 TERMs are retitled to the term itself, with a sense in parentheses
  where several TERMs share a term. Each old title is kept verbatim in
  `statement:`. The other 17 TERMs already had short titles and are unchanged.
