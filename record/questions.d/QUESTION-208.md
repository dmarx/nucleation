---
number: 208
status: Open
formerly:
- QUESTION-tmpog8lp
title: "Does the expected structure function of a computable i.i.d. source match its distortion-rate function, with the right-hand step of Grünwald and Vitányi's Theorem 6.27 filled in?"
version: 1
tags:
- information-theory
- learning-theory
date: '2026-10-20'
line: formal-apparatus
summary: >-
  Filed when the promotion audit (batch 050, [ADR-047](../decisions.d/ADR-047.md) v2) narrowed and
  promoted [THEORY-244](../theory.d/THEORY-244.md) to the entropy and mutual-information bridges, which
  it re-derived. The distortion-rate bridge rests on a step in Theorem
  6.27 that the reading found asserted, so it left the title. The former
  promote_when's clause for it is held here.
---

# QUESTION-208: Does the expected structure function of a computable i.i.d. source match its distortion-rate function, with the right-hand step of Grünwald and Vitányi's Theorem 6.27 filled in?

## Why it is a question

[THEORY-244](../theory.d/THEORY-244.md) now states two expectation bridges as re-derived: entropy and
mutual information are the expectations of their Kolmogorov counterparts to
within K(f). Grünwald and Vitányi ([LIT-224](../literature.d/LIT-224.md), read in [NOTE-776](../notes.d/NOTE-776.md)) also state a
third. For a recursive distortion d, a total recursive source f and m
i.i.d. repetitions, the expected structure function brackets the
distortion-rate function, (1/m) E h_x(mR + K(f, d, m, R) + O(log n)) ≤
D*_m(R) ≤ (1/m) E h_x(mR), and the per-symbol limit equals D*(R) (Theorem
6.27, Corollary 6.29). The reading found the right-hand step asserted: it
identifies h_x(mR) with the radius of x's sphere in a canonical cover, with
complexity conditioned on mR where h_x is unconditional. The arXiv record
carries the authors' own warning about errors in the draft.

## What would answer it

A published version of Theorem 6.27, or of the Vereshchagin–Vitányi
individual rate–distortion paper it follows, that fills in the right-hand
inequality, or a derivation the record can follow step by step. It is
answered no by a computable source f for which expected Kolmogorov
complexity exceeds entropy by more than K(f) plus a constant (which would
also break [THEORY-244](../theory.d/THEORY-244.md)'s first bridge), or by a recursive source and
distortion for which (1/m) E h_x(mR) fails to converge to D*(R).
Empirical compression ratios cannot settle it, since a real compressor
gives only upper bounds on K.
