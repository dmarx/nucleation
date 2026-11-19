---
status: Read
paper: LIT-tmp9r948
title: 'Feng, Prabhumoye and colleagues — Maximize Your Data''s Potential: Enhancing LLM Accuracy with Two-Phase Pretraining'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2412.15285v1 (PDF):
    §§1–7, limitations, ethics and appendix text in full; per-benchmark
    tables skimmed. Running notes on the branch claude/readers/scheduling-
    followups (the procedure proposed in pull request 537). Quotations
    rechecked by the filer by script against the downloaded text.
date: '2026-11-19'
summary: >-
  Two-phase blends against random order of the same blend at fixed tokens:
  a small gain, mostly in math and code, confounded with an end-of-run
  anneal; no cost measure; single runs.
---
<!-- inactive-ok-file: CLAIM-756 THEORY-tmpd6smn THEORY-tmpd6l4a — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmp58c4t: Feng, Prabhumoye and colleagues — Maximize Your Data's Potential: Enhancing LLM Accuracy with Two-Phase Pretraining

## Key results

1. Random-order control: "The weight for each dataset here is the same as
   our two-phase approach but the order in which the the dataset is seen
   during pretraining is random." (§2)
2. Headline: two-phase "outperforms random data ordering and natural
   distribution of tokens by 3.4% and 17% on average accuracies"
   (abstract), 52.86 against 51.12 points (Table 4), from the best of six
   phase-2 lengths; at the standard 30 per cent the gain is 1.16 points.
3. Where it falls: "tasks such as code and math are sensitive to the
   ordering of high-quality data in the second phase" (§4).
4. Length: "Pretraining with the P2 blend for the final 40% gives the best
   results." (§5.3)
5. Confound: "We start P2 with the intermediate LR reached at the end of
   P1 , and anneal using cosine LR decay to 3e-6" (App. A); the random
   baseline's schedule is not stated.

## Bearing on the record

- **[CLAIM-756](../claims.d/CLAIM-756.md)**, background: order at fixed total data, final accuracy, no
  later cost with and without an earlier acquisition.
- **[THEORY-tmpd6smn](../theory.d/THEORY-tmpd6smn.md)** (Liu and colleagues), qualifies: code and math
  concentrated late help base-model code and math scores; Liu's late code
  hurt fine-tuning. Different targets; neither controls the schedule.
- **[THEORY-tmpd6l4a](../theory.d/THEORY-tmpd6l4a.md)** (Skill-it), by analogy: phasing by quality beats
  random order, where skill sequencing did not; different orderings.
- **[THEORY-tmp0lbb1](../theory.d/THEORY-tmp0lbb1.md)**, **[THEORY-tmplutfz](../theory.d/THEORY-tmplutfz.md)**, **[CLAIM-596](../claims.d/CLAIM-596.md)**, **[THEORY-2006](../theory.d/THEORY-2006.md)**:
  parallels; phase 2 past 40 per cent degrades every category.
- **[THEORY-tmprqq7k](../theory.d/THEORY-tmprqq7k.md)**: a name collision only.

## Limitations

Single runs; headline chosen on the evaluation; schedule confound; Table
14's 0 per cent row not comparable with the others; proprietary data.
