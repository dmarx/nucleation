---
status: Read
paper: LIT-tmpfmva5
title: 'Yue et al. — Does RL incentivize reasoning beyond the base model?'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2504.13837v5, https://arxiv.org/pdf/2504.13837,
    text by pdftotext. Read: the abstract, §1, the RLVR background (§2),
    the §3 math results (Fig. 2, Minerva, Oat-Zero and DAPO), the §4.1
    summary, the perplexity analysis, §4.2 (distillation), §4.4 briefly,
    the KL and entropy ablations, and §7. Skimmed: the code and
    visual-reasoning results, §5 and the appendices; Figs. 20–21 were not
    seen. The filer rechecked every quote below against the downloaded
    text.
date: '2026-11-15'
summary: >-
  RLVR from pretrained bases wins pass@k at small k and loses it at large
  k; the RL models' correct paths are already likely under the base model;
  distillation lifts the whole curve. The authors: RLVR sharpens within the
  base prior. A measured case of reliability and reachability moving in
  opposite directions under one intervention.
---
<!-- inactive-ok-file: LIT-tmpfmva5 THEORY-tmp9rnyv LIT-tmp7463t LIT-tmpnkxqn LIT-tmpdyhv5 THEORY-tmpmapw3 — new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 THEORY-1703 THEORY-1672 CLAIM-663 ARG-093 CLAIM-654 — Proposed; the claim this reading bears on and the record's agentic extension of the dispute -->

# NOTE-tmp4mog9: Yue et al. — Does RL incentivize reasoning beyond the base model?

## Contribution

A systematic comparison of base models and their zero-RL RLVR
counterparts (Qwen2.5 7B, 14B and 32B; LLaMA-3.1-8B; GRPO, PPO and
others) by pass@k up to large k on math, code and visual reasoning. RLVR
helps at small k and the base model overtakes it at large k. Perplexity
analysis places the RL models' paths inside the base model's distribution,
and distillation, unlike RLVR, expands what is reachable.

## Key insight

pass@1 and pass@k at large k are different properties of a sampling
process, and RLVR as practised raises the first at the cost of the second:
it makes already-reachable answers more likely and some reachable answers
less.

## Assumptions

- Zero-RL from pretrained bases for math. Pass@k is taken as the measure
  of a reasoning boundary.
- "The base model is an upper bound" means: of what it samples at up to
  k = 256 or 1024. Correctness is by final answer; base-model chains of
  thought "manually selected from 2048 samplings" for the hardest AIME24
  questions are offered as genuine solutions.

## Key results

- **The crossover** (abstract): "while RLVR-trained models outperform their
  base models at smaller values of k (e.g., k=1), base models achieve
  higher pass@k score when k is large. Moreover, we observe that the
  reasoning capability boundary of LLMs often narrows as RLVR training
  progresses."
- **Consistency** (§3): "base models consistently catch up to and
  eventually surpass RL-trained models across all benchmarks"; on Minerva
  at 32B the base model leads "by approximately 9% at k = 128".
- **Sampling efficiency** (§4.1): "the observed improvement in average
  scores stems from more efficient sampling on these already solvable
  problems"; "RLVR mainly sharpens the distribution within the base
  model's prior rather than expanding beyond it."
- **Distillation** (§4.2): the distilled model's pass@k curve "is
  consistently and significantly above" the base model's.
- **KL** (ablation): with a KL coefficient of 0.001 the model reaches
  "similar pass@1 to GRPO without KL, but with a much lower pass@128."
- **Entropy** (ablation): "reduced entropy contributes to the narrowing",
  but "it alone does not fully account for the reduction."
- **Conclusion** (§7): "current RLVR rarely elicits fundamentally new
  reasoning patterns"; "emerging techniques may mitigate some of the
  limitations identified here."

## Concepts

RLVR; pass@k as a reasoning boundary; sampling efficiency and its gap;
sharpening within the base prior; distillation as expansion; entropy
reduction.

## Bearing on the record

- **CLAIM-567**: a measured case. RLVR raises reliability (pass@1) while
  shrinking what is reachable at large k, so the two are distinct
  properties of a process, which the claim demonstrates. It also shows a
  trade between them under one intervention, which the claim does not
  assert.
- **CLAIM-576 and QUESTION-392**: whether RL "creates a capability" depends
  on the budget at which the repertoire is read. The contrast with
  distillation is a candidate for QUESTION-392's line between creating a
  capability and making one cheaper to reach. Whether RL is a change of
  architecture or of affordability in the claim's terms is not settled by
  the paper.
- **The agentic extension** (LIT-2441, THEORY-1703, CLAIM-663, ARG-093;
  LIT-2414, THEORY-1672; CLAIM-654): Zhai et al. extend this paper's
  question with an interaction-depth axis, and Zhu et al. find multi-turn
  RL above the base model's Pass@K boundary, unlike this single-turn
  result, and only at ample budgets. The record held the extension and not
  this source.
- **Brown et al.** (THEORY-tmpmapw3) supplies the metric; ProRL
  (LIT-tmp7463t) contests the conclusion; Meng et al. (LIT-tmpnkxqn) and
  Balasubramanian and Kasiviswanathan (LIT-tmpdyhv5) give token-level and
  formal counterparts of the sharpening reading.
- **On A's math**: the paper does not state π* ∝ π0 exp(r/β), and most of
  its runs train without KL.

## Limitations

- Mostly Qwen2.5 bases.
- RL runs are short, the point ProRL contests.
- Pass@k at k ≤ 1024 bounds the base model's reach only empirically.
