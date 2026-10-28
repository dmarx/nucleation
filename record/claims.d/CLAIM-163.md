---
number: 163
status: Superseded
superseded_by:
- ARG-tmp8meez
formerly:
- CLAIM-tmpigdl0
title: '"Synchronization" is an analogy without a mechanism: phase synchrony among coupled oscillators has a coupling, an order parameter and transitions, valuations that fail to cross have none of these, and the word adds nothing to "the curves do not cross"'
version: 2
history:
- version: 2
  date: '2026-10-28'
  note: >-
    Moved to ARG-tmp8meez under ADR-061, as its own worked example: the
    claim is wholly about whether the synchronization analogy carries, so
    it is the argument from CLAIM-169, THEORY-069 and THEORY-070 to
    CLAIM-162, form analogy, Proposed. The objection to CLAIM-162 is now
    that argument's verdict. The text below is unchanged.
role: counter
warrant: interpretive
tags:
- behavioral-integration
- complex-systems
date: '2026-10-11'
line: will-organization
grounds:
- THEORY-069
uses:
- TERM-050
summary: >-
  The record's own anticipated objection to the owner's framing, and the
  kind [ADR-032](../decisions.d/ADR-032.md) found most often real: same structure, not the same
  mechanism. Open. [TERM-050](../terms.d/TERM-050.md) defines synchronization without
  dynamics, so the claims survive with the word replaced, but then the
  word is only a name. The body says what would turn the analogy into a
  mechanism.
objected_by:
- CLAIM-198
---
<!-- inactive-ok-file: CLAIM-162 — Proposed; the claim this objection targets, open -->
<!-- inactive-ok-file: THEORY-069 — Proposed; the coordination-dynamics reading that sets the standard the analogy is held to -->
<!-- inactive-ok-file: ADR-061 — Proposed; the decision under whose migration this entry was filed or revised -->
<!-- inactive-ok-file: ARG-tmp8meez CLAIM-169 CLAIM-198 THEORY-070 — Proposed; the argument this claim moved to, its premises and the reply that still names this claim, open -->

# CLAIM-163: "Synchronization" is an analogy without a mechanism: phase synchrony among coupled oscillators has a coupling, an order parameter and transitions, valuations that fail to cross have none of these, and the word adds nothing to "the curves do not cross"

## The claim

In coordination dynamics ([THEORY-069](../theory.d/THEORY-069.md)), synchronization has parts: coupled
components, a collective variable (relative phase) and transitions between
stable patterns, with critical fluctuations and slowing before a switch.
[TERM-050](../terms.d/TERM-050.md) and [CLAIM-162](CLAIM-162.md) take the word and none of these parts.
Interests whose curves do not cross are not coupled, have no phase, and do
not "lock". On this objection the word adds nothing that "the valuations
do not cross" does not already say. Worse, it invites the reading that
flow or mindfulness is literally neural synchrony, which nothing here
argues.

## Why it is still open

The reply already available is partial. [TERM-050](../terms.d/TERM-050.md) disclaims the
dynamics, so the claims survive with the word replaced, but that concedes
the objection's point about the word.

The analogy would become a mechanism if the parts could be found:

- **A coupling.** Ainslie's self-prediction couples successive choices,
  since each choice changes the expected value of the series. That is a
  candidate.
- **An order parameter.** For example, the share of choices in a domain
  that keep the same ranking across delays.
- **Transitions.** Entering and leaving flow, or a rule breaking into a
  lapse district, would behave as switches between stable patterns. They
  would show hysteresis, and critical slowing in the order parameter before
  a lapse.

None of this is in the record, so the objection stands, Proposed.

## Note of 2026-10-12: [LIT-638](../literature.d/LIT-638.md), as an interlocutor reads it

An interlocutor's reading, relayed by the owner, takes [LIT-638](../literature.d/LIT-638.md) (read in [NOTE-502](../notes.d/NOTE-502.md); [THEORY-088](../theory.d/THEORY-088.md)) as "a qualification of CLAIM-163, not a refutation". The record's reading of the paper supports part of that.

