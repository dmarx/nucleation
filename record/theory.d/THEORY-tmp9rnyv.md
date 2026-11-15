---
status: Proposed
promote_when: >-
  Independent base-to-RLVR comparisons on at least two model families not
  used by the authors, with pass@k reported up to k of at least 256,
  showing the RL model ahead at k = 1 and behind at the largest k, the RL
  model's correct paths assigned high likelihood by the base model, and a
  model distilled from a stronger teacher from the same base ahead at
  every k.
title: 'Yue and colleagues find that RLVR-trained language models beat their base models in pass@k at small k but are overtaken by them as k grows into the hundreds, across model families, RL algorithms and math, code and visual-reasoning benchmarks, with the RL models'' reasoning paths already of high likelihood under the base model, and read RLVR as sharpening sampling within the base model''s distribution rather than expanding it, whereas distillation from a stronger teacher raised pass@k at every k'
version: 1
tags:
- learning-theory
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpfmva5
bears_on:
- QUESTION-392
corroborates:
- CLAIM-567
summary: >-
  Yue et al. (2025), LIT-tmpfmva5, read in NOTE-tmp4mog9. One intervention
  raises reliability and lowers reachability at a large sampling budget,
  which corroborates CLAIM-567's distinction between them; the claim rests
  on its own demonstration, not on this. Not listed as corroborating
  CLAIM-576: whether RL changes affordability or the repertoire is what the
  dispute with ProRL (THEORY-tmpxu3kz) is about. The single-turn source of
  the dispute the record holds in its agentic form (THEORY-1703,
  THEORY-1672). The wording is the reader's; adopting it is the owner's
  call.
---
<!-- inactive-ok-file: THEORY-tmpxu3kz THEORY-tmpmapw3 THEORY-tmpr8g5y THEORY-tmppt44k — Proposed; new entries filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 THEORY-1703 THEORY-1672 — Proposed; the claim this account bears on and the agentic extension of the dispute -->

# THEORY-tmp9rnyv: Yue and colleagues find that RLVR-trained language models beat their base models in pass@k at small k but are overtaken by them as k grows into the hundreds, across model families, RL algorithms and math, code and visual-reasoning benchmarks, with the RL models' reasoning paths already of high likelihood under the base model, and read RLVR as sharpening sampling within the base model's distribution rather than expanding it, whereas distillation from a stronger teacher raised pass@k at every k

## The result

Yue et al. (2025), LIT-tmpfmva5; read in NOTE-tmp4mog9.

Base models and their zero-RL counterparts are scored by pass@k with
Brown et al.'s metric (THEORY-tmpmapw3) up to k = 256 or 1024. "Base models
consistently catch up to and eventually surpass RL-trained models across
all benchmarks" (§3); the boundary "often narrows as RLVR training
progresses" (abstract). Perplexity places RL paths inside the base
distribution. A small KL penalty gives "similar pass@1 to GRPO without KL,
but with a much lower pass@128", and matching entropy by temperature does
not close the gap. Distillation's curve "is consistently and significantly
above" the base model's (§4.2). Each could have come out the other way:
the RL curve could have stayed above at every k, as distillation's did.

## What it does not show

- That RL cannot expand the boundary. The runs are short and start from
  pretrained bases; ProRL (THEORY-tmpxu3kz) reports expansion after long
  training from a distilled model on non-math tasks, and Zhu et al.
  (THEORY-1672) above-boundary success for multi-turn agents at ample
  budgets.
- That the base model's boundary is its pass@k at k = 1024; larger k could
  move it.
- The closed form π* ∝ π0 exp(r/β), which the paper does not state and
  mostly does not train under. Its formal counterpart under a KL anchor is
  Balasubramanian and Kasiviswanathan's (THEORY-tmppt44k); its token-level
  counterpart is Meng et al.'s (THEORY-tmpr8g5y).
