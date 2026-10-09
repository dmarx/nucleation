---
status: Read
paper: LIT-tmp686hl
title: 'Test-Time Training for Few-Shot Learning'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read from the arXiv v2 PDF (25 Mar 2025, 22 pp.). Sections 1–7 and
    the Limitations read in full, with Table 1 and the text of Figures
    1, 5–9. The appendices (task lists, synthetic-data generation for
    fine-tuning, hyperparameters, augmented-inference details, per-task BBH
    results) were looked over, not read. The PMLR camera-ready PDF was
    fetched only to check the 61.9%/62.8% discrepancy, which it shares.
    Bar heights are taken from printed labels and the text, not estimated
    from the plots.
date: '2026-10-09'
summary: >-
  Shows that turning a task's few-shot demonstrations into a temporary
  weight update (per-task LoRA on leave-one-out in-context tasks) improves
  an 8B model over conditioning on the same demonstrations: 50.5% → 57.8%
  on BIG-Bench Hard, and large gains on ARC. The update works best when it
  is trained in the in-context format, and gains concentrate on tasks with
  structural rules or distribution shift.
---

<!-- inactive-ok-file: THEORY-tmpllqzv — Proposed; named as the neighbouring account -->

# NOTE-tmppmfwl: Test-Time Training for Few-Shot Learning

## Contribution

A systematic study of test-time training for language models in the
few-shot setting, where the test task arrives with demonstrations. It
characterises the design (how to build the training set from the
demonstrations, which loss, which parameters to update, how to infer) and
shows on ARC and BIG-Bench Hard that the update beats in-context learning
with the same demonstrations, by margins that are large where the task's
structure is novel to the model.

## Key insight

The demonstrations in a prompt can be used twice: as evidence the model
conditions on, and as a training set for a brief, discarded change to the
model. The second use extracts more from the same examples on tasks the
model cannot already do, and it extracts most when the training examples
are themselves in-context tasks, so that the update improves the model's
use of context rather than replacing it.

## Assumptions

- The test task comes with K demonstrations (2–7 for ARC, 10 for BBH)
  and no other labelled data.
- The update is LoRA (rank 64 on BBH) on a pretrained or fine-tuned
  Llama model, per task by default, discarded after the task.
- ARC models are first fine-tuned on synthetic ARC-like tasks distinct
  from those evaluated; BBH models are not.
- ARC scoring is pass@2 exact match, with augmented inference and
  hierarchical voting over invertible transformations; BBH uses greedy
  decoding.
- Hyperparameters were tuned on the same 80 ARC tasks used for ablations
  (the authors flag this).

## Key results

- **Figure 1 / §5.3 (BBH).** Zero-shot 40.9%, ICL 50.5%, TTT 57.8%;
  without demonstration permutations 55.7%; loss on the test output only
  54.4%; loss on inputs and outputs 55.9%; direct I/O 51.5%; shared
  adapter 59.8%. Standard errors average 0.4%.
- **Figure 9 / §5.4.** Largest TTT-over-ICL gains: Dyck languages, Ruin
  names, Movie recommendation, Hyperbaton; Boolean expressions declines
  85.7% → 80.4%. Of 27 tasks, 12 gain at least 2 points, 2 lose at least
  2.
- **Figure 5 (ARC, 1B).** FT 5% → TTT 29%; direct I/O loses 11 tasks
  (38%), no transformations 16 (55%), shared adapter 7 (24%); the
  demonstration loss adds 26% → 29%.
- **Figure 6.** Fine-tuned accuracy rises with size to 36% at 8B; after
  TTT, the 1B and 3B models are equal.
- **Table 1 (full ARC public validation, pass@2).** Fine-tuned 8B 18.3%;
  + TTT 47.1%; TTT on the BARC model 53.0%; with program synthesis 58.5%
  and 62.8% (the text says 61.9% for the last); average human 60.2%.
  Semi-private submission 47.5%.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A temporary weight update on a task's demonstrations improves accuracy over conditioning on them | strong (for the tested setting) | BBH 50.5 → 57.8 over 5 seeds; ARC ablations |
