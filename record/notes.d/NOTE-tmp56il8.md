---
status: Read
paper: LIT-tmprlq7z
title: 'Mueller, Geiger, Wiegreffe, Arad et al. — MIB, a mechanistic interpretability benchmark'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full from the arXiv copy (arXiv:2504.13151v2, 9 June 2025,
    fetched from arxiv.org/pdf/2504.13151 on 2026-10-26), text extracted
    with pdftotext. Its footer reads "Proceedings of the 42nd International
    Conference on Machine Learning, Vancouver, Canada. PMLR 267, 2025". v1
    was not compared. Read: §§1–6, Appendices B (limitations), C (tasks,
    counterfactuals, model accuracy), D (circuit methods and Tables
    14–17), E (InterpBench training) and F (causal abstraction, the
    featurizers, DAS, hyperparameters, and each task's causal model with
    Table 18). The leaderboard screenshots (Figs. 5–6) and the per-layer
    heat maps of Appendix F were read from captions only. The causal
    variable track's Table 3 was tabulated by the record
    (THEORY-tmp4lqc8).
date: '2026-10-26'
summary: >-
  A benchmark for two kinds of mechanistic-interpretability method, with
  fixed counterfactual inputs, private test sets and new metrics. In
  circuit localization, edge attribution patching with integrated
  gradients does best on average and node-level circuits poorly; in
  causal-variable localization, supervised distributed alignment search
  gives the highest interchange-intervention accuracy, and features of
  public sparse autoencoders selected by a learned mask never beat the
  same mask on the model's own hidden dimensions.
---
<!-- inactive-ok-file: CLAIM-tmpwr001 THEORY-802 CLAIM-278 CLAIM-427 — Proposed; the claims and readings this bears on, cited as open -->

# NOTE-tmp56il8: Mueller, Geiger, Wiegreffe, Arad et al. — MIB, a mechanistic interpretability benchmark

## Contribution

It fixes what comparing interpretability methods means for two tasks the
field calls localization. One is finding the subgraph of model components
that carries a behaviour (circuit localization). The other is finding the
features of a hidden vector that carry a variable of a hypothesized causal
model (causal-variable localization). For each it fixes the
counterfactual inputs, metrics that do not depend on a circuit-size
threshold, public and private test splits, and baselines. Its two findings
are that integrated-gradient attribution beats exact activation patching
and mask learning on average, and that sparse-autoencoder features are no
better units for a known causal variable than neurons.

## Key insight

A localization claim is only as good as the counterfactuals and the unit
of analysis it is evaluated with, and both have to be held fixed before
methods can be compared. Held fixed, a popular unsupervised feature
basis, the SAE's, does not localize task variables better than the
coordinates the model already has. The method that does best is the one
supervised by the hypothesis it is evaluated against.

## Assumptions

- **Models.** Llama-3.1 8B, Gemma-2 2B, Qwen-2.5 0.5B and GPT-2 Small,
  plus an InterpBench model (6 layers, 4 heads, d_model = 64) trained with
  SIIT to implement a known simplified IOI circuit.
- **Tasks.** IOI, two-operand Arithmetic, a synthetic colour MCQA (260
  instances), and ARC Easy and Challenge. The causal-variable track adds
  RAVEL. Not every model is run on every task.
- **Circuits.** Nodes are submodules or heads, edges are information flow
  between them; a neuron counts as 1/d_model of its node's outgoing edges.
  Faithfulness f(C) = (m(C) − m(∅))/(m(N) − m(∅)) with m the logit
  difference between the original and counterfactual answers.
- **Causal variables.** A high-level causal model H is supplied for each
  task. A featurizer F maps a hidden vector to features, and a submission
  aligns a variable X with features Π_X at a chosen location. Evaluation
  is interchange-intervention accuracy (IIA): the share of base–
  counterfactual pairs on which intervening on Π_X in the LM and on X in H
  give the same output (for IOI, a mean squared error on logits). Examples
  the model gets wrong are filtered out.

## Key results

- **Two circuit metrics.** CPR, the area under the faithfulness curve over
  circuit sizes k ∈ {0.001, …, 1} (higher better), rewards components that
  help. CMD, the area between that curve and 1 (0 best), rewards any
  component with a strong effect. InterpBench gives an edge AUROC against
  the known circuit.
