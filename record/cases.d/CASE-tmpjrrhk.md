---
status: Proposed
title: 'Fairy circles in Sun and colleagues'' shrub–grass kernel model, rerun: the hollow rings are made by the kernel contraction imposed by hand, with or without grass, and grass erodes them rather than holding them in balance, so the model does not show a form whose making and keeping are separate mechanisms'
version: 1
standing: documented
kind: executed-study
tags:
- ecology
- complex-systems
date: '2026-11-14'
line:
- distributed-agency
bears_on:
- QUESTION-281
draws_on:
- THEORY-tmplznge
reported_in:
- NOTE-tmpmu9w0
summary: >-
  An executed simulation study of the fairy-circle scenario in Sun et
  al. (2026), run on 2026-11-14 by a reimplementation of the authors'
  archived notebook (Zenodo 10.5281/zenodo.23751909, FariyCircle.ipynb),
  three seeds. Starting from the authors' shrub-spot pattern, hollow rings
  form when the shrub depletion radius is contracted by hand, whether or
  not grass is present. Without contraction no rings form. With shrub
  recruitment left on, no rings form. With grass present the rings decay
  to almost none by 2,500 steps; without grass they stay unchanged. The
  paper's account, in which grass competition constrains the shrubs and
  the hollow sustains them against "the siege by surrounding grasses", is
  not what the model does. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---

# CASE-tmpjrrhk: Fairy circles in Sun and colleagues' shrub–grass kernel model, rerun: the hollow rings are made by the kernel contraction imposed by hand, with or without grass, and grass erodes them rather than holding them in balance, so the model does not show a form whose making and keeping are separate mechanisms

## The case

**The claim tested.** Sun et al. (2026; read in [NOTE-tmpmu9w0](../notes.d/NOTE-tmpmu9w0.md), account in
[THEORY-tmplznge](../theory.d/THEORY-tmplznge.md)) explain fairy circles in their dryland shrub–grass
transition zone as follows: "Slightly elevated precipitation allows
grasses to occupy the interspaces, intercepting water and constraining
the shrubs' resource-foraging range, which induces hollow center
formation." The rings then persist as metastable states, in "a balance in
which shrubs utilize resources from the central hollow to counter the
siege by surrounding grasses" (p. 6). On that account, making the form
(hollowing) and keeping it (balance with grass) are different mechanisms,
which is what [QUESTION-281](../questions.d/QUESTION-281.md)'s answer asks for.

**What the authors' code does.** The archived notebook first grows a
shrub-spot pattern on a 600 × 600 lattice at s = 0.7, with no grass. Its
shrub kernel has depletion radius 40, facilitation 0.05 and mortality
scaling 5, against Table 1's 20, 0.01 and 0.5; none of the three is
reported in the paper. It crops a 400 × 400 window and then, at s = 0.8,
does three things at once: it seeds grass on 30% of the empty cells,
contracts the shrub radius from 40 to 20 (the paper's "halved"), and
switches shrub recruitment off. A second scenario uses s = 0.9 with radius
15. The notebook runs 500 and 200 steps and plots the result. The paper's
Methods describe the same scenario but not these parameter values.

**The study.** The notebook's update rules were reimplemented and
checked against its code, including its mirror-padded convolution. Six
variants were run from the same spot pattern, varying one factor at a
time. A "ring" is a connected hole of at least 20 cells enclosed by a
shrub patch. The study was run with three seeds (2234, the authors'; 11;
12).

| Variant | Rings, by step (seeds 2234 / 11 / 12) |
|---|---|
| Authors' scenario, s = 0.8, radius 40 → 20, grass, no shrub recruitment | 50: 14/19/10; 500: 8/7/6; 1,000: 3/3/4; 2,500: 0/2/1 |
| Same, radius kept at 40 (no contraction) | 0 at every step, all seeds |
| Same, contraction but **no grass** | 17/25/11, unchanged from step 50 to step 500 |
| Authors' scenario with shrub recruitment on | 0 at every step, all seeds |
| Authors' second scenario, s = 0.9, radius 40 → 15 | 50: 42/41/34; 500: 20/18/15 |
| Same, radius kept at 40 | 0 at every step, all seeds |

Over the authors' s = 0.8 run (seed 2234), shrub cover fell from about 0.16 at step 50 to 0.10 at step 2,500
while the rings fell to almost none. Grass occupied between 0% and 12% of
ring interiors at any checkpoint.

## What it shows

- **The contraction makes the hollows, and grass is not needed.** Rings
  form in every seed with no grass on the lattice, and never without the
  contraction. In the model, "grass constrains the shrubs' foraging range"
  is not a mechanism: the range is shortened by hand, and the shorter
  kernel alone puts the depletion inside the patch.
- **Grass removes the rings rather than keeping them.** With grass
  present they decay steadily; without it they are fixed. The
  persistence that remains is set by the absence of shrub recruitment,
  which leaves nothing to grow back into the hollow, and with recruitment
  on there are no rings to persist.
- **So the model does not separate making from keeping.** One imposed
  change makes the form, and nothing in the dynamics then holds it. It
  lasts a few hundred to a few thousand steps while grass erodes it. That
  is a slow transient, and "metastable" fits it only in the weak sense of
  long-lived. The authors' "supercooling" balance is not what the code
  does.

## What it cannot show

- **Anything about real fairy circles.** Hollow shrub rings in the field
  may arise and persist as the paper says. This tests only the model the
  paper offers as their explanation.
- **That no kernel model could do it.** A model in which grass competition
  shortened the shrub kernel dynamically, rather than by hand, might
  separate the two mechanisms. That model is not in the paper.
- **Robustness beyond three seeds, one window size and these thresholds.**
  The ring count depends on the 20-cell threshold; the zero and nonzero
  contrasts do not.

## Reproduction

The reimplementation (`fc.py`, about 100 lines, NumPy and SciPy) and its
per-seed outputs were written in the session's scratchpad and are not
committed: this record holds no code. The study can be rebuilt from the
authors' notebook by applying the one-factor changes in the table above.
