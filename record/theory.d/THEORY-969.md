---
number: 969
status: Active
formerly:
- THEORY-tmp5t37f
title: 'In hierarchical LDA every document draws all its words from the topics on one root-to-leaf path of a tree drawn from the nested Chinese restaurant process, so the prior is a nested sequence of partitions of the documents, exchangeable in them, and two documents share a topic only by sharing the whole path above it: no document can draw on two sibling subtrees'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-1176. The construction is the paper's §3
    and §4, and §6.3 states the single-path restriction in words. The
    consequences are re-derived below from the generative process, and
    the exchangeability was checked by enumeration. That meets the
    condition for Active under ADR-047 v2.
tags:
- probabilistic-modeling
- information-retrieval
date: '2026-10-26'
source:
- LIT-1542
summary: >-
  Blei, Griffiths and Jordan (2010), [LIT-1542](../literature.d/LIT-1542.md), read in [NOTE-1176](../notes.d/NOTE-1176.md).
  hLDA's overlap between documents is nested by construction: at each
  level of the tree the documents are partitioned, and a document can
  share topics with two others only if one of the two shares all of its
  shared topics with it. It is a statement about the model, not about the
  data, and it says nothing about whether the tree the sampler finds is
  identified. The multiple-path relaxation is the nested HDP's ([LIT-002](../literature.d/LIT-002.md)).
---
<!-- inactive-ok-file: CLAIM-454 — Proposed; the claim this account is set beside, open -->

# THEORY-969: In hierarchical LDA every document draws all its words from the topics on one root-to-leaf path of a tree drawn from the nested Chinese restaurant process, so the prior is a nested sequence of partitions of the documents, exchangeable in them, and two documents share a topic only by sharing the whole path above it: no document can draw on two sibling subtrees

## Source

Blei, Griffiths and Jordan (2010), *Journal of the ACM* 57(2),
[LIT-1542](../literature.d/LIT-1542.md), read in full in [NOTE-1176](../notes.d/NOTE-1176.md) from arXiv 0710.0845v3. The
model is the paper's §3 (the nCRP) and §4 (hLDA). The single-path
restriction is stated in §6.3: "a document can only access the topics that
lie along a single path in the tree." The derivations below are the
record's.

## What was actually shown

hLDA's generative process (§4): every node k of an infinite tree carries a
topic βₖ ~ Dirichlet(η). Document d draws a path cᵈ ~ nCRP(γ), level
proportions θᵈ ~ GEM(m, π), and then, for each word, a level z ~ Mult(θᵈ)
and the word from the topic at level z of cᵈ.

**Nested partitions.** Let the path's node at depth ℓ be cᵈ[ℓ]. Two
documents are in the same depth-ℓ block when cᵈ[ℓ] = cᵉ[ℓ]. Since a node at
depth ℓ has exactly one parent, cᵈ[ℓ] = cᵉ[ℓ] implies cᵈ[ℓ′] = cᵉ[ℓ′] for
every ℓ′ < ℓ. So the depth-(ℓ + 1) partition refines the depth-ℓ one, and
the tree is the nested sequence the paper describes ("A tree can be viewed
as a nested sequence of partitions").

**Overlap is nested.** The topics document d can use are exactly those on
cᵈ. Two documents share the topic at node k iff both paths pass through k,
and then they share every topic above k. If d shares node k with e and
node k′ with f, with k and k′ siblings, then cᵈ passes through two nodes of
the same depth, which a path cannot do. So no document draws on two
sibling subtrees, and the sets of topics documents can use form a chain
under inclusion along each path. Which of a path's topics a given document
actually uses is set by θᵈ and its words. That is the only freedom within
a path.

**Exchangeability.** At each node the choice among children is a CRP over
the documents passing through it, and the CRP's probability of a seating
does not depend on arrival order (§3, citing Pitman). The probability of a
set of paths is the product, over nodes, of the CRP probabilities of the
induced seatings, so it does not depend on the order of the documents
either. Re-checked by enumeration: five depth-two paths, with two
documents sharing a full path and two sharing only the root's child, give
the same probability, 1.12 × 10⁻³ at γ = 1.3, in all 120 orders.

What could have failed: a path-based prior could have allowed a document
to branch, as the multiple-path variant the paper names in §4 would. It
does not, and the paper says so.

## What this does not say

- **Not that the inferred tree is identified.** This is a property of the
  model's support. Whether the sampler's tree is the only one the data
  support is [THEORY-1010](THEORY-1010.md)'s question, and the paper has no theorem.
- **Not that a document's topics are all used.** θᵈ may put almost no mass
  on some levels, so a document's effective topics may be fewer than its
  path's.
- **Not that hierarchy in data must be nested.** The model imposes the
  nesting. A corpus whose documents mix sibling themes is still fitted,
  by assigning each document one path, and the misfit shows only in
  likelihood.
- **Not about the nested HDP.** [LIT-002](../literature.d/LIT-002.md)'s model ([NOTE-023](../notes.d/NOTE-023.md)) gives each word
  its own path and removes the restriction.

## Connections

- **[QUESTION-276](../questions.d/QUESTION-276.md), condition 2.** If documents are members' activity,
  hLDA can express overlapping participation only as shared ancestry,
  which is a partition at every level. That is the restriction T21 noted,
  and the reason it turned to the nested HDP.
- **[CLAIM-454](../claims.d/CLAIM-454.md).** A path is a position in a hierarchy of word
  distributions. Whether members on the same path form a perspective is
  the question the claim says such an allocation leaves open.
- **The author–topic model and the mixed membership blockmodel**
  ([THEORY-972](THEORY-972.md), [THEORY-993](THEORY-993.md)) give overlap of another kind:
  memberships on a simplex, with no nesting.
