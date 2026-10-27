---
status: Active
title: 'Black-boxing a passive linear circuit, which keeps only the Lagrangian relation its terminals'' potentials and currents can jointly satisfy, is a hypergraph functor from open circuits to Lagrangian relations: the external behaviour of a circuit glued from parts is the relational composite of the parts'' external behaviours, so circuits with the same behaviour are interchangeable in every composite, and the effective relation a composite presents at its boundary is fixed by its parts'' black boxes alone'
version: 1
tags:
- compositionality
- mathematics
date: '2026-10-27'
source:
- LIT-tmpdkjum
summary: >-
  Baez and Fong (arXiv 2015, TAC 2018), [LIT-tmpdkjum](../literature.d/LIT-tmpdkjum.md), read in [NOTE-tmpigjto](../notes.d/NOTE-tmpigjto.md):
  Thm 1.1, proved as Thm 7.7, for circuits of passive, linear, two-terminal
  components over a field with positive elements, inductors and capacitors
  entering through the Laplace transform with zero initial conditions. The
  functor is not faithful, which is the point: circuits with one behaviour
  are identified. It says nothing about nonlinear or active components, and
  nothing in time-domain terms.
---

# THEORY-tmp99qi9: Black-boxing a passive linear circuit, which keeps only the Lagrangian relation its terminals' potentials and currents can jointly satisfy, is a hypergraph functor from open circuits to Lagrangian relations: the external behaviour of a circuit glued from parts is the relational composite of the parts' external behaviours, so circuits with the same behaviour are interchangeable in every composite, and the effective relation a composite presents at its boundary is fixed by its parts' black boxes alone

## Source

Baez and Fong, "A Compositional Framework for Passive Linear Networks",
[LIT-tmpdkjum](../literature.d/LIT-tmpdkjum.md) (arXiv 1504.05625v6), Thm 1.1 (p. 7), Thm 7.7 (p. 47), Section 8
(pp. 48–51); read in [NOTE-tmpigjto](../notes.d/NOTE-tmpigjto.md).

## What was actually shown

**The categories.** Circ has finite sets as objects and open circuits as
morphisms: a cospan X → N ← Y of finite sets with a passive linear circuit on
N, composed by pushout, which glues the outputs of one circuit to the inputs
of the next (Def. 5.3, Cor. 5.4, p. 30). LagRel has finite sets as objects and,
as morphisms X → Y, Lagrangian subspaces of F^X ⊕ (F^X)* ⊕ F^Y ⊕ (F^Y)*,
composed as relations (Def. 5.15, p. 35). Both are hypergraph categories.

**The theorem.** "There exists a hypergraph functor, the black box functor
■ : Circ → LagRel, mapping a finite set X to the symplectic vector space
F^X ⊕ (F^X)* it generates, and an open circuit (N, E, s, t, r, i, o) to the
Lagrangian relation ⋃_{v∈Graph(dQ)} S^t i(v) × So(v) ⊆ F^X ⊕ (F^X)* ⊕ F^Y ⊕
(F^Y)*, where Q is the circuit's power functional" (Thm 1.1, p. 7; the black
square and conjugation overlines are lost in extraction). Thm 7.7 builds it as
a composite of four hypergraph functors: extended power functional, graph of
its differential, restriction to the terminals by Kirchhoff's laws, and a sign
flip on input currents. Thm 8.4 and the computation on p. 51 show the result is
Thm 1.1's formula, in which the interior has been eliminated by the principle
of minimum power.

**What it means, in the authors' words.** "The Lagrangian relation does not
shed any light on the internal workings of a circuit … Fortunately, the
Lagrangian relation of a circuit is enough to completely characterize its
external behavior, including how it interacts when connected with other
circuits. Put more precisely, the black boxing process is functorial: we can
compute the black boxed version of a circuit made of parts by computing the
black boxed versions of the parts and then composing them" (p. 7).

**What could have come out otherwise.** The obvious semantics, Dirichlet
forms composed by minimizing over the shared terminals, is not a category: it
has no identity, because an ideal wire has no power functional (Prop. 3.6,
p. 23). The theorem needs the move to Lagrangian relations, where the ideal
wire is a relation (p. 5). Composition in the target is not automatic either.
Gluing must impose equal potentials and opposite currents on the shared
terminals (Thm 7.4, p. 46), and that the black box of a glued circuit equals
the composite of black boxes is the content of the functor's existence.

**The identification.** The functor is many-to-one: a 2-ohm resistor "has the
same Lagrangian relation as two 1-ohm resistors in series" (p. 7), and two
parallel resistors give the same image as one (p. 32). By functoriality, two
circuits with one black box give one black box in any composite and any
tensor product.

## What this does not say

- **Nothing outside passive, linear, two-terminal networks.** Sources,
  nonlinear components and transformers are excluded (p. 3). The analogy with
  mechanical, hydraulic and chemical networks is a table and citations (p. 3),
  not a result.
- **Nothing in the time domain.** Inductors and capacitors enter as
  impedances in ℝ(s) after a Laplace transform with zero initial conditions
  (p. 16). The black box of an RLC circuit is an exact frequency-dependent
  relation; the paper does not turn it into a time-domain statement, and it
  says nothing about a circuit with a nonzero initial interior state.
- **Not that the composite's boundary relation is "emergent" beyond its
  parts.** It is new relative to each part, as in [CLAIM-tmpose3y](../claims.d/CLAIM-tmpose3y.md)'s
  "neither part has", but functoriality means it is computed from the parts'
  black boxes and the gluing. No information about the interiors beyond
  their black boxes enters.
- **Not that the external behaviour is a function.** It is a relation: an
  ideal wire, or a circuit with a terminal used twice, gives no map from
  potentials to currents (p. 23), which is why the target is LagRel.
- **Not that every Lagrangian relation is some circuit's behaviour.** The
  surjectivity proved is onto Dirichlet forms for real resistor circuits
  (Prop. 2.12, by citation to the star-mesh transform); the image of ■ in
  LagRel is not characterized here.
- **Not a statement about constraints or apparatus.** Those readings are the
  record's ([CLAIM-tmpose3y](../claims.d/CLAIM-tmpose3y.md)), not the paper's.
