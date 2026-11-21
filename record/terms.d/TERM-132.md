---
number: 132
status: Proposed
formerly:
- TERM-tmp7i7ed
title: 'local degrees of freedom (of an entry)'
version: 3
history:
- version: 2
  date: '2026-11-21'
  note: >-
    After the readings of 2026-11-21 of the semicontraction papers: the
    conserved part is distinguished from a seminorm's kernel, which
    semicontraction leaves uncontrolled; the conserved part is the exact
    invariants. Those readings join draws_on.
- version: 3
  date: '2026-11-21'
  note: >-
    A dated note: TERM-tmp7m4at and CLAIM-tmp8v75o sort this term's parts by
    the predicates on a feature. No change to the definition.
tags:
- design-rationale
- complex-systems
date: '2026-11-20'
line:
- nucleating-argument
- record-as-apparatus
draws_on:
- THEORY-960
- THEORY-2044
- THEORY-2143
- THEORY-2142
summary: >-
  The features of a record entry that a restatement copies with error:
  neither pulled onto a fixed point of the restating step (contracting)
  nor copied exactly (conserved). The owner's phrase at U1 of the session
  of 2026-11-20, given this sense by the assistant at U5. The wording is
  the assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: TERM-tmp7m4at TERM-tmp0g123 CLAIM-tmp8v75o CLAIM-tmpj4fzn — Proposed; filed on 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2142 THEORY-2143 — Proposed; cited in the readings of 2026-11-21 -->
<!-- inactive-ok-file: THEORY-2044 CLAIM-189 — Proposed; the partial-contraction reading the term's "conserved part" is fixed against, and the claim on legitimate change -->
<!-- inactive-ok-file: CLAIM-772 CLAIM-779 CLAIM-778 — Proposed or Deferred; filed in this contribution of 2026-11-20 -->

# TERM-132: local degrees of freedom (of an entry)

## Definition

Treat restating an entry, by a session reading it, a filer revising it or a
manuscript drafted from it, as one step of a chain. The step does one of
four things to each feature of the entry ([CLAIM-772](../claims.d/CLAIM-772.md)):

- **contracting**: pulls it toward the step's own fixed point, the
  convention, whatever it was before;
- **conserved**: copies it exactly;
- **copied with error** (neutral): leaves it where it was, plus an error;
- **expansive**: magnifies a difference in it.

The **conserved part** of the step is the set of features it copies
exactly. The sense is fixed against DeGroot's invariant πF ([THEORY-960](../theory.d/THEORY-960.md)) and
the property partial contraction leaves free ([THEORY-2044](../theory.d/THEORY-2044.md)). It is not the kernel
of a seminorm in which the step contracts: in semicontraction theory
([THEORY-2143](../theory.d/THEORY-2143.md), [THEORY-2142](../theory.d/THEORY-2142.md)) the kernel is only where the step does not
contract, and may hold features copied with error or magnified. The
conserved part is the smaller set the step copies exactly, the exact
invariants, such as DeGroot's πF or vᵀx in affine averaging.

An entry's **local degrees of freedom** are its features copied with error.
They are free in the sense that nothing holds them: a contracted feature
goes to the convention and a conserved one stays put, while one copied with
error random-walks and loses its start as 1/n ([CLAIM-779](../claims.d/CLAIM-779.md)). The life
cycle of an entry is the movement of features out of this part
([CLAIM-778](../claims.d/CLAIM-778.md)).

## Not to be confused with

- **The fields an entry may fill.** The schema's options are what the
  contracting part converges on, not the entry's degrees of freedom.
- **Degrees of freedom of a dynamical system** in the physicist's sense, the
  number of independent coordinates. A feature can be a coordinate of the
  entry and still not be free in this sense, because the step holds it.
- **What may legitimately change.** [CLAIM-189](../claims.d/CLAIM-189.md) holds that a developing
  argument changes legitimately. A feature that is not free can still be
  changed, by a deliberate revision that announces itself; the term is about
  what restatement does unprompted.

## Note of 2026-11-21: the parts, by predicate

Read an entry's predicates as tests ([TERM-tmp7m4at](TERM-tmp7m4at.md)), and the three parts are
sorted by the predicates on a feature ([CLAIM-tmp8v75o](../claims.d/CLAIM-tmp8v75o.md), part 5): a feature
given a descriptor, a predicate the entry passes when it is added such as an
exact value, is conserved from then on at the entry's own value; one given an
imposition, a value common to entries that the entry did not meet, is
contracting, at the convention; one that no predicate bounds is a local
degree of freedom. [CLAIM-tmpj4fzn](../claims.d/CLAIM-tmpj4fzn.md) reads an entry's life cycle as the accrual
of predicates, which moves features out of the last part, and calls it
stabilization in the control-theoretic sense ([TERM-tmp0g123](TERM-tmp0g123.md)).

