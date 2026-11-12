---
number: 108
status: Open
formerly:
- QUESTION-tmpkbkoh
title: When a structured record does better than a summary, a transcript or a posterior
  on revision tasks, is it because it retains more, because what it retains is easier
  to reach, or because the operations a reviser needs are easier to perform on it?
version: 3
history:
- version: 2
  date: '2026-11-07'
  note: >-
    Line nucleating-argument replaced by records-of-inquiry, at the split of that
    line (ADR-082). No other change.
- version: 3
  date: '2026-11-08'
  note: >-
    Carries nucleating-argument again beside its new line, at ADR-
    tmpyb8vm's rule (version 2): an entry the split moved keeps the old
    line when it answers, refines or objects to one of that line's
    entries, and it refines QUESTION-038. No other change.
tags:
- epistemology
- design-rationale
date: '2026-10-15'
line:
- records-of-inquiry
- nucleating-argument
refines:
- QUESTION-038
summary: >-
  A5's second question, with A3's question B and A4 §4's decomposition: information
  retained, information accessible, information used correctly. The three are different
  findings, and a comparison that does not separate them cannot say which one [CLAIM-295](../claims.d/CLAIM-295.md)
  rests on.
---
<!-- inactive-ok-file: CLAIM-182 CLAIM-184 CLAIM-190 CLAIM-295 — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->
<!-- inactive-ok-file: CLAIM-tmp8qsef — filed from the exchange "luria experiment design", Proposed or Deferred; cited in the note of 2026-11-12 -->
<!-- inactive-ok-file: SYNTHESIS-015 — Deferred, Proposed; cited in the note of 2026-11-12 for what each holds, not as settled -->
<!-- inactive-ok-file: CASE-tmp8rg2s — filed from the exchange "luria experiment design", Proposed or Deferred; cited in the note of 2026-11-12 -->
<!-- inactive-ok-file: THEORY-tmp5rm74 THEORY-tmp5vepa THEORY-tmpaxysg THEORY-tmpcfp6p THEORY-tmphrkr5 THEORY-tmpkjz86 THEORY-tmplr84w THEORY-tmpo4vs4 THEORY-tmpol9my THEORY-tmpvuz7f THEORY-tmpw88x9 THEORY-tmpyzyqe — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# QUESTION-108: When a structured record does better than a summary, a transcript or a posterior on revision tasks, is it because it retains more, because what it retains is easier to reach, or because the operations a reviser needs are easier to perform on it?

## Why it is a question

A4 §4: "A graph could outperform a summary because it retains more
information, because it retrieves information more reliably, or because
the model is better at executing operations on explicit relationships.
Those are different findings." [QUESTION-038](QUESTION-038.md) asks what turns a persisting
structure into an anchor. This asks which of three mechanisms is doing
the work when one does.

A3's question B, whether structured addressability reduces unannounced
drift, is held here rather than filed apart: it is the drift-measured
special case, and [CLAIM-182](../claims.d/CLAIM-182.md) already states it as a thesis. A3's counter
goes with it: "A structured record may make agents less willing to revise
erroneous commitments. Less drift is not necessarily more epistemic
progress" ([CLAIM-184](../claims.d/CLAIM-184.md)).

An answer is a design that manipulates retention, access budget and
format independently, scored on decisions in an externally specified
environment and not on reproducing the record's own graph ([CLAIM-190](../claims.d/CLAIM-190.md)).
[CASE-091](../cases.d/CASE-091.md) is that design. A negative result counts: "if narrative summaries or
latent representations preserve the same revision competence more
efficiently, that tells us something about the limits of nucleation's
architecture."

## Note of 2026-11-12: the owner's "equip an agent with luria", and the ablations proposed, from "luria experiment design"