- **Circuit localization** (Table 2, CMD; Table 14, CPR).
  - EAP-IG-inputs with counterfactual ablations "achieves the highest
    performance on average on both CMD and CPR". EAP-IG-activations, EAP
    and UGS are competitive on CMD.
  - Counterfactual ablations beat mean and optimal ablations.
  - Node-level circuits do poorly, "because each node included 'costs'
    many edges".
  - Exact edge activation patching (EActP) dominates only IOI on GPT-2, and
    on InterpBench its AUROC is 0.28, below the random circuits' 0.44. The
    best InterpBench AUROC is EAP-IG-activations' 0.81.
- **Causal-variable localization** (Table 3). Five featurizers: the full
  vector, DBM (a learned binary mask) over the model's own dimensions, DBM
  over PCA components, DBM over SAE features (Gemma Scope, Llama Scope),
  and DAS, a learned orthogonal subspace trained on the IIA objective.
  - "DAS consistently achieves the best results." "DBM on standard hidden
    dimensions is a strong baseline." "DBM on PCA or SAE features does not
    outperform DBM on standard dimensions."
  - Tabulated here over the sixteen task–variable–model cells that have an
    SAE row: SAE features had lower mean IIA than neurons in all sixteen,
    by 1 to 14 points (mean 6.9), and DAS had the highest mean in fifteen.
    The exception is Gemma-2's carry variable, where every method is near
    chance.
  - Carry-the-one is not localized: Gemma-2 at chance, Llama-3.1 with
    "only faint signs of success". In Appendix F.5.2 the apparent carry
    signal at the last token, under counterfactuals that change only the
    carry, "is likely a representation of the tens-digit output, which
    perfectly correlates with the ones-carry variable in these
    counterfactual". With random counterfactuals, "we see a total failure".
  - IOI: the token and position signals of the S-inhibition heads can be
    disentangled at head level, and better below it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | EAP-IG-inputs with counterfactual ablations is the best circuit localization method on average | moderate | Tables 2, 14–16 over the model–task cells where it ran; the ranking varies by cell |
| C2 | Counterfactual ablations localize better than mean or optimal ablations | moderate | Table 2; the authors attribute it to matching the evaluation setting |
| C3 | Exact activation patching is not the best method despite computing exact indirect effects | moderate | Table 2; run on fewer examples for cost, which the authors note may explain part of it |
| C4 | Supervised DAS gives the best causal-variable alignments | strong, for these tasks | Table 3; DAS optimizes the evaluation objective on training pairs, evaluated on held-out ones |
| C5 | SAE features are not better units than neurons for localizing known causal variables | strong, for the tested SAEs, sites and tasks | Table 3, all sixteen cells ([THEORY-tmp4lqc8](../theory.d/THEORY-tmp4lqc8.md)) |
| C6 | Non-basis-aligned directions are generally better units than neurons | moderate | DAS beats DBM over neurons, but DAS is also supervised and DBM is a mask, so unit and supervision are confounded |
| C7 | MIB shows there has been "real progress" in mechanistic interpretability | weak | inferred from methods separating from random and from each other |

## Concepts

- **Circuit localization**: finding a subgraph of the computation graph
  that carries a task behaviour.
- **Causal-variable localization**: finding features Π_X of a hidden
  vector that play the role of variable X in a high-level causal model.
- **Featurizer**: an invertible map F from a hidden vector to a feature
  space; SAE featurizers keep the base input's reconstruction error to be
  invertible.
- **Interchange intervention**: run the base input with a variable (or
  features) fixed to its value on a counterfactual input.
- **CPR, CMD**: integrated circuit performance ratio and integrated
  circuit–model distance, defined above.

## Connections

It builds on causal abstraction (Geiger et al. 2021, 2024), on activation
patching and attribution patching (Vig et al.; Nanda; Syed et al.), on
EAP-IG (Hanna et al. 2024), on Li and Janson's optimal ablations and UGS,
on InterpBench (Gupta et al. 2024) and on RAVEL (Huang et al. 2024). Its
SAE finding agrees with AxBench, where SAEs "struggle against simple
steering baselines". The record holds the neighbouring work on
interchange interventions: Makelov et al. ([LIT-968](../literature.d/LIT-968.md)), Wu et al.'s reply
([LIT-961](../literature.d/LIT-961.md)), and [LIT-987](../literature.d/LIT-987.md). Read since, on 2026-10-26: the paper that
introduced DAS (Geiger et al., [LIT-tmpsavwt](../literature.d/LIT-tmpsavwt.md)); attribution patching,
through Kramár et al.'s AtP* ([LIT-tmp4de8g](../literature.d/LIT-tmp4de8g.md)); ACDC ([LIT-tmpoku9b](../literature.d/LIT-tmpoku9b.md)), a
circuit-discovery method of the family the circuit track scores; and
Wang et al.'s IOI circuit ([LIT-tmpj9tel](../literature.d/LIT-tmpj9tel.md)), from which the IOI tasks and
the InterpBench model's circuit come.

