### Added

- [CASE-351](record/cases.d/CASE-351.md) (executed-study, documented, Proposed), carrying out
  [LEAD-052](record/leads.d/LEAD-052.md): a depth-3 tree whose levels carry input and target strengths
  set independently, trained by exact kernel flow, NTK-parametrized ReLU
  networks of width 64 to 4096, deep linear networks of two and three
  layers, and two-layer ReLU networks from small and order-one scale.
  Code, tests and results under scratch/studies/lead-052/.
- [CLAIM-929](record/claims.d/CLAIM-929.md) (Proposed, thesis, demonstrated): on tree-symmetric data
  every kernel of inner products and norms commutes with the level
  projectors, so kernel flow orders the levels by input strength alone,
  while a decoupled deep linear network orders them by input times target
  strength; neither order is set by tree depth.
- [CLAIM-930](record/claims.d/CLAIM-930.md) (Proposed, thesis, empirical): a small two-layer ReLU
  network from small scale keeps the deep linear direction with its spread
  of acquisition times compressed; in NTK parametrization the dependence
  on target strength vanishes between width 256 and 1024.

### Changed

- Dated notes of 2026-11-22 on [QUESTION-217](record/questions.d/QUESTION-217.md), [QUESTION-039](record/questions.d/QUESTION-039.md) and [LEAD-052](record/leads.d/LEAD-052.md);
  [LEAD-052](record/leads.d/LEAD-052.md) gains `operationalized_in: CASE-351`. No status, title or
  stage changed.
