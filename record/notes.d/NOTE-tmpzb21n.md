---
status: Read
paper: LIT-tmpsavwt
title: 'Geiger, Wu, Potts, Icard and Goodman — Distributed alignment search (DAS)'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv PDF, 2303.02536v4 (21
    February 2024; 28 pages), whose header reads "Proceedings of Machine
    Learning Research vol 236:1–23, 2024, 3rd Conference on Causal Learning
    and Reasoning". Text extracted with pdftotext, tables with its layout
    mode. Read: §§1–6 (introduction, related work, the method with
    Definitions 1–5 and the boolean example, the hierarchical-equality
    experiment with the random-network control, the MoNLI experiment,
    conclusion) and Appendices A–D (data, reproducibility, the brute-force
    and localist baselines, subspace DAS, runtimes, the learned rotations,
    common questions). Figures read from captions. Earlier arXiv versions
    were not compared.
date: '2026-10-26'
summary: >-
  Causal abstraction tests whether a network implements a high-level
  causal model by interchange interventions under an alignment of
  variables, which earlier work found by brute-force search over disjoint
  sets of neurons. DAS learns the alignment instead: an orthogonal
  rotation trained by gradient descent so that swapping rotated subspaces
  between inputs reproduces the high-level model's counterfactuals. In a
  feed-forward network trained on hierarchical equality and in BERT
  fine-tuned on monotonicity NLI it finds alignments with interchange
  intervention accuracy of 1.00 where the best localist ones reach 0.73
  and 0.51. In BERT the entailment subspace decomposes into the two word
  identities; in the equality network it does not. On random networks DAS
  raises accuracy above chance only when the hidden layer is much wider
  than the input.
---
<!-- inactive-ok-file: THEORY-802 CLAIM-tmpwr001 CLAIM-263 — Proposed; the account, claim and test this reading bears on, cited as open -->

# NOTE-tmpzb21n: Geiger, Wu, Potts, Icard and Goodman — Distributed alignment search (DAS)

## Contribution

It removes the assumption that a high-level variable must live in a
fixed set of neurons. Earlier causal-abstraction analyses chose an
alignment of variables to disjoint neuron groups and searched over such
groups by brute force; DAS searches over all orthogonal changes of basis
by gradient descent, and aligns variables with subspaces. It is the
method MIB later found best for causal-variable localization
([THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md)) and the method whose subspace patches Makelov et al.
([LIT-968](../literature.d/LIT-968.md)) and Wu et al.'s reply ([LIT-961](../literature.d/LIT-961.md)) argue over.

## Key insight

Whether a network "implements" an algorithm under interchange
interventions depends on the basis in which one looks. The paper's
boolean example makes it exact: a linear network whose first layer
rotates the input by 20° fails the conjunction model in the neuron basis
and passes it perfectly once the hidden layer is rotated back by 20°.
So a failed localist test does not show the algorithm is absent, and the
basis should be searched, not assumed.

## Assumptions

- **Constructive causal abstraction** (Definition 1): H abstracts L under
  alignment Π = ({Π_X}, {τ_X}) when τ(L_{I←i}(x)) = H_{τ(I←i)}(τ(x)) for
  every input and intervention.
- **Interchange intervention** (Definition 2): fix chosen variables to the
  values they take on source inputs, run on a base input.
- **Distributed interchange intervention** (Definition 3): with an
  invertible R from the target variables N to a space Y decomposed into
  orthogonal subspaces Y_0, …, Y_k, replace the mechanism of N by
  F*(v) = R⁻¹(Proj_{Y_0} R F_N(v) + Σ_j Proj_{Y_j} R F_N(s_j)). It is a
  soft intervention: Y_0 keeps the base input's value.
- **Training objective** (Definition 4): cross-entropy between the high-
  level model's counterfactual output and the low-level network's output
  under the distributed intervention; only R is trained (PyTorch's
  orthogonal parametrization), the network and high-level model are
  frozen. Target layer and subspace sizes are discrete hyperparameters.
- **IIA** (Definition 5): the share of aligned interventions whose low-
  and high-level effects agree; it coincides with α-on-average
  approximate causal abstraction (Geiger et al. 2023).
- **Baselines.** Brute force over sliding windows of neurons equal to the
  subspace size (for BERT only windows starting at 0, 64, 128, 256 and
  512 of the [CLS] vector), and the "closest" localist alignment, an
  axis-aligned signed permutation read off the learned rotation
  (Algorithm 1).
