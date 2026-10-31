---
status: Proposed
promote_when: >-
  Independent replications, with several seeds per scale and reported
  variances, in which removing the data-target residual from the gradient
  reaching the trunk lowers next-token loss against standard MTP, and the
  residual's signal-to-noise ratio falls relative to the KL component's,
  at scales beyond 1.2B. A result in which the gain disappears across
  seeds, or reverses with scale, would count against it; further single
  runs at the same scales would not settle it.
title: 'In multi-token-prediction pre-training at 167M to 1.2B parameters, the part of the MTP gradient that pulls toward the sampled target carries about four-fifths of the MTP gradient reaching the shared trunk with roughly a quarter of the signal-to-noise ratio of the self-distillation part, and removing it from the trunk improves next-token loss, speculative decoding and zero-shot accuracy by small margins'
version: 1
tags:
- learning-theory
- representation-learning
date: '2026-10-31'
source:
- LIT-tmpu9af8
summary: >-
  Teoh (2026), LIT-tmpu9af8, §6 Figs. 3–4 and Tables 2–6; read in
  NOTE-tmp8ljm4. Proposed: one run per scale, four scales, no seeds or
  variances, margins of one to two percent. It does not show that
  data-anchored correction is dispensable: the output head keeps it, and
  the paper attributes the explicit-KL variant's weaker head to its
  absence there.
---

# THEORY-tmpjc4k3: In multi-token-prediction pre-training at 167M to 1.2B parameters, the part of the MTP gradient that pulls toward the sampled target carries about four-fifths of the MTP gradient reaching the shared trunk with roughly a quarter of the signal-to-noise ratio of the self-distillation part, and removing it from the trunk improves next-token loss, speculative decoding and zero-shot accuracy by small margins

## Source

Teoh (2026), LIT-tmpu9af8, §6.1–6.3, Figs. 3–6, Tables 2–6 and
Appendix E, pp. 7–12 and 21–23 of arXiv 2610.38331v1; read in
NOTE-tmp8ljm4.

## What was actually shown

On frozen checkpoints of LLaMA-style models (167M, 332M, 689M, 1.2B;
K = 3 DeepSeek-style heads), the residual component had about 4× lower
gradient SNR than the KL component, the ratio widening from 4.1× to 4.6×
with scale (Fig. 3). Its share of the MTP gradient reaching the trunk,
measured as the projection ⟨g_hard, g_res⟩ / ‖g_hard‖², was about 80% at
every scale. A unit hidden-state step along it raised NTP loss; one along
the KL component lowered it (Fig. 4a). Trained with the residual removed,
models reached lower NTP loss at every scale and lower MTP loss from 689M
(Fig. 4b–c). They had higher acceptance length in every
speculative-decoding cell (Table 2) and higher average zero-shot accuracy
(Table 3), and led on seven of eight fine-tuning cells at 1.2B (Table 4).
At 332M the advantage held across λ_MTP ∈ {0.25, …, 1} and K ∈ {3, …, 8}
(Fig. 5).

What could have come out otherwise: the residual could have carried
useful signal that the trunk needed, in which case removing it would have
raised NTP or MTP loss.

## What this does not say

- **That correction against the data is unnecessary.** Soft-MTP keeps
  cross-entropy at the shared output head. The explicit-KL variant, which
  removes it there as well, had a lower-rank readout (321 against 437,
  Fig. 6) and was weaker on most metrics (Table 6).
- **That the effect grows with scale beyond the tested range.** Four
  points, one run each.
- **That the SNR gap causes the gain.** The two are reported side by
  side; no intervention isolates the mechanism.
- **Anything about other self-distillation settings.** The finding is
  about MTP heads with a shared head and a same-model teacher.
