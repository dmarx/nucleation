---
number: 759
status: Active
formerly:
- CLAIM-tmpj540o
title: 'A symmetry of the data gives a network a balanced partition of its units where the symmetry group acts on the units by permuting them: weights fixed by such an action make the group act by automorphisms of the weighted unit graph, whose orbits are always a balanced partition; where the group acts only on the inputs, or on hidden coordinates by an orthogonal mixing that maps no unit onto a multiple of another, data symmetry fixes no partition of units; and for a vocabulary of at least five tokens larger than a layer''s width, the relabelling group can permute that layer''s units only through the sign of the relabelling, as a group of order at most two'
version: 2
history:
- version: 2
  date: '2026-11-20'
  note: >-
    Narrowed and promoted at the status review's ruling (the owner
    delegated these rulings). It has no premises and nothing objects to
    it; the derivation was re-derived step by step and checked by
    scratch/formal/claim759_orbit_balance_check.py, whose three controls
    fire. Two clauses of the title were corrected as mis-statements
    (README §2, kind 3), with a dated note only. Step 4 shows the
    relabelling group can act on a narrower layer through its sign, a
    nontrivial action of order two, so "cannot permute the units
    nontrivially at all" was false; it now says "only through the sign of
    the relabelling", and step 4's condition n ≥ 5 is in the title. And
    "only where" claimed an exclusivity the case split did not cover:
    step 3 handled an action on the inputs alone and an orthogonal mixing
    that moves no unit to another, but not a signed or scaled permutation
    of units, which is orthogonal or monomial and still maps units onto
    units. That gap is a hole in the case split that nobody asserted as a
    thesis, so it is recorded under "What it does not show", not filed.
    Step 1 now says biases are among the fixed weights, which THEORY-1065's
    cell types need, and the body's "(unread)" for Velarde and colleagues,
    read since, now points to THEORY-2055. The old title was "A symmetry of the data gives a
    network a balanced partition of its units only where the symmetry
    group acts on the units by permuting them: weights fixed by such an
    action make the group act by automorphisms of the weighted unit graph,
    whose orbits are always a balanced partition; where the group acts only
    on the inputs, or on hidden coordinates by mixing rather than
    permuting, data symmetry fixes no partition of units, and for a
    vocabulary larger than the width the relabelling group cannot permute
    the units nontrivially at all".
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
- QUESTION-492
summary: >-
  The assistant's, from a check offered on 2026-11-19 after filing the
  exchange "Topological protection explained" and accepted by the owner
  the same day. It tests the route the filing first wrote into
  [QUESTION-492](../questions.d/QUESTION-492.md) for the owner's U9 hunch: data invariant under token
  relabelling keeps gradient descent in the symmetric weights
  ([THEORY-981](../theory.d/THEORY-981.md)), weight symmetry gives orbit synchrony ([THEORY-276](../theory.d/THEORY-276.md)), and
  balanced partitions generalize that ([THEORY-1065](../theory.d/THEORY-1065.md)). The route holds only
  where the relabelling group permutes the network's units. It does not
  in Li and Webb's models ([THEORY-2035](../theory.d/THEORY-2035.md)), whose residual width (768) is
  below most of their vocabularies, so their results cannot be reached by
  this route and the hunch needs learned, not symmetry-forced, partitions.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-2055 — Proposed; cited in this filing of 2026-11-19 -->
<!-- inactive-ok-file: THEORY-2035 — Proposed; cited in this filing of 2026-11-19 -->

# CLAIM-759: A symmetry of the data gives a network a balanced partition of its units where the symmetry group acts on the units by permuting them: weights fixed by such an action make the group act by automorphisms of the weighted unit graph, whose orbits are always a balanced partition; where the group acts only on the inputs, or on hidden coordinates by an orthogonal mixing that maps no unit onto a multiple of another, data symmetry fixes no partition of units; and for a vocabulary of at least five tokens larger than a layer's width, the relabelling group can permute that layer's units only through the sign of the relabelling, as a group of order at most two

## The derivation

**1. Fixed weights give automorphisms.** Let a group G act on a
network's units by a permutation σ, and suppose the weights, biases
included, are fixed by it: w(σi, σj) = w(i, j) for all units i, j and all σ in G. Then each σ is
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
orthogonal mixing that maps no unit onto a multiple of another, fixed
weights intertwine the actions but no unit is mapped to another, and there
are no orbits of units.

