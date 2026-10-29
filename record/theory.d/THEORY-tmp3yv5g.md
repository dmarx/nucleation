---
status: Proposed
promote_when: >-
  A measurement, on more than one trained CycleGAN and more than one pair
  of domains, that the information the reverse generator uses to
  reconstruct the source lies in a component of the intermediate image
  its human reader does not perceive: for instance, that removing or
  randomising the high-frequency, low-amplitude component destroys
  reconstruction while leaving judges unable to tell the edited
  intermediate from the original, with the information in that
  component estimated, not shown by example. A demonstration on one model
  by pictures does not settle it.
title: 'A CycleGAN trained to translate aerial photographs to maps and back satisfies its cycle-consistency loss by encoding details of the photograph in a low-amplitude, high-frequency signal in the generated map: the reconstruction recovers details the visible map lacks, is destroyed by noise of three 8-bit levels or by JPEG compression and survives low-frequency change, and the same sensitivity lets an imperceptible perturbation of almost any map make the reverse generator output any chosen photograph'
version: 1
tags:
- representation-learning
- information-theory
date: '2026-10-29'
source:
- LIT-tmp36f4u
summary: >-
  Chu, Zhmoginov and Sandler (2017), LIT-tmp36f4u, §§2–4, read in
  NOTE-tmpty1lx. One trained model on one dataset. The noise curve
  (Fig. 3, 50 photographs) is the only quantitative result; the hidden
  details, the composing edits and the attack are shown by examples.
  Proposed: an empirical finding about one model, said by the authors to
  recur on other datasets, not shown.
---
<!-- inactive-ok-file: CLAIM-342 — Proposed; the claim this finding bears on, cited as open -->

# THEORY-tmp3yv5g: A CycleGAN trained to translate aerial photographs to maps and back satisfies its cycle-consistency loss by encoding details of the photograph in a low-amplitude, high-frequency signal in the generated map: the reconstruction recovers details the visible map lacks, is destroyed by noise of three 8-bit levels or by JPEG compression and survives low-frequency change, and the same sensitivity lets an imperceptible perturbation of almost any map make the reverse generator output any chosen photograph

## Source

Chu, Zhmoginov and Sandler (2017), LIT-tmp36f4u, §§2–4 (pp. 1–4) of arXiv
1712.02950v2; read in NOTE-tmpty1lx.

## What was actually shown

**The model.** CycleGAN with generators F (photograph to map) and G (map to
photograph), trained 500 epochs on about 1,000 of each, with
discriminators for realism and an L1 cycle loss ‖GFx − x‖ + ‖FGy − y‖
(p. 1).

**Hidden detail.** For a photograph not seen in training, GFx reproduces
details absent from Fx, such as a pattern of dots on a roof that the map
shows as solid grey (Fig. 1, p. 2). Local contrast enhancement of Fx shows
a high-frequency signal absent from training maps (Fig. 2, p. 2).

**Its physical form.** V = E‖G(Fx + z) − GFx‖₁ under Gaussian noise z
reaches nearly its maximum at standard deviation 3/256, three levels of an
8-bit image, and falls to its minimum once the noise is spatially
correlated over σ ≥ 2 pixels; JPEG compression of Fx destroys the
reconstruction (Fig. 3, p. 3). The information is in high spatial
frequencies at low amplitude.

**Its consequence.** Gradient descent on ‖Gy − x*‖ from almost any map y₀
finds a map y* that looks like y₀ and that G renders as the chosen x*
(Fig. 5, p. 4). The authors report that the perturbation needed shrinks as
training proceeds (p. 4).

**What could have failed.** The reconstruction could have lost the
undrawn details, as it would if the map carried only what it shows; or
small noise could have left GFx intact, as it would if the information
were in the visible layout.

## What this does not say

- **That this holds for CycleGAN generally.** One model; other datasets are
  asserted (p. 2), not reported.
- **How much information the hidden channel carries.** No estimate is
  given; "hides" is shown by example.
- **Why it happens.** The unequal-complexity explanation is argued
  (THEORY-tmpocg1h), not tested.
- **That the discriminator failed.** Fx passes as a map: the discriminator
  scores realism, which the hidden signal does not disturb.
- **That every cycle-consistent model hides information.** A model whose
  intermediate has room for the source's information (the authors'
  proposed fourth channel, p. 5) need not.
