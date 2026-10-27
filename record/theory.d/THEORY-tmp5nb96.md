---
status: Active
title: 'Robinson''s claim that sheaves are the canonical data structure for sensor integration rests on an axiomatization, not a theorem: six axioms are posited as what an integrated sensor system must be and a sheaf is defined as whatever satisfies them, the paper calls sheaves one of many co-universal information representations, and its consistency and fusion tools need only a presheaf'
version: 1
tags:
- mathematics
- information-theory
date: '2026-10-27'
source:
- LIT-tmpn521a
summary: >-
  Robinson (2017), LIT-tmpn521a, read in NOTE-tmpdshmx from arXiv v3. A
  textual finding about the paper, Active as such. The word "canonical" is
  never defined for sheaves as a sensor model; its technical uses are the
  standard ones for cohomology. It does not say that sheaves are a poor
  model, or that no theorem of this kind could be proved.
---
<!-- inactive-ok-file: CLAIM-tmpdjt64 — Proposed; the claim that drew on the paper's word, cited as open -->

# THEORY-tmp5nb96: Robinson's claim that sheaves are the canonical data structure for sensor integration rests on an axiomatization, not a theorem: six axioms are posited as what an integrated sensor system must be and a sheaf is defined as whatever satisfies them, the paper calls sheaves one of many co-universal information representations, and its consistency and fusion tools need only a presheaf

## Source

Robinson (2017), LIT-tmpn521a, §§1, 3–5 of arXiv 1603.01446v3 (pp. 1–2,
7–18, 22–29, 32); the arXiv abstract. Read in NOTE-tmpdshmx.

## What was actually shown

**The argument for "canonical" is a definition.** Section 3 opens: "we
posit a set of six Axioms to specify what this integrated system must be. A
sheaf is precisely any mathematical object satisfying all six Axioms. We
motivate the Axioms by way of examples" (pp. 7–8). The axioms are the
definition of a sheaf of pseudometric spaces on a topology, motivated one
at a time by the search-and-rescue and coin-counting examples. The paper
also matches Wald's definition of data fusion and says "This article shows
that this is precisely what is provided by sheaf theory" (p. 2).

**The word, where it occurs.** Sheaves "provide a common, canonical
language for heterogeneous datasets" (p. 1); "The foundational and
canonical nature of sheaves means that existing approaches ... already
illuminate some portion of sheaf theory" (p. 2); "Sheaf theory provides
canonical computational tools" (p. 4). Its precise uses are standard
mathematics: cohomology is "a canonical family of invariants" and the
Godement resolution is "the canonical ... resolution" (p. 32). No
statement, proposition or theorem says sheaves are unique, initial,
terminal or universal among sensor-integration models. The arXiv abstract
calls the paper "expository": its purpose is "to explain why sheaves are
the canonical data structure".

**The paper's own concession.** "Although there are many co-universal
information representations (of which sheaves are one), the stumbling
block for integration approaches is the lack of theoretically-motivated
computational approaches" (p. 29). The advantage claimed is the tooling,
cohomology above all, not uniqueness.

**The limits it states.** Axiom 3 "is a true limitation" (Remark 7, p. 12).
Axiom 6 "can always be satisfied if S(U₁ ∪ U₂) has not been constrained by
the sensor models", by defining the union's observations as the fibre
product, eq. (1) (p. 18). Relational databases "often do not satisfy Axiom
6" (Example 17, p. 22). The claim that Axiom 6 is "a necessary and
sufficient constraint" (p. 17) is asserted, not proved.

**The tools need less.** The consistency radius (Definition 20), the
distance bound (Proposition 23) and data fusion (Problem 19) are all stated
for a presheaf, Axioms 1–5 (pp. 22–25; THEORY-tmpiycpt). The sheaf
condition and linearity (Axiom 7) enter in Section 5, for cohomology.

## What this does not say

- **That sheaves are a poor model of sensor systems.** The worked examples
  fit the axioms, and the cohomology examples (30–32) show what the extra
  structure buys.
- **That no precise sense of "canonical" exists.** A universal property
  for some category of sensor models could perhaps be stated and proved;
  this paper does not do it.
- **That later work has not.** Only this paper was read.
- **That gluing language in the record is unsupported.** CLAIM-tmpdjt64
  uses gluing as one formal setting among three; it does not lean on the
  word "canonical", only on the paper's being a working example.
