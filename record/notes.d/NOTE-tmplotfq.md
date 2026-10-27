---
status: Read
paper: LIT-tmpf4hwb
title: 'Wang, Hu, Du, Cheng, Wang and Zou — Fine-tuning mechanisms of LLMs via circuit analysis'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Read in full from the arXiv copy (arXiv:2502.11812v2, 13 June 2025,
    fetched from arxiv.org/pdf/2502.11812 on 2026-10-26), text extracted
    with pdftotext. Its footer reads "Proceedings of the 42nd International
    Conference on Machine Learning, Vancouver, Canada. PMLR 267, 2025". v1
    was not compared. Read: §§1–7 and Appendices A–N. The figures (circuit
    diagrams, accuracy, faithfulness, robustness and change-rate plots)
    were read from captions and text; their plotted values were not seen.
    The gain of CircuitLoRA over LoRA was recomputed from Tables 1 and 4,
    and a null model for the node–edge comparison was simulated by the
    record (THEORY-tmpoirdq).
date: '2026-10-26'
summary: >-
  When Pythia-1.4B is fine-tuned with LoRA on arithmetic tasks it starts
  out failing, EAP-IG circuits of 5% of edges found at successive
  checkpoints keep most of their nodes and change most of their edges
  (change rates 15–24% for nodes, 66–80% for edges), mostly in the middle
  layers; giving higher LoRA rank to the layers whose edges change most
  beats uniform and random rank allocation at similar size, and the union
  of two subtasks' circuits approximates a two-step task's circuit. The
  node–edge contrast carries no comparison against a null.
---
<!-- inactive-ok-file: CLAIM-367 CLAIM-329 CLAIM-tmpwr001 THEORY-tmpoirdq — Proposed; the claims and the account this reading bears on, cited as open -->

# NOTE-tmplotfq: Wang, Hu, Du, Cheng, Wang and Zou — Fine-tuning mechanisms of LLMs via circuit analysis

## Contribution

Earlier circuit studies of fine-tuning (Prakash et al. 2024, Chhabra et
al. 2024) used tasks the pretrained model already did well, and found
fine-tuning enhancing an existing circuit, for instance by adding heads.
This paper builds five arithmetic tasks on which the pretrained models
start poor and improve greatly, tracks EAP-IG circuits across eleven
checkpoints, and reports that the circuits' node sets stay largely the
same while their edge sets change a great deal. It then turns that into a
rank-allocation rule for LoRA, and tests whether two subtasks' circuits
combine into a compositional task's.

## Key insight

Fine-tuning that teaches a model something it could not do may work by
reconnecting components it already has rather than recruiting new ones:
"fine-tuning primarily modifying edges rather than merely introducing new
components to form new circuits".

## Assumptions

- **Models.** Pythia-1.4B-deduped for the main analysis; GPT-Neo-2.7B and
  OPT-6.7B for Add/Sub(100) only (Appendix H).
- **Fine-tuning.** LoRA mainly, at ranks 2–32; full fine-tuning, AdaLoRA
  and IA3 in comparisons. Batch 8 with accumulation 4, 2–4 epochs, a
  learning rate per task and rank (Appendix A).
- **Circuits.** EAP-IG with m = 5 interpolation steps and a corrupted input
  per task (the operator changed, an operand changed, one sequence term
  changed). A circuit is the top 5% of edges. Faithfulness is
  1 − |F(M) − F(C)|/F(M), with F measured by KL divergence. 80% of each
  dataset trains, 20% is held out for circuits and accuracy.
- **Change.** ΔS = (1/n) Σ_t Δs_{t→t+1}/S₀, the average count of nodes (or
  edges) changing between consecutive checkpoints relative to the initial
  circuit's count. For the before–after comparison of §4.3, edges above
  the 95th percentile of scores in the initial and final circuits.

## Key results

- **Faithfulness and robustness** (§4.1). Circuits exceed 80%
  faithfulness at every checkpoint except Add/Sub before fine-tuning
  (77.52%). Under data perturbations of 10–90%, edge Jaccard similarity is
  higher for the pretrained and fine-tuned models than for a randomly
  initialized one.
- **Convergence** (§4.2). Node and edge changes between consecutive
  checkpoints decrease as accuracy rises.
- **Edges change more than nodes** (§4.2, Table 5). Node and edge change
  rates: Add/Sub(100) 17.4% and 69.5%, Mul/Div 23.2% and 76.9%, Sequence
  24.2% and 67.9%, LCM 23.9% and 80.4%, Function 15.4% and 65.8%. The
  ratio is 2.8 to 4.3; the text says "a factor of 2–3" in §4.2 and
  "approximately 2–4×" in Appendix K. The same holds under AdaLoRA, IA3 and
  full fine-tuning, and for the two larger models, which change more.
- **Where** (§4.3). Added nodes are mostly in the middle and later layers,
  added and deleted edges in the middle layers; shallow layers change
  least.
- **CircuitLoRA** (§5, Tables 1, 4, 6). Five "critical layers" with the
  largest aggregate edge-score change get rank r_c, the rest r_o. At
  similar parameter counts it beats LoRA and RandomLoRA (five random
  critical layers) in every column of Tables 1 and 4, and AdaLoRA at a
  smaller budget (Table 6). The abstract's "average performance
  improvement of 2.46% over standard LoRA" was not reproduced from the
  tables: over Table 1 the two configurations average 2.35 points (3.42
  and 1.27), and over Tables 1 and 4 together 1.84.
