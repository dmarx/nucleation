---
status: Proposed
promote_when: >-
  Promoted by a test on a crowd-built canvas in which a model using only
  local canvas context is compared with a copy-the-last-state baseline and
  with a model given off-canvas coordination data (templates, overlay
  histories, forum plans) or recovered coalitions. The account holds if the
  local model beats the baseline mainly on objects that spread by a local
  recolouring rule, and the coordination-aware model gains mainly on
  designs copied from templates, across many objects and held-out time.
  It is refuted if local context predicts template-copied designs as well
  as spreading ones, or if neither model beats persistence. What cannot
  settle it: more illustrated outputs, or SSIM scores without a persistence
  baseline.
title: 'Objects on a crowd-built canvas are of two kinds, those that spread by a local recolouring rule and are predictable from the canvas itself, and those copied from designs coordinated off the canvas, which local canvas dynamics do not predict'
version: 1
tags:
- complex-systems
- social-science
date: '2026-10-13'
source:
- LIT-tmpmc817
summary: >-
  Adams, Fernandez & Witkowski (2022), [LIT-tmpmc817](../literature.d/LIT-tmpmc817.md), read in [NOTE-tmp3i3lt](../notes.d/NOTE-tmp3i3lt.md).
  A CNN predicting each pixel of the 2017 r/place canvas from its 3×3
  neighbourhood recovers objects that grow by recolouring neighbours (Blue
  Corner, German flags) and misses designs whose plan lived off the canvas
  (EU dove, US flag) at a six-hour horizon. Short-horizon predictability dips
  mid-event. The evidence is one illustrated output and SSIM curves with no
  persistence baseline. The paper models no participants and does not
  measure anyone's reach.
---
<!-- inactive-ok-file: THEORY-tmp7w5tq THEORY-tmpbrxww CLAIM-tmpgfyls — Proposed; sister readings of r/place studies and an open claim, cited for context, nothing here rests on them -->

# THEORY-tmpy8l36: Objects on a crowd-built canvas are of two kinds, those that spread by a local recolouring rule and are predictable from the canvas itself, and those copied from designs coordinated off the canvas, which local canvas dynamics do not predict

## Source

Adams, Fernandez & Witkowski (2022), [LIT-tmpmc817](../literature.d/LIT-tmpmc817.md), read in [NOTE-tmp3i3lt](../notes.d/NOTE-tmp3i3lt.md):
the CNN section, Figs. 4–6, Discussion and Conclusion.

## What was actually shown

A convolutional network takes a 3×3 patch of a 10-minute snapshot of the
2017 canvas and outputs the centre pixel 10 minutes, 1, 3 or 6 hours later.

- Prediction worsens as the horizon lengthens (Fig. 4).
- One frame ahead, the reconstructed final canvas is nearly the real one,
  with mean SSIM 0.95. Six hours ahead, the EU dove, the objects inside the
  Blue Corner and the central US flag are missing. Objects "growing
  linearly over time such as the blue corner or the German flags" are
  partly recovered (Fig. 5, Discussion).
- Short-horizon accuracy dips in the middle of the event and recovers
  toward the end, while activity stays high (Fig. 6).

The authors give a mechanism that is a reading of the case. Some objects
are defined by a simple local rule (recolour a neighbour blue, or black).
Others are copies of an external image, whose pixels depend on their
position in a design. A local model can learn the first kind. The second
kind needs "extra inputs".

## What this does not say

- **It is barely tested.** There is no copy-the-last-frame baseline, so
  SSIM of 0.95 at ten minutes may be persistence. There are no error bars,
  and the split into predictable and unpredictable objects rests on one
  figure. This is a hypothesis with an illustration.
- **It does not measure participants' reach.** The exchange proposed this
  paper as a start on how far different participants' reach extends. It
  models no participants. "Locality" here is a pixel's spatial and temporal
  context.
- **It does not show that coordination caused the missed objects.** The
  authors infer it from what the missed objects are (flags, emblems,
  famous images). No coordination data were used.
- **The mid-event dip is unexplained.** The authors' reading, that rules
  are more mixed when objects are forming and competing, is not tested.

## Connections

No relations are declared, because the evidence is too thin to support or
answer anything. What it points at:

- **[QUESTION-tmpeqxa9](../questions.d/QUESTION-tmpeqxa9.md).** If local dynamics miss exactly the template-copied
  designs, then the canvas alone does not reveal coordination by planning.
  That is consistent with the question's second horn, unmeasured.
- **[QUESTION-tmpuz3py](../questions.d/QUESTION-tmpuz3py.md).** This is the flat model that A8 §5 proposed to beat
  with latent coalitions. Its authors predict per-coalition models would do
  better, and they leave it untested. Wu & Silva's recovered coalitions
  ([THEORY-tmp7w5tq](THEORY-tmp7w5tq.md)) would supply the units.
- **[CLAIM-tmpgfyls](../claims.d/CLAIM-tmpgfyls.md).** The Blue Corner and the Void share a rule type and
  oppose their neighbours. That fits the claim and adds nothing to it.
- Litherland & Mørch ([LIT-tmprqknl](../literature.d/LIT-tmprqknl.md)), whose Mona Lisa case this paper
  invokes, show the off-canvas design work directly ([THEORY-tmpbrxww](THEORY-tmpbrxww.md)).
