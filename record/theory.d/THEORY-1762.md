---
number: 1762
status: Proposed
formerly:
- THEORY-tmph4vkf
title: 'Herrmannsdoerfer, Benz and Juergens propose that a modeling language be evolved as a recorded sequence of coupled transactions, each pairing a metamodel adaptation with the migration of existing models — reusable library operations for recurring changes, custom ones for metamodel-specific changes — from which a migrator can be generated, and report that in the reconstructed histories of the GMF and PCM metamodels nearly all coupled changes were covered by reusable operations, with only a handful of custom migrations needed.'
version: 1
tags:
- databases
- design-rationale
date: '2026-11-12'
source:
- LIT-2479
promote_when: >-
  a reading of §4 confirms the coupled-transaction and language-history
  design with generated migrators, and §6 confirms that reusable coupled
  transactions covered nearly all non-extension changes in both case-study
  metamodels, with custom transactions at or below 2%.
bears_on:
- QUESTION-458
summary: >-
  The central account of [LIT-2479](../literature.d/LIT-2479.md), read in [NOTE-1811](../notes.d/NOTE-1811.md). Proposed until
  its promote_when is met.
---

# THEORY-1762: Herrmannsdoerfer, Benz and Juergens propose that a modeling language be evolved as a recorded sequence of coupled transactions, each pairing a metamodel adaptation with the migration of existing models — reusable library operations for recurring changes, custom ones for metamodel-specific changes — from which a migrator can be generated, and report that in the reconstructed histories of the GMF and PCM metamodels nearly all coupled changes were covered by reusable operations, with only a handful of custom migrations needed.

## The account

Herrmannsdoerfer, Benz and Juergens propose that a modeling language be evolved as a recorded sequence of coupled transactions, each pairing a metamodel adaptation with the migration of existing models — reusable library operations for recurring changes, custom ones for metamodel-specific changes — from which a migrator can be generated, and report that in the reconstructed histories of the GMF and PCM metamodels nearly all coupled changes were covered by reusable operations, with only a handful of custom migrations needed.

