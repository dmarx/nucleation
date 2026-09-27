---
status: Read
paper: LIT-tmporlvo
title: 'The Lattice Representation Hypothesis of Large Language Models'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (full text, arXiv v3 PDF (25 Jul 2026; ICLR 2026
    camera-ready), 16 pp.: §§1–4, the additional analysis, related work,
    conclusion, ethics and reproducibility statements, Appendices A (LLM
    use), B (proof of Theorem 1, Lemmas 1–3, Props 2–3, Cor 1, B.4), C
    (proof of Prop 1 with remarks), D (discussion, limitation, Figure 6) and
    the references. Figures 4 and 5b report their results only as bar
    charts, so their values are read off the plots, not stated in the text;
    I give no numbers for them. The released code was not inspected.). The
    first NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  Thresholding linear attribute directions (Fisher-LDA probes) gives a
  crisp object–attribute incidence, and the paper's Theorem 1 is the
  standard fact that any such incidence has a complete concept lattice.
  The geometric meet is half-space intersection; the join is defined as
  the set union of two cones and "approximated by the conic hull" of their
  directions, which as written is not a lattice join. On five WordNet
  domains with GPT-4o-annotated attributes, the probes recover the
  incidence at F1 69.7–83.2 on three 7–8B models, and profile-based
  subsumption reaches F1 57.1–77.1. No lattice law is ever tested.
---

<!-- inactive-ok-file: LIT-230 — Deferred: cited as context for the comparison with van Rijsbergen; the directive lapses when its status changes -->
<!-- inactive-ok-file: LIT-243 — Deferred: cited as context for the comparison with van Rijsbergen; the directive lapses when its status changes -->
<!-- inactive-ok-file: LIT-264 — Deferred: cited as context for the comparison with van Rijsbergen; the directive lapses when its status changes -->
# NOTE-tmphkmry: The Lattice Representation Hypothesis of Large Language Models

## Contribution

The paper names a "Lattice Representation Hypothesis" in four steps. First, it treats each binary attribute's linear direction (after Park, Choe & Veitch, [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md)) as a half-space with a threshold. Second, it reads the resulting object–attribute incidence as a formal context in the sense of formal concept analysis (FCA). Third, it defines a region algebra (meet, join) and a soft inclusion score on attribute-projection profiles. Fourth, it reports that on five WordNet-derived domains, Fisher-LDA probes on three 7–8B LLMs recover an LLM-annotated incidence and predict WordNet subsumption above mean-centroid and random baselines.

The formal results are standard: Theorem 1 is the basic theorem of FCA applied to a thresholded relation, and Proposition 1 is a translation. What is new is the framing and the evaluation protocol.

## Key insight

Once a probe with a threshold turns each object–attribute pair into yes or no, the geometry has finished its work. What follows is the ordinary Galois connection between objects and attributes, whose closed pairs always form a complete lattice. The paper says as much: "Once I_δ is fixed, the statement becomes a standard FCA result" (App. B, plan of proof). The lattice is therefore guaranteed by the construction and is not evidence about LLMs. The empirical question is only whether the thresholded probes agree with an external incidence and hierarchy.

## Assumptions

- **Linear Representation Hypothesis** for binary attributes, in Park et al.'s intervention form (Def. 2: moving along ℓ̄_m raises Pr(m = 1) and leaves causally separable attributes unchanged). It is assumed, not re-tested. The experiments do not use Def. 2 at all: directions come from Fisher LDA on labelled objects (Eq. 11), which is the measurement (probe) reading, not the intervention reading.
- **Thresholded incidence.** In the idealised case, m(g) = 1 ⇔ v_g·ℓ̄_m ≥ τ_m. In practice the soft incidence is P_α(m(g) = 1) = σ(α(v_g·ℓ̄_m − τ_m)) (Eq. 1), and the crisp relation is I_δ = {(g, m) : P_α ≥ δ} (Theorem 1).
- **Finite G, M** for Theorem 1. The lattice is over the sampled objects, not over R^d.
- **Canonical form.** There exists c with Dc = τ (Prop. 1). This holds for any τ if the k directions are linearly independent (k ≤ d; App. C Remark (i)). With 60–184 attributes per domain in hidden dimensions of several thousand, independence is plausible but not checked.
- **Concepts as origin-passing cones.** R(Y) = {v ∈ R^d : v·d_m ≥ 0 ∀ m ∈ Y} (Def. 6), after the canonical shift.
- **Evaluation data.** WordNet is_a hierarchies for five domains (Table 4: objects 7342 / 7704 / 2506 / 1009 / 2802; attributes 100 / 145 / 184 / 60 / 107; "#Hypernyms" 7473 / 8051 / 2628 / 1079 / 3003 for Animal / Plant / Food / Event / Cognition). The attribute schema and binary incidence come from GPT-4o (§4.1). Each object embedding is the mean over its synset lemmas of the last hidden state, averaged across token positions, of the lemma string alone, without context (Eq. 10). No train/test split is described, though §4.2 refers to "the training set (Section 4.1)".