| C2 | Training the update on leave-one-out in-context tasks beats training on bare input-output pairs | moderate | Figure 5, Figure 8 |
| C3 | Gains concentrate on tasks with structural rules or distribution shift | weak | Figure 9; the authors call the reason "an open question" |
| C4 | TTT on in-context examples matches average human performance on ARC | weak | ensemble with program synthesis; text and Table 1 disagree by 0.9 points; tuned on part of the evaluation set; leakage possible |
| C5 | The results show the limitations of in-context learning for novel tasks | moderate (interpretive) | follows from C1 for the tasks where ICL fails and TTT succeeds |

## Method

For each test task with demonstrations {(x_k, y_k)}: build D_TTT from
leave-one-out tasks (each pair in turn as query, the rest as context, in
permuted orders), expanded on ARC by invertible geometric and colour
transformations; train task-specific LoRA weights on the language-model
loss over the demonstration outputs and the query output; predict with the
adapted model, on ARC under each transformation, aggregating by
hierarchical voting; discard the adapter.

## Concepts

- **test-time training (this paper)**: "temporarily updating model
  parameters during inference using a loss derived from input data".
  Footnote 2 separates it from TTT layers, where an RNN's hidden state is
  treated as parameters ([LIT-tmp8hsmf](../literature.d/LIT-tmp8hsmf.md)).
- **leave-one-out in-context task**: d_j = ({(x_k, y_k)}_{k≠j}, x_j, y_j).
- **direct I/O**: training on each (x_k, y_k) alone, without context.
- **augmented inference**: predicting under several invertible
  transformations and voting.

## Connections

Its lineage is local learning (Bottou and Vapnik 1992), transduction and
Sun et al.'s (2020) test-time training for vision. The paper cites Min et
al. ([LIT-tmpgsgpo](../literature.d/LIT-tmpgsgpo.md)) for the evidence that in-context learning does not
resemble standard learning algorithms, and its own first author's earlier
work on in-context learning as implicit learning (the same line as von
Oswald et al., [LIT-tmp2vilw](../literature.d/LIT-tmp2vilw.md)). Sun et al. ([LIT-tmp8hsmf](../literature.d/LIT-tmp8hsmf.md)) put the update
inside a layer and make it per token; here it is per task and on the
network's own weights.

## Bearing on the record

- **On the difference between changing the evidence and changing the
  interpreter.** The paper holds the evidence fixed (the K
  demonstrations) and changes only whether the model is also updated on
  it. The update helps, and helps most where the model cannot already do
  the task. So, behaviourally, using examples as context and using them
  as a training signal are not interchangeable in a language model of
  this size. This sits beside [THEORY-tmpllqzv](../theory.d/THEORY-tmpllqzv.md), which says that in
  linear attention the two are the same computation: there the "update"
  is to a model held in activations, here it is to the network's own
  weights.
- **Transient adaptation.** The update is discarded after each task, so
  it is as short-lived as a context, yet it is a change of parameters, not
  of input. Persistence and the locus of the change come apart here.
- **Agreement with the anthology.** [ANTH-LIT-379](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-379.md) reads the paper the same
  way on the main results. The one discrepancy (61.9% vs 62.8%) is in the
  paper, and is noted on the LIT.
- No instruction for machine-learning practice is drawn here.

## Limitations

- Two benchmarks, one model family, 1B–8B parameters.
- ARC hyperparameters tuned on the ablation subset; public ARC and BBH may
  be in pretraining data (authors' limitations).
- ARC results depend on a separate fine-tuning stage on synthetic tasks
  and on augmented inference, both outside the TTT comparison proper.
- The text and Table 1 disagree on the ensemble's score.
- No account of why some tasks benefit and others decline.

## Open questions

- Which property of a task predicts whether the update adds to
  conditioning? The authors propose structural rules and distribution
  shift and leave it open.
- If the update were kept rather than discarded, would the gain transfer
  to later tasks, and at what cost to others? The shared-adapter result on
  BBH suggests transfer among related tasks; the paper does not test
  persistence.
