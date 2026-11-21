---
status: Proposed
title: "Mitzenmacher's survey supports multiplicative growth with exponentially distributed ages as a route to a power law, but keeps preferential attachment apart from it, so it corroborates the identification of the two and does not ground it"
version: 1
form: source
grounds:
- THEORY-tmp23821
concludes:
- CLAIM-tmply70l
tags:
- probabilistic-modeling
- network-science
date: '2026-11-21'
line:
- formal-apparatus
summary: >-
  CLAIM-tmply70l, the assistant's derivation that the Barabási–Albert power
  law is the age mechanism in logarithmic time, listed Mitzenmacher
  (LIT-tmpwdtfj) among its grounds. Read, the survey gives the age
  mechanism for Gibrat growth (§7: exponential ages on an exponentially
  growing Web, Reed's double Pareto) and an attachment model that always
  has entry (§3), but treats them separately and never casts attachment in
  log-time. It is independent evidence for the ingredient, not a premise of
  the identification, which is the claim's own derivation. So it moves to
  corroborates. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmply70l THEORY-tmp23821 — Proposed; the claim and the reading this argument joins -->

# ARG-tmpp2xln: Mitzenmacher's survey supports multiplicative growth with exponentially distributed ages as a route to a power law, but keeps preferential attachment apart from it, so it corroborates the identification of the two and does not ground it

## The inference

CLAIM-tmply70l: what separates linear preferential attachment from
Gibrat's lognormal growth is continual entry, because the mean-field
attachment solution is proportional growth with exponentially distributed
log-ages.

## Critical questions (source)

**Does the work say this, read in context?** It says the ingredient. §7:
"instead of examining X_t for a specific value of t, we examine the random
variable X_T where T itself is a random variable", and a lognormal stopped at
an exponential time has power-law tails; Huberman and Adamic's sites, with
exponentially distributed ages on a growing Web, are the example. §3's
model adds a page at every step. The paper does not join §3 to §7, except
through its own recursive-tree model, and does not say attachment's power
law is an age effect.

**Is it said within the scope the claim needs?** For Gibrat growth with
entry, yes. For the identification, no; that is the claim's change of
variables, which it checks by simulation.

**Does the claim lean on the reading for more than it holds?** Listing it
as a ground suggested the identification was the survey's. It is not.

## Verdict

LIT-tmpwdtfj moves from the claim's grounds to `corroborates` on
THEORY-tmp23821. The claim still grounds on Barabási and Albert and on
Reed (both unread) and on its own derivation.
