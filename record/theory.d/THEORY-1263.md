---
number: 1263
status: Proposed
formerly:
- THEORY-tmpjz0xp
promote_when: >-
  Replications with several training seeds per scale, in more than one
  model family or domain, in which the privileged-context teacher's
  advantage is measured at each scale tested and the gain of
  privileged-context distillation tracks the share of supervision on
  states where that advantage is large, with the per-entry clip removed
  or held fixed as a control. Results in which unclipped OPSD keeps its
  gain at scale would count against it; more single runs on the same
  benchmarks would not settle it.
title: 'In on-policy self-distillation of language-model reasoning, a privileged-context teacher''s advantage is concentrated on the student''s failed trajectories and is smaller at larger scale, and restricting supervision to the student''s verified trajectories, with the student''s own failed attempt as the teacher''s context, keeps the gain over the base model where standard on-policy self-distillation loses it'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-31'
source:
- LIT-1883
summary: >-
  Hossain, Kousar and Tourni (2026), [LIT-1883](../literature.d/LIT-1883.md), Tables 1, 2 and 5; read
  in [NOTE-1479](../notes.d/NOTE-1479.md). Proposed: single training runs, Qwen3 only, the
  teacher's advantage measured at two of three scales, and a second
  candidate cause, per-entry clipping, left in every run. It does not
  show that the teacher's privileged knowledge is useless; it shows that
  it is hard to transmit where the student cannot see what it rests on.
---

# THEORY-1263: In on-policy self-distillation of language-model reasoning, a privileged-context teacher's advantage is concentrated on the student's failed trajectories and is smaller at larger scale, and restricting supervision to the student's verified trajectories, with the student's own failed attempt as the teacher's context, keeps the gain over the base model where standard on-policy self-distillation loses it

## Source

Hossain, Kousar and Tourni (2026), [LIT-1883](../literature.d/LIT-1883.md), §§3.2–5.3, Tables 1, 2,
4–6, Figs. 2 and 5; read in [NOTE-1479](../notes.d/NOTE-1479.md).

## What was actually shown

From prefixes of failed student rollouts, the frozen initial model given
the gold reference recovered the correct answer in 77% of continuations
against 37% for the student at 1.7B, and 67% against 50% at 4B. From
prefixes of verified rollouts the difference was at most 4 points
(Table 1). Unrelated or empty references gave no gain, so the advantage
comes from the reference's content. OPSD supervises mostly failed
trajectories (about 70%, Table 5). Its gain over the base model fell from
3.05 to 1.98 to 0.14 points at 1.7B, 4B and 8B. OASIS, which supervises
only verified trajectories and conditions the teacher on another rollout,
gained 3.64, 3.84 and 3.19 (Table 2). On verified scaffolds the teacher's
distribution moved by TV of at most 0.065 when the gold reference was
replaced by the student's own failed attempt (Fig. 2b).

What could have come out otherwise: OASIS's gain could have faded with
scale as OPSD's did, or the teacher could have needed the gold reference
on verified scaffolds too.

## What this does not say

- **That the privileged-information gap causes OPSD's decline.** The two
  are reported together. Per-entry clipping, which reverses gradients on
  the teacher's preferred tokens and affects about a third of tokens, is
  present in every run, and the authors offer it as a second explanation
  of late drift.
- **That the advantage keeps shrinking.** It was measured at 1.7B and 4B
  only.
- **That the teacher adds nothing on verified trajectories.** OASIS beats
  GRPO with the same verifier (Table 2), so the dense teacher signal
  helps there; what it carries is mostly not the reference.
- **Anything beyond Qwen3 and competition mathematics**, or beyond 100
  steps of LoRA training.
