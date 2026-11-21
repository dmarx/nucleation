---
status: Proposed
title: "A population of independent factored modes relaxing on average as a power law, with no hierarchy of singular orders, shows that slow training relaxation can be singular without that hierarchy, so a power law in training relaxation does not indicate one"
version: 1
form: existence
rests_on:
- CLAIM-tmpuc8ro
concludes:
- CLAIM-tmpv5asv
tags:
- learning-theory
- complex-systems
date: '2026-11-21'
line:
- learned-structure
summary: >-
  A39 §5 of the exchange "Rich Get Richer Power Laws" offers singular
  modes as a rival to critical slowing for the slow relaxation of training
  (CLAIM-tmpv5asv), through "a hierarchy of such degeneracies". In
  CLAIM-tmpuc8ro every mode has the same learning coefficient (½) and
  multiplicity (2), and the population still relaxes on average as a power
  law with a logarithmic correction, because each mode's rate is set by a
  conserved imbalance whose density does not vanish at zero. So the
  construction supports A's rival and narrows its mechanism: the power law
  needs neither criticality nor a hierarchy of singular orders, and does
  not indicate either. Proposed. The wording is the assistant's (Claude,
  in this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpuc8ro CLAIM-tmpv5asv CLAIM-tmpcbfdj CLAIM-769 — new and Proposed, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21, or a Proposed claim the record already held, cited for the general mechanism -->

# ARG-tmpgt6ax: A population of independent factored modes relaxing on average as a power law, with no hierarchy of singular orders, shows that slow training relaxation can be singular without that hierarchy, so a power law in training relaxation does not indicate one

## The inference

A39 §5, quoted in CLAIM-tmpv5asv: "A hierarchy of such degeneracies could
generate a broad distribution of learning times. However, that would not
automatically establish a scale-free collective phase. It could be a
collection of algebraically relaxing singular modes."

CLAIM-tmpuc8ro: for K = a²b² with zero target, gradient flow conserves
D = a² − b², each mode relaxes exponentially at rate 2|D| after an
algebraic stretch, and with a, b ∼ N(0, σ²) the density of D diverges
logarithmically at zero. The population mean goes as ⟨|q|⟩ ∼ (log σ²t)/t²
and ⟨K⟩ ∼ (log σ²t)/t³, checked on 2 × 10⁶ modes against the predicted
local exponents −2 + 1/ln(σ²t) and −3 + 1/ln(σ²t).

So one coherent case has the two things apart: an aggregate power law in
relaxation, and no hierarchy of singular orders (every mode has λ = ½,
m = 2) and no criticality. It follows that a power law in training
relaxation does not indicate a hierarchy of singular orders, which is
CLAIM-tmpv5asv's narrowing of A's alternative.

## Critical questions

- **Is the case coherent?** Yes: a closed-form solution, checked against
  numerical integration to seven digits, and a population whose
  exponents approach the predicted ones as t grows. Its idealizations
  (independent modes, zero target, no noise or weight decay) restrict
  what it can explain in a real network, which CLAIM-tmpuc8ro says; they
  do not make it incoherent, and an existence argument needs only one
  coherent case.
- **Does it separate the very things the conclusion says can come
  apart?** It separates power-law aggregate relaxation from a hierarchy
  of singular orders: every mode has the same order. It also separates it
  from criticality: nothing is tuned and the modes do not interact. It
  does not separate power-law relaxation from singularity altogether:
  every mode here is singular, and the conserved D that sets the rates
  exists because the parameters are factored. So the conclusion is
  narrow: what the power law fails to indicate is the hierarchy, not
  singularity. Superposed exponentials with rates spread down to zero
  would give a power law with no singularity at all; that is the general
  mechanism (CLAIM-769), which this case instantiates.

## Verdict

Supports CLAIM-tmpv5asv's first part, that some slow, power-law-like
relaxation in training may be singular rather than critical, and narrows
A39's route to it: a broad distribution of rates from one singular order
suffices, so a hierarchy of degeneracies is not needed and a power law does
not indicate one. Proposed.
