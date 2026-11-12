---
status: Proposed
title: 'A proposed study of governed schema adaptation: agents given a record whose grammar may or may not be adequate, under fixed or modifiable schemas crossed with informal or explicit change governance, scored on semantic correction without regressions'
version: 2
history:
- version: 1
  date: '2026-11-12'
  note: Filed from the exchange "luria experiment design", A45 Study 2 and A48 §6.
- version: 2
  date: '2026-11-12'
  note: >-
    At the owner's review of #484 on 2026-11-12, which split the routine-task
    prediction from CLAIM-tmppk8g6: the study now names a secondary estimand
    for it, CLAIM-tmpbszhs, on the tasks where no schema change is warranted,
    reported apart from the interaction. The arms are unchanged.
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
draws_on:
- THEORY-tmprcmsd
- THEORY-tmpdui86
- THEORY-tmp1o5v5
- THEORY-tmpru0yr
- THEORY-tmpqb5z0
- THEORY-tmp4d13i
- THEORY-tmpe8wmn
- THEORY-tmph4vkf
- THEORY-tmpxbva2
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
<!-- inactive-ok-file: CLAIM-tmppk8g6 CLAIM-tmpbszhs — filed from the same exchange, Proposed; the claims its interaction and its secondary estimand would test -->
<!-- inactive-ok-file: THEORY-tmp1o5v5 THEORY-tmp37mxv THEORY-tmp4d13i THEORY-tmpdui86 THEORY-tmpe8wmn THEORY-tmph4vkf THEORY-tmphkpxr THEORY-tmpqb5z0 THEORY-tmprcmsd THEORY-tmpru0yr THEORY-tmpxbva2 — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

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
alone, after EvoOntology ([LIT-2311](../literature.d/LIT-2311.md)), "a serious comparator, rather than a
weak static-ontology baseline" (A45); and a governed plain-Markdown
baseline, to separate the review process from the record's machinery.
The primary estimand is the interaction, which [CLAIM-tmppk8g6](../claims.d/CLAIM-tmppk8g6.md) predicts
positive on misfit tasks. A secondary estimand, set apart at the owner's
review of #484, compares the governed with the ungoverned arms on the tasks
where no schema change is warranted: justified correction, source
verification, provenance and review quality, against cost. It tests
CLAIM-tmpbszhs, which predicts no benefit there. The two are reported
separately and neither is read from the other: a benefit of governance on
routine tasks leaves the interaction as it was.

