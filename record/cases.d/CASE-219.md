---
number: 219
status: Proposed
formerly:
- CASE-tmpu0s44
title: 'A proposed stochastic assembly study: hold a target organization fixed, vary the relative availability and the strength or arrangement of components at fixed total expenditure, and measure feasibility, the probability and time of assembly, kinetic traps, early intermediates and persistence'
version: 1
standing: stipulated
kind: proposed-study
tags:
- complex-systems
- natural-sciences
- mathematics
date: '2026-11-05'
line:
- realizability
illustrates:
- CLAIM-567
- CLAIM-566
summary: >-
  A's design, from the synthesis on DNA origami pasted by the owner on
  2026-11-05, §8. It is a small stochastic assembly model with a stated
  target A and a state X_t of which interactions exist. Three questions are
  kept apart: feasibility (A is admissible), assembly (Pr(X_T ∈ A) is high)
  and persistence (Pr(X_t ∈ A) stays high over a horizon). A varies the
  relative availability, strength and arrangement of components, holding
  total expenditure fixed where possible, and names six measurements. A
  expects either result to be informative: a small early intervention that
  raises the probability of global organization without changing the final
  requirements, or early stabilization that traps. The assistant's
  annealing toy ([CASE-216](CASE-216.md)) runs one slice of it, with temperature in
  place of allocation. The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-184 — Proposed or new; entries this study would test, cited as open -->

# CASE-219: A proposed stochastic assembly study: hold a target organization fixed, vary the relative availability and the strength or arrangement of components at fixed total expenditure, and measure feasibility, the probability and time of assembly, kinetic traps, early intermediates and persistence

## The case

A's design: "construct a small stochastic assembly model with a specified
target organization". It keeps three questions apart:

| | Condition |
|---|---|
| Feasibility | A is physically admissible |
| Assembly | Pr(X_T ∈ A) is sufficiently high |
| Persistence | Pr(X_t ∈ A) over a horizon is high |

"Now vary the relative availability of components and the strength or
arrangement of their interactions, while holding total resource
expenditure fixed where possible." A's measurements:

- the probability of assembling the intended structure;
- the time required for successful assembly;
- the frequency and duration of kinetic traps;
- which partial structures appear early;
- whether an early intermediate raises or lowers the probability of eventual
  success;
- whether the finished structure persists without further intervention.

A's two outcomes: "a relatively small early assembly intervention
substantially improves the probability of global organization without
changing the final structural requirements", or "early stabilization
creates a kinetic trap and makes the desired final organization less
likely". In A's words, "Both results would be valuable."

## What it can show

- **The three properties apart,** in one model: [CLAIM-567](../claims.d/CLAIM-567.md)'s feasible,
  reachable and reliably reachable, and [CLAIM-566](../claims.d/CLAIM-566.md)'s assembling and
  persisting. Regeneration is not in the design.
- **An answer to [QUESTION-400](../questions.d/QUESTION-400.md)** for the model, if the allocation is
  varied at fixed total and the distribution of final forms is measured.
- **The anchor question both ways:** whether an early anchor helps, as a
  nucleus, or entrenches the wrong form ([CLAIM-184](../claims.d/CLAIM-184.md)).

## What has been run

- **The assistant's annealing toy** ([CASE-216](CASE-216.md)) runs one slice, with the
  level of a resource varied rather than its allocation. It shows both of
  A's outcomes. A brief hot step that makes the nucleus without the trap
  raises the folded fraction within the hour from at best 90.4 % to
  98.5 %. Cooling too far first lets the trap form, and that trap holds
  through sixteen hours.
- **In molecules,** Dunn et al. vary the arrangement of seam staples and
  measure the distribution of final shapes. That is the strength-and-
  arrangement half of the design.

Being stipulated, the study shows nothing until it is run. What it would
show about organizations depends on a mechanism of their own.

## Note of 2026-11-05: the further DNA origami readings

The works cited in A's two syntheses on DNA origami, pasted by the owner on 2026-11-05, read in this pull request.

**Lee Tin Wah, David, Rudiuk, Baigl and Estévez-Torres, "Observing and controlling the folding pathway of DNA origami".** Lee Tin Wah et al. (2016), [LIT-2137](../literature.d/LIT-2137.md), is a partial, real instance of
the proposed study: it holds the target design fixed and varies the
relative availability of components, and measures intermediates and where
folding nucleates. But it is not at fixed total expenditure (the stock
rose) and it measures neither the probability nor the time of assembly nor
a defect census under the altered allocation, which the proposed study
asks for.

No status changes.

## Note of 2026-11-05: Shirt-Ediss et al., "Optimising DNA origami assembly by reducing off-target interactions", read

Cited in A's third synthesis on DNA origami, pasted by the owner on 2026-11-05.

**Shirt-Ediss, Torelli et al., "Optimising DNA origami assembly".** Shirt-Ediss, Torelli et al. (2026), [LIT-2123](../literature.d/LIT-2123.md), read in [NOTE-1627](../notes.d/NOTE-1627.md), partly realise the proposed study
for sequence: a fixed target in four shapes, three sequence variants each, assembly yield by AFM and
persistence on storage, blind and replicated in a second lab for two shapes. What varies is the base
sequence, not availability or arrangement of components, and neither time of assembly nor early
intermediates is measured.

No status changes.
