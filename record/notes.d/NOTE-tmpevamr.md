---
status: Read
paper: LIT-2278
title: 'Xue et al. — PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from https://arxiv.org/pdf/2608.04003. **Read**
    (2026-11-12): main text §§1–6 read; appendices skimmed (metric
    definitions, judge validation headings). A delegated reader drafted the
    reading; quotations were rechecked by script against the downloaded copy,
    and any that did not match were kept as paraphrase without quotation
    marks.
date: '2026-11-12'
summary: >-
  PAST-Bench tests whether personal AI agents (Hermes, OpenClaw and others)
  get better at later tasks by reusing experience retained from earlier
  ones, without retraining. Each of 26 task families is a sequence of
  fresh-session episodes (context wiped between them) in which earlier
  episodes give the agent a chance to save a fact, a procedure, a correction
  or a pre-seeded reference, and later ones test reuse; every evaluation
  episode is run with persistence on and off under the same prompt, grader,
  tools and seed, and controls check shortcuts, distractors, stale state and
  wrong-mechanism reuse. Alongside the score gap Δ it reports mechanism
  evidence (memory writes and reads, skill creation and patching, update
  correctness).
---
<!-- inactive-ok-file: CASE-tmpy1ebu CLAIM-tmp8qsef — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->
<!-- inactive-ok-file: CLAIM-184 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpevamr: Xue et al. — PAST-Bench: Benchmarking the Foundations of Recursive Self-Improvement in Personal Agents

## Contribution

A performance-attribution benchmark that pairs persistence-on/off runs within
task families and reports whether a gain flowed through the intended
save–retrieve–update pathway.

## Key results

- §1: "Online self-evolution is not RSI in its full form, but it provides a
  concrete behavioral and infrastructural substrate on which stronger forms
  of recursive improvement can be built".
- §1: "Evaluating self-evolution is thus a performance-attribution problem".
- §3: with context wiped between episodes, "Any improvement of a later episode
  over an earlier one must therefore flow through the persistent substrate".
- §3.2: "We treat this as a strong design control rather than a causal
  proof"; Δ counts as evidence "only when it clears the upper bound set by the
  family's control episodes".
- §1 contributions: agents that tie on Δ differ in mechanism evidence
  ("Hermes vs. nanobot: 0.64 vs. 0.57 at the same Δ = +0.13").
- §4.3 (Update failure): "Old persistent evidence remains active after
  correction"; Hermes traces record the correction in-session while "the next
  episode reads an older artifact". The fix E5 writes the update "as the new
  authoritative artifact in place of the prior value".
- §4.3 (Memory fix E2): memory written "with type, scope, entity, current
  value, superseded value, and expiry", rendering "only the in-scope current
  binding".
- §4.4: "The +0.02 difference is smaller than the run-to-run variation, so we
  do not interpret it as a stable overall gain"; the clearer shift is Update
  (+0.12 → +0.24).
- §4.4: "target gains can coexist with regressions elsewhere, component
  effects can reverse in combination, and a runtime change need not transfer
  uniformly."

## Assumptions

Synthetic task families; an LLM judge for task scores (validated against
humans in Appendix B.4, not read); persistence is benchmark-managed state;
the matched ablation isolates persistence (stated as a design control, not
proof).

## Concepts

Online self-evolution; performance attribution; task family; cold, learn,
evaluate and control episodes; persistence on/off (w/ and w/o evolve);
self-evolution gap Δ; mechanism-evidence score; capabilities (memory,
procedural reuse, information gathering, update); stale-state control;
Hermes+ mechanisms E1–E5 (plan, render, route, gate, close).

## Bearing on the record

CASE-tmpy1ebu calls it "PAST-Bench's fresh-session persistence ablations"
and QUESTION-tmp7a7l4 lists it among "prior art on self-improving agents".
The first is accurate. The second needs a qualification: the authors say
their setting "is not RSI in its full form"; it tests whether retained
experience helps, not whether the improver improves. It does not perform
the earlier-vs-later improver comparison that LIT-2273 calls a swap test.

- **CASE-tmpy1ebu** (inheritance arms: fresh instances inheriting knowledge
  only, organization only, both, or neither): **supports** the design's
  fresh-instance, matched on/off logic, and adds a measurement the case
  lacks, mechanism evidence that a gain went through the intended pathway,
  which would distinguish "inherited apparatus used" from a lucky score.
- **QUESTION-tmp7a7l4**: **qualifies** its prior-art list (as above):
  PAST-Bench is a precursor for the question's "Inheritance" level, not
  evidence about improved improvers.

- **QUESTION-108** and **CASE-091** (when a structured record beats a summary
  or transcript; memory ablations with information and budget controlled):
  §4.3 is direct evidence on the "structure" side: loose notes left stale and
  current values competing, and typed bindings with a superseded value
  rendered only as current fixed Memory; a correction left in an unstructured
  transcript fragment was re-read as stale. Supports the question's second
  mechanism (easing retrieval) for update tasks; not a test of a governed
  record.
- **CLAIM-tmp8qsef** (the record computes no withdrawals; retiring an
  entry reports dependants and leaves judgment): E5 overwrites the old value
  in place; PAST-Bench's update tasks are single-entity and do not test
  dependants, so it does not bear on the withdrawal question (LIT-2281 does).
- **CLAIM-184** (anchors entrench; retirement by status works only if
  superseded anchors stop attracting structure): the Update failure, old
  evidence "remains active after correction", is a small empirical instance of
  the claim's condition; E2's suppression of superseded entries at render time
  is the remedy the claim names. Supports, illustratively.
- Duplicate check: arXiv id and both titles not held elsewhere.

## Limitations

Synthetic families evaluated in isolation; LLM judge; headline Hermes+ gain
within noise; effects model- and capability-dependent; "online
self-evolution" only, not improver change.
