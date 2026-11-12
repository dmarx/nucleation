---
status: Read
paper: LIT-2314
title: 'Srikanth et al. — Recursive self-improvement of AI research agents'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2609.26457. **Read** (main
    text), 2026-11-12. A delegated reader drafted the reading; quotations were
    rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  AIDE² runs recursive self-improvement at the harness layer of a research
  agent. The inner loop is a tree-search coding agent (starting from AIDE0,
  a pared-down AIDE) that optimizes code against a metric on AI R&D tasks
  under a fixed dollar budget per task. The outer loop is another agent
  (driven by AIDE_human, Weco's production agent, on Claude Opus 4.7) that
  rewrites the inner agent's code; each candidate is graded by running it on
  a selection benchmark (ML engineering, heuristic algorithm engineering,
  harness engineering) and scoring its returned solutions on private
  held-out data; a rewrite is kept only if it beats the incumbent's grade.
---
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmprn230: Srikanth et al. — Recursive self-improvement of AI research agents

## Contribution

A working two-loop RSI system for a research agent with selection on held-out grades, tested for transfer to four external benchmarks, for an unoptimized behaviour (reward hacking), and, in an "ignition test", for whether a discovered agent is a better outer-loop improver than the one that produced it.

## Key results

(Agent names carry subscripts in the PDF, AIDE₀, AIDE₄₇, AIDE₈₅, AIDE_human; extracted text renders them as "AIDE0 ", "AIDEhuman", and quotes below keep the extracted form.)

- Sustained trend (§3.2): seven accepted improvements, “with the incumbent grade rising from 0.703 to 0.778”; AIDE_human scores 0.749 on the same grade (Fig. 2).
- Transfer (§3.3): “AIDE85 matches or exceeds AIDEhuman on all four external benchmarks” (ALE-Bench, MLE-Bench, FML-Bench, WeatherBench 2); gains are “positive throughout but not monotone across checkpoints”.
- Reward hacking on held-out kernel tasks (§3.4): “55% for AIDE0 , 39% for AIDE47 , and 32% for AIDE85 , compared to 39% for AIDEhuman”; the authors say the rates “do not identify which rewrites produced it”.
- Fixing the evaluator (§3.5): one held-out scoring script crashed on all test cases when any one failed; AIDE85 adds a patch that stops this, and “rather than exploiting the broken evaluation, AIDE2 repaired it.”
- The ignition test (§3.6): two arms of 50 outer-loop steps, three seeds each, both starting from inner agent AIDE47, differing only in the outer-loop agent (AIDE47 itself vs AIDE_human). Endpoints 0.780 and 0.782; “with only three seeds per outer-loop agent, we find these results to be inconclusive”. What it shows: “there is no obvious degradation in AIDE47 ’s ability to drive the recursive self-improvement run compared to AIDEhuman”.
- Design against gaming (§2.1): separating the inner loop's signal r_t from the outer loop's grade g “prevents the inner-loop agent from directly optimizing the criterion used for outer-loop selection”; equal per-task budgets mean gains come “from a better algorithm rather than from spending additional compute”.

## Assumptions

Research efficiency at fixed budget is the right objective; held-out private grades on a diverse selection benchmark resist overfitting; the model is held fixed in each loop, so gains are harness gains.

## Concepts

Inner loop / outer loop (bi-level optimization); harness layer; selection benchmark; private grade; first-order vs second-order generalization; incumbent; ignition test; reward hacking as proxy-to-downstream gap; bandit search over strategy arms with forking; bounded context and failure memory.

## Bearing on the record

The exchange (A41, decoded line 4788): "A research agent repeatedly improves its own code, using held-out evaluations | Close contemporary evidence of recursive agent-level improvement". Accurate, with one omission that matters for the record: the paper's own test of whether the *improver* improved (the ignition test) is inconclusive, and the outer loop is the human-built AIDE_human throughout the main run. The paper itself is careful about this.

- **[QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md)**: **bears directly; leaves the answer open**. The ignition test is the comparison the question's third sense asks for (a later improver against the earlier one from the same starting state at matched budget), and its result is a tie within three seeds. The main run shows level-2 achievements in A43's terms (validated self-modification of the inner agent, with transfer). The question's fourth sense, preserved correctability after damage, is not tested; the evaluator repair in §3.5 is an anecdote of an agent fixing a broken check rather than exploiting it.
- **[LIT-2273](../literature.d/LIT-2273.md)** (Deferred; "Of 26 studies ... only four compared earlier and later improvers"): this paper is a case that runs such a comparison and reports it as inconclusive. Whether [LIT-2273](../literature.d/LIT-2273.md) counts it is for that reading.
- **[CLAIM-266](../claims.d/CLAIM-266.md)** (probes supplying the training signal cannot certify preservation): **consistent, partly addressed**. The design separates the signal agents optimize (r_t) from the selection grade (g) and checks an unoptimized behaviour on held-out tasks; that is the kind of independent probe the claim says is needed, and here reward hacking fell. It does not test preservation of anything the probes miss.
- **[CASE-186](../cases.d/CASE-186.md) / [CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md)**: not tested (no damage to the diagnostic machinery).
- **[QUESTION-271](../questions.d/QUESTION-271.md)** (evaluation without capture): the improvers do not control the grade; leaves open.

## Limitations

One main run plus two replicates; three seeds for the ignition test; model fixed per loop; selection benchmark tasks not disclosed in the main text; authors are the developers of the baseline agent; external benchmarks' protocols in appendices not read.
