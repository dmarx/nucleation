---
status: Proposed
title: "The record's simulation of the two-dimensional sandpile, as evidence, corroborates the claim that a power law does not by itself indicate criticality in its granted bullet that self-organized criticality reaches a critical point without tuning, since the cutoff grows with lattice size and no parameter was set"
version: 1
form: evidence
rests_on:
- CLAIM-tmpfwwrf
concludes:
- CLAIM-841
tags:
- complex-systems
- natural-sciences
date: '2026-11-22'
line:
- formal-apparatus
summary: >-
  CLAIM-tmpfwwrf, a reproduction of the BTW sandpile at L = 16 to 128,
  finds an avalanche-size cutoff growing as roughly L^2.5 with nothing
  tuned. CLAIM-841 grants SOC as a route to a critical point without
  outside tuning, and lists a cutoff growing with system size among the
  observations that discriminate criticality. So the simulation is
  independent evidence for that bullet, and corroborates the claim; it
  says nothing on the claim's thesis about other routes, and one
  discriminating observation is not all of them. The wording is the
  assistant's (Claude, in this session); adopting it is the owner's
  call.
---
<!-- inactive-ok-file: CLAIM-tmpfwwrf CLAIM-841 THEORY-tmpehudh — Proposed or new; the simulation, the claim it corroborates and the reading it checks -->

# ARG-tmpb6zg7: The record's simulation of the two-dimensional sandpile, as evidence, corroborates the claim that a power law does not by itself indicate criticality in its granted bullet that self-organized criticality reaches a critical point without tuning, since the cutoff grows with lattice size and no parameter was set

## The inference

CLAIM-tmpfwwrf: ⟨s²⟩/⟨s⟩ goes 92, 467, 2,607, 15,822 at L = 16, 32, 64,
128, and the size where the complementary distribution falls below
10^(−4) grows as L^2.58, from an empty start with nothing set but the
threshold. CLAIM-841's "What it does not say" grants SOC as a route
ending at a critical point without outside tuning; its "What would show
criticality instead" counts a cutoff that scales with system size among
the discriminating observations.

## Critical questions (evidence)

**Is the evidence sound?** The code reproduces Dhar's exact mean
avalanche size to within 0.2 per cent at all four sizes, a check that
would fail for wrong toppling rules or wrong boundaries.

**Does it bear on the conclusion, and how much?** On the bullet, yes: a
cutoff set by the lattice, not by an intrinsic scale, with no parameter
moved, is what "a critical point without outside tuning" predicts. It
does not test the other discriminators the claim lists: no data
collapse, no control parameter, no second observable. So it corroborates
the bullet; it does not establish that the sandpile is critical in every
sense the claim requires.

**Is there a rival explanation?** A distribution with an intrinsic
cutoff would stop growing once L exceeded it; over L = 16 to 128 the
growth factor per doubling rises (5.1, 5.6, 6.1) rather than falling.
Corrections to scaling make the exponents effective ones.

## Verdict

CLAIM-tmpfwwrf `corroborates` CLAIM-841 through its SOC bullet. It also
meets, for two dimensions, the `promote_when` of THEORY-tmpehudh (noted
there); promotion stays the owner's call.
