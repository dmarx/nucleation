---
number: 92
status: Proposed
formerly:
- CLAIM-tmpqz0mv
title: 'Translation can be posed as a context-indexed information bottleneck: compress the source while preserving information about the responses in each measurement context separately'
version: 1
role: thesis
defeated_if: >-
  The context-indexed objective selects the same renderings as a
  rate–distortion objective with a fixed pragmatic distortion, so that
  indexing by context adds nothing.
tags:
- information-theory
- philosophy-of-language
date: '2026-10-08'
line: pragmatic-transport
grounds:
- LIT-338
- THEORY-163
summary: >-
  A86 §2, kept in C6 Appendix C with a sharper caveat, recovered. The
  manuscript keeps the caveat (§5) and cites Tishby, Pereira and Bialek
  in its references, but states no bottleneck anywhere in its text.
---
<!-- inactive-ok-file: THEORY-163 — Proposed; colour naming near the information-bottleneck bound, cited as the nearest precedent, not as settled -->

# CLAIM-092: Translation can be posed as a context-indexed information bottleneck: compress the source while preserving information about the responses in each measurement context separately

## The claim

A86 §2: min I(U;V) − β Σ_C w_C I(V;Y_C), a bottleneck whose relevance variables
are the responses Y_C in each context, with the caveat that it does "**not**
presume that every locally contextual measurement admits a single joint
assignment." A86 used it to argue that a lexically distant refrain can be "a
more efficient representation of a communicative act than a literal
translation". C6 Appendix C: "The Y_C in different incompatible contexts must
not silently be collected into one globally joint random vector. An
information-bottleneck objective can instead sum context-indexed mutual
informations computed in distinct joint experiments, or optimize an explicitly
sampled measurement-context variable."

## Where it went

The manuscript §5 keeps the caveat ("Uncritically writing I(V;Y_1,...,Y_n) would
assume precisely the global representation the sheaf model is intended to test")
and drops the objective. That leaves Tishby, Pereira and Bialek ([LIT-338](../literature.d/LIT-338.md)) in the
reference list with nothing citing them, as the workbench entry of 2026-10-09
found. Nothing argued against the objective.

## Correction, 2026-10-09

The bottleneck is in C7, in Appendix C, which the extracted manuscript omits:
"A weighted bottleneck objective may sum information terms across separately
elicited contexts, but that sum is a designed scalar objective, not an assertion
that the Y_C admit a common joint distribution." So Tishby, Pereira and Bialek are
cited by the full draft's appendix, though not by name and not in its body. What
was dropped is the objective's place in the main argument, not the objective.

## The nearest precedent, and what it implies

Zaslavsky et al. ([LIT-810](../literature.d/LIT-810.md), [THEORY-163](../theory.d/THEORY-163.md)) apply the bottleneck to
word meanings, with one relevance variable rather than a context-indexed
one. Their formulation also sharpens this claim's defeat condition. Once
meanings are distributions and distortion is KL divergence, the bottleneck
*is* rate–distortion with that distortion. A context-indexed bottleneck
therefore adds something only if the indexing changes the distortion.
