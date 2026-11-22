---
status: Proposed
title: 'In a small transformer that has memorized arbitrary facts, fine-tuning some of them away by unlearning, overwriting or training on an unrelated task mostly leaves them recoverable, by another cue, the runner-up answer, a probe, reverting one early block''s update or relearning related facts, so the apparent forgetting is mostly readdressing and interference, not loss; the update that hides a fact sits mainly in the routing into the memory, not at the read-out; and only gradient ascent, which damages the whole model, leaves forgetting that looks like loss'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant from the run of LEAD-043
    (CASE-tmprir2y), as a delegated worker.
role: thesis
warrant: empirical
defeated_if: >-
  A rerun with matched training worlds, at this scale or larger, finds the
  readers no better than their rate on the twin world's values for facts
  forgotten by unlearning, overwriting or a new task; or finds that the
  recovery comes from information other than the fact itself, in that it
  survives in a world where the fact was never trained; or finds that
  reverting the read-out (late blocks and head) restores more forgotten
  facts than reverting the first layer's blocks; or finds that gradient
  ascent stopped at its criterion with the rest of the model intact (not
  collapsed) leaves the facts recoverable no worse than unlearning does,
  which would make ascent's apparent loss a by-product of the collapse
  and leave the exception unsupported. A result at LM scale on natural
  facts that differs does not defeat the toy-scale claim but bounds it.
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-22'
line:
- learned-structure
- realizability
grounds:
- CASE-tmprir2y
bears_on:
- QUESTION-275
- QUESTION-010
summary: >-
  What the toy-scale run of [CASE-tmprir2y](../cases.d/CASE-tmprir2y.md) finds, stated so that it can fail. In a
  two-layer numpy transformer (4 seeds, a matched twin for each), 87 to
  98 percent of the facts forgotten by unlearning, overwriting or a new
  task are recovered by at least one of eleven readers, against 28 to 46
  percent for values the model never held, at 2.8 to 3.6 readers per fact
  against 0.4 to 1.0. An untrained cue recovers 73 to 79 percent after
  fine-tuning at one cue; the old value is the runner-up in about a third
  of overwritten facts; reverting one first-layer block restores 41 to 55
  percent, reverting the head 0 to 13. Gradient ascent collapses retained
  accuracy to 8 to 19 percent, and run past its criterion leaves no
  reader above baseline. It is a toy: two layers, random facts,
  templates that do not generalize. The wording is the assistant's
  (Claude, in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CASE-tmprir2y CASE-274 CLAIM-697 — new or Proposed; the run this rests on, the design it reduces, and the claim whose realization cost it uses -->

# CLAIM-tmp2eemo: In a small transformer that has memorized arbitrary facts, fine-tuning some of them away by unlearning, overwriting or training on an unrelated task mostly leaves them recoverable, by another cue, the runner-up answer, a probe, reverting one early block's update or relearning related facts, so the apparent forgetting is mostly readdressing and interference, not loss; the update that hides a fact sits mainly in the routing into the memory, not at the read-out; and only gradient ascent, which damages the whole model, leaves forgetting that looks like loss

## The claim

[CASE-274](../cases.d/CASE-274.md) names five things apparent forgetting can be: readdressing,
interference, downstream suppression, a higher realization cost, and
loss. In the toy run of [CASE-tmprir2y](../cases.d/CASE-tmprir2y.md), with every readout set against a twin
that never held the value:

- **Readdressing.** Unlearning at cue A leaves 73 percent of facts
  answered at cue B (twin 1 percent); overwriting at A, 79 percent (twin
  0).
- **Interference.** After overwriting, the old value is the runner-up in
  31 to 32 percent of facts (twin 6 to 7), comes back under sampling more
  often (coverage at N = 256: 0.24 to 0.37 against 0.06 to 0.08, a higher
  realization cost in [CLAIM-697](CLAIM-697.md)'s sense), and is relearned in a third to a
  half of the steps.
- **Where the change sits.** Reverting a single first-layer block's
  update restores 41 to 55 percent of facts in the unlearn and overwrite
  arms; reverting the head restores 0 to 13. Probes on the second layer's
  residual read 18 to 29 percent (twin 3 to 6). The fine-tuning mostly
  changed how a query reaches the stored fact, not the store or the
  read-out, so this is not [CASE-274](../cases.d/CASE-274.md)'s downstream suppression.
- **Loss.** Only gradient ascent gives a pattern like loss, and it is
  loss of the model, not of the targets: retained accuracy falls to 8 to
  19 percent. Stopped at its criterion, probes and relearning still find
  the targets (relearning half takes the other half from 8 to 44–48
  percent; twin to 3).

## What it does not say

It does not say forgetting in language models is readdressing. Memorized
random facts in two layers are the case most favourable to a surviving
trace, the templates did not generalize to unseen subjects, and the
readers recover several signatures for the same fact, so the outcomes are
not exclusive classes. It does not test [CASE-274](../cases.d/CASE-274.md)'s response-geometry
prediction.
