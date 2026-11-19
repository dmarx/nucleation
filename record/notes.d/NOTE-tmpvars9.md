---
status: Read
paper: LIT-tmp1zmvj
title: 'He and colleagues — Is Grokking Worthwhile? Functional Analysis and Transferability of Generalization Circuits in Transformers'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2601.09049v1 (PDF):
    the whole paper, figures read from page images; the code README for
    model settings. Running notes on the branch
    claude/readers/task-composition (ADR-108). Quotations rechecked by the
    filer by script against the downloaded text.
date: '2026-11-19'
summary: >-
  Grokking read as integrating facts into an early reasoning path; a
  shortcut (fake grokking) at high first-stage accuracy that fails to
  compose new facts. Organizations compared, not matched; no intervention;
  single runs.
---
<!-- inactive-ok-file: LEAD-tmphfbq0 CLAIM-754 CLAIM-756 LEAD-tmpadknn — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpvars9: He and colleagues — Is Grokking Worthwhile? Functional Analysis and Transferability of Generalization Circuits in Transformers

## Key results

1. **Same path, faster.** With full augmentation, "the final model trained
   with fewer steps follows the same reasoning path as naturally grokked
   models" (§3).
2. **Grokking reinterpreted.** "grokking is the process of integrating
   memorized atomic facts into an naturally established reasoning path"
   (abstract).
3. **Fake grokking.** With second-hop-only augmentation, "their final
   answer to composition queries does not come through a correctly
   recovered bridge entity" (§4).
4. **Later acquisition.** Fake-grokked models, "despite achieving
   comparable performance on original OOD facts, fail to adapt to
   compositional reasoning mixing new and old facts" (§5.2); by the
   reader's reading of Fig. 2 the fake model is ahead on first-stage
   held-out accuracy, not matched. "when a novel fact is required in the
   second hop, models fail to complete the inference despite correctly
   recovering the bridge entity" (§5.2).
5. **Transfer equal across routes.** "the model trained under full
   supervision exhibits identical transferability when applied to new
   facts compared to a natural grokked one" (§3).
6. **Remedy asserted, not run.** "models still require either (i) an
   additional grokking phase, or (ii) substantially more finetuning data
   covering the new facts and their compositions" (§5.2).

## Bearing on the record

- **LEAD-tmphfbq0**, the closest to its part (b): a circuit and a shortcut,
  each followed into a later acquisition, with the organization predicting
  the later curve; the shortcut has higher first-stage accuracy and learns
  worse later. No intervention, no cost number, single runs. A testbed for
  (c), the reader's suggestion: ablate or patch the bridge layers before
  fine-tuning.
- **CLAIM-754**, an illustration: the operational and developmental
  frontiers come apart (the fake model ahead now, behind later).
- **CLAIM-756**, weak illustration: an organization's value shows in later
  acquisition, not first-stage accuracy; no costs.
- **CLAIM-519**, supports: the same behaviour with different internal
  paths; the paper's own mechanism evidence is observational.
- **LEAD-tmpadknn**, background: a case of similar present competence
  with different later acquisition.
- **CLAIM-758**, qualifies weakly: longer training (grokking) does not raise
  later cost here.
- **QUESTION-039** and **THEORY-039**, parallel: staged events, saturation,
  then bridge recovery, then integration.
- **QUESTION-360**, parallel: transfer to new facts as the test of a
  reusable organization.
- **CASE-294**, design caution: a held-out two-hop family built with new
  second-hop facts could fail for reasons unrelated to checkpoint age.
- **THEORY-984**, parallel: an internal bridge found with interventions,
  which this paper lacks.

## Limitations

Single runs; no model size in the text; two conditions undefined; first
stage not matched; no numeric cost; one architecture family and one
synthetic graph. The record lacks the work this builds on (Wang and
colleagues 2024, on grokking of implicit reasoning).
