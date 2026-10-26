---
status: Proposed
promote_when: >-
  A comparison of fine-tuning's circuit change against a null at the same
  edge budget: the change between circuits of two fine-tuning runs from
  different seeds, or of the same checkpoint on resampled circuit data,
  or of a reshuffle that keeps node importances. The account is confirmed
  if fine-tuning's edge change exceeds the null's while its node change
  does not, and if the kept nodes are shown to do the same work after
  fine-tuning (by patching or ablation), not merely to be listed again.
  It is rejected if the null produces the same node–edge contrast, or if
  the kept nodes' function changes as much as the edges. More tables of
  node and edge change rates without a null cannot settle it, since a
  fixed fraction of a dense graph's edges produces the contrast by itself.
title: 'When a pretrained language model is fine-tuned on a task it initially fails, it acquires the task mainly by reconnecting components it already has rather than by recruiting new ones: the circuits found before and after keep most of their nodes and change most of their edges, as Wang, Hu, Du, Cheng, Wang and Zou propose from LoRA fine-tuning of Pythia-1.4B on arithmetic'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Proposed from NOTE-tmplotfq. The change rates are the paper's
    Table 5. The null-model simulation and the reason the rates alone do
    not settle the account are the record's.
tags:
- representation-learning
- learning-theory
date: '2026-10-26'
source:
- LIT-tmpf4hwb
summary: >-
  Wang et al. (2025), [LIT-tmpf4hwb](../literature.d/LIT-tmpf4hwb.md), read in [NOTE-tmplotfq](../notes.d/NOTE-tmplotfq.md). Their EAP-IG
  circuits (top 5% of edges) change edges 2.8–4.3 times as much as nodes
  over LoRA fine-tuning on five arithmetic tasks. A record simulation
  shows that a fixed edge budget on a transformer-sized graph gives the
  same contrast when only edge-level noise is resampled, so the counts do
  not yet show reorganization. Fine-tuning only, one model for most
  results, arithmetic only.
---
<!-- inactive-ok-file: CLAIM-329 — Proposed; the claim this account bears on, cited as open -->

# THEORY-tmpoirdq: When a pretrained language model is fine-tuned on a task it initially fails, it acquires the task mainly by reconnecting components it already has rather than by recruiting new ones: the circuits found before and after keep most of their nodes and change most of their edges, as Wang, Hu, Du, Cheng, Wang and Zou propose from LoRA fine-tuning of Pythia-1.4B on arithmetic

## Source

Wang, Hu, Du, Cheng, Wang and Zou (2025), ICML 2025, arXiv:2502.11812,
[LIT-tmpf4hwb](../literature.d/LIT-tmpf4hwb.md), read in full in [NOTE-tmplotfq](../notes.d/NOTE-tmplotfq.md): §4 and Appendices D, E, F, G,
H and K. The conclusion's words: "fine-tuning primarily modifying edges
rather than merely introducing new components to form new circuits".

## What is asserted, and by whom

The authors assert that fine-tuning on a task the model fails "creates new
circuits through significant reconfiguration of connections among
components", against earlier findings that fine-tuning on tasks already
done well adds components to an existing circuit.

**The measurement** (Table 5). Average change between consecutive
checkpoints, relative to the initial circuit's size:

| task | nodes | edges | ratio |
|---|---|---|---|
| Add/Sub (100) | 17.4% | 69.5% | 4.0 |
| Mul/Div | 23.2% | 76.9% | 3.3 |
| Sequence | 24.2% | 67.9% | 2.8 |
| LCM | 23.9% | 80.4% | 3.4 |
| Function | 15.4% | 65.8% | 4.3 |

The contrast holds under AdaLoRA, IA3 and full fine-tuning, and for
GPT-Neo-2.7B and OPT-6.7B on Add/Sub.

## What the record holds toward it

**Why the counts alone do not settle it (the record's).** A circuit here
is the top 5% of edges of a dense layered graph. The record built a graph
the size of Pythia-1.4B's (24 layers of 16 heads and an MLP, plus input
and logits: 410 nodes, 80,581 forward edges), gave each edge a score equal
to a fixed node importance at each end times independent log-normal noise,
and compared the top-5% circuits from two independent draws of the noise
only. The node sets differed by 5.1% and the edge sets by 129.7% (counted
as the symmetric difference over the circuit's size). With uniform random
scores the node sets did not differ at all. So, with node importances held
fixed, resampling edge-level noise yields "nodes kept, edges changed" by
itself. The paper's robustness analysis (edge Jaccard under data
perturbation, higher for trained than for random models) bounds the noise
in its circuits, but it is not a comparison at the same budget, and the
paper reports none.

**What does support it.** The circuits are faithful at every checkpoint,
the change concentrates in the middle layers rather than spreading
uniformly, and the edges that change most predict where extra LoRA rank
helps (CircuitLoRA beats random critical layers in every column of Tables
1 and 4). That last is evidence that the changed edges are not noise.

## What would confirm or reject it

The promote_when above.

## Bearing

- [QUESTION-tmpivbso](../questions.d/QUESTION-tmpivbso.md) cites this work for relations reorganizing while
  components stay. As filed, it is the hypothesis, not the finding, and
  the null above is the test that question's own design would also need.
- [CLAIM-329](../claims.d/CLAIM-329.md): "the same components" is judged here by resemblance (the node
  appears again), not by what the component does or where its function
  came from.
