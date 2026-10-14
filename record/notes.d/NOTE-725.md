---
number: 725
status: Read
formerly:
- NOTE-tmp3i3lt
paper: LIT-1034
title: 'Adams, Fernandez & Witkowski — Two Ways of Understanding Social Dynamics'
version: 1
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Read in full from the arXiv PDF, v2 of 15 June 2022
    (arxiv.org/pdf/2206.03563), a four-page conference-style paper with six
    figures. Text extracted with pdftotext; the figures were not inspected
    beyond their captions, which carry the quantitative results. Read: all
    of it, references included. Quotations checked by script against the
    extracted text, whitespace normalised.
date: '2026-10-13'
summary: >-
  A short, preliminary study of the 2017 canvas alone. Transitions between
  10-minute snapshots are tallied as cellular-automaton-style neighbourhood
  rules, and a CNN predicts each pixel from its 3×3 neighbourhood. Prediction
  worsens with the horizon and dips in the middle of the event. Locally
  growing objects are predicted, and designs coordinated off the canvas are
  missed. There are no baselines or error bars, and participants are never
  modelled.
---
<!-- inactive-ok-file: CLAIM-280 THEORY-224 — Proposed; an open claim and this reading's account, cited as what this reading bears on -->

# NOTE-725: Adams, Fernandez & Witkowski — Two Ways of Understanding Social Dynamics

## Contribution

Two exploratory analyses of the 2017 r/place canvas that use only the canvas
states, with no annotations and no participant data. One counts how often
each local "rule" (a neighbourhood state and the centre pixel's next
colour) occurs between 10-minute snapshots. The other trains a small CNN to
predict a pixel's colour 10 minutes to 6 hours ahead from its 3×3
neighbourhood. The aim is to see which objects the canvas's own local
dynamics account for, and which need coordination off the canvas.

## Key insight

The canvas alone holds two kinds of object. Some grow by a simple local
rule: the Blue Corner and the Void spread by recolouring neighbours, and
flags extend. Others are copies of a design held somewhere else: the Mona
Lisa, the dove on the EU flag, the US flag. A local predictor of canvas
states finds the first kind and misses the second. "These examples are all
extrinsic collaborations between users, which cannot be predicted unless
the model is trained with extra inputs."

## Assumptions

- The canvas is treated as a synchronous 2D cellular automaton between
  10-minute snapshots (682 in all). A "rule" is one neighbourhood state with
  the centre pixel's outcome, at radius 1 or 2.
- An object is "a set of spatially local rules that don't change over
  time", after Krakauer et al. on individuality. The authors note at once
  that externally defined images make the canvas's rules inconsistent.
- CNN input: a 3×3 patch, RGB channels separately. Output: the centre
  pixel in a later frame. Scored by SSIM.
- Data: the 2017 dataset, including placements before the 72-hour event.

## Key results

- **Rule frequencies (Figs. 1–2).** Radius-1 rules repeat more than radius-2
  rules, which the authors grant may only reflect the smaller rule space.
  The number of distinct rules grows over the event. No null model is
  computed; comparison with white noise is left for the future.
- **Horizon (Fig. 4).** The further ahead the target frame, the worse the
  prediction.
- **Time course (Fig. 6).** One frame ahead, accuracy falls in the middle of
  the event (frames 400–500) against frame 450 and rises again later; 36
  frames ahead, the last frames are predicted better than the first. The
  authors read this as rules "statistically more difficult to infer for the
  middle time frame of the experiment, in spite of edits and interactions
  remaining intense until the end".
- **What is and is not predicted (Fig. 5).** One frame ahead, the output is
  nearly the final canvas (mean SSIM 0.95). Thirty-six frames ahead, the EU
  dove, the objects inside the Blue Corner and the central US flag are
  missing. Objects "growing linearly over time such as the blue corner or
  the German flags" are partly predicted.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Short-horizon canvas states are predictable from 3×3 local context; predictability falls with horizon | weak | SSIM curves with no persistence baseline; a near-static canvas scores high by copying |
| C2 | Predictability dips mid-event although activity stays high | weak | pairwise tests on frames every ~8 h; no correction, model not described in detail |
| C3 | Objects that spread by local recolouring are predictable from the canvas; designs coordinated off it are not | weak | one illustrated output (Fig. 5) |
| C4 | Users' placement decisions depend more on short-term than long-term context | speculative | inferred from C1 |

## Concepts

- **Rule.** One neighbourhood configuration and the centre pixel's next
  colour; a CA rule in the usual sense is a set of these.
- **Extrinsic collaboration.** Interaction between users "outside of the
  direct activity of editing the canvas" (subreddits, private
  discussions).
- **Object as persisting rule set.** An object persists if the local rules
  that define it persist in that space.

## Connections

It reads Litherland & Mørch ([LIT-1037](../literature.d/LIT-1037.md)) as showing that r/place objects
"are more fully understood using additional data, particularly on a social
level", and Rappaz et al. (2018) as clustering users. It borrows the idea
of individuals as temporal constants from Krakauer et al. (2020) and the
neural-CA set-up from Mordvintsev et al. (2020). It does not mention the
2022 data, which did not yet exist.

## Bearing on the record

**What the filing expected, and what the paper is.** The exchange (A8)
proposed it as a start on estimating how far different participants' reach
extends. It does not do that. It models no participants, and its "locality"
is the spatial and temporal context of a pixel on the canvas, not a
person's reach. Its only remark about users is that predictability "would
probably increase if analyzing each subset of users that were collaborating
together". That is left to future work.

**[QUESTION-084](../questions.d/QUESTION-084.md) and [QUESTION-093](../questions.d/QUESTION-093.md).** The paper is a flat,
local model of the canvas, the baseline A8 §5 proposed to beat with a
latent-coalition model. Its failure on coordinated designs is what such a
model would have to fix. But without a persistence baseline and with one
illustrated output, the failure is not measured. It is a pointer for both
questions, not evidence on either.

**[CLAIM-280](../claims.d/CLAIM-280.md).** The authors' working definition of an object, "in
order for an object to persist, the set of rules that define it must
persist over time in that local space", identifies the product with a
persisting local rule set. They note that a static image like the Mona
Lisa "would be changed back according to the set of rules" when perturbed.
That is the repair regime in CA language. They do not measure it.

**[CLAIM-279](../claims.d/CLAIM-279.md).** The Blue Corner and the Void are two objects with the same
kind of rule (recolour neighbours) and opposite valence to their
neighbours. That is consistent with the claim but adds nothing to it.

## Limitations

- No baseline. One-frame-ahead SSIM of 0.95 on a canvas that changes little
  in 10 minutes may be no better than copying the last frame, and the paper
  does not check.
- No error bars and no description of the CNN beyond its input and output.
  Statistical tests compare a handful of frames.
- The rule-frequency analysis lacks the null model the authors themselves
  call for.
- The claim about coordinated designs rests on one figure.
- Only the 2017 canvas; no participant or community data.

## Open questions

- Does a 3×3 CNN beat a copy-last-frame baseline at any horizon, and where
  on the canvas? Where it does, local dynamics carry information; where it
  does not, the "rules" found are persistence.
- If the same model is trained per recovered coalition (Wu & Silva,
  [LIT-1032](../literature.d/LIT-1032.md)), does predictability of coordinated designs rise? That is
  A8 §5's test.