- **Union circuits** (§6, Tables 2, 3, 7). On two-step tasks like
  "(61 − 45) * 45 =", the union of the Add/Sub and Mul/Div circuits shares
  more top-k edges with the compositional task's circuit (69, 259, 470 at
  k = 100, 500, 1000) than Add/Sub does with Mul/Div or Sequence. At 5% of
  edges the union recovers 89.2% faithfulness. Using it for CircuitLoRA
  gives 65.5% against the compositional circuit's 67.2% and LoRA's
  59.6–64.7%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Circuits with high faithfulness exist in the pretrained model on tasks it fails | moderate | Fig. 2; faithfulness is relative to the model's own performance, so a circuit can be faithful to a failing model |
| C2 | Circuits converge as fine-tuning proceeds | moderate | decreasing change counts, Fig. 3 and Appendix D |
| C3 | Fine-tuning changes edges more than nodes, so it forms new circuits by reorganizing connections | weak for the inference, strong for the counts | Table 5; no null comparison at the same edge budget (see Limitations and [THEORY-tmpoirdq](../theory.d/THEORY-tmpoirdq.md)) |
| C4 | Allocating LoRA rank by circuit edge change improves accuracy at similar size | moderate | Tables 1, 4, 6, means of five seeds, no variances reported; CircuitLoRA's learning rates for critical layers differ from the baselines' |
| C5 | The union of subtask circuits approximates the compositional circuit | moderate | Tables 2, 3, 7; one compositional task family |

## Concepts

- **Circuit**: the top 5% of edges by EAP-IG score, with their endpoint
  nodes.
- **Robustness**: edge Jaccard similarity between a circuit and the
  circuit found on a perturbed dataset.
- **Change rate ΔS**: defined above.
- **Critical layers**: the five layers with the largest aggregate
  edge-score change between the circuits before and after fine-tuning.
- **Union circuit**: the edge union of subtask circuits, at matched edge
  count.

## Connections

It contrasts itself with Prakash et al. (2024) on entity tracking and
Chhabra et al. (2024) on IOI (the task of [LIT-tmpj9tel](../literature.d/LIT-tmpj9tel.md)), where fine-tuning on tasks already done
well enhanced existing mechanisms, and with Jain et al. (2024) on
procedurally defined tasks. It uses Hanna et al.'s EAP-IG, which descends from attribution patching
([LIT-tmp4de8g](../literature.d/LIT-tmp4de8g.md)) and ACDC ([LIT-tmpoku9b](../literature.d/LIT-tmpoku9b.md)), and builds on
LoRA, AdaLoRA and IA3. The Mechanistic Interpretability Benchmark
([LIT-tmprlq7z](../literature.d/LIT-tmprlq7z.md)) independently ranks EAP-IG first among circuit localization
methods.

## Bearing on the record

- **The identification.** The exchange's sentence is "recent work on
  fine-tuning finds that circuit connectivity can change substantially
  even when the components involved remain similar" (T24, §1, with no
  citation). The abstract says "while circuits maintain high node
  similarity before and after fine-tuning, their edges undergo
  significant changes", against prior work "that show circuits only add
  some additional components after fine-tuning". Every clause matches, and
  the work it contrasts itself with (Prakash et al., Chhabra et al.) found
  the opposite, so neither is the cited work. The identification holds as
  far as one sentence can fix one paper.
- **[QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md).** The exchange read this as the network analogue of
  members reorganizing into new perspectives. It bears on that more
  weakly than the exchange suggested. It is about fine-tuning a pretrained
  model on narrow arithmetic, not development from initialization. Its
  "components" are whole heads and MLPs, and its "edges" are attribution
  scores above a percentile, so a changed edge is a change in which
  connections clear a threshold, not a measured change in what flows. And
  the node–edge contrast is what a fixed edge budget produces even without
  reorganization ([THEORY-tmpoirdq](../theory.d/THEORY-tmpoirdq.md)). What the question can take from it is
  a design point: a claim that relations reorganize while components stay
  must be measured against a null at the same budget.
- **[CLAIM-367](../claims.d/CLAIM-367.md).** The paper finds the LoRA layers that matter by circuit
  change, so its rank allocation is a condition of training placed by the
  analyst according to what the network's circuits did. That fits the
  claim's point that conditions of training belong to the network,
  optimizer and data together.
- **[CLAIM-329](../claims.d/CLAIM-329.md).** Whether a fine-tuned circuit with the same nodes is "the
  same" circuit is the continuity question the claim answers by causal
  transmission. The paper decides it by overlap of node and edge sets,
  which is resemblance.
- **[CLAIM-tmpwr001](../claims.d/CLAIM-tmpwr001.md).** Nodes kept with edges changed is a network case of
  constituents kept while their organization changes, but only if the
  edge changes are shown to exceed what thresholding alone produces.
- CircuitLoRA is an instruction for machine-learning practice and is the
  anthology's; this work carries the anthology-candidate flag.

## Limitations

- **No null for C3.** With a circuit defined as a fixed fraction of a
  dense graph's edges, edge sets can change while node sets barely do,
  even if only edge-level noise changes. The paper's robustness analysis
  shows circuits are stable under data perturbation, which bounds noise,
  but it does not compare fine-tuning's edge change against seed-to-seed
  or resampling change at the same budget.
- **Faithfulness on failing models.** A circuit faithful to a model that
  fails the task reproduces the failure.
- **CircuitLoRA's controls.** The critical layers get their own learning
  rates (Appendix A), which RandomLoRA is not reported to share; means of
  five seeds without variances; the headline 2.46% is not recoverable
  from the tables.
- **One model for most results.** The cross-model comparison is one task.
- **Figures** were not seen as images, so the plotted robustness and
  faithfulness values are taken from the text.

## Open questions

- Does fine-tuning's edge change exceed what retraining from a different
  seed, or resampling the circuit data, produces at the same edge budget?
- Do the kept nodes do the same thing after fine-tuning? Node identity is
  not node function.
