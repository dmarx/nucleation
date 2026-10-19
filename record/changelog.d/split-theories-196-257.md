### Added

- [THEORY-tmpfydax](record/theory.d/THEORY-tmpfydax.md) (Active): the planar lower bound on the precision of
  hyperbolic tree embeddings, split from [THEORY-196](record/theory.d/THEORY-196.md). A root with
  deg_max ≥ 15 chains needs Ω((ℓ/ε) log deg_max) bits per coordinate at
  distortion 1 + ε ≤ 2. It is proved by exact hyperbolic trigonometry,
  with explicit constants, where [LIT-874](record/literature.d/LIT-874.md) used a small-angle approximation
  as an equality.
- [THEORY-tmp7brn5](record/theory.d/THEORY-tmp7brn5.md) (Active): exact dynamical independence in linear VAR
  models, split from [THEORY-257](record/theory.d/THEORY-257.md). The VAR criterion is re-derived. For order
  above 1 the exceptional set is proved Lebesgue-null, where [LIT-979](record/literature.d/LIT-979.md)
  counted equations. For VAR(1), exact coarse-grainings exist on open sets
  but not at every scale generically.
- [QUESTION-tmpr1c4g](record/questions.d/QUESTION-tmpr1c4g.md): whether the code-based upper bound for tree
  embeddings in H^r, r > 2, is matched by a lower bound. This is the
  higher-dimensional half of the condition formerly on [THEORY-196](record/theory.d/THEORY-196.md).

### Changed

- [THEORY-196](record/theory.d/THEORY-196.md) extends [THEORY-tmpfydax](record/theory.d/THEORY-tmpfydax.md) and stays Proposed. Its promote_when
  narrows to Sarkar's distortion bound, the upper bound it still rests on.
- [THEORY-257](record/theory.d/THEORY-257.md) extends [THEORY-tmp7brn5](record/theory.d/THEORY-tmp7brn5.md) and stays Proposed. Its title now
  restricts "generically none is exact" to VAR order above 1, its VAR(1)
  bullet is corrected, and [NOTE-791](record/notes.d/NOTE-791.md)'s C4 is annotated.
- Both carry out the promotion audit's batch-012 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
