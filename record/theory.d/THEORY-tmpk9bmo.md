---
status: Proposed
title: 'Kiczales and colleagues argue that some design decisions cross-cut a program''s functional decomposition and can be expressed cleanly only in separate aspect languages woven with the base program, and treat reflection and metaobject protocols as one lower-level means to that end'
version: 1
tags:
- software-engineering
date: '2026-11-12'
source:
- LIT-tmpeg56k
bears_on:
- QUESTION-388
promote_when: >-
  The paper is confirmed to call the properties such design decisions
  address aspects, to say they cross-cut the system's basic functionality,
  to present the weaving of aspect and component programs as its
  technique, and in §8.2 to call reflection "one powerful tool" for the
  goal of aspect-oriented programming. Nothing about the technique's
  effectiveness is asked.
summary: >-
  The central account of [LIT-tmpeg56k](../literature.d/LIT-tmpeg56k.md), skimmed in [NOTE-tmpds3ww](../notes.d/NOTE-tmpds3ww.md) as a weak
  stand-in for Part I of The Art of the Metaobject Protocol. It bears on [QUESTION-388](../questions.d/QUESTION-388.md)
  through §6.2: reflective access was judged too powerful to leave
  unbounded, and bounded by a language its designers wrote. Proposed until
  the paper is read in full.
---
<!-- inactive-ok-file: NOTE-tmpds3ww — Skimmed; the reading of the source -->

# THEORY-tmpk9bmo: Kiczales and colleagues argue that some design decisions cross-cut a program's functional decomposition and can be expressed cleanly only in separate aspect languages woven with the base program, and treat reflection and metaobject protocols as one lower-level means to that end

## The account

Some properties a program must have, its aspects, cross-cut the
decomposition its component language imposes, so their code is scattered
and tangled. Writing them in separate aspect languages and weaving them
with the components captures them cleanly. Reflection, "a base language
and (one or more) meta-languages that provide control over the base
language's semantics and implementation", is one tool for this, and
"AOP is a goal, for which reflection is one powerful tool" (§8.2).
Because such access "is so powerful that it can be dangerous or difficult
to use", the authors bound it with a higher-level aspect language (§6.2).

## Bearing

[QUESTION-388](../questions.d/QUESTION-388.md): a precedent for bounding a meta-level's power by a narrower
language fixed by designers outside the system, which leaves the
reconfiguration's criterion external. It does not address who should
govern reconfiguration.
