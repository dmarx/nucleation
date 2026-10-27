---
status: Read
paper: LIT-tmp5b0z9
title: 'Marks, Rager, Michaud, Belinkov, Bau and Mueller — Sparse feature circuits'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv copy (arXiv:2403.19647v3, 27
    March 2025, fetched from arxiv.org/pdf/2403.19647), 36 pages, headed
    "Published as a conference paper at ICLR 2025"; text extracted with
    pdftotext. v1 and v2 were not compared. Read: §§1–8, the
    reproducibility statement, and Appendices A (edge weights, aggregation,
    stop- and pass-through gradients, Jacobian–vector products), B (the
    Pythia-70M autoencoders with Tables 3–6, and the Gemma Scope ones), C
    (the agreement, Bias in Bios and cluster circuits, from their captions
    and text), D (sample features and neurons), E (classifier training and
    concept bottleneck probing), F (human ratings, Table 7), G (behaviour
    discovery by clustering) and H (quality of the linear approximations).
    The references were skimmed. Figure 3 (faithfulness and completeness)
    was read from a page rendering of p. 5; the circuit diagrams of
    Figures 4 and 7–18 and the scatter plots of Figure 25 were read from
    captions and text only.
date: '2026-10-26'
summary: >-
  Circuits whose nodes are sparse-autoencoder features and autoencoder
  error terms, found in Pythia-70M and Gemma-2-2B by linear approximations
  to indirect effects. On subject–verb agreement, circuits of about 100 and
  500 nodes carry half or more of the behaviour on held-out pairs, where
  neuron circuits need far more, but without the error nodes the feature
  circuits carry little. The annotated circuits show two pathways for
  agreement across a clause. A human removing gender features from a
  classifier's circuit (SHIFT) brings profession accuracy on balanced data
  near an oracle's, and the method runs without supervision on thousands of
  behaviours clustered from the Pile.
---
<!-- inactive-ok-file: THEORY-tmpyawf9 THEORY-tmpt45mh CLAIM-tmpwr001 THEORY-802 — Proposed; accounts and claims this reading files or bears on, cited as open -->
# NOTE-tmpr0gdc: Marks, Rager, Michaud, Belinkov, Bau and Mueller — Sparse feature circuits

## Contribution

It makes circuits out of sparse-autoencoder features. Each hidden state
with an autoencoder is written as a sum of feature terms plus an error
term ε(x), both treated as nodes of the model's computation graph, and
nodes and edges are kept if their estimated indirect effect on a metric
passes a threshold. The estimates are attribution patching or, where that
fails, integrated gradients. It then uses the circuits two ways: to read a
mechanism (agreement across a clause), and to edit a classifier by
removing features a human judges spurious.

## Key insight

Do not throw away what the dictionary misses. Keeping the error term as a
node makes the decomposition exact, so a circuit can be scored for
faithfulness without pretending the features are the whole story. The
same bookkeeping shows how much of the story they are: drop the error
nodes and most of the behaviour goes.

## Assumptions

- **Models and autoencoders.** Pythia-70M with the authors' own
  autoencoders for every embedding, attention, MLP and residual site (width
  64 × d_model, ReLU, MSE plus L1 with λ = 0.1, about 2 billion Pile
  tokens, resampling as in Bricken et al.); and Gemma-2-2B with the public
  Gemma Scope JumpReLU autoencoders of width 16,384, choosing the one with
  L0 nearest 100 at each site, embeddings excluded.
- **Indirect effect.** IE(m; a; x_clean, x_patch) = m(x_clean | do(a =
  a_patch)) − m(x_clean), with m a log-probability difference; for single
  inputs, zero-ablation. Attribution patching is a first-order Taylor
  estimate; integrated gradients averages it over ten points between clean
  and patch. Integrated gradients is used because attribution patching
  underestimates effects in the layer-0 MLP and early residual stream
  (Appendix H).
- **Edges.** The effect of an upstream node on a downstream one with all
  intermediate nodes held at their clean values, estimated with stop
  gradients.
- **Faithfulness** of a circuit C is (m(C) − m(∅))/(m(M) − m(∅)), with
  nodes outside C mean-ablated to position-specific means; completeness is
  the faithfulness of the complement. "We ignore the first 1/3 of our
  circuit, and only evaluate the latter 2/3", because train and test pairs
  do not share tokens.
- **Neurons** are basis directions of any site, "not necessarily preceded
  by a nonlinearity". Neuron circuits have no error terms.

## Key results

