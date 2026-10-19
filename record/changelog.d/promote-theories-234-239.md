### Added

- [QUESTION-tmpogcb0](record/questions.d/QUESTION-tmpogcb0.md): whether the relational linear properties reported in
  released language models lie in the subspaces that enter the logits, so
  that they are properties of the distribution. This is the trained-model
  half of the condition formerly on [THEORY-234](record/theory.d/THEORY-234.md).

### Changed

- [THEORY-234](record/theory.d/THEORY-234.md) is narrowed and promoted to Active. Its title said a
  relational property is shared across equivalent models "only when" it
  lies in the logit subspaces. Theorem 14 gives a sufficient condition, so
  the title now says "when". Theorems 5 and 14 are re-derived in a dated
  note.
- [THEORY-239](record/theory.d/THEORY-239.md) is narrowed and promoted to Active. The top-d left singular
  span attains the minimum worst-case linear-probe error, but it is not the
  unique span that does, as its title and the thesis said. A dated note
  re-derives the bound, gives the counterexample, and works a non-reversible
  three-state case. [NOTE-770](record/notes.d/NOTE-770.md), [LIT-975](record/literature.d/LIT-975.md) and [QUESTION-052](record/questions.d/QUESTION-052.md) are corrected to
  match.
- Both carry out the promotion audit's batch-012 decisions ([ADR-047](record/decisions.d/ADR-047.md)).
