---
status: Read
paper: LIT-tmp2gj7u
title: 'Nichol and others 2018 — On First-Order Meta-Learning Algorithms'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1803.02999 (served arXiv:1803.02999v3,
    22 Oct 2018; HTTP 200, application/pdf). Kind of copy (step 5): arXiv
    preprint posted by the authors (OpenAI technical report; no other venue
    stated in the copy); lawful. Date: 2026-11-19. Nothing stopped the
    fetch. Text extracted with pdftotext to dl/text.txt. Read: abstract and
    sections 1-8 in full (meta-learning an initialization, FOMAML, the
    Reptile algorithm, sine-wave case study, Taylor-series analysis 5.1, the
    solution-manifold argument 5.2, Omniglot/Mini-ImageNet results, inner-
    loop gradient combinations, mini-batch overlap, discussion, future
    work). Skipped: the step-by-step algebra of eqs. 13-24 and 36-41 was
    followed only for its conclusions; the appendix (hyperparameter tables)
    and references.
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmparjas: Nichol and others 2018 — On First-Order Meta-Learning Algorithms

## Contribution

Nichol, Achiam and Schulman (OpenAI, 2018) introduce Reptile, a first-order
meta-learning algorithm for an initialization: sample a task, run k steps
of SGD or Adam on it, and move the initialization toward the trained
weights. They show by a Taylor expansion that Reptile, first-order MAML and
MAML share the same leading terms, one minimizing the expected loss (joint
training) and one maximizing the inner product of gradients from different
mini-batches of the same task, which they read as within-task
generalization. Few-shot results match MAML.

## Key results

- **The algorithm** (abstract): Reptile "works by repeatedly sampling a
  task, training on it, and moving the initialization towards the trained
  weights on that task".
- **With one inner step it is joint training** (§3): with k = 1, "this
  algorithm corresponds to stochastic gradient descent on the expected
  loss"; with k > 1, "Reptile converges to a solution that’s very
  different from the minimizer of the expected loss".
- **Joint training can be useless** (§4, sine waves): the expected loss
  "is minimized by the zero function f (x) = 0", while MAML and Reptile
  give an initialization that outputs about zero before training but whose
  internal features let it fit a sampled wave after training.
- **Two terms** (§5.1): "the first term minimizes the expected loss (joint
  training), the second and more interesting term maximizes within-task
  generalization"; the ratio of the second to the first "increases
  linearly with both the stepsize α and the number of iterations k".
- **Informal second account** (§5.2): Reptile seeks a point "close (in
  Euclidean distance) to each task τ ’s manifold of optimal solutions",
  flagged as "a informal argument and should be taken much less seriously".
- **Few-shot results** (§6.1, Tables 1-2): Mini-ImageNet 5-shot 5-way
  65.99% with transduction against MAML's 63.11%; slightly worse than MAML
  on Omniglot.
- **More inner steps help** (§6.2): "all the methods improve as the number
  of mini-batches increases".
- **Ordinary SGD does part of this already** (§7): "when doing stochastic
  gradient descent, we are automatically performing a MAML-like update
  that maximizes the generalization between different minibatches", so
  "joint training plus fine tuning will continue to be a strong baseline".
- **RL negative** (§8): "So far, we have obtained negative results, since
  joint training is a strong baseline".

## Assumptions

- A task distribution from which tasks are sampled; small αk for the
  Taylor analysis ("the Taylor series approximation only holds for small
  αk", §5.1).
- Within-task generalization across mini-batches stands in for fast
  learning on new tasks.
- Mini-batches in the inner loop are distinct (momentum and overlap hurt,
  §6.1 footnote, §6.3).

## Concepts

- **Reptile**, **FOMAML**, **joint training** (minimizing the expected loss
  over tasks).
- **AvgGrad** and **AvgGradInner**: the joint-training term and the
  gradient-inner-product term.
- **Shared-tail versus separate-tail FOMAML**.
- **Transduction** via batch normalization at test time.

## Bearing on the record

- **[CASE-tmphsr99](../cases.d/CASE-tmphsr99.md)**: supports Reptile as a cheap meta-trained arm (no
  second derivatives, no train/test split per task), and sets a design
  rule: the arm differs from joint training only for k > 1, and its
  difference grows with αk, so the case's matched resources must fix k and the
  inner budget, with joint training plus fine-tuning on the same tasks as
  the control, which the authors call a strong baseline. Their RL result
  is negative, so the arm should not be extended to the interactive arms
  without a pilot.
- **[CLAIM-tmp8ljvp](../claims.d/CLAIM-tmp8ljvp.md)**: qualifies the claim's view that a present objective
  and future adaptability are separate. If, as §7 suggests, plain SGD
  already contains a term rewarding generalization between mini-batches,
  ordinary training is partly a meta-objective; overconsolidation, if it
  occurs, would be that term ceasing to pay, not its absence. The paper
  does not test this outside few-shot classification.
- **[QUESTION-tmpwqepn](../questions.d/QUESTION-tmpwqepn.md)**: supports the candidate answer that the objective
  of fast adaptation is already in the literature, and adds that it can be
  had nearly for free (first-order, from joint-training-like updates). It
  leaves open everything about tasks not drawn from the training
  distribution.

## Limitations

- An OpenAI report; the copy states no peer-reviewed venue.
- The second theoretical account is informal by the authors' own flag.
- Only Omniglot and Mini-ImageNet; small CNNs; RL results negative and not
  shown.
- "there is a large gap between training and testing error" (§8): meta-
  overfitting is noted and not studied.