## Key results

- **Theorem 1 (Existence of Lattice Geometry; restated as Theorem 2, App. B).** For finite G, M, embeddings v_g, directions ℓ̄_m, thresholds τ_m, α > 0 and δ ∈ (0, 1), the set F_δ of pairs (X, Y) with X = Y′, Y = X′ under I_δ is (i) closed under the Galois connection and (ii) a complete lattice under extent inclusion. The proof is Lemmas 1–3 (antitone Galois connection, closure operators, concepts are closed pairs), Prop. 2 (partial order), Prop. 3 (⋀(X_i, Y_i) = (∩X_i, (∩X_i)′), ⋁(X_i, Y_i) = ((∪X_i)″, ∩Y_i)) and Cor. 1. *Holds for:* any binary relation whatever; nothing geometric is used. B.4 says that raising δ removes incidences and "typically" coarsens the lattice.
- **Proposition 1 (Canonical representation).** If Dc = τ, then σ(α(v_g·d_i − τ_i)) = σ(α((v_g − c)·d_i)) for all g, i (Eq. 2). *Holds when:* τ ∈ range(D). c is unique up to ker(D) (App. C Remark (ii)).
- **Definition 7 (meet/join).** A ∧ B := R(Y_A ∪ Y_B). A ∨ B := R(Y_A) ∪ R(Y_B), "approximated by the conic hull spanned by the attribute directions of A and B". See the corrections: the join as written is not in the family, and the stated approximation is the dual of the meet.
- **Soft algebra (Eqs. 4–9).** The profile is π_C(m) = (1/n) Σ_i v_i·d_m, ℓ2-normalised over m. Inclusion is Incl(A ⊑ B) = Σ_m φ(π_B(m)) σ(π_A(m)) / Σ_m φ(π_B(m)), with φ = softplus. The meet profile is min{π_A, π_B} and the join profile is max{π_A, π_B}. Soft equality is the harmonic mean of the two inclusions. (Eq. 7 refers to "Eq. (2)" for inclusion; it means Eq. 5.)
- **Table 1 (formal-context recovery), macro precision/recall/F1 over attributes.**
  - Linear F1: LLaMA3.1-8B 82.5 / 82.4 / 80.1 / 71.5 / 75.0; Gemma-7B 83.2 / 83.2 / 80.0 / 71.4 / 75.4; Mistral-7B 81.8 / 81.7 / 78.2 / 69.7 / 74.1 (Animal / Plant / Food / Event / Cognition).
  - Mean F1 ranges 50.1–68.4, and Random F1 ranges 45.0–50.1.
- **Table 2 (subsumption from Eq. 5).**
  - Linear F1: LLaMA 77.1 / 70.4 / 75.4 / 68.3 / 69.6; Gemma 75.1 / 71.4 / 75.6 / 65.6 / 66.4; Mistral 72.1 / 57.1 / 62.0 / 61.8 / 61.1.
  - Mean beats Linear on Mistral WN-Plant (60.5 vs 57.1 F1).
  - The decision rule that turns a soft inclusion score into a predicted edge, and how negative pairs are sampled, are not stated (unverified).
