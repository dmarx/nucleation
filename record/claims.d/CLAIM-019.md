---
number: 19
status: Active
formerly:
- CLAIM-tmp5ty0h
title: 'Lévi-Straussian transformational analysis, as Descola reads it and as it has been modelled computationally, is direct prior art for structural transport, not only a philosophical precursor'
version: 1
role: granted
tags:
- linguistics
- social-science
date: '2026-10-08'
line: pragmatic-transport
grounds:
- LIT-775
summary: >-
  A102 §2, recovered: Lévi-Strauss treated myth variants as related by
  transformations, and "Recent computational work has explicitly modeled
  his analysis". The manuscript §2 mentions Lévi-Strauss's
  transformations but cites neither Descola nor the computational work.
---
<!-- inactive-ok-file: LIT-775 — Deferred; unread here or set aside, cited as what the exchange or manuscript names and not leaned on -->

# CLAIM-019: Lévi-Straussian transformational analysis, as Descola reads it and as it has been modelled computationally, is direct prior art for structural transport, not only a philosophical precursor

## The claim

A102 §2: "Lévi-Strauss already treated variants of myths as related through
transformational structures. Recent computational work has explicitly modeled
his analysis using discrete-event systems and simulations of narrative
transformation. That is much closer prior art than merely invoking structuralism
as a philosophical precursor." A102 named Descola (2016) and Doja, Capocchi and
Santucci (2021).

## Where it went

Manuscript §2: "Lévi-Strauss extended relational and transformational analysis
to myths: variants reveal their structures through changes of elements and
positions. This is a productive antecedent". That is the precursor framing A102
warned against. Neither Descola nor Doja et al. is cited, and the record does
not hold them. It holds *Structural Anthropology* ([LIT-775](../literature.d/LIT-775.md)), unread. Granted,
because it is a point about priority that the manuscript's own §1 disclaimer of
novelty ([CLAIM-023](CLAIM-023.md)) commits it to.

## What the two works show, read

- **Descola** ([LIT-822](../literature.d/LIT-822.md)) supports transformation as the keystone of the
  method: "a structure is not a system". He also cites Lévi-Strauss saying
  that in myth the analyst makes the cuts and chooses the path between
  variants.
- **Doja, Capocchi and Santucci** ([LIT-804](../literature.d/LIT-804.md)) give only a software
  framework for transformations the analyst supplies, with a mapping of one
  folktale's mythemes. No hypothesis about myth is tested.

So "has been modelled computationally" should be qualified. The actual
transformation model was said to be in Santucci, Doja and Capocchi 2020
(*Symmetry* 12(10):1706), now registered and read (see below).

## The 2020 model, read

Santucci, Doja and Capocchi 2020 ([LIT-807](../literature.d/LIT-807.md), [NOTE-632](../notes.d/NOTE-632.md)) contain no
richer model than the 2021 paper summarised. The software has three kinds
of operation:

- **Substituting one term for another, chosen by the user, in every
  mytheme.** Homology, inversion, opposition and symmetry are all this one
  operation.
- **Adding a mytheme.**
- **Removing a mytheme.**

The canonical formula is illustrated but never computed, and the authors
concede that the relation values "are not obtained from the software
system". The validation generates 70 myths from the *Mythologiques* and 28
Corsican tales by choosing transformations that produce them, with no
measure, so it cannot fail.

So "modelled computationally" should read: the software encodes and runs an
analyst's transformations; it does not find or test them.

