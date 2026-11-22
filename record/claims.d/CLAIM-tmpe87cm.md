---
status: Proposed
title: 'Under multiplicative co-occurrence with any implication structure among binary attributes and positive strengths, every attribute is an exact linear readout of the full-rank PMI embedding; on a balanced tree the PMI eigenvectors are branch contrasts whose eigenvalues fall strictly with depth, so a truncated embedding keeps exactly the shallow attributes and merges siblings below the cut'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-147: the
    derivation QUESTION-025's first limb asks for. The closed form is
    checked numerically in scratch/studies/lead-147/ (tree_pmi.py and its
    tests).
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation's steps: that the column space of
  J X Λ Xᵀ J equals that of J X when Λ is positive diagonal; that the
  affine terms of the PMI vanish under double centring; or the eigenvalue
  computation for the balanced tree (the branch contrasts as eigenvectors,
  their eigenvalues and multiplicities). Or a balanced-tree instance of
  the model, with positive strengths, whose PMI spectrum departs from the
  closed form. Not defeated by real co-occurrence departing from the
  model, which the claim does not assert, by unbalanced trees, whose
  eigenvectors the claim does not state, or by negative strengths, which it
  excludes.
tags:
- representation-learning
- mathematics
date: '2026-11-22'
line:
- pragmatic-transport
answers:
- QUESTION-025
bears_on:
- QUESTION-178
grounds:
- THEORY-185
summary: >-
  The model of [THEORY-185](../theory.d/THEORY-185.md) with its independence dropped: binary
  attributes closed upward under any implication order, each shared
  attribute multiplying co-occurrence by a positive factor, so the PMI is
  X Λ Xᵀ plus affine terms. Implication does not remove the linear
  directions. Every attribute is read out exactly, by an affine map, from
  the full-rank spectral embedding, and the recovered incidence and its
  concept lattice equal the generating ones. What implication changes is
  the spectrum. On a balanced b-ary tree, the eigenvectors are branch
  contrasts rather than one per attribute. A branching at depth ℓ gives
  eigenvalue μ_ℓ = w Σ_{ℓ′>ℓ} λ_ℓ′ b^(D−ℓ′), with multiplicity (b−1)bˡ,
  and these fall strictly with depth for any positive strengths. So a
  rank-(b^K − 1) embedding reads out exactly the attributes of depth at
  most K. Below the cut, each attribute's readout is the same constant on
  every descendant of its depth-K ancestor, so siblings merge. Along a
  tree, PMI additivity is therefore the same thing as piecewise constancy
  on the finest groups: it has content only where attributes cross-cut,
  as in analogy families. The wording is the assistant's (Claude, in this
  session); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-186 THEORY-201 LIT-267 CLAIM-119 — Proposed; cited as the accounts this derivation meets, not as settled -->

# CLAIM-tmpe87cm: Under multiplicative co-occurrence with any implication structure among binary attributes and positive strengths, every attribute is an exact linear readout of the full-rank PMI embedding; on a balanced tree the PMI eigenvectors are branch contrasts whose eigenvalues fall strictly with depth, so a truncated embedding keeps exactly the shallow attributes and merges siblings below the cut

## The claim

**Model.** There are n words and d binary attributes, and X is the n × d
0/1 incidence. An implication order on the attributes (k ⇒ l) holds in X:
x_ik = 1 gives x_il = 1. Which combinations occur is otherwise free. A
tree is the case where incomparable attributes exclude each other. Each
shared attribute multiplies the co-occurrence of two words by
exp(λ_k), with λ_k > 0. The PMI matrix is then

  M = X Λ Xᵀ + u 1ᵀ + 1 uᵀ + c 1 1ᵀ,  Λ = diag(λ).

This is [THEORY-185](../theory.d/THEORY-185.md)'s model without its independence. Its ±1 coding of
attributes differs from the 0/1 coding only by affine terms of this form.

**1. Every attribute is a linear readout.** Let J = I − 11ᵀ/n. Double
centring removes the affine terms, since J1 = 0, so
J M J = (J X Λ^{1/2})(J X Λ^{1/2})ᵀ. Its column space is that of
J X Λ^{1/2}, and so that of J X, because Λ^{1/2} is invertible. The
spectral embedding E (eigenvectors of J M J times the square roots of
their eigenvalues, all nonzero ones kept) spans the same space. So each
centred attribute column is E w_k for some w_k, and x_k = E w_k + mean(x_k)
exactly. Thresholding at ½ recovers X, and the concept lattice of the
recovered context is the generating one. Nothing here uses independence.
When columns of X are dependent, for instance when a parent is the
disjoint union of its children, the vectors v_k in e_i = Σ_k x_ik v_k are
not unique, but the readout is still exact.

