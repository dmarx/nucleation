---
status: Proposed
title: 'A symmetry of the data gives a network a balanced partition of its units only where the symmetry group acts on the units by permuting them: weights fixed by such an action make the group act by automorphisms of the weighted unit graph, whose orbits are always a balanced partition; where the group acts only on the inputs, or on hidden coordinates by mixing rather than permuting, data symmetry fixes no partition of units, and for a vocabulary larger than the width the relabelling group cannot permute the units nontrivially at all'
version: 1
role: thesis
warrant: demonstrated
defeated_if: >-
  An error in the derivation below: a group of automorphisms of a weighted
  directed graph whose orbits are not a balanced partition, or a
  nontrivial action of the symmetric group on n letters, n at least 5, on
  fewer than n points whose image has more than two elements.
tags:
- mathematics
- network-science
- representation-learning
date: '2026-11-19'
line:
- learned-structure
- formal-apparatus
bears_on:
- QUESTION-tmpex36a
summary: >-
  The assistant's, from a check offered on 2026-11-19 after filing the
  exchange "Topological protection explained" and accepted by the owner
  the same day. It tests the route the filing first wrote into
  [QUESTION-tmpex36a](../questions.d/QUESTION-tmpex36a.md) for the owner's U9 hunch: data invariant under token
  relabelling keeps gradient descent in the symmetric weights
  ([THEORY-981](../theory.d/THEORY-981.md)), weight symmetry gives orbit synchrony ([THEORY-276](../theory.d/THEORY-276.md)), and
  balanced partitions generalize that ([THEORY-1065](../theory.d/THEORY-1065.md)). The route holds only
  where the relabelling group permutes the network's units. It does not
  in Li and Webb's models ([THEORY-tmpmtmq7](../theory.d/THEORY-tmpmtmq7.md)), whose residual width (768) is
  below most of their vocabularies, so their results cannot be reached by
  this route and the hunch needs learned, not symmetry-forced, partitions.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-tmpz825j — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-tmpmtmq7 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-tmpj540o: A symmetry of the data gives a network a balanced partition of its units only where the symmetry group acts on the units by permuting them: weights fixed by such an action make the group act by automorphisms of the weighted unit graph, whose orbits are always a balanced partition; where the group acts only on the inputs, or on hidden coordinates by mixing rather than permuting, data symmetry fixes no partition of units, and for a vocabulary larger than the width the relabelling group cannot permute the units nontrivially at all

## The derivation

**1. Fixed weights give automorphisms.** Let a group G act on a
network's units by a permutation σ, and suppose the weights are fixed by
it: w(σi, σj) = w(i, j) for all units i, j and all σ in G. Then each σ is
an automorphism of the weighted directed graph of units.

**2. Automorphism orbits are balanced.** Take an orbit O and two units i
and j = σi in one orbit P. The map k ↦ σk sends the inputs of i bijectively
onto the inputs of j, preserves weights, and maps O onto itself. So the
total input weight to i from O equals that to j from O, for every pair of
orbits: the orbit partition is balanced, and by [THEORY-1065](../theory.d/THEORY-1065.md) its synchrony
subspace is invariant under any admissible dynamics on the graph. That is
[THEORY-276](../theory.d/THEORY-276.md)'s orbit synchrony, stated as a partition.

**3. Without a permutation action there is no partition.** If G acts
only on the input coordinates (token one-hots) and trivially on the
units, weights fixed by G satisfy W g = W for the first layer: every
token's column is the same, and the network cannot tell tokens apart. A
trained network that does tell them apart has left the fixed subspace,
so the data's symmetry constrains it, at most, through its population
gradient, and imposes no partition. If G acts on hidden coordinates by an
orthogonal mixing that is not a permutation, fixed weights intertwine the
actions but no unit is mapped to another, and there are no orbits of
units.

**4. Width bounds the action.** For n ≥ 5, any homomorphism from the
symmetric group on n letters into the symmetric group on m < n letters has
an image of order at most 2: its only normal subgroups are the trivial
group, the alternating group and itself, and it cannot embed in the
smaller symmetric group since n! > m!, so the kernel contains the
alternating group. So when the vocabulary V
exceeds the number of units in a layer, relabelling can permute that
layer's units only through the sign of the relabelling, or not at all.

## What it shows about the hunch

[THEORY-981](../theory.d/THEORY-981.md)'s confinement needs the network to be equivariant under the
group, which for a permutation of tokens means the group acting on every
layer, and needs training to start in the fixed subspace. Li and Webb's
transformers (width 768) were trained at vocabularies up to 10,000 with
learned embeddings and random initialization. By step 4 the relabelling
group cannot permute their residual units at V > 768 (their MLPs' widths
were not checked), and by step 3 a
mixing action gives no unit partition. So their symbolic representations
were not forced into a balanced partition of units by the symmetry of
their data. If role abstraction coincides with balanced structure among
units there, it is learned structure, the kind Velarde and colleagues
report (unread), and the question stays open in that form.

## What it does not show

That such learned partitions are absent. That symmetry is irrelevant to
role abstraction: the invariant rule direction Li and Webb measure can be
a fixed vector of a mixing action without any partition of units.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Velarde and colleagues ([THEORY-tmpz825j](../theory.d/THEORY-tmpz825j.md)), read, give a route to balanced partitions of units that needs no symmetry of the data: covering partitions persist under gradient descent by equal updates, and are said to attract SGD, by citation to Chen and colleagues (2023). They report that automorphisms are "never observed" in trained networks. That is compatible with the claim and does not test its derivation. It confirms that if partitions coincide with role abstraction in Li and Webb's models, the mechanism would be of this learned kind.

No status change.
