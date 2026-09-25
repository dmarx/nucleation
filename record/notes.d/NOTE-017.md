---
number: 17
status: Skimmed
formerly:
- NOTE-tmphgp0u
paper: LIT-003
title: 'A structure theorem for generalized-noncontextual ontological models'
version: 1
date: '2026-09-25'
summary: >-
  In any diagram-preserving generalized-noncontextual ontological model of a tomographically local operational theory, the model must be an exact (non-overcomplete) frame representation of the associated GPT, so the number of ontic states equals the GPT dimension (for example exactly d² for a qudit).
---

<!-- inactive-ok-file: LIT-003 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-017: A structure theorem for generalized-noncontextual ontological models

## Contribution

The authors take a theory to be classically explainable when it admits a generalized-noncontextual ontological model. They extend ontological models and generalized noncontextuality from prepare-measure scenarios to arbitrary compositional scenarios, using process theories. Under reasonable assumptions such models have a rigid structure: a frame representation that is not overcomplete. It follows that the number of ontic states is bounded by the dimension of the associated generalized probabilistic theory, which helps prove noncontextuality no-go theorems and certify contextuality experimentally. They also prove that three notions of classical explainability coincide in compositional scenarios: a noncontextual model of the operational theory, a positive quasiprobability representation of its GPT, and an ontological model of its GPT.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Results listed as three items: (1) the triple equivalence of classicality notions, generalizing earlier prepare-measure results; (2) the structure theorem: diagram-preserving quasiprobabilistic models are exact frame representations; (3) ontic-state cardinality equals GPT dimension (§1.1).
- Categorical restatement: a GPT is a monoidal category and its representations are strong monoidal functors into subcategories of FVect_R; for tomographically local GPTs every such functor is naturally isomorphic to the standard one, so ontological models are essentially unique (§1, §4.6).
- The dimension bound gives new, simpler proofs that operational quantum theory has no generalized-noncontextual model (§1, §4.3).
- Tomographic locality is necessary: the real-amplitude qutrit stabilizer subtheory has a noncontextual model (Gross's Wigner function, 9^n ontic states) but violates the structure theorem (§5.2).
- Diagram preservation is defended as a natural generalization of standard assumptions such as the identity process being represented by the identity (§5.1).

## Open questions

- Strongest claim: uniqueness and rigidity of noncontextual models. A deeper read should scrutinize diagram preservation, the load-bearing assumption (§5.1, App. B), and the proof of Theorem 4.1 (App. B).
- It formalizes the classicality criterion items 14 and 17 appeal to. The §5.2 example ties back to item 14's odd-prime stabilizer/epistricted equivalence.
- ML link: none direct. The "positive quasiprobability representation" criterion is a nonnegativity-of-a-linear-representation condition, but any ML analogy is speculative.
