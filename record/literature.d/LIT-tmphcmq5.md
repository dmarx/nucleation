---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmp54otp](../notes.d/NOTE-tmp54otp.md)); worth reading as the only study in the batch of connectivity under federated averaging. Client models, though close in weight space, leave the low-loss region of the global model more as client data grow more heterogeneous, and FedAvg global models trained from one initialisation under different heterogeneity are separated on the straight line (accuracy drops of about 10%) but joined by a one-bend polygonal chain. A mean-field bound, extending the dropout-stability route of Kuditipudi et al. and Shevchenko and Mondelli, makes the connectivity error grow with √h(α), a heterogeneity factor, and shrink with width; width and heterogeneity trends in MNIST and CIFAR-10 runs agree. The theory treats heterogeneity as isotropic Gaussian noise on each neuron''s update, an assumption the paper checks only by plotting noise norms.'
title: 'Mode Connectivity and Data Heterogeneity of Federated Learning'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the arXiv HTML of v1 (29 September 2023), main text,
    Appendix A and Appendix B (the proofs of Theorems 1–2, followed through
    Proposition 1 and the Theorem 1 bound). No venue is given on arXiv and
    none was confirmed. Filed with the owner's batch on mode connectivity
    and model merging (ADR-027). Not held in the Anthology of the SOTA: a
    grep of its record for the arXiv id and the title found nothing. The
    anthology holds FedAvg itself (ANTH-LIT-307).
tags:
- loss-landscapes
- anthology-candidate
date: '2026-10-03'
published: '2023-09-29'
arxiv: '2309.16923'
first_author: 'Zhou'
keywords:
- 'federated learning'
- 'mode connectivity'
- 'data heterogeneity'
- 'mean-field theory'
- 'dropout stability'
- 'loss landscape visualization'
- 'FedAvg'
extends:
- LIT-tmplpsy5
implementations: []
summary: >-
  Zhou, Zhang & Tsang (2023), preprint. Under Dirichlet label skew and PACS
  domain shift, low-loss overlaps between FedAvg client models and the
  global model shrink as heterogeneity grows; client models stay close to
  the global one yet move in different directions within a round. Global
  models from one initialisation under different heterogeneity have
  function dissimilarity above 0.2, show an error barrier on the line, and
  are joined without barrier by a polygonal chain. A mean-field analysis of
  two-layer networks bounds dropout and connectivity errors by terms
  proportional to √h(α) and decreasing in width N.
---

<!-- inactive-ok-file: LIT-tmpqno1r — Proposed: named for its parallel argument that data structure sets the barrier, not leaned on -->

# LIT-tmphcmq5: Mode Connectivity and Data Heterogeneity of Federated Learning

Tailin Zhou, Jun Zhang and Danny H. K. Tsang (2023), arXiv preprint — [ARXIV-2309.16923](https://arxiv.org/abs/2309.16923)

## Key takeaways

- **Heterogeneity shrinks the overlap between client and global solutions.**
  On VGG11 with CIFAR-10 and PACS, the region where a client model and the
  global model both have low loss is smaller under α = 0.1 than under α =
  0.5 (Dirichlet label skew), and smaller on PACS (§IV, Figs. 2–3). Client
  models stay near the global model throughout training but move in
  different directions within a round (Fig. 4).
- **Global models are distinct modes in one region.** FedAvg models from one
  initialisation trained under α = 0.1, 0.2 and 0.5 disagree on more than 20%
  of predictions, are closer to each other than to their initialisation,
  show an error barrier on the line that grows with heterogeneity and over
  rounds, and are joined without barrier by a one-bend polygonal chain
  (§V, Figs. 5–7; accuracy drops of about 10% on the line, App. A-B).
- **A bound in heterogeneity and width.** Modelling heterogeneity as
  Gaussian noise of variance βh(α) on each neuron's FedAvg update (Assumption
  5), the global model of a two-layer network is ε_D-dropout stable and two
  such models are ε_C-connected by a 7-segment path, with ε_D, ε_C ∝
  √h(α)·((√log N + z)/√N + √ε(√(D + log N) + z)) (Theorems 1–2). Dropout
  error and the linear barrier fall with width, from N = 200 to N = 6400, in
  MNIST runs (§VII, Fig. 9).

## Standing in the record

Filed with the owner's batch on mode connectivity and model merging, under
`loss-landscapes` ([ADR-027](../decisions.d/ADR-027.md)). Federated averaging is weight averaging done
repeatedly, so this is the batch's view of merging from inside training:
the global model is the average of client models, and the question is
whether the average lies where the clients' losses are low.

It extends Kuditipudi et al. ([LIT-tmplpsy5](LIT-tmplpsy5.md)). Theorem 2 is their result that
dropout-stable networks are connected by a short piecewise-linear path,
applied to FedAvg models ("Following [20], we demonstrate that dropout-stable
NNs in FL have mode connectivity"), with the dropout stability supplied by a
mean-field analysis after Shevchenko and Mondelli (2020) and Mei et al.,
none of which the record holds. The paper uses Garipov et al.'s path
objective and polygonal chain ([LIT-tmpotq71](LIT-tmpotq71.md)) for its non-linear paths, and
cites Entezari et al. ([LIT-tmp2uwzo](LIT-tmp2uwzo.md)) for permutation as a possible source of
the linear barrier, which its function-dissimilarity measurement argues
against for these models.

The anthology holds FedAvg ([ANTH-LIT-307](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-307.md)). The batch's GNN reading
([LIT-tmpqno1r](LIT-tmpqno1r.md)) makes a parallel argument, with graph homophily in place of
client heterogeneity as the data property that sets the barrier. Mirzadeh et
al. ([LIT-tmp2e9aa](LIT-tmp2e9aa.md)) report the opposite outcome for a shared start: their
multitask and continual solutions are linearly connected, while these global
models, also from one start, are not.
