### Added

- [QUESTION-tmpa5vf9](record/questions.d/QUESTION-tmpa5vf9.md): whether hyperbolic networks' advantage on tree-like
  data goes with the Möbius bias translations and the distance-based output
  layer. It holds [THEORY-566](record/theory.d/THEORY-566.md)'s former promote_when, unchanged, and refines
  [QUESTION-025](record/questions.d/QUESTION-025.md).
- [QUESTION-tmpujty6](record/questions.d/QUESTION-tmpujty6.md): whether Blackwell-equivalent representations of
  trained networks stitch differently by a measurable margin under the
  paper's protocol. It holds [THEORY-176](record/theory.d/THEORY-176.md)'s former promote_when, unchanged.

### Changed

- [THEORY-566](record/theory.d/THEORY-566.md), Active: in Ganea et al.'s hyperbolic networks, curvature acts
  only through the bias translations and the distance-based output layer.
  The composition argument is written out, with the sense of "conjugated".
- [THEORY-176](record/theory.d/THEORY-176.md), Active: the stitching penalty is not Blackwell's order. A
  constructed example now shows that Blackwell-equivalent representations
  can stitch differently, inside the paper's own map class. These changes
  carry out the promotion audit's batch-027 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
