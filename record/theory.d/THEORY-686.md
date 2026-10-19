---
number: 686
status: Active
formerly:
- THEORY-tmpyncg4
title: "An observation modelled as a monotone map between preorders can show of a joined system more than the join of its observations of the parts, and out of a preorder with all joins the observations that preserve all joins, the empty join and infinite joins included, are exactly the left adjoints"
version: 2
history:
- version: 2
  date: '2026-10-19'
  note: >-
    Corrected, then promoted from Proposed to Active, at the owner's
    direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-686.yaml, batch 009, ADR-047).
    The title said the observations that never have a generative effect are
    exactly the left adjoints. Having no generative effect concerns binary
    joins only, and it is weaker than preserving all joins. The constant
    map to the top of {0 < 1} has no generative effect, but it is not a left
    adjoint, because it does not preserve the empty join. A map from
    ℕ ∪ {∞} to {0 < 1} can preserve binary joins and ⊥ and still fail at
    the join of ℕ. The title and the matching sentence under "Adjoints" now
    say "preserve all joins", and the counterexamples are added. The
    promote_when asked for a read proof of Prop. 1.111 and Thm 1.115. Under
    ADR-047 v2 (the owner's rule of 2026-10-19), a checked step-by-step
    re-derivation meets a request for a proof the record does not hold. The
    re-derivations are in the note of 2026-10-19 below. The promote_when is
    removed.
tags:
- mathematics
- compositionality
date: '2026-10-16'
source:
- LIT-803
summary: >-
  Fong & Spivak (2018), [LIT-803](../literature.d/LIT-803.md), Chapter 1, read closely in a Skimmed NOTE
  ([NOTE-601](../notes.d/NOTE-601.md)) whose other chapters were seen only at their openings. Def.
  1.93, after Adam, defines a generative effect as Φ(a) ∨ Φ(b) < Φ(a ∨ b).
  Prop. 1.111 and Thm 1.115 give that left adjoints preserve all joins and,
  from a source with all joins, only they do. The results are standard order
  theory, re-derived by the record because NOTE-601 is a skim. The absence
  of generative effects is weaker than preserving all joins, and does not
  characterise the left adjoints.
---

<!-- inactive-ok-file: NOTE-601 — Skimmed; the reading this account rests on, which is why it is Proposed -->
<!-- inactive-ok-file: CLAIM-119 — Proposed; named for the vocabulary it uses, not leaned on -->

# THEORY-686: An observation modelled as a monotone map between preorders can show of a joined system more than the join of its observations of the parts, and out of a preorder with all joins the observations that preserve all joins, the empty join and infinite joins included, are exactly the left adjoints

## Source

Fong & Spivak (2018; Cambridge University Press 2019), *Seven Sketches in
Compositionality*, [LIT-803](../literature.d/LIT-803.md), skimmed in [NOTE-601](../notes.d/NOTE-601.md). All of Chapter 1 and §3.4
were read closely, exercises read but not worked. Chapters 2 and 4–7 were
read only at their openings and summaries, and nothing here rests on them.

## What was actually shown

**Observation and generative effect (Def. 1.93, Ex. 1.94).** Following Elie
Adam's thesis, an observation of systems is a monotone map Φ : P → Q between
preorders. For any a, b with joins, Φ(a) ∨ Φ(b) ≤ Φ(a ∨ b). Φ has a
generative effect when the inequality is strict for some a, b: "we see
something when we observe the combined system that we could not expect by
merely combining our observations of the pieces".

**The worked example.** On the five partitions of {•, ◦, ∗}, ordered by
coarsening, let Φ ask "is • connected to ∗?". Φ is monotone. Joining two
partitions, in neither of which • and ∗ are connected, can connect them.

**Adjoints (Props 1.107, 1.111, Thm 1.115).** f ⊣ g iff p ≤ g(f(p)) and
f(g(q)) ≤ q. Left adjoints preserve joins and right adjoints meets. If P has
all joins, a monotone map out of P preserves all joins iff it is a left
adjoint, the right adjoint being given by a meet formula. So, out of a
preorder with all joins, the observations that preserve all joins are exactly
the left adjoints. An observation without generative effects preserves the
binary joins only, which is weaker (see "What this does not say").

**Closure (§1.4.4).** For any adjunction g∘f is a closure operator, and every
closure operator arises from an adjunction with the inclusion of its fixed
points.

**What could have come out otherwise.** Join preservation could have been
weaker than having an adjoint. Out of a preorder with all joins it is not.

## What this does not say

- **That an observation without generative effects is a left adjoint.**
  Having no generative effect means preserving binary joins. A left adjoint
  also preserves the empty join and infinite joins. On {0 < 1}, the constant
  map f ≡ 1 has no generative effect, since 1 ∨ 1 = 1, but f(⊥) = 1 ≠ ⊥, so
  it is not a left adjoint. From ℕ ∪ {∞} to {0 < 1}, the map sending each
  finite n to 0 and ∞ to 1 preserves binary joins and ⊥, but ⋁ℕ = ∞ goes to
  1 while ⋁f(n) = 0.

- **That the characterisation holds without all joins.** Thm 1.115 needs the
  source to have all joins. Without them a join-preserving map need not be a
  left adjoint.
- **That generative effects are a defect.** The definition marks where an
  observation of a composite cannot be computed from observations of the
  parts. Adam's interest, which the book follows, is in measuring them.
- **That translation or reading has generative effects.** [NOTE-601](../notes.d/NOTE-601.md) notes the
  definition makes the question precise; the book does not raise it, and no
  claim is made here.
- **That the book's later chapters support anything here.** Monoidal
  categories, resource theories, co-design and toposes were not read.
- **That the book connects this to formal concept analysis.** It does not.
  That the derivation operators of a formal context form an antitone Galois
  connection whose closed sets are the concepts is [NOTE-601](../notes.d/NOTE-601.md)'s link.

## Connections

- [CLAIM-119](../claims.d/CLAIM-119.md) holds that communicative categories form a concept lattice. The
  closure-operator construction of §1.4.4 is the order theory under formal
  concept analysis, by [NOTE-601](../notes.d/NOTE-601.md)'s link, and supports the claim's vocabulary,
  not its empirical content.
- [THEORY-519](THEORY-519.md) is a research instance of the same theme: a composition-
  preserving map from syntax to semantics, which exists only once the
  semantics carries a backward channel.

## Note of 2026-10-19: the three facts, re-derived

[NOTE-601](../notes.d/NOTE-601.md) is a skim, so the record re-derives what this account uses. This
meets the promotion condition under ADR-047 v2.

1. **Observations can only gain on joins.** Since a ≤ a ∨ b, Φ(a) ≤ Φ(a ∨ b),
   and likewise for b. So Φ(a ∨ b) is an upper bound of Φ(a) and Φ(b), and it
   lies above their join wherever that join exists.
2. **Left adjoints preserve all joins (Prop. 1.111).** Let f ⊣ g, so that
   f(p) ≤ q iff p ≤ g(q). For a family (a_i) with a join, f(⋁a_i) is an
   upper bound of the f(a_i), by monotonicity. If q is any upper bound of
   them, then each a_i ≤ g(q), so ⋁a_i ≤ g(q), and so f(⋁a_i) ≤ q. The
   empty family gives f(⊥) = ⊥.
3. **Out of a preorder with all joins, preserving all joins makes a left
   adjoint (Thm 1.115).** Put g(q) = ⋁{p : f(p) ≤ q}. Then
   f(g(q)) = ⋁{f(p) : f(p) ≤ q} ≤ q, using that f preserves this join, and
   p ≤ g(f(p)), because p is in the set for q = f(p). Those two
   inequalities are equivalent to f ⊣ g.
