---
number: 1879
status: Proposed
formerly:
- THEORY-tmp9mg7s
promote_when: >-
  An independent replication on a decoder language model other than
  Llama3-8B shows that setting each task's LoRA down-projection before
  fine-tuning to the smallest-variance directions of the other tasks'
  features improves task-arithmetic merges beyond seed variation, and,
  in the same run, that the measured output shift ‖B_j A_j H_iᵀ‖ falls
  under the constraint and tracks the merge gain across tasks. Gains for
  other merging methods would not settle it, since the title asserts
  them for task arithmetic only.
title: 'Low-variance LoRA projections reduce merge loss'
statement: >-
  Merged LoRA models lose accuracy because each task's low-rank update
  shifts the layer outputs on the other tasks' inputs, and constraining each
  task's down-projection before fine-tuning to the smallest-variance
  directions of the other tasks' latent features reduces the loss, raising
  task-arithmetic merges of eight GLUE LoRAs on Llama3-8B from 63.3 to 72.8
  average
version: 1
tags:
- loss-landscapes
- representation-learning
- anthology-candidate
date: '2026-11-15'
source:
- LIT-2650
summary: >-
  Zhang & Zhou (2025), [LIT-2650](../literature.d/LIT-2650.md), read in [NOTE-1965](../notes.d/NOTE-1965.md). The term is
  B2A2h1, task 2's update on task 1's input; OSRM minimizes
  ‖A_t H_¬tᵀ‖_F over orthonormal A_t, whose solution is the r
  smallest-eigenvalue eigenvectors of the other tasks' feature
  covariance. On Llama3-8B it lifts task arithmetic from 63.28 to 72.75
  but leaves TIES at 52.69 against 53.01, and its gains shrink with model
  size. That the output shift is the cause is the paper's account; it
  does not measure the term falling with the gain. The wording is the
  reader's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1897 — Proposed; filed with this entry -->
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account this one is set beside -->

# THEORY-1879: Low-variance LoRA projections reduce merge loss

## Source

Zhang & Zhou (2025), [LIT-2650](../literature.d/LIT-2650.md), read in [NOTE-1965](../notes.d/NOTE-1965.md): §§1–4.4 and
§§5.2–5.3.

## The result

- **The account** (§4.1, Eq. 1). With LoRAs summed,
  W_m h1 = (W0 + B1A1 + B2A2) h1, so task 2's update adds B2A2h1 to
  task 1's output.
- **The constraint** (§4, Eqs. 2–3). Exact orthogonality to task 1's
  features is impossible, since their matrix is typically full rank, so
  A_t minimizes ‖A_t H_¬tᵀ‖_F: the r smallest-eigenvalue eigenvectors of
  the other tasks' feature covariance.
- **Effect** (Table 5). On Llama3-8B over eight GLUE tasks, task
  arithmetic goes from 63.28 to 72.75 average with OSRM. The result could
  have gone the other way: a constraint chosen for the other tasks might
  have cost the task's own accuracy more than it saved in the merge.

## What it does not show

- **That the output shift is the mechanism.** The account is derived, and
  the remedy helps task arithmetic, but the run does not measure B_jA_jH_i
  falling and the merge gain tracking it.
- **A general remedy.** TIES is not improved on Llama3-8B (53.01 to
  52.69), gains are inconsistent across methods and shrink with model
  size.
- **Propagation.** The account is first-order and layer-local. Zhu
  (2026), [THEORY-1897](THEORY-1897.md), finds most of the activation cross-term in
  language-model merges is carried from earlier layers.
- **The usual merging setting.** It needs the other tasks' data before
  fine-tuning, which independently released LoRAs do not allow.
- **Anything about sign in coordinates.** It rivals [THEORY-107](THEORY-107.md) as a
  location for interference only loosely; both can hold, and the paper
  does not test sign against scale.
