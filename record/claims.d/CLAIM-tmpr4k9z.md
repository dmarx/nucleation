---
status: Proposed
title: "Progressive learning can be described by two partial orders, semantic entailment among the regions a representation assigns and informational refinement among its checkpoints in Blackwell's sense, neither of which need be a chain: learning is then the construction of an increasingly informative branching order of distinctions, and a narrower region counts as progress only while it stays correct"
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A training run in which held-out decodability at every semantic level
  only ever grows and every later checkpoint Blackwell-dominates every
  earlier one for every target in the hierarchy, across architectures and
  hierarchies, so that progressive learning is a chain and the partial
  orders add nothing to a single scalar of progress; or an argument that
  checkpoint informativeness cannot be compared by garbling at all.
tags:
- representation-learning
- information-theory
- learning-theory
date: '2026-11-21'
line:
- learned-structure
answers:
- QUESTION-tmpseqwl
bears_on:
- QUESTION-217
rests_on:
- CLAIM-199
grounds:
- THEORY-189
- LIT-tmpk3r9g
- LIT-tmpl34bu
summary: >-
  A33 §2, §7 and §10 and A35 §2–§3 and §9 of the exchange "Rich Get Richer
  Power Laws" (2026-11-21), answering the owner's U21 ([QUESTION-tmpseqwl](../questions.d/QUESTION-tmpseqwl.md)): "both
  entailment and Blackwell informativeness are partial orders", so "a more
  accurate picture of learning might be a branching partial order of
  acquired distinctions", and "the biggest conceptual shift is from
  learning a set of points to learning a structured family of increasingly
  specific, partially ordered regions." Narrowing counts only with
  correctness: "a network could become more confident without becoming
  more correct." The wording is A's (the other assistant in the exchange
  "Rich Get Richer Power Laws", A33 and A35); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: ARG-tmpwo5ou LIT-tmpk3r9g LIT-tmpl34bu — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21; Deferred works registered from that exchange and not read -->

# CLAIM-tmpr4k9z: Progressive learning can be described by two partial orders, semantic entailment among the regions a representation assigns and informational refinement among its checkpoints in Blackwell's sense, neither of which need be a chain: learning is then the construction of an increasingly informative branching order of distinctions, and a narrower region counts as progress only while it stays correct

## The claim

**Two refinements.** A35 §2: "**Semantic refinement:** A sparrow is a more
specific concept than a bird. **Informational refinement:** A
representation at training step t₂ tells us more about a semantic variable
than the representation at step t₁." The first is cone inclusion: in a
transitive cone system c ∈ C(p) implies C(c) ⊆ C(p) ([THEORY-189](../theory.d/THEORY-189.md)). The
second is Blackwell's order applied across checkpoints: Z_(t₂) dominates
Z_(t₁) for Y if P(Z_(t₁) | Y) = T∘P(Z_(t₂) | Y) for a stochastic T independent of
Y ([CLAIM-199](CLAIM-199.md) holds the order and its reach).

**Both partial, so learning branches.** A35's example: a network learns
bird against mammal, then red against blue while partly losing the first;
neither representation dominates; a later one that holds both dominates
both. "A single chain of progressively narrower cones may therefore be too
restrictive." Conjunction makes it richer: a red bird is the intersection
C_red ∩ C_bird, "not … representable by a single cone of the original
family", and under a reference measure P₀ the extra selectivity of a
conjunction is ΔS = log₂[P₀(A)P₀(B)/P₀(A ∩ B)] (A35 §3), which is minus the
pointwise mutual information of the two cone events under P₀: zero for
independent constraints, negative for redundant ones.

**Restriction, softly.** A33 §2: learning as U_i(t + Δt) ⊆ U_i(t) for the
set of interpretations compatible with what the network knows of sample i,
a filtration. But "semantic entailment and temporal refinement are not
identical", a network revises and forgets, so A33 would "treat temporal
cone consistency as a hypothesis about the stable portion of representation
learning, or a soft regularizer". Backward-compatible learning already
constrains updated embeddings to earlier cones (Bui and colleagues,
[LIT-tmpk3r9g](../literature.d/LIT-tmpk3r9g.md)); hyperbolic learning with labels at several granularities is
nearby (Atigh and colleagues, [LIT-tmpl34bu](../literature.d/LIT-tmpl34bu.md)). Both are registered and unread.

**Narrowing is not progress.** A33 §7: "It could shrink its cone around an
incorrect interpretation", so A35 §5 measures progress by coverage,
specificity and stability together: sets A_t(x) with P(Y ∈ A_t(X)) ≥ 1 − δ,
improving "specificity at fixed reliability", with no forced monotone
contraction.

A35's closing hypothesis: "Progressive learning is the dynamical
construction of an increasingly informative partial order over semantic
possibilities, embedded within a high-dimensional measure whose
concentration properties govern the statistical thresholds at which those
distinctions become detectable."

## Checked

A35's table of joint specificity for two cones of 10% each: −log₂ 0.04 =
4.64, −log₂ 0.01 = 6.64, −log₂ 0.001 = 9.97 bits. Arithmetic only; the
overlaps are illustrative, as A35 says.

## Gaps

- **No map to U_i(t).** A33 gives no rule taking a network's parameters or
  embeddings to the set of interpretations it holds, so "set-valued
  learning" is not yet defined.
- **Estimating dominance.** Blackwell dominance between checkpoints needs the
  garbling T, and the record holds that Blackwell-type quantities lack
  finite-data estimators ([CLAIM-235](CLAIM-235.md)). A35 also notes the data-processing
  inequality does not compare checkpoints, since the encoder changes; usable
  information ([THEORY-846](../theory.d/THEORY-846.md), [CLAIM-455](CLAIM-455.md)) is the measure A35 turns to.
- **Cones and caps.** The cost of restriction is computed for spherical caps
  about the origin; how much of it reaches Ganea's cones is [ARG-tmpwo5ou](../arguments.d/ARG-tmpwo5ou.md).
