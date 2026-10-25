---
status: Active
status_note: >-
  read 2026-10-25 (NOTE-tmphq8v2) in full, from arXiv v2, the TMLR
  version; worth reading for two ways of letting separately trained
  low-rank operators act on one denoising trajectory without merging them,
  by turns (LoRA Switch) or by averaging their guided predictions (LoRA
  Composite), for GPT-4V and human judgements preferring both to weight
  merging as LoRAs are added (THEORY-tmpg6v1v), and for its ablation in
  which, at equal shares of steps, the switching interval and the LoRA
  acting first change the result (THEORY-tmp6s2xi). Read it knowing that
  the merging baseline's summed update grows with the number of LoRAs,
  which the design does not separate from the methods' idea; that the two
  methods are never compared head to head by the judge; that the judge
  has a positional bias of about ten points and correlates 0.45 with two
  annotators; and that §5.1.1 attributes LoRA Switch's scores to LoRA
  Composite.
title: 'Multi-LoRA Composition for Image Generation'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed, not read. At U46 of the exchange (the continuation of "Review
    PR 327 Improvements", shared at
    https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824) the
    reply says its next experiment "would test something more distinctive
    than multi-LoRA image composition", and cites no work; the record's
    reading of those turns named this one from memory, and the lookup
    confirmed it. Checked on 2026-10-25 against the arXiv record: Ming
    Zhong, Yelong Shen, Shuohang Wang, Yadong Lu, Yizhu Jiao, Siru Ouyang,
    Donghan Yu, Jiawei Han and Weizhu Chen, arXiv 2402.16843, v1 submitted
    26 February 2024, which is `published:`; v2 of 19 November 2024 gives
    Transactions on Machine Learning Research (TMLR), 2024. The summary
    follows the arXiv abstract.
- version: 2
  date: '2026-10-25'
  note: >-
    Read in full (NOTE-tmphq8v2), from arXiv v2, which is headed as the
    TMLR (11/2024) version. Status Deferred → Active. THEORY-tmpg6v1v (the
    main comparison) and THEORY-tmp6s2xi (the switching ablation,
    Proposed) filed. The OpenReview forum of the TMLR review is added as
    the URL. The summary is checked against the reading and kept.
tags:
- compositionality
- anthology-candidate
date: '2026-10-25'
published: '2024-02-26'
arxiv: '2402.16843'
url: 'https://openreview.net/forum?id=25FT0DqhVZ'
first_author: 'Zhong'
keywords:
- 'LoRA'
- 'multi-LoRA composition'
- 'LoRA Switch'
- 'LoRA Composite'
- 'text-to-image'
- 'ComposLoRA'
implementations: []
summary: >-
  Zhong et al. (2024). Composing several LoRAs in a text-to-image model
  gets harder as their number grows. Taking a decoding-centric view, the
  paper gives two training-free methods: LoRA Switch alternates between
  LoRAs at each denoising step, and LoRA Composite incorporates all of
  them at every step to guide synthesis. On ComposLoRA, a testbed of 480
  composition sets, a GPT-4V-based evaluation finds both better than the
  prevalent baseline, most clearly as the number of LoRAs grows
  (abstract).
---
<!-- inactive-ok-file: THEORY-tmp6s2xi — Proposed; this reading's account of the switching ablation, its sample unreported -->
# LIT-tmpxsvgv: Multi-LoRA Composition for Image Generation

Zhong, M., Shen, Y., Wang, S., Lu, Y., Jiao, Y., Ouyang, S., Yu, D., Han,
J. & Chen, W. (2024). Multi-LoRA composition for image generation.
*Transactions on Machine Learning Research*. arXiv:2402.16843.

Read in full on 2026-10-25 (NOTE-tmphq8v2). The main comparison is held
in THEORY-tmpg6v1v and the switching ablation in THEORY-tmp6s2xi. LoRA
Composite turns out to be MultiDiffusion's per-step average
(LIT-tmp03agp, THEORY-tmpt2q0g) with every mask full and LoRA-modified
models in place of prompts.

## Why this is here

Filed as the work behind the genre U46 named. At U46 the reply gave its
perspectives separately learned denoising capabilities (LoRA adapters) and
combined their contributions step by step; LoRA Switch and LoRA Composite
are per-step versions of that combination, without the learned allocation
of influence that the exchange wanted to add. The record holds none of the
LoRA literature. It bears on [QUESTION-tmpu6zq7](../questions.d/QUESTION-tmpu6zq7.md), a population of denoisers being
one of the mechanisms of influence it asks about, and on the
audited-governance study [CASE-tmpjmerx](../cases.d/CASE-tmpjmerx.md), whose arms decide which specialist
acts. Filed for that question, not as an instruction for practice.