At U10 of the exchange "luria experiment design" (2026-11-10, https://chatgpt.com/share/6af35bfc-35f8-83e9-a63d-d594703eabda) the owner asked for evaluations, "e.g. equip an agent with
luria and evaluate the agent against some task". A's proposals bear on this
question's three mechanisms, retaining more, easing retrieval, making
operations cheap:

- A27 and A29: run MEME ([LIT-2281](../literature.d/LIT-2281.md), unread), whose Cascade and Absence tasks
  test dependent facts that stop holding, with plain files, retrieval, a
  typed record, and a typed record with checks, under two ingestion modes:
  every arm given the same gold extracted facts, which isolates
  representation and retrieval, and every arm ingesting raw conversation,
  which tests the whole workflow. Ingestion cost is reported apart from
  query cost: "A structured record could gain on update handling while
  losing badly on time and tokens spent writing records."
- A32: hold the record's contents fixed and vary access, a shared
  transcript, indexed notes, a typed record, a governed one, citing this
  question for the split.
- A36 E1: on [CLAIM-293](../claims.d/CLAIM-293.md)'s two worlds, "A Luria agent that simply follows
  graph edges and reaches the same conclusion in both situations has failed
  the substantive task"; and a targeted dependency report against the full
  graph, since a gain there would put the value in "making an operation
  cheap, not in graph structure as such". [CASE-091](../cases.d/CASE-091.md) holds the design these
  extend.
- A17: a counter-effect to test for, that "a well-structured record might
  anchor the assistant too strongly to its existing explanatory
  vocabulary" ([SYNTHESIS-015](../syntheses.d/SYNTHESIS-015.md), [CLAIM-184](../claims.d/CLAIM-184.md)).

A20 and A27 named agent-memory systems as comparators: Generative Agents
([LIT-tmpiufjk](../literature.d/LIT-tmpiufjk.md)), HippoRAG ([LIT-tmp9oc9e](../literature.d/LIT-tmp9oc9e.md)), A-MEM ([LIT-tmpqhq20](../literature.d/LIT-tmpqhq20.md)), GraphRAG
([LIT-tmppcaeo](../literature.d/LIT-tmppcaeo.md)), LongMemEval ([LIT-2282](../literature.d/LIT-2282.md)) and MemoryAgentBench ([LIT-2279](../literature.d/LIT-2279.md)), all
unread. [CLAIM-tmp8qsef](../claims.d/CLAIM-tmp8qsef.md) bears on the third mechanism: what the record makes
cheap is finding the dependants, not deciding them. Open.

A further proposed test, the filer's own idea, accepted by the owner:
[CASE-tmp8rg2s](../cases.d/CASE-tmp8rg2s.md), a study of curation completeness scored on the record's
own corrected filings, which bears on the third mechanism. The wording of
this paragraph is the assistant's (Claude, in this session); adopting it is
the owner's call.

## Note of 2026-11-12: 12 readings of the works of "luria experiment design"

Read on 2026-11-12 among the works of the exchange "luria experiment design"; each reading's NOTE and THEORY hold the detail.

- **Mo, Zheng et al.** ([THEORY-tmpyzyqe](../theory.d/THEORY-tmpyzyqe.md)): The paper's matched design (same task, output format and scoring; vary only who controls the evidence) is the same shape as [CASE-091](../cases.d/CASE-091.md)'s information-equivalent vs. budget-equivalent arms, and its own caution, that "Active" bundles retrieval control with interaction and tool competence, is the confound [CASE-091](../cases.d/CASE-091.md) controls for. A methodological parallel; it does not test records. Leaves open.
- **Xue et al.** ([THEORY-tmpvuz7f](../theory.d/THEORY-tmpvuz7f.md)): §4.3 is direct evidence on the "structure" side: loose notes left stale and current values competing, and typed bindings with a superseded value rendered only as current fixed Memory; a correction left in an unstructured transcript fragment was re-read as stale. Supports the question's second mechanism (easing retrieval) for update tasks; not a test of a governed record.
- **Hu, Wang and McAuley** ([THEORY-tmp5vepa](../theory.d/THEORY-tmp5vepa.md)): **supports** the question's premise that the competence at stake is revision, not retrieval: retrieval-oriented memory does well on retrieval and fails on updates whose consequences span several facts, and even full context fails beyond short lengths. It does not test a structured record, so it leaves the question open; it is a usable external test for [CASE-091](../cases.d/CASE-091.md)'s revision arm.
- **Jung, Rubinstein, Uselis, Yun and Oh** ([THEORY-tmpo4vs4](../theory.d/THEORY-tmpo4vs4.md)): **supports** the question's third mechanism, making an operation cheap: systems that hold the rule and the change event still fail because nothing finds the dependants at the time of change; the one configuration that succeeds does so by finding dependants at ingest and writing the consequence. It **qualifies** a reading on which structure alone helps: Graphiti, a temporal knowledge graph, scores near zero overall, and its triple extraction "strip[s] the contingency wording". MEME is a ready external test for the record's arms; not yet run with one.
- **Wu et al.** ([THEORY-tmpaxysg](../theory.d/THEORY-tmpaxysg.md)): **qualifies** in a direction the question anticipates ("A negative result counts"): compressing sessions into extracted summaries or facts lost information and lowered accuracy, except on multi-session reasoning where facts helped; and structure at reading time (JSON plus Chain-of-Note) helped only together. This is evidence that the value of a structured representation depends on the question type and on reading, not on structure as such; it does not test a governed record.
- **Romera-Paredes et al.** ([THEORY-tmpw88x9](../theory.d/THEORY-tmpw88x9.md)): **leaves open**; the programs database is a structured store of scored candidates, but the paper does not compare it with an unstructured alternative.
- **Wang et al.** ([THEORY-tmplr84w](../theory.d/THEORY-tmplr84w.md)): **leaves open**, but offers a candidate task family: questions whose answers need facts from several papers, where a record of prior readings could be compared with retrieval.
- **Jiménez Gutiérrez et al.** ([THEORY-tmphrkr5](../theory.d/THEORY-tmphrkr5.md)): Asks whether a structured record outperforms a summary because it retains more, makes information easier to reach, or makes operations easier. **Verdict: supports one arm, the retrieval arm, and leaves the others open.** HippoRAG is a clean instance of the "easier to reach" mechanism. The same passages are retained; only the index changes, and multi-hop retrieval improves. The paper does not evaluate revision tasks, so it says nothing about the "operations" arm. Its retrieval gain is largest on entity-centric data (2Wiki). That suggests the retrieval benefit depends on how well the index's structure matches the questions asked.
- **Park et al.** ([THEORY-tmp5rm74](../theory.d/THEORY-tmp5rm74.md)): **bears on the second mechanism; leaves the question open.** The memory stream retains everything and wins by retrieval: sec. 4.1's argument against summarizing is that a summary loses the specific memories, and 6.5.2 and 7.2 show that failures come from retrieval, not retention (the memory existed but was not surfaced). The ablation removes memory, reflection and planning wholesale, so it does not separate retention from access from operations; it does not test the question's split. A design that does ([CASE-091](../cases.d/CASE-091.md)) could take this architecture as its "retrieval over everything" arm.
- **Blanchet and Michinov** ([THEORY-tmpcfp6p](../theory.d/THEORY-tmpcfp6p.md)): **bears weakly.** Transactive memory here is specialization of who encodes what, i.e. a division of retention plus knowledge of where it sits; groups that expect turnover keep redundant knowledge instead. A record that makes "who holds what" durable regardless of membership would remove the reason to avoid specializing; this is an inference, not tested.
- **Edge et al.** ([THEORY-tmpol9my](../theory.d/THEORY-tmpol9my.md)): **Qualifies and sharpens.** GraphRAG's design is a direct instance of the "easier to reach" mechanism: the benefit over vector RAG comes from pre-computing summaries that cover the whole corpus, and its own Experiment 2 finds no significant gain of the graph conditions over graph-free map-reduce summarization (TS), only a cost gain. That is a published case where structure's measured value is accessibility and cost, not retention or operations, which is the separation QUESTION-108 asks for.
- **Xu et al.** ([THEORY-tmpkjz86](../theory.d/THEORY-tmpkjz86.md)): **Qualifies.** A-MEM's ablation is a rare published separation inside one system: adding LLM-made links (without evolution) improves multi-hop QA over the same notes without links, which bears on the "easier to reach" mechanism (links bring related notes into the retrieved context) rather than "retains more" (the same notes are stored in both arms). It does not test the "operations" mechanism, and its evolution step trades retention for currency: it may lose information when it rewrites. So it is evidence that structure helps by reach on QA tasks, and no evidence on revision tasks, which are what QUESTION-108 is about.

The question is unchanged.
