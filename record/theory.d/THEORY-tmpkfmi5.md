---
status: Proposed
promote_when: >-
  A second group's measurements, on CLIP ViTs or other pretrained models,
  that (1) post-hoc linearised fine-tuned models lose single-task
  accuracy, so fine-tuning is not in the linear regime; (2) fine-tuning
  the linearisation enlarges the region of low disentanglement error and
  raises task-addition accuracy and negation forgetting over ordinary
  fine-tuning; and (3) task addition from random initialisation stays
  near chance. It is refuted if, at equal single-task accuracy,
  linearised and ordinary task vectors add equally well, since then the
  gain is single-task fit and not disentanglement.
title: 'Ortiz-Jimenez, Favero and Frossard: task arithmetic in CLIP ViTs is not explained by fine-tuning in the linear regime, since they do not fine-tune in it, but by weight disentanglement, each task vector changing the output only on its own task''s inputs; pretraining supplies it, and fine-tuning the model''s linearisation strengthens it and improves task addition and negation'
version: 1
tags:
- loss-landscapes
- learning-theory
- anthology-candidate
date: '2026-11-15'
source:
- LIT-tmphs8vv
bears_on:
- QUESTION-069
- QUESTION-318
summary: >-
  Ortiz-Jimenez, Favero & Frossard (2023), [LIT-tmphs8vv](../literature.d/LIT-tmphs8vv.md), read in
  [NOTE-tmpmq65g](../notes.d/NOTE-tmpmq65g.md). Post-hoc linearised CLIP models lose single-task
  accuracy, so ordinary fine-tuning is nonlinear; disentanglement error is
  small near the pretrained weights; linearised fine-tuning raises task
  addition by up to 5.8 points and negation forgetting by up to 13.1,
  less for larger models; from random initialisation task addition is
  near chance. Disentanglement is by construction equivalent to the
  property it explains. The wording is the reader's; adopting it is the
  owner's call.
---
<!-- inactive-ok-file: THEORY-tmpup4vk THEORY-107 THEORY-tmpjlixb — new tmp codes, or Proposed; source, reading and neighbouring accounts, named and not leaned on -->

# THEORY-tmpkfmi5: Ortiz-Jimenez, Favero and Frossard: task arithmetic in CLIP ViTs is not explained by fine-tuning in the linear regime, since they do not fine-tune in it, but by weight disentanglement, each task vector changing the output only on its own task's inputs; pretraining supplies it, and fine-tuning the model's linearisation strengthens it and improves task addition and negation

## Source

Ortiz-Jimenez, Favero & Frossard (2023), [LIT-tmphs8vv](../literature.d/LIT-tmphs8vv.md), read in
[NOTE-tmpmq65g](../notes.d/NOTE-tmpmq65g.md): §§1–7.

## The result

- **A negative result first** (§3): linearising a fine-tuned CLIP ViT
  after the fact costs single-task accuracy, so fine-tuning is not in the
  NTK regime and the NTK cannot be why task arithmetic ([THEORY-tmpup4vk](THEORY-tmpup4vk.md))
  works.
- **The condition** (§4): weight disentanglement, f(x; θ0 + Σ α_t τ_t) =
  Σ g_t(x; α_t τ_t) + g0(x), each g_t zero off task t's inputs. Its error
  is small in a region around θ0 and grows as α passes 1.
- **The method** (§5): fine-tuning f_lin directly enlarges that region.
  Task addition, ViT-B/32 71.4 → 76.5 and L/14 85.1 → 88.5; negation
  target, ViT-B/32 24.0 → 10.9, with the control held.
- **The origin** (§6.2): from random initialisation task addition gives
  3.8–6.1%, so the property comes from pretraining.

## What it does not show

- **An independent cause.** The authors note that disentanglement is
  equivalent to the task-arithmetic property. It makes the property
  measurable; it does not explain it from something else.
- **That the kernel account holds for the networks.** Eigenfunction
  localisation is a sufficient condition for kernels, shown by a
  local-energy plot on a few pairs.
- **That the gain lasts at scale.** It shrinks as models grow.
- **Anything about coordinates.** Sign conflicts ([THEORY-107](THEORY-107.md)) are not
  tested, and no layer features are measured. Cross-task linearity
  ([THEORY-tmpjlixb](THEORY-tmpjlixb.md)) measures those, and its authors read weight
  disentanglement as a consequence of it.
- **Beyond disjoint supports.** Property 1 assumes the tasks' inputs do
  not overlap.
