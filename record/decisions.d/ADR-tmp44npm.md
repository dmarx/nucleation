---
status: Proposed
title: "An argument's title names its route, its grounds and the step, before its conclusion, and a Rejected argument says where its conclusion's own standing lives, so that rejecting a route is not read as rejecting what it concludes"
version: 1
tags:
- record
- taxonomy
date: '2026-11-21'
summary: >-
  At the owner's objection of 2026-11-21 to [ARG-tmpmvc5e](../arguments.d/ARG-tmpmvc5e.md), whose title
  stated a conclusion ("the behaviour of sloppy models carries over to
  overparameterized neural networks") and whose status, Rejected, judged
  only one route to it: "marking it rejected predisposes future inquiry
  to treat that conclusion (which I think is actually probably correct)
  as rejected, rather than this particular path to that conclusion as
  rejected." Under [ADR-061](ADR-061.md) an argument's status is a verdict on the
  inference, not the conclusion, but its title, which the index shows,
  did not say so. Decided: a title leads with the grounds and the step
  ("X, by analogy, shows that Y"), never the bare conclusion; a Rejected
  argument's summary says where the conclusion's own standing lives, in
  the claim or question that holds it, or that no entry holds it; and an
  untouched conclusion with content of its own is held in an entry of
  its own. One of two alternatives filed together; the other, [ADR-tmpcjfyy](ADR-tmpcjfyy.md),
  makes the title state the verdict instead. The assistant leans to this
  one. The wording is the assistant's (Claude, in this session); adopting
  it is the owner's call.
---
<!-- inactive-ok-file: ADR-tmpcjfyy ARG-tmpmvc5e ARG-tmpv3nqz ARG-tmp2w77g ARG-tmp09yqc ARG-tmpdvwy2 CLAIM-tmp7ijze CLAIM-tmpcg4uu — Proposed, Rejected or new; the alternative and the first application -->

# ADR-tmp44npm: An argument's title names its route, its grounds and the step, before its conclusion, and a Rejected argument says where its conclusion's own standing lives, so that rejecting a route is not read as rejecting what it concludes

## Context

An ARG records what the record says about support: that these grounds do, or do not, establish this conclusion ([ADR-061](ADR-061.md)). Its status is the verdict on the inference, not on the conclusion. "X does not show Y" is the ARG from X to Y, Rejected.

The title is the part of an entry that travels. It is what the index lists, what a search returns and what another entry's reader sees beside the code. Of the record's 40 Rejected ARGs on 2026-11-21, most were titled "X shows that Y", which names the route. Some stated the conclusion alone. The five filed that day from the exchange "Rich Get Richer Power Laws" included [ARG-tmpmvc5e](../arguments.d/ARG-tmpmvc5e.md), "The behaviour of sloppy models carries over to overparameterized neural networks…". Its body said what failed, the analogy from a regular Fisher spectrum, and that "what survives is the weak point that few combinations matter". Its title and status together read as the record rejecting the conclusion.

The owner objected: "this is a *conclusion* that doesn't hold relative to the inference relative to regular fisher matrices specifically. We don't know that that conclusion doesn't hold, but populating the arg with the prose of the conclusion and marking it rejected predisposes future inquiry to treat that conclusion (which I think is actually probably correct) as rejected, rather than this particular path to that conclusion as rejected. maybe we need to be more careful about how we construct our args?" The owner also holds that the conclusion is probably correct, now [CLAIM-tmp7ijze](../claims.d/CLAIM-tmp7ijze.md).

## Decision

- **A title names the route first.** An ARG's title leads with its grounds and the step it takes: "X, by <form>, shows that Y", or "X supports Y". It never states the bare conclusion. A reader of the title alone must be able to tell what was inferred from what.
- **A Rejected ARG says where its conclusion stands.** Its summary has one sentence giving the conclusion's own standing, apart from this route. That sentence names the claim or question that holds the conclusion, with its status, or says that no entry holds it, or says that the record holds evidence against it, naming the entry.
- **An untouched conclusion is held on its own.** Where a route fails but its conclusion is not shown false and has content of its own ([ADR-072](ADR-072.md)), the conclusion is held in a claim or question of its own, in the voice of whoever put it forward. The ARG's `concludes` points there. Rejecting the route then leaves that entry's standing unchanged, as [ADR-061](ADR-061.md) intends.
- **The rule is about construction, not status.** [ADR-061](ADR-061.md)'s convention stands: a route that fails is Rejected.

## Alternatives considered

- **[ADR-tmpcjfyy](ADR-tmpcjfyy.md): titles state the verdict.** A route that fails would be an Active ARG titled "X does not show Y". That is the most legible in an index. But it flips [ADR-061](ADR-061.md)'s convention, so a reader would need to know both the status and the title's polarity to read either. It also needs a sweep of every held ARG's status. It is filed beside this one so the owner can choose.
- **A required `route:` field** naming the grounds and the step. It is machine-checkable, but it changes luria.yaml, which is the owner's ([ADR-082](ADR-082.md)), and it duplicates `grounds` and `form`, which already hold the route as data. The problem is in the prose that travels.
- **Status quo.** Readers would go on reading a route's rejection as the conclusion's, which is the harm the owner named, and most at risk where the conclusion is probably true.

## Consequences

- **First application, in this pull request.** The five ARGs filed on 2026-11-21 are retitled, and each Rejected one's summary gains its standing sentence:
  - [ARG-tmpmvc5e](../arguments.d/ARG-tmpmvc5e.md) and [ARG-tmpv3nqz](../arguments.d/ARG-tmpv3nqz.md) now conclude [CLAIM-tmp7ijze](../claims.d/CLAIM-tmp7ijze.md), the owner's claim that the conclusion probably holds by another route.
  - [ARG-tmp2w77g](../arguments.d/ARG-tmp2w77g.md)'s conclusion is told against by [THEORY-1499](../theory.d/THEORY-1499.md).
  - [ARG-tmp09yqc](../arguments.d/ARG-tmp09yqc.md)'s conclusion is held by other routes, [CLAIM-478](../claims.d/CLAIM-478.md) and [SYNTHESIS-054](../syntheses.d/SYNTHESIS-054.md).
  - [ARG-tmpdvwy2](../arguments.d/ARG-tmpdvwy2.md)'s conclusion is [CLAIM-tmpcg4uu](../claims.d/CLAIM-tmpcg4uu.md)'s, Proposed and untouched.
- **A sweep of the 35 older Rejected ARGs** is its own pull request once this is adopted ([ADR-071](ADR-071.md)). They are retitled where the title states the conclusion alone, and the standing sentence is added. Most already lead with their grounds. Those that state the bare conclusion are the ones at risk, such as [ARG-053](../arguments.d/ARG-053.md), "Low observed exercise of a specialized capability is evidence that its maintenance expenditure is wasteful".
- **The `read-and-file` skill's step 9** gains a sentence on titles, in the adoption pull request.