- **Fig. 4 (concept algebra, MRR).** For each domain, 200 pairs sharing at least one descendant and one ancestor. The gold meet is the lowest shared descendant and the gold join the least common hypernym. Candidates are ranked by Eqs. 8–9. The operator beats Random and Mean everywhere, with smaller gains on Event and Cognition; values are shown only as bars on a 0–0.6 axis.
- **Table 3 (qualitative).** Top-10 join and meet terms for six sibling pairs (dog/wolf, cat/lion, sparrow/robin, horse/zebra, carrot/parsnip, eagle/falcon). The joins are sensible hypernyms (predator, canine, avian, equid, raptor). The "meets" are mostly A itself and A's hyponyms or near-siblings (for dog ∧ wolf: dog, hound, puppy, terrier, …; for horse ∧ zebra: horse, pony, stallion, …). They are not common subconcepts of both inputs, and to my knowledge these pairs have no shared WordNet descendant. So they fall outside the Fig. 4 sampling condition.
- **Fig. 5b (scaling).** LLaMA-3 3B / 8B / 70B. The gains are modest on physical domains and larger on Event and Cognition (graph only).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Thresholded linear attributes induce a complete concept lattice over the objects | proof (of a standard FCA theorem) | Thm 1, App. B. True of every binary relation, so it carries no information about LLMs |
| C2 | Thresholds can be absorbed into a global shift, giving origin-passing half-spaces | proof | Prop. 1, App. C; condition Dc = τ solvable (sufficient: independent directions, k ≤ d) |
| C3 | Concept meet is half-space intersection and join is the least subsuming region, approximated by a conic hull | assertion (definition) | Def. 7. The join as written (set union) is not a region, and the stated approximation (conic hull of directions) is dual to the meet (my check). Unused in experiments |
| C4 | The fuzzy min/max of profiles is a soft meet/join | assertion (definition) | Eq. 6. Under the paper's own Eq. 5, the min profile behaves as an upper bound of A, not a lower one (my simulation, see Limitations). Not tested by the symmetric Eqs. 8–9 |
| C5 | LLM embeddings support the half-space model (single direction plus threshold separates attributes) | experiment | Table 1, Fig. 3: Linear F1 69.7–83.2 vs Mean 50.1–68.4, Random 45.0–50.1; the "ground truth" is GPT-4o annotation |
| C6 | Subsumption can be predicted from projection profiles | experiment | Table 2: Linear F1 57.1–77.1; one cell loses to Mean; decision rule unstated |
| C7 | Meet and join operators recover gold lowest-shared-descendants and least-common-hypernyms better than baselines | experiment (graph only) | Fig. 4, 200 pairs per domain; no numbers in text |
| C8 | Join returns hypernyms and meet returns "refined category intersections" | qualitative illustration | Table 3; the meets listed are refinements of one input, not intersections |
| C9 | Larger models gain most on abstract domains | experiment (graph only) | Fig. 5b, LLaMA-3 3B–70B |
| C10 | "LLMs implicitly organize conceptual knowledge into a lattice geometry" and encode "the algebraic backbone of concept lattices" (§1, Conclusion) | assertion | Exceeds C5–C9. No lattice law, closure or recovered-lattice comparison is tested, and the lattice of C1 exists for any relation |
| C11 | The operators can serve as logic-guided regularisers and "logical steering" (meet = enforce both, join = abstraction, negation = crossing the hyperplane) | assertion | App. D; not run |

## Method

1. Build a formal context per WordNet domain. Objects are synsets under the domain root. GPT-4o proposes salient binary attributes and annotates each object with a binary attribute vector (few-shot).
2. Embed each object as the mean, over its lemma strings, of the token-averaged last hidden state (Eq. 10), on LLaMA3.1-8B, Gemma-7B and Mistral-7B, plus LLaMA-3 3B/8B/70B for scaling.
3. For each attribute, take the Fisher-LDA direction ℓ̄_m = (Σ₊ + Σ₋ + λI)⁻¹(µ₊ − µ₋), with Ledoit–Wolf shrinkage (Eq. 11), and the midpoint threshold between the mean projections of positive and negative objects (Eq. 12). Predict m̂(g) = 1[v_g·d_m ≥ τ_m] and score it against the annotations (Table 1).
4. Form concept profiles π_C (Eq. 4) and score subsumption by Eq. 5 against WordNet is_a (Table 2).
5. Form meet/join profiles by min/max (Eq. 6), rank candidate concepts by soft equality (Eqs. 8–9), and report the MRR of the gold meet/join (Fig. 4) plus top-10 lists (Table 3).

