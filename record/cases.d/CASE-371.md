---
number: 371
status: Proposed
formerly:
- CASE-tmprir2y
title: 'A toy-scale forgetting study run on CPU: in a two-layer transformer that memorized random subject–relation–object facts, facts fine-tuned away by unlearning, overwriting or an unrelated new task stay recoverable, by an untrained cue, a probe, the runner-up answer, reverting one block''s update or relearning the other half, at rates well above a matched twin''s, while gradient ascent wrecks the whole model; and the union of these readers also recovers a fact the twin never held in a quarter to nearly half of cases'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-043 as a delegated
    worker. Scripts, tests, per-item results and the analysis are committed
    under scratch/studies/lead-043/.
standing: documented
kind: executed-study
tags:
- representation-learning
- learning-theory
- anthology-candidate
date: '2026-11-22'
line:
- learned-structure
- realizability
- pragmatic-transport
variant_of:
- CASE-274
bears_on:
- QUESTION-275
- QUESTION-010
draws_on:
- THEORY-281
- THEORY-1888
- THEORY-1870
summary: >-
  A toy-scale stand-in for [CASE-274](CASE-274.md)'s design, for [LEAD-043](../leads.d/LEAD-043.md). numpy only, CPU, about
  two hours of compute on a shared machine. A two-layer transformer
  (d 64, 4 heads, no layer norm, hand-written backward pass) memorizes 256
  random facts under two query templates. 32 target facts are then
  fine-tuned away in seven arms: unlearning toward a uniform output,
  gradient ascent and overwriting with new values, each at one cue or two,
  with rehearsal of the rest; and an unrelated new task without
  rehearsal. Every model has a twin trained from the same initialization
  on a world that differs only in the target values, so every readout has
  a false-positive rate. Pooled over 4 seeds and both worlds, in the
  unlearning, overwriting and new-task arms 87 to 98 percent of the
  forgotten facts are recovered by at least one reader, against 28 to 46
  percent for the twin's values, and the average fact is recovered by 2.8
  to 3.6 readers against 0.4 to 1.0. An untrained cue recovers 73 to 79
  percent when one cue was fine-tuned; reverting one early block's update
  restores 41 to 55 percent; relearning half the targets makes the second
  fine-tuned-away value faster to
  learn after overwriting or a new task (8 to 8.5 steps against 17.5 to
  25.5 for the twin). Gradient
  ascent instead collapses the model (retained facts at 8 to 19 percent),
  and run past its criterion leaves no reader above baseline. The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CASE-274 CLAIM-697 CLAIM-698 THEORY-1888 THEORY-1870 — Proposed; the design this run reduces, the claims it bears on, and the erasure readings it draws on -->

# CASE-371: A toy-scale forgetting study run on CPU: in a two-layer transformer that memorized random subject–relation–object facts, facts fine-tuned away by unlearning, overwriting or an unrelated new task stay recoverable, by an untrained cue, a probe, the runner-up answer, reverting one block's update or relearning the other half, at rates well above a matched twin's, while gradient ascent wrecks the whole model; and the union of these readers also recovers a fact the twin never held in a quarter to nearly half of cases

## A toy-scale stand-in

[LEAD-043](../leads.d/LEAD-043.md) asks for [CASE-274](CASE-274.md)'s study: train, fine-tune a capability away,
and ask with probes, relearning and interventions whether the forgetting
was loss, readdressing, interference or suppression. Only a CPU was
available and torch is not installed, so this is a toy: a model of about
110 thousand parameters, memorized random facts, minutes per run. It
keeps the design's two load-bearing parts, synthetic facts with no
outside source and matched training worlds, and drops most of its
interventions and its budget axis. What an LM-scale version would add is
at the end.

## What was run

- **Facts.** 128 subjects × 4 relations, each fact an object drawn at
  random from 16. Three templates query a fact: A `[s, r_A, Q]`,
  B `[r_B, s, Q]`, C `[r_C, Q, s]`. Pretraining (600 full-batch Adam
  steps) covers the 64 old subjects under A and B, and C only for the 48
  subjects that are not targets. Every model reaches 100 percent on its
  training rows.
- **Targets and twins.** 16 subjects × relations 0 and 1: 32 target
  facts. The twin world changes every target value and nothing else; the
  twin starts from the same initialization on the same schedule. Each
  model is read against its own values and against the other world's,
  which it never held. The second rate is the readout's baseline.