**The seed.** [CASE-131](CASE-131.md), started at the repository state before [ADR-044](../decisions.d/ADR-044.md):
two claims, a `supports` whose converse asserts a dependency nobody made,
and new evidence that one corroborates the other. A27: "the scorer should
**not require that exact field name**. It should verify the semantic
property". A29's specification: B may increase support for A; A does not
depend on B; A survives B's retirement; unrelated relations still resolve;
and no schema change is accepted without approval. A follow-up operation,
retiring B, checks that the new semantics survive use. Other development
episodes: [ADR-043](../decisions.d/ADR-043.md) (warrant), [ADR-049](../decisions.d/ADR-049.md) (partly answered questions), [ADR-061](../decisions.d/ADR-061.md)
(support judgements moved to ARG), [ADR-082](../decisions.d/ADR-082.md) (a line split) and [ADR-084](../decisions.d/ADR-084.md) (a
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
- **The inquiry frontier after the change** (A48, from [TERM-092](../terms.d/TERM-092.md)): whether
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
  answers and miss errors ([LIT-tmpka8bp](../literature.d/LIT-tmpka8bp.md)), so no single LLM judge decides
  whether a change is good.
- Comparators: COPE, the coupled-evolution approach behind Edapt
  ([LIT-tmp5mdsg](../literature.d/LIT-tmp5mdsg.md)), and KGCL ([LIT-2313](../literature.d/LIT-2313.md)), against which A48 would ask whether
  a change can be restated as "a precise, independently intelligible
  change specification".

## Note of 2026-11-12: 11 readings of the works of "luria experiment design"

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **DARPA** ([THEORY-tmphkpxr](../theory.d/THEORY-tmphkpxr.md)): SAIL-ON's "update its model of the world" after "characterize how the world changed" is the agent-level analogue of revising categories; its novelty hierarchy is a ready-made way to grade "inadequate categories". **Leaves open.**.
- **Liu and Yadav** ([THEORY-tmp37mxv](../theory.d/THEORY-tmp37mxv.md)): **leaves open**. STATE-Bench varies only the memory system on fixed tasks. Nothing in it requires revising a schema or a procedure's representation. It could serve only as the "transfer" or downstream-utility check the exchange proposed, not as a test of governed schema adaptation.
- **Bragg et al.** ([THEORY-tmprcmsd](../theory.d/THEORY-tmprcmsd.md)): On controls: AstaBench's principle 3 (cost and tool access as confounders) **supports** the cases' control "Matched evidence, tools, models and budgets across arms". It is independent support from a benchmark-design paper.
- **Boult et al.** ([THEORY-tmpdui86](../theory.d/THEORY-tmpdui86.md)): On the failure kind "schema inadequacy: the grammar cannot express the distinction" versus "missing evidence": **qualifies**. Boult's distinction between rejection under ambiguity (Chow) and recognition of an unknown corresponds to the case's split between "record the uncertainty" and "amend the grammar". The paper warns that a detector built for the first does not serve the second.
- **Thorne, Vlachos, Christodoulopoulos and Mittal** ([THEORY-tmp1o5v5](../theory.d/THEORY-tmp1o5v5.md)): Its failure kind "missing evidence: the ambiguity cannot be resolved", with the correct response "record the uncertainty or ask for more; change nothing", has a direct analogue in FEVER's NOTENOUGHINFO label. FEVER's guidance to annotators to keep world knowledge out of the verdict is a precedent for scoring an abstention as correct. Bears as a design precedent, nothing more.
- **OAEI** ([THEORY-tmpru0yr](../theory.d/THEORY-tmpru0yr.md)): The Interactive track's oracle design is a precedent for the case's "deterministic rule-based simulator" reviewer. That reviewer is the exchange's design, not the case's text. Weak bearing.
- **Anonymous** ([THEORY-tmpqb5z0](../theory.d/THEORY-tmpqb5z0.md)): **supports a design element and supplies a ready instrument**. The case's table of failure kinds includes "missing evidence … change nothing", and its rule is that tasks must include "cases where the correct action is no schema change". TRACE-OU-Bench builds both in: INSUFFICIENT_EVIDENCE, REJECT as "unwarranted, redundant", and many NO_UPDATE proposals. Its sequential snapshots match the case's demand that a repair be checked by "later operations on the repaired record". The difference: TRACE-OU scores a decision about a proposal. The case asks an agent to recognize the misfit, and to propose and migrate the change itself.
- **Chong, Zhang, Fan and Du** ([THEORY-tmp4d13i](../theory.d/THEORY-tmp4d13i.md)): **supports the design choice** of a performance-gated arm; the paper's reciprocal two-fold protocol (build and gate on one fold, test frozen on the other) is a usable template for that arm.
- **Hegde et al.** ([THEORY-tmpe8wmn](../theory.d/THEORY-tmpe8wmn.md)): **supports** using a KGCL-style restatement as a check on change legibility; note the restatement covers content edits, so a schema change in luria would need change types KGCL does not have.
- **Herrmannsdoerfer, Benz and Juergens** ([THEORY-tmph4vkf](../theory.d/THEORY-tmph4vkf.md)): **supplies a baseline and a task taxonomy.** COPE's classification of changes (metamodel-only, metamodel-independent coupled, metamodel-specific coupled) can stratify the study's "schema inadequacy" items. An operation-based history with generated migrators is a natural "explicit migration, informal governance" arm.
- **Orzechowski, Tawfiq and Kosciolek** ([THEORY-tmpxbva2](../theory.d/THEORY-tmpxbva2.md)): **supports the scoring design**. The paper shows a schema-derived checker missing exactly the class of error CASE-tmppm4do cares about (changes of meaning), and checks whose flags corrupt correct work when acted on, which argues for the case's hidden-assertion oracle with known ground truth and for counting regressions. It also supplies a design lesson the case can adopt: compare every checker with a trivial baseline and with a random flag at the same rate.

The case is unchanged.
