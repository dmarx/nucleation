---
status: Read
paper: 'LIT-tmp5jynk'
title: 'Coecke, Fritz and Spekkens — A mathematical theory of resources'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Read on 2026-11-05 from arXiv v3 (2014-11-28),
    https://arxiv.org/pdf/1409.5531, 32 pp., extracted with pdftotext
    -layout; the Information and Computation version was not consulted.
    Read closely: §1 Introduction; §2 (Definition 2.1, Examples 2.4–2.6);
    §§3.1–3.2 (partitioned process theories, Theorem 3.4); the opening of
    §3.3 with Lemma 3.11 and Theorem 3.12; §3.4 (universally-combinable
    processes, Definition 3.20); §4 (Definition 4.1, Theorem 4.2, Examples
    4.3–4.4, the phenomenology of §4.2, Theorem 4.13, Proposition 4.14);
    §5 (monotones, rates, Theorem 5.6); §6 Closing. Skimmed: Examples
    3.13–3.18 (communication, entanglement, asymmetry, nonuniformity,
    athermality) and Appendix A (the proof of Theorem 3.12). Quotes checked
    by string match against the extracted text. Section numbers are the
    paper's.
date: '2026-11-05'
summary: >-
  A resource theory is a symmetric monoidal category of resources and of
  the transformations that cost nothing. Such theories are generated from a
  process theory partitioned into free and costly processes, as theories of
  states and of processes. Forgetting which free transformation does a
  conversion leaves a preordered commutative monoid, which carries
  catalysis, monotones and conversion rates; its combination law can be
  sum or supremum over the same kind of order. Costs on transformations are
  left as the open problem.
---
<!-- inactive-ok-file: THEORY-tmpir3m0 TERM-tmp26wo4 CLAIM-tmpbi4ca CLAIM-tmpuk8gq NOTE-601 — Proposed, Skimmed or new; cited from the reading of Coecke, Fritz & Spekkens (2016) as open -->

# NOTE-tmpkmvs1: Coecke, Fritz and Spekkens — A mathematical theory of resources

## Contribution

One abstract definition covering chemistry, randomness, Shannon channels,
entanglement, asymmetry, nonuniformity, athermality and
compass-and-straightedge constructions: "We propose that a resource theory
be associated with a symmetric monoidal category wherein the objects are
resources and the morphisms are transformations of the resources" (§1).
Constructions that generate such theories from a free/costly partition of
processes, a "partial decategorification" to a preordered commutative
monoid, and the first general results on catalysis, monotones and rates.

## Key insight

The questions usually asked of a resource theory, what can be converted
into what, need only the order: "The requisite mathematical formalism turns
out to be that of a commutative (equivalently, Abelian or symmetric)
preordered monoid" (§1). How resources combine is a separate choice: "We
here emphasize that the monoid structure of a resource theory can vary
independently of the preorder structure" (§1).

## Assumptions

- **Strict** symmetric monoidal categories (Remark 2.3, by Mac Lane's
  strictification).
- **Free processes** form a sub-SMC containing every object, closed under ∘
  and ⊗, with identities and symmetries (Def. 3.3).
- **Free means free.** Morphisms are transformations that cost nothing;
  there is no grading of morphisms by an amount spent. In the convertibility
  layer which free operation achieves a conversion is "of secondary
  interest" (§4).
- **Static.** The free set does not change with time or with what has been
  spent; no rates or dynamics.

## Key results

- **Definition 2.1.** Morphisms in D(A, B) "represent transformations of
  resource A into resource B that can be implemented without any cost".
  Free resources are the objects A with D(I, A) non-empty (Def. 2.2).
- **Theories of states and processes** (§3). From a partitioned process
  theory (C, C_free): a theory of states (Theorem 3.4), of
  parallel-combinable processes (Theorem 3.12, via 1-combs), and of
  universally-combinable ones (Definition 3.20, via n-combs). The second is
  motivated by its limit: "there is no way to try and produce g by
  consuming f1 and f2 sequentially" (§3.4).
- **Decategorification** (Theorem 4.2, §4.1). Keeping only existence of a
  conversion gives (R, +, ≽, 0); equivalently "a theory of resource
  convertibility is a symmetric monoidal category enriched over the poset
  of truth values {0, 1}."
- **Sum against supremum** (Examples 4.3–4.4). Combination "in the theory of
  food it is given by component-wise addition of natural numbers; in the
  theory of proficiency, it is given by the order-theoretic supremum", and
  "the tensor of two proficiency levels is the maximum of the two."
- **Catalysis** (Theorem 4.13). "If R is non-interacting and quantity-like,
  then R is catalysis-free."
- **Monotones** (§5). "For any R there exists a complete family of
  monotones" (Proposition 5.2); "The preorder structure of a resource
  theory is more fundamental" than any single monotone (§1). Extensive
  monotones bound conversion rates (Theorem 5.6).
- **Open** (§6). "A major problem that we have not yet touched upon is
  epsilonification"; the proposed route is "replacing the preorder by a
  cost function".

## Concepts

