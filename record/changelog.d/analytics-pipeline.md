### Added

- `scratch/formal/analytics/`: an Apache Hamilton dataflow for the record's derived numbers, at the owner's suggestion of 2026-11-21. It computes record snapshot counts, the decision census tables and agreement, the term-change audit, growth snapshots and the rate studies. Each run writes one JSON dated by the commit it read. It also reports how many decisions the census has not yet coded, so staleness shows. Tests reproduce the manuscript's figures at the commits it read. No CI workflow runs it yet.
