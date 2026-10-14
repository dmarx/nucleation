---
status: Read
paper: LIT-946
title: 'Kirsanov et al. — The Geometry of Prompting'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from arXiv:2502.08009v1 (11 February 2025), text
    extracted with pdftotext: §§1–5, the limitations, and appendix A
    (dataset generation, the open datasets, models, embedding extraction,
    the definition of manifold capacity and participation ratio, the
    in-context and prompt-tuning protocols). Figures 3–26 were read from
    their captions and axis labels; curves were not read off, so the
    results below are as the text states them. The published version is in
    Findings of NAACL 2025; the arXiv v1 was the copy read.
date: '2026-10-14'
summary: >-
  In base Llama-3.1-8B (and Gemma-2-2B), demonstrations reorganise the
  geometry of the input sentence's representation at early-to-middle layers,
  while an instruction acts mainly on the last token and soft prompts only
  on late layers: matched accuracy, different mechanisms. Few-shot failures
  from the choice of examples or from relabelled categories leave the class
  manifolds separable and fail at the readout.
---
<!-- inactive-ok-file: CLAIM-029 CLAIM-118 THEORY-tmp94b56 THEORY-tmpgub9t — Proposed; the claims this reading bears on and the theories it files, open -->

# NOTE-tmpjl88t: Kirsanov et al. — The Geometry of Prompting

## Contribution

The paper measures what three ways of adapting a decoder-only model to a
classification task (an instruction, demonstrations, and a trained soft
prompt) do to the geometry of its internal representations. It uses
manifold capacity, which links linear separability of class point clouds
to their geometry. After it, there is evidence that methods of similar
accuracy act at different layers and on different tokens, and that
accuracy and representational separability can come apart.

## Key insight

Accuracy has two parts: how separable the classes are in the residual
stream, and how well the model's own unembedding reads that separation
out. Demonstrations improve the first; an instruction mostly improves the
second. When few-shot prompting fails, the first is usually intact and the
second has failed.

## Assumptions

- **Classification with a fixed label set.** Manifold capacity is defined
  for one-vs-rest dichotomies of P classes. The authors say this
  "simplif[ies] the more complex tasks" and does not reach multi-token
  outputs.
- **Capacity as defined here.** For P classes, project the points randomly
  to D_proj dimensions and find the critical dimension D* at the
  inflection of the probability that a random one-vs-rest dichotomy is
  separable; α = P / D* (App. A.3.2). Dimension is the participation ratio
  (Σλ)²/Σλ² of each class's covariance, and radius the largest pairwise
  distance; both are simplifications of Chou et al.'s (§3.5).
- **Two embeddings.** "Sentence" embeddings mean-pool the residual stream
  over the input sentence's tokens only, excluding the prompt. "Last-token"
  embeddings take the final position (§3.4).
- **Base models only.** Llama-3.1-8B, with Gemma-2-2B as replication.
  "Instruction" names only the prompt format; no model was instruction
  tuned (footnote 1).
- **One instruction template.** "This is a text classification task.
  Possible categories are …" (§3.3). Wording is not varied.
- **Synthetic data.** The main dataset is 1000 sentences written by Claude
  3.5 Sonnet, each labelled for sentiment, topic and intent (five classes
  each). Single-task results are replicated on AG News and TREC (coarse).
  Demonstrations: 1 to 40, three seeds each.

## Key results

- **Accuracy (§4.1, Fig. 3).** The instruction beats demonstrations with
  ≤5 examples; more than 5 surpass it and plateau. Letter-code labels need
  more examples. Consistently shuffled labels ("Joy" → "Anger") fail: the
  model "failed to generalize beyond pretrained associations", low on both
  the target and the original labels.
- **Sentence level (Fig. 4).** Demonstrations, "but not abstract
  instruction", raise capacity at early-to-middle layers (a peak around
  layer 12), by lowering manifold dimension and improving correlation
  structure. Gold, letter and shuffled labels give little difference:
  "sentence representation is primarily influenced by input distribution
  examples, rather than input-output mapping."
- **Last token (Fig. 5).** The instruction raises capacity over the raw
  sentence from about layer 8 on. Demonstrations raise it further, "despite
  lower task performance for cases with few examples". Letter labels give
  much lower last-token capacity; shuffled labels give capacity "similar to
  the gold label setting".
- **Sensitivity to examples (Fig. 6).** At five demonstrations, accuracy
  across samplings runs "from below 0.1 to approximately 0.6", while final-
  layer capacity barely changes, and the worst runs still exceed the
  instruction's capacity with a layer profile "nearly identical" to the
  best. So the instability "is driven primarily by poor readout alignment
  rather than differences in representational geometry".
- **Multi-task (§4.2, Figs. 7–8).** At the sentence level, demonstrations
  for a different task on the same sentences also raise capacity for the
  unprompted labels, less than for the prompted ones ("synergy"). At the
  last token, demonstrations of a different task raise capacity for the
  unprompted labels in early layers and lower it in late layers
  ("interference", a "representational trade-off"). The coherent–incoherent
  difference follows center–axes correlations, not the dimension or radius
  of single manifolds.
