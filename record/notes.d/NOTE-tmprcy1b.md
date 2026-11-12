---
status: Skimmed
paper: LIT-2324
title: 'Liu, Yang et al. — ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Skimmed on 2026-11-12 from https://arxiv.org/pdf/2503.21248. **Skimmed**
    (abstract, §1, §3.1 assumption, §4 results text, §5 analysis, §6
    conclusion, Limitations read; tables and appendices not read closely).
    Read 2026-11-12. A delegated reader drafted the reading; quotations were
    rechecked by script against the downloaded copy, and any that did not
    match were kept as paraphrase without quotation marks.
date: '2026-11-12'
summary: >-
  ResearchBench evaluates LLMs on three sub-tasks into which Yang et al.
  (2025b) decompose hypothesis discovery: retrieving "inspirations" (papers
  not known to be related to the research question), composing hypotheses
  from background plus inspirations, and ranking hypotheses. The
  decomposition is claimed "sufficient": solving the sub-tasks perfectly
  solves discovery, under the assumption that most hypotheses arise from a
  background plus inspirations. An LLM agent extracts question, background,
  inspirations and hypothesis from 1,386 papers (2024 onward, 12
  disciplines).
---
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmprcy1b: Liu, Yang et al. — ResearchBench: Benchmarking LLMs in Scientific Discovery via Inspiration-Based Task Decomposition

## Contribution

- A large, contamination-resistant, automatically renewable benchmark for the three
  sub-tasks.
- An analysis of inspiration retrieval as an out-of-distribution task, with a scaling
  plateau near 70B.

## Key results

1. Abstract: the sub-tasks are "a sufficient set of scientific discovery
   sub-tasks—inspiration retrieval, hypothesis composition, and hypothesis ranking—where
   sufficient means that perfectly solving these sub-tasks perfectly solves the overall
   discovery task." (PDF text has line-break hyphens; quote checked on the joined text.)
2. §1, p. 1: the decomposition "is viable under the fundamental assumption that most
   hypotheses originate from a research background combined with inspirations."
3. §3.1: support for the assumption across disciplines is by consultation: "After extensive
   discussions with researchers in other disciplines ... we find that this assumption is
   largely and widely true across disciplines."
4. §4.1: "even in the final round (4% retained), where only 3 papers are selected, accuracy
   remains above 40%, with GPT-4o leading at 45.65%."
5. §4.1: retrieval ability is "stuck in a bottleneck at around 70B parameters."
6. §4.3: "many LLMs have strong position bias"; Llama-3.1-8B "reaches self-contradictory
   results 91.67% of the time" when a pair is compared in both orders.
7. §5.2, error analysis of 100 failures per task: for retrieval "56% of errors were because
   the model judged relevance only by title or abstract overlap"; for ranking "83% of errors
   arise from how models process the order of comparison rather than the content itself."
8. §6: "LLMs show strong retrieval but only moderate composition and ranking, indicating
   they capture useful associations yet lack deeper integrative reasoning."
9. Limitations: the benchmark "is also not designed to evaluate a discovery system’s
   ability ... to leverage external experimental feedback for hypothesis updating".

## Assumptions

- The background-plus-inspirations account of where hypotheses come from (Koestler-style
  association), asserted sufficient; supported by cognitive-science citations and
  discussion with researchers, not tested.
- The published paper's own hypothesis is the ground truth; LLM-extracted components are
  accurate (expert validation reported, not checked here).
- Papers from 2024 onward are outside training data.

## Concepts

inspiration retrieval; hypothesis composition; hypothesis ranking; sufficient
decomposition; hit ratio; negative inspirations at three distances; position bias;
"research hypothesis mines"; contamination-free renewal.

## Bearing on the record

The LIT records only that it was cited (A14). Nothing to correct. One caution for any
later use: the "sufficient" decomposition is the authors' assumption (results 2–3), and
the paper itself excludes revision of hypotheses on experimental feedback (result 9), so it
does not measure theory revision.

The LIT names no code and no new entry cites [LIT-2324](../literature.d/LIT-2324.md). Bearings found:
- **[QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md) / [CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md)**: no bearing (single-shot generation, no
  improvement loop).
- **[LIT-2321](../literature.d/LIT-2321.md) (HypoBench), [LIT-2307](../literature.d/LIT-2307.md), [LIT-2329](../literature.d/LIT-2329.md), [LIT-tmpsxqr6](../literature.d/LIT-tmpsxqr6.md)**: a family of AI
  hypothesis-generation evaluations; ResearchBench tests generation from literature
  (closer to Si et al.'s ideation than to HypoBench's explanation of data), and excludes
  feedback-driven updating, which [LIT-2329](../literature.d/LIT-2329.md) measures.
- **[CLAIM-266](../claims.d/CLAIM-266.md)** (Active) and **[QUESTION-271](../questions.d/QUESTION-271.md)** (Open): *leaves open*; the 83% order-driven
  ranking errors (result 7) are an evaluator-reliability finding that would matter to any
  design using an LLM as hypothesis ranker, but no optimization against the ranker occurs.

## Limitations

Tables not checked number by number; the extraction framework's accuracy and the
negative-inspiration construction were only skimmed. The ACL Anthology version was not
compared with arXiv v3.
