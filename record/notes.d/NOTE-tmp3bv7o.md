---
status: Skimmed
paper: LIT-tmpygfnl
title: 'Yao et al. — ReAct, for one use'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Skimmed on 2026-11-15 from arXiv:2210.03629v3, https://arxiv.org/pdf/2210.03629,
    text by pdftotext, for A's single use only. Read: the abstract, the
    §3.1 action space, the §3.3 comparison of ReAct with CoT (Table 2) and
    the passage on outdated labels around Fig. 4. Not read: §2, the rest of
    §3, the decision-making sections (ALFWorld, WebShop) and the
    appendices. The filer rechecked every quote below against the
    downloaded text.
date: '2026-11-15'
summary: >-
  ReAct interleaves reasoning traces with actions on a Wikipedia API;
  retrieved facts reduce chain-of-thought's hallucination and can be newer
  than a dataset's labels. Skimmed for one use: a fact supplied in context
  with the weights unchanged, a plain case of improving the signal and not
  the interpreter (CLAIM-118).
---
<!-- inactive-ok-file: LIT-tmpygfnl — new entry filed in the same contribution -->
<!-- inactive-ok-file: CLAIM-576 THEORY-591 THEORY-1773 — Proposed; the claim this reading bears on weakly and two neighbouring readings -->

# NOTE-tmp3bv7o: Yao et al. — ReAct, for one use

## Contribution

A prompting method in which a language model alternates free-text
reasoning with actions in an environment. On HotpotQA and Fever the
actions are three calls to a simple Wikipedia API: search[entity] returns
the first five sentences of a page, lookup[string] the next sentence
containing the string, and finish[answer] ends the task (§3.1).

## Key insight

Reasoning alone works only from what the model already holds; letting it
act brings new information into the context, which the reasoning then
uses.

## Assumptions

Few-shot prompting of a frozen model; the API returns Wikipedia text;
success is exact match (HotpotQA) or label accuracy (Fever).

## Key results

- **Abstract**: "actions allow it to interface with and gather additional
  information from external sources such as knowledge bases or
  environments"; ReAct "overcomes prevalent issues of hallucination and
  error propagation in chain-of-thought reasoning by interacting with a
  simple Wikipedia API".
- **§3.3**: "ReAct outperforms CoT on Fever (60.9 vs. 56.3) and slightly
  lags behind CoT on HotpotQA (27.4 vs. 29.4)". Table 2, a hand labelling
  of 200 sampled HotpotQA trajectories (50 correct and 50 incorrect from
  each method): hallucination is 56% of
  CoT's failures and 0% of ReAct's. The best methods combine the
  two, "ReAct → CoT-SC and CoT-SC → ReAct".
- **Around Fig. 4**: on an outdated HotpotQA label, "Only ReAct is able to
  retrieve up-to-date information from the Internet and provide a
  reasonable answer."

## Concepts

Interleaved reasoning and acting; action space; grounding; hallucination;
CoT-SC fallback.

## Bearing on the record

- **CLAIM-118 (signal and interpreter)**: the retrieved observation is a
  clear case of improving the signal, not the interpreter: the weights are
  unchanged and the new fact arrives in context. A standard example that
  fits the claim's distinction; it does not test it.
- **CLAIM-576**: weakly. A tool that supplies information is an
  observational capability in the claim's sense, which makes an existing
  possibility discoverable.
- **THEORY-591**: if A's point is that a queried source becomes part of the
  cognitive system, Adams and Aizawa's marks of cognition argue against
  counting it so; CLAIM-118's line places it in the signal either way.

## Limitations

A skim for one use. The decision-making half, the ablations and the
appendices were not read, so the paper's central account of reasoning and
acting as synergistic across both kinds of task is not assessed here.
