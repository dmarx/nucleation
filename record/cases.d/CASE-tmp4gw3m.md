---
status: Proposed
title: 'A fail-safe relay: a valve held closed only while current energizes a relay opens by spring when the current stops, so an absence of input has an immediate consequence with no test, stored expectation or timeout'
version: 1
standing: stipulated
kind: construction
tags:
- control-theory
- epistemology
date: '2026-11-12'
line:
- record-as-apparatus
bears_on:
- QUESTION-285
summary: >-
  The counterexample in the review of #483 the owner relayed on
  2026-11-12, to the first version of CLAIM-tmpz1xb5, which made a
  started interval, a stored expectation and a timeout necessary for an
  absence to carry anything. A relay must stay energized to hold a valve
  closed. When the current stops, a spring opens the valve. The absence
  of input has an immediate, consequential effect, with no separately
  initiated test, no stored expectation and no timeout event. Physical
  organization is still required, the relay state, the spring and the
  coupling. The claim was narrowed to registering a bounded non-response.
  The case marks the edge of that scope and is not a counterexample to
  the narrowed claim. No relation scheme links a case to a claim's scope
  (bounds runs from a THEORY), so the claim's body cites it. Proposed.
  The case is the review's; adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpz1xb5 CASE-tmpv6i22 CASE-tmpaky45 — filed from the same exchange, Proposed -->

# CASE-tmp4gw3m: A fail-safe relay: a valve held closed only while current energizes a relay opens by spring when the current stops, so an absence of input has an immediate consequence with no test, stored expectation or timeout

## The case

From the review of #483 the owner relayed on 2026-11-12: "a fail-safe
relay that must remain energized to hold a valve closed; remove the
current and a spring opens the valve."

A valve is held closed by a relay. The relay holds only while a control
current energizes it, and a spring pulls the valve open otherwise. When
the current stops, for whatever reason, the valve opens at once.

Held fixed: the relay, the spring and their coupling. Varied: whether
the current is present.

## What it can show

That an absence can be consequential with no apparatus that registers it
as the failure of an expected event. Nothing starts a test, nothing
stores what should have happened, and nothing waits for a deadline. The
review: "The absence of input has an immediate consequential effect with
no separately initiated test, stored expectation or timeout event". This
is the design principle of fail-safe systems: absence of the holding
signal is itself the trigger. It is the same organization a sprinkler
could have if its detector held the valve shut (CASE-tmpv6i22).

So a timeout is sufficient for a consequential absence and not
necessary. CLAIM-tmpz1xb5 is narrowed to registering a bounded
non-response, as in the debugger's test (CASE-tmpaky45), and this case
lies outside it.

## What it cannot show

- That the absence is registered as anything. Nothing here classifies
  the outcome or keeps a trace of the current's stopping once the valve
  has opened, beyond the valve's position.
- That the relay's absence means what the debugger's does. The relay
  carries no evidence about a mechanism under test. It acts on an
  absence; it does not diagnose one.
