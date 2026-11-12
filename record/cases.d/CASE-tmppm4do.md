---
status: Proposed
title: 'A proposed study of governed schema adaptation: agents given a record whose grammar may or may not be adequate, under fixed or modifiable schemas crossed with informal or explicit change governance, scored on semantic correction without regressions'
version: 1
standing: stipulated
kind: proposed-study
tags:
- design-rationale
- databases
- epistemology
date: '2026-11-12'
line:
- record-as-apparatus
bears_on:
- QUESTION-tmps5iou
summary: >-
  From the exchange "luria experiment design" (2026-11-10). The owner asked
  at U10 for "evaluations or benchmarks", "e.g. equip an agent with luria
  and evaluate the agent against some task", having asked at U8 about
  schema modifiability coupled to governance. A proposed the design over
  six turns: A27's "Inquiry Evolution Benchmark", A29's GSAE, A36's E8,
  A39's Study D, A45's Study 2 and A48's Study B, each refining the last.
  This entry gathers them. Not run; the stipulated part is the design. The
  design is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: ADR-082 ADR-084 — Proposed; historical episodes the study would draw on, cited as open -->
<!-- inactive-ok-file: LIT-2311 LIT-2313 LIT-tmpka8bp LIT-tmp5mdsg — Deferred; registered from the same exchange, not read -->
<!-- inactive-ok-file: CLAIM-tmppk8g6 — filed from the same exchange, Proposed; the claim the study's interaction would test -->

# CASE-tmppm4do: A proposed study of governed schema adaptation: agents given a record whose grammar may or may not be adequate, under fixed or modifiable schemas crossed with informal or explicit change governance, scored on semantic correction without regressions

## The case

From the exchange "luria experiment design"
(https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda).

**The task.** Each episode gives an agent team a record, its configuration
and a triggering source or problem. A29: the agent must "recognize that the
current representation cannot state a needed distinction, propose an
appropriate change, and maintain the existing record through that change",
or recognize that it can. The failures are matched across four kinds
(A39 Study D):

| failure | correct response |
|---|---|
| instance error: an entry misfiled under an adequate grammar | correct the entry |
| schema inadequacy: the grammar cannot express the distinction | amend the grammar and migrate |
| governance inadequacy: the distinction is expressible, the rules block the correction | revise the procedure, if justified |
| missing evidence: the ambiguity cannot be resolved | record the uncertainty or ask for more; change nothing |

A29: "The task distribution should include cases where the correct action
is **no schema change**", since "A benchmark consisting only of genuine
schema gaps rewards an agent that expands the schema whenever it encounters
something unfamiliar."

**The arms.** A45 §3 and A48 §6: a fixed or a modifiable schema, crossed
with informal or explicit change governance (proposal, authority, approval
and migration, enforced by the harness, not by instruction). Two further
arms: performance-gated evolution, changes accepted on held-out tests
alone, after EvoOntology (LIT-2311), "a serious comparator, rather than a
weak static-ontology baseline" (A45); and a governed plain-Markdown
baseline, to separate the review process from the record's machinery.
The primary estimand is the interaction, which CLAIM-tmppk8g6 predicts
positive on misfit tasks.

**The seed.** CASE-131, started at the repository state before ADR-044:
two claims, a `supports` whose converse asserts a dependency nobody made,
and new evidence that one corroborates the other. A27: "the scorer should
**not require that exact field name**. It should verify the semantic
property". A29's specification: B may increase support for A; A does not
depend on B; A survives B's retirement; unrelated relations still resolve;
and no schema change is accepted without approval. A follow-up operation,
retiring B, checks that the new semantics survive use. Other development
episodes: ADR-043 (warrant), ADR-049 (partly answered questions), ADR-061
(support judgements moved to ARG), ADR-082 (a line split) and ADR-084 (a
scheme narrowed, an extension partly undone).

## What it would measure

- **Semantic correction without material regression**, the primary
  outcome, scored by hidden assertions and forbidden inferences, not by
  similarity to the record's own patch. A50 adds metamorphic properties as
  the oracle: renaming a scheme without changing its semantics leaves
  query results equivalent; retiring nonessential corroboration does not
  invalidate an independent argument.
- **Diagnosis before repair** (A29): the level of the failure named first,
  with no edits, then the repair, then later operations on the repaired
  record: "recognition, implementation, and continued usefulness".
- **Schema-change necessity**: precision and recall on true misfits
  against instance errors.
- **Migration fidelity, governance compliance and cost**, each reported on
  its own. A29: "The primary outcome should be semantic task success
  without regressions, not the presence of an ADR. Otherwise a governed
  workflow could win merely because the evaluation rewards its own
  paperwork." A29 again: "an approval system can appear successful simply
  by refusing to change anything."
- **The inquiry frontier after the change** (A48, from TERM-092): whether
  agents formulate the questions the new distinction makes relevant,
  pursue them under budget, and find other questions harder to ask.

## Controls and limits

- Historical episodes are public and may be in a model's training data.
  A29: use them "for development and interpretive case studies", and
  confirm on new tasks "with altered domains, different relation names,
  changed taxonomies and new counterexamples", varying "the actual
  conceptual distinction being required".
- Matched evidence, tools, models and budgets across arms; review time
  counted as cost; at least two model families.
- The evaluator and the hidden truth stay outside every agent's writable
  environment.
- A29 on scoring with a model judge: ontology-based checkers flag correct
  answers and miss errors (LIT-tmpka8bp), so no single LLM judge decides
  whether a change is good.
- Comparators: COPE, the coupled-evolution approach behind Edapt
  (LIT-tmp5mdsg), and KGCL (LIT-2313), against which A48 would ask whether
  a change can be restated as "a precise, independently intelligible
  change specification".
