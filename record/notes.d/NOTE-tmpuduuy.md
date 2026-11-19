---
status: Read
paper: LIT-tmpm4bnq
title: 'Raghu and others 2019 — Rapid Learning or Feature Reuse? Towards Understanding the Effectiveness of MAML'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/1909.09157 (21 pages; header "Published
    as a conference paper at ICLR 2020"). Raghu, Raghu, Bengio and Vinyals.
    Kind of copy (step 5): arXiv preprint, the authors' own manuscript (the
    ICLR 2020 camera-ready). Lawful. Date: 2026-11-19. HTTP 200, no bot
    check, no refusal. No email address sent. Text extracted with pdftotext
    to dl/text.txt; PDF in dl/paper.pdf. Read: abstract, §1-§7 in full (pp.
    1-9), Appendix A (datasets and experimental setup) opening. Skipped:
    Appendices B-D (additional freezing and representational results, ANIL
    details, NIL head comparisons), except as cited in the main text. Table
    values read from the text, not re-derived. Note: the record's LIT (LIT-
    tmpm4bnq) is filed under first author Raghu; the batch key "anil" names
    the paper's algorithm.
date: '2026-11-19'
---

# NOTE-tmpuduuy: Raghu and others 2019 — Rapid Learning or Feature Reuse? Towards Understanding the Effectiveness of MAML

## Contribution

Aniruddh Raghu, Maithra Raghu, Samy Bengio and Oriol Vinyals ask whether MAML's few-shot success comes from "rapid learning", meaning large, efficient changes to representations in the inner loop, or from "feature reuse", where the meta-initialization already holds good features. Freezing the network body at test time and comparing representations before and after adaptation (CCA, CKA) both show feature reuse. That leads to ANIL (inner loop on the head only), which matches MAML, and NIL (no head, cosine similarity on frozen features), which matches too. Training with task-specific heads (MAML/ANIL) learns better features than multiclass or multitask training.

## Key results

- The answer (abstract, p. 1): "finding that feature reuse is the dominant factor".
- Freezing the body (Table 1 caption, p. 4): "freezing even all four convolutional layers of the network (all layers except the network head) hardly affects accuracy".
- Representations barely move (§3.2.2, p. 5): "with CCA similarity scores of > 0.9, indicating that the inner loop induces little to no functional change".
- Throughout training (§3.3, p. 5): "even early on in training, significant feature reuse is taking place".
- ANIL (abstract, p. 1): "ANIL matches MAML’s performance on benchmark few-shot image classification and RL".
- The head at training time matters for the features (§5.2, p. 9): "Multitask training, which has no task specific head, performs the worst, even worse than random features".
- Other meta-learners (§6, pp. 9-10): the authors read prior results as showing that "feature reuse" rather than "rapid learning" dominates model-based meta-learning too.
- Their own limit (§7, p. 10): "our study mainly considered benchmark datasets, such as Omniglot and MiniImageNet".

## Assumptions

- That test tasks from the benchmarks' held-out classes share the training classes' useful features. That is the regime where reuse suffices.
- That CCA and CKA similarity near 1 means no functional change in a layer.
- The original MAML 4-layer convolutional architecture and hyperparameters.

## Concepts

- Rapid learning: adaptation by large, efficient changes in representations, from a well-conditioned initialization.
- Feature reuse: adaptation in which the body's features are used as they are and only the head aligns to the task.
- ANIL (Almost No Inner Loop) and NIL (No Inner Loop).

## Bearing on the record

- CLAIM-tmp8ljvp: supports the Not-one-scalar clause in a weaker form than the claim gives it. The paper separates two routes to fast few-shot performance: reusing features held, and changing features quickly. It shows MAML's performance on these benchmarks takes the first. It does not show the capacity to acquire new structure moving apart from reusable structure over training, and it measures no retention. What it does show is that a learner can adapt fast on new tasks with almost no capacity to change its representations, so fast adaptation is not evidence of plasticity. The authors themselves call "rapid learning" something future algorithms should do more of.
- CASE-tmphsr99: a methodological warning. An adaptation budget measured on task families that existing features already serve measures reuse, not the capacity to acquire. The case's held-out synthetic families (parity, associative retrieval, two-hop composition) should be checked against a frozen-body or linear-probe baseline (NIL-style), so a low budget is not read as plasticity. The case's frozen-readout mode (A54) already gives that baseline, and this paper says why it matters.
- CLAIM-tmp5vg7p: leaves open. It says nothing on loss of plasticity, forgetting or late interventions.

## Limitations

- Small convolutional networks on Omniglot and MiniImageNet. The tasks are drawn from one distribution, which favours reuse.
- No continual or long-horizon setting. Plasticity loss and forgetting are not studied.
- Similarity indices are summaries. The paper notes a slight dip in higher layers that it attributes to compounding.
