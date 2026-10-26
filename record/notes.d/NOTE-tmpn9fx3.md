---
status: Read
paper: LIT-tmpsuo6l
title: 'Ameisen et al. — Circuit tracing: revealing computational graphs in language models'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read on 2026-10-26 from the HTML of the Transformer Circuits article
    (transformer-circuits.pub/2025/attribution-graphs/methods.html, headed
    "Published March 27, 2025"), fetched that day and reduced to text by
    the reader's own script. Read in full: the abstract, Introduction,
    Building an Interpretable Replacement Model, Attribution Graphs (with
    the acronym, factual-recall and addition case studies), Global Weights,
    Evaluations, the Biology summary, Limitations, Discussion with its Coda,
    and Related Work. Read among the appendices: CLT Implementation Details
    (compute and ML details), Validating the Replacement Model (all three
    parts), Nuances of Steering with Cross-Layer Features, Unexplained
    Variance and Choice of Steering Factors, and the opening of Similar
    Features and Supernodes. Not read: the rest of the appendices
    (Attribution Graph Computation, Graph Pruning, Iterative Patching,
    Details of Interventions, the interface notes, residual norms,
    interference weights, number output weights, the small-versus-large
    addition comparison, additional evaluation details, prompt lists).
    The article's figures and graphs are interactive; they were not
    rendered, and their content is taken from the text, captions and the
    inline tables, which the text reproduces.
date: '2026-10-26'
summary: >-
  A cross-layer transcoder (CLT) replaces a model's MLPs with sparse
  features, each reading one layer and writing to all later ones. On one
  prompt, freezing attention patterns and normalization denominators and
  adding back the reconstruction error makes a local replacement model that
  reproduces the model exactly and is linear between features, so its
  attribution graph decomposes each feature's pre-activation into edges.
  The graphs are hypotheses about the model, tested by perturbing features
  in it. The authors' own measurements: the replacement matches the
  model's top token on about half of prompts, and its perturbation
  responses agree with the model's for a layer or two and then diverge.
---
<!-- inactive-ok-file: CLAIM-tmpwr001 THEORY-022 THEORY-802 THEORY-tmpkd3fq — Proposed; the record's own claim and neighbouring accounts this reading bears on, cited as open -->
# NOTE-tmpn9fx3: Ameisen et al. — Circuit tracing: revealing computational graphs in language models

## Contribution

A procedure for drawing, on one prompt, the graph of features through which
a large language model reaches its output, with a stated sense in which the
graph is exact and a stated sense in which it is a hypothesis. It is exact
for a local replacement model: the original with its MLPs replaced by a
cross-layer transcoder, its attention patterns and normalization
denominators frozen, and its reconstruction error added back as constants.
It is a hypothesis about the original, tested by perturbing features in
the original and checking downstream effects. The paper also measures,
more than most such work, how far the two come apart.

## Key insight

Make the problem linear where you can and say where you could not. The
transcoder bridges each MLP nonlinearity, the frozen attention patterns and
denominators remove the others, and what is left is a large fully connected
network on one prompt whose only nonlinearities are the features' own
thresholds. Every edge is then a direct linear effect, and every feature's
pre-activation is the sum of its incoming edges. The cost is moved, not
removed. In the Discussion's words, the complexity of credit assignment
"must have gone into the frozen components", or into multi-step paths, or
into "our CLT taking a non-mechanistically faithful shortcut".

## Assumptions

