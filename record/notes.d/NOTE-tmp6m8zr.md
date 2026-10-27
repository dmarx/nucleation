---
status: Read
paper: LIT-tmpoku9b
title: 'Conmy, Mavor-Parker, Lynch, Heimersheim and Garriga-Alonso — Towards automated circuit discovery (ACDC)'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full on 2026-10-26 from the arXiv PDF, 2304.14997v4 (28 October
    2023, the NeurIPS 2023 version; 35 pages), text extracted with
    pdftotext. Read: §§1–6, Appendices B–N (impact statement, metrics,
    subnetwork probing and HISP, the design-choice experiments with Tables
    2–3, the IOI, Greater-Than, Docstring, tracr, induction and gendered
    pronoun appendices, the reset-network experiments, OR gates, and the
    connection to causal scrubbing) and the references. The ROC curves,
    circuit diagrams and KL-against-edges plots were read from their
    captions and the text; the AUCs are from Tables 2 and 3. Earlier
    arXiv versions were not compared.
date: '2026-10-26'
summary: >-
  Names a three-step workflow behind manual circuit discovery (choose a
  behaviour, metric and dataset; choose the units of the computational
  graph; patch activations to prune the graph) and automates the third
  with ACDC, which visits nodes from the output back and removes each
  incoming edge whose replacement by its value on a corrupted input raises
  the KL divergence from the full model by less than a threshold. Against
  circuits reported by earlier manual work it ranks edges with AUCs of
  0.85–0.98 on three language-model tasks, beating two adapted pruning
  methods there, but does poorly on compiled tracr programs unless zero
  activations are used, misses negative components at sparse thresholds,
  and keeps only one input of an OR gate.
---
<!-- inactive-ok-file: THEORY-802 THEORY-tmpoirdq THEORY-tmpkd3fq THEORY-tmp1dufu — Proposed; accounts this reading bears on, cited as open -->

# NOTE-tmp6m8zr: Conmy, Mavor-Parker, Lynch, Heimersheim and Garriga-Alonso — Towards automated circuit discovery (ACDC)

## Contribution

It makes "finding the circuit" an algorithm with a threshold, and gives
the first quantitative comparison of circuit-finding methods against
circuits that people had found by hand. Before it, the subgraph in an IOI
or Greater-Than paper was the product of weeks of patching experiments;
after it, a comparable subgraph comes out of one run, and the question of
how good such a subgraph is has a number (an AUC against the reported
circuit, or KL divergence against edge count).

## Key insight

The manual practice was already a greedy search: start at the output,
patch each incoming connection, keep the ones that matter, recurse. Run
that search exhaustively over edges of a fixed computational graph,
with one fixed criterion (KL divergence to the full model's output), and
it becomes reproducible. The price is that every judgment the human made
along the way, about units, metric, corrupted inputs and order, becomes a
hyperparameter, and the paper finds the results sensitive to all of them.

## Assumptions

- **A task** is a set of prompts x_i on which the behaviour shows and a
  matched set x′_i on which it does not; activations on x′_i are the
  corrupted values. A subgraph H is evaluated by running the model on x_i
  with every edge not in H set to its value on x′_i (interchange
  intervention, following causal scrubbing, [LIT-tmpqtkua](../literature.d/LIT-tmpqtkua.md)).
- **The computational graph** is chosen in advance: heads split into
  query, key and value inputs, and MLPs, with edges between any earlier
  and later component through the residual stream; token positions are
  merged except in the gendered-pronoun study. GPT-2 Small's graph has
  about 32,000 edges (32,923 in Figure 15's caption).
- **ACDC (Algorithm 1).** Sort nodes from output to input; for each
  parent edge w → v, remove it if D_KL(G‖H_new) − D_KL(G‖H) < τ. The order
  of parents is a hyperparameter, lexicographic from later to earlier
  layers and from higher to lower head index, and "in one case … the
  order of the parents affected experimental results" (induction,
  Appendix J).
- **Baselines.** Subnetwork probing (Cao et al.) without its probe, with
  the same metric and a mask that interpolates between clean and
  corrupted activations; and head importance scores for pruning (Michel
  et al.), generalized to corrupted activations, which the authors note is
  attribution patching (Nanda 2023) up to the absolute value.
- **Ground truth** is the circuit reported by earlier work, rebuilt at the
  edge level by the authors (IOI 1,041 edges; Greater-Than 262; Docstring
  37; tracr 10 and 15). The authors call it "not 100% reliable": the IOI
  circuit gets a logit difference of 3.24 against the model's 4.11 (KL
  0.44), and the Greater-Than circuit a probability difference of 72%
  against 84% (KL 0.078).