- **Soft prompts (§4.3, Fig. 9).** A trained 5-token soft prompt beats
  demonstrations, with no effect of length (1 to 20). It leaves early and
  middle layers unchanged (no peak near layer 12), acts at late layers,
  raises last-token capacity above the instruction and below
  demonstrations, and lowers capacity for unrelated tasks more than
  demonstrations do.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Instruction, demonstrations and soft prompts reach similar accuracy through different representational effects | moderate | §4.1, §4.3; one main model, a replication, synthetic plus two open datasets |
| C2 | Demonstrations reshape intermediate representations of the input; an instruction does not | moderate | sentence-level capacity, Fig. 4, Figs. 13–16 |
| C3 | What reshapes them is the input sentences, not the correctness of labels | moderate | little difference across gold, letter and shuffled labels, Fig. 4 |
| C4 | Few-shot instability and failure on flipped labels are readout failures, not tangled representations | moderate | Fig. 6 and the shuffled-label capacity, §4.1 |
| C5 | Prompting for one task trades away late-layer separability for others | weak | Fig. 8, center–axes correlations, Fig. 22 |
| C6 | Soft prompts work mainly by aligning representations to the readout | weak | late-layer effects, Fig. 9; argued in §5, not tested directly |

## Concepts

- **Category manifold.** The point cloud of embeddings of all sentences
  with one label.
- **Manifold capacity.** "The number of linearly decodable classes per
  dimension": P / D*, where D* is the critical projection dimension.
- **Readout alignment.** How well the model's unembedding uses the
  separability present in the last-token embedding.
- **Coherent / incoherent.** Whether the labels used to form the manifolds
  are the ones the prompt asks about.

## Connections

It uses Chung et al.'s manifold capacity (2018) and Chou et al.'s
correlated extension (2024). Its label-shuffling result echoes Min et al.
([LIT-814](../literature.d/LIT-814.md)), that correct input–label pairs matter less than the input
distribution, and Pan et al.'s split of task recognition from task
learning. Davidson et al. ([LIT-942](../literature.d/LIT-942.md), read in [NOTE-tmppb5ub](NOTE-tmppb5ub.md)) reach the
same verdict on demonstrations against instructions by a causal method.

## Bearing on the record

- **[QUESTION-024](../questions.d/QUESTION-024.md).** The LIT registered this paper as "evidence that
  prompting methods with matched performance adapt a model through
  distinct representational mechanisms. That counts against a single frame
  induced from examples." The first sentence is right. The second goes past
  the paper. It holds one instruction wording fixed and compares prompt
  *forms*; it does not vary the wording of an induced frame and ask whether
  the effect survives, which is what [QUESTION-024](../questions.d/QUESTION-024.md) asks. What it does show
  that bears on the question: demonstrations change how the input itself is
  represented, and the change comes from the example sentences, not from
  their labels (C3). That is a sense in which something is induced from
  examples rather than told.
- **The triage's reading of the pair.** The curation entry of 2026-10-14
  says this paper and [LIT-942](../literature.d/LIT-942.md) "point opposite ways on whether one induced
  frame is shared". They point the same way: neither finds a mechanism
  common to demonstrations and instructions.
- **[CLAIM-029](../claims.d/CLAIM-029.md).** Its "toward the defeater" item cites Lu et al.: order
  alone moves accuracy from near chance to near the state of the art, so
  the "frame" is sensitive to surface form. C4 here splits that finding.
  Across samplings of examples, the representation is nearly unchanged and
  the readout is what moves. If the frame is the representation the
  context sets, this paper says it is more stable than the accuracy
  suggests. Order was not varied here, only which examples were drawn, so
  it does not settle Lu et al.'s case.
- **[CLAIM-118](../claims.d/CLAIM-118.md).** The geometry–readout split is a third axis beside
  context and interpreter: a context can change what is decodable without
  changing what the model's own decoder reads.
- Files [THEORY-tmp94b56](../theory.d/THEORY-tmp94b56.md). C1–C2 are held, with
  [LIT-942](../literature.d/LIT-942.md), by [THEORY-tmpgub9t](../theory.d/THEORY-tmpgub9t.md).
- The discussion proposes geometric optimisation of prompts and trained
  linear readouts. That is practice for the anthology and is not carried
  here.

## Limitations

- **Synthetic data**, written by another language model; the open
  datasets replicate the single-task results only.
- **Base models only**, so "instruction" is a prompt format, not the
  instruction-following that post-training builds.
- **One instruction wording, three seeds**, and no statistical tests
  reported.
- **Simplified geometry.** Dimension and radius are not the anchor-point
  quantities in which capacity is analytically expressed.
- **Readout alignment is inferred, not measured.** The paper proposes, but
  does not run, the comparison of trained linear classifiers with the
  unembedding.

## Open questions

- Would a trained linear readout on the "failed" few-shot runs recover the
  accuracy, as C4 predicts?
- Does instruction tuning change where an instruction acts?
- Does the readout account cover order effects as well as example choice?
