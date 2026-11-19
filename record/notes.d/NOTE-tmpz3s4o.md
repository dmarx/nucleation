---
status: Read
paper: LIT-tmp5gwuj
title: 'Mordvintsev and others 2020 — Growing Neural Cellular Automata'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://distill.pub/2020/growing-ca/ (HTTP 200, HTML, the
    journal's own open article page; DOI 10.23915/distill.00023, published
    Feb. 11, 2020). Kind of copy (step 5): the publisher's open-access
    version of record. The page states: "Diagrams and text are licensed
    under Creative Commons Attribution CC-BY 4.0". Lawful. Date: 2026-11-19.
    No fetch obstacle. Read: the whole article text: introduction, Model
    (cell state, perception, update rule, stochastic update, alive masking),
    Experiments 1-4 (growing, "What persists, exists", learning to
    regenerate, rotating the perceptive field), Related Work, Discussion
    (embryogenetic modelling, engineering), and the captions of the
    interactive figure and videos. Not seen: the videos and interactive demo
    themselves (the text was extracted from HTML; the animations' behaviour
    is known only from their captions and the surrounding prose); the Colab
    notebooks; the footnoted references. Text extracted from the HTML
    (scripts and styles stripped) to dl/text.txt.
date: '2026-11-19'
---
<!-- inactive-ok-file: CLAIM-606 CLAIM-672 — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmpz3s4o: Mordvintsev and others 2020 — Growing Neural Cellular Automata

## Contribution

Mordvintsev, Randazzo, Niklasson and Levin (Distill, 2020, DOI 10.23915/distill.00023) train a continuous cellular automaton whose update rule is a small neural network shared by all cells (about 8,000 parameters), so that from a single seed cell it grows a target image (an emoji) on a grid. Each cell holds 16 channels: RGB, an alpha channel marking living cells, and 12 hidden channels. Cells perceive only their 3×3 neighbourhood through fixed Sobel filters, update stochastically without a global clock, and empty cells are zeroed. The article proceeds by three training regimes that separate growing, persisting and regenerating: training only to reach the target at a step count gives growth without stable persistence; a "sample pool" that restarts training from earlier outputs makes the target an attractor; damaging pool samples during training gives strong regeneration.

## Key results

- Experiment 1: training only to reach the target after 64-96 steps grows the pattern, but "Many of the patterns exhibit instability for longer time periods"; "Some tend to die out, some don’t seem to know how to stop growing, but some happen to be almost stable!"
- Interactive figure caption: "Growing models were trained to generate patterns, but don't know how to persist them."
- Experiment 2: the aim is to make "the target pattern an attractor", done by the sample pool, which forces the CA "to learn how to persist or even improve an already formed pattern, in addition to being able to grow it from a seed."
- Interactive figure caption: "Persistent models are trained to make the pattern stay for a prolonged period of time. Interstingly, they often develop some regenerative capabilities without being explicitly instructed to do so".
- Experiment 3: models trained only to grow and persist, then damaged, show "some regenerative properties upon being damaged, but not full re-growth"; models differ, and "the lizard" develops "quite strong regenerative capabilities, without being explicitly trained for it!"
- Experiment 3: nothing in the training stops "explosive mitoses (uncontrolled growth), unresponsiveness to damage (overstabilization), or even self destruction".
- Experiment 3: damaging pool samples during training aims "to increase the basin of attraction for our target pattern"; the resulting models "are much more robust, including to types of damage not experienced in the training process (for instance rectangular damage as above)."
- Experiment 4: rotating the Sobel kernels "produces rotated versions of the pattern for an angle of choosing without retraining".

## Assumptions

- A fixed, shared update rule (the "genome") applied by every cell; perception by fixed gradient filters; per-cell dropout of updates as asynchrony.
- An alive mask imposed from outside the learned rule: cells with no mature neighbour are set to zero each step.
- Damage is erasure of a region of state; there is no turnover of cells or components otherwise.
- The target image is supplied by the loss; the system is trained, not evolved.

## Concepts

- Neural cellular automaton: a recurrent residual convolutional network with per-pixel dropout, in the authors' own phrase.
- Target pattern as an attractor of the coupled cell dynamics; regeneration as a wide basin of attraction.
- Sample-pool training: reusing the system's own outputs as starting states so that it learns to persist from wherever it ventures.
- The analogy to biological morphogenesis, regeneration and an anatomical setpoint (Levin's planarian work, cited in the Discussion).

## Bearing on the record

- CLAIM-566: supports, and qualifies. The three training regimes separate assembly, persistence and regeneration in one system: growth-only models assemble and do not persist; persistence-trained models persist and only "often" regenerate; damage-trained models regenerate robustly. The qualification is that the two later properties are not independent here: training for persistence brings partial regeneration "without being explicitly instructed", because both come from making the target an attractor. Also, regeneration here is after damage, not after turnover, and the regenerating constraints (the learned rule, the alive mask, the perception filters) are supplied and fixed from outside the pattern, so this is regeneration without closure in TERM-070's sense.
- CLAIM-672: supports. The same grown lizard can be held as a nearly stable pattern without repair, or as an attractor that repairs itself after a strike, according to how the rule was trained, which is the claim's point that the mode of persistence is not fixed by the form.
- CLAIM-606: leaves open. A neural CA pattern is a localized structure upheld by continuous updating with an outside alive mask; the article never withdraws the updating or measures what would happen, which is the claim's test.

## Limitations

- Qualitative: the persistence and regeneration results are shown in animations of a few models, not measured across seeds.
- The regenerating rule, perception and alive mask are fixed parts of the model, so the article says nothing about a pattern producing its own constraints.
- The authors speak of an attractor and a basin of attraction informally; no dynamical analysis is given (Masumori et al. 2026, LIT-tmp19eqc, supply one).
