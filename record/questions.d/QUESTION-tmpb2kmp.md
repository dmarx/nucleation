---
status: Open
title: "Inside Kadanoff's kernel families, where each hidden spin couples to a block through a kernel of fixed form, does the exact trace condition force the coarse Hamiltonian to keep the relevant operators, or does some further stated condition still have to choose them?"
version: 1
tags:
- natural-sciences
- representation-learning
date: '2026-10-20'
line: 'formal-apparatus'
summary: >-
  The promotion condition formerly on [THEORY-202](../theory.d/THEORY-202.md). [THEORY-202](../theory.d/THEORY-202.md) was narrowed
  and promoted on 2026-10-20 ([ADR-047](../decisions.d/ADR-047.md) v2): over general Boltzmann
  machines, neither a matched partition function nor Kadanoff's exact
  trace condition fixes which variables a coarse-graining keeps. Its
  second counterexample needs visible–visible couplings, so it lies
  outside Kadanoff's kernel families. Whether the trace condition
  suffices inside those families is open.
---

# QUESTION-tmpb2kmp: Inside Kadanoff's kernel families, where each hidden spin couples to a block through a kernel of fixed form, does the exact trace condition force the coarse Hamiltonian to keep the relevant operators, or does some further stated condition still have to choose them?

## Why it is a question

[THEORY-202](../theory.d/THEORY-202.md) holds the general case. A joint Hamiltonian can match the
partition function with the wrong marginal. A hidden system that does not
interact with the visible one meets the trace condition exactly, with a
coarse Hamiltonian chosen freely. That second construction needs a
general Boltzmann machine. Kadanoff's schemes fix the kernel's form, so
that each hidden spin couples to a block, which excludes it. Whether
exactness inside those families keeps the relevant operators, or still
leaves the coarse variables free, is not settled by either source. Until
2026-10-20 it was [THEORY-202](../theory.d/THEORY-202.md)'s promote_when.

## What would answer it

- A treatment of variational renormalization, read and checked, that
  states a further condition under which a coarse-graining counts as a
  renormalization (a fixed kernel form, a short-range condition on the
  coarse Hamiltonian, or the preservation of named observables) and shows
  that the trace condition does not imply it inside Kadanoff's families.
- A proof that, inside those families, the trace condition does force the
  coarse Hamiltonian to keep the relevant operators.

What cannot settle it: more examples of coarse-grainings that preserve Z
or satisfy the trace condition.
