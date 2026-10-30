---
number: 263
status: Proposed
formerly:
- CLAIM-tmp3uhl1
title: "Whether two trained networks compute the same way can be tested by quotienting the architecture's full symmetry group and measuring what remains: a barrier that survives alignment marks a different mechanism, connection after alignment means shared feature structure, and the test cannot run where features have no counterpart"
version: 3
history:
- version: 1
  date: '2026-10-13'
  note: >-
    Split from CLAIM-187 under ADR-040, at the owner's request ("move
    forward as recommended"). The assistant restated the protocol for
    trained networks, as measured in the record's mode-connectivity
    readings, without CLAIM-187's carry-over to communicative kinds.
    CLAIM-187 now rests on this claim.
- version: 2
  date: '2026-10-27'
  note: >-
    A dated note added: Zoom In's universality hypothesis, read on
    2026-10-26, is the hypothesis this claim's test would probe
    across models; Zoom In itself offers anecdote. The claim is
    unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    THEORY-111, THEORY-112 and THEORY-113 were narrowed to what their
    sources measured and promoted by the eleventh status review (ADR-057).
    Steps 1, 3 and 4 now say what those readings hold. Old step 1 quoted
    THEORY-112's former title, "without which a barrier remains"; old step
    3 read "Along a low-loss path every layer's features interpolate the
    endpoints'"; old step 4 began: Merging fails "where their features have no
    counterpart in the other model". The last
    bullet of "What it does not say" read "It rests on five Proposed
    readings"; it now rests on two, THEORY-115 and THEORY-116. The claim
    is unchanged.
role: thesis
warrant: interpretive
defeated_if: >-
  Pairs of trained networks that share a mechanism by an independent test
  (the same input attributes relied on, the same features up to
  alignment) found separated by a barrier that survives quotienting the
  full symmetry group; or pairs that do not share one found connected
  after alignment, with features that interpolate along the path.
tags:
- representation-learning
- loss-landscapes
date: '2026-10-13'
line:
- learned-structure
grounds:
- THEORY-111
- THEORY-112
- THEORY-113
- THEORY-115
- THEORY-116
summary: >-
  The general content of [CLAIM-187](CLAIM-187.md), filed alone in learned-structure under
  [ADR-040](../decisions.d/ADR-040.md): a measured protocol for asking whether two trained solutions
  are the same solution. Quotient the full symmetry group, including the
  orthogonal map on a transformer's residual stream ([THEORY-112](../theory.d/THEORY-112.md)). Read a
  barrier that survives as a difference of mechanism ([THEORY-116](../theory.d/THEORY-116.md)).
  Between linearly connected image classifiers, nearly every layer's
  features interpolate ([THEORY-111](../theory.d/THEORY-111.md)). The
  test cannot run where features have no counterpart ([THEORY-113](../theory.d/THEORY-113.md)) or the
  objectives share no structure ([THEORY-115](../theory.d/THEORY-115.md)). It is the first claim in
  the learned-structure line.
supports:
- CLAIM-187
complements:
- CLAIM-366
---
<!-- inactive-ok-file: THEORY-986 — Proposed; Zoom In's universality hypothesis, cited as what the test would probe -->
<!-- inactive-ok-file: THEORY-115 THEORY-116 THEORY-108 CLAIM-187 — Proposed; the readings the protocol is assembled from, a case for it, and the claim that carries it further, open -->

# CLAIM-263: Whether two trained networks compute the same way can be tested by quotienting the architecture's full symmetry group and measuring what remains: a barrier that survives alignment marks a different mechanism, connection after alignment means shared feature structure, and the test cannot run where features have no counterpart

## The claim

The record's mode-connectivity readings, taken together, give a protocol
for asking whether two independently trained networks have found the same
solution:

1. **Quotient the full group.** Once the architecture's symmetries are
   factored out, most of the linear barrier between independently trained
   solutions disappears. The group must be the full one: for transformers
   it includes an orthogonal map on the residual stream, since
   permutations alone leave a barrier ([THEORY-112](../theory.d/THEORY-112.md)).
2. **Read the residue.** A barrier that survives the removal of symmetries
   "marks a difference in the input attributes the two models rely on:
   they compute by different mechanisms" ([THEORY-116](../theory.d/THEORY-116.md)).
3. **Inside a basin, structure interpolates.** In the image classifiers
   measured, along a low-loss linear path nearly every layer's features
   were proportional to the interpolation of the endpoints'
   ([THEORY-111](../theory.d/THEORY-111.md)). So connection
   after alignment is sameness of feature structure, not only of loss.
4. **Know when the test cannot run.** Merging fails, Stoica et al. argue,
   where features have no counterpart in the other model ([THEORY-113](../theory.d/THEORY-113.md)), and connectivity
   holds only when the objectives share structure ([THEORY-115](../theory.d/THEORY-115.md)).

The protocol turns "do these two networks compute the same way?" into a
measurement: quotient, then look for a barrier. It also says what a failed
comparison means, which is that the test does not apply, not that the
answer is no.

## Where the record applies it

[CLAIM-187](CLAIM-187.md) carries the protocol to communicative realizations, where the
admissible group, the path and the measure would all have to be defined.
It rests on this claim for the protocol and keeps that carry-over, its
weak point, as its own. [THEORY-108](../theory.d/THEORY-108.md)'s phase III is a ready case for the
protocol inside this line: whether its poor connectivity survives
permutation alignment.

## What it does not say

- It does not say why training reaches connected solutions. That is the
  line's open question, and this claim is a way of testing for it.
- It does not say a symmetry group is always known. For an architecture
  it is derived; elsewhere it must be chosen.
- It rests on two Proposed readings, [THEORY-115](../theory.d/THEORY-115.md) and [THEORY-116](../theory.d/THEORY-116.md). Hence
  Proposed.

## Note of 2026-10-27: universality, the hypothesis its test would probe

Zoom In ([LIT-1543](../literature.d/LIT-1543.md), [NOTE-1182](../notes.d/NOTE-1182.md)), read on 2026-10-26 at the
owner's request, states universality: analogous features and circuits
form across networks trained on different data and with different
architectures ([THEORY-986](../theory.d/THEORY-986.md)). That is the hypothesis this claim's test
would probe across models, a barrier that survives alignment marking a
different mechanism and connection after alignment marking shared feature
structure. Zoom In names the test the hypothesis needs and offers
evidence it calls "anecdotal", from vision networks. The nearest
measurement the record holds is Towards Monosemanticity's agreement of
features across two seeds of one architecture ([NOTE-1191](../notes.d/NOTE-1191.md)), which
compares features by their activations, not by the quotient this claim
asks for. The claim is unchanged.

## Note of 2026-10-29: what holds it back

Step 2 is [THEORY-116](../theory.d/THEORY-116.md)'s stated direction, that a barrier surviving
alignment marks a different mechanism, which no held source tests on deep
networks trained on the same data: the evidence is co-occurrence in one
synthetic-cue protocol and a one-layer proof of the converse. Step 4's
"only when the objectives share structure" is [THEORY-115](../theory.d/THEORY-115.md)'s, whose breaking
cases plot raw loss that the endpoint's forgetting largely explains.
