---
status: Read
paper: LIT-tmpbi4vz
title: 'Yin and Steinhardt 2025 — Which Attention Heads Matter for In-Context Learning?'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    URL read: https://arxiv.org/pdf/2502.14010 (HTTP 200, 1.4 MB PDF, arXiv
    v1 of 19 Feb 2025). Kind of copy: arXiv preprint (step 5, first place to
    look). Date: 2026-11-19. Nothing stopped the fetch. Text extracted with
    pdftotext -layout to dl/text.txt. Read: the whole main text (abstract,
    §§1-7, Table 1 summary of findings, Table 2 models), Figures 1-6
    captions. Skipped: references and the appendices (A.1-A.11: all-head
    scores, other ablation methods, FV task-execution tests, per-task
    ablations, head locations in all 12 models, overlap of ablated sets,
    per-model training curves); A.10 and A.11 opening paragraphs only
    glanced at.
date: '2026-11-19'
---

# NOTE-tmpa9eoe: Yin and Steinhardt 2025 — Which Attention Heads Matter for In-Context Learning?

## Contribution

The paper compares two mechanisms proposed for in-context learning in the same 12 models (Pythia 70M–6.9B deduped, GPT-2 117M–1.6B, Llama 2 7B). Induction heads find an earlier occurrence of the current token and copy what followed, scored on repeated random token sequences. Function-vector (FV) heads carry a compact task representation, scored by Todd et al.'s causal mediation: how much patching in a head's mean task-conditioned activation restores the correct output on prompts with shuffled labels. Three moves: ablation "with exclusion", which ablates induction heads that are not FV heads and vice versa, because the two scores correlate; two different ICL metrics, few-shot accuracy on 19 held-out tasks against Olsson et al.'s token-loss difference; and tracking both scores over 8 checkpoints of 7 Pythia models.

## Key results

- Table 1 and §4, Figure 4. "Ablating FV heads hurts few-shot ICL accuracy more than ablating induction heads." With exclusion, ablating non-FV induction heads costs about as much as random ablation, "comparable to random ablations in models" above 1B parameters, while ablating non-induction FV heads still hurts substantially. The gap widens with scale: the "importance of FV heads increases with model scale"; at 70M the two have similar effects (§2.3).
- §3, Figure 3. The two sets are mostly distinct: zero overlap of the top 2% in seven of twelve models, 5–15% in the rest; FV heads sit in slightly deeper layers. But scores correlate: FV heads are around the 90–95th percentile of induction score, and vice versa.
- §4, Figure 4 bottom. On token-loss difference the pattern reverses for models over 345M: induction ablations matter more. The experiment "demonstrates that few-shot ICL accuracy and token-loss" difference measure different things, which the authors take as the main reason earlier work credited induction heads.
- §5.1, Figure 5. In all Pythia models induction heads appear at about "step 1,000 out of 143,000, while FV heads appear" around step 16,000; induction scores rise sharply then plateau, while "FV scores demonstrate a gradual but" sustained increase to the end of training. Few-shot ICL accuracy starts rising with the induction heads and "continues to gradually increase throughout training."
- §5.2, Figure 6. "Some FV heads evolve from induction heads during training": many eventual FV heads first have high induction scores that decline as FV scores rise. "Importantly, this pattern is unidirectional; we" found no induction head that gains FV score.
- §6. Two conjectures: induction heads are a precursor that FV heads supersede (C1), or FV heads are polysemantic combinations (C2). The authors favour C1 and mark "FV heads implement more complex or abstract computations than induction heads." as speculation (Table 1).

## Assumptions

- ICL is few-shot accuracy with 10 demonstrations on tasks from Todd et al. (and 8 added), split so that tasks used to find FV heads are not used to evaluate ablations.
- "Induction head" and "FV head" are the top 2% by each score; mean ablation, with other ablation methods in an appendix.
- FV scores use corrupted prompts with shuffled labels, so they measure heads that carry the task when the input–label pairing is uninformative.

## Concepts

- **Induction head**: a head that attends to the token after an earlier occurrence of the current token.
- **Function vector (FV) head**: a head whose mean activation on a task carries enough of the task to restore correct outputs when patched in (Todd et al. 2024; Hendel et al. 2023 for task vectors).
- **Ablation with exclusion**: ablating heads of one type while sparing the top heads of the other, to remove the confound of correlated scores.
- **Token-loss difference**: loss at token 50 minus loss at token 500 (inverted from Olsson et al.), which the authors separate from few-shot ICL.

## Bearing on the record

- **THEORY-990** (qualifies, against its strong form). THEORY-990 holds Olsson et al.'s proposal that induction heads are the mechanism of most ICL at every size. For few-shot ICL accuracy in models from about 1B to 7B, Yin and Steinhardt find induction heads without FV character dispensable and FV heads necessary. The proposal survives only for token-loss difference, Olsson et al.'s own metric.
- **THEORY-973** (consistent, scoped). The small-model result there uses token-loss difference. Yin and Steinhardt agree that induction heads carry that metric, and that induction heads form early and abruptly (about step 1,000 in Pythia). They show it is a different quantity from few-shot task accuracy.
- **CASE-tmphsr99** (bears on the in-context arm and its interventions). The CASE's model is Pythia, and the reading gives a developmental baseline for it. ICL heads keep forming late: FV scores and few-shot ICL accuracy rise from about step 16,000 to the end of training in all seven Pythia sizes. So in-context adaptability is still rising at late checkpoints, the pattern A56 said would count against overconsolidation read as a loss of all adaptability. The CASE's query–key reset intervention could remove FV heads, which carry ICL, and that is a cost to score. The reading spans 70M–6.9B, so the CASE's 70M and 160M are inside its range; at 70M induction and FV heads matter about equally.
- **THEORY-1353** (bears on). THEORY-1353 has plasticity loss as the depletion of uncommitted heads. Yin and Steinhardt show heads being repurposed late in Pythia training, induction heads becoming FV heads, which is commitment by conversion as well as by recruitment. They do not measure plasticity.
- **CLAIM-tmp1l2s7** (supports, as an instance of separate movement). Within one training run the head-level organization changes (FV heads strengthen) while the few-shot ICL frontier keeps growing gradually. This is the operational frontier for one route measured across checkpoints. It is not the developmental frontier, which needs acquisition budgets the paper does not measure.
- **CLAIM-118** (leaves open). FV heads are a candidate site where what the context supplies (the demonstrations) becomes a task representation used by a fixed interpreter. The paper does not address the distinction.

## Limitations

- Correlational developmental evidence: the precursor story (C1) is a conjecture, and C1 does not explain FV heads with low induction scores throughout training.
- Pythia checkpoints only for training dynamics (8 per model); a single run per size.
- Simple, mostly lexical ICL tasks with 10 demonstrations; FV scores depend on Todd et al.'s task set.
- The top-2% thresholds and mean ablation are choices; robustness to other ablation methods is reported only in an appendix, which was not read.
