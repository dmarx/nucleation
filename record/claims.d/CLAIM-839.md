---
number: 839
status: Proposed
formerly:
- CLAIM-tmpr4k9z
title: "Progressive learning can be described by two partial orders, semantic entailment among the regions a representation assigns and informational refinement among its checkpoints in Blackwell's sense, neither of which need be a chain: learning is then the construction of an increasingly informative branching order of distinctions, and a narrower region counts as progress only while it stays correct"
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    After the readings of Bui et al. (LIT-2989, NOTE-tmpvu3vp) and Ghadimi
    Atigh et al. (LIT-2993, NOTE-tmpyyvdy): the sentence calling them
    unread replaced in place by what they show, with four qualifications
    on Bui et al.; in the grounds, LIT-2989 replaced by its reading
    THEORY-tmpe9367 (ARG-tmpf206e) and LIT-2993 removed, its reading
    corroborating the semantic half only (ARG-tmpv9jbe); dated notes
    added, including the assistant's norm-growth claim CLAIM-tmpxcy5s
    (ARG-tmpotmon). Title and thesis unchanged.
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
- QUESTION-512
bears_on:
- QUESTION-217
rests_on:
- CLAIM-199
grounds:
- THEORY-189
- THEORY-tmpe9367
summary: >-
  A33 §2, §7 and §10 and A35 §2–§3 and §9 of the exchange "Rich Get Richer
  Power Laws" (2026-11-21), answering the owner's U21 ([QUESTION-512](../questions.d/QUESTION-512.md)): "both
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
<!-- inactive-ok-file: ARG-153 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-tmpe9367 THEORY-tmpsj6u9 CLAIM-tmpxcy5s ARG-tmpf206e ARG-tmpv9jbe ARG-tmpotmon CLAIM-816 — Proposed; the readings of Bui et al. and Ghadimi Atigh et al. filed 2026-11-22, the assistant's norm-growth claim, the arguments that say how each bears here, and a claim cited for context -->

# CLAIM-839: Progressive learning can be described by two partial orders, semantic entailment among the regions a representation assigns and informational refinement among its checkpoints in Blackwell's sense, neither of which need be a chain: learning is then the construction of an increasingly informative branching order of distinctions, and a narrower region counts as progress only while it stays correct

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
[LIT-2989](../literature.d/LIT-2989.md)); hyperbolic learning with labels at several granularities is
nearby (Ghadimi Atigh and colleagues, [LIT-2993](../literature.d/LIT-2993.md)).

*Revised 2026-11-22, after reading both:* Bui and colleagues
([THEORY-tmpe9367](../theory.d/THEORY-tmpe9367.md)) do constrain updated embeddings to earlier cones, with
four qualifications. The constraint is a soft penalty (a hinge weighted
0.3), and the paper never reports how many new embeddings lie inside
their cones. The cones are per item, apexed at the same item's old
embedding, not cones of concepts. They link two separately trained
models, the old one frozen, not checkpoints of one run. And the order is
imposed by design, not observed in learning. What it bears out is A33's
"soft regularizer" reading ([ARG-tmpf206e](../arguments.d/ARG-tmpf206e.md)). Ghadimi Atigh and colleagues
([THEORY-tmpsj6u9](../theory.d/THEORY-tmpsj6u9.md)) nest cones semantically, a label's cone containing its
descendants', for each sample at one time, with no temporal restriction;
they bear on the semantic half only ([ARG-tmpv9jbe](../arguments.d/ARG-tmpv9jbe.md)).

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
  about the origin; how much of it reaches Ganea's cones is [ARG-153](../arguments.d/ARG-153.md).

## Note of 2026-11-22: Bui, Yang, Chen, Neves, Ju, Ying, Shah and Zhao, read

Supports the restriction half in part, and qualifies it. Read
([NOTE-tmpvu3vp](../notes.d/NOTE-tmpvu3vp.md), [THEORY-tmpe9367](../theory.d/THEORY-tmpe9367.md)), the scheme is exactly A33's fallback,
temporal cone consistency as a soft regularizer, and it works: removing
the cone term costs most when the architecture changes (CIFAR100 CMC@1
compatibility 0.937 with it, −0.178 without). The four qualifications
are now in the body. Two more points. Per item, the generations form a
chain of nested cones, not a branching order, so the claim's branching
is untouched. And the scheme's narrowing is built in: every point of
such a cone lies farther from the origin than its apex, so a satisfied
constraint makes each embedding more "certain" whether or not it is
correct ([CLAIM-tmpxcy5s](CLAIM-tmpxcy5s.md), the assistant's, checked numerically). That is
a demonstrated case of the rule this claim ends with, that a narrower
region counts as progress only while it stays correct ([ARG-tmpotmon](../arguments.d/ARG-tmpotmon.md)).
The Blackwell half is untouched.

## Note of 2026-11-22: Ghadimi Atigh, van Spengler, Long, Ayoughi, Kasarla and Mettes, read

A weak parallel, for the semantic half only. Read ([NOTE-tmpyyvdy](../notes.d/NOTE-tmpyyvdy.md),
[THEORY-tmpsj6u9](../theory.d/THEORY-tmpsj6u9.md)), the paper supervises with regions whose narrowness
matches the label's specificity: "the more specific a sample's label,
the more narrowly defined the region in the embedding space should be for
optimization" (§1). It has no checkpoints, branching or temporal
restriction, and its "coarse-to-fine" (§3.2) names a label projection,
not an order of learning. The reading moves from grounds to
corroborates ([ARG-tmpv9jbe](../arguments.d/ARG-tmpv9jbe.md)). It also shows that cones alone leave
samples "biased towards internal classes", so the radial placement
needs its own term ([CLAIM-816](CLAIM-816.md)).