## Key results

- **Recovery of reported circuits (§4.1, Figure 3, Table 2).** With
  corrupted activations and KL divergence, edge AUCs for ACDC, HISP and
  SP: Docstring 0.982, 0.805, 0.937; Greater-Than 0.853, 0.693, 0.806;
  IOI 0.869, 0.789, 0.823. ACDC is highest on all three. On the tracr
  programs (an L2 metric) ACDC scores 0.679 and 0.200 with corrupted
  activations and 1.000 on both with zero activations (Table 3), where
  the circuit "was perfectly recovered by ACDC at any threshold τ > 0".
- **Sensitivity (§4.1, Appendix E).** Optimizing the task metric instead
  of KL makes ACDC better on Docstring and worse on Greater-Than and IOI
  (edge AUC 0.461 and 0.589 with the loss metric); "it is not a very
  robust method". Zero activations gave lower KL on induction for all
  methods and far worse results on Docstring.
- **Abstract's headline (Appendix G).** On Greater-Than, a run with the
  probability-difference metric and τ = 0.01585 kept 68 of about 32,000
  edges, all in the reported circuit, recovering its five component types.
- **IOI (Figure 1, Appendix F).** At τ = 0.0575 ACDC returns nine heads,
  all in the 26-head IOI circuit, from three of its classes, in 8 minutes
  on an A100. It omits the negative name movers and previous-token heads;
  a run at τ = 0.00398 keeps 443 of 32,923 edges and finds the negative
  heads together with many heads the IOI work did not report.
- **Docstring (Appendix H, Table 4).** At τ = 0.095 ACDC keeps 34 edges
  (KL 1.2) against the rebuilt 37-edge manual circuit (KL 1.1); it finds
  head 1.0, which the original authors added later, and misses head 1.2.
- **Induction (§4.2, Appendix J).** On a two-layer attention-only model
  (305 edges), above about 20 edges every point on the KL-against-edges
  Pareto frontier is an ACDC run; at τ = 0.5623 it finds the two
  induction heads (1.5, 1.6) and the previous-token head (0.0).
- **Reset networks (Appendix L).** All methods reach lower KL on the
  trained network than on one with permuted weights, but HISP and SP with
  zero activations, and SP somewhat with corrupted activations, can also
  fit the reset network, "evidence against Q2" (that they avoid
  components that do not take part).
- **OR gates (Appendix M).** In a one-layer toy where an MLP computes
  1 − ReLU(1 − x − y) from two heads that each output 1, ACDC keeps only
  one input, because it prunes the first input it visits and then needs
  the second; HISP keeps neither; SP keeps one and extra nodes.
- **Relation to causal scrubbing (Appendix N).** ACDC searches the narrow
  class of causal-scrubbing hypotheses in which each path either matters
  or is resampled from one corrupted datum.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Manual circuit discovery follows a three-step workflow whose patching step can be automated | interpretive | §2, with five earlier studies |
| C2 | With corrupted activations and KL, ACDC ranks reported edges better than HISP and SP on IOI, Greater-Than and Docstring | strong for these three tasks and these baselines | Table 2 |
| C3 | ACDC recovers the tracr circuits exactly with zero activations and poorly with corrupted ones | strong for two small programs | Tables 2–3, Figures 9–10, 21 |
| C4 | Results are sensitive to the metric, the kind of ablation and the parent order | strong | Appendix E, J |
| C5 | Methods optimizing one metric miss negative components at sparse thresholds | moderate | §4.1, Appendix F.3 |
| C6 | Greedy edge pruning keeps only one input of an OR gate | demonstrated in a toy ([THEORY-tmp1bwxc](../theory.d/THEORY-tmp1bwxc.md)) | Appendix M |
| C7 | ACDC can help new interpretability work (gendered pronouns) | anecdotal | Appendix K |

## Concepts

- **Corrupted activations**: activations on a matched prompt without the
  behaviour, patched into every edge outside the candidate circuit.
- **Edge AUC**: the area under the ROC curve for classifying edges as in or
  out of the reported circuit, over a sweep of τ (or λ, or k).
- **Reset network**: the model with each layer's Q, K, V head dimensions
  and MLP biases permuted, a control that should have no circuit to find.
