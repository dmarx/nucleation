---
number: 514
status: Open
formerly:
- QUESTION-tmpsy8qn
title: 'Does the incidence order of a network''s singular strata, which stratum lies in the closure of which, map onto the order in which its representations refine one another, and how far from one-to-one is the map?'
version: 1
tags:
- learning-theory
- loss-landscapes
- representation-learning
date: '2026-11-21'
line:
- learned-structure
refines:
- QUESTION-217
summary: >-
  A37 §6, A39 §§7–8 and A43 §14 of the exchange "Rich Get Richer Power
  Laws" (2026-11-21): the hypothesis that "the stages of hierarchical
  representation learning correspond to transitions among functionally
  distinct strata of a singular neural-network model", sharpened into a
  map Φ from strata to a semantic partial order. A says it "requires a
  model-specific construction". The assistant adds the smallest
  construction where the strata and their incidence can be stated. The
  wording is A's (the other assistant in the exchange "Rich Get Richer
  Power Laws", A37, A39, A43); adopting it is the owner's call.
---

<!-- inactive-ok-file: CASE-302 CLAIM-828 CLAIM-555 — Proposed or new -->

# QUESTION-514: Does the incidence order of a network's singular strata, which stratum lies in the closure of which, map onto the order in which its representations refine one another, and how far from one-to-one is the map?

## The question

A39 §8 describes a network by "three coupled objects": the image M = F(Θ),
a stratification Θ = ∪ S_α by local functional identifiability, and for
each stratum a semantic order P_α. It asks for the map S_α ↦ P_α. A39
closes: "whether the incidence structure of the singular strata — which
strata lie in the closures of which others — can be mapped onto the
partial order of semantic entailment". A43 §14 names the map Φ and says it
"need not be one-to-one". Several strata can carry the same semantics,
and "two semantic refinements can be acquired within the same generic
full-rank stratum, without crossing a singular boundary". So "a partial
correspondence would already be an interesting discovery".

A37 §6 states the cautions. "A boundary of an entailment cone is not
automatically an algebraic singularity." A semantic order can classify
strata, but singular geometry needs "an appropriate analytic local model".
A39 §7: "A semantic distinction becoming usable does not require the
parameter-to-function map to change rank at that moment."

## What the assistant adds

**Which stratification.** A43 says the incidence relation is a partial
order "under the usual stratification conditions" and does not say which.
For an analytic or semialgebraic map, the sets of constant Jacobian rank
are a natural first cut, but they need not satisfy the frontier condition
(that a stratum meeting another's closure lies wholly inside it). A
Whitney stratification refining them exists for such maps and does
satisfy it, so its incidence relation is a partial order. An answer must
say which stratification it uses.

**The smallest case.** In F(a, b) = (a + b, ab) ([CASE-302](../cases.d/CASE-302.md)), the rank
strata are {a ≠ b} (rank 2, dimension 2) and {a = b} (rank 1, dimension
1), and {a = b} lies in the closure of {a ≠ b}. The incidence order has
two elements: "two mechanisms merged" below "two mechanisms distinct".
The learning coefficient at a true point is 3/4 on the lower stratum and 1
on the upper. If the two mechanisms were the features for two sibling
concepts, this is the smallest instance of the correspondence A
proposes: a two-element chain mapped onto "undifferentiated" below
"differentiated". It is a stipulation, not a finding. The question is
whether trained networks supply such a map nontrivially.

**The gate model.** In [CLAIM-828](../claims.d/CLAIM-828.md), a parent gate g moves a child's
threshold. The child's inactive stratum {a = b = 0} lies in the closure of
its active ones, and the gate's dependency order is a candidate for the
semantic order. That is one construction of a partial Φ, in a model where
the semantic order is put in by hand.

## What would count as an answer

A model with a semantic order fixed independently of its parameters (a
synthetic hierarchy), its strata computed or their learning coefficients
estimated, and the map Φ exhibited: which incidence relations carry
semantic refinements and which refinements happen inside one stratum. A
negative answer is a model in which refinements and stratum changes are
unrelated. [CLAIM-555](../claims.d/CLAIM-555.md) holds a nearby identification, of the compatibility
complex of a training distribution's demands with the singular geometry,
from which a semantic order might be read. The entailment-cone side of
the exchange (Ganea et al., [LIT-866](../literature.d/LIT-866.md)) is another theme of the same filing.

## Note of 2026-11-21: Hoogland, Wang, Farrugia-Roberts, Carroll, Wei & Murfet, read

Leaves the question open (NOTE-tmp2pgi8). The paper measures no strata.
Its estimated coefficient is not monotone over training (it falls in three
stages), so if stages climbed a chain of strata by incidence, the estimate
would not show the climb monotonically, or the estimate tracks something
else. No relation written.
