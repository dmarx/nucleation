# LEAD-114 progress

- **Lead:** LEAD-114 — Learn a non-abelian task with no matrix representation
  imposed, and recover its irreducibles from the weights without supplying the
  group, or show them unrecoverable. Advances QUESTION-058.
- **Branch:** claude/lead-114-blind-irrep (cut from origin/staging)
- **Worker:** delegated (Claude, this session)

## Task as understood

Train a small numpy network on a non-abelian group's multiplication, inputs
one-hot indices (NO matrix representation imposed), output a softmax over
|G| classes. Then recover the group's irreducibles from the trained weights
*without supplying the group*, with a *group-supplied control*. Where the
network's learned operation is used to recover irreps, the group came from the
network, not from us.

## Choices made (lead leaves these open)

- Group: S3 (main; smallest non-abelian; irreps dims 1,1,2). S4 as an
  extension if time (dims 1,1,2,3,3) to show the method is not special to the
  tiny case.
- Encoding: one-hot element indices. Imposes no matrix representation (lead
  requirement).
- Architecture: shared embedding E (|G|xd) + one hidden ReLU layer + unembed,
  cross-entropy, weight decay, held-out-batch GD. Standard group-composition
  toy model; known to admit irrep structure.
- "Blind": recovery uses only the trained weights plus the binary operation the
  network itself learned (T_net[g][h] = argmax logits). The true Cayley table,
  group name and true irreps are never given to the blind path. The control
  supplies the true group.
- Recovery method: Peter-Weyl simultaneous block-diagonalisation of the left+
  right regular representations of the reconstructed operation (yields the
  number of irreps and each dimension), cross-checked by class-sum characters;
  then isotypic projection of the learned embeddings (variance explained per
  irrep). Blind vs control.

## Done

- Step 0: read CLAUDE.md, design principles, ADR-001, ADR-048, run-lead skill,
  QUESTION-058, CLAIM-382, docs/record.md fields.
- Step 1: searched record/ ("irreducible", S3/S4, non-abelian, recover) —
  target not already held. Env: numpy 2.5.3, scipy 1.18.1, pytest 9.1.1, no
  torch -> numpy only.

## Next

- Write groups.py (abstract tables + one-hot data), model.py (train), commit.
- reptheory.py (Peter-Weyl + characters + isotypic projection), tests.
- run pipeline, persist results JSONL, then file CASE/CLAIM/changelog.