- **CLT.** For layer ℓ, a^ℓ = JumpReLU(W_enc^ℓ x^ℓ), and the MLP output of
  layer ℓ is reconstructed as Σ_{ℓ' ≤ ℓ} W_dec^{ℓ'→ℓ} a^{ℓ'}. Loss: summed
  MSE over layers plus λ Σ tanh(c · ‖W_dec,i‖ · a_i). Features from 300K to
  10M on the 18-layer model ("18L", no MLP in layer 0, so 17 CLT layers),
  300K to 30M on Claude 3.5 Haiku.
- **Local replacement model** for prompt p: CLT in place of the MLPs,
  attention patterns and normalization denominators from the model's
  forward pass on p, and at each (position, layer) an error term equal to
  the true MLP output minus the CLT output on p.
- **Edges.** A_{s→t} = a_s w_{s→t}, with w the sum over all linear paths
  (residual and frozen attention OV) from s's decoders to t's encoder,
  computed by a backward Jacobian with stop-gradients on MLP outputs,
  attention patterns and normalization denominators. Error nodes have no
  inputs.
- **Graph nodes.** Output nodes for the tokens covering 95% of probability
  (at most 10), active features at each position, token embeddings, error
  nodes.
- **Pruning** by indirect influence on the logits, B = (I − A)⁻¹ − I over
  the row-normalized absolute adjacency matrix (a DAG, so the Neumann
  series terminates).
- **Validation by constrained patching**: a feature's decodings are changed
  over a chosen layer range, MLP outputs in the range are clamped to
  precomputed values, attention patterns stay frozen, and the end layer of
  the range is chosen to maximize the effect.

## Key results

- **Replacement fidelity.** The largest 18L CLT (10M features) matches the
  model's top token on 50% of a set of pretraining-style prompts filtered
  to those the model gets right with confidence under 80%. Normalized
  reconstruction error ~11.5% at L0 88 (18L, 10M); 21.7% at L0 235 (Haiku,
  30M). CLTs beat per-layer transcoders (PLTs) at equal size on every
  metric, and both beat thresholded neurons.
- **Graphs.** On one prompt, mean path length 2.3 for a 10M CLT against 3.7
  for 10M PLTs; on another, completeness 0.80 against 0.78 and replacement
  score 0.61 against 0.37. Pruning at the default threshold (0.8) on an
  acronym prompt leaves 55 nodes at completeness 0.70; at 0.95, 236 nodes
  at 0.87. CLTs collapse "amplification" chains: a seven-step chain of
  Copenhagen features in a PLT graph becomes layer-1 features, which the
  authors count both as a gain and as a case of the CLT's causal structure
  differing from the model's.
- **Case studies.** Acronym ("The National Digital Analytics Group (N" →
  "DAG"), factual recall (Michael Jordan → basketball, 65% confidence) and
  two-digit addition (36 + 59 = 95, on Haiku). In addition, inputs split
  into a ones-digit path (lookup-table features such as _6 + _9 →
  sum = _5) and low- and moderate-precision magnitude paths, which
  combine. Inhibiting the _6 input feature makes Haiku answer 98; inhibiting
  _9 gives 91, not the 92 the same logic predicts ("such numerology must be
  taken with a grain of salt").
- **Global weights.** Virtual weights between features are dominated by
  interference: features that never co-occur on the data have large
  weights. Weighting by co-activation statistics (TWERA, E[a_j a_i]/E[a_j]
  × V_ij) makes them more interpretable, but "heavily relies on the
  coactivation statistics" and loses inhibition. Restricted to the 2,931
  features active on addition, the virtual-weight graph of 18L is
  interpretable.
- **Faithfulness (Evaluations and appendix).** Over 20 prompts, a node's
  logit influence predicts the KL effect of ablating it better than its
  direct logit edge or its activation. Feature-to-feature: Spearman 0.72
  between graph influence and the normalized effect of ablating the source
  (constrained patching over [i, i + 2]). The local replacement model's
  response to perturbation agrees with the model's "when measured one
  layer after the intervention" and then diverges; directions degrade
  gradually, magnitudes "catastrophically", and both are slightly worse for
  larger dictionaries.
- **Validation is partly guaranteed.** "Direct feature-feature interactions
  described by an attribution graph are nearly forced to be confirmed in
  steering experiments (when we freeze attention patterns) … and guaranteed
  when choosing the intervention layer to be the same as the target
  feature's encoder layer. Thus, the nontrivial thing we are testing with
  perturbation experiments is the validity of the attribution graph's
  claims about 'knock-on effects.'"
- **Steering strengths are ad hoc.** Inhibition usually needs clamping to
  negative multiples of the original activation, and injection needs
  activations "significantly greater than that feature's typical
  activations".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | On a prompt, the local replacement model reproduces the model's activations and outputs exactly, and each feature's pre-activation is the sum of its incoming edges | strong (by construction) | Local Replacement Model; Constructing an Attribution Graph; re-derived in THEORY-tmpbtnf0 |
| C2 | Under constrained patching with frozen attention, a direct edge's predicted effect is confirmed by construction when the patch ends at the target's encoder layer, so perturbations test only knock-on effects and outputs | strong (by construction; the authors' own statement) | Appendix: Nuances of Steering; THEORY-tmpbtnf0 |
| C3 | The replacement's perturbation responses track the model's for about a layer and diverge with depth, worse in magnitude than direction and slightly worse for larger dictionaries | moderate (18L; 20 prompts for the influence tests) | Evaluating Mechanistic Faithfulness and its appendix; THEORY-tmpm4ifd |
| C4 | CLTs give shorter paths and higher replacement scores than PLTs of equal size, and both beat thresholded neurons | moderate (dataset averages shown as plots; two single-prompt tables) | Evaluations |
| C5 | A feature whose pre-activation is additively separable in two operands cannot be a general sum feature, so one-step addition needs intermediate lookup-table features | strong (argument), with the separability premise | Addition Case Study, footnote; THEORY-tmp7rb6m |
| C6 | Haiku adds two-digit numbers by parallel ones-digit and magnitude heuristics that combine, a "graph of heuristics" | moderate for 36 + 59 and the addition domain | Addition Case Study; Global Weights in Addition |
| C7 | Global virtual weights are dominated by interference and need on-distribution statistics to read | moderate (examples) | Global Weights |

## Concepts

- **Cross-layer transcoder (CLT)**: a sparse dictionary whose features each
  read the residual stream at one layer and write to the MLP outputs of
  that layer and all later ones.
- **Replacement model / local replacement model**: the model with the CLT
  in place of its MLPs; the local version adds frozen attention, frozen
  denominators and error terms for one prompt.
- **Attribution graph**: nodes are active features, embeddings, error terms
  and output logits on one prompt; edges are direct linear effects in the
  local replacement model.
- **Supernode**: a hand-made group of features with a shared role on the
  prompt; "the not-very-principled abstraction of 'supernodes'".
- **Virtual weight**: ⟨Σ_ℓ W_dec^{s,ℓ}, W_enc^t⟩, the input-invariant part
  of a residual-direct edge.
- **Mechanistic faithfulness**: how far perturbations in the local
  replacement model have the same downstream effects as in the model.
- **Constrained patching**: perturbing a feature's decodings over a layer
  range with MLP outputs clamped inside it, so no knock-on effect arises
  within the range.

## Connections

It extends Dunefsky et al. (LIT-tmptgo43), "essentially the same" attribution
rule, to cross-layer features, with error nodes from Marks et al. and a
global pruning rule. It inherits the freezing of QK circuits from Elhage et
al.'s framework. Its addition features place Nikankin et al.'s "bag of
heuristics" in a graph and set it beside Kantamneni and Tegmark's Fourier
subspaces. Its companion is LIT-tmpjvwet. The same team's superposition
paper is LIT-323 and its interpretability-by-dictionary line includes the
workspace paper LIT-1347. MIB (LIT-tmprlq7z) is the neighbouring attempt to
score circuit localization against a fixed counterfactual.

## Bearing on the record

- **CLAIM-tmpwr001.** The paper builds the claim's caution into its method:
  features are units of a stand-in, the graph is a hypothesis, and the
  authors measure the stand-in's divergence. Its own example of divergence
  (Copenhagen–Denmark amplification invisible in CLT graphs) is a case of a
  representation that reproduces outputs while computing differently.
- **THEORY-022.** The addition features here are not the grokking network's
  circle: they include ones-digit lookup tables, magnitude ranges and
  "starts with 51" patterns, some of which "aren't describable in Fourier
  terms", alongside mod-10 and mod-100 features that are. The record's
  claim is about a network trained on modular addition; this is a model
  trained on text, and both are compatible. THEORY-tmp7rb6m explains why
  some intermediate step is forced.
- **THEORY-802 and QUESTION-234.** The authors concede the decomposition is
  a choice: supernodes are hand-grouped, features split with dictionary
  size ("the degree of generality of the features appears to decrease with
  the size of our cross-layer transcoder"), and "there's no guarantee that
  the CLT features are the most parsimonious way to split up the
  computation". That is THEORY-802's basis-relativity at the level of
  dictionaries, not tested here.
- **THEORY-tmp8cat0 / THEORY-tmpkd3fq.** The Limitations section says the
  method cannot see induction: on "Aunt Sally … Aunt" the graph shows only
  that "Sally" was earlier, "a kind of regression" against the earlier
  attention-only analyses. Attribution graphs therefore give no test of
  THEORY-tmpkd3fq's large-model thesis.
- **QUESTION-tmpivbso.** A CLT trained per checkpoint would give the
  circuit-only description the question compares against, but nothing here
  matches features across checkpoints, and the cost is large (estimated
  210 H100 hours for 2M features on Gemma 2 2B).
- **Accounts filed.** THEORY-tmpbtnf0 (Active, by construction): what an
  attribution graph is exact for and what a perturbation can test.
  THEORY-tmpm4ifd (Active, as measured): the replacement's faithfulness on
  18L. THEORY-tmp7rb6m (Active, re-derived): the parallelogram constraint.

It is interpretability practice, not an instruction for training models;
the anthology may want it as a reading (`anthology-candidate`).

## Limitations

The authors' own list, which the record keeps: attention circuits are
missing (QK is frozen; "we have also found many cases where this
limitation renders our attribution graphs essentially useless", induction
and multiple choice among them); reconstruction error leaves "dark matter", and on
an obfuscated jailbreak prompt almost every node is an error node; inactive
and inhibitory features are invisible unless a contrasting prompt is
chosen; graphs stay complex; features split or absorb; global weights are
hard to read; mechanistic faithfulness is unguaranteed and validated
coarsely, by perturbing supernodes and choosing the most effective layer.
The record adds:

- **Validation strength varies with the layers.** Because direct effects
  are confirmed by construction, a reported validation means more when
  it concerns outputs or multi-hop effects. The case-study figures do not
  always say which they are.
- **The faithfulness figures disagree.** The Evaluations section reports
  "~0.8 cosine similarity" one layer after a perturbation; the appendix
  puts the 10M dictionary's figure "around 60–80%".
- **Counting slip.** The Biology section announces "nine behavioral case
  studies" and lists ten.
- **A footnote slip.** The parallelogram footnote begins "Write f_pre for
  the preactivation of x", meaning of f.
- **Pruning figures.** The text says pruning cuts nodes tenfold "while only
  reducing the behavior explained by 20%"; the one table shows completeness
  0.70 at the default threshold, with no unpruned value for that prompt, so
  the 20% cannot be checked from what is shown.

## Open questions

- Can QK attribution (pairs of key-side and query-side features) be made
  tractable, so that induction and multiple-choice become visible?
- Does training a replacement for faithfulness rather than MSE close the
  layer-by-layer divergence?
- How much of a validated circuit survives a different dictionary of
  similar fidelity?
