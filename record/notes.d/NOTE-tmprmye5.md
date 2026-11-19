---
status: Read
paper: LIT-tmpjzvu6
title: 'Brown and colleagues — Language Models are Few-Shot Learners'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2005.14165v4: §§1-8
    in full, appendices B and C skimmed, the captions of D and H, figures
    1.2 and 3.8 as images; appendices A, E, F and G skipped. Running notes
    on the branch claude/readers/gpt3 (the procedure proposed in pull request 537), deleted at filing.
    Quotations rechecked by the filer by script against the downloaded text.
date: '2026-11-19'
summary: >-
  Few-shot in-context learning across model sizes at fixed pretraining
  data: performance with K demonstrations in the context, and no weight
  update, rises with K and with size, and the gain over zero-shot grows
  with size. Accuracy is plotted against K; examples to a level can only
  be read off a figure for one task. No comparison without pretraining,
  and pretraining length is not varied. In-context learning changes no
  weights, and the authors leave open whether it learns tasks or
  recognizes them.
---
<!-- inactive-ok-file: TERM-131 THEORY-2039 CLAIM-756 CLAIM-697 — Proposed; entries this reading bears on -->

# NOTE-tmprmye5: Brown and colleagues — Language Models are Few-Shot Learners

## Contribution

An empirical case that in-context ability grows with model size, and a
vocabulary: meta-learning for the outer loop (pretraining) with an inner
loop, "in-context learning" for the inner loop, and zero-, one- and
few-shot for the number of demonstrations.

## Key results

1. **Scale and in-context efficiency.** "Larger models make increasingly
   efficient use of in-context information." (Fig. 1.2); "While
   zero-shot performance improves steadily with model size, few-shot
   performance increases more rapidly, demonstrating that larger models
   are more proficient at in-context learning." (Fig. 1.3). Accuracy is
   plotted against K by size; examples to a level is never reported as a
   number.
2. **What scale means.** Model size at fixed data: "All models were
   trained for a total of 300 billion tokens." (Table 2.1). No model
   without pretraining is compared.
3. **An exchange rate.** "GPT-3 requires less than eight total examples
   per task to outperform a fine-tuned BERT-Large on overall SuperGLUE
   score" (§3.7), the reference "fine-tuned on the SuperGLUE training set
   (125K examples)" (Fig. 3.8): demonstrations against fine-tuning
   examples, across different systems.
4. **No weights change.** In-context learning "occurs within the
   forward-pass upon each sequence" (Fig. 1.1); "these “learning” curves
   involve no gradient updates or fine-tuning, just increasing numbers of
   demonstrations given as conditioning" (§1); few-shot gives
   demonstrations "but no weight updates are allowed" (§2).
5. **Learning or recognition, left open.** The terms "remain agnostic on
   the question of whether the model learns new tasks from scratch at
   inference time or simply recognizes patterns seen during training"
   (footnote 1); "Synthetic tasks such as wordscrambling or defining
   nonsense words seem especially likely to be learned de novo, whereas
   translation clearly must be learned during pretraining" (§5); on
   synthetic tasks "the model really does appear to learn these tasks at
   test time" (§3.9.2).
6. **Where it fails.** "Larger values of K are usually but not always
   better" (§2.4); "WiC is a notable weak spot with few-shot performance
   at 49.4% (at random chance)" (§3.7); comparison tasks barely above
   chance (§5).

## Assumptions

Benchmark accuracy at a given K stands in for task acquisition;
contamination handled by clean subsets; one run per size on a fixed
token budget.

## Concepts

Meta-learning (outer and inner loop); in-context learning; zero-, one-
and few-shot; in-context learning curves; task recognition against de
novo learning; contamination; amortized pretraining compute.

## Bearing on the record

- **CLAIM-756.** Weak evidence for its premise: larger pretrained models
  reach a level with fewer examples, and a few demonstrations rival
  125,000 fine-tuning examples. Short of what the owner's point at U37
  needs: the comparison is across sizes, not with and without pretraining;
  pretraining's cost is not set against the saving; and the later
  "acquisition" retains nothing.
- **TERM-131.** Evidence on the open point LEAD-tmpn5ruw named. Against
  counting in-context learning as learning in the term's sense: no
  weights change and nothing is said to persist beyond the sequence. For
  it, within a sequence: the context is retained state that changes later
  outputs, and the authors call it learning. Pretraining, the outer loop,
  is learning in the term's sense either way. In CLAIM-754's terms the
  success may be the operational frontier reached with a larger operating
  budget (the context) rather than an acquisition.
- **THEORY-2039** (Pan and colleagues) operationalizes the question the
  authors leave open, on these models.

## Limitations

Figure values read by eye; Table H.1 not read cell by cell; the NeurIPS
version not compared.