- **The networks** solve their tasks perfectly on train and test before
  any alignment is sought. Each cell reports the best of three seeds for
  the rotation, "interchange intervention accuracies for the learned
  alignment on training data" (Tables 1–2 captions).

## Key results

- **Boolean example** (§3). W rotates (x₁, x₂) by 20°, the readout is
  h₁ + h₂ − 1.8. On input (0, 1), h = (−0.34, 0.94) and the output is
  −1.2; setting h₁ to 1.34 gives 0.48. An interchange of H₁ from (1, 1)
  into the base (0, 1) gives −0.26, so false, where the high-level model
  gives true. Rotating by −20° makes the hidden units equal the inputs,
  and the alignment is perfect. (The record recomputed these values.)
- **Hierarchical equality** (§4, Table 1). A three-layer ReLU network on
  (w = x) = (y = z). For the two-equality-relations model, DAS reaches
  IIA 0.88–1.00 at layer 1 (1.00 with |N| = 16 and subspaces of 8 each,
  0.99 with |N| = 32), 0.51–0.67 at layer 2 and about 0.5 at layer 3; the
  best brute-force alignment reaches 0.60 and the closest localist one
  0.73. A model with only the left equality reaches 0.99 at layer 1; a
  model holding only the first argument's identity stays near 0.5, and so
  does an attempt to find the first argument's identity inside the left-
  equality subspace. The authors read this as a relation "entirely
  abstracted from the entities participating in the relation".
- **Random networks** (§4.4, Figure 3). On frozen random networks at
  chance, IIA for the two-equality model is 0.50, 0.50, 0.51, 0.55 and
  0.64 at hidden sizes 16, 64, 256, 1028 and 4096 with 16 input
  dimensions. The authors take this as "a check that demonstrates DAS
  cannot construct entirely new behaviors from random structure".
- **MoNLI** (§5, Table 2). BERT-base fine-tuned on MNLI and then MoNLI,
  [CLS] token, layers 7, 9 and 11. The negation-and-lexical-entailment
  model reaches 1.00 at layer 9 with subspaces of 256 each; lexical
  entailment alone 1.00 at layer 9; a model holding only the premise
  word's identity 0.93–0.96 at layer 9. The closest localist alignments
  reach 0.47–0.51. Inside the learned entailment subspace a second
  rotation aligns the two words' identities at 0.97–0.98, so the
  entailment representation is "a 'data structure' containing two
  representations of word identity".
- **Runtime** (Appendix B). DAS 502 s and 1105 s against brute force
  31 s and 198 s over a few windows; exhaustive brute force is estimated
  at C(32, 16) ≈ 6 × 10⁸ and C(768, 32) alignments.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A localist failure can be a failure of basis, not of the algorithm | demonstrated | the boolean example (re-computed) |
| C2 | In the trained equality network and in fine-tuned BERT, learned rotations give near-perfect IIA where localist alignments do not | strong for these two networks, on the rotation's training data | Tables 1–2 ([THEORY-tmpgqlal](../theory.d/THEORY-tmpgqlal.md)) |
| C3 | The equality network's relation representation does not decompose into the inputs' identities; BERT's entailment representation does | moderate | last columns of Tables 1–2 |
| C4 | DAS cannot construct new behaviour from random structure | weak: true at small widths, contradicted in part at 4096 | Figure 3 ([THEORY-tmpqhbjf](../theory.d/THEORY-tmpqhbjf.md)) |
| C5 | Gradient search is faster than exhaustive brute force | strong | Appendix B |

## Concepts

- **Alignment**: a map from each high-level variable to low-level
  variables (here, a subspace) and a function τ from their values to the
  high-level variable's values.
- **Localist vs distributed**: aligned with disjoint neuron sets, or with
  subspaces of a rotated basis.
- **IIA**: interchange intervention accuracy.
- **Subspace DAS**: a second rotation inside a learned subspace, to test
  whether it decomposes into finer variables.

## Connections

It extends causal abstraction (Geiger et al. 2021) and approximate
abstraction (Beckers, Eberhardt and Halpern, [LIT-1310](../literature.d/LIT-1310.md); Geiger et al.
2023), and counts circuit analyses, causal scrubbing ([LIT-tmpqtkua](../literature.d/LIT-tmpqtkua.md))
among them, as causal abstraction. Its successors in the record are
Boundless DAS (cited by Wu et al., [LIT-961](../literature.d/LIT-961.md)), the critique of subspace
patching by Makelov et al. ([LIT-968](../literature.d/LIT-968.md)), MIB's causal-variable track
([LIT-tmprlq7z](../literature.d/LIT-tmprlq7z.md), [THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md)) and [LIT-987](../literature.d/LIT-987.md).

