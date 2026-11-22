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

- Step 2-4: wrote groups.py, model.py, reptheory.py, test_lead114.py (10
  tests pass), run.py. Ran pipeline (9 items, ~75s), results.jsonl written.
- Bug found and fixed: recover_irreps sorted dims/char but returned blocks
  unsorted, so per-irrep fractions were misaligned (fixed: blocks reordered;
  guard test test_blocks_align_with_sorted_dims added; pipeline re-run).

## Results (corrected)

- Blind recovery of the irreducibles SUCCEEDS whenever the net learned the
  group (its argmax operation is a valid group): full character table + dims
  recovered from the net's own operation, no group supplied, matching the
  group-supplied control to ~1e-14. S4-grok -> [1,1,2,3,3]; S3-fit -> [1,1,2].
- Control's diagnostic fires: S3-mem (25% holdout, memorises, test_acc~0) ->
  reconstructed operation is NOT a group -> blind recovery refuses. The limit
  is the network, not the method.
- Weights carry the irreps as their group-Fourier power spectrum: trivial
  (constant) ~0; faithful irreps dominate (S3 ~78% on the 2-dim standard;
  S4 ~78% on the two 3-dim irreps); sign rep smallest. Dominant non-trivial
  irrep is seed-dependent (approximate universality).
- Scope: recovery is up to isomorphism (characters/dims/isotypic projectors);
  explicit per-element matrices only up to a basis within each isotypic block.

- Step 6: filed CASE-tmpjgjtj (executed-study), CLAIM-tmpie2v3 (answers
  QUESTION-058), CLAIM-tmpkgzd8 (complements it), changelog fragment
  record/changelog.d/lead-114.md, dated notes on LEAD-114 and QUESTION-058
  (no status/stage changes). Per-file checks pass. All pushed.

## Done — lead carried out

Nothing outstanding on this worker's part. Owner decides LEAD-114's status/
stage and whether to promote the two Proposed claims.
