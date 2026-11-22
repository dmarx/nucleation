# LEAD-172 progress

- Lead: LEAD-172 (modular-addition checkpoint study, prospective test)
- Branch: claude/lead-172-modular-addition
- Task as understood: train small transformers on modular addition (CPU,
  ~1 hour budget, one or two small models, a few seeds); at checkpoints
  measure training-kernel eigenspaces and per-layer coupling among Fourier
  modes; fit on early checkpoints, predict later change (circuit formation,
  generalization), including under a held-out intervention; compare against
  a null at equal edge budget. File a CASE (executed-study), a CLAIM if
  warranted, dated notes on QUESTION-275, QUESTION-360, QUESTION-217,
  CLAIM-698 and LEAD-172, and a changelog fragment.

## Done

## Next

- Write training/measurement script with append-only JSONL checkpoints and resume.

## Choices

- torch is not installed: numpy only, hand-written forward and backward.
