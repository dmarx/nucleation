---
number: 343
status: Open
formerly:
- QUESTION-tmphbreu
title: 'Does a rerun of Sarkar, Mukherjee and Sato''s released harness, or an independent implementation, reproduce Table 1''s single-path, uniform and holonomy-weighted accuracies on S4 synchronization with outliers within their intervals, including the paired holonomy − uniform gains?'
version: 1
tags:
- network-science
- compositionality
date: '2026-10-30'
line: formal-apparatus
summary: >-
  The promotion condition formerly on [THEORY-1158](../theory.d/THEORY-1158.md), moved here when the
  status review of 2026-10-30 promoted it under [ADR-065](../decisions.d/ADR-065.md). The accuracies
  are the paper's, on 1000 instances per cell, and were not rerun; the AUC
  ceiling, which is arithmetic, was recomputed and needs no rerun.
---

# QUESTION-343: Does a rerun of Sarkar, Mukherjee and Sato's released harness, or an independent implementation, reproduce Table 1's single-path, uniform and holonomy-weighted accuracies on S4 synchronization with outliers within their intervals, including the paired holonomy − uniform gains?

## Why it is a question

[THEORY-1158](../theory.d/THEORY-1158.md) reports Table 1 of [LIT-1820](../literature.d/LIT-1820.md) (read in [NOTE-1331](../notes.d/NOTE-1331.md)): composition
through third vertices gains 26–45 points over a single path, and
Wilson-loop routing adds 0.6–7.8 more. The released code was not run, so
the accuracies are the paper's own. The second half of [THEORY-1158](../theory.d/THEORY-1158.md), the
AUC ceiling set by exactly flat clean data, was recomputed by enumerating
S4 and does not depend on a rerun.

## What would answer it

A rerun of the released harness, or an independent implementation, that
reproduces Table 1's single-path, uniform and holonomy columns within their
stated intervals, including the paired holonomy − uniform gains. A rerun on
new synthetic data built flat does not bear on the arithmetic half of
[THEORY-1158](../theory.d/THEORY-1158.md), which is already checked.
