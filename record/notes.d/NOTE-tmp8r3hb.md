---
status: Read
paper: LIT-2317
title: 'Majumder et al. — DiscoveryBench: Towards Data-Driven Discovery with Large Language Models'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2407.01725. **Read** (main
    text), 2026-11-12. A delegated reader drafted the reading; quotations were
    rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  DiscoveryBench asks whether LLM agents can search for and verify
  hypotheses from datasets alone. A data-driven hypothesis is a sentence
  whose truth a verification procedure can infer from a dataset; it
  decomposes into sub-hypotheses, each with a context (boundary conditions),
  variables and a relationship. Tasks give a dataset, metadata and a goal
  formed by masking one of these dimensions of a target hypothesis.
---

# NOTE-tmp8r3hb: Majumder et al. — DiscoveryBench: Towards Data-Driven Discovery with Large Language Models

## Contribution

A formalism for data-driven hypotheses (context, variables, relationship; semantic trees), a benchmark from real published workflows plus a controllable synthetic counterpart, and a faceted evaluation of open-ended answers.

## Key results

- Ceiling (Abstract; §7): “even the best system scores only 25%”.
- Elaborate prompting does not help (§6): “effective reasoning prompts such as React and planning with a self-critic (DataVoyager) do not help improve the simple CodeGen agent”; only Reflexion with the oracle HMS as feedback improves significantly.
- Context first (§6): accurate context prediction is needed for accurate variables and relationships, but “it does not guarantee success”.
- Workflow categories (§6): best non-oracle performance 55% on correlation analysis, 0% on spatial analysis, pollen dating and ecological modelling.
- Domain knowledge (§6): for archaeology tasks DataVoyager (GPT-4p) “jumps from 9.9% (w/ domain knowledge) to 17.5% (w/o domain knowledge)”. The parenthetical labels appear reversed relative to the sentence's claim that hints help; read as stated, the numbers say the opposite.- Difficulty (§6): performance falls with workflow length, and finding a relationship given context and variables is easier than finding context or variables.
- Building the benchmark (§4): replicating data-first workflows took “up to 90 person-hours per dataset, often (30%) not resulting in success”; of 785 Zenodo items examined, 3 of 14 candidate repositories passed all checks.

## Assumptions

A discovery task has a unique target hypothesis recoverable from the data; an LLM judge can decompose and match hypotheses reliably; DB-SYNTH's LLM-generated semantic trees capture the complexity of real workflows (supported by similar scores on both).

## Concepts

Data-driven hypothesis; verification procedure; context, variables, relationship; hypothesis semantic tree and forest; workflow length as difficulty; discovery goal by masking a dimension; HMS; discovery agent.

## Bearing on the record

The exchange (A14's chart, decoded exchange lines 650–652): "ICLR 2025 · best reported system on its 264 real-data tasks" at 25%. Accurate for arXiv v1 (the 25% figure is the best overall, as the abstract says; whether it is per DB-REAL only is not stated so precisely in v1). A later turn (decoded) notes only that AstaBench includes DiscoveryBench among its tasks.

The LIT names no code. On recheck:

- **[CLAIM-470](../claims.d/CLAIM-470.md)** (inquiry as specification: a question fixes which differences would count as an answer): **illustrates**. DiscoveryBench's goals are formed by masking one dimension of a hypothesis, so the goal fixes what kind of difference (a context, a variable set, a relationship) would answer it; goals that leave context or variables open are harder than those that fix them.
- **[TERM-092](../terms.d/TERM-092.md)** (inquiry frontier at a budget): **leaves open**; workflow length as a difficulty measure is a crude analogue, not a test.
- **[CLAIM-266](../claims.d/CLAIM-266.md) / [CASE-144](../cases.d/CASE-144.md)** (evaluation): the benchmark's evaluation is an LLM judge; the paper does not test its agreement with humans in the main text. Leaves open.

## Limitations

v1 preprint (the ICLR version may differ); LLM-based evaluation; small number of source papers for DB-REAL; agents and models from mid-2024; the domain-knowledge result as printed is internally inconsistent.