- **Arms** (all at learning rate 3e-4, rehearsing every non-target row
  except in newtask):
  - *unlearn* A or AB: the targets at those cues are trained toward a
    uniform output;
  - *ascent* A or AB: negative cross-entropy on the targets;
  - *overwrite* A or AB: the targets trained to new values that neither
    world holds;
  - *newtask*: 256 facts of 64 new subjects, no rehearsal, the classic
    catastrophic-forgetting set-up.

  Each arm trains until its criterion (target accuracy at the
  fine-tuned cues at most 1/16; for overwrite, the new values learned;
  for newtask, the new facts learned) and then as many steps again, at
  least 100 in all, so that forgetting is not read at the boundary where
  any nudge restores it. Two further arms, ascent stopped at the first
  step meeting the criterion, were added after the first runs showed
  that ascent run longer collapses the model (seeds 0 and 2 only).
- **Seeds.** 4 per arm (2 for the early-stopped ascent), each with its
  twin: 256 target facts per arm, of which 173 to 256 were forgotten at
  cue A.

## The readers

Each is applied to every target fact that the fine-tuned model gets
wrong at cue A.

- **Another cue** (readdressing): B when only A was fine-tuned, C
  otherwise.
- **The runner-up** (interference): the argmax once the top answer is
  removed.
- **Logit lens and probes** (suppression): at each of the four residual
  stages after the embedding, the head applied directly, and linear and
  one-hidden-layer MLP probes fitted on the same model's retained facts.
- **Weight-delta reversion** (where the change sits): each block's
  fine-tuning update reverted alone, and from a block downward.
- **Sampling coverage** ([CLAIM-697](../claims.d/CLAIM-697.md)): 1 − (1 − p)^N at cue A for
  N = 1, 16, 256, with no selector.
- **Relearning**: half of the target subjects relearned at the
  fine-tuned cues (with rehearsal); steps to criterion, and the accuracy
  of the held-out half, which is never trained.

## Results

Rates are among facts forgotten at A, own values / the twin's values,
pooled over seeds and worlds (scratch/studies/lead-043/summary.md has
every readout).

| arm | retained acc. | other cue | runner-up | best probe | best single revert | any reader | readers per fact |
|---|---|---|---|---|---|---|---|
| unlearn A | 1.00 | 0.73 / 0.01 (B) | 0.05 / 0.06 | 0.22 / 0.05 | 0.55 / 0.04 | 0.98 / 0.46 | 3.6 / 0.7 |
| unlearn AB | 1.00 | 0.08 / 0.06 (C) | 0.11 / 0.06 | 0.18 / 0.06 | 0.51 / 0.03 | 0.95 / 0.45 | 3.0 / 0.8 |
| overwrite A | 1.00 | 0.79 / 0.00 (B) | 0.32 / 0.07 | 0.29 / 0.04 | 0.41 / 0.00 | 0.93 / 0.30 | 3.2 / 0.4 |
| overwrite AB | 1.00 | 0.10 / 0.06 (C) | 0.31 / 0.06 | 0.29 / 0.03 | 0.43 / 0.00 | 0.89 / 0.28 | 2.8 / 0.4 |
| newtask | 0.33 | 0.25 / 0.06 (B) | 0.25 / 0.05 | 0.32 / 0.05 | 0.34 / 0.06 | 0.87 / 0.44 | 2.9 / 1.0 |
| ascent A | 0.09 | 0.01 / 0.08 (B) | 0.02 / 0.08 | 0.09 / 0.06 | 0.02 / 0.08 | 0.35 / 0.40 | 0.5 / 1.1 |
| ascent AB | 0.09 | 0.01 / 0.07 (C) | 0.00 / 0.08 | 0.08 / 0.08 | 0.02 / 0.08 | 0.31 / 0.44 | 0.4 / 1.1 |
| ascent A, early | 0.17 | 0.06 / 0.08 (B) | 0.09 / 0.05 | 0.28 / 0.03 | 0.08 / 0.06 | 0.59 / 0.31 | 1.4 / 0.9 |
| ascent AB, early | 0.19 | 0.02 / 0.07 (C) | 0.10 / 0.05 | 0.34 / 0.04 | 0.09 / 0.07 | 0.52 / 0.38 | 1.3 / 1.0 |

Retained accuracy is on non-target old facts at A; for newtask, all old
facts. Relearning, median steps to criterion, own / twin, and the
held-out half's accuracy at A before and after:

