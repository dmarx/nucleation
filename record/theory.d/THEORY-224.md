---
number: 224
status: Proposed
formerly:
- THEORY-tmpy8l36
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
version: 2
history:
- version: 2
  date: '2026-10-29'
  note: >-
    The supports entry for CLAIM-273 is replaced by corroborates: the
    sixteenth status review (ADR-057), at the status review's ruling
    (the owner delegated these rulings), moved this reading from
    CLAIM-273's grounds to its corroborated_by (ADR-058). That claim
    cites it as one illustration of its general form and does not use
    its contested thesis. A dated note says what holds it back. The
    status is unchanged.
tags:
- complex-systems
- social-science
date: '2026-10-13'
source:
- LIT-1034
summary: >-
  Adams, Fernandez & Witkowski (2022), [LIT-1034](../literature.d/LIT-1034.md), read in [NOTE-725](../notes.d/NOTE-725.md).
  A CNN predicting each pixel of the 2017 r/place canvas from its 3×3
  neighbourhood recovers objects that grow by recolouring neighbours (Blue
  Corner, German flags) and misses designs whose plan lived off the canvas
  (EU dove, US flag) at a six-hour horizon. Short-horizon predictability dips
  mid-event. The evidence is one illustrated output and SSIM curves with no
  persistence baseline. The paper models no participants and does not
  measure anyone's reach.
corroborates:
- CLAIM-273
---
<!-- inactive-ok-file: THEORY-218 CLAIM-279 — Proposed; sister readings of r/place studies and an open claim, cited for context, nothing here rests on them -->

# THEORY-224: Objects on a crowd-built canvas are of two kinds, those that spread by a local recolouring rule and are predictable from the canvas itself, and those copied from designs coordinated off the canvas, which local canvas dynamics do not predict

## Source

Adams, Fernandez & Witkowski (2022), [LIT-1034](../literature.d/LIT-1034.md), read in [NOTE-725](../notes.d/NOTE-725.md):
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

One relation is declared: it corroborates CLAIM-273's imported-order half,
which does not rest on it. The evidence is too thin to support or answer
anything else. What it points at:

- **[QUESTION-084](../questions.d/QUESTION-084.md).** If local dynamics miss exactly the template-copied
  designs, then the canvas alone does not reveal coordination by planning.
  That is consistent with the question's second horn, unmeasured.
- **[QUESTION-093](../questions.d/QUESTION-093.md).** This is the flat model that A8 §5 proposed to beat
  with latent coalitions. Its authors predict per-coalition models would do
  better, and they leave it untested. Wu & Silva's recovered coalitions
  ([THEORY-216](THEORY-216.md)) would supply the units.
- **[CLAIM-279](../claims.d/CLAIM-279.md).** The Blue Corner and the Void share a rule type and
  oppose their neighbours. That fits the claim and adds nothing to it.
- Litherland & Mørch ([LIT-1037](../literature.d/LIT-1037.md)), whose Mona Lisa case this paper
  invokes, show the off-canvas design work directly ([THEORY-218](THEORY-218.md)).

## Note of 2026-10-29: what holds it back

Read in full (NOTE-725), but its promote_when is unmet. The paper has no
persistence baseline, no error bars and no coordination data, and its
split into two kinds rests on one illustrated six-hour reconstruction. No
test on a crowd-built canvas has compared a local model with a copy-the-
last-state baseline and a coordination-aware model. Narrowing to what
Adams et al. report would free nothing, since CLAIM-273 now cites it as
corroboration.
