---
status: Active
status_note: >-
  read 2026-11-15 ([NOTE-tmp80eb1](../notes.d/NOTE-tmp80eb1.md)) from arXiv v3 (NeurIPS 2026), main text
  and most appendices. Worth reading for its account of why
  residual-stream persona steering loses coherence over multi-turn
  dialogue (steered states written to the KV cache are reused), and for
  its 2×2 cache-isolation test. The "duality" of the title is not stated
  or proved in the body.
title: 'Prompt-Activation Duality: Improving Activation Steering via Attention-Level Interventions'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 at the owner's request ("read and
    file"). Checked first: not held. Citation from the arXiv API and the
    PDF: Diancheng Kang, Zheyuan Liu, Ningshan Ma, Yue Huang, Zhaoxuan Tan
    and Meng Jiang, NeurIPS 2026; v1 2026-05-11, which is `published:`,
    then v2 2026-05-14 and v3 2026-11-10. The v3 PDF abstract narrows the
    claim to "prompt-localizable behaviors"; the arXiv listing's abstract
    was not updated. Read by a delegated reader; the filer string-matched
    every quotation used.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2026-05-11'
arxiv: '2605.10664'
first_author: 'Kang'
keywords:
- 'activation steering'
- 'persona vectors'
- 'KV cache'
- 'multi-turn dialogue'
- 'attention decomposition'
- 'coherence'
implementations: []
summary: >-
  Kang, Liu, Ma, Huang, Tan & Jiang (2026), NeurIPS. Residual-stream
  persona steering (Chen et al.'s persona vectors) loses coherence over
  10-turn dialogue, while a system prompt under the same protocol does
  not. The authors attribute part of the loss to KV-cache contamination:
  steered token states are cached and reused, so the perturbation
  compounds. A 2×2 test, injecting or not and with a steered or clean
  cache, shows a clean cache raising coherence by 15 points and cutting
  repetition. Injection itself remains the larger cause. GCAD takes its
  steering vector from the system prompt's cropped contribution to
  attention and gates it per token. On Qwen2.5-7B (one judge, point
  estimates) it moves 10-turn coherence drift from −18.6 to −1.9.
---

<!-- inactive-ok-file: THEORY-1334 — Proposed; the persona-direction THEORY the reading bears on -->

# LIT-tmpi20ed: Prompt-Activation Duality: Improving Activation Steering via Attention-Level Interventions

Diancheng Kang, Zheyuan Liu, Ningshan Ma, Yue Huang, Zhaoxuan Tan and Meng
Jiang, "Prompt-Activation Duality: Improving Activation Steering via
Attention-Level Interventions", NeurIPS 2026; arXiv:2605.10664.

## Key takeaways

*From the reading, [NOTE-tmp80eb1](../notes.d/NOTE-tmp80eb1.md).*

- **The failure.** "We identify KV-cache contamination as a key failure
  mode", and "Since prompt-only control remains stable under the same
  protocol (Figure 1), the problem is not long context alone."
- **The test.** Cleaning the cache under steering raises coherence (51.2
  against 36.1) and nearly removes repetition loops, "so steered cache
  states are one cause of the collapse". But "The trait thus needs a
  steered cache": cleaning also cuts trait expression by 13 points.
- **The method's account.** "The real problem is what residual steering
  writes into the cache", so GCAD changes what is written: a cropped,
  gated, attention-level signal taken from the system prompt.
- **The "duality"** is in the title only. The body claims that prompting
  and steering are "closely linked by construction", and supports
  attention as the trait-bearing channel empirically.

## Standing in the record

Filed on 2026-11-15 at the owner's request. It attacks the steering
method of Chen et al.'s Persona Vectors ([LIT-1998](LIT-1998.md), [NOTE-1524](../notes.d/NOTE-1524.md)), and bears
on the record's multi-turn persona dynamics ([LIT-1991](LIT-1991.md), [THEORY-1339](../theory.d/THEORY-1339.md),
[QUESTION-443](../questions.d/QUESTION-443.md)) and on [THEORY-1334](../theory.d/THEORY-1334.md). The recipe is machine-learning practice
and carries the `anthology-candidate` flag. Its account of how
interventions persist through cached states is filed here.