| arm | steps | held-out half, own | held-out half, twin |
|---|---|---|---|
| unlearn A | 4 / 5 | 0.05 → 0.19 | 0.04 → 0.09 |
| unlearn AB | 6 / 9 | 0.09 → 0.14 | 0.09 → 0.07 |
| overwrite A | 8 / 17.5 | 0.00 → 0.14 | 0.00 → 0.05 |
| overwrite AB | 8.5 / 25.5 | 0.00 → 0.20 | 0.00 → 0.03 |
| newtask | 8.5 / 22 | 0.38 → 0.42 | 0.07 → 0.06 |
| ascent A | 592.5 / 489.5 | 0.08 → 0.10 | 0.10 → 0.06 |
| ascent AB | 600 / 600 | 0.09 → 0.12 | 0.07 → 0.07 |
| ascent A, early | 34 / 54.5 | 0.08 → 0.44 | 0.08 → 0.03 |
| ascent AB, early | 35.5 / 65 | 0.08 → 0.48 | 0.09 → 0.03 |

In plain words:

- **Unlearning at one cue is readdressing.** Facts pushed to a flat
  output at A are still answered at B, which fine-tuning never touched,
  in 73 percent of cases.
- **Overwriting is interference plus readdressing.** The old value is
  the runner-up in 31 to 32 percent of facts (6 to 7 percent for the
  twin's) and is learned back in a third of the steps the twin needs.
  Sampling finds it more often than the twin's value (coverage at
  N = 256: 0.24 to 0.37 against 0.06 to 0.08), so in [CLAIM-697](../claims.d/CLAIM-697.md)'s terms it
  has moved to a higher realization cost.
- **The update that hides a fact sits early.** Reverting one block of
  the first layer restores 41 to 55 percent of the facts in the unlearn
  and overwrite arms; reverting the head restores 0 to 13 percent. What
  the fine-tuning changed is mostly the routing into the memory, not the
  memory or the read-out. That is not [CASE-274](CASE-274.md)'s downstream suppression,
  which would show as a late revert restoring the fact.
- **Gradient ascent is the exception.** It drives the targets'
  probability to zero, for most models within 12 to 25 steps, and takes the retained facts
  with it. Stopped there, probes on the second layer's residual still read
  the value (28 to 34 percent against 3 to 4) and relearning half restores
  the held-out half from 8 to 44 or 48 percent while the twin falls to
  3. Run 100 steps or more, no reader beats the baseline and relearning
  does not converge in 600 steps. In this toy, ascent's forgetting is the
  only kind that looks like loss, and it is the loss of everything.
- **Coverage without a selector says nothing about a fact flattened to
  uniform.** After uniform unlearning p is 1/16 for the true value and
  for the twin's alike, and coverage at N = 256 is 1.00 for both.

## The baseline problem

The twin's column is not small. The same eleven readers recover a value
the twin never held in 28 to 46 percent of its facts, because each
reader is right by chance about one time in sixteen and they are many.
A survival test that asks whether any reader recovers the value, without
a matched world, would have called nearly half of a never-learned table
"retained". This is what [QUESTION-010](../questions.d/QUESTION-010.md)'s note of 2026-11-15 proposed the twin
for, and here it was needed. With random facts nothing else implies a
target value, so a recovery above the twin's rate cannot be the rebuild
from correlates that [THEORY-1888](../theory.d/THEORY-1888.md), [THEORY-1870](../theory.d/THEORY-1870.md) and [THEORY-281](../theory.d/THEORY-281.md) warn of.

## Its limits

- **Scale and data.** Two layers, 64 dimensions, 256 memorized facts,
  no natural text. Memorized random facts are the easiest case for a
  trace to survive in and the hardest for a template to generalize:
  template C, never trained on the target subjects, read them at 14
  percent before any fine-tuning, so unseen query variants could not be
  tested.
- **Readers.** Probes are fitted on retained facts of the same model; a
  fact stored in a subspace that retained facts do not use would be
  missed. The table counts recoveries; it does not classify each fact
  into one outcome, and most recovered facts show several signatures at
  once, so [CASE-274](CASE-274.md)'s outcomes are not exclusive classes here.
- **Relearning.** Steps to criterion are coarse when the output is flat
  (4 to 9 steps for both worlds after unlearning).
- **Not run.** Closed-form linear erasure, cue remapping beyond the three
  templates, task-vector merges, RL, the budget axis beyond coverage, and
  [CASE-274](CASE-274.md)'s response-geometry prediction ([CLAIM-698](../claims.d/CLAIM-698.md)), which needs a
  prediction made before the recovery tests.
- **Choices that shape the result.** Equal weight on the forget and
  retain losses; one learning rate; the stopping rule. Ascent's collapse
  may be specific to them.

## What an LM-scale version would add

Natural and synthetic facts in a pretrained language model, where a value
can be rebuilt from correlated knowledge, so the matched-world control
does real work and not only bookkeeping; paraphrase and multi-hop queries
that generalize, which this toy's templates did not; layer-wise linear
erasure as a forgetting method beside fine-tuning; the full budget axis
with a selector; and a pre-registered response-geometry prediction
against feature similarity and attribution.
