---
status: Proposed
promote_when: >-
  A Read NOTE, on this book or on another held source, that follows the
  proofs of the two order-theoretic facts the account uses: that left
  adjoints between preorders preserve joins (Prop. 1.111), and that out of
  a preorder with all joins a monotone map preserving joins is a left
  adjoint (Thm 1.115). A gap in either would refute the second half as
  stated. More worked examples of generative effects cannot settle it, and
  neither can an application of the definition to translation or reading,
  which would test a use of the account, not the account.
title: "An observation modelled as a monotone map between preorders can show of a joined system more than the join of its observations of the parts, and out of a preorder with all joins the observations that never do so are exactly the left adjoints"
version: 1
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
  Prop. 1.111 and Thm 1.115 give that left adjoints preserve joins and, from
  a source with all joins, only they do. The results are standard order
  theory, and [NOTE-601](../notes.d/NOTE-601.md) filed no THEORY because the record had no use for
  stating textbook theorems separately. It is filed Proposed because it
  rests on a skim.
---

<!-- inactive-ok-file: NOTE-601 — Skimmed; the reading this account rests on, which is why it is Proposed -->
<!-- inactive-ok-file: CLAIM-119 — Proposed; named for the vocabulary it uses, not leaned on -->

# THEORY-tmpyncg4: An observation modelled as a monotone map between preorders can show of a joined system more than the join of its observations of the parts, and out of a preorder with all joins the observations that never do so are exactly the left adjoints

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
all joins, a monotone map out of P preserves joins iff it is a left adjoint,
the right adjoint being given by a meet formula. So, out of a preorder with
all joins, the observations without generative effects are exactly the left
adjoints.

**Closure (§1.4.4).** For any adjunction g∘f is a closure operator, and every
closure operator arises from an adjunction with the inclusion of its fixed
points.

**What could have come out otherwise.** Join preservation could have been
weaker than having an adjoint. Out of a preorder with all joins it is not.

## What this does not say

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
- [THEORY-tmpf7k6q](THEORY-tmpf7k6q.md) is a research instance of the same theme: a composition-
  preserving map from syntax to semantics, which exists only once the
  semantics carries a backward channel.
