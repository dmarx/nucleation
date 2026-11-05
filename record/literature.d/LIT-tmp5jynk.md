---
status: Active
status_note: >-
  read 2026-11-05 (NOTE-tmpkmvs1) from arXiv v3; worth reading as the
  foundational categorical account of resource theories: a resource theory
  is a symmetric monoidal category whose morphisms are the transformations
  that cost nothing, generated from a partition of processes into free and
  costly, and most questions asked of it depend only on its preordered
  commutative monoid of convertibility, whose combination law (sum, or
  supremum) can vary independently of the order. Its main limits:
  morphisms carry no cost, so there is no grading by amount spent; costs on
  conversions ("epsilonification") are named in §6 as the major open
  problem; static, with no time or rates; some proofs only sketched.
title: 'A mathematical theory of resources'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 from the owner's pasted synthesis on
    resource-bounded realizability (written by another assistant, A, in
    the same exchange as the emergency-readiness bibliography, pasted
    2026-11-04), whose Response 3 §2 calls it "A foundational reference",
    citing "Coecke, Fritz, and Spekkens, A mathematical theory of
    resources" to ScienceDirect. The attribution is correct. Citation
    checked against Crossref and the arXiv API, which agree: Bob Coecke,
    Tobias Fritz and Robert W. Spekkens, in that order, Information and
    Computation 250 (2016), 59–86, journal article, issue October 2016,
    doi:10.1016/j.ic.2016.02.008. arXiv:1409.5531 [quant-ph], v1 submitted
    2014-09-19, which is `published:`. Not held before. Copy: arXiv v3 of
    2014-11-28 (minor revisions, per the arXiv comment),
    https://arxiv.org/pdf/1409.5531, 32 pp., extracted with pdftotext
    -layout; the journal version was not consulted. Status set to Active.
tags:
- mathematics
- information-theory
date: '2026-11-05'
published: '2014-09-19'
arxiv: '1409.5531'
doi: '10.1016/j.ic.2016.02.008'
first_author: 'Coecke'
keywords:
- 'resource theory'
- 'symmetric monoidal category'
- 'partitioned process theory'
- 'free processes'
- 'preordered commutative monoid'
- 'resource convertibility'
- 'catalysis'
- 'monotones'
- 'conversion rates'
implementations: []
summary: >-
  Coecke, Fritz & Spekkens (2014; Information and Computation 2016). "We
  propose that a resource theory be associated with a symmetric monoidal
  category wherein the objects are resources and the morphisms are
  transformations of the resources", the morphisms being those that "can
  be implemented without any cost". Such theories arise from a process
  theory partitioned into free and costly processes, as theories of states,
  of parallel-combinable processes and of universally-combinable ones.
  Forgetting which free transformation achieves a conversion leaves a
  preordered commutative monoid, on which catalysis, quantity-like and
  quality-like theories, monotones and conversion rates are defined; sum
  and supremum appear as two combination laws over the same kind of order.
  Costs on conversions are left open.
---
<!-- inactive-ok-file: THEORY-tmpir3m0 — Proposed and new; cited from the reading of Coecke, Fritz & Spekkens (2016) as open -->

# LIT-tmp5jynk: A mathematical theory of resources

Coecke, B., Fritz, T. & Spekkens, R. W. (2016). A mathematical theory of resources. *Information and Computation* 250: 59–86. doi:10.1016/j.ic.2016.02.008. arXiv:1409.5531 (v1 2014).

## Key takeaways

*From the reading, NOTE-tmpkmvs1. Section numbers are arXiv v3's.*

- **The definition** (§1, Def. 2.1). A resource theory is a symmetric
  monoidal category: objects are resources, ∘ is sequential and ⊗ parallel
  composition, and a morphism is a transformation that "can be
  implemented without any cost". Costliness is binary: free or not.
- **Generated from free processes** (§3). A process theory with a sub-SMC
  of free processes yields resource theories of states, of
  parallel-combinable processes and of universally-combinable ones
  (Theorems 3.4, 3.12; Definition 3.20).
- **The order is what matters** (§4). Keeping only whether a conversion
  exists gives "a commutative (equivalently, Abelian or symmetric)
  preordered monoid", and "the monoid structure of a resource theory can
  vary independently of the preorder structure": in the theory of food
  combination is addition, in the theory of proficiency the supremum
  (Examples 4.3–4.4).
- **First results** (§§4–5). Non-interacting quantity-like theories are
  catalysis-free (Theorem 4.13); a complete family of monotones always
  exists (Proposition 5.2); extensive monotones bound conversion rates
  (Theorem 5.6).
- **Open** (§6): "A major problem that we have not yet touched upon is
  epsilonification", with the suggestion of "replacing the preorder by a
  cost function".

## Standing in the record

The pasted synthesis on resource-bounded realizability cites it as the
foundational reference for resource theories, which it is. It does not
contain what the synthesis builds on it: in this paper morphisms are free
and carry no cost, so the composition law A proposes for costed processes,
(max, +) on peak capacity and expenditure, is not here. Sum and maximum
appear in the paper as two ways of combining resources in parallel, not
as two ways of composing the costs of successive steps. Costed composition
is the quantale-enriched line of Lawvere (LIT-tmpuqt9i) and Marsden &
Zwart (LIT-tmpeei4c), which opens from this paper's §6. The record's
contextuality resource theory (LIT-845, LIT-846) is an instance of the
framework, and Seven Sketches chapter 2 (LIT-803) teaches its
convertibility layer. Filed from it: THEORY-tmpir3m0.
