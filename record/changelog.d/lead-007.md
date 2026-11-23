### Added

- LIT-tmpkuq67 (Active): Lippl and Lindsey, "Inductive biases of
  multi-task learning and finetuning: multiple regimes of feature reuse"
  (arXiv 2310.02396, NeurIPS 2024), registered and read by the lead run of
  2026-11-23 for LEAD-007, as the precursor of Anguita and colleagues.
- NOTE-tmpw2i45 (Read): main text and most appendices of the arXiv HTML
  of v4; two proofs skipped.
- THEORY-tmpw69kb (Proposed): the shallow-network theory (feature reuse
  against sparse new features, the conservation law, nested feature
  selection reached by rescaling after pretraining).
- THEORY-tmpfysqg (Proposed): rescaling before fine-tuning helps ResNets
  and not Vision Transformers.
- CASE-tmpjn7jc (executed-study, documented, Proposed): a diagonal-network
  run, 40 seeds, code and results under scratch/studies/lead-007/.
- CLAIM-tmp7n00e (Proposed, thesis, demonstrated): a pretrained network
  and its function-preserving rescaling learn differently under full
  fine-tuning, alike under readout-only training, and the better of them
  reverses with the main task.
- CLAIM-tmp2tjpt (Proposed, thesis, interpretive) and CLAIM-tmpew899
  (Proposed, counter, interpretive, `objects_to` the former): alternative
  readings of the check, two learners with one function (the assistant's
  lean) or one learner under two procedures.
- ARG-tmpbvq7y (Proposed, existence): the support the first reading gives
  CLAIM-754.

### Changed

- Dated notes of 2026-11-23 on LEAD-007, CLAIM-754, CLAIM-675,
  THEORY-2077, CLAIM-tmp2k67n, CLAIM-758, CLAIM-756 and CASE-294.
- THEORY-2077 gains `extends: THEORY-tmpw69kb`; LIT-2861 gains
  `extends: LIT-tmpkuq67`. No status, title or stage changed.