- **Negative component**: a head whose output lowers the task metric, such
  as IOI's negative name movers.

## Connections

It is causal scrubbing ([LIT-tmpqtkua](../literature.d/LIT-tmpqtkua.md)) turned into a search, and its HISP
baseline is attribution patching, which AtP* ([LIT-tmp4de8g](../literature.d/LIT-tmp4de8g.md)) studies and
which Syed, Rager and Conmy later found to outperform ACDC. The ground
truths come from the IOI (LIT-tmpj9tel), Greater-Than and Docstring studies and from
tracr. The record's later circuit work rests on its descendants: Wang et
al.'s circuits over fine-tuning ([LIT-tmpf4hwb](../literature.d/LIT-tmpf4hwb.md), [THEORY-tmpoirdq](../theory.d/THEORY-tmpoirdq.md)) are found
with edge attribution patching with integrated gradients, and MIB
([LIT-tmprlq7z](../literature.d/LIT-tmprlq7z.md)) benchmarks that family. The induction task links it to
Olsson et al. ([LIT-tmpe7b5o](../literature.d/LIT-tmpe7b5o.md)).

## Bearing on the record

- **[THEORY-802](../theory.d/THEORY-802.md) and [QUESTION-234](../questions.d/QUESTION-234.md).** Two findings bear on "several
  distinct, fully correct" explanations. First, the OR-gate case: when
  two paths are each sufficient, greedy pruning returns one of them, and
  which one depends on visiting order ([THEORY-tmp1bwxc](../theory.d/THEORY-tmp1bwxc.md)), so the returned
  circuit is one of several sufficient subgraphs. Second, the IOI run at a
  low threshold returns many heads the manual work did not report while
  matching the model better than the manual circuit does (KL 0.44 for the
  reported circuit). Neither is a tie between basis-related alignments of
  one variable; both are underdetermination at the level of components,
  which [QUESTION-234](../questions.d/QUESTION-234.md) does not ask about.
- **[THEORY-tmpoirdq](../theory.d/THEORY-tmpoirdq.md).** That account's caution, that edge counts under a
  fixed budget can change without reorganization, has a companion here:
  which edges a pruning method keeps depends on threshold, metric and
  order, so a change in the returned circuit between checkpoints need not
  be a change in the model.
- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** ACDC is a ready circuit-only arm for checkpoints
  in small attention-only models: the paper's induction setting is the
  question's. Its sensitivity to order and ablation type means a
  developmental series would need those fixed across checkpoints.
- **[THEORY-tmp8cat0](../theory.d/THEORY-tmp8cat0.md), [THEORY-tmp1dufu](../theory.d/THEORY-tmp1dufu.md).** ACDC on the two-layer
  attention-only induction model finds the two induction heads and the
  previous-token head, the circuit those accounts follow over training,
  in a trained model only.

No instruction for machine-learning practice is recorded; which method
to use is the anthology's question (`anthology-candidate`).

## Limitations

- **Ground truth is partial.** Reported circuits are themselves
  incomplete (the IOI circuit's logit difference is 3.24 against 4.11),
  so false positives against them may be real components.
- **Not robust.** By the authors' account, results depend on metric,
  corruption distribution and parent order.
- **An internal inconsistency in §4.1.** The text says "ACDC achieves a
  greater AUC on the IOI and Greater-Than and tracr-reverse tasks than
  both of the other methods", in the paragraph that also says ACDC
  "achieved poor performance on both tracr tasks in Fig. 3". With
  corrupted activations (Figure 3, Table 2) ACDC's tracr-reverse AUC is
  0.200, below HISP's 0.577; it leads there only with zero activations
  (Table 3, 1.000).
- **Table 3's caption** reads "AUCs for corrupted activations, Zero
  Ablation"; the table is the zero-ablation one.
- **Docstring counts.** Appendix H says the circuit has "8 main heads
  (0.2, 0.4, 0.5, 1.4, 2.0, 3.0, and 3.6)", which lists seven, and calls
  the rebuilt circuit "the circuit of 39 edges" where Figure 18a and Table
  4 give 37.
- **Small evaluation.** IOI uses 50 prompts from one template;
  Greater-Than 100 prompts; induction 40 sequences.

## Open questions

- Is there a pruning rule whose output does not depend on visiting order
  when the model has redundant paths, and what would it return for an OR
  gate: both inputs, or a set of alternatives?
- How much of the gap between reported and recovered circuits is error in
  the reported circuits?
