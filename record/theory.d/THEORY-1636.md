---
number: 1636
status: Proposed
formerly:
- THEORY-tmph775l
title: 'Kiczales, des Rivières and Bobrow specify a metaobject protocol that describes CLOS as an extensible CLOS program, so that users can change the language''s behaviour by specializing its metaobjects, within explicit restrictions that preserve implementors'' freedom'
version: 1
tags:
- software-engineering
date: '2026-11-12'
source:
- LIT-2335
bears_on:
- QUESTION-388
promote_when: >-
  Chapter 5 is confirmed to describe the protocol as "a description of CLOS
  itself as an extensible CLOS program", to give its purpose as letting
  users extend and customize CLOS's behaviour, and to mediate that by
  explicit restrictions on implementations and on portable programs.
  Nothing from Part I, which was not read, is asked.
summary: >-
  The account of chapter 5 of [LIT-2335](../literature.d/LIT-2335.md), skimmed in [NOTE-1718](../notes.d/NOTE-1718.md) from
  a community hypertext the owner ruled usable. It bears on [QUESTION-388](../questions.d/QUESTION-388.md):
  the machinery of change is inside the system, the space of permitted
  changes fixed by its designers.
---
<!-- inactive-ok-file: NOTE-1718 — Skimmed; the reading of the source -->

# THEORY-1636: Kiczales, des Rivières and Bobrow specify a metaobject protocol that describes CLOS as an extensible CLOS program, so that users can change the language's behaviour by specializing its metaobjects, within explicit restrictions that preserve implementors' freedom

## The account

Each kind of program element, class, slot definition, generic function,
method and method combination, is a metaobject, and CLOS's behaviour is
provided by methods on the metaobjects' classes. Users change the language
by subclassing specified metaobject classes and adding methods to
specified generic functions. "This balance between user extensibility and
implementor freedom is mediated by placing explicit restrictions on each":
portable programs may not redefine specified classes, generic functions,
methods or method combinations, and may override a specified method only
where its description allows. Redefinition propagates: discriminating
functions are recomputed and registered dependents notified.
