---
status: Skimmed
paper: LIT-tmp6x1cq
title: 'Geiger and others 2025 — Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2301.04709 (HTTP 200, 1.2 MB PDF; arXiv
    v4 of 8 May 2025, the JMLR 26 (2025) 1-63 version, CC-BY 4.0), fetched
    2026-11-19. Kind of copy (step 5): arXiv preprint, the authors' own
    upload of the published JMLR article (licence CC-BY 4.0 stated on p. 1).
    No obstacle. Text extracted with pdftotext -layout to dl/text.txt. Read:
    abstract; §1 Introduction; §2.3 opening (Definition 25, exact
    transformation; Remarks 26-27); §2.3.2 (Definition 31 alignment, Remark
    32, Definition 33 constructive abstraction, Remarks 34-35); §2.3.3
    opening (marginalization, variable merge, value merge); §2.4 (Definition
    41 approximate transformation, Example 5); §2.5 in full (Definitions
    44-46 interchange interventions, recursive and distributed; Remark 47
    constructing alignments; Definition 48 interchange intervention
    accuracy); §2.6 (hierarchical-equality example, handcrafted and trained
    networks); §3.1 (modular features, polysemanticity, linear
    representation hypothesis); §3.2 (graded faithfulness); §4 Conclusion.
    Skipped: §2.1-2.2 (causal models, intervention algebras, Theorems 20-21)
    beyond the notation table; §2.3.1 (bijective translation, Theorem 30);
    §2.7 (cycles, infinite variables); §3.3-3.8 (the survey of methods:
    LIME, integrated gradients, mediation, path patching, ablation,
    scrubbing, SAEs, DAS, steering).
date: '2026-11-19'
---
<!-- inactive-ok-file: CASE-tmpsjjgx CLAIM-tmpj540o — Proposed; cited in this filing of 2026-11-19 -->

# NOTE-tmp1nqoj: Geiger and others 2025 — Causal Abstraction: A Theoretical Foundation for Mechanistic Interpretability

## Contribution

Geiger, Ibeling, Zur, Chaudhary, Chauhan, Huang, Arora, Wu, Goodman, Potts and Icard (arXiv 2301.04709, v4 2025; JMLR 26, 2025) set out causal abstraction as the criterion for when a transparent high-level algorithm faithfully describes a network's low-level mechanisms. A high-level model is an exact transformation of a low-level one when translating low-level solutions under an intervention gives the high-level solutions under the corresponding intervention. Constructive abstraction is the case where the translation comes from an alignment: a partition of low-level variables into cells, one per high-level variable plus a forgotten cell, with maps from cell values to high-level values. They generalize interventions to "interventionals" (functionals from old to new mechanisms), so that distributed features such as rotated subspaces can be targeted. They define graded faithfulness as approximate transformation, and recast a wide range of interpretability methods (patching, mediation, ablation, causal scrubbing, SAEs, DAS, steering) in these terms. Skimmed: definitions and the worked example, not the survey of methods.

## Key results

- **Exact transformation** (Definition 25, p. 13): M∗ is an exact transformation of M when "the interventional ω(I) on M∗ results in the same total settings of V∗ as the result of first determining a setting of V from I and then applying the translation τ", i.e. τ(Solve(M_I)) = Solve(M∗_ω(I)) (Eq. 3).
- **Alignment** (Definition 31, p. 16): a partition Π of the low-level variables into "non-overlapping, non-empty cells ΠXH ⊆ VL for each XH ∈ VH , in addition to a (possibly empty) cell Π⊥", with "a partial surjective map πXH : ValΠXH → ValXH" for each cell.
- **Constructive abstraction** (Definition 33, p. 17): "H is a constructive abstraction of L under an alignment ⟨Π, π⟩ iff H is an exact transformation of L under (τ π , ω π )." It decomposes into marginalization, variable merge and value merge (§2.3.3).
- **Interchange intervention** (Definition 44, p. 21): the model "is provided a ‘base’ input and an intervention is performed that fixes some variables to be the values they would have if different ‘source’ inputs were provided."
- **Distributed interchange intervention** (Definition 46, pp. 21–22): apply a bijective translation, perform the interchange in the new variables, and translate back. This is how rotated subspaces (DAS) are targeted.
- **Alignment only on realized values** (Remark 47, p. 22): "we are only able to interpret low-level interchange interventions as high-level interchange interventions"; and the construction "is not well defined because two different inputs can produce the same zL while producing different" high-level values, in which case "the causal abstraction relationship simply wouldn’t hold for the alignment."
- **Interchange intervention accuracy** (Definition 48, p. 23): "simply the proportion of interchange interventions where the low-level and high-level causal models have the same input–output behavior". It is a special case of approximate transformation.
- **Worked example** (§2.6, pp. 23–27): a tree algorithm for hierarchical equality abstracts a handcrafted network exactly. For a trained network, "Looking at the network weights provides no insight into whether or not it implements the algorithm H", and a learned rotation (DAS) is needed (p. 27).
- **Modular features** (§3.1, p. 30): "We propose to define modular features as any set of variables that form an intervention algebra accessed by a bijective translation."

