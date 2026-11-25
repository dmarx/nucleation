---
status: Proposed
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A showing that, for organizations of the kind in question, every
  separation of observing from acting authority, or of one purpose of access
  from another, that keeps constituents' protection lowers correctability as
  much as an equal cut in the information collected would, so that the
  trade-off is fixed by the amount of information and architecture cannot
  move it.
tags:
- society-and-governance
- privacy
- self-governance
- software-engineering
date: '2026-11-24'
line:
- dependence-and-domination
- organizational-normativity
works:
- governance-of-becoming
uses:
- TERM-064
- TERM-085
complements:
- CLAIM-359
- CLAIM-523
- CLAIM-tmpp91oy
- CLAIM-tmp9xge5
title: 'Separate authority to observe from to act'
statement: >-
  An organization's capacity to discover and correct its deficiencies and
  its constituents' protection against unjustified, informationally mediated
  intervention are distinct achievements whose joint realizability turns on
  separating authority to observe from authority to act, and access for one
  purpose from access for another, sufficient observability under bounded
  authority, not on maximizing or minimizing the information available
summary: >-
  A42 §§8–9 and 13 of the exchange "Memes, Contracts, and Systemic
  Normativity" (ChatGPT, 2026-11-24), its proposition D, "Privacy-preserving
  correctability", with its principle of "sufficient observability under
  bounded authority, rather than maximum observability". [CLAIM-359](CLAIM-359.md) already
  holds security and self-governance as distinct achievements, with least
  privilege, separation of duties and revocable authorization serving both;
  this carries them from execution to observation. Its model is stipulated.
  The SRE side is another group's filing. The wording is A's (ChatGPT, in the
  exchange "Memes, Contracts, and Systemic Normativity"); adopting it is the
  owner's call.
---


# CLAIM-tmp3cywa: Separate authority to observe from to act

## The claim

A42 §13: "An organization should be capable of discovering and correcting
relevant deficiencies without unnecessarily exposing its constituents to
discretionary intervention." It lists the distinctions to be kept:
authority to observe and authority to act; access for one purpose and
access for another; public accountability and unrestricted personal
exposure; detection of violations and enforcement of conformity;
independent dissent and consequentially harmful conduct; legitimate
confidentiality and concealment of wrongdoing. Without them, "An
organization ... may respond to its need for correctability by
establishing an architecture of pervasive control."

A42 §8 puts each reliability concern beside an autonomy concern: can we
diagnose the component, and what internal distinctions must it disclose;
can we audit it, and can it challenge inappropriate auditing; can we detect
anomalous behaviour, and who determines what counts as anomalous. Hence
"**sufficient observability under bounded authority**, rather than maximum
observability". It notes that [CLAIM-359](CLAIM-359.md) recognizes "independent audits, least
privilege, separation of duties and revocable authorization" (checked:
[CLAIM-359](CLAIM-359.md)'s body names them), and that "These mechanisms apply to
observation as well as execution."

## The formal version

A42 §9 splits tasks into justified ones 𝒬₊ and unjustified ones 𝒬₋ and takes
L₊(M) = L(M; 𝒬₊, B₊) and L₋(M) = L(M; 𝒬₋, B₋), "applications of [TERM-064](../terms.d/TERM-064.md)'s
task-relative legibility measure". The aim is an architecture that "makes
justified tasks adequately realizable while appropriately restricting the
affordances for unjustified tasks", not the one with most information. Its
interactive model is stipulated ("The functions are stipulated, not
empirical estimates"); it assumes safeguards that cut exposure without
cutting diagnostic use, which is the case the claim needs to exist, not a
showing that it does. A42 names the mechanisms ("Data minimization,
purpose limitation, local computation, aggregation, controlled disclosure
and independent authorization") and their limit: "risks arising from
combining apparently innocuous information". "The research objective would
be to identify conditions under which those mechanisms expand the jointly
realizable space of reliability and autonomy."

## What is held and what is added

[CLAIM-359](CLAIM-359.md) holds the distinction of achievements and the safeguards that serve
both; [CLAIM-523](CLAIM-523.md) and [TERM-085](../terms.d/TERM-085.md) hold correctability. Added: the separation
applied to observation, and the two-task reading of [TERM-064](../terms.d/TERM-064.md)'s score.
