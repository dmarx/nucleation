---
status: Read
paper: LIT-tmpe21sz
title: 'Ma and colleagues — At Which Training Stage Does Code Data Help LLMs Reasoning?'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2309.16298v2 (PDF):
    §§1–5 and appendices A–H; references only to check citations. Running
    notes on the branch claude/readers/scheduling-followups (the procedure
    proposed in pull request 537). Quotations rechecked by the filer by
    script against the downloaded text.
date: '2026-11-19'
summary: >-
  Code at pretraining, at instruction tuning and both; a code-decreasing
  schedule tried only at instruction tuning. Unmatched comparisons, single
  runs, tiny test sets.
---
<!-- inactive-ok-file: LEAD-tmpjdtrl THEORY-tmpd6smn CLAIM-596 — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmphkwyp: Ma and colleagues — At Which Training Stage Does Code Data Help LLMs Reasoning?

## Key results

1. The baseline is a released checkpoint: "we use the open-sourced
   PanGu2.6B and PanGu13B of the PanGu-α team"; the code model is trained
   "from scratch on the mixed code data for comparison" (§1.1), with a
   different tokenizer.
2. Claim: adding code in pretraining "may be more effective than
   increasing the model parameter size" (§3.3.1); Table 2 contradicts it on
   Logic, a set of about 22 items.
3. Schedule, instruction tuning only: "using a higher code data ratio in
   the early stage and gradually reducing the code data ratio in the later
   stage achieved the best results in code question answering (CosQA) and
   code generation (MBPP) tasks"; "we leave the validation of this phase to
   later work" (§3.3.4).

## Bearing on the record

- **LEAD-tmpjdtrl**, code first: does not support it; code is never
  strictly first and no later cost is measured.
- **THEORY-tmpd6smn** (Liu and colleagues), the useful bearing: the record
  already holds a better-controlled answer, at matched tokens, to the
  pretraining-stage question this paper leaves open.
- **CLAIM-596**, by analogy: end scores cannot tell a changed rate of later
  learning from a head start.
- **CLAIM-756**, **QUESTION-039**, **THEORY-tmpd6l4a**, **THEORY-tmpk9cmk**:
  background.

## Limitations

Unmatched data, tokens, compute and tokenizer; one code model; single runs;
small test sets; gold rationales in the input for the "with CoT" results.