**4. Width bounds the action.** For n ≥ 5, any homomorphism from the
symmetric group on n letters into the symmetric group on m < n letters has
an image of order at most 2: its only normal subgroups are the trivial
group, the alternating group and itself, and it cannot embed in the
smaller symmetric group since n! > m!, so the kernel contains the
alternating group. So when the vocabulary V, at least 5,
exceeds the number of units in a layer, relabelling can permute that
layer's units only through the sign of the relabelling, or not at all.

**Re-derived and checked at the status review of 2026-11-20.** Step 2: for
σ in G, i in P and O an orbit, Σ_{k∈O} w(k, i) = Σ_{k∈O} w(σk, σi) =
Σ_{k'∈σO} w(k', σi), and σO = O, so every unit of P receives the same input
weight from O. Step 4: a homomorphism's kernel is normal; for n ≥ 5 the
normal subgroups of S_n are 1, A_n and S_n; a trivial kernel would embed
S_n in S_m with m < n, impossible since n! > m!; so the kernel contains
A_n and the image has order 1 or 2. scratch/formal/claim759_orbit_balance_check.py
finds every orbit partition balanced on 279 weighted digraphs averaged over
a random permutation group, and every homomorphism from S_5 to S_4 or S_3
of image order 1 or 2, order 2 included. Its controls fire: the same
graphs before averaging are unbalanced on their orbit partitions; S_4 maps
onto S_3, so n ≥ 5 is needed; and the enumerator finds the identity of S_5.

## What it shows about the hunch

[THEORY-981](../theory.d/THEORY-981.md)'s confinement needs the network to be equivariant under the
group, which for a permutation of tokens means the group acting on every
layer, and needs training to start in the fixed subspace. Li and Webb's
transformers (width 768) were trained at vocabularies up to 10,000 with
learned embeddings and random initialization. By step 4 the relabelling
group can permute their residual units at V > 768 only through the sign
of the relabelling, which tells no token from another (their MLPs' widths
were not checked), and by step 3 a
mixing action gives no unit partition. So their symbolic representations
were not forced into a balanced partition of units by the symmetry of
their data. If role abstraction coincides with balanced structure among
units there, it is learned structure, the kind Velarde and colleagues
report ([THEORY-2055](../theory.d/THEORY-2055.md), read since: see the note of 2026-11-19 below), and the question stays open in that form.

## What it does not show

That such learned partitions are absent. Anything about a group that maps
units onto units up to a sign or a positive scale, a signed permutation
with an odd activation or a permutation with rescaling across a ReLU: such
an action is neither step 1's permutation nor step 3's mixing, and its
orbits need not be balanced in step 2's sense. That symmetry is irrelevant to
role abstraction: the invariant rule direction Li and Webb measure can be
a fixed vector of a mixing action without any partition of units.

## Note of 2026-11-19: readings for the exchange "Topological protection explained"

Velarde and colleagues ([THEORY-2055](../theory.d/THEORY-2055.md)), read, give a route to balanced partitions of units that needs no symmetry of the data: covering partitions persist under gradient descent by equal updates, and are said to attract SGD, by citation to Chen and colleagues (2023). They report that automorphisms are "never observed" in trained networks. That is compatible with the claim and does not test its derivation. It confirms that if partitions coincide with role abstraction in Li and Webb's models, the mechanism would be of this learned kind.

No status change.

## Note of 2026-11-19: Chen, Kunin, Yamamura and Ganguli, read
<!-- inactive-ok-file: THEORY-2009 — Proposed; cited from the readings of 2026-11-19 -->

Compatible, and parallel ([THEORY-2009](../theory.d/THEORY-2009.md); [NOTE-2127](../notes.d/NOTE-2127.md)). Chen and colleagues' permutation sets come from the hidden-unit permutation symmetry of the parameterization, which does act on the units by permuting them, for every dataset. Its fixed sets are orbit partitions of the kind the claim's second step describes. But the group is the architecture's, not the data's, so this is the learned route the claim's closing sentence leaves open. It does not test the claim's derivation. The claim is unchanged.