## Concepts

- **Formal context / formal concept** — (G, M, I) with I ⊆ G × M. A concept is (A, B) with A′ = B and B′ = A under the derivation maps of Def. 4, which the paper calls "the Galois connections".
- **Soft incidence** — P_α(m(g) = 1) = σ(α(v_g·ℓ̄_m − τ_m)). It is a per-pair Bernoulli marginal; no joint distribution over attributes is defined.
- **I_δ** — the crisp relation obtained by thresholding the soft incidence at confidence δ.
- **Canonical form** — the shift v ↦ v − c with Dc = τ, making every attribute boundary pass through the origin.
- **Concept region R(Y)** — the polyhedral convex cone ∩_{m∈Y} {v : v·d_m ≥ 0}.
- **Projection profile π_C** — the average projection of a concept's context embeddings on each attribute direction, ℓ2-normalised; called "a continuous analogue of an FCA intent" (p. 5).
- **Inclusion(A ⊑ B)** — the softplus(π_B)-weighted mean of σ(π_A). It is not reflexive: for normalised profiles |π| ≤ 1, so Incl(A ⊑ A) ≤ σ(1) ≈ 0.73 (my observation from Eq. 5).
- **Meet / join** — region intersection and region union (Def. 7). For profiles, min and max (Eq. 6).

## Connections

**Same construction as van Rijsbergen's ch. 2, with the incidence computed instead of given.** Van Rijsbergen ([LIT-262](../literature.d/LIT-262.md); [NOTE-239](NOTE-239.md), ch. 2) follows Hardegree (1982) and reads an inverted file as a Galois connection (tr, in) between documents and index terms. His artificial classes are the Galois-closed sets and his monothetic kinds are classes whose attributes determine them and are determined by them. That is exactly an FCA formal concept (extent, intent), and Xiong's F_δ is the set of monothetic kinds of the context (G, M, I_δ). The one difference is where the incidence comes from:

- In van Rijsbergen the incidence is a fact of indexing: the document carries the term.
- In Xiong it is (g, m) ∈ I_δ ⇔ v_g·ℓ̄_m ≥ τ_m + α⁻¹ logit δ, a thresholded linear functional on a learned embedding.

Once I_δ is fixed the two constructions coincide, and the paper concedes that the geometry plays no further role (App. B). The profile-and-softplus inclusion of Eq. 5 is a separate matter: it scores weighted agreement across many attributes rather than possession of all of them. That is closer to what classification theory calls polythetic classes than to monothetic kinds. Whether van Rijsbergen's ch. 2 draws the monothetic/polythetic contrast is not recorded in [NOTE-239](NOTE-239.md) (unverified).

**Two polarities of one inner product.** Van Rijsbergen's other lattice, the lattice of subspaces (ch. 2 p. 39; ch. 5), is also the closed-set lattice of a Galois connection, but of a different relation: orthogonality, v·w = 0. Its closed sets are subspaces and the join is the closed linear span. Xiong's region level (Def. 6) corresponds to the relation v·d ≥ 0, whose closed sets over all of R^d are closed convex cones (bipolar theorem), and whose join is the closed conic hull of the union of the regions. The paper does not frame it this way; this is my reading.

