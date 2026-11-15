---
status: Read
paper: LIT-tmp7463t
title: 'Liu et al. — ProRL'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Read on 2026-11-15 from arXiv:2505.24864v1, https://arxiv.org/pdf/2505.24864,
    text by pdftotext. Read: the abstract, §1, §2.2–2.3 (entropy collapse,
    DAPO, the KL penalty and reference reset), the §3 headline results
    (tables skimmed), §4.1, §4.2 (with the Fig. 4 caption), §4.3, the
    opening of §4.4, §6 and App. A (limitations). Skipped: the appendix
    figures, the per-task plots and the training details, so the per-task
    evidence was read through captions and text only. The filer rechecked
    every quote below against the downloaded text.
date: '2026-11-15'
summary: >-
  Prolonged, diversity-preserving RL from a distilled 1.5B reasoning model
  raises pass@k up to 128 on many non-math tasks, sometimes from zero;
  gains shrink where the start model is already strong and are nil or
  negative on math. The counterclaim to Yue et al., and the test case for
  whether RL changes what is reachable.
---
<!-- inactive-ok-file: CLAIM-576 THEORY-1703 THEORY-1672 CLAIM-663 — Proposed; the claim this reading tests and the agentic extension of the dispute -->

# NOTE-tmppn4n4: Liu et al. — ProRL

## Contribution

Long RL training (more than 2k steps) of DeepSeek-R1-Distill-Qwen-1.5B on
136K problems in math, code, STEM, logic puzzles and instruction
following, with GRPO, DAPO's components, a KL penalty and periodic hard
resets of the reference policy and optimizer. The authors report pass@k
gains, including on tasks where the starting model fails at every k tried,
and argue that earlier negative results stopped training too soon and
looked only at math.

## Key insight

If exploration is kept alive (entropy maintained, the policy allowed to
drift by resetting its anchor), RL can keep improving past the point where
short runs plateau, and the gains come where the start model was weakest.

## Assumptions

- The "base" is already a distilled reasoning model, not a pretrained
  base.
- "Extensive sampling" is pass@k up to k = 128 in the plots and text read.
- Novelty is measured as low overlap with a pretraining corpus (the
  Creativity Index against DOLMA), not as absence from the base model's
  samples.

## Key results

- **Abstract**: "prolonged RL (ProRL) training can uncover novel reasoning
  strategies that are inaccessible to base models, even under extensive
  sampling"; "RL-trained models consistently outperform base models across
  a wide range of pass@k evaluations, including scenarios where base models
  fail entirely regardless of the number of attempts."
- **§1**: contrary findings come from "an overreliance on specialized
  domains like mathematics" and "premature termination of RL training",
  "typically no more than hundreds of steps".
- **§2.2–2.3**: entropy collapse is the obstacle; DAPO's components are
  "specifically designed to maintain exploration and output diversity";
  the loss is L_GRPO − β·D_KL(πθ‖πref) (Eq. 4), and "we hard-reset the
  reference policy" to a recent snapshot.
- **§4.1**: "a significant negative correlation between the base model's
  reasoning boundary and the extent of reasoning improvement after RL";
  where base pass@128 is high, gains are "minimal or even negative", "a
  narrowing of the reasoning boundary".
- **§4.2, Fig. 4**: per-task trends fall into diminish, plateau and
  sustained; on math the final model shows "decreased or unchanged
  reasoning capacity compared to the base model, aligning with observations
  of prior work".
- **§4.4**: restates Dang et al.'s bound E[pass@k] ≤ 1 − ((1 − E[ρx])² +
  Var(ρx))^{k/2} (Eq. 5).
- **Novelty**: prolonged RL gives trajectories "with higher novelty" by the
  Creativity Index.
- **App. A**: one 1.5B model; it "remains unclear how well our approach
  scales to larger models"; resets "may lead to inconsistent results".

## Concepts

Prolonged RL; entropy collapse; DAPO (decoupled clipping, dynamic
sampling); KL penalty with reference-policy reset; reasoning boundary
(pass@k); Creativity Index; diminish, plateau and sustained regimes.

## Bearing on the record

- **CLAIM-576 and QUESTION-392**: the test case. A pass@k that rises from
  zero means RL moved an unreached target into reach, which under the
  claim is more than a budget change. Whether it is the claim's change of
  architecture, or a target the start model would reach at k far above
  128, the paper cannot rule out.
- **CLAIM-567**: in the other direction from Yue et al.: reachability at a
  fixed sampling budget can grow under training. That the two properties
  move separately is the claim's point either way.
- **Yue et al. (LIT-tmpfmva5)**: the two do not straightforwardly conflict.
  Different start model, training length, task mix and k; and ProRL
  reports narrowing on math, agreeing with Yue there.
- **The agentic extension**: Zhu et al. (THEORY-1672) find RL above the base
  Pass@K boundary for multi-turn agents only at ample budgets, and Zhai et
  al. (THEORY-1703, CLAIM-663) expansion only on compositional retrieval.
  ProRL's single-turn expansion is likewise task-conditional: largest where
  the start model is weak.
- **On A's math**: the KL penalty is present, but the resets mean there is
  no fixed π0 for an exponential tilt, and the paper does not state the
  closed form.

## Limitations

- One 1.5B model; per-task evidence read through captions.
- "Regardless of the number of attempts" rests on finite k.
- The base is a distilled model, so "beyond the base model" is beyond a
  model already trained on a stronger model's reasoning.
