---
status: Open
title: "Does causal emergence of effective information in Hoel, Albantakis and Tononi's temporal and spatio-temporal macros survive a common intervention distribution, or does it come from comparing a macro step that spans several micro steps with a single micro step?"
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Filed at the rejection of THEORY-787 on 2026-10-30 (owner's direction),
    for the one case THEORY-1167's bound does not reach. It refines
    QUESTION-204.
tags:
- causality
- information-theory
date: '2026-10-30'
line: 'formal-apparatus'
refines:
- QUESTION-204
summary: >-
  THEORY-1167 bounds the effective information of a coarse-graining of one
  transition by the micro's. LIT-1038's temporal and spatio-temporal macros
  are not of that form: the macro effect lies several micro steps ahead,
  and the comparison is with one micro step. The question is whether their
  positive causal emergence survives a common distribution, and whether
  that comparison is a fair one.
---
<!-- inactive-ok-file: THEORY-787 — Rejected; the account whose remaining case this question holds -->

# QUESTION-tmpzfd02: Does causal emergence of effective information in Hoel, Albantakis and Tononi's temporal and spatio-temporal macros survive a common intervention distribution, or does it come from comparing a macro step that spans several micro steps with a single micro step?

## Why it is a question

THEORY-787 was rejected on 2026-10-30, because its own condition was met
for a coarse-graining of one transition (THEORY-1167). LIT-1038 also
reports emergence in macros of time. In one, a second-order Markov
element answers a two-spike burst. In the other, nine heterogeneous
elements are coarse-grained in space and time together (NOTE-726). There
the macro effect is k micro steps ahead, and LIT-1038 compares it with the
micro mechanism over one step. THEORY-1167's "What this does not say"
leaves this case out, and so does CLAIM-tmpxk5cy.

## What would answer it

There are two comparisons, and they need to be kept apart.

- **Against the k-step micro mechanism.** Take the macro map f applied to
  X_t and to X_{t+k}, scored with the same distribution over micro states.
  Data processing gives I(f(X_t); f(X_{t+k})) ≤ I(X_t; X_{t+k}), as in
  THEORY-1167. That is expected to settle this comparison against
  emergence. It has not been checked on LIT-1038's examples, and the
  second-order element needs its state space defined so that the map is
  a function of the micro state.
- **Against the one-step micro mechanism, LIT-1038's comparison.** The
  k-step and the one-step micro mechanisms can differ in effective
  information either way. So a macro gain over the one-step micro may
  measure the change of horizon, not the coarse-graining. The answer is a
  recomputation of LIT-1038's two examples under a common distribution,
  against both the one-step and the k-step micro mechanism. Each
  comparison would then be credited to the horizon or to the coarse-
  graining.
