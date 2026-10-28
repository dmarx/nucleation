---
number: 1058
status: Active
formerly:
- THEORY-tmp49y4o
title: 'Given constructor theory''s principles of locality and of classical information, a single further prohibition, that two information observables with mutually disjoint attributes have a union that is not an information observable, is enough for a medium to have information attributes that cannot be distinguished, unclonable and jointly unsharp observables, measurements that are deterministic yet unpredictable, irreducible disturbance by measurement, and locally inaccessible information; quantum information is an instance'
version: 1
tags:
- quantum-foundations
- information-theory
date: '2026-10-27'
source:
- LIT-1663
summary: >-
  Deutsch & Marletto (2015), [LIT-1663](../literature.d/LIT-1663.md), §§7–8, read in [NOTE-1219](../notes.d/NOTE-1219.md).
  Active as a conditional. The derivations are informal but complete
  arguments from principles II–IX, and each feature is shown in the paper's
  own terms with no probabilities. The principles themselves are
  conjectures. It does not say that superinformation singles out quantum
  theory, or that the quantum features are derived from anything not
  already assumed.
---

# THEORY-1058: Given constructor theory's principles of locality and of classical information, a single further prohibition, that two information observables with mutually disjoint attributes have a union that is not an information observable, is enough for a medium to have information attributes that cannot be distinguished, unclonable and jointly unsharp observables, measurements that are deterministic yet unpredictable, irreducible disturbance by measurement, and locally inaccessible information; quantum information is an instance

## Source

Deutsch & Marletto (2015), [LIT-1663](../literature.d/LIT-1663.md), §§2, 6–8; read in [NOTE-1219](../notes.d/NOTE-1219.md).
Equations (8.1)–(8.3) checked against the arXiv preprint 1405.5563.

## What was actually shown

**The prohibition.** A superinformation medium **M** is an information
medium with at least two information observables, with mutually disjoint
attributes, whose union is not an information observable (§7). "From here
on, we propose no further principles." For a qubit, any two orthogonal
states form an information observable, and no union of two or more such
sets does.

**The features, each argued from the principles** (§8, with *X*, *Y* such a
pair):

- *Indistinguishable attributes* (8a). If every *x* ∈ *X* were
  distinguishable from every *y* ∈ *Y*, then IV makes *X*∪*Y* measurable, VI
  makes its attributes preparable, and measure–compute–reprepare gives
  every permutation. Pairwise measurement with III gives cloning. Then
  *X*∪*Y* would be an information variable, which is a contradiction.
- *No-cloning* (8c). Repeated cloning of {*x*, *y*} would prepare *z*(∞),
  and IX would make *x*(∞) and *y*(∞) distinguishable, so *x* and *y*
  would be.
- *Undetectable sharpness* (8b) and *no joint sharpness or measurement* (8d).
- *Deterministic unpredictability* (8e). For maximal *X* and input *y*, no
  prediction "the outcome will be *x*" is true, yet {χ̄̄_y, χ̄_y} is sharp,
  so it is predictable that the outcome is one of the *x* not
  distinguishable from *y*. This is the constructor-theoretic counterpart
  of the projector onto fewer than three photons.
- *Irreducible disturbance* (8f), the impossibility (8.1).
- *Consistent repeated measurement* (8g), through (8.2)–(8.3).
- *Discrete and continuous* (8h): each quantum information observable is
  discrete, and there is a continuum of them with no union an information
  observable.
- *Locally inaccessible information* (8i): under coherence, the
  controlled-not (8.4) and its extension (8.5) yield an information variable
  {(0,1), ψ(1)} of **M**1⊕**M**2 not measurable through products of local
  variables, while locality II holds.

Each step could have failed: a feature not reachable from the prohibition
and the principles would have needed a further prohibition. The paper needs
none.

## What this does not say

- That principles II–IX hold. They are conjectured (§6). The authors say IV
  and V need hold only "for a special class of substrates", and that VI and
  VII are simplifying assumptions.
- That superinformation is quantum theory. Quantum information is shown to
  be an instance. Whether other theories satisfy the prohibition is not
  asked.
- That quantum theory is derived. "We are not trying to derive quantum
  theory, or any other existing law, from anything" (§1).
- That the proofs are formal. They are prose arguments, and some cite
  principles loosely: 8c names "assumption VII" for preparability, which is
  VI.
- What explains the unpredictability. "It is up to the subsidiary theories
  to *explain* this deterministic unpredictability" (§8e); the Everettian
  account is offered as one such explanation, not derived.
