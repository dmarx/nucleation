---
status: Proposed
title: "Barabási and Albert's mean-field derivation and the chapter's first-mover reading, read as sources, carry the age half of the claim that entry separates linear attachment from Gibrat growth, while Model B's transient power law without growth qualifies its Pólya-urn contrast without defeating it"
version: 1
form: source
grounds:
- THEORY-tmpfrz0k
- THEORY-tmpzmy66
concludes:
- CLAIM-830
tags:
- network-science
- probabilistic-modeling
date: '2026-11-22'
line:
- formal-apparatus
summary: >-
  Whether Barabási and Albert (LIT-3004, NOTE-tmpwgw8e) and the chapter
  (LIT-2968, NOTE-tmpnpqc8) carry CLAIM-830. They carry its premise, the
  arrival-time derivation at equal intervals, and its age reading: "hubs
  are large because they arrived earlier", with γ = 1/β + 1, so the
  survival exponent 1/β = 2 is the claim's λ/g. Neither casts the process
  in log time or compares it with Gibrat, so the identification is the
  claim's own. Model B, preferential attachment among a fixed set of
  vertices, shows power-law scaling at early times; that qualifies the
  claim's contrast with a Pólya urn but does not meet its defeated_if,
  since the tail is transient. The wording is the assistant's (Claude, in
  this session); adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-830 THEORY-tmpfrz0k THEORY-tmpzmy66 — Proposed; the claim and the readings this argument joins -->

# ARG-tmpmylwc: Barabási and Albert's mean-field derivation and the chapter's first-mover reading, read as sources, carry the age half of the claim that entry separates linear attachment from Gibrat growth, while Model B's transient power law without growth qualifies its Pólya-urn contrast without defeating it

## The inference

CLAIM-830. Grounds: THEORY-tmpfrz0k (the premise) and THEORY-tmpzmy66
(the age reading and the caveat).

## Critical questions (source)

**Does the work say this, read in context?** The premise, yes:
∂k_i/∂t = k_i/2t, k_i = m(t/t_i)^0.5, "Assuming that we add the vertices
at equal time intervals" (preprint pp. 6 to 7). The age reading, yes: "The
earlier node i was added, the higher is its degree ki(t). Hence, hubs are
large because they arrived earlier, a phenomenon called first-mover
advantage" (chapter §5.4), and (5.10) "links the degree exponent" to the
dynamical exponent. The caveat, yes: the continuum theory "fails to
accurately predict the pre-factors" (§5.5), as the claim's "accounts for
the exponent ... not for any one node's degree". The identification with
Gibrat growth in log time, no: neither source mentions log time, and
Gibrat appears only in the chapter's bibliography.

**Is it said within the scope the claim needs?** For the premise and the
age half. Not for the identification, which stays the claim's derivation.

**Is there a counter-instance?** Model B. "In model B we start with N
vertices and no edges ... While at early times the model exhibits
power-law scaling, P(k) is not stationary", and it ends with all vertices
connected (preprint p. 6). That is linear attachment without entry
showing a power law, which the claim's `defeated_if` names. It does not
defeat it:

- the tail is transient, and the claim's contrast (and its `defeated_if`)
  concern the long-run tail; "stationary" should be written into the
  contrast;
- the early phase is not a Pólya urn among equals. Nodes start at degree
  zero, counted as one, and the chapter says that early on "each new link
  connects previously unconnected nodes. In this stage the model's
  evolution is indistinguishable from the Barabási-Albert model with m=1"
  (§5.6). *On the delegated reader's gloss, not the chapter's or the
  paper's*, those previously unconnected nodes act as entrants, so the
  transient power law is entry in effect and fits the claim's thesis.

## Verdict

Support for the premise and the age half; THEORY-tmpfrz0k replaces
LIT-3004 in the grounds, and THEORY-tmpzmy66 corroborates. Model B
qualifies the Pólya-urn contrast, corrected in place on CLAIM-830.
