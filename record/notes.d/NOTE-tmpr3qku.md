---
status: Skimmed
paper: LIT-2275
title: 'Mo, Zheng et al. — AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Skimmed on 2026-11-12 from https://arxiv.org/pdf/2609.07611. **Skimmed**
    (2026-11-12): abstract, §1, §2 (start), §3 overview and Figure 2, §7
    conclusion and limitations read; §§4–6 results read only through the
    introduction's and conclusion's statements of them; appendices not read. A
    delegated reader drafted the reading; quotations were rechecked by script
    against the downloaded copy, and any that did not match were kept as
    paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  A benchmark for LLM scientific ideation under two matched settings: Static
  (the model reads a curated set of reference papers and writes one
  80–150-word hypothesis) and Active (the model gets only the subfield name
  and a Semantic Scholar search tool with a 10-call budget, and must find
  its own evidence). Hypotheses are scored by an ensemble of LLM critics on
  originality, feasibility, clarity, impact and specificity, with
  originality argued against prior art retrieved at judging time. Across 33
  matched models and 40 densely scored subfields in five disciplines, Active
  evaluation separates models more than Static, improves about twice as fast
  across model generations, and its gain is capability-gated; the gain comes
  from grounding (feasibility, clarity, specificity) and leaves measured
  originality unchanged.
---
<!-- inactive-ok-file: THEORY-052 — Proposed; cited for what each holds, not as settled -->

# NOTE-tmpr3qku: Mo, Zheng et al. — AgentIdeaBench: Benchmarking Scientific Ideation in the Agent Era

## Contribution

A matched Static–Active protocol for ideation, and evidence that a curated
reading list understates and compresses differences that agent-controlled
retrieval reveals.

## Key results

- Abstract: "Active exploration reveals considerably more capability
  headroom"; "Performance scales about twice as fast as under static
  observation, and the exploration gain is capability-gated".
- Abstract: "The gain reflects better grounding, improving feasibility,
  clarity, and specificity while leaving measured originality unchanged under
  our critics."
- §1: Active improves "at +1.16 against +0.54 points per year" along the
  knowledge-cutoff axis.
- §7: "Retrieval equalizes idea diversity without equalizing quality".
- §7, limitation: "Every dimension score in this paper is an LLM judgment."
- §7, limitation: the Active condition bundles retrieval control with
  multi-turn interaction and tool competence; "Results here should be read as
  effects of agent-controlled retrieval as a whole rather than of retrieval
  control in isolation."
- §6 (end, "Three controls bound the claim"): the Scientific World Modeling
  refinement loop's pooled gain does not survive multiple-comparison
  correction, and "A compute-matched best-of-3 baseline meets or exceeds it".

## Assumptions

LLM critics, grounded by retrieved prior art, measure originality and
quality well enough to rank models (a small human pairwise-agreement study is
in Appendix B, not read); the Static reference sets are representative;
model knowledge cutoff indexes model generation.

## Concepts

Static observation vs. active exploration; literature-verified scoring;
critic ensemble; originality-dominant weighting; capability gating; headroom;
Scientific World Modeling (generation-time thought-experiment loop);
compute-matched baseline.

## Bearing on the record

The LIT says nothing beyond "cited ... as a reading"; the registration lists
it as work 43, and the exchange's content curation does not
cite it in any new entry. Its relevance to the luria program is indirect: it
is an evaluation-design paper on who controls the evidence an agent reasons
from. No characterization to correct.

The LIT names none, and no entry filed from the exchange
cites it.

- **[QUESTION-108](../questions.d/QUESTION-108.md)** (when a structured record does better than a summary,
  transcript or posterior) and **[CASE-091](../cases.d/CASE-091.md)** (memory ablation with information
  and budget controlled separately): the paper's matched design (same task,
  output format and scoring; vary only who controls the evidence) is the same
  shape as [CASE-091](../cases.d/CASE-091.md)'s information-equivalent vs. budget-equivalent arms, and
  its own caution, that "Active" bundles retrieval control with interaction
  and tool competence, is the confound [CASE-091](../cases.d/CASE-091.md) controls for. A methodological
  parallel; it does not test records. Leaves open.
- **[CLAIM-266](../claims.d/CLAIM-266.md) / [CLAIM-149](../claims.d/CLAIM-149.md)** (probes that train cannot certify): every score is
  an LLM judgment; the paper grounds originality in retrieved prior art to
  reduce judge bias, which is a partial response of the kind those claims call
  for. Illustrative only.
- "Ideation" hits ([NOTE-440](NOTE-440.md), [NOTE-467](NOTE-467.md), [THEORY-052](../theory.d/THEORY-052.md), etc.) were
  not about LLM ideation benchmarks. Duplicate check: arXiv id and title not
  held elsewhere.

## Limitations

Skimmed only; results sections and appendices unread. Scores are LLM
judgments; Active bundles several capabilities; the world-modeling extension
is unconfirmed by the authors' own controls.
