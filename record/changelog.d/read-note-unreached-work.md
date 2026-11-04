### Added

- Three lint checks, `read_but_unreached`, `read_but_unfetched` and `read_but_unreviewed`, fail on a `Read` note whose work is marked `Unavailable`, `Unfetched` or `Deferred` ([ADR-tmpr8ui6](record/decisions.d/ADR-tmpr8ui6.md)). A `Skimmed` note on such a work is allowed. There are no matches today.
