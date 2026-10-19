---
number: 171
status: Active
formerly:
- THEORY-tmpquo32
title: 'When the causal constraints on events depend on context, deterministic assignments that are causal in each context can fail to glue into one causal assignment, so causal structure is itself a source of contextuality'
version: 3
history:
- version: 2
  date: '2026-10-09'
  note: >-
    Abramsky, Barbosa and Searle 2024 (LIT-843) added as a source. Its
    Example 7.2 is a second, independent instance of deterministic data
    failing to glue because causal pasts are incomparable, and its Example
    7.3 adds a gluing that is not unique. The claim is unchanged.
- version: 3
  date: '2026-10-19'
  note: >-
    Promoted from Proposed to Active at the owner's direction, carrying out
    the promotion audit's decision (record/promotion-audit/decisions/THEORY-171.yaml,
    batch 008, ADR-047). The title is an existence statement, and one
    checked example settles it. LIT-808's Θ₃ was followed step by step in
    NOTE-612, and the decision re-derives it. Under ADR-047 v2, the owner's
    rule of 2026-10-19, a step-by-step re-derivation in the decision file
    meets a request for a proof the record lacks. The promote_when asked for
    more than the title claims: a refereed version or a checked proof of
    Theorem 2.34's characterisation. That condition moves, unchanged, to
    QUESTION-143. The summary now reports the iff as the source's
    unchecked theorem, not as part of the account, and the promote_when is
    removed. The title is unchanged.
tags:
- causality
- contextuality
- quantum-foundations
- mathematics
date: '2026-10-09'
source:
- LIT-808
- LIT-800
- LIT-843
summary: >-
  From Gogioso & Pinzani's trilogy: The Topology of Causality, [LIT-808](../literature.d/LIT-808.md),
  read in [NOTE-612](../notes.d/NOTE-612.md), with the definitions of The Combinatorics of
  Causality, [LIT-800](../literature.d/LIT-800.md) ([NOTE-635](../notes.d/NOTE-635.md)). Over a space of input histories
  with the lowerset topology, causal functions form a separated presheaf,
  and on the space Θ₃ it is not a sheaf: two causal assignments on disjoint
  opens give one event two outputs on their common extension. That example
  was checked here, and it settles the claim. The source's Theorem 2.34,
  that the presheaf is a sheaf exactly when no two contexts impose
  incompatible causal pasts on a common event, is reported as the source's.
  Its proof was not read, and it is QUESTION-143. It does not say any
  physical or quantum data display the effect.
supports:
- CLAIM-038
---

<!-- inactive-ok-file: LIT-813 — Superseded; the withdrawn predecessor, whose sheaf claim this account corrects -->

# THEORY-171: When the causal constraints on events depend on context, deterministic assignments that are causal in each context can fail to glue into one causal assignment, so causal structure is itself a source of contextuality

## Source

Gogioso and Pinzani, *The Topology of Causality* (2023), [LIT-808](../literature.d/LIT-808.md),
Section 2.3: Definition 2.22, Theorem 2.30, Definition 2.23, Proposition
2.33 and Theorem 2.34, with the worked example on the space Θ₃, as read in
[NOTE-612](../notes.d/NOTE-612.md). The spaces, tip events and tightness are those of
*The Combinatorics of Causality*, [LIT-800](../literature.d/LIT-800.md) (Definitions 3.13–3.16,
Proposition 3.32, Theorem 3.33), as read in [NOTE-635](../notes.d/NOTE-635.md).

## What was actually shown

In Abramsky and Brandenburger's framework ([LIT-016](../literature.d/LIT-016.md)), the deterministic
local assignments always form a sheaf. Contextuality comes only from
probabilistic (or possibilistic) data that admits no global section
([THEORY-012](THEORY-012.md)). Gogioso and Pinzani replace the no-signalling scenario with a
space of input histories Θ, which can encode definite, indefinite and
input-dependent causal order. They give Θ the lowerset topology. A causal
function on an open set λ assigns outputs to the tip events of λ's
histories. Theorem 2.30 shows these form a separated presheaf, in which a
compatible family glues iff its compatible join is causal.

