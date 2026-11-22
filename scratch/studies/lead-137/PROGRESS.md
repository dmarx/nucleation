# LEAD-137 progress

- Lead: LEAD-137 — Check on a non-lattice system of coupled agents whether
  variables chosen for informativeness across a buffer match the gap-isolated block.
- Branch: claude/lead-137-informative-gap-isolated (cut from origin/staging).
- Advances: QUESTION-065, CLAIM-157.

## Task as understood

In a NON-lattice coupled-agent linear stochastic system (modular/random
coupling graph), for a region R separated from a far environment E by a
buffer B, compute:
  (1) the "informative-across-buffer" variable: the direction in R whose
      coarse variable carries the most information about the far environment
      E (top canonical-correlation direction of (x_R, x_E) under the
      stationary covariance Sigma), per QUESTION-065 / THEORY-205 (leading
      transfer-matrix eigenvector) / THEORY-198.
  (2) the "gap-isolated block" variable (CLAIM-157): R's slow collective
      mode, the leading eigenvector of the dynamics restricted to R (A_RR),
      the projector onto the block's joint mode (CLAIM-164).
Compare alignment across a range of systems (symmetric vs asymmetric
coupling, modularity, coupling strength, buffer width, seeds). Match extends
QUESTION-065's lattice result; divergence in a local system bounds CLAIM-157.

## Done
- Read CLAUDE.md, design principles, ADR-001, ADR-048, run-lead skill, lead,
  QUESTION-065, CLAIM-157, CASE-045, docs/record.md fields.
- Step 1: target not already held. CASE-tmpwyp15 (LEAD-083) tests
  compensation/entrainment/block-test in a phi4 lattice + Kuramoto; it does
  NOT compute informativeness-across-buffer. CASE-tmpfktyl is Game of Life.
  No executed study computes the informative-across-buffer vs gap-isolated
  comparison.

## Next
- Write study script (numpy/scipy, python3 -I) + pytest.
- Run across systems, persist per-item JSONL.
- File CASE (executed-study) + CLAIM(s) + lead note + changelog.

## Choices made
- Model: linear Gaussian VAR(1) on a modular graph (communities on a path,
  random within a community -> non-lattice). Stationary cov Sigma via
  discrete Lyapunov. Informativeness = equal-time MI (CCA); gap-isolated
  block = slow mode of dynamics. Rationale in script README.
