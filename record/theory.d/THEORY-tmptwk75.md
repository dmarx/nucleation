---
status: Proposed
promote_when: 'A test of the link from the optimal learner to trained networks, on the quantity the theory predicts: the threshold model size or mixing ratio, predicted in advance from the measured loss-versus-size curve of the second domain and the facts'' total entropy Htot, matched by networks trained to convergence over several seeds and several values of r, with recall rising over a width of about Htot past the threshold. It is refuted if the measured thresholds depart systematically from (1/(r·p))^(1/(α+1)), or if networks below the threshold do learn the facts given enough further training, which would make the wall a matter of dynamics and not of allocation. More sigmoid-shaped curves in r or in size are the wrong kind of evidence: they show a threshold, not that capacity allocation sets it.'
title: Language models trained by gradient descent on a mixture of random facts and other data reach the capacity-optimal allocation, so the model size and the mixing ratio at which they begin to learn the facts are those of an optimal capacity-bounded learner
version: 1
tags:
- learning-theory
- information-theory
date: '2026-10-20'
source:
- LIT-984
summary: The link that [THEORY-293](THEORY-293.md)'s title asserted before the promotion audit narrowed it (batch 036) to the optimal learner's theorem and the observation of a threshold in Pythia models. Gu, Lyu, Li and Zhang (2025), [LIT-984](../literature.d/LIT-984.md), read in [NOTE-796](../notes.d/NOTE-796.md), explain the trained models' thresholds by the optimal learner's. The one quantitative check, a size exponent of 1.152 against a predicted 1.283, is recorded against it. Filed under [ADR-047](../decisions.d/ADR-047.md) v4 so the wide form stays a thesis evidence can confirm or reject.
extends:
- THEORY-293
answers:
- QUESTION-176
---

# THEORY-tmptwk75: Language models trained by gradient descent on a mixture of random facts and other data reach the capacity-optimal allocation, so the model size and the mixing ratio at which they begin to learn the facts are those of an optimal capacity-bounded learner

## Source

Gu, Lyu, Li and Zhang (2025), [LIT-984](../literature.d/LIT-984.md), §§3–5, read in [NOTE-796](../notes.d/NOTE-796.md). The optimal
learner's threshold is Theorem 4.3; the Pythia runs are §3 (Figs. 1–4, Table
1).

## What is asserted, and by whom

The thesis is that SGD-trained language models behave as the optimal
capacity-bounded learner does: they allocate capacity optimally between the
facts and the other domain, so their threshold model size scales as
(1/(r·p))^(1/(α+1)) and their recall rises within about Htot past it. The
authors assert it ([NOTE-796](../notes.d/NOTE-796.md), C5, weak). They also extend it, more weakly
still, to the frequency at which open model families learn a fact (C6); that
extension is not filed here.

## What the record holds toward it

- [THEORY-293](THEORY-293.md) (Active): Theorem 4.3 for the optimal learner, and a threshold in model size and in mixing ratio in Pythia models from 14M to 6.9B on synthetic biographies mixed into web text, mostly single-seed.
- Against it, so far: the measured size exponent, 1.152, is about 10% below the predicted 1.283, with no interval ([NOTE-796](../notes.d/NOTE-796.md), Limitations). Below the threshold ratio, much longer training barely helps (C4, moderate), which fits allocation rather than dynamics but was extrapolated from fits over r in [0.2, 0.55].

## What would confirm or reject it

Thresholds predicted in advance and matched across seeds and mixing ratios
confirm it; a systematic departure from the predicted exponent, or networks
below the threshold that learn the facts with enough further training,
reject it. [QUESTION-176](../questions.d/QUESTION-176.md) asks the same thing as a question; this entry is the
answer the authors propose.