- The orthogonality relation is symmetric, so its Galois map V ↦ V⊥ is itself an orthocomplement, and the subspace lattice is orthomodular.
- The half-space relation's Galois map is the dual cone C ↦ C*, an order-reversing involution that is not a complement: C ∩ C* ≠ {0} in general, and the positive orthant is self-dual.
- Composing with negation gives the polar C° = −C*. On closed convex cones this is an orthocomplementation (C ∩ C° = {0}; C + C° = R^d by Moreau's decomposition).
- The lattice of cones is not orthomodular. For a = cone{(1,1)} ≤ b = the first quadrant in R^2, b ∧ a° = {0}, so a ∨ (b ∧ a°) = a ≠ b (my check).

**Distributivity.** The paper never mentions distributivity, complements or Boolean structure; a text search finds none. My checks, not the paper's:

- (i) *The FCA lattice of Theorem 1 need not be distributive, even in canonical form with independent directions.* Take R^3, objects v_g = e_1, e_2, e_3, directions d_m = e_1, e_2, e_3 and thresholds 0.5. Then I_δ is the diagonal. The concept lattice is M₃ (bottom, three atoms ({g_i}, {m_i}), top), and a ∧ (b ∨ c) = a ≠ ⊥ = (a ∧ b) ∨ (a ∧ c). This is the same failure van Rijsbergen exhibits for monothetic kinds (humans, lizards, birds; p. 38).
- (ii) *The region lattice {R(Y)} with the correct closure join is Boolean, hence distributive, when the directions are linearly independent.* With independent directions any sign pattern of v·d_m is attainable, so R(Y) ⊆ {v·d_m ≥ 0} iff m ∈ Y, and the lattice is the reversed power set of M. This is exactly the canonical-form regime of Prop. 1.
- (iii) *With dependent directions (k > d) it is not distributive.* A brute-force enumeration in R^2 with d = e_1, e_2, e_1 + e_2 gives a 7-element lattice in which a = R({e_2}) has a ∧ (R({e_1+e_2}) ∨ R({e_1})) = a, while (a ∧ R({e_1+e_2})) ∨ (a ∧ R({e_1})) = R({e_2, e_1+e_2}) ⊊ a. The same enumeration finds failures for 5 and 6 equally spaced directions, and none for 3 or 4.
- (iv) *With the conic-hull join on all convex cones* it fails exactly as subspaces do on van Rijsbergen's p. 39: three rays in a plane with a between b and c give a ∧ (b ∨ c) = a but (a ∧ b) ∨ (a ∧ c) = {0}.
- (v) *The paper's literal Def. 7 (∩, ∪ on point sets)* is distributive, as any algebra of sets is, but ∪ leaves the family.

So whether "the lattice" is Boolean depends on which of the paper's several lattices is meant. The object-level lattice, which is the only one proved to be a lattice, behaves like van Rijsbergen's monothetic kinds. Its non-distributivity comes from the finite sample of objects, not from non-commuting projections.

**Join and negation.** Van Rijsbergen's join of subspaces is the closed span, and the orthocomplement V⊥ makes the subspace lattice an orthomodular lattice with a non-truth-functional "choice negation" (ch. 5 p. 66). Xiong defines no complement on concepts. App. D says "Negation corresponds to crossing the relevant threshold hyperplane", which is attribute-level: {v·d ≥ 0} ↦ {v·(−d) ≥ 0}, and the two share the boundary hyperplane. For a concept with |Y| ≥ 2, the set complement of R(Y) is a union of open half-spaces, which is non-convex and not in the family. The polar cone is generated by −d_m (m ∈ Y), is not in general any R(Y′), and supplies an orthocomplement only on the larger lattice of all convex cones, where orthomodularity fails (above). Within the paper's own family, then, there is no orthocomplement. Negation stays Boolean at the level of single attributes and is undefined for concepts.

**Observables vs. thresholded functionals.** In van Rijsbergen a yes/no question is a projector P, self-adjoint and idempotent, and a state ρ gives it probability tr(ρP) (Gleason, dimension ≥ 3; ch. 6 p. 81). For a pure state x and a rank-one P = |d⟩⟨d| this is (d·x)², which is sign-blind: x and −x are the same state. In the Linear Representation Hypothesis a binary concept is a linear functional plus a sign or threshold. The functional is ⟨ℓ̄_m, ·⟩, the Riesz representer ([ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md)'s Riesz isomorphism; van Rijsbergen p. 74; [LIT-230](../literature.d/LIT-230.md), [LIT-243](../literature.d/LIT-243.md)), and the concept is the half-space {v : ⟨ℓ̄_m, v⟩ ≥ τ}. Its whole content is the sign that the projector discards. The lattice elements differ accordingly: subspaces (closed under ±) against cones. Xiong's soft version plays no role of a probability measure on its lattice:

- σ(α(v·d − τ)) is a per-attribute Bernoulli marginal. In canonical form, P(m) + P(¬m) = σ(αv·d) + σ(−αv·d) = 1, so it is additive only over an attribute and its hyperplane-reflection.
- No probability is assigned to R(Y) for |Y| ≥ 2 and no joint over attributes is defined.
- Theorem 1 immediately thresholds the marginals away.
- The Eq. 5 inclusion is not a conditional probability and is not even reflexive (Incl(A ⊑ A) ≤ σ(1)).
- The min/max profile operators are Gödel t-norm/co-norm on real-valued, signed, ℓ2-normalised vectors. They do satisfy min + max = x + y coordinatewise, but that is a property of the reals, not a valuation on the lattice.

There is nothing corresponding to Gleason's uniqueness.

**Order and compatibility.** Every operation in the paper is order-independent: ∩ and ∪ of sets, min and max of profiles, and a closure that is idempotent and monotone. Nothing is measured sequentially, no state is updated after a "question", and no projection onto a region is ever applied. Thresholding a projection is not projecting, and alternating projections onto convex sets, which would not commute, are never used. So nothing in the text corresponds to van Rijsbergen's non-commuting A → R → A (ch. 1 pp. 21–22), or to his compatibility relation, under which distribution holds for compatible elements. Whether the paper's non-distributive lattices admit a meaningful compatibility relation is left to Open questions. For the same reason contextuality in either sense ([THEORY-012](../theory.d/THEORY-012.md)'s global-section sense; [THEORY-013](../theory.d/THEORY-013.md)'s Contextuality-by-Default) has no purchase on the text. There are no contexts of jointly performable measurements and no context-indexed distributions: the attribute marginals are all read off one fixed embedding.

**Kernel invariance ([THEORY-004](../theory.d/THEORY-004.md), [THEORY-008](../theory.d/THEORY-008.md)).** This is my inference, not the paper's. The Fisher direction of Eq. 11 is a regularised linear readout of exactly [THEORY-008](../theory.d/THEORY-008.md)'s family, w = G⁻¹Xᵀz/M with G a (within-class) covariance plus λI. By Sherman–Morrison, the within-class and total-covariance forms give parallel directions when the classes are equally weighted. The midpoint threshold (Eq. 12) is likewise a function of the projections. So the recovered incidence I_δ, and with it the Theorem 1 lattice and the Eq. 4 profiles, is a function of the embedding kernel and the labels. It is invariant under orthogonal reparametrisation ([THEORY-004](../theory.d/THEORY-004.md)), and in the λ → 0 limit under any invertible linear map v ↦ Av, since (Av)·A^{−T}Σ⁻¹Δµ = v·Σ⁻¹Δµ. The larger invariance is the one Park et al. §3 require ([ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md): the inner product is not identified by training). The paper's Mean baseline has only the orthogonal invariance, which may be part of why it loses. The paper does not discuss any of this, and it does not use the causal inner product of §2.1 in its experiments.

**Antecedents in the paper not held in either record.** Park, Choe, Jiang & Veitch (ICLR 2025) on categorical concepts as polytopes and hierarchy as orthogonality, which this paper positions itself against as "extensional"; Xiong & Staab (ICLR 2025) on FCA lattices in masked LMs; Engels et al. (ICLR 2025) on non-linear features; Ganter & Wille's FCA. The anthology holds the paper's other direct antecedent, [ANTH-LIT-606](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-606.md) (account [ANTH-THEORY-090](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-090.md)), which the anthology's account [ANTH-THEORY-034](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-034.md) extends.

## Bearing on the record

- **No THEORY in this record is supported or contradicted by the paper's own claims.** It does not address the kernel ([THEORY-004](../theory.d/THEORY-004.md), [THEORY-008](../theory.d/THEORY-008.md)) or contextuality ([THEORY-012](../theory.d/THEORY-012.md), [THEORY-013](../theory.d/THEORY-013.md)). Read through [THEORY-008](../theory.d/THEORY-008.md), its attribute directions are regularised readouts, and its empirical content is therefore a statement about the embedding kernel. That is consistent with [THEORY-008](../theory.d/THEORY-008.md) but not evidence for it.
- **Candidate THEORY, not sourced by this paper.** One inner product gives two polarities: orthogonality yields the orthomodular subspace lattice of [LIT-262](../literature.d/LIT-262.md), and v·d ≥ 0 yields the lattice of convex cones. The latter is an ortholattice under the polar map but is not orthomodular, and its thresholded, finite-sample restriction is an ordinary FCA lattice. Filing this needs a source for cone duality and for FCA (Ganter & Wille; Birkhoff's polarities), neither of which is held. This reading is my working, not the paper's.
- **For [LIT-262](../literature.d/LIT-262.md).** The paper is a modern, learned-embedding instance of van Rijsbergen's ch. 2 construction, arrived at independently: it cites FCA, not Hardegree or van Rijsbergen. It confirms that construction's reach and adds none of the ch. 5–6 apparatus: no projectors, no trace-rule probability, no conditional.
- **ML practice.** The anthology already holds the work ([ANTH-LIT-460](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-460.md)) and files no practice from it, correctly. App. D's regulariser and "logical steering" uses are not run. Nothing here changes that.
- **Corrections to the anthology's reading** are listed in the header and should be reported to that record, not edited from here. The most consequential concerns the join and the GPT-4o origin of the "ground-truth" formal context.

## Limitations

- **The lattice is not evidence.** Theorem 1 holds for any binary relation, so "LLMs encode concept lattices" (abstract, Conclusion) is supported only to the extent that the thresholded incidence matches an external one (Table 1, at 70–83 F1). No lattice-level agreement is measured: for example, recovered vs. annotated concept lattices, or closure and absorption laws.
- **The attribute ground truth is itself LLM output** (GPT-4o), unvalidated against human annotation. The probes and the annotator share the medium being studied.
- **The join is ill-defined as written** (see corrections), and the soft operators are not shown to be soft versions of the region operators. Under the paper's own Eq. 5 their orientation is reversed. In my simulation (20–50 random attribute dimensions, 16,000 draws across four scale/shift settings, with and without ℓ2 renormalisation), Incl(A ⊑ min(π_A, π_B)) > Incl(min ⊑ A) and Incl(max ⊑ A) > Incl(A ⊑ max) in every draw. So the "meet" profile sits above A and the "join" profile below it: min is the FCA join's intent (shared attributes) and max the meet's. This matches the paper's own description of π as "a continuous analogue of an FCA intent". The effect is small in magnitude (mean inclusion values 0.47–0.54). The symmetric equality scores of Eqs. 8–9 used for Fig. 4 cannot detect it. Whether the released code follows Eq. 6 as printed is unverified.
- **Table 3's "meets" are refinements of one input, not common subconcepts,** and its pairs appear not to meet the Fig. 4 sampling condition. The qualitative claim of "refined category intersections" is not what the table shows.
- **Embeddings are of isolated lemma strings,** token-averaged, not of contexts, and Def. 2's intervention property is never checked. The paper's own limitation (App. D) names only non-linear features (Engels et al.) and domain generality.
- **Unreported protocol details:** train/test split, Table 2's decision rule and negative sampling, the definition of the Mean baseline in Tables 1–2, and numeric MRR values.
- Minor slips: Eq. 7 cites "Eq. (2)" for Eq. 5; App. C writes rowspace for the range of D; Fig. 4 axis labels only.

## Open questions

- Does the object-level lattice recovered from the probes (at a fixed δ) match the lattice of the annotated context? What is the δ-sensitivity (App. B.4 notes δ changes the lattice)? This is the direct test of the hypothesis and is not run.
- With attributes a model learned rather than ones an annotator named (for example, sparse-autoencoder features), does the thresholded incidence still give a lattice that aligns with WordNet?
- Is there a compatibility relation on these lattices, in van Rijsbergen's lattice-theoretic sense (ch. 5), under which distribution is restored locally? Do "incompatible" attribute pairs coincide with dependent (non-orthogonal under the causal inner product) directions? The text gives nothing to go on.
- Would any sequential use of these concepts (steer toward a meet, then read a join) show order effects? If so, would a Contextuality-by-Default analysis ([LIT-264](../literature.d/LIT-264.md), [THEORY-013](../theory.d/THEORY-013.md)) find contextuality or only inconsistent connectedness? The paper performs no sequential operation, so this is untouched.
- Does a sign-blind, Gleason-style measure (tr(ρP) on subspaces spanned by attribute directions) predict the incidence as well as the sign-sensitive half-space rule? That would say whether LLM attribute concepts are better modelled as van Rijsbergen's projectors or as Xiong's half-spaces.

## Corrections to the seeded skim

- The join is not "the conic hull of the two concepts' attribute directions — the smallest region covering both" ([ANTH-LIT-460](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-460.md) takeaways; the anthology's reading of it; [ANTH-THEORY-034](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-034.md)). Def. 7 (p. 5) defines the join as the set union A ∨ B := R(Y_A) ∪ R(Y_B). It says this "can be approximated by the conic hull spanned by the attribute directions of A and B" (p. 5; "their defining directions", p. 5 l. above Def. 7). The union of two cones is in general neither convex nor a region R(Y), so it is not in the lattice. The conic hull of the attribute directions {d_m} lives in the dual space, and its dual cone is R(Y_A ∪ Y_B), which is the meet (my check). The least region in the family that contains both is R of the Galois closure of Y_A ∩ Y_B (my check). None of these three objects is used in the experiments, which use the min/max profiles of Eq. 6. The anthology presents as settled a definition the paper states inconsistently.
- The complete lattice proved is the lattice of the crisp object context F_δ (Theorem 1, App. B), a finite FCA lattice over the sampled objects. It is not a lattice of regions. "The regions form a complete lattice under inclusion" (the anthology's reading; [ANTH-THEORY-034](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-034.md) "What was actually shown") is not proved in the paper. It is true for the family {R(Y)}, which is closed under intersection and contains R^d, but only with the closure join, not the paper's union.
- "Soft versions are defined" is accurate for definitions, but the soft incidence does no work in the theorem. It is thresholded at δ into a crisp relation before any lattice appears, and App. B.4 says α "does not affect order-theoretic conclusions". Thresholding σ(α(v·d − τ)) ≥ δ is a hard threshold at τ + α⁻¹·logit(δ). No soft or fuzzy lattice is proved.
- The anthology's reading says the paper "builds on the causal inner product … which is what makes the independence condition for the canonical form more than a convenience". The causal inner product appears only in the §2.1 preliminaries. Prop. 1 does not use it: the condition is solvability of Dc = τ. The experiments use raw last-layer hidden states averaged over token positions, with Fisher-LDA directions (Eq. 11), not the unified space g, ℓ of §2.1. The link to causal separability is the anthology's inference.
- The canonical-form condition is Dc = τ solvable, i.e. τ in the column space (range) of D. Linear independence of the k attribute directions (so k ≤ d) is the sufficient condition given in App. C, Remark (i). That remark says "rowspace(D) = R^k", a slip for the range of D. The anthology's "canonical form when attribute directions are linearly independent" is right as a sufficient condition.
- Evidence is not simply "WordNet sub-hierarchies, a hand-built ontology" ([ANTH-LIT-460](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-460.md), [ANTH-THEORY-034](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/theory.d/THEORY-034.md)). Only the is_a hierarchy and the synsets come from WordNet. The attribute schema (60–184 attributes per domain) and the full object–attribute incidence were generated by GPT-4o with few-shot prompting (§4.1; App. A) and treated as ground truth. So Table 1 measures agreement between one LLM's annotations and linear probes on other LLMs' embeddings. This is a circularity the "friendliest test" framing misses.
- The anthology's reading says LLM embeddings "encode the concept lattices and their logical structure". What is tested is (i) per-attribute probe recovery (Table 1), (ii) pairwise subsumption from the Eq. 5 score (Table 2) and (iii) MRR ranking of gold meet/join candidates (Fig. 4). No closure, lattice identity or recovered-lattice comparison is reported.
- The anthology's reading, recommendation R2, says generalisation "needs a conic hull rather than an average". The experiments' join is the coordinatewise max of attribute profiles (Eq. 6), not a conic hull. What the evidence supports is profile max/min beating a mean-embedding baseline in Fig. 4.
- The paper's own summaries of Table 1 overstate it slightly. The text says Linear is "above 70%" on abstract domains, but Mistral-7B WN-Event is 69.7. It says Mean is "59–68% F1", but Gemma-7B Mean is 50.1–56.3 and Mistral Event is 56.5. It says Random is "45–48%", but the Cognition rows are 49.3–50.1. In Table 2, "consistently outperforms" fails for Mistral-7B WN-Plant, where Linear F1 is 57.1 and Mean F1 is 60.5.
