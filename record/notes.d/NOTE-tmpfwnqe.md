---
status: Read
paper: LIT-2281
title: 'Jung, Rubinstein, Uselis, Yun and Oh — MEME: Multi-entity & Evolving Memory Evaluation'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2605.12477. **Read**
    (2026-11-12): main text §§1–6 read in full; appendices skimmed. A
    delegated reader drafted the reading; quotations were rechecked by script
    against the downloaded copy, and any that did not match were kept as
    paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  MEME organizes agent-memory evaluation on two axes, entity scope (single
  vs. multi-entity) and temporal dynamics (static vs. evolving), with six
  tasks: Exact Recall, Aggregation, Tracking, Deletion, and two
  dependency-reasoning tasks no earlier benchmark scores: Cascade (a
  dependent fact changes by a stated rule after an upstream update) and
  Absence (after an upstream change with no replacement rule, the right
  answer is "Uncertain"). Episodes (~35K tokens) are generated from
  hand-built DAGs of entities, dependency edges and conditional rules in two
  domains, so gold answers are computed by propagation. Six memory systems
  across three paradigms (raw retrieval; LLM-processed memory: Mem0,
  Graphiti; file-based agents: Karpathy Wiki, MD-flat) all fail Cascade (avg
  0.03) and Absence (avg 0.01), although they encode and retain the rule and
  the change event; the failure is at retrieval or answering.
---
<!-- inactive-ok-file: CLAIM-tmp8qsef — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmpfwnqe: Jung, Rubinstein, Uselis, Yun and Oh — MEME: Multi-entity & Evolving Memory Evaluation

## Contribution

A taxonomy and benchmark that score dependency propagation and
uncertainty-after-change in agent memory, and a stage-wise diagnosis
(encoding, maintenance, retrieval) of why current systems fail at it.

## Key results

- Abstract: "all systems collapse on dependency reasoning under the default
  configuration (Cascade: 3%, Absence: 1% in average accuracy) despite
  adequate static retrieval performance."
- §3.1: Absence "recognizes that a dependent entity is uncertain after an
  upstream change with no replacement rule, where the correct answer is
  uncertainty rather than a new value."
- §4.1: a gold-facts in-context ceiling "confirms that the tasks are solvable
  in principle: 0.91 overall with Claude Opus 4.7".
- §5: "Across all six systems the dependency rule and the change event are
  written and retained, but at retrieval the change event is either
  out-ranked by the pre-change value (vector retrievers) or never surfaced at
  all".
- §4.4: "A capable answering LLM cannot reconstruct dependencies that the
  memory layer never preserved."
- §4.4: closure in MD-flat × Opus 4.7: at ingest it writes "an explicit
  contingency entry naming the parent. When the change later arrives, it
  scans for dependent contingency entries and writes the propagated value in
  place." Cascade 0.32, Absence 0.59 (Table 4).
- §4.2: in-context gpt-4.1-mini (0.36 overall) beats five of six memory
  systems on accuracy; memory systems win on per-query cost.
- §5: "the path forward is memory architectures that natively propagate
  updates through dependent facts at maintenance".

## Assumptions

Dependency rules stated explicitly in conversation (a best-case framing, per
§6); fictitious entity values; LLM-generated dialogue; GPT-4o judge (98.6%
agreement with author annotations on 144 samples); trivial-pass filtering
(credit requires correct answers before and after the change).

## Concepts

Entity scope × temporal dynamics; Exact Recall, Aggregation, Tracking,
Deletion, Cascade, Absence; dependency reasoning; ripple effect (from
knowledge editing); pre-change value; encoding / maintenance / retrieval
stages; contingency entry; raw retrieval vs. LLM-processed vs. file-based
memory; internal vs. answering LLM.

## Bearing on the record

QUESTION-108's note: "run MEME ..., whose Cascade and Absence tasks test
dependent facts that stop holding". Accurate; Absence specifically tests that
a fact that stops holding is reported as uncertain rather than replaced.
A27's proposed arms (plain files, retrieval, typed record, typed record with
checks; gold-fact vs raw ingestion) fit MEME's design, which already has a
file-based arm (MD-flat) and a gold-facts ceiling.

- **QUESTION-108** (when a structured record beats a summary, transcript or
  posterior): **supports** the question's third mechanism, making an
  operation cheap: systems that hold the rule and the change event still fail
  because nothing finds the dependants at the time of change; the one
  configuration that succeeds does so by finding dependants at ingest and
  writing the consequence. It **qualifies** a reading on which structure
  alone helps: Graphiti, a temporal knowledge graph, scores near zero
  overall, and its triple extraction "strip[s] the contingency wording". MEME
  is a ready external test for the record's arms; not yet run with one.

- **CLAIM-tmp8qsef** (Proposed: the record computes no withdrawals;
  retiring an entry reports what rests on it and leaves whether each dependant
  falls to judgment): MEME's Absence task is that situation (a support
  changes, no rule says what follows, the correct state is "uncertain"), and
  its Cascade task is the case where a stated rule does decide it. The
  finding that failing systems hold the dependency but never surface it
  supports the value of the record's reporting of dependants; the record's
  leaving the verdict to judgment corresponds to Absence's correct answer,
  not to Cascade's. Supports the claim's division; does not test it.
- **CLAIM-293** (topology does not fix revision): MEME's gold answers *are*
  fixed by the DAG plus rules; it is a setting where the claim's condition
  (same edges, different evidence) does not arise. Contrast, not evidence.
- **CASE-091**: MEME is a candidate external task for its revision arm;
  information-equivalent conditions correspond to MEME's gold-facts ceiling.
- No held entry names Cascade/Absence tasks or "ripple effect" in this sense
  (LIT-706's "ripple effect" is emotional contagion). Duplicate check: arXiv
  id and title not held elsewhere.

## Limitations

Two hand-crafted graphs; synthetic dialogues; 100 episodes; most ablations
on 10–40-episode subsets; explicit conditional phrasing only.
