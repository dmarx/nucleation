---
status: Read
paper: LIT-tmp6erox
title: 'The two dragons of cognition: recursive condensation for predictive processing'
version: 1
history:
- version: 1
  date: '2026-10-01'
  note: >-
    Read in full (Full text of the version of record, the publisher's
    open-access PDF from frontiersin.org (CC BY 4.0, 15 pp., with a text
    layer, extracted with PyMuPDF). I read the front matter (received 31 Dec
    2025, revised 20 Feb 2026, accepted 27 Feb 2026, published 23 Mar 2026;
    editor and two reviewers named), the abstract, and §§1–7 with every
    subsection: §1.1–1.5; §2, §2.1.1–2.1.3, §2.2; §3.1 (Theorem 1, Remark
    1), §3.1.1, §3.2.1–3.2.3 (Remark 2), §3.3, §3.3.1 (Table 1, Definition
    1), §3.3.2; §4.1.1–4.1.4, §4.2; §5.1 (Definition 2), §5.1.1–5.1.2,
    §5.2.1–5.2.3 (Theorem 2); §6.1 (Table 2), §6.2.1–6.2.3; §7. I also read
    the four figure captions, the data-availability, contributions, funding,
    conflict-of-interest and generative-AI statements, and the reference
    list (about 55 entries). Nothing was skipped. There is no supplementary
    material, despite the boilerplate data-availability line. The HTML
    landing page was checked for metadata only. No preprint under this title
    was found: an arXiv search of the author's papers turns up related
    preprints by Li (2024–2026) whose vocabulary this paper uses, but none
    with this title, so `published:` is the publisher's printed publication
    date. The page's `citation_online_date` (2026-02-27) is the acceptance
    date. No anthology entry exists for this DOI or title.). The first NOTE
    on this paper, which was seeded from its abstract alone.
date: '2026-10-01'
summary: >-
  A "Hypothesis and Theory" essay proposing that the neocortex is a
  "biological Savitch machine". Alternating expansion ("odd parity") and
  contraction ("even parity") phases manufacture the disjoint closed sets
  of Urysohn's Lemma, and storing ("memoizing") the condensed tokens
  converts exponential search into polynomial "navigation". Its one
  non-standard formal result, Theorem 2, R(N) ∝ b^{αN} (§5.2.2, p. 11), is
  stated without proof. There is no data, simulation or model. The two
  mathematical pillars are misdescribed: Savitch's theorem saves space at
  the cost of time and does not memoize, and Urysohn's Lemma gives a
  continuous separator, not a linear one, and is not an "if and only if".
---

# NOTE-tmp68638: The two dragons of cognition: recursive condensation for predictive processing

## Contribution

The paper is a single-author theoretical essay with no experiments, simulations or quantitative model. It proposes that the brain resolves two obstacles. The first is the "Time Dragon": exponential search over counterfactual futures. The second is the "Space Dragon": the curse of dimensionality. Both are resolved by one mechanism, "Recursive Condensation". The mechanism has three parts:

- An alternation between "odd-parity" metric expansion (search) and "even-parity" topological contraction (closure) produces disjoint closed representations. Urysohn's Lemma then guarantees that these can be separated.
- The three-stage cycle Search → Closure → Navigation, called the "Topological Trinity Transformation" (TTT), is identified with the constructive proof of Urysohn's Lemma (Table 1, Definition 1).
- Under "Memory-Amortized Inference" (MAI), storing the condensed tokens in cortical columns makes the cortex a "memoized Savitch machine", and linear cortical growth yields exponential "predictive reach" (Theorem 2).

The paper then maps the scheme onto the canonical microcircuit, PNG→assembly plasticity under STDP, the free-energy principle, and slow oscillations as "dark energy", and it closes with three predictions (§6.2).

## Key insight

The author's pivot is that separability is a topological condition (disjoint closed sets) rather than a volumetric one, so a system that actively collapses each concept's representation to a point-like "token" with a margin can classify by distance to prototypes regardless of ambient dimension (Remark 1, the "core-oriented" alternative to kernel inflation, p. 6). The rest of the paper leans on Savitch's theorem as a licence for trading time for space, and on the idea that a stored prior is "a fossilized Search path" (§4.2, p. 10).

## Assumptions

