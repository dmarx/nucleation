### Added

- Two lint checks, `read_but_unreached` and `read_but_unfetched`, fail on a `Read` note whose work is marked `Unavailable` or `Unfetched` ([ADR-068](record/decisions.d/ADR-068.md)). A `Skimmed` note on such a work is allowed. There are no matches today.
