---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmpsyjfz](../notes.d/NOTE-tmpsyjfz.md)) from the arXiv preprint, v1 (§§1–8,
  the references and Appendix A; Appendices B–L skipped), with v3
  skimmed (abstract, introduction, Figure 1, §4.2 and §6). v3, updated
  2026-09-01, is retitled "Reading the Gate, Not the Interference:
  Output-Side Interference Measurement Does Not Track Merge Collapse",
  and adds that where merging collapses the activation cross-term is "a
  bystander, not the carrier": erasing all of it "repairs none of the
  collapse". The title here is v1's, the version the exchange cites.
  Worth reading here as an exact layerwise account of where the
  non-additive part of a two-task-vector merge lives in a language model:
  mostly transported and amplified from earlier blocks, rebuilt
  downstream when erased early, and causally effective on output
  non-additivity by its direction, not its norm. It also replicates
  cross-task linearity in LoRA-merged LMs (cosines 0.93–0.98), which bears
  on [QUESTION-318](../questions.d/QUESTION-318.md). Single-author preprint, not peer-reviewed.
title: 'Orientation, not magnitude: the causal structure of task-vector interference in merged language models'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on how model merging fails (interference between task vectors).
    A gave the title and the date and no author. Citation checked against
    the arXiv API and the v1 abstract page: Chencheng Zhu (UNSW Sydney),
    sole author, cs.LG, no journal reference; v1 submitted 2026-08-12,
    which is `published:`, v2 2026-08-24, v3 2026-09-01. arXiv title
    searches missed the work because v3 is retitled; a web search for
    the exact v1 phrase found it, and the v1 page confirmed the title.
    OpenAlex answered "Rate limit exceeded" and Semantic Scholar 429;
    neither was retried. No email address was sent to any service.
tags:
- representation-learning
- loss-landscapes
- causality
- anthology-candidate
date: '2026-11-15'
published: '2026-08-12'
arxiv: '2608.11797'
first_author: 'Zhu'
keywords:
- 'task vectors'
- 'model merging'
- 'task-vector interference'
- 'cross-term'
- 'cross-term erasure'
- 'transport'
- 'expression gating'
- 'cross-task linearity'
- 'LoRA'
implementations: []
summary: >-
  Zhu (2026). In LoRA task-arithmetic merges of two task vectors into
  Qwen2.5-1.5B, with reduced replications on Llama-3.2-1B and
  Qwen2.5-7B, the exact four-corner activation cross-term at the final
  prompt token is mostly transport of the term earlier blocks produced
  (about 65–70% of the layerwise flux, gain above 1 per late block),
  is rebuilt downstream when erased early, and reduces output
  non-additivity when erased along its own direction, while norm-matched
  wrong directions make it worse. An instruction template suppresses the
  expressed interaction of a two-vector merge while internal generation
  grows. v3, retitled, finds the cross-term a "bystander" where merging
  actually collapses. Bears on [THEORY-107](../theory.d/THEORY-107.md), as a non-coordinate account
  of interference, and on [QUESTION-318](../questions.d/QUESTION-318.md), as partial evidence for
  layerwise linearity in language models.
---
<!-- inactive-ok-file: THEORY-107 — Proposed; the coordinate account of merge interference this reading bears on -->

# LIT-tmpdc2rl: Orientation, not magnitude: the causal structure of task-vector interference in merged language models

Zhu, C. (2026). Orientation, not magnitude: the causal structure of
task-vector interference in merged language models. arXiv:2608.11797v1.
Retitled in v3 (2026-09-01): Reading the Gate, Not the Interference:
Output-Side Interference Measurement Does Not Track Merge Collapse.

## Key takeaways

*From the reading, [NOTE-tmpsyjfz](../notes.d/NOTE-tmpsyjfz.md).*

- **The quantity** (§3.2, Eq. 1): Iℓ = h^AB_ℓ − h^A0_ℓ − h^0B_ℓ + h^00_ℓ
  "is everything non-additive that has accumulated before block ℓ", read
  at "the final prompt token".
- **Transport dominates** (abstract, §4.2): the layerwise flux is
  "dominated by amplifying transport of the existing cross-term", at
  "∼65–70% in both model families": 69% on Qwen and 65% on Llama, with
  ∥Tℓ∥/∥Iℓ∥ = 1.08 per late block on Qwen and 1.14 on Llama.
- **Regrowth** (§5): "erase at depth 3 or 8 and the network rebuilds the
  cross-term essentially exactly", ρ = 1.00/0.99; ρ falls to 0.94 erasing
  at depth 14 and 0.84 at depth 20.
- **Direction, not norm** (§5, Table 2): "the sign of the effect is decided
  by direction alone". Erasure removes "roughly 19% of expressed
  interference"; a norm-matched displacement "in the wrong direction makes
  interference worse".
- **Expression gating** (§6): an instruction wrapper raises local
  generation while the same erasure finds "a 13× mean ratio" less to
  remove, because the wrapper inflates the main effect, not because the
  interaction shrinks.
- **Cross-task linearity replicated** (§7): "layerwise linearity cosines
  are 0.93–0.98 across every family".
- **v3**: where merging collapses, "the cross-term is a bystander, not the
  carrier"; and with six task vectors rather than two the template raises
  R "from 0.003 to 0.82", so the gate holds for two-vector merges only.

## Standing in the record

A, in the exchange, says the paper defines a layerwise interference term,
that propagation accounts for roughly 65–70% of it, that it can be
amplified in late blocks, that it reappears downstream when removed, that
its direction matters more than its norm, and that prompt formatting can
suppress its behavioural expression. The reader found each sentence
accurate to v1; the regrowth sentence understates it (the term returns
essentially whole after early erasure). A omits two things v3 adds: the
work is retitled away from the "orientation" framing, and the cross-term
does not carry merge collapse, so its causal effect is on output
non-additivity, not on whether the merge works. The formatting sentence
holds for two-vector merges only; at six vectors the template amplifies
the expressed interaction.

Its measure of interference is the activation cross-term, not sign
conflict in coordinates, so it does not test [THEORY-107](../theory.d/THEORY-107.md)'s account. Its
replication of cross-task linearity is the record's first evidence on
[QUESTION-318](../questions.d/QUESTION-318.md)'s layerwise half outside image classification, with the
caveats in [NOTE-tmpsyjfz](../notes.d/NOTE-tmpsyjfz.md). The source of that measurement, Zhou et al.
(2024), arXiv 2402.03660, is not held. Nor is the author's companion
paper, Zhu, Li & Cai (2026), arXiv 2608.09490, whose abstract only was
read.
