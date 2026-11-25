---
number: 2047
status: Proposed
formerly:
- THEORY-tmpte85d
title: 'Laplacian eigenmaps minimize Dirichlet energy'
statement: >-
  Belkin and Niyogi show that embedding the vertices of a weighted
  neighbourhood graph by minimizing the Dirichlet energy Σ(y_i − y_j)²W_ij
  under the constraints yᵀDy = I and yᵀD1 = 0 gives the eigenvectors of Ly =
  λDy with the smallest non-zero eigenvalues, that the constraints exist to
  stop the energy from collapsing every vertex onto a constant, and that the
  graph Laplacian so used is a discrete analogue of the Laplace-Beltrami
  operator on the data manifold
version: 1
source:
- LIT-2794
tags:
- representation-learning
- mathematics
date: '2026-11-19'
promote_when: >-
  The reduction of the constrained minimization to the generalized
  eigenproblem (§2) is re-derived, which is elementary linear algebra; the
  Laplace-Beltrami analogy is asserted only as an analogy and needs
  nothing further.
summary: >-
  From the reading of [LIT-2794](../literature.d/LIT-2794.md) in [NOTE-2120](../notes.d/NOTE-2120.md). Belkin, Niyogi
  (2001), Advances in Neural Information Processing Systems 14 (NIPS
  2001), read from the proceedings PDF on papers.nips.cc. Laplacian
  eigenmaps embed the vertices of a heat-kernel-weighted neighbourhood
  graph by minimizing the Dirichlet energy Σ(y_i − y_j)²W_ij under yᵀDy =
  I and yᵀD1 = 0, which gives the eigenvectors of Ly = λDy with the
  smallest non-zero eigenvalues. The constraints are there because the
  energy alone collapses every vertex onto a constant, and each connected
  component is treated separately. The graph Laplacian is argued,
  heuristically, to approximate the Laplace-Beltrami operator. The authors
  speculate that the natural clusters it brings out might ground
  perceptual categories. Here because A27 grounded the owner's U12
  connection, dissipation of differences as self-supervised learning, in
  it ([CLAIM-481](../claims.d/CLAIM-481.md)'s note of 2026-11-19; [LIT-228](../literature.d/LIT-228.md) holds the SSL equivalence).
  It has the energy and the collapse but no flow. Read in its NOTE.
---

# THEORY-2047: Laplacian eigenmaps minimize Dirichlet energy

## The account

For a symmetric weight matrix W on a graph, D = diag(Σ_j W_ij) and L = D − W, Σ_ij (y_i − y_j)²W_ij = 2yᵀLy. Minimizing it under yᵀDy = 1 gives the smallest generalized eigenvector of Ly = λDy, which is the constant vector, eigenvalue 0, collapsing all vertices onto one value; on a connected graph it is the only such vector, and the constraint yᵀD1 = 0 removes it, leaving the eigenvector of the smallest non-zero eigenvalue. In m dimensions the constraint YᵀDY = I prevents collapse onto a subspace of dimension less than m, and the solution is the m eigenvectors after the constant. On a disconnected graph each component is embedded separately. The authors motivate heat-kernel weights by the heat equation on the manifold and note the method's relation to spectral clustering.

## What it does not show

No convergence of the graph Laplacian to the Laplace-Beltrami operator is proved here, and no dynamics: the paper minimizes an energy, it does not study a flow. The suggestion that natural clusters could ground categories is speculation.
