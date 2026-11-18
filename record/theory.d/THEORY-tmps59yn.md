---
status: Proposed
promote_when: >-
  An independent replication of the Table 4 contrast: OFT experts on a
  base model other than Llama-3.1-8B, merged by averaging their
  inverse-Cayley generators in so(d) with and without the rescaling
  Σ‖Q_i‖/‖ΣQ_i‖, over several seeds, with the corrected merge ahead by
  more than seed variation, and the uncorrected mean's norm measured
  below the members' mean norm. Results on LoRA or full fine-tuning, or
  against other baselines, would not settle it, since the title is about
  the OFT case.
title: 'Averaging the so(d) generators of models adapted by orthogonal finetuning shrinks the merged rotation as conflicting directions cancel, and rescaling the mean generator to the members'' mean norm is what lifts the merge, on five Llama-3.1-8B experts from 41.01 to 46.25, above the experts'' own 44.71'
version: 1
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpspkpa
summary: >-
  Yang, Shi & Liu (2026), [LIT-tmpspkpa](../literature.d/LIT-tmpspkpa.md), read in [NOTE-tmpy669h](../notes.d/NOTE-tmpy669h.md). Each
  task's rotation is mapped to so(d) by the inverse Cayley transform (not
  a matrix logarithm), the generators are averaged, the mean is rescaled
  by Σ‖Q_i‖/‖ΣQ_i‖, and the result is mapped back by the Cayley transform.
  The ablation separates the geometry from the rescaling: averaging in
  so(d) without it scores 41.01, barely above averaging rotations
  directly (39.53). One base model, the authors' own experts, no seeds.
  The wording is the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the other ablation in which rescaling matters most -->

# THEORY-tmps59yn: Averaging the so(d) generators of models adapted by orthogonal finetuning shrinks the merged rotation as conflicting directions cancel, and rescaling the mean generator to the members' mean norm is what lifts the merge, on five Llama-3.1-8B experts from 41.01 to 46.25, above the experts' own 44.71

## Source

Yang, Shi & Liu (2026), [LIT-tmpspkpa](../literature.d/LIT-tmpspkpa.md), read in [NOTE-tmpy669h](../notes.d/NOTE-tmpy669h.md): §§1–6,
Tables 1–4.

## The result

- **The construction** (§3, Eqs. 2, 5, 6). Each OFT expert's rotation R_i
  gives a skew-symmetric Q_i = (R_i − I)(R_i + I)⁻¹. By the triangle
  inequality ‖ΣQ_i‖ ≤ Σ‖Q_i‖, so the plain mean "can suffer from magnitude
  collapse due to destructive interference". OrthoMerge multiplies the
  mean by c = Σ‖Q_i‖/‖ΣQ_i‖ and maps back with R = (I + Q)(I − Q)⁻¹.
- **The ablation** (Table 4). On five Llama-3.1-8B OFT experts: averaging
  the rotations directly 39.53, their sequential product 40.76, averaging
  in so(d) without correction 41.01, with correction 46.25. The experts
  average 44.71 (Table 1). The comparison could have gone the other way:
  if the geometry did the work, the uncorrected so(d) mean would have
  carried most of the gain, and it carries 1.5 of 6.7 points.
- **Against baselines** (Table 1). Task arithmetic, TIES and TSV-M applied
  to the same OFT experts reach 41.46, 44.61 and 44.97.

## What it does not show

- **That hyperspherical energy is the mechanism.** The paper motivates the
  method by preserving it; no result measures it as a mediator.
- **That cancellation is the whole loss.** The ablation shows rescaling
  helps; that the uncorrected mean's shortfall is caused by cancelled
  norm rather than by rescaling doing something else (a larger effective
  step) is the paper's reading, not a separate test.
- **That it transfers beyond OFT.** For LoRA and full fine-tuning the
  method's rotation carries little of the update under Conflict-Aware
  decoupling (Fig. 4), and its gains on MergeBench Llama-3.2-3B are small
  and mixed, one negative (Table 2).
- **Anything about sign in coordinates.** It bears on [THEORY-107](THEORY-107.md) only by
  analogy: a second method in which handling magnitude matters most. It
  does not test [THEORY-107](THEORY-107.md)'s oracle-sign condition.
- **A symmetry.** Its orthogonal maps are the adaptation and change the
  function; [THEORY-112](THEORY-112.md)'s orthogonal map is a symmetry that preserves it.
- **That the experts are surpassed generally.** One base, five tasks, the
  authors' own experts, no seeds or intervals.
