---
status: Proposed
promote_when: >-
  Two results, by a second group, on models or tasks outside CLIP image
  classification: that per-layer updates of full fine-tuning from one
  start are close to low-rank, and that truncating each to its top
  singular components and orthogonalising them across tasks raises merged
  accuracy well above task arithmetic. And a test that separates overlap
  from truncation: at fixed rank and update norm, merges whose layers'
  singular vectors overlap more across tasks lose more. It is refuted if
  accuracy loss does not track singular-vector overlap once rank and norm
  are held fixed.
title: 'Gargiulo et al.: for CLIP ViTs fully fine-tuned on 8 to 20 image tasks from one start, each layer''s weight update is close to low-rank, merging loses accuracy where different tasks'' singular vectors overlap, and truncating each update to its top singular components and orthogonalising them across tasks raises merged accuracy by about 15 points over task arithmetic on ViT-B/32'
version: 1
tags:
- loss-landscapes
- mathematics
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmpbknaa
summary: >-
  Gargiulo et al. (2025), [LIT-tmpbknaa](../literature.d/LIT-tmpbknaa.md), read in [NOTE-tmpv6jne](../notes.d/NOTE-tmpv6jne.md). Keeping 3%
  of each task's singular components per layer costs 1.5% accuracy;
  cross-task singular-vector overlap is highest in early layers; TSV-M
  reaches 85.86 against 70.79 for task arithmetic on ViT-B/32 with 8
  tasks; the ablation needs both truncation and decorrelation. That
  overlap is the cause rests on an association over three task sets. A
  rival diagnosis to TIES's sign conflicts, [THEORY-107](THEORY-107.md). The wording is
  the reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-107 THEORY-tmpqv3ve — new tmp codes, or Proposed; source, reading and neighbouring accounts, named and not leaned on -->

# THEORY-tmp6ikb6: Gargiulo et al.: for CLIP ViTs fully fine-tuned on 8 to 20 image tasks from one start, each layer's weight update is close to low-rank, merging loses accuracy where different tasks' singular vectors overlap, and truncating each update to its top singular components and orthogonalising them across tasks raises merged accuracy by about 15 points over task arithmetic on ViT-B/32

## Source

Gargiulo, Crisostomi, Bucarelli, Scardapane, Silvestri & Rodolà (2025),
[LIT-tmpbknaa](../literature.d/LIT-tmpbknaa.md), read in [NOTE-tmpv6jne](../notes.d/NOTE-tmpv6jne.md): §§1–7 and supplementary §A.

## The result

- **Low rank** (§3.2): per-layer task matrices of CLIP ViTs, fully
  fine-tuned, keep nearly all accuracy at 3% of their singular components.
- **Overlap as interference** (§3.3, supp. §A): STI measures how far the
  concatenated singular vectors of different tasks depart from
  orthogonal. Collinear vectors double when they agree and cancel when
  they disagree.
- **The merge** (Table 2): TSV-M beats task arithmetic by 15.45 points and
  Consensus TA by 10.71 on average on ViT-B/32 across 8, 14 and 20 tasks,
  with no scaling coefficient.
- **Both steps matter** (Table 4): truncation alone is worse than task
  arithmetic; decorrelation alone at full rank gains 3.1 to 6.1; together
  15.8 to 17.5.
- **Overlap tracks loss** (Fig. 8): lower STI goes with higher accuracy,
  on three task sets.

## What it does not show

- **That overlap causes the loss.** The evidence is an association and an
  ablation that changes rank and overlap together. No experiment varies
  overlap at fixed rank and norm.
- **Anything outside vision.** CLIP image classification only, on one set
  of public checkpoints.
- **Anything against TIES directly.** TIES is not run. The comparison of
  sign against structure is the over-counting paper's ([THEORY-tmpqv3ve](THEORY-tmpqv3ve.md)),
  which runs both.
- **Anything about LoRA.** The low-rank updates are full fine-tuning
  updates found to be close to low-rank, not adapters.
