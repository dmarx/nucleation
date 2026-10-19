### Added

- [QUESTION-tmpavq90](record/questions.d/QUESTION-tmpavq90.md): whether a coarse-graining short of full capture keeps
  longer-range couplings bounded by the information lost, in two or more
  dimensions. It holds [THEORY-198](record/theory.d/THEORY-198.md)'s former promote_when, unchanged, and
  refines [QUESTION-065](record/questions.d/QUESTION-065.md).
- [QUESTION-tmpgpocu](record/questions.d/QUESTION-tmpgpocu.md): whether a lossy-compression generalisation bound
  gives a non-trivial value for an algorithm with infinite I(S;W). It holds
  [THEORY-248](record/theory.d/THEORY-248.md)'s former promote_when, unchanged.

### Changed

- [THEORY-315](record/theory.d/THEORY-315.md), Active: for a state whose four-state reflection orbit is
  realizable, preparation noncontextuality bounds |⟨X⟩| + |⟨Z⟩| ≤ 1. An
  independent derivation, which needs no outcome determinism, meets its
  promote_when.
- [THEORY-198](record/theory.d/THEORY-198.md), Active after narrowing: full capture makes the coarse measure
  factorize across the block in 1D, and in D dimensions under the per-block
  capture hypothesis, now stated in the title with the no-cancellation
  exclusion. The Lemma is re-derived.
- [THEORY-248](record/theory.d/THEORY-248.md), Active after narrowing: the Lipschitz rate-distortion bound
  is finite wherever the output law's rate-distortion function is finite at
  distortion ε/(2L). Theorem 4 and Corollary 6 are re-derived. These
  changes carry out the promotion audit's batch-019 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