## Assumptions

- Deterministic causal models with input variables. Acyclic models are used for interchange interventions; cycles are treated separately in §2.7, not read.
- An alignment's high-level values are assigned by stipulation from the inputs that realize them (Remark 47), so the test covers only interventions to realized values.
- Graded faithfulness needs three choices: a similarity, a distribution over interventions and a statistic (Definition 41). The paper leaves these to the use case.

## Concepts

- **Exact transformation, constructive abstraction, approximate transformation.**
- **Alignment** ⟨Π, π⟩: a partition of low-level variables plus value maps, i.e. a quotient of the variables and their values.
- **Interventional**: a map from old mechanisms to new ones, generalizing hard and soft interventions.
- **Intervention algebra**: a class of interventionals with commutativity and left-annihilativity, which "can essentially be treated as hard interventions" in translated variables (§1).
- **Interchange intervention (single, recursive, distributed); interchange intervention accuracy (IIA).**

## Bearing on the record

- **[QUESTION-tmpcb0bf](../questions.d/QUESTION-tmpcb0bf.md)** — supports its interventional arm by giving its criterion precisely. A defect or wall would be a computational feature if a high-level model with a wall variable abstracts the network under an alignment, tested by interchange interventions (Definition 44) or distributed ones (Definition 46) and scored by IIA (Definition 48). Remark 47 limits what can be tested: only interventions to values the network realizes on some input. A12's test, moving a domain wall while approximately preserving the surrounding ordered configurations (as quoted in [QUESTION-tmpcb0bf](../questions.d/QUESTION-tmpcb0bf.md)), would have to be phrased as an interchange from a source input that places the wall elsewhere. The paper adds no control for frozen random networks, which [THEORY-1002](../theory.d/THEORY-1002.md) requires. Its own trained example rests on DAS, whose accuracy [THEORY-1002](../theory.d/THEORY-1002.md) shows can be above chance in wide random networks.
- **[QUESTION-tmpex36a](../questions.d/QUESTION-tmpex36a.md)** — leaves open, with one point of contact (the reader's observation, not the paper's). An alignment is itself a quotient: a partition of units with value maps (Definition 31), decomposed into variable merge and value merge. A fibration base merges units whose activities are equal for every input. That is a variable merge with an identity value map, and the base's forward computation is exact, as Velarde and colleagues prove ([LIT-tmpzusyw](../literature.d/LIT-tmpzusyw.md)). Neither paper connects the two. The worked example's task, hierarchical equality, is a relational-rule task of the kind the question names.
- **[TERM-062](../terms.d/TERM-062.md)** — contrast only. Causal abstraction is interventional; [TERM-062](../terms.d/TERM-062.md)'s causal states are predictive.
- **[CLAIM-tmpj540o](../claims.d/CLAIM-tmpj540o.md), [THEORY-1065](../theory.d/THEORY-1065.md), [THEORY-1059](../theory.d/THEORY-1059.md), [CASE-tmpsjjgx](../cases.d/CASE-tmpsjjgx.md)** — no direct bearing.

## Limitations

- Skimmed. The intervention-algebra theorems (§2.2), bijective translation (§2.3.1) and the method survey (§3.3–3.8) were not read, so no verdict is given on the paper's unification claims.
- The framework says when an abstraction holds. It does not say how to find an alignment, and in practice it relies on search methods such as DAS, whose false positives on random networks the record holds ([THEORY-1002](../theory.d/THEORY-1002.md)).
- Faithfulness is graded by choices of similarity, distribution and statistic that the paper does not fix.
