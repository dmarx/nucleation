---
status: Active
status_note: >-
  skimmed 2026-11-15 ([NOTE-tmp3bv7o](../notes.d/NOTE-tmp3bv7o.md)) from the arXiv PDF, v3, for A's one
  use only: the abstract, the §3.1 action space, the §3.3 comparison with
  chain of thought (with Table 2) and the passage on outdated labels around
  Fig. 4. The decision-making half (ALFWorld, WebShop), the rest of §2–3
  and the appendices were not read. Worth reading here as a plain case of
  improving the signal without touching the interpreter ([CLAIM-118](../claims.d/CLAIM-118.md)): a
  queried Wikipedia API supplies facts in context, with the weights
  unchanged.
title: 'ReAct: Synergizing Reasoning and Acting in Language Models'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and skimmed on 2026-11-15 from the owner's pasted
    continuation of the ChatGPT exchange "Explain String Theory", in A's
    turn on a model querying an external source for a fact it lacked.
    Citation checked on the arXiv API: Shunyu Yao, Jeffrey Zhao, Dian Yu,
    Nan Du, Izhak Shafran, Karthik Narasimhan and Yuan Cao (Princeton and
    Google Research); v1 submitted 2022-10-06, which is `published:`; v3
    (2023-03-10), the ICLR camera-ready version, is the copy read. The PDF
    header reads "Published as a conference paper at ICLR 2023". OpenAlex
    and Semantic Scholar both refused with HTTP 429 and were not retried.
    No email address was sent to any service. The record held no LIT for
    this work.
tags:
- agency
- information-retrieval
- anthology-candidate
date: '2026-11-15'
published: '2022-10-06'
arxiv: '2210.03629'
first_author: 'Yao'
keywords:
- 'reasoning and acting'
- 'language models'
- 'chain-of-thought'
- 'tool use'
- 'HotpotQA'
- 'Fever'
- 'ALFWorld'
- 'WebShop'
implementations:
- https://react-lm.github.io
summary: >-
  Yao et al. (2023), arXiv:2210.03629, ICLR 2023. Prompting a model to
  interleave reasoning traces with actions on a simple Wikipedia API lets
  it ground answers in retrieved facts, reducing the hallucination of
  chain-of-thought on HotpotQA and Fever and recovering facts newer than a
  dataset's labels; ReAct alone beat CoT on Fever and slightly lagged it on
  HotpotQA. Here for A's single use, a model querying a source that supplies
  a fact it lacked, and for [CLAIM-118](../claims.d/CLAIM-118.md). Skimmed; no THEORY filed.
---
<!-- inactive-ok-file: NOTE-tmp3bv7o — Skimmed; the reading filed in the same contribution -->
<!-- inactive-ok-file: THEORY-591 THEORY-1773 — Proposed; neighbouring readings on tools in cognition and on tool-using agents -->

# LIT-tmpygfnl: ReAct: Synergizing Reasoning and Acting in Language Models

Yao, S., Zhao, J., Yu, D., Du, N., Shafran, I., Narasimhan, K. & Cao, Y.
(2023). ReAct: Synergizing Reasoning and Acting in Language Models.
*International Conference on Learning Representations* (ICLR 2023).
arXiv:2210.03629.

## Key takeaways

*From the skim, [NOTE-tmp3bv7o](../notes.d/NOTE-tmp3bv7o.md); the knowledge-task half only.*

- **Actions gather information** (abstract): "actions allow it to interface
  with and gather additional information from external sources such as
  knowledge bases or environments"; ReAct "overcomes prevalent issues of
  hallucination and error propagation in chain-of-thought reasoning by
  interacting with a simple Wikipedia API".
- **Mixed against CoT** (§3.3): "ReAct outperforms CoT on Fever (60.9 vs.
  56.3) and slightly lags behind CoT on HotpotQA (27.4 vs. 29.4)". In Table
  2, hallucination is CoT's major failure mode (56%), and 0% of ReAct's.
- **New facts** (around Fig. 4): where a HotpotQA label was outdated, "Only
  ReAct is able to retrieve up-to-date information from the Internet and
  provide a reasonable answer."

## Standing in the record

A's single use is accurate: a model can query an external source that
supplies a previously unknown factual answer, and the outdated-label case
shows a fact absent from the model's training-time knowledge. The reader's
caution: if A leans on ReAct for performance, ReAct alone is slightly worse
than CoT on HotpotQA, and the paper's best results combine it with CoT-SC.

Nearby held entries: [THEORY-1773](../theory.d/THEORY-1773.md) (a tool-use agent benchmark) and
[THEORY-591](../theory.d/THEORY-591.md) (Adams and Aizawa against counting tools as part of cognition).
Its prompting method is ML practice and belongs to the anthology
([ADR-048](../decisions.d/ADR-048.md)); hence the flag.
