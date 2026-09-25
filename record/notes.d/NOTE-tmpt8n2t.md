---
status: Skimmed
paper: LIT-tmp2ny9z
title: 'Nested Hierarchical Dirichlet Processes'
version: 1
date: '2026-09-25'
summary: >-
  Letting each word follow its own path through a shared topic tree, via document-specific distributions over paths (a global nCRP as base for per-document nCRPs), fixes the single-path restriction of the nested CRP and, with stochastic variational inference, scales hierarchical topic models to millions of documents.
---

<!-- inactive-ok-file: LIT-tmp2ny9z — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmpt8n2t: Nested Hierarchical Dirichlet Processes

## Contribution

The paper introduces the nested hierarchical Dirichlet process for learning tree-structured topic hierarchies. Unlike the nested Chinese restaurant process, where a document uses topics along one root-to-leaf path, the nHDP gives each document its own distribution over paths in a shared tree, so individual words can take different paths and documents can mix themes from different branches. The authors derive a stochastic variational inference algorithm for it and demonstrate it on 1.8 million New York Times articles and roughly 2.7 million Wikipedia pages.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Motivation: the nCRP's single path forces either too few topics per document (shallow trees) or too many nodes (deep trees), and duplicates topics across subtrees (e.g. a "sports medicine" article) (§1, Fig. 1).
- Construction: as the HDP places a global DP beneath per-document DPs, the nHDP places a global nCRP (stick-breaking form) beneath per-document nCRPs over the same tree (§1, §3).
- Inference: stochastic variational inference with truncated stick-breaking, splitting local (per-document) and global variables; the arXiv abstract also mentions greedy per-document subtree selection (§4, arXiv abstract).
- Batch comparison on JACM, Psych. Review and PNAS abstracts: variational nHDP beats variational nCRP on held-out predictive log-likelihood on all three, and beats Gibbs nCRP on the two larger ones (Table 2, §5).
- Large scale: on NYT and Wikipedia the stochastic nHDP is compared with stochastic LDA and stochastic HDP on held-out predictive log-likelihood as documents stream in, plus tree-size and per-document statistics and example topic trees (Figs. 2-11); sensitivity to hyperparameters shown (Figs. 12-14).

## Open questions

- The advantage over nCRP grows with corpus and document size in Table 2, but the Gibbs-nCRP beats variational nHDP on the smallest corpus; check how much of the large-scale gain is due to the model versus the inference method.
- Large-scale evaluation is held-out likelihood plus qualitative trees; no human evaluation of hierarchy quality was seen in the skim.
- ML link: a canonical example of stochastic variational inference applied to a deep Bayesian nonparametric model; relevant to history of scalable VI rather than to current practice.