## Bearing on the record

- **[QUESTION-234](../questions.d/QUESTION-234.md) and [THEORY-802](../theory.d/THEORY-802.md).** Three observations.
  - *The converse of [THEORY-243](../theory.d/THEORY-243.md).* [THEORY-243](../theory.d/THEORY-243.md) shows two basis-related
    alignments that tie; the boolean example shows a model that fails in
    one basis and holds in another. Together they say the verdict of an
    interchange test is relative to the decomposition into units, which
    is [THEORY-802](../theory.d/THEORY-802.md)'s thesis; the boolean case is constructed, so it does
    not meet [THEORY-802](../theory.d/THEORY-802.md)'s promote_when.
  - *A symmetry built into the instrument.* In Definition 3 the rotation
    enters only through R⁻¹ Proj_{Y_j} R, the orthogonal projector onto the
    subspace R⁻¹Y_j. Any two rotations that map the same subspaces give
    identical interventions on every input, so DAS can identify at most a
    set of subspaces, and every alignment it finds ties with all its
    rotations within those subspaces. That is a uniqueness bound up to a
    stated symmetry for the instrument, not for networks, of the kind
    [QUESTION-234](../questions.d/QUESTION-234.md)'s second answer asks for (the record's observation; the
    paper does not state it).
  - *Two high-level models that both pass in a trained network.* In BERT
    the lexical-entailment model and, inside its subspace, the
    two-identities model both reach near-perfect IIA. They are related by
    refinement, not by a change of basis, so this is not the tie
    [THEORY-802](../theory.d/THEORY-802.md) is about, but it is a trained-network case of more than one
    correct abstraction at one site.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** The MoNLI decomposition is the claim's warning met
  in a network: what was aligned as the variable that decides the label
  (entailment) turned out, one level down, to be the two inputs it is
  computed from.
- **[THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md).** That account notes DAS is supervised by the causal
  model it is scored against. The random-network control is the paper's
  own measure of how much that supervision can manufacture: nothing at
  widths near the input's, 14 points above chance at 4096
  ([THEORY-tmpqhbjf](../theory.d/THEORY-tmpqhbjf.md)).
- **[CLAIM-263](../claims.d/CLAIM-263.md).** A rotation learned per layer is one way to quotient a
  basis symmetry before comparing mechanisms; DAS quotients it relative
  to a hypothesis, [CLAIM-263](../claims.d/CLAIM-263.md) relative to another network.

No instruction for machine-learning practice is recorded
(`anthology-candidate`).

## Limitations

- **Training-set IIA.** Both tables report accuracy "on training data" of
  the rotation, though held-out sets were built (Appendix A.2). With a
  learned rotation, held-out accuracy is what bears on overfitting the
  alignment.
- **Table 2's brute-force row is Table 1's.** The MoNLI brute-force
  baseline, 0.60, 0.56, 0.52, 0.64, 0.64, 0.57, 0.50, 0.51, 0.54, repeats
  the hierarchical-equality row digit for digit; for a different network
  and task this is almost certainly a copying error, so the MoNLI
  comparison with brute force is not usable as printed. The localist row
  differs and stands.
- **The brute-force baseline is said to search "over all layers"** yet is
  reported per layer.
- **Subspaces that fill the layer.** The 1.00 for hierarchical equality
  uses |N| = 16 with two 8-dimensional subspaces, so together they span
  the whole layer and no base component is kept.
- **The random control is read too strongly.** 0.64 at width 4096 is above
  chance; the conclusion that DAS "cannot construct entirely new
  behaviors" holds only for narrow layers.
- **Small slips.** C(768, 32) ≈ 4.2 × 10⁵⁶, not the 2 × 10⁵⁸ of Table 3;
  "|N| = 1028" is presumably 1024; §4.4 refers to "Table 4.4" for
  Figure 3; Algorithm 1 builds L and returns P.
- **Two toy-scale settings**, binary variables, one token position in
  BERT.

## Open questions

- Held out, do the near-perfect alignments survive?
- In a trained network, does a different rotation whose subspaces cross
  the learned ones reach the same IIA? That is [QUESTION-234](../questions.d/QUESTION-234.md) asked of DAS,
  and the paper's three seeds per cell could have shown it.