**2. The balanced tree.** Take a complete b-ary tree of depth D, with an
attribute at every node below the root and w words at each leaf. Each word
carries its leaf and all its ancestors. λ_ℓ is the strength at depth ℓ.
Then (X Λ Xᵀ)_ij = Σ λ_ℓ over the depths ℓ ≤ depth(lca(i, j)). Take a node
at depth ℓ and a vector constant on each of its b child subtrees, summing
to zero, and zero elsewhere. Rows outside the node's subtree see a
constant and give 0. A row in child j gets −Λ_{≤ℓ} N_{ℓ+1} c_j from the
other children and N_{ℓ+1} Λ_{≤ℓ} c_j + S_{ℓ+1} c_j from its own. Here
Λ_{≤ℓ} = Σ_{ℓ′≤ℓ} λ_ℓ′, N_ℓ′ = w b^(D−ℓ′) is the number of words under a
depth-ℓ′ node, and S_{ℓ+1} = Σ_{ℓ′>ℓ} λ_ℓ′ N_ℓ′. The vector is therefore
an eigenvector, with

  μ_ℓ = w Σ_{ℓ′=ℓ+1}^{D} λ_ℓ′ b^(D−ℓ′),  multiplicity (b−1) bˡ,  ℓ = 0 … D−1.

These Σ_ℓ (b−1)bˡ = b^D − 1 contrasts, with the constant vector and the
zero-eigenvalue contrasts within a leaf, span the space. Since
μ_ℓ − μ_{ℓ+1} = w λ_{ℓ+1} b^(D−ℓ−1) > 0, the plateaus are ordered by depth
for every choice of positive strengths. Shallow branchings always come
first. This is unlike [THEORY-185](../theory.d/THEORY-185.md)'s raw-ratio clause, which needs a
condition on the strengths.

**3. Truncation.** The indicator of a depth-ℓ attribute is constant on the
children of each node above depth ℓ. So it lies in the span of the
constant vector and the contrasts of levels 0 … ℓ−1. The top b^K − 1
centred eigenvectors (levels below K) therefore read out exactly every
attribute of depth ≤ K. For a deeper attribute (depth ℓ > K), the
least-squares readout is b^{−(ℓ−K)} on the whole subtree of its depth-K
ancestor and 0 elsewhere. That value is identical for the attribute and
all its siblings and cousins under that ancestor. With threshold ½, a
probe misses every member and never fires outside the ancestor. The
recovered context is the tree cut at depth K, and its lattice is the
generating lattice cut there.

**4. What additivity means along a tree.** The indicators of all the
ancestors span exactly the indicators of the finest groups (here the
leaves). So "the PMI is additive across the attributes of the hierarchy"
says only that words in the same finest group have the same PMI row, up
to their own affine term. Additivity constrains the PMI only where
attributes cross-cut. In a 2 × 2 analogy quadruple, the interaction
P_a − P_b − P_c + P_d must vanish. A pure tree cannot produce that
quadruple across branches, because each attribute lies in one branch. So
implication alone gives tree-shaped directions and no parallelograms;
parallelograms need a product of orders.

**Checks.** scratch/studies/lead-147/tree_pmi.py builds the model, and its
tests (test_tree_pmi.py) verify the closed form to 1e-14 for several b, D
and w. They also verify exact full-rank readout for random implication
DAGs, and the truncation statement, including the readout value below the
cut. derivation_check.txt holds one run.

## Connections

- The branch contrasts are the tree wavelets that Saxe, McClelland &
  Ganguli ([LIT-862](../literature.d/LIT-862.md), [THEORY-186](../theory.d/THEORY-186.md)) found for item similarity in a
  supervised linear network. Here they come from co-occurrence and PMI.
- The ordering by depth fits Cagnetta & Wyart's finding ([THEORY-201](../theory.d/THEORY-201.md))
  that a finite corpus shows only the shallow levels of a hierarchy. In
  this model, noise of a given size masks the deepest plateaus first.
- For [LIT-267](../literature.d/LIT-267.md) and [CLAIM-119](CLAIM-119.md), the first step survives implication
  at full rank. At the ranks embeddings use, a lattice read off by
  thresholding is the hierarchy cut at a depth set by the spectrum.

## What it does not say

- That real co-occurrence follows this model. That is the measurement
  ([QUESTION-178](../questions.d/QUESTION-178.md) and the case filed with this claim).
- Anything about the eigenvectors of unbalanced trees or general
  contexts. Part 1 holds for them; parts 2 and 3 are stated for the
  balanced tree.
- Anything under noise. The ordering by depth suggests that noise removes
  deep levels first, but no bound is derived.
- That a direction exists for each attribute in the sense of one
  eigenvector per attribute. The readout is exact, but the eigenvectors
  are contrasts.
