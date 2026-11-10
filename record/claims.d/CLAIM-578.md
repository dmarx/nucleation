---
number: 578
status: Active
formerly:
- CLAIM-tmplysd0
title: 'Computational complexity belongs to a family of problems posed over configuration spaces, with an encoding and permitted operations, and not to a configuration space: one fixed finite space has none, and over the same instances finding a solution and navigating between solutions can fall in different classes'
version: 2
history:
- version: 2
  date: '2026-11-06'
  note: >-
    Promoted at the twenty-sixth status review (ADR-057), at the status review's ruling (the owner delegated these rulings).
    THEORY-1372, THEORY-1407 and THEORY-1380 move from grounds to
    corroborated_by (ADR-058): the body cites them as instances of the
    question deciding the class, Eppstein's across models as well as
    questions, and the first clause follows from what a complexity class is.
    THEORY-1375, promoted in the same review, carries the second clause: the
    reconfiguration versions of NP-complete search problems are
    PSPACE-complete over the same instances. No objection is on file, and
    nothing meets the defeat condition. The claim is unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A notion of computational complexity, in the sense of complexity classes,
  under which one fixed finite configuration space with one fixed question
  falls in a nontrivial class; or an error in the cited theorems such that,
  in each case cited, finding a solution and navigating between solutions
  over the same instances fall in the same class after all. Not defeated by
  descriptive or algorithmic-information complexity of a single object,
  which are other senses, nor by results that a given problem's class is
  robust across reasonable encodings, which the claim allows.
tags:
- mathematics
- complex-systems
- philosophy-of-science
date: '2026-11-05'
line:
- realizability
- formal-apparatus
grounds:
- THEORY-1375
complements:
- CLAIM-567
- CLAIM-565
bears_on:
- QUESTION-376
summary: >-
  A's proposal, from the pasted synthesis on resource-bounded realizability
  (three responses, pasted by the owner on 2026-11-05, continuing the
  exchange on constraint architectures), Response 1 §2, after Eppstein:
  "Computational complexity is not an intrinsic property of a configuration
  space by itself." A complexity class is a set of problems over infinitely
  many instances; one fixed space with one question is decided by lookup.
  Over the same instances the question decides the class: positive 1-in-3
  SAT is NP-complete to satisfy and polynomial to navigate (Gopalan et
  al.), the reconfiguration versions of many NP-complete problems are
  PSPACE-complete (Ito et al.), and Eppstein's folding problems run from
  fixed-parameter tractable to undecidable by model and question. For the
  record it means that one organization's compatibility complex carries no
  complexity. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: NOTE-1555 NOTE-1572 THEORY-1380 — Proposed or Skimmed; A's proposals of 2026-11-04 and 2026-11-05, the readings' accounts and partial readings, and the entries filed beside them, cited as filed, nothing here resting on their being settled -->

# CLAIM-578: Computational complexity belongs to a family of problems posed over configuration spaces, with an encoding and permitted operations, and not to a configuration space: one fixed finite space has none, and over the same instances finding a solution and navigating between solutions can fall in different classes

## The claim

A (Response 1 §2): "Computational complexity is not an intrinsic property
of a configuration space by itself. It belongs to a family of problems
posed over that space, together with an encoding and permitted
operations." A lists four tasks the same kind of constraint system
supports, finding a valid configuration, counting them, deciding whether
one is reachable from another, and finding the least expensive
transformation, and concludes that a universality class "might have to
preserve not merely the topology of a space, but also its computational
problem structure."

**One fixed space has no complexity.** A complexity class is a set of
decision problems, each over infinitely many encoded instances. One finite
configuration space with one question is a single instance, or finitely
many, answered by a table of constant size. It has a complexity only once
a family is declared: all crease patterns of a kind, all formulas over a
constraint language, all organizations of a design, indexed by size. The
readers of Bulatov and of Zhuk make this point for one crease pattern or
one organization ([NOTE-1572](../notes.d/NOTE-1572.md), [NOTE-1555](../notes.d/NOTE-1555.md)).

**Over the same instances, the question decides the class.**

- **Finding against navigating, both ways** (Gopalan, Kolaitis, Maneva and
  Papadimitriou; [NOTE-1584](../notes.d/NOTE-1584.md); [THEORY-1407](../theory.d/THEORY-1407.md)). For positive 1-in-3 SAT,
  "This set is tight (actually, it is componentwise bijunctive), but not
  Schaefer": satisfying it is NP-complete, deciding whether two solutions
  are joined by single flips is polynomial, and global connectivity is
  coNP-complete. For positive NAE-3SAT, satisfying is NP-complete and both
  connectivity problems are PSPACE-complete.
- **Finding against reconfiguring** (Ito et al.; [NOTE-1595](../notes.d/NOTE-1595.md);
  [THEORY-1375](../theory.d/THEORY-1375.md)). "We demonstrate that a host of reconfiguration problems
  derived from" "NP-complete problems are PSPACE-complete, while some are
  also NP-hard to approximate"; matroid bases and matchings stay
  polynomial. Least cost along a path is a fourth question: the minmax
  versions, which compute the least worst intermediate cost, are strongly
  NP-hard for power supply and 2-approximable for set cover.
- **Folding** (Eppstein; [NOTE-1611](../notes.d/NOTE-1611.md); [THEORY-1372](../theory.d/THEORY-1372.md)). Flat foldability
  of a finite crease pattern is fixed-parameter tractable in ply and
  treewidth; reaching one flat state from another in the hinged-square toy
  model is PSPACE-complete, "even for instances with bounded treewidth";
  counting its states is #P-complete; flat foldability of infinite
  self-similar patterns is undecidable. These are different models as
  well as different questions, as A says: "Depending on the precise folding
  model and question".
- **Quantifying the question** (Zhuk; [NOTE-1555](../notes.d/NOTE-1555.md); [THEORY-1380](../theory.d/THEORY-1380.md)). For
  fixed finite languages the existence question splits cleanly into
  polynomial and NP-complete; once the question is quantified, the
  conjectured trichotomy fails and other classes appear (§10.6).

Checked against the filed readings by the filer.

## What it does not say

- **That complexity is arbitrary.** For a declared family, question,
  encoding and set of moves it is a fact, and often robust to reasonable
  changes of encoding.
- **That complexity measures physical cost.** A: "two algorithms can have
  the same computational complexity while requiring completely different
  amounts of physical energy or control." Resources are [TERM-105](../terms.d/TERM-105.md)'s;
  complexity is growth with size.
- **Anything about one organization.** [CLAIM-347](CLAIM-347.md)'s compatibility complex is
  of one organization and so carries no complexity in this sense; the
  question whether the record's organizational models have complexity is
  first the question of which family they belong to.
- **That the four tasks exhaust the questions.** Diagnosing which
  obstruction blocks a transition is another, with its own complexity
  ([CLAIM-575](CLAIM-575.md)).
