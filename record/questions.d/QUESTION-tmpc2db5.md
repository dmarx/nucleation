---
status: Answered
title: 'When the levels are the spectral subspaces of a symmetric learning operator, cut by eigenvalue, and acquisition is that operator''s own linear evolution, do the order in which the levels refine one another and the order in which they are acquired admit one common chain?'
version: 1
tags:
- learning-theory
- representation-learning
- information-theory
date: '2026-10-21'
line: learned-structure
refines:
- QUESTION-217
summary: >-
  The commuting case of [QUESTION-217](QUESTION-217.md), split off under [ADR-049](../decisions.d/ADR-049.md). Yes, by
  eigenvalue, and by construction: [THEORY-745](../theory.d/THEORY-745.md) for truncated diffusion
  maps, [THEORY-758](../theory.d/THEORY-758.md) for the multilevel diffusion-wavelet chain, and
  [THEORY-774](../theory.d/THEORY-774.md) for gradient flow near a fit in the hopping model. It is
  Conjecture A with every commutator exactly zero. When an independently
  given hierarchy agrees with the operator's order, and where relevance
  enters, stay with [QUESTION-217](QUESTION-217.md).
answered_by:
- THEORY-745
- THEORY-758
- THEORY-774
---

<!-- inactive-ok-file: THEORY-186 THEORY-759 — Proposed; the cases the commuting answer leaves open, cited as open -->

# QUESTION-tmpc2db5: When the levels are the spectral subspaces of a symmetric learning operator, cut by eigenvalue, and acquisition is that operator's own linear evolution, do the order in which the levels refine one another and the order in which they are acquired admit one common chain?

## Answer

Yes. Both orders are the order of the eigenvalues, so they agree by
construction. This is A2's Conjecture A in the case [A, P_ℓ] = 0 exactly,
split off from [QUESTION-217](QUESTION-217.md) on 2026-10-21 ([ADR-049](../decisions.d/ADR-049.md)).

- **One operator, one threshold.** [THEORY-745](../theory.d/THEORY-745.md) (Active, re-derived). For
  the reversible walk of a symmetric kernel on a finite set, keeping the
  diffusion coordinates with |λ_l|^t > δ|λ₁|^t gives maps that are nested
  as t grows. So the steps t order a refinement chain by |λ_l|. The modes
  that t steps of the operator suppress below δ are the ones dropped, in
  the same order. Untruncated, nothing coarsens.
- **Many levels.** [THEORY-758](../theory.d/THEORY-758.md) (Active, re-derived). For a self-adjoint T
  with spectrum in [0, 1], the diffusion-wavelet levels are spectral
  subspaces, exactly nested, and each is T-invariant, so each projector
  commutes with T. Each level is an exactly closed coarse-graining of
  x_{t+1} = Tx_t. Nesting needs no spectral decay.
- **A learner.** [THEORY-774](../theory.d/THEORY-774.md) (Active). In the hopping model the Fisher
  metric is the least-squares metric g = JᵀJ, and its k-th eigenvalue is of
  order t^(3/2−k). Its Connections note, the reader's remark and not the
  paper's, that g is the Gauss–Newton Hessian, so gradient flow near a
  zero-residual fit acquires the eigendirections in the order of λ_k. The
  nested effective models read off the same eigenvectors are a refinement
  chain, so here relevance to the parameters joins the chain too. The
  order holds in the θ coordinates only. Natural-gradient flow would fit
  every direction at one rate.

Each entry says the agreement holds because the levels are the
operator's own spectral projectors. The answer is therefore a statement
of what the commuting case is, not evidence that learners go from coarse
to fine.

## What it leaves to [QUESTION-217](QUESTION-217.md)

The general case, where the levels are given independently of the
learning operator: when such a hierarchy agrees with the operator's
order, and how far it may fail to commute before the orders come apart.
[THEORY-186](../theory.d/THEORY-186.md)'s fine-first case and [THEORY-759](../theory.d/THEORY-759.md)'s order by frequency are
Proposed. Relevance to a task, which [THEORY-745](../theory.d/THEORY-745.md) and [THEORY-758](../theory.d/THEORY-758.md) leave
out, also stays with the parent. So do [THEORY-746](../theory.d/THEORY-746.md), [THEORY-775](../theory.d/THEORY-775.md) and
[CLAIM-394](../claims.d/CLAIM-394.md), which order levels by slowness and say nothing on acquisition.