The new phenomenon comes from non-tight spaces, where one event can be the
tip of two different histories under a common extension. The worked case
is Θ₃, the meet of the spaces of total(A, B) ∨ discrete(C) and
discrete(A) ∨ total(C, B). Event B has causal past {A, B} in one and
{B, C} in the other. Take λ = {A:a, B:b}↓ and λ′ = {B:b, C:c}↓. These are
disjoint opens, so any pair of sections is compatible. Put f(A:a, B:b)_B = 1
on λ and f′(B:b, C:c)_B = 0 on λ′. Each is causal in its context, but the
join gives B two different outputs on {A:a, B:b, C:c}, which Θ₃'s causal
functions forbid. So there is no gluing, and the presheaf is not a sheaf.
This example was followed step by step in the reading.

Theorem 2.34, which the record reports and has not checked ([QUESTION-143](../questions.d/QUESTION-143.md)),
generalises it. With at least two outputs per event, the
presheaf is a sheaf iff Θ has no solipsistic contextuality witness: two
tip-equivalent histories whose minimal common extensions are not all
histories (Proposition 2.33). Tight spaces are always sheaves. Every space
induced by a causal order is tight ([LIT-800](../literature.d/LIT-800.md), Proposition 3.32). The
effect therefore needs causal constraints that differ between contexts,
which no single order supplies. By Theorem 2.48, a witness yields a
deterministic empirical model on the fully solipsistic cover that extends
to no standard empirical model. The introduction states that 1767 of the
2644 causally complete spaces on 3 events with binary inputs have this
property. That figure was not checked.

What could have come out otherwise: the sheaf property could have survived
the passage from no-signalling to arbitrary causal spaces, as the authors'
withdrawn 2021 paper ([LIT-813](../literature.d/LIT-813.md)) asserted for definite orders. For
order-induced (tight) spaces it does survive, and for non-tight ones it
fails.

## What this does not say

- **Not that quantum or any physical data show it.** Every example is a
  combinatorial space and a deterministic assignment. No experiment, and
  no quantum process, is shown to produce a solipsistically contextual
  model. The examples in [LIT-788](../literature.d/LIT-788.md) are all on the standard cover, where
  a deterministic model always glues (Corollary 2.50).
- **Not that it is the same as Kochen–Specker contextuality or
  non-locality.** Those are failures of probabilistic data to come from a
  global distribution over a sheaf of deterministic sections. This is a
  failure of the deterministic sections themselves, one level down.
- **Not that it arises for a fixed causal order.** Order-induced spaces,
  definite or indefinite, are tight and give sheaves. The effect needs
  contexts with incompatible causal pasts for one event, as in meets of
  order-induced spaces with non-nested pasts ([LIT-800](../literature.d/LIT-800.md), Theorem 3.33).
- **Not that the general theorem is checked here.** The proof of
  Theorem 2.34 was not read, and the paper is an unrefereed preprint. The
  characterisation is [QUESTION-143](../questions.d/QUESTION-143.md).
- **Not a statement about language, meaning or translation.** The analogy
  to contexts of interpretation with incompatible dependency structure is
  the reader's to make and is not drawn by the paper.

## Note of 2026-10-19: the existence claim, re-derived

The promotion audit's batch 008 re-derived the Θ₃ example ([ADR-047](../decisions.d/ADR-047.md) v2).
Θ₃ is the meet of the spaces of total(A, B) ∨ discrete(C) and
discrete(A) ∨ total(C, B). So event B has causal past {A, B} in one and
{B, C} in the other. {B:b} alone is a history in neither, so
λ = {A:a, B:b}↓ and λ′ = {B:b, C:c}↓ share no history, and any two sections
on them are compatible. Set B's output to 1 on λ, where its past is
{A:a, B:b}, and to 0 on λ′, where its past is {B:b, C:c}. Each is causal on
its open. On the extension {A:a, B:b, C:c}, B is the tip of both
sub-histories, so a causal function there must give B both outputs. No
gluing exists, and the presheaf of causal functions is not a sheaf.
[LIT-843](../literature.d/LIT-843.md)'s Example 7.2 is an independent second instance of the same kind.
That is everything the title asserts. The characterisation, which says
exactly which spaces fail, is [QUESTION-143](../questions.d/QUESTION-143.md).
