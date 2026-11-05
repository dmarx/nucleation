---
status: Open
title: 'Can changing how a fixed stock of resources is allocated among otherwise unchanged components alter which form nucleates, and so which form results, even when the set of attainable final forms stays the same?'
version: 1
tags:
- complex-systems
- natural-sciences
- society-and-governance
date: '2026-11-05'
line:
- realizability
- readiness
summary: >-
  A's question, from the synthesis on DNA origami pasted by the owner on
  2026-11-05, §4: "Can changing the allocation of influence or resources
  among otherwise unchanged components alter which organizational form
  nucleates, even when the set of attainable final forms remains the
  same?" A grounds it in Wah et al.'s 2016 report that raising the
  concentration of the centre staples moves where a DNA origami rectangle
  starts folding; the reading shows the edge staples were cut and the total
  raised at the same time, so no fixed stock was reallocated. Dunn et al.'s result, filed in the same pull request,
  answers its molecular form in part: changing only the stability of
  intermediates redirects one template among final shapes of about equal
  free energy. Whether an organizational form behaves so needs a mechanism
  of its own. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp2h496 CLAIM-583 CLAIM-567 CASE-tmpu0s44 — Proposed or new; the DNA origami readings and entries of this pull request, cited as open -->

# QUESTION-tmpg0j9y: Can changing how a fixed stock of resources is allocated among otherwise unchanged components alter which form nucleates, and so which form results, even when the set of attainable final forms stays the same?

## Why it is a question

A: "Resources don't only determine whether a structure can be assembled.
Their distribution can determine the developmental path through which it
assembles." A writes the choice of the next event as a competition,

  Pr(i binds next | x) = k_i⁺(x) c_i / Σ_{j ∈ A(x)} k_j⁺(x) c_j,

so the abundance c_i of a component sets which partial structure forms
first, and that structure sets what can follow. The record holds that the
same constraint system can differ in reachability ([CLAIM-583](../claims.d/CLAIM-583.md)) and that
feasible, reachable and reliably reachable come apart ([CLAIM-567](../claims.d/CLAIM-567.md)). It does
not ask whether the allocation of a fixed stock, rather than its amount or
the constraints, selects the outcome.

## What the record already has on it

- **Changing stabilities redirects the outcome.** Dunn et al. ([NOTE-tmpvgzvb](../notes.d/NOTE-tmpvgzvb.md),
  [THEORY-tmp2h496](../theory.d/THEORY-tmp2h496.md)) change only the staples that stabilize intermediates, and
  products shift among final shapes of about equal free energy. In their
  model, misfolds fall from 52 % to 1 %.
- **Concentration acts as a stability.** The lead's observation, not A's: in
  dilute solution a component's concentration enters its binding free
  energy as a term kT ln c. So reallocating a fixed stock of staples shifts
  the local free energies of the steps their binding enables. In A's own
  schematic energy that is a change of the g_i at fixed J. If Dunn et al.'s
  mechanism carries over, an allocation can select among final forms
  wherever early binding is effectively irreversible, and can only reroute
  the path wherever it is not.
- **Where it may only reroute.** Wah et al. 2016, read in this pull request,
  moved where a rectangle starts folding from the edges to the centre. They
  did not reallocate a fixed stock, as A's account suggests. The central
  staples were raised to 670 nM, the edge staples cut to 1.2 nM and the ramp
  slowed, all at once, so the total rose. Rectangles still formed, but no
  yield was given under the change. The authors' account is equilibrium:
  folding starts where staples melt highest, and concentration sets the
  melting temperature. That is the kT ln c effect above, not A's kinetic
  competition. The reading shows the path rerouted; it does not show the
  final form selected.
- **Where allocation has a window.** Majikes et al. 2021: a single fold's
  yield falls as staple excess rises, because two staples can each take one
  end of the fold and block it. The ratio of components, not only their
  amount, decides whether the target forms.

## What would answer it

- **In molecules,** an experiment or model that holds total staple stock fixed
  and varies only its allocation, measuring the distribution of final
  forms, not only the folding path. A's proposed study ([CASE-tmpu0s44](../cases.d/CASE-tmpu0s44.md)) is
  one design for it.
- **In organizations,** a model in which a fixed budget is divided among
  units whose early commitments are hard to reverse, and in which the set
  of attainable final configurations is shown not to depend on the
  allocation. A shift in the realized configuration with the allocation
  would answer it yes for that model.
