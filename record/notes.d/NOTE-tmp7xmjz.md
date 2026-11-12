---
status: Read
paper: LIT-2285
title: 'Romera-Paredes et al. — Mathematical discoveries from program search with large language models'
version: 1
history:
- version: 1
  date: '2026-11-12'
  note: >-
    Read on 2026-11-12 from
    https://www.nature.com/articles/s41586-023-06924-6.pdf. A delegated reader
    drafted the reading; quotations were rechecked by script against the
    downloaded copy, and any that did not match were kept as paraphrase
    without quotation marks.
date: '2026-11-12'
summary: >-
  FunSearch pairs a frozen, pretrained code LLM with a programmatic
  evaluator in an evolutionary loop. The user supplies an `evaluate`
  function and a program skeleton; the LLM proposes new versions of the one
  function to evolve (e.g. a priority function), proposals are run and
  scored, and high scorers are kept in a programs database organised as
  islands and fed back as prompts ("best-shot prompting"). Applied to the
  cap set problem it found a 512-element cap set in dimension 8, larger than
  previously known, and improved lower bounds on the asymptotic capacity via
  admissible sets; applied to online bin packing it found heuristics beating
  first fit and best fit.
---
<!-- inactive-ok-file: CASE-tmpy1ebu — filed from the exchange "luria experiment design", Proposed or Deferred; cited as filed alongside this entry -->

# NOTE-tmp7xmjz: Romera-Paredes et al. — Mathematical discoveries from program search with large language models

## Contribution

Evidence that an LLM, constrained by an evaluator it cannot influence, can contribute verifiably
new results on established open problems, and a method whose correctness guarantee comes wholly
from the evaluator.

## Key results

1. Method (abstract): "an evolutionary procedure based on pairing a pretrained LLM with a systematic evaluator".
2. Role of the evaluator (intro): the LLM provides creative solutions "with an evaluator, which guards against confabulations and incorrect ideas".
3. Cap set (main text): "in dimension n = 8, FunSearch found a larger cap set than what was previously known" (512 vectors, Fig. 4).
4. Programs, not solutions (abstract): FunSearch "searches for programs that describe how to solve a problem, rather than what the solution is".
5. LLM's role (Discussion): "the LLM should instead be seen as a source of diverse (syntactically correct) programs with occasionally interesting ideas".
6. Scope (Discussion): FunSearch works best with "(1) availability of an efficient evaluator; (2) a 'rich' scoring feedback quantifying the improvements (as opposed to a binary signal) and (3) ability to provide a skeleton with an isolated part to be evolved"; theorem proving "falls outside this scope".

## Assumptions

Problems that are "easy to evaluate" though hard to solve; the evaluator is correct, fixed and
outside the search; a human-written skeleton isolates what may change.

## Concepts

Program search; evaluator as guard against confabulation; best-shot prompting; islands model;
skeleton; Kolmogorov-compressed inductive bias; interpretability of discovered programs.

## Bearing on the record

No new entry on the branch cites [LIT-2285](../literature.d/LIT-2285.md); the exchange named it as reading (the registration
curation lists it). The LIT's tags (mathematics, agency) fit. Nothing to correct beyond metadata.

- **[CASE-tmpy1ebu](../cases.d/CASE-tmpy1ebu.md)** (outer evaluation boundary: agents may revise operational tests, never hidden
  ground truth): **supports** as a clean positive case: all of FunSearch's reliability comes from
  an evaluator the search cannot edit, and the authors say it is limited to problems that have one.
- **[CLAIM-266](../claims.d/CLAIM-266.md)** (probes that supply the training signal cannot certify what the system preserves):
  **consistent, boundary case**: in FunSearch the probe *is* the target (the score is the
  mathematical quantity), so there is nothing beyond the probe to preserve; this is the
  condition under which optimizing against the probe is safe.
- **[QUESTION-tmp7a7l4](../questions.d/QUESTION-tmp7a7l4.md)**: **does not bear** on improving the improver: the LLM, prompt strategy and
  evaluator are fixed; only the population improves.
- **[QUESTION-108](../questions.d/QUESTION-108.md)** (when a structured record does better than a summary or transcript):
  **leaves open**; the programs database is a structured store of scored candidates, but the
  paper does not compare it with an unstructured alternative.

## Limitations

Supplementary Information (full results, prompts, ablations) not read; claims about asymptotic
bounds taken from the main text only.
