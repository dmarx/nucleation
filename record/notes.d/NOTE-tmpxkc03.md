---
status: Read
paper: LIT-2290
title: 'Yin et al. — Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2410.04444. A delegated
    reader drafted the reading; quotations were rechecked by script against
    the downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  Gödel Agent is an LLM agent that can read and rewrite its own running
  code, including the code that analyses and modifies itself, by inspecting
  Python runtime memory and monkey patching; its main loop is a recursive
  function so that rewritten logic takes effect in the next call. Given only
  an environment description, a feedback mechanism and a chain-of-thought
  starting policy, it improves its task policy on DROP, MGSM, MMLU and GPQA,
  matching or beating hand-designed agents and Meta Agent Search (a
  meta-learning approach with a fixed meta-algorithm). In 100 optimisation
  trials on MGSM it often makes harmful edits along the way, occasionally
  kills its own improvement loop, and ends worse than its starting policy in
  14% of trials.
---
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpxkc03: Yin et al. — Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement

## Contribution

A working implementation of an agent whose self-improvement routine is itself within the scope of
its self-modification, demonstrating feasibility rather than state of the art.

## Key results

1. Claim (§1): it "can analyze and modify its own code, including the code for analyzing and modifying itself".
2. Implementation (§1): it retrieves its code "in the runtime memory and modify it by monkey patching".
3. Results (§5.3): Under the same setting, Gödel Agent achieves either optimal or comparable results to Meta Agent Search across all tasks; on MGSM it "outperforms it by 11%".
4. Robustness (§6.2): in 100 MGSM trials it makes erroneous changes "which can result in either terminating unexpectedly (4%) or experiencing temporary performance drops (92%)"; "Only in 14% of trials, optimization ultimately failed".
5. Self-damage (§6.2): unexpected terminations are rare and typically occur when Gödel Agent modifies its recursive improvement module, making further self-optimization impossible.
6. Scope (Limitations): "The experiments presented in this paper are intended to demonstrate the feasibility of recursive self-improvement."
7. Opacity (Limitations): "a system capable of complete self-referential at the outset may lose this capability as it evolves".

## Assumptions

Benchmark accuracy as the sole objective signal, supplied by an external evaluator the agent does
not modify; a strong closed LLM (GPT-4o/GPT-3.5 per Table 1 variants) as the reasoning engine;
four initial supportive tools (thinking before acting, error handling, code running, LLM calls).

## Concepts

Self-referential agent; recursive self-improvement; runtime-memory self-inspection
("self-awareness" in a non-philosophical sense, footnote 1); monkey patching; hand-designed vs
meta-learning-optimized vs self-referential agents.

## Bearing on the record

[QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md) lists it among "prior art on self-improving agents", unread. **Accurate.** It
does **not** run the matched-start comparison of an earlier and a later improver that the
question requires; its evidence is the final task policy's score. The paper's own robustness
result (5 above) is the most relevant finding for the question.

- **[QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md)**: **leaves the improver question open** (no earlier-vs-later improver
  comparison) and **bears on the correctability half**: an agent that can edit its own
  improvement module can disable it, and the paper reports that this is how its terminations
  happen. Its recovery from temporary drops relies on reverting to a previous best, with
  the external evaluator unchanged.
- **[CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md)** (damage to the collective's own diagnostic machinery): **supports the premise**
  with an observed case of self-inflicted damage to the improver; not a designed lesion.
- **[QUESTION-388](../questions.d/QUESTION-388.md) / [CLAIM-485](../claims.d/CLAIM-485.md)**: **leaves open**: the agent rewrites its procedures, not the
  objective or the evaluator, so it is evidence about reprogramming, not revision of governing
  standards.

## Limitations

Reasoning benchmarks with closed answers; baselines' numbers taken from Hu et al. (2024) (Table 1
footnote); one robustness study (MGSM); no cross-domain transfer of the improver.
