---
status: Skimmed
paper: LIT-tmp3u6bb
title: 'Hospedales and others 2020 — Meta-Learning in Neural Networks: A Survey'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2004.05439 (served arXiv:2004.05439v2, 7
    Nov 2020; HTTP 200, application/pdf). Kind of copy (step 5): arXiv
    preprint posted by the authors (the survey later published in IEEE
    TPAMI; the copy states no venue); lawful. Date: 2026-11-19. Nothing
    stopped the fetch. Text extracted with pdftotext to dl/text.txt. Read:
    abstract; §1 introduction; §2 background in full (definition, 2.1
    formalizing meta-learning incl. meta-overfitting, bilevel and feed-
    forward views, 2.2 history, 2.3 related fields: transfer, domain
    adaptation/generalization, continual learning, multi-task learning,
    hyperparameter optimization, hierarchical Bayes, AutoML); §3 taxonomy
    (3.1 previous, 3.2 proposed); §4.1 the opening of meta-representation
    (parameter initialization, optimizer, feed-forward models) and its
    discussions of transductive, symbolic representations and amortization;
    §4.3 meta-objective and episode design in full; §5.7 continual, online
    and adaptive learning; §6 challenges and open questions (task
    distributions, meta-generalization, task families, computation cost and
    many-shot); §7 conclusion. Skipped: §4.1's later meta-representation
    items (losses, architectures, attention, modules, datasets, curricula,
    etc.), §4.2 meta-optimizer beyond its opening, §5 applications other
    than 5.7 (few-shot, RL, NAS, Bayesian, unsupervised, active learning,
    etc.), Table 1 beyond its caption, references.
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmphsr99 CLAIM-tmp5gbzr CLAIM-tmp8ljvp — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmpfnzxf: Hospedales and others 2020 — Meta-Learning in Neural Networks: A Survey

## Contribution

Hospedales, Antoniou, Micaelli and Storkey (2020) survey neural-network
meta-learning, define it as learning an explicitly defined meta-objective
end to end over multiple learning episodes, formalize it in task-
distribution, bilevel and feed-forward views, position it against transfer,
continual, multi-task learning and hyperparameter optimization, and propose
a taxonomy on three axes: meta-representation (what is learned),
meta-optimizer (how) and meta-objective (why). Skimmed: taxonomy,
formalization, meta-objective and episode design, continual learning and
challenges.

## Key results

- **Definition** (§1): a model "gains experience over multiple learning
  episodes – often covering a distribution of related tasks – and uses
  this experience to improve its future learning performance".
- **What sets contemporary meta-learning apart** (§2): "an explicitly
  defined meta-level objective, and endto-end optimization of the inner
  algorithm with respect to this objective".
- **Meta-overfitting** (§2.1): "meta-overfitting is an issue whereby the
  metaknowledge learned on the source tasks does not generalize to the
  target tasks", seen as "learning an inductive bias ω that constrains
  the hypothesis space of θ too tightly around solutions to the source
  tasks".
- **Against transfer learning** (§2.3): "In TL the prior is extracted by
  vanilla learning on the source task without the use of a
  meta-objective"; against multi-task learning, "the point of
  meta-learning is often to solve unseen future tasks".
- **Continual learning is mostly not meta-learning** (§2.3): "most
  continual learning methodologies are not meta-learning methodologies
  since this meta objective is not solved for explicitly".
- **The taxonomy** (§3.2): "Meta-Representation (“What?”)",
  "Meta-Optimizer (“How?”)", "Meta-Objective (“Why?”)".
- **Objectives can target learning speed** (§4.3): when validation loss is
  summed after each inner step, "metatraining also encourages faster
  learning in the base task".
- **Amortization** (§4.1): "how much task-specific optimization is
  performed during meta-testing vs how much learning is amortized during
  meta-training"; MAML "provides limited amortization", feed-forward
  models are "fully amortized".
- **Continual-learning meta-objectives** (§5.7): a support set with one new
  task and "the query set contains examples drawn from all tasks seen until
  now".
- **Open challenges** (§6): meta-generalization to tasks "drawn from a
  different distribution than the training tasks" is "inevitable in many
  potential practical applications"; task families "may not be
  available"; online meta-optimization methods "suffer from a short-horizon
  bias".

## Assumptions

- A declared task family p(T), or a single task split into episodes; a
  meta-objective that can be written down.
- Neural networks trained end to end; the survey excludes random search and
  Bayesian hyperparameter optimization as meta-learning.

## Concepts

- **Meta-knowledge ω**, **base/inner** and **meta/outer** learning,
  **bilevel optimization**, **meta-training/meta-testing**,
  **support/query sets**.
- **Meta-underfitting**, **meta-overfitting**, **meta-generalization**,
  **memorisation** (after Yin et al.).
- **Amortization** (none, limited, semi-, fully amortized).
- **Short-horizon bias** of online meta-optimization.

## Bearing on the record

- **QUESTION-tmpwqepn**: supports the candidate answer that meta-learning's
  objective already targets future learning (its definition says so),
  and maps the space of such objectives (speed, asymptotic performance,
  continual retention, robustness). It also confirms the limit: every
  objective presupposes a declared task family or episode design, and the
  survey lists out-of-distribution meta-generalization and the absence of
  task families as open. It leaves the question's unspecifiable future
  open.
- **CLAIM-tmp8ljvp**: supports its clause that the objective is not new,
  and names the meta-level analogue of its failure: meta-overfitting as an
  inductive bias that "constrains the hypothesis space of θ too tightly",
  close to the claim's raised cost of reaching other capabilities. The
  survey frames it as a generalization failure across tasks, which is the
  rival naming the claim's defeated_if anticipates.
- **CLAIM-tmp5gbzr**: leaves open; the survey's amortization axis is the
  trade of paying during meta-training against paying at meta-test, a
  relative of CLAIM-303 and CLAIM-569 rather than of this claim.
- **CASE-tmphsr99**: supports separating adaptation modes as the case does
  (feed-forward/in-context versus fine-tuning are fully versus limited
  amortization), and gives a vocabulary for the arms.

## Limitations

- A survey: no results of its own; skimmed, not read in full, so its
  application sections are unchecked here.
- As of 2020, before in-context learning in large language models was
  the dominant form of the topic.
