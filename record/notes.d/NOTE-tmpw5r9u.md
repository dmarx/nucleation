---
status: Read
paper: LIT-tmpofzg6
title: 'Akter and colleagues — Front-Loading Reasoning: The Synergy between Pretraining and Post-Training Data'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2510.03264v1 (HTML,
    CC BY 4.0): §§1–7 and appendices B and C in full; references skimmed.
    Running notes on the branch claude/readers/scheduling-followups (the
    procedure proposed in pull request 537). Quotations rechecked by the
    filer by script against the downloaded text.
date: '2026-11-19'
summary: >-
  Reasoning data placed in pretraining against SFT only: a lasting
  advantage after SFT and RL that doubled SFT does not erase. Total
  reasoning data not matched; final scores; single runs.
---
<!-- inactive-ok-file: CLAIM-756 CLAIM-758 THEORY-tmpd6smn — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpw5r9u: Akter and colleagues — Front-Loading Reasoning: The Synergy between Pretraining and Post-Training Data

## Key results

1. The question: "Is adding reasoning data earlier during pre-training any
   better than introducing it during post-training, when the token counts
   are controlled?" (abstract). Only pretraining tokens (1T) are fixed;
   reasoning arms carry about 200B reasoning tokens that the baseline lacks.
2. "SFT is not a substitute for a strong reasoning foundation built during
   pretraining" (§4). Given twice the SFT data, "this enhanced baseline
   still fails to match the performance of even our weakest
   reasoning-pretrained model" (§5).
3. Quality in SFT: "blindly scaling diverse reasoning data during SFT
   degrades performance" (§5).
4. Redundancy: seeing the same data in both phases helps, "indicating that
   the second exposure reinforces rather than overwrites learning" (App. C).

## Bearing on the record

- **CLAIM-756**, weak qualification: a later acquisition goes further
  after an earlier one, in final scores; the earlier phase's cost is folded
  into a fixed pretraining budget and never valued.
- **CLAIM-758** and **THEORY-2006**, qualifies: no worsening of later SFT
  from reasoning-rich pretraining at 8B and 1T in one run per arm; later SFT
  on mixed-quality data erodes the earlier advantage, a weak parallel to
  collateral forgetting.
- **THEORY-tmpd6smn** (Liu and colleagues), the closest parallel:
  specialized data substituted into pretraining helps later fine-tuning.
- **CLAIM-754**, by analogy: pretraining choices that barely move base
  scores move what SFT can reach.
- **QUESTION-039**, **TERM-131**, **THEORY-tmplutfz**: background.

## Limitations

Single runs; total reasoning data unmatched; headline percentages do not
reproduce exactly from the tables; no decontamination stated.
