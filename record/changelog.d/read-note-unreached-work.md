### Added

- Three lint checks, `read_but_unreached`, `read_but_unfetched` and `read_but_unreviewed`, fail on a `Read` note whose work is marked `Unavailable`, `Unfetched` or `Deferred` ([ADR-068](record/decisions.d/ADR-068.md)). A `Skimmed` note on such a work is allowed. There are no matches today.
