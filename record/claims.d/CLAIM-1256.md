---
number: 1256
status: Proposed
formerly:
- CLAIM-tmpb1wyc
title: 'Over-reliable providers lower resilience'
statement: >-
  A provider whose realized reliability exceeds its declared guarantee can
  lower the resilience of the organization built on it: those who depend on
  it stop maintaining the fallbacks the guarantee would require, so its rare
  failures propagate, and holding realized reliability near the declared
  level keeps their expectations at the guarantee
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A comparison across dependent services in which consumers of providers
  whose realized availability runs well above the declared objective keep
  fallbacks as often, and suffer no more propagated outages, than
  consumers of providers held near their objective; or a record of
  synthesized outages that do not reduce the dependencies added on a
  provider; or a showing that the claim adds nothing to CLAIM-603, that
  the declared guarantee plays no part in which losses become harmful.
tags:
- software-engineering
- society-and-governance
date: '2026-11-24'
line:
- dependence-and-domination
- readiness
works:
- governance-of-becoming
grounds:
- CASE-424
- LIT-3234
complements:
- CLAIM-603
- CLAIM-677
summary: >-
  A34 §2 of the exchange "Memes, Contracts, and Systemic Normativity"
  (ChatGPT, 2026-11-24), from the SRE book's global Chubby planned outage
  ([CASE-424](../cases.d/CASE-424.md)): "Increasing the reliability of an individual component
  can decrease the resilience of the encompassing organization if other
  components adapt by losing their capacity to accommodate its failure."
  The last clause, the remedy of holding realized reliability near the
  guarantee, is the book's, which A34 paraphrases more loosely; the gap
  fill says so. The wording is A's (ChatGPT, in the exchange "Memes,
  Contracts, and Systemic Normativity"); adopting it is the owner's call.
rests_on:
- CLAIM-1216
---

<!-- inactive-ok-file: ARG-257 CASE-424 CLAIM-603 CLAIM-677 LIT-3234 — Proposed, Deferred or new; filed or registered with the exchange 'Memes, Contracts, and Systemic Normativity', cited whatever their standing -->

# CLAIM-1256: Over-reliable providers lower resilience

## The claim

A34 §2 reads the Chubby planned outage ([CASE-424](../cases.d/CASE-424.md)) as "a concrete
instance of the developmental mechanism we have been discussing": a chain
from "Exceptional service reliability" through "Expectation formation",
"Adaptive specialization" ("Fallback mechanisms become neglected or
absent"), "Implicit dependency" and "Systemic vulnerability" to
"Controlled perturbation exposes the dependency". "The service's actual
behavior had become the basis of a structural expectation stronger than
its declared guarantee." Its general sentence is the one quoted in the
summary.

A34 bounds it itself: "It is important not to overstate the case: this
directly demonstrates acquired dependence and mismatched expectations, not
necessarily a mutually maintained implicit contract in our narrower
sense." The claim here keeps to that: acquired dependence beyond a
declared guarantee, not an implicit contract (the exchange's account of
implicit contracts is filed from U16 onward, by another group).

## What it adds to the record

[CLAIM-603](CLAIM-603.md) holds that a capability lost because another reliably supplies
it is the Black Queen's loss, and that the supply decides whether the loss
is dependence or division of labour. [CLAIM-677](CLAIM-677.md) holds that adoption can
make a technology practically compulsory. Neither has a declared
guarantee in it. This claim's content is the gap between what the
provider declares and what it realizes: the consumers' loss is a
dependence on more than the provider underwrote, and the provider can
close the gap from its side.

## Gap filled: the book's remedy is calibration, not only exposure

A34 says "Google's historical response was to introduce controlled
outages when necessary to expose inappropriate dependencies". The SRE
book ([LIT-3234](../literature.d/LIT-3234.md), checked against the web edition on 2026-11-24) states
the principle more sharply: "SRE makes sure that global Chubby meets, but
does not significantly exceed, its service level objective. In any given
quarter, if a true failure has not dropped availability below the target,
a controlled outage will be synthesized by intentionally taking down the
system." The remedy is to keep the realized regularity at the declared
one, spending the error budget on purpose, so that dependents meet the
guarantee as it is; exposure of the dependencies already formed is its
effect ("we are able to flush out unreasonable dependencies on Chubby
shortly after they are added"). That is the claim's last clause. The
section is the assistant's (Claude, in this session); adopting it is the
owner's call.

## Standing

Proposed, in A's voice, from one documented specimen; [ARG-257](../arguments.d/ARG-257.md) says
how much the specimen carries. [LEAD-265](../leads.d/LEAD-265.md) would test it in simulation.

## Note of 2026-11-24: the structural expectation it instantiates, the closing pass

<!-- inactive-ok-file: CLAIM-1216 — Proposed; filed from the same exchange -->

A20 §2's consumer that "gave up its buffer against a reliable producer"
and "now presupposes reliable delivery" is held as [CLAIM-1216](CLAIM-1216.md): an
expectation embodied in a capacity no longer maintained. This claim is
that mechanism with a declared guarantee beside it, so that the excess of
realized over declared reliability is what induces the loss, and with the
book's remedy of holding realized reliability near the guarantee. It
complements the earlier entry; it does not rest on it, since the Chubby
case carries it alone. The wording is the assistant's (Claude, in this
session); adopting it is the owner's call.

## Note of 2026-11-24: rests on structural expectation, at the owner's ruling on duplicates

At the owner's word (2026-11-24), this claim now rests on [CLAIM-1216](CLAIM-1216.md)
instead of complementing it. [CLAIM-1216](CLAIM-1216.md) (A20 §2) is the mechanism: an
expectation realized in a capacity the dependent has stopped maintaining.
This claim (A34 §2, Google's Chubby) applies it to a provider whose
realized reliability exceeds its guarantee, and adds the remedy, holding
realized reliability near the declared level. Not a duplicate: one is the
mechanism, the other its engineering consequence. The wording is the
assistant's (Claude, in this session); adopting it is the owner's call.
