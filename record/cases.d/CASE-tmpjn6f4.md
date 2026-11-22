---
status: Proposed
title: 'In small models trained by gradient descent on MSE without re-whitening, the whitened class-separation singular values do not grow as (4t/N)^(1/4): without weight decay they grow exponentially or as a steep power and spread apart while NC1 stalls, and with weight decay they grow, stall and regrow, or collapse in a late instability; Han, Papyan and Donoho''s renormalized flow, run as a control, matches the law to five digits'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-035. Code,
    tests, per-item results and a summary under scratch/studies/lead-035/.
standing: documented
kind: executed-study
tags:
- learning-theory
- representation-learning
- loss-landscapes
date: '2026-11-22'
line:
- learned-structure
bears_on:
- QUESTION-051
- QUESTION-181
draws_on:
- THEORY-278
summary: >-
  [LEAD-035](../leads.d/LEAD-035.md) asked for the singular values ω_j of Σ_W^(−1/2)M̃ in trained
  models, set against the (4t/N)^(1/4) law that Han, Papyan and Donoho
  derive for unconstrained features under a flow re-whitened after every
  step ([THEORY-278](../theory.d/THEORY-278.md)). In numpy, four classes, 50 per class, full-batch
  gradient descent on MSE, three seeds: the renormalized flow, run as a
  control, matches the exact solution to 4×10⁻⁵ (late log-log slope
  0.256). Every model trained without re-whitening departs from the law.
  With no weight decay, unconstrained features (gradient of the
  least-squares loss alone, or joint descent on classifier and features)
  grow ω_j exponentially and spread them apart (max/min to 4–175), and
  two ReLU networks, one with batch normalization, grow them with late
  log-log slopes 2.4–3.9 and max/min 2.4–15; NC1 stalls at 0.05–0.42
  throughout. With weight decay 5×10⁻⁴, the plain network's ω_j grow,
  stall while NC1 falls, and regrow; the batch-normalized one's rise to
  about 10⁴ and then fall tenfold in a late loss spike. Toy data and small
  models, so it bears on [QUESTION-181](../questions.d/QUESTION-181.md) by kind, not at the scale Han and
  colleagues measured.
---
<!-- inactive-ok-file: THEORY-797 CLAIM-tmpcpr7t LIT-tmpxyq0h — Proposed, Deferred or new; the proposal this study tests, the claim filed from it, and the work registered beside it -->

# CASE-tmpjn6f4: In small models trained by gradient descent on MSE without re-whitening, the whitened class-separation singular values do not grow as (4t/N)^(1/4): without weight decay they grow exponentially or as a steep power and spread apart while NC1 stalls, and with weight decay they grow, stall and regrow, or collapse in a late instability; Han, Papyan and Donoho's renormalized flow, run as a control, matches the law to five digits

## What was asked

[LEAD-035](../leads.d/LEAD-035.md), from [NOTE-783](../notes.d/NOTE-783.md)'s open question: "A measurement of the SNR
singular values in a trained network, against (4t/N)^(1/4), would settle
whether the closed form describes training." The closed form is
[THEORY-278](../theory.d/THEORY-278.md)'s derived half (Lemma 5, Proposition 2, Corollary 1 of [LIT-974](../literature.d/LIT-974.md)):
on the central path, with no weight decay and features re-whitened to
Σ_W = I after every step (assumption A3), dω_j/dt = (1/N) ω_j/(C + ω_j²)²,
so ω_j ~ (4t/N)^(1/4) and max/min ω → 1. [THEORY-797](../theory.d/THEORY-797.md) proposes that
trained networks follow these dynamics; [QUESTION-181](../questions.d/QUESTION-181.md) asks whether they do.

## What was done

All in numpy, CPU, full-batch gradient descent on the sample-averaged MSE,
C = 4 classes, N = 50 per class, three seeds per setting
(scratch/studies/lead-035/, README there).

- **Time unit.** A pytest check confirms that one small step of the
  projected (renormalized) flow moves each ω_j at Lemma 5's rate when t is
  the learning rate times the number of steps and gradients are of the
  sample-averaged loss. Every model uses that unit.
- **Control, `ufm-renorm`.** Unconstrained features in R^16, the projected
  gradient of the least-squares loss, re-whitened after each step.
- **A3 dropped, `ufm-lsplain`.** The same, with the classifier at its
  least-squares optimum, but no projection and no re-whitening.
- **Ordinary training of the same model, `ufm-joint`.** Gradient descent
  on (W, b, H) jointly, no weight decay.
- **Networks.** A ReLU MLP 20-64-32 (`mlp2`) and a 20-64-64-32 MLP with
  full-batch batch normalization before each ReLU (`mlp3bn`), on a
  four-class Gaussian mixture in R^20, learning rate 0.05, 200,000 steps,
  weight decay 0 or 5×10⁻⁴. ω_j is read from the penultimate features.