- **Agreement circuits** (simple, within a relative clause, across a
  relative clause, across a prepositional phrase; data adapted from
  Finlayson et al.). "The majority of performance in Pythia-70M, resp.
  Gemma-2-2B is explained by only 100, resp. 500 nodes", against "around
  1500, resp. 50000 neurons". In the rendering of Figure 3 the Pythia
  neuron curve reaches about 0.5 at 1,500 nodes, but the Gemma panel
  stops at 30,000 nodes with the neuron curve near 0.3, so the 50,000 is
  beyond the plotted range. With all error nodes removed, the feature
  circuits reach only about 0.25 (Pythia) and stay near zero (Gemma);
  removing only the attention and MLP errors costs less. The authors:
  "removing residual stream SAE error nodes severely disrupts the model".
- **Completeness.** Ablating a few feature nodes removes the behaviour,
  even with all errors left in; hundreds (Pythia) or thousands (Gemma) of
  neurons are needed to do the same.
- **Agreement across a relative clause.** Small circuits (86 nodes,
  faithfulness 0.21 for Pythia; 223 nodes, 0.21 for Gemma) show two
  pathways: subject-number features feed verb-form features directly, and
  the number is also carried to the clause's end by features that detect
  PP/RC boundaries. Gemma adds "NP number trackers" active across a noun
  phrase. Agreement across a relative clause and across a prepositional
  phrase share over 85% of their features in both models.
- **Interpretability.** Crowdworkers from an alignment Slack channel rated
  features higher than neurons on a 0–100 scale: random 52.8 against 32.6;
  agreement-circuit features 62.3 against 30.2; Bias in Bios circuit
  features 81.5 against 36.0 (Table 7).
- **SHIFT.** A linear head on Pythia-70M or Gemma-2-2B is trained on male
  professors and female nurses, where gender predicts profession
  perfectly. The circuit has 67 features (Pythia) and 46 (Gemma); the
  authors judged 55 and 43 task-irrelevant and zero-ablated them. On
  balanced data, profession accuracy goes from 61.9 to 88.5 (Pythia) and
  67.7 to 76.0 (Gemma), gender accuracy falls to 54.0 and 51.5, and after
  retraining the head profession reaches 93.1 and 95.0, at the oracle's
  93.0 and 95.0. Random ablations do nothing. The neuron skyline, given the
  balanced data, reaches 75.5 and 65.1.
- **Unsupervised circuits.** Pile contexts that Pythia-70M predicts
  confidently, with induction cases removed, are clustered (by gradients,
  activations or effects), and a circuit is found per cluster. Cluster 475
  ("to" as an infinitival object) and cluster 382 (incrementing sequences)
  each turn out to use two or more mechanisms that converge at the output
  "without fully intersecting" ([THEORY-tmpyawf9](../theory.d/THEORY-tmpyawf9.md)).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Sparse feature circuits are small and faithful compared with neuron circuits | moderate | Figure 3; feature circuits include error nodes, which are not comparable to neurons, and the first third is not scored |
| C2 | The features alone, without the error terms, carry little of the behaviour | strong for these tasks, read from Figure 3 | the "w/o SAE errors" curves |
| C3 | Pythia-70M and Gemma-2-2B do agreement across a clause by two pathways, carrying number to the clause end | moderate | annotated circuits at faithfulness 0.21 |
| C4 | Sparse features in circuits are more interpretable than neurons | moderate | crowd ratings from one community (Table 7) |
| C5 | SHIFT removes a classifier's reliance on an unintended signal without disambiguating labels | strong for this setting | Table 2, one dataset, two models |
| C6 | SHIFT finds the best features to remove "optimally or near-optimally" | weak | for Gemma the feature skyline beats it (80.8 against 76.0 profession); for Pythia SHIFT beats the "skyline" on worst group (76.0 against 62.9), so the skyline is no upper bound |
| C7 | The pipeline discovers circuits for thousands of behaviours without supervision | moderate as existence | the clusters are not evaluated, as the authors say |

## Concepts

- **Sparse feature circuit**: a subgraph of feature and error nodes, at
  token positions, with edges, selected by estimated indirect effect.
- **SAE error node**: ε(x) = x − x̂ at a site, kept as a node; dense and
  "not yet captured by our SAEs", so not interpretable.
- **Attribution patching / integrated gradients**: linear estimates of an
  indirect effect from one gradient, or an average over ten.
- **SHIFT**: inspect a classifier's feature circuit, ablate features
  judged task-irrelevant, optionally retrain the head.
- **NP number tracker**: a Gemma feature active on all tokens of a noun
  phrase whose head has a given number.

## Connections

