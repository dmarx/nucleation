---
status: Proposed
title: 'Still shows that, for a partially observable information engine whose memory is formed at one temperature and used to extract work at another, minimising the lower bound on dissipation over the memory map is the information bottleneck: keep the information about the work-relevant variable, discard the rest, with the temperature ratio as the trade-off'
version: 1
source:
- LIT-tmpsp5bi
tags:
- thermodynamics
- information-theory
date: '2026-11-19'
bears_on:
- QUESTION-tmprj00l
promote_when: >-
  An independent re-derivation or check of Eqs. (5)–(10) in the published
  PRL version, confirming the dissipation bound −Q ≥ k(T·I[M,X] −
  T'·I[M,Y]) under the stated assumptions (fixed preparation, unchanged
  marginals, memory map depending only on the observable data) and that
  its minimisation over p(m|x) is the information bottleneck objective
  with α = T'/T.
summary: >-
  From the reading of LIT-tmpsp5bi in NOTE-tmp9h01y. Still (arXiv
  1705.00612, 2017; Physical Review Letters 124, 050601, 2020). The letter
  extends Szilárd's engine to partial observability and two temperatures.
  Forming a memory costs at least kT·I[M,X], and extracting work recovers
  at most kT'·I[M,Y], where Y is what the extraction device can
  manipulate. Minimising the resulting dissipation bound over the memory
  map is exactly the information bottleneck, with the temperature ratio as
  its trade-off. The agent's action never changes the next cycle's data,
  so the result is a no-feedback baseline. Here because the exchange made
  it the bridge between memory and thermodynamics: it is the nearest prior
  result for QUESTION-tmprj00l and extends THEORY-026 to a cyclic engine.
  Read in its NOTE (arXiv v3).
---

# THEORY-tmp6miip: Still shows that, for a partially observable information engine whose memory is formed at one temperature and used to extract work at another, minimising the lower bound on dissipation over the memory map is the information bottleneck: keep the information about the work-relevant variable, discard the rest, with the temperature ratio as the trade-off

## The account

Forming a memory M of observable data X costs at least kT·I[M,X] of dissipated heat. Using it to extract work recovers at most kT'·I[M,Y], where Y is the part of the system the extraction device can manipulate. Isothermally, the irrelevant information I[M,X|Y] bounds dissipation from below. With two temperatures the bound is k(T·I_mem − T'·I_rel), and the memory map that minimises it solves the information bottleneck. A Szilárd–Carnot protocol saturates the bound, with efficiency η_C − (T/T')·I_irrel/I_rel.

## What it does not show

- It does not treat feedback. The system is re-prepared identically each cycle and its marginals never change, so the agent's action does not shape what it will see.
- "Relevant" is fixed by the extraction device and computed from observational p(y|x). Nothing here says which partition a physically costed memory keeps when observational and interventional relevance differ.
- It does not count the cost of revising or maintaining the memory, or of computing the encoder.
- The bounds are ensemble averages that one protocol saturates; real engines are not shown to approach them.
