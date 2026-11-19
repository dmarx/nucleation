---
status: Read
paper: LIT-tmps3oxd
title: 'Blakeney and colleagues — Does your data spark joy? Performance gains from domain upsampling at the end of training'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2406.03476v1 (PDF):
    all 13 pages, including appendix A. Running notes on the branch
    claude/readers/scheduling-followups (the procedure proposed in pull
    request 537). Quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  End-of-training upsampling of domain and code data at fixed tokens:
  gains on hard benchmarks, an intermediate best duration, and dataset
  ablations run cheaply in the late phase. One run each.
---
<!-- inactive-ok-file: THEORY-tmpd6smn CLAIM-756 — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmpfwg5y: Blakeney and colleagues — Does your data spark joy? Performance gains from domain upsampling at the end of training

## Key results

1. At 20 per cent: "DU: 6.90 pp on MMLU, 8.26 pp on GSM8K, 6.17 pp on
   HumanEval, and 3.95 pp on the Gauntlet v0.3" (Fig. 2).
2. Duration: "MMLU peaks at 10% and Gauntlet v0.3 Core Average peaks at
   20%" (§3.3); GSM8K "improves monotonically as duration of domain
   upsampling is increased" (§3.4).
3. Late against throughout is inferred, not run: "We do not rule out that
   there is an alternate mix that achieves similar performance as the 20%
   domain upsampling experiment when trained for the full training
   duration" (§3.3).
4. Without the math subsets, "performance is worse then the baseline model
   with no domain upsampling" (§3.4).

## Bearing on the record

- **[THEORY-tmpd6smn](../theory.d/THEORY-tmpd6smn.md)** (Liu and colleagues), qualifies most directly: here a
  late phase heavy in code raises code and math scores of a 7B base model;
  Liu found late code worse than none for small models after fine-tuning.
  A plasticity-window reading of Liu should not be generalized to the
  conclusion that late specialized data hurts without these qualifications.
- **[CLAIM-756](../claims.d/CLAIM-756.md)**, background: the late phase is the acquisition, judged by
  final score; nothing earlier is varied.
- **[THEORY-tmplutfz](../theory.d/THEORY-tmplutfz.md)**, parallel; **[THEORY-tmp0lbb1](../theory.d/THEORY-tmp0lbb1.md)**, **[THEORY-tmpd6l4a](../theory.d/THEORY-tmpd6l4a.md)**,
  **[QUESTION-039](../questions.d/QUESTION-039.md)**, **[CASE-294](../cases.d/CASE-294.md)**: parallels or background.

## Limitations

One model, one budget, one base run; datasets unnamed; schedule role
unaddressed; the savings claim compares across systems.