- **Resource theory**: an SMC (D, ∘, ⊗, I) read as resources and free
  transformations (Def. 2.1).
- **Partitioned process theory** (C, C_free) (Def. 3.3).
- **Theory of resource convertibility**: a preordered commutative monoid
  (R, +, ≽, 0), with a ≽ b and c ≽ d implying a + c ≽ b + d (Def. 4.1).
- **Catalyst** c for a, b: a ⋡ b but a + c ≽ b + c (Def. 4.8).
- **Non-interacting** (a Riesz decomposition property, Def. 4.11),
  **quantity-like** (Def. 4.12), **quality-like** a + a ≃ a (Def. 4.16).
- **Monotone** (Def. 5.1), additive and supremal monotones (Def. 5.3);
  **conversion rate** R(a → b) (Def. 5.5).

## Connections

Generalizes the resource theories of quantum information (entanglement,
asymmetry, athermality) treated as examples in §3. Fritz's later work and
Seven Sketches chapter 2 ([LIT-803](../literature.d/LIT-803.md), which cites it as [CFS16]) teach the
convertibility layer as symmetric monoidal preorders. Marsden & Zwart
([LIT-tmpeei4c](../literature.d/LIT-tmpeei4c.md)) take up its §6 open problem by enriching in a quantale, and
criticize its quantitative elements as "ad-hoc".

## Bearing on the record

- **A's characterization** (Response 3, §2). A: "In the mathematics of
  resource theories, one studies which states or processes can be
  converted into which others, with particular attention to how resources
  behave under composition. A foundational reference is Coecke, Fritz, and
  Spekkens". Right: the paper is foundational for the categorical account
  and treats convertibility of states and of processes under sequential and
  parallel composition. The sentence is A's own, not the paper's.
- **No cost on morphisms.** A goes on to give costed processes a
  composition law, (c_p, e_p) ⊙ (c_q, e_q) = (max(c_p, c_q), e_p + e_q),
  "Peak capacity composes using maximum. Expenditure composes using
  addition." That law is not in this paper. Here morphisms are free and
  carry no cost; the costly things are objects. Sum and maximum appear
  only as two combinations of resources in parallel (food and proficiency;
  additive and supremal monotones), not as compositions of the costs of
  successive steps. Costed composition comes from quantale enrichment:
  Lawvere's metric spaces ([LIT-tmpuqt9i](../literature.d/LIT-tmpuqt9i.md)) and Marsden & Zwart ([LIT-tmpeei4c](../literature.d/LIT-tmpeei4c.md)),
  which this paper only gestures at in §6.
- **What A leaves out.** For A's process layer the paper's most relevant
  distinction is between parallel-combinable and universally-combinable
  processes (§3.4): whether resource processes can be consumed only side by
  side or in any order. A's "running two processes simultaneously may
  require adding their peak demands" is a different matter, a shared
  capacity, which the paper does not treat. And the paper deliberately
  forgets which transformation achieves a conversion (Theorem 4.2), the
  information A's process layer says is essential.
- **[TERM-tmp26wo4](../terms.d/TERM-tmp26wo4.md)** (six resource types): qualifies. With no grading by
  amount spent, none of the six is a cost on transitions here; only a stock
  fits, as an object combined by ⊗. The quantity-like and quality-like
  split is the nearest analogue of the term's "not one budget": two
  combination laws over orders of the same kind behave differently
  (catalysis is possible only in the supremum theory). The reader's
  reading.
- **[CLAIM-tmpuk8gq](../claims.d/CLAIM-tmpuk8gq.md)** (a Pareto frontier of sufficient budgets): supports
  the lesson, by analogy. The paper's point that no single monotone captures
  a non-total preorder is the resource-side form of the claim's point that
  no weighted total describes the sufficient budgets.
- **[CLAIM-tmpbi4ca](../claims.d/CLAIM-tmpbi4ca.md)** (threshold as infimum over paths of the peak): the
  paper has no path costs; the threshold's structure is the enriched one
  ([LIT-tmpeei4c](../literature.d/LIT-tmpeei4c.md)).
- **[LIT-845](../literature.d/LIT-845.md), [LIT-846](../literature.d/LIT-846.md)** (the resource theory of contextuality; categories of
  empirical models): instances of this framework, with simulations as
  morphisms. **[LIT-803](../literature.d/LIT-803.md)** (Seven Sketches; [NOTE-601](NOTE-601.md) skimmed chapter 2 at its
  opening only): its chapter 2 is the textbook version of §4.
- Filed: [THEORY-tmpir3m0](../theory.d/THEORY-tmpir3m0.md). No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- **The authors'.** "Our first small results are nothing but the very
  beginnings of a detailed investigation" (§6); epsilonification and cost
  functions not handled; size issues with equivalence classes of combs set
  aside.
- **Proofs.** Lemmas 3.11 and 3.19 are informal sketches; the sequential
  composition of universally-combinable processes is omitted as tedious.
- **No quantitative cost on transformations**, no time, rate or dynamics, a
  fixed free set.
