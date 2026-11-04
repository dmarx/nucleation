---
status: Proposed
title: 'scenario-conditioned response readiness: the probability that an organization operating under a specified policy can deliver an effective response to a specified contingency within its deadline'
version: 1
tags:
- operations-research
- agency
- causality
date: '2026-11-04'
line:
- distributed-agency
complements:
- TERM-055
summary: >-
  A's proposal, from the exchange on emergency readiness (2026-11-04; its
  share link could not be fetched, and its text was pasted by the owner),
  section 4 of A's "Proposed additions to Nucleation PR [#401](https://github.com/dmarx/nucleation/issues/401)", where A
  named it "scenario-conditioned operational readiness". Renamed on
  filing, to keep it apart from [TERM-055](TERM-055.md)'s operational availability and
  [TERM-094](TERM-094.md)'s action readiness. R^π_O(c, τ | s) is the probability of an
  effective response by τ when contingency c is imposed on organization O
  in state s under its actual policy π. It is a family indexed by
  contingency, not one number. The wording is A's; adopting it is the
  owner's call.
---

# scenario-conditioned response readiness: the probability that an organization operating under a specified policy can deliver an effective response to a specified contingency within its deadline

## Definition

  R^π_O(c, τ | s) = Pr_π(effective response by τ | do(c), s),

with c an imposed contingency, τ its deadline, s the organization's
initial state, and π the response policy the organization actually
follows. The do(c) is the point: this is readiness for a specified
situation, imposed, not success conditional on the situations that
happened to be observed. An organization that never met c has a value of
R for it all the same.

**No single scalar.** The object is the family
{R^π_O(c, τ_c | s) : c ∈ C}, one value per contingency and its deadline.
Two organizations' readiness profiles can be incomparable, each more
ready for some contingencies than the other.

## What it is not

- **Operational availability ([TERM-055](TERM-055.md)).** That is the chance that a
  resource is deployed for a task before the deadline, given the cue
  actually supplied, taking the supremum over the procedures available.
  This term is about an organization's effective response under a
  specified policy, which includes recognizing the contingency,
  mobilizing for it and performing successfully, and it takes the policy
  as followed, not the best one available. So a system can have the
  equipment and the personnel, each available in [TERM-055](TERM-055.md)'s sense, and
  low readiness, because its dispatch policy fails to mobilize them. The
  two are complements: availability of each resource is one factor of
  this term.
- **Action readiness ([TERM-094](TERM-094.md)).** Frijda's term is a state of an agent:
  a preparation for action that claims control over behaviour. This term
  is not a state at all but a probability, of an organization, for a
  contingency, and it says nothing about what claims control. An
  organization with no state of preparation can be ready in this sense,
  and one fully prepared can be unready for the contingency imposed.
- **Utilization or realized performance.** It is defined under
  intervention, so a record of what was done does not measure it.