- **Candidate collective variables.** Slow cortical activity is organized by interacting spiral defects, with phase singularities and their topological charge as collective descriptors ([NOTE-502](../notes.d/NOTE-502.md) C1–C2, moderate to strong). That widens what could fill this objection's second part beyond relative phase. It measures no valuations.
- **Not transitions in this claim's sense.** Spiral configurations carry task information above chance (C3, moderate), and their routing role is read from averages and a model with no perturbation (C4, weak to moderate). Neither shows switches with hysteresis or critical slowing.
- **The form of the transition test.** [LIT-638](../literature.d/LIT-638.md) claims transitions are continuous, not discrete switches between metastable states (C5, weak), against [LIT-080](../literature.d/LIT-080.md). This objection's transition test presupposes discrete switching. [QUESTION-079](../questions.d/QUESTION-079.md) asks which description holds.

The reading recommends recasting this objection so that "the absence of a specified dynamical mechanism", not of phase synchrony, is decisive. That is already its framing: its title calls the word "an analogy without a mechanism", and relative phase is its example of a collective variable, not a requirement. [QUESTION-078](../questions.d/QUESTION-078.md) files the reading's suggestion that coordination, not synchronization, is the organizing concept for the will line. Recorded as advice; the status is unchanged.


## Note of 2026-10-12: a stipulated crowd case with all three parts

[CASE-074](../cases.d/CASE-074.md), the democracy-mode variant of Twitch Plays Pokémon with
the running tally visible, has all three parts this objection asks for,
in toy form:

- **A coupling.** The visible tally ties each voter to the aggregate.
- **A collective variable.** The vote share.
- **Transitions.** With strong enough feedback the vote locks in early.
  There are two stable outcomes, and probably hysteresis.

With the tally hidden, the coupling is gone, and the counts are
independent integrators. One design choice turns the mechanism on or
off.

This bears on the objection without grounding either side. The case is
stipulated. Its parts are voters, not one person's interests, so it
shows that a population of valuers can have the full mechanism, not
that a will has it. No status change and no typed edge. The case also
prompted [QUESTION-077](../questions.d/QUESTION-077.md): is agreement produced by coupling a
different kind of integration from agreement because valuations
coincide? If it is, it may be where the mechanism lives.

*Drawn by the assistant and filed at the owner's request.*

## Note of 2026-10-18: candidate parts from the broader sense

A45 of the exchange of 2026-10-17 recommended using the broader sense of
synchronization (filed as [TERM-061](../terms.d/TERM-061.md)) "to specify coupling,
observable coordination, and intervention-based tests; do not regard the
objection as refuted yet". Read against this objection's three parts:

- **A coupling.** A45's local dynamics, z_{t+1} = F_local(z_t, c_t, E_t,
  h_t): the processes' proposals respond to one another through influence
  relations E_t, with h_t "exceptional supervisory intervention".
- **A collective variable.** On the record's reading, how often h_t is
  needed (A45's supervisory cost counts the encounters with h_t ≠ 0). It
  stays defined while the processes keep distinct rankings, which
  relative phase would not need and [TERM-050](../terms.d/TERM-050.md)'s crossing curves cannot
  give.
- **Transitions.** A45's sequence from "Recurrent conflict" to "Learned
  accommodation" would be a switch in that variable, "not a necessary
  progression".

None is measured, in a person or a model. The objection stands, Proposed,
and the status is unchanged. [CLAIM-358](CLAIM-358.md) is stated in the broader
sense and inherits the objection.

## Note of 2026-10-28: moved to [ARG-tmp8meez](../arguments.d/ARG-tmp8meez.md)

This objection says the word "synchronization" carries no mechanism from
coordination dynamics to valuations, which is a verdict on an analogy.
Under [ADR-061](../decisions.d/ADR-061.md) it is now [ARG-tmp8meez](../arguments.d/ARG-tmp8meez.md), from [CLAIM-169](CLAIM-169.md), [THEORY-069](../theory.d/THEORY-069.md) and
[THEORY-070](../theory.d/THEORY-070.md) to [CLAIM-162](CLAIM-162.md), Proposed, whose critical question "what relevant
difference is there?" is answered: the mechanism. [CLAIM-198](CLAIM-198.md)'s reply still
names this claim, and the argument's body records it.
