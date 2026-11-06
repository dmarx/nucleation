---
number: 400
status: Open
formerly:
- QUESTION-tmpg0j9y
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
<!-- inactive-ok-file: CASE-215 — Proposed or new; cited from the note on A's predictions -->
<!-- inactive-ok-file: THEORY-1439 CASE-219 — Proposed or new; the DNA origami readings and entries of this pull request, cited as open -->

# QUESTION-400: Can changing how a fixed stock of resources is allocated among otherwise unchanged components alter which form nucleates, and so which form results, even when the set of attainable final forms stays the same?

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

- **Changing stabilities redirects the outcome.** Dunn et al. ([NOTE-1643](../notes.d/NOTE-1643.md),
  [THEORY-1439](../theory.d/THEORY-1439.md)) change only the staples that stabilize intermediates, and
  products shift among final shapes of about equal free energy. In their
  model, misfolds fall from 52 % to 1 %.
- **Concentration acts as a stability.** The assistant's observation, not A's: in
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
  forms, not only the folding path. A's proposed study ([CASE-219](../cases.d/CASE-219.md)) is
  one design for it.
- **In organizations,** a model in which a fixed budget is divided among
  units whose early commitments are hard to reverse, and in which the set
  of attainable final configurations is shown not to depend on the
  allocation. A shift in the realized configuration with the allocation
  would answer it yes for that model.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Lee Tin Wah, David, Rudiuk, Baigl and Estévez-Torres, "Observing and controlling the folding pathway of DNA origami".** Lee Tin Wah et al. (2016), [LIT-2137](../literature.d/LIT-2137.md), read in full (main text and
supplement, [NOTE-1625](../notes.d/NOTE-1625.md)), is the paper A's question leans on, now read
rather than taken on A's account. It qualifies the question: with
sequences unchanged, raising the central staples and cutting the edge
staples reroutes where the rectangle starts folding (edges to centre), and
the same kind of rectangle still forms. But it does not test the
question's premise of a fixed stock: the total staple amount rose, the
ramp was slowed, and no final-form distribution or yield was measured
under the change. The authors' account is equilibrium (folding starts
where staples melt highest, concentration setting the melting
temperature), the assistant's "kT ln c" reading rather than A's kinetic
competition. The reading shows the path rerouted; it does not show the
final form selected.

No status changes.

## Note of 2026-11-05: A's predictions on productive nucleation

From the fourth synthesis on DNA origami by another assistant (A), "Predicting which organizations will successfully nucleate", pasted by the owner on 2026-11-05.

A's Prediction 5 extends this question from allocation to timing. Policies with "identical cumulative expenditure" can give different formation probabilities, because "early interactions change the state in which later interventions operate". A links this to budgeting rules: "A use-it-or-lose-it rule might change not just total spending, but the timing of investments in relationships that are necessary for later competence". The record holds the year-end spending readings ([LIT-2028](../literature.d/LIT-2028.md), [LIT-2103](../literature.d/LIT-2103.md)). The assistant's [CASE-215](../cases.d/CASE-215.md) shows both signs in one model: front-loading helps when nucleation uses the supply, and delay helps when the supply traps the unnucleated scaffold.

No status changes.
