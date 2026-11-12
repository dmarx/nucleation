---
status: Read
paper: LIT-2310
title: 'Chi et al. — AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2608.20318. **Read** (main
    text), 2026-11-12. A delegated reader drafted the reading; quotations were
    rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  The paper argues that recursive self-improvement compounds mainly through
  the "algorithmic design level" (objectives, update rules, regularization,
  schedules), as opposed to systems engineering or data, and builds a
  benchmark that isolates it: ten frozen research repositories covering ten
  families of training algorithm. An agent gets 4 hours on one B300 GPU and
  a cheap proxy metric to rewrite the repository's training algorithm; its
  source code alone is then rerun from scratch for up to 12 hours and scored
  by an evaluator fixed in advance and hidden from it, against the
  repository's own algorithm run identically. Scores map each metric onto
  one scale (0 uninformative, 0.1 the shipped algorithm, 1.0 the optimum).
---
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmp5gx1z: Chi et al. — AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement

## Contribution

A benchmark for whether an agent improves the learning procedure rather than the artefact, with a clean development/evaluation separation and a classification of what each submission changed.

## Key results

- Overall (Abstract): “Across 29 configurations of 6 systems on all 10 tasks the mean score is 0.166, and the best system reaches 0.250”.
- Worse than baseline (§3.2): 124 of the 290 cells fall below 0.1, i.e. “more than two fifths of the attempts leave the repository with something worse than what it had”.
- What submissions change (§4.1): of 263 classifiable submissions, 141 stay on the run side and 122 touch how the model learns; those average 0.226 against 0.126, “a gap of 0.100 against a standard error of 0.022”, with the caveat that “It is also not a randomized comparison”.
- Reasoning effort (§4.2): the share touching the learning algorithm “rises from 8.0% to 64.0%”; mean score rises from 0.094 to 0.196.
- Spend does not order the systems (§3.2): “Whatever is separating these systems, it is not how much exploration they bought.”
- The exceptions (§4.3): the three standout submissions each “built something measurable before acting”, such as an evaluation rig five hundred times faster than the one supplied.
- Boundary of the guarantee (§2): the proxy may draw on the same corpus as the final evaluation; the separation is “one of access and timing rather than of sample disjointness”.

## Assumptions

- Improvements to a training algorithm are what a successor would inherit, so they are the link through which RSI compounds (argued in §1, not tested).
- An LLM classifier reading diffs identifies which side of the run/learning line a change falls on.
- The repository's shipped algorithm under identical budget is the right baseline.

## Concepts

Algorithmic design level vs systems and data levels; exploration budget vs verification budget; proxy metric vs fixed hidden evaluator; mapped score with baseline pivot at 0.1; run-side vs learning-side changes; "nerve".

## Bearing on the record

The exchange's table (A41, decoded): "Agents redesign training algorithms rather than merely optimize task outputs | Useful precedent for testing *improvements to the improvement process*". The first half is accurate as to what the benchmark asks. The second overstates: AI4AI-Bench tests a single round in which an agent improves a training algorithm. No agent improves itself, no improved procedure is fed back, and nothing compares an earlier with a later improver. It measures the step the authors say RSI would compound through, not the recursion. [QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md) lists it as "prior art on self-improving agents"; it is prior art on agents improving another system's learning procedure.

- **[QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md)**: **leaves open**. It does not compare earlier and later improvers; its baseline design (same hardware, budget, evaluator, asset; only the source differs) is the matched comparison the question asks for, applied once.
- **[CLAIM-266](../claims.d/CLAIM-266.md)** (probes supplying a training signal cannot certify preservation): **consistent with, not a test**. The design keeps the scoring evaluator out of the agent's reach and admits the proxy may share data with it.
- **[CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md)**: its "product gain without improver gain" outcome has an analogue here: run-side tuning that raises a score without changing the learning rule. Illustration only.

## Limitations

Ten tasks; one GPU per task; LLM-classified diffs; the learning-side advantage is observational; six 2026 systems; cost of exploration only ($5,334) excludes the verification runs.