## Bearing on the record

- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** Two of MIB's results are the claim's point in
  networks. A feature recovered without the causal hypothesis, an SAE
  feature, did not carry the task variable better than raw coordinates did.
  And the carry-the-one case shows a representation that tracks the
  variable under one family of counterfactuals (it is the output digit,
  correlated with the carry there) and fails under another. Whether a
  recovered feature is the variable that does the work depends on
  interventions that separate it from what it is correlated with. That is
  a supporting case in a new setting, not a test of the claim about
  perspectives.
- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** The exchange cited MIB as "a useful warning", and
  the reading bears it out with two qualifications. The warning is about
  SAE features on residual streams of two pretrained models, selected by
  a mask, for variables supplied in advance; it is not about dictionaries
  in general, and not about features tracked across training. And the
  method that wins, DAS, is supervised by the very causal model it is
  scored against. A coupled feature–circuit model fitted to checkpoints
  would have to be scored by interventions it was not fitted to, which is
  [CLAIM-427](../claims.d/CLAIM-427.md)'s third grade and [CLAIM-278](../claims.d/CLAIM-278.md)'s caution.
- **[THEORY-802](../theory.d/THEORY-802.md) and [THEORY-243](../theory.d/THEORY-243.md).** MIB scores an alignment by IIA alone. Two
  alignments that tie on every interchange intervention, the case
  [THEORY-243](../theory.d/THEORY-243.md) proves in a constructed network, would score identically, so MIB
  cannot see the non-uniqueness [THEORY-802](../theory.d/THEORY-802.md) asserts and does not claim to.
  Its DAS subspaces are learned orthogonal directions of up to half the
  residual stream (for the answer-token variables), and the full vector
  reaches 100% best-layer IIA in four cells: a large enough subspace passes
  interchange tests without isolating anything. The averages over layers,
  not the best-layer figures, carry the comparison.
- **[THEORY-504](../theory.d/THEORY-504.md).** Gemma Scope's residual-stream SAEs cost more next-token
  loss than MLP or attention ones. MIB's SAE comparisons are on residual
  streams, the site [THEORY-504](../theory.d/THEORY-504.md) found worst by loss, and the SAE
  interventions carry the base input's reconstruction error. Both may
  depress SAE scores. MIB does not test other sites.
- The leaderboards and method rankings are guidance for interpretability
  practice, which is the anthology's; nothing is drawn here as an
  instruction.

## Limitations

- **The authors'.** The two tracks separate featurization from circuit
  finding, which interact. Completeness cannot be measured without ground
  truth except on InterpBench. The causal-variable paradigm "presumes the
  existence of the high-level model in the computation graph". Language
  models only. No exhaustive hyperparameter searches for baselines.
- **Coverage.** SAEs only for Gemma-2 and Llama-3.1; Arithmetic only on
  Llama-3.1 in the circuit track; IOI causal variables only on GPT-2's
  four S-inhibition heads; EActP, optimal ablations and UGS only where
  tractable. MCQA has about 100 training examples, and PCA does badly
  there for that reason, the authors suspect.
- **Supervision and unit confounded.** DAS differs from DBM-over-neurons
  in both the unit (rotated directions) and the training signal, so C6
  does not isolate the unit.
- **Counts.** The abstract's "four tasks and five models" counts four
  language models plus InterpBench, and RAVEL is a fifth task in the
  causal-variable track.

## Open questions

- Do SAE features localize task variables better at MLP or attention
  outputs, or with selection other than a binary mask?
- Is there a carry-the-one variable in these models, perhaps nonlinear?
- How would a featurizer learned without supervision from H, but scored by
  MIB, compare with DAS trained on a different counterfactual family?
