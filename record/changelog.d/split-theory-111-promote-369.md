### Added

- [THEORY-732](record/theory.d/THEORY-732.md), Active: for ReLU networks on a linear path, weak
  additivity and commutativity at every layer give exact layerwise
  linear feature connectivity, output linearity bounds the path's error
  by twice the endpoints', and one hidden layer with interpolating minima
  gives the exact case. Split from [THEORY-111](record/theory.d/THEORY-111.md).

### Changed

- [THEORY-369](record/theory.d/THEORY-369.md), Active, narrowed to a fixed number of points and clusters of
  at least two: as dimension grows, an optimal nearest-neighbour search
  must read every such cluster, with probability tending to 1. The record's
  concentration proof is written in.
- [THEORY-111](record/theory.d/THEORY-111.md) stays Proposed for its empirical regularity and the step to
  many-model averages, and now extends [THEORY-732](record/theory.d/THEORY-732.md). These changes carry
  out the promotion audit's batch-016 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
