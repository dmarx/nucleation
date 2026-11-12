---
status: Read
paper: LIT-2294
title: 'Li, Naito and Shirado — Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://raw.githubusercontent.com/mlresearch/v306/main/assets/li26ej/li26ej.pdf.
    A delegated reader drafted the reading; quotations were rechecked by
    script against the downloaded copy, and any that did not match were kept
    as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  The paper adapts the Hidden Profile paradigm from social psychology into a
  65-task benchmark for multi-agent LLMs. In each task shared facts favour a
  wrong option and facts distributed one per agent jointly support the right
  one; agents are not told the information is asymmetric. Tasks are admitted
  only if single agents with full information get at least 80% and agents
  with the hidden profile at most 20% before discussion.
---
<!-- inactive-ok-file: CASE-tmpiocs1 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: LIT-1399 — Unavailable; cited for what each holds, not as settled -->

# NOTE-tmpr7r0u: Li, Naito and Shirado — Systematic Failures in Collective Reasoning under Distributed Information in Multi-Agent LLMs

## Contribution

A controlled benchmark that separates failures of pooling distributed information from failures
of individual reasoning, by construction, and a diagnosis that the failure lies in surfacing
unshared facts, not in integrating them once surfaced.

## Key results

1. Headline gap (abstract): "multi-agent LLMs achieve only 30.1% accuracy under distributed information, compared to 80.7% accuracy for single agents given complete information".
2. Mechanism (abstract): agents "fail to reason about what others might know but have not yet expressed, leading to premature convergence on shared evidence".
3. Group size (§6.1, Table 4): "improvement from communication drops from +0.348 at N = 3 to +0.006 at N = 7".
4. Extended discussion (§6.1, Table 2): performance peaks at 15 rounds and declines at 20, "suggesting extended discussion reinforces incorrect consensus rather than promoting exploration".
5. Where it fails (§6.3, Table 6): Reveal-All raises accuracy to 92.6% (GPT-4.1) and 98.2% (Gemini-2.5-Flash); "the failure lies in surfacing information, not reasoning over it". The Secretary arm (a passive per-round summary of disclosed facts) gives 0.241 (GPT-4.1) and 0.713 (Gemini-2.5-Flash): "Passive summarization yields more limited and model-dependent gains".
6. Dissent (§6.2, Table 5): for GPT-4.1 one adversarial agent of four takes accuracy from 0.233 to 0.492, but "Simple dissent hurts Gemini-2.5-Flash" (0.889 to 0.306).
7. Structured protocol (§6.4, Table 7): in the Exchange stage "each agent shares 1–2 decision-relevant facts and gives one reason the current front-runner may be incorrect"; baseline to structured: GPT-4.1 0.037 to 0.800, Gemini-2.5-Flash 0.173 to 0.727, Flash-Lite 0.043 to 0.743. Evaluated on **18 tasks**, 5 runs each, 4 agents, not on all 65.
8. Human verification (§3.2): human groups pre-discussion 0.125, post 0.385, full profile 0.604.

## Assumptions

- Ground truth is fixed and every task is solvable by one agent given everything; the only
  obstacle is distribution. Tasks were generated and filtered with GPT-4.1, so the benchmark's
  difficulty is partly defined against that model.
- Agents are not told information is asymmetric; "Informing Asymmetry" prompting is a separate arm (0.367).
- The protocol and the bottleneck ablations use an 18-task subset; the headline 30.1/80.7 uses all tasks and 15 models.

## Concepts

Hidden profile; shared-information bias; latent information asymmetry; information exploration vs
integration (citing March 1991); premature convergence; Reveal-All, Secretary, structured dissent,
Exchange-then-Decide protocol.

## Bearing on the record

[QUESTION-tmpxq2sb](../questions.d/QUESTION-tmpxq2sb.md) quotes A39: agents "achieved 30.1% accuracy, versus 80.7% for single agents
given complete information. A lightweight structured communication protocol improved
performance." **Accurate**, with two qualifications one should carry: (a) the protocol result
is on 18 of the 65 tasks with three models, not the benchmark as a whole; (b) the paper itself
contains a shared-summary arm (Secretary) whose gains are small and model-dependent, which is the
nearest published analogue of "a shared record" and is a baseline the question must also beat.
[CASE-tmpiocs1](../cases.d/CASE-tmpiocs1.md)'s "65 hidden-profile problems" is correct.

- **[QUESTION-tmpxq2sb](../questions.d/QUESTION-tmpxq2sb.md)** (does a shared typed governed record help beyond a structured
  protocol, and at which stage): **supports the framing and sharpens it.** The paper localises the
  failure at what [CLAIM-403](../claims.d/CLAIM-403.md) calls admission (surfacing), not uptake: once disclosed, facts are
  integrated. So a record helps only if it changes what gets surfaced; a record that holds only
  what agents choose to post is close to the Secretary arm. The baseline is three-fold: chat,
  Secretary (passive shared summary), Exchange-then-Decide.
- **[CASE-tmpiocs1](../cases.d/CASE-tmpiocs1.md)** (the proposed adaptation): **supports**; the benchmark's arms and the
  18-task subset are the natural comparison set; the record arm should be compared to Secretary,
  not only to chat and the protocol. Group-size results (Table 4) argue for varying N.
- **[CLAIM-403](../claims.d/CLAIM-403.md)** (separable stages admission, recognition, credibility, uptake): **supports** as an
  instance: Reveal-All shows admission is the binding stage in this setting.
- **[CLAIM-346](../claims.d/CLAIM-346.md)** (feasibility, aggregation, epistemic coordination independent): **supports** as an
  instance of epistemic coordination failing with aggregation intact.
- **[LIT-1399](../literature.d/LIT-1399.md)** (hidden-profile meta-analysis, held): the paper drew its five adapted scenarios
  from the studies Lu et al. (2012) summarises; consistent.

## Limitations

Synthetic, multiple-choice tasks with one correct option; GPT-4.1-generated and filtered;
protocol on a subset; no human-AI mixed groups; no persistent shared memory arm beyond Secretary.