It builds on Bricken et al. ([LIT-tmpn9ui7](../literature.d/LIT-tmpn9ui7.md)) for the autoencoders and on
causal mediation in interpretability (Vig et al., Finlayson et al.), with
attribution patching (Nanda; Syed et al.; Kramár et al., [LIT-tmp4de8g](../literature.d/LIT-tmp4de8g.md)) and integrated
gradients (Sundararajan et al.; Hanna et al.). Gemma Scope is [LIT-611](../literature.d/LIT-611.md). Its
behaviour clusters follow Michaud et al.'s quantization model. Its last
author leads MIB ([LIT-tmprlq7z](../literature.d/LIT-tmprlq7z.md)), whose circuit track scores the same family
of attribution methods, and the record's crosscoder reading ([LIT-tmpuuwok](../literature.d/LIT-tmpuuwok.md),
[NOTE-tmpq065x](NOTE-tmpq065x.md)) takes its indirect effects from this paper. Templeton et
al. ([LIT-tmp8w8uj](../literature.d/LIT-tmp8w8uj.md)) cite it as the next step after features. Its
successor and induction features recover at feature level the heads of
Olsson et al. ([LIT-tmpe7b5o](../literature.d/LIT-tmpe7b5o.md)). Transcoders ([LIT-tmptgo43](../literature.d/LIT-tmptgo43.md)) cite its error
nodes as an addition they do not use, and Circuit Tracing ([LIT-tmpsuo6l](../literature.d/LIT-tmpsuo6l.md))
builds them into its replacement model.

## Bearing on the record

- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** The paper gives the claim's point a number in a
  network. The features recovered without the task are not enough to
  carry it: with the error terms removed, the agreement circuits recover
  little, and the authors' own method keeps the unexplained remainder as a
  node so that faithfulness is not lost. And what carries agreement is not
  a feature but an arrangement: features for number, boundaries of the
  distractor clause, and verb forms, connected across positions. That is
  the claim's "organized relationship among them" in a transformer, found
  by interventions, not read off a feature.
- **[THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md).** MIB's finding that SAE features localize supplied
  variables worse than neurons, and this paper's that feature circuits are
  smaller than neuron circuits, are compatible: these feature circuits
  include error nodes that are dense, high-dimensional and not neurons, and
  without them the comparison is not made. The paper says the two cannot
  "fairly be compared".
- **[THEORY-tmpt45mh](../theory.d/THEORY-tmpt45mh.md) and [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** The crosscoder study of
  subject–verb agreement across checkpoints uses this paper's indirect
  effects on the same task. The two-pathway circuit here, read in one
  finished model, is what a developmental study would track: the question
  is when the clause-boundary pathway forms relative to the direct one.
- **[THEORY-tmp8cat0](../theory.d/THEORY-tmp8cat0.md) and [THEORY-tmpvqsx2](../theory.d/THEORY-tmpvqsx2.md).** The cluster circuits find
  succession and narrow induction features composing to predict "4" after
  "Chapter 3 … Chapter": an induction mechanism split into token-specific
  features, where Olsson et al. had heads.
- **[THEORY-802](../theory.d/THEORY-802.md).** The circuits are found by effects on one metric over one
  family of contrasts. Alignments related by a change of basis within a
  site would score the same, and the paper does not test uniqueness.
- **SHIFT** is a method for ML practice, which the anthology holds; the
  record keeps only what it shows about features (that a human can sort a
  classifier's circuit features into task-relevant and spurious ones, and
  that removing the latter works here).

## Limitations

- **The first third is not scored.** Faithfulness and completeness are on
  the latter two thirds of each circuit.
- **Error nodes.** Feature circuits are only faithful with error nodes,
  whose content is unknown; the residual-stream errors carry the most.
- **Annotation is the authors'.** Circuit labels, and the SHIFT judgement
  of which features are task-irrelevant, are made by the authors.
- **Small models and one task family** for the faithfulness study;
  Pythia-70M only for the unsupervised clusters, which are not evaluated.
- **Rating pool.** Crowdworkers from one alignment community, as the
  authors note.
- **Inconsistencies.** SHIFT expands to "Sparse Human-Interpretable
  Feature Trimming" in §1 and "Spurious Human-interpretable Feature
  Trimming" in §4. Gemma Scope's width is given as 8 × d in §2 but is
  16,384 in Appendix B.2; Gemma-2-2B's residual width is 2,304, so 8 × d
  would be 18,432 (checked here). The Gemma neuron figure of 50,000 lies
  beyond Figure 3's plotted range. Figure 9's caption, for the
  prepositional phrase, speaks of "the last token of the RC". §4 says that
  for Gemma "the feature ablations damage model performance", while
  Table 2 shows its balanced profession accuracy rising from 67.7 to 76.0
  on ablation; the damage meant is presumably on the ambiguous set, which
  the table does not report. Appendix E.1 chose Gemma's probe layer using
  the balanced set, which the authors flag; Appendix E.2 calls CBP
  "Concept Bottleneck Proving".

## Open questions

- What is in the residual-stream error terms that the agreement circuits
  need? Is it features the dictionary missed, or something no sparse
  dictionary at this width holds?
- Do the two agreement pathways form at different times in training?
- Would circuits found with one contrast family survive interventions
  from another, as MIB's counterfactual design would require?