- Neocortical surface area "grows roughly linearly" across mammals while behavioural sophistication grows "superlinearly" (§1, p. 1, citing Buzsáki 2006). §2.2 (p. 5) cites the same source for the "exponential growth of the neocortex", and the paper never reconciles the two.
- Cortical columns share one canonical circuit (Mountcastle's principle), and each column can be treated as one discrete operator (§2.2, §4.1).
- Representations live in a normal topological space in which concepts can be made closed and disjoint (Theorem 1, §3.2.1).
- Free-energy minimisation is the dominant framework for cortical function and can be reinterpreted geometrically (§5).
- P ≠ NP (§2, §7). It is stated as consensus, and §7 then treats it as a constraint that AGI "must respect".
- The topological and complexity-theoretic constructions describe brain dynamics literally: "The brain does not merely satisfy the theorem; it executes the proof steps in time" (§3.2.2, p. 7).

## Key results

The paper has two formal statements and the rest is interpretation.

- **Theorem 1 (Urysohn Separability, p. 6).** For disjoint closed sets A, B in a normal space there is a continuous f whose decision boundary lies in X \ (A ∪ B). This is Urysohn's Lemma, cited, not proved. The paper infers from it that "a linear readout mechanism exists regardless of the ambient dimension D" (p. 6). That inference does not follow, since the lemma's f is continuous and in general nonlinear.
- **Remark 1 (p. 6).** Kernel methods versus "metric collapse". If each class is collapsed to a prototype C_A, C_B, the rule f(x) ≈ d(x,C_A)/(d(x,C_A)+d(x,C_B)) depends only on distance to prototypes. This is a nearest-centroid rule. Its success presupposes that the collapse has already been achieved correctly.
- **Remark 2 (p. 7).** The "Euler Thermostat", χ = β₀ − β₁ + …. Too many components (high β₀) is said to be overfitting, and too many loops (high β₁) "entanglement". This is asserted.
- **Definition 1, Table 1 (p. 8).** The "Urysohn-TTT isomorphism" pairs the proof's open-set, closure and interpolation steps with Search, Closure and Navigation. "Isomorphism" here is an analogy: no structure-preserving map is defined.
- **PLCA (§3.3.2, p. 8).** "A cognitive system minimizes the metabolic and temporal cost of frequent inference by maximizing the topological separability of its latent representations." It is stated as a principle.
- **Definition 2 (p. 10).** A system is "entangled" if an input x ∈ U_A ∩ U_B ≠ ∅, in which case "no continuous separating function f exists". As stated this contradicts Theorem 1: A and B can be disjoint closed sets, and so be Urysohn-separable, while their open neighbourhoods overlap.
- **§5.1.1 (p. 10).** "Minimizing Free Energy is the dynamical process of driving the system toward Urysohn Disjointness". §5 opens by calling this "mathematically equivalent to maximizing topological closure". No derivation is given.
- **Theorem 2 (Amortization Cost Theorem, p. 11).** "Under MAI, a linear increase in structural capacity (space N) yields an exponential increase in predictive reach. R(N) ∝ b^{αN}". R is "the maximum depth L traversable without divergence", b is the branching factor, and α is "the compression ratio of the column". No proof is given. As written it makes the *depth* exponential in N. The preceding cost comparison, search O(b^L) against structure O(N), would instead suggest depth linear in N, with the number of covered paths b^{αN}. The statement is unverified and ambiguous.
- **§5.2.3 (p. 11).** A covering-number gloss: adding columns refines an ε-net, whose size |N(ε)| scales exponentially in intrinsic dimension d. This is informal.
- **Predictions (§6.2, pp. 12–13).**
  1. Pyramidal–interneuron gamma (PING) cycles are the parity alternation, and gamma dysregulation in schizophrenia is "Topological Leakage".
  2. Sharp-wave ripples in slow-wave sleep perform "Global Closure". SWR deprivation, or disruption of SWR nesting within the Slow-4 (0.01–0.027 Hz) envelope, should "specifically impair transitive inference".
  3. In time-to-first-spike SNNs, learning in "topological traps" shows temporal compression of the spike train, and a "metric slingshot penalty" should "significantly reduce" time-to-solution.

  None is quantified and none is tested.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Savitch's theorem shows nondeterministic search, exponential in time, is "polynomially simulable in space", and the brain trades space for time by storing midpoints (abstract; §1.4, p. 3; §2.2 Clue 2, p. 4) | assertion (misstatement) | Savitch is cited. Savitch's construction recomputes midpoints rather than storing them, which is how it saves space, and its deterministic simulation still takes time 2^{O(s²)}. "Memoized Savitch" (§1.4) inverts the theorem's trade-off. |
| C2 | Distinct concepts can be separated by a continuous function "if and only if they are closed and disjoint sets" (§2.2 Clue 1, p. 4) | assertion (misstatement) | Urysohn 1925 is cited. The lemma gives sufficiency in normal spaces only. Sets that are not closed but have disjoint closures, such as (0,1) and (2,3) in ℝ, are also separable. |
| C3 | Because Urysohn's Lemma is dimension-agnostic, "a linear readout mechanism exists regardless of the ambient dimension D" (§3.1, p. 6) | informal argument (non sequitur) | Theorem 1 gives a continuous f, not a linear one. A linear rule follows only after collapse to prototypes (Remark 1), which assumes the separation problem has been solved. |
| C4 | The TTT (Search → Closure → Navigation) is "the dynamical execution of the constructive proof of Urysohn's Lemma" (§3.3.1, Table 1) | analogy | It is a table pairing proof steps with phases, with no formal map. |
| C5 | The brain "ensures" PLCA holds, and contribution 3 says "We prove" it (p. 3; §3.3.2, p. 8) | informal argument | No proof is given. |
| C6 | Minimising variational free energy is "mathematically equivalent" to maximising topological closure (§5 intro, §5.1.1, p. 10) | assertion | No derivation is given, and Definition 2, its key definition, contradicts Theorem 1. |
| C7 | Linear growth in columns gives exponential predictive reach, R(N) ∝ b^{αN} (Theorem 2, p. 11) | assertion | It is stated as a theorem with no proof, and its form is ambiguous (see Key results). The generative-AI statement (p. 13) says Gemini 3.1 "was used to assit the development of theoretical ideas (i.e., Theorems 1 and 2)". |
| C8 | Layer IV is the open set, L2/3 lateral inhibition the "Urysohn cut", and L5/6 the condensed token. Prediction error is "topological mismatch" (§4.1, Fig. 4) | assertion | It cites Bastos et al. 2012 and Keller & Mrsic-Flogel 2018 for the standard picture. The topological reading is the author's own. |
| C9 | PNGs are 1-cycles (β₁), columnar assemblies 0-cycles (β₀), and STDP collapses the one into the other (§4.2, p. 10) | assertion | It cites Izhikevich 2006 and Caporale & Dan 2008 for the phenomena, not for the homological reading. A temporally ordered firing pattern is not a homology class in any defined complex. |
| C10 | Brain "dark energy" (baseline metabolism) is the thermodynamic cost of maintaining the topological scaffold against the Second Law. Down-states are "Quotienting (Reset)" (§6.1, p. 12) | assertion | It cites Raichle 2001, Gong & Zuo 2025, Dang-Vu 2008 and Pang 2023 for the phenomena. No energy accounting is given. |
| C11 | Gamma PING is the parity clock, and schizophrenia is topological leakage (§6.2.1) | prediction, untested | Supporting citations are Traub 1997, Insel 2010, Fletcher & Frith 2009 and Sterzer 2018. No measure of "leakage" is defined. |
| C12 | SWR deprivation, or disrupted SWR/Slow-4 nesting, specifically impairs transitive inference (§6.2.2) | prediction, untested | Supporting citations are Buzsáki 2015, Staresina 2015 and Lecci 2017. The paper does not discuss existing SWR-disruption studies. |
| C13 | A "metric slingshot penalty" in surrogate-gradient SNNs "significantly reduces" time-to-solution in non-convex landscapes (§6.2.3) | prediction, untested | None is given. "GHL" (Fig. 1, §6.2.3) is never defined in the paper. |
| C14 | LLMs "are theoretically bounded", and a true AGI "must respect the fundamental constraint that P ≠ NP" (§7) | assertion | No argument is given beyond §2.1.3's characterisation of LLMs as "statistical oracles". |
| C15 | Urysohn-prepared supports give continual learning without catastrophic forgetting, and OOD detection as distance to closed support (§3.2.3, p. 7) | assertion | It cites two surveys (Wang et al. 2024; Yang et al. 2024). No method or experiment is given. |

## Method

There is no method in the empirical sense. The paper argues by analogy across three "clues" (Urysohn, Savitch, Mountcastle; Fig. 2, Table 2). It restates one classical theorem (Theorem 1), states one new "theorem" without proof (Theorem 2), and assigns topological readings to known neural phenomena. Figures 1–4 are conceptual illustrations, which the generative-AI statement says were generated with Gemini 3.1.

## Concepts

- **Time Dragon / Space Dragon.** These are combinatorial explosion of search, and either NPSPACE-vs-DSPACE or the curse of dimensionality. The usage is inconsistent across sections.
- **Recursive Condensation.** Repeated collapse of entangled manifolds into quotient spaces M₀ → M₁ → …, where each step is a column acting as a quotient map q: X → X/∼ (§4.1).
- **Parity Alternation Principle.** Alternation of odd parity (expansion, search, associated with β₁) and even parity (contraction, closure, associated with β₀). "Parity" names the homological degree only by association, and no parity operator is defined.
- **Topological Trinity Transformation (TTT).** Search → Closure → Navigation.
- **Metric Collapse.** diam(U) → 0, so U → {x*}, with a margin δ (§3.3).
- **Urysohn operator / Urysohn cut.** A column, or lateral inhibition, as the separation step.
- **Memory-Amortized Inference (MAI).** Storing condensed states to avoid recomputing search (§5.2.2, citing Gershman & Goodman 2014 for amortized inference).
- **Principle of Least Computational Action (PLCA).** §3.3.2.
- **Topological Entanglement.** Definition 2.
- **Euler Thermostat.** Remark 2.
- **Predictive Reach R(N).** Theorem 2.
- **Metric slingshot.** Gradient descent toward a goal in a warped metric (Fig. 1, §6.2.3).

## Connections

- **[THEORY-030](../theory.d/THEORY-030.md) (Landauer prices only logically irreversible steps).** This shares vocabulary, and the paper's thermodynamic language runs against it. The paper's metric collapse and quotient map is a many-to-one map, so [THEORY-030](../theory.d/THEORY-030.md)'s account would price it, at k ln 2 of exported entropy per bit of lost distinguishability. Holding the resulting structure would not be priced, yet §6.1 attributes baseline metabolic cost to "fighting the Second Law … to maintain this topological scaffold", and §5.1.2 calls the system a "Maxwell's Demon of geometry" that "dissipates metabolic heat … to actively reduce the topological entropy". No dynamics or accounting is supplied, so the paper does not bear on [THEORY-030](../theory.d/THEORY-030.md)'s promote_when. That condition asks for a derivation for stated dynamics, and the paper offers none.
- **[THEORY-026](../theory.d/THEORY-026.md) (only nonpredictive memory is wasteful, absent feedback).** This also shares vocabulary only. The paper's "a Prior is simply a fossilized Search path" and its claim that structure converts "the high cost of active search into the zero-cost inertia of structure" (§5.1.2) gesture at the same territory, the energetics of predictive memory. However, the paper has no driven system, no information measure and no feedback distinction. It does not bear on [THEORY-026](../theory.d/THEORY-026.md)'s promote_when.
- **[THEORY-035](../theory.d/THEORY-035.md) (Rejected: SGD compression explains generalisation).** The paper's slogan "not compression for bandwidth's sake but condensation for separability's sake" (§6.1) is a cousin of the rejected account: a representation is said to generalise because it collapses. It is offered with even less support, no measurement of any kind. The paper does not engage the information-plane literature, and it does not bear on that theory's reinstatement conditions.
- **[THEORY-008](../theory.d/THEORY-008.md) (what a regularized linear readout can decode is fixed by the normalized kernel).** This is vocabulary only. The paper's "linear readout" claims (§3.1, §3.3) rest on Urysohn's continuous separator, not on any readout analysis. [THEORY-008](../theory.d/THEORY-008.md) is the record's precise version of what a linear readout can and cannot extract.
- **[NOTE-169](NOTE-169.md) / [LIT-135](../literature.d/LIT-135.md) (Seth, conscious AI and biological naturalism).** Both engage predictive processing and the free-energy principle and link FEP to metabolism. Seth (per [NOTE-169](NOTE-169.md)) takes the FEP at a favourable reading, through the Jarzynski equality and Landauer. Li reinterprets FEP topologically instead. The two share vocabulary and do not engage each other.
- **[NOTE-311](NOTE-311.md) / [LIT-358](../literature.d/LIT-358.md) (Stone 1937, Boolean rings and general topology).** This is the record's one close reading in point-set topology near Urysohn's work. It bears on nothing here except as a reminder that separation axioms (normality) are hypotheses, which C2 elides.
- **No other connections.** No other record entry treats complexity-theoretic accounts of cognition, cortical columns or Savitch's theorem. Li's related preprints visible on arXiv are not in the record, and their arXiv titles share this paper's vocabulary: "Memory-Amortized Inference: A Topological Unification of Search, Closure, and Structure", "The Homological Brain: Parity Principle and Amortized Inference", "The Urysohn Machine", "The Metric Slingshot". This paper cites none of them. They were not read.

## Bearing on the record

The paper is filed for its subject: a strong computational-neuroscience claim that leans on mathematics. Its value to the record is mainly as a worked example of a recurring failure, a theorem's name used as a licence for a claim the theorem does not make, here in both Savitch's and Urysohn's cases. Nothing in it bears on any THEORY's promote_when.

**For ML practice (the Anthology of the SOTA) it carries nothing.** Its ML-flavoured claims are asserted with survey citations and no method or experiment: continual learning without forgetting, OOD detection by distance to closed support, "gate-then-refine" compute scaling, a slingshot penalty for SNNs, and LLMs being "theoretically bounded". The prototype or centroid rule in Remark 1 is an old technique, and nothing here adds evidence for it.

## Limitations

- **Savitch is misread.** The theorem simulates NSPACE(s) in DSPACE(s²) by recursive midpoint search that *recomputes* reachability rather than storing it. That is why the space is small. The deterministic simulation takes 2^{O(s²)} time. The theorem does not convert exponential time into polynomial anything, and memoizing all midpoint results would forfeit the space bound. The paper half-acknowledges the recompute/recall distinction ("provided it can recompute (or recall)", p. 3) but builds MAI on the "recall" reading.
- **Urysohn is overstated.** The "if and only if" (C2) is false. Continuity is not linearity (C3). The existence of a separating function in a metric space is trivial anyway: d(x,A)/(d(x,A)+d(x,B)) separates any two disjoint closed sets. It says nothing about sample complexity, which is what the curse of dimensionality concerns.
- **The paper contradicts itself.**
  - Definition 2 contradicts Theorem 1 (see Key results).
  - "Space Dragon" has three meanings (see corrections).
  - Cortical growth is called both "roughly linear" (p. 1) and "exponential" (p. 5), citing the same book.
- **The headline outruns the body.** The abstract says "we demonstrate", contribution 3 says "We prove", and §6 says it "moves beyond metaphor" with "falsifiable predictions". The body offers a restated classical lemma, an unproved scaling claim and untested qualitative predictions.
- **Generative-AI involvement in the formal content.** The paper says Gemini 3.1 was used to develop Theorems 1 and 2 and to generate Figures 1–4, and ChatGPT 5.4 to polish §§1 and 6 (pp. 13–14).
- **Undefined and uncited material.** "GHL" is never defined. The framework terms (MAI, parity alternation, TTT, metric slingshot) come from the author's preprints, which are not cited, so the paper is not self-contained.
- **Possible reviewer overlap (noted, not judged).** Gong & Zuo (2025), cited for "dark energy" and SSOs (§6.1, Table 2), is co-authored by one of the two named reviewers (Xi-Nian Zuo).
- **Untested.** No neural, behavioural or simulated data appear anywhere.

## Open questions

- Is there a statement of Theorem 2 that is both precise and true? What are N, R, b and α as measurable quantities, and is reach meant to be depth or the number of paths?
- Can any of the §6.2 predictions be made discriminating? That would mean a quantity predicted by the TTT that differs from what standard predictive-coding or replay accounts predict, for example for SWR disruption and transitive inference.
- Does the author's unread preprint series supply the missing proofs or a model (notably "Memory-Amortized Inference: A Topological Unification of Search, Closure, and Structure" and "The Homological Brain")? That would decide whether this paper is a summary of worked-out results or the whole of the case.

## Corrections to the seeded skim

- none (there was no seed or dossier)
- The publisher abstract says that nondeterministic problems are "exponential in time … but polynomially simulable in space (the 'Space Dragon'), as formalized by Savitch's theorem". In the body (§2, p. 3) the Space Dragon is first the NPSPACE-vs-DSPACE question, "already slain in 1970". Elsewhere (§1.1, p. 2; §3.1, p. 5) it is the curse of dimensionality. These three uses are incompatible, and the abstract's "exponential search in time becomes polynomial reuse in space" is not what Savitch's theorem says (see Limitations).
- The abstract says "we demonstrate that separability is a property of connectivity, not volume". The body offers no demonstration beyond restating Urysohn's Lemma (Theorem 1, p. 6) and a heuristic remark (Remark 1).
- Contribution 3 says "We prove that this sequence satisfies the Principle of Least Computational Action" (p. 3). No proof appears. PLCA is stated as a principle (§3.3.2, p. 8) and argued informally.
- Contribution 5 says "we derive a scaling law". Theorem 2 is stated with no derivation (p. 11), and §5.2.3 calls it "the rigorous justification".