- Measured at log-spaced steps: ω_j, L_LS (Lemma 1's loss, checked against
  the least-squares fit), the network's own loss L, NC1 = tr(Σ_W Σ_B†)/C,
  training accuracy. Runs stop where ω leaves double precision.

## Results

Late window is the last decade of t; slopes are of log ω_j on log t
(the law says 0.25); "spread" is max/min ω at the end.

| Model | Late slopes | Spread (start → end) | NC1 at end | Shape |
|---|---|---|---|---|
| ufm-renorm | 0.256–0.257 | 1.4–2.3 → 1.000 | 0.005 | the law; within 4×10⁻⁵ of Proposition 2's exact solution, ω/(4t/N)^(1/4) = 0.993 at t = 4×10⁶ |
| ufm-lsplain | 2.7–4.8 | → 4.4–175 | 0.05–0.11 | exponential (in the late window an exponential leaves 170–2000 times less residual than a power) |
| ufm-joint | 2.6–5.5 | → 4.2–160 | 0.05–0.11 | exponential, as lsplain, at the same rate per unit t; L⊥/L_LS ≤ 0.006, so it is on the central path |
| mlp2, wd 0 | 2.4–3.6 | 1.3–2.0 → 2.6–15 | 0.22–0.42 | steepening; full training accuracy by t ≈ 30 |
| mlp3bn, wd 0 | 2.4–3.9 | 1.4–1.7 → 2.4–11 | 0.26–0.31 | steepening |
| mlp2, wd 5×10⁻⁴ | 0.11–0.30 | 1.3–2.0 → 1.1–1.5 | 10⁻⁴–3×10⁻³ | fast growth to ω ≈ 150, a stall from t ≈ 500 to 4000 while NC1 falls tenfold, then regrowth (local slope 0.5–1 at the end) |
| mlp3bn, wd 5×10⁻⁴ | −0.2 to −0.6 | 1.4–1.7 → 2.0–4.1 | 10⁻⁶–10⁻⁴ | growth to ω ≈ 10⁴ by t ≈ 4000, then a tenfold fall with a 100-fold rise in L_LS |

The absolute level, against (4t/N)^(1/4) in this time unit, is 40–55 times
the law for mlp2 with weight decay, 500–800 times for mlp3bn with weight decay, and 6×10³ to 10⁵ times for the rest; the
networks' features are not free, so the unit is not theirs, but the slopes
and spreads do not depend on it.

Two things explain the unconstrained-features results, and the first is
shown, not only measured. The least-squares loss is unchanged by any
invertible affine map of the features, so its gradient is orthogonal to
every such direction and plain gradient flow conserves Σ_T and the global
mean (test `test_plain_ls_gradient_conserves_second_moment`). Without
re-whitening, ω can then grow only by Σ_W turning singular inside a fixed
Σ_T, along the C − 1 directions the least-squares readout uses, which
need not be the class-mean directions. So ω diverges while
tr(Σ_W Σ_B†) stalls: separation in whitened coordinates without
collapse of variability onto the means. The renormalization A3 is what
forbids that route; it forces the class means themselves outward, slowly,
and that is the quarter power.

The networks stay near the central path while L_LS is above 10⁻⁴
(L⊥/L_LS ≤ 0.35 for mlp2, ≤ 1.3 for mlp3bn, after the first transient,
t ≥ 5), as Han and colleagues measured; the share rises late, as L_LS
falls toward rounding. So the departure from the law is not a departure
from the central path; it is the missing renormalization.

## What it shows

In every un-renormalized setting tried, the ω_j are not (4t/N)^(1/4).
Without weight decay they grow far faster and spread apart, which is
[QUESTION-181](../questions.d/QUESTION-181.md)'s and [THEORY-797](../theory.d/THEORY-797.md)'s "no": "near the central path, the ω_j
spread apart or stall while L⊥_LS stays negligible". With weight decay,
the setting of Han and colleagues' experiments, ω neither follows the law
nor settles in 200,000 steps. The closed form describes the renormalized
flow and, in these models, not gradient descent.

## Limits

- Toy scale: four classes, 200 samples, synthetic Gaussian data, MLPs of
  32–64 units, full-batch gradient descent with no momentum, no
  augmentation, three seeds. Han and colleagues trained VGG, ResNet and
  DenseNet with SGD, momentum and weight decay on five image datasets.
- The batch normalization here normalizes each unit's total variance over
  the full batch, without affine parameters; it is not the
  within-class re-whitening of A3 and was not meant to be.
- With weight decay, 200,000 steps (t = 10⁴) did not settle ω; the
  late-window slopes there average a stall and a regrowth and are not a
  power-law regime. The batch-normalized runs end in an instability whose
  cause was not studied.
- The direction claim of Corollary 2 (the limit set by the early singular
  vectors) was not measured.
- One step size per model; the exponential rate in unconstrained features
  is per unit t and matched between lsplain and joint, but step-size
  dependence was not swept.
