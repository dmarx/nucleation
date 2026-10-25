---
status: Deferred
status_note: >-
  filed 2026-10-25, not read. Registered as prior art for turns U45 and
  U46 of the owner's exchange of 2026-10-24/25, which named "multi-LoRA
  image composition" at U46 without citing a work. No NOTE is filed.
title: 'Multi-LoRA Composition for Image Generation'
version: 1
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
tags:
- compositionality
- anthology-candidate
date: '2026-10-25'
published: '2024-02-26'
arxiv: '2402.16843'
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
# LIT-tmpxsvgv: Multi-LoRA Composition for Image Generation

Zhong, M., Shen, Y., Wang, S., Lu, Y., Jiao, Y., Ouyang, S., Yu, D., Han,
J. & Chen, W. (2024). Multi-LoRA composition for image generation.
*Transactions on Machine Learning Research*. arXiv:2402.16843.

Not read. The summary is drawn from the abstract or from what the work
is standardly cited for. A reading should check it first.

## Why this is here

Filed as the work behind the genre U46 named. At U46 the reply gave its
perspectives separately learned denoising capabilities (LoRA adapters) and
combined their contributions step by step; LoRA Switch and LoRA Composite
are per-step versions of that combination, without the learned allocation
of influence that the exchange wanted to add. The record holds none of the
LoRA literature. It bears on {{F-Q-INFL}}, a population of denoisers being
one of the mechanisms of influence it asks about, and on the
audited-governance study {{F-K-AUDIT}}, whose arms decide which specialist
acts. Filed for that question, not as an instruction for practice.
