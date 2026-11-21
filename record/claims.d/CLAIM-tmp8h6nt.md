---
status: Proposed
title: 'A power-law distribution does not identify the mechanism that produced it, nor does a shared power law show a shared mechanism or universality class; the mechanism has to be read from the dynamics, whether gain scales with size, whether there are floors or resets, whether the cutoff grows with the system, after the tail has been fitted against alternatives such as the lognormal'
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A family of mechanisms, each producing a power-law tail, whose members
  could be told apart from the shape of the size distribution alone (its
  exponent, its curvature, its cutoff) without dynamics or a change of
  system size; or a case in which the three dynamical tests named here
  pick the wrong mechanism.
tags:
- probabilistic-modeling
- complex-systems
- philosophy-of-science
date: '2026-11-21'
line:
- formal-apparatus
rests_on:
- CLAIM-tmp1dlyp
grounds:
- LIT-tmpjai28
- LIT-tmpwdtfj
- LIT-tmpl2b2l
summary: >-
  A's, from A1 §4 and §7 and A3 §3 to §7 of the exchange "Rich Get Richer
  Power Laws" (2026-11-20). A power law is a description and a mechanism
  is a cause. Several mechanisms give the same tail, and they measure
  different things, entity sizes against event sizes. So identification
  needs dynamics, and Clauset, Shalizi and Newman's point that a straight
  log-log line is not evidence of a power law comes first. The
  assistant (Claude, in this session) adds a section naming the confound
  A's attachment test leaves open, and marks A's "key intervention" row
  as unsupported. The works are registered and unread. The wording is A's
  (the other assistant in the exchange "Rich Get Richer Power Laws", A1
  and A3); adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmpjai28 LIT-tmpwdtfj LIT-tmpl2b2l LIT-tmp1cgul — Deferred; registered from this exchange and not read -->
<!-- inactive-ok-file: CLAIM-tmp1dlyp CLAIM-tmpiervv CLAIM-tmply70l LEAD-tmpp8z85 THEORY-777 THEORY-789 — Proposed or new; claims and the lead filed with this one, and held readings cited as neighbours -->

# CLAIM-tmp8h6nt: A power-law distribution does not identify the mechanism that produced it, nor does a shared power law show a shared mechanism or universality class; the mechanism has to be read from the dynamics, whether gain scales with size, whether there are floors or resets, whether the cutoff grows with the system, after the tail has been fitted against alternatives such as the lognormal

## The claim (A1, A3)

- **Description is not mechanism.** "The distribution describes *what the
  system looks like*. The mechanism explains *how it got there*" (A1 §7).
  "Just because you observe extreme inequality does not mean cumulative
  advantage created it." "Multiplicative random growth, for example,
  often produces lognormal distributions instead. A power-law pattern in
  data is therefore not, by itself, proof of preferential attachment"
  (A1 §4).
- **The mechanisms measure different things.** "Preferential attachment
  explains how **some entities become much larger than others**.
  Self-organized criticality explains how **some events become much
  larger than others**" (A3 §3). A's reasoning adds that "similar
  power-law plots can represent different quantities: Kesten sizes,
  network degrees, or avalanche events. Their exponents and empirical
  tests aren't interchangeable."
- **A shared law is not a shared class.** Power laws express scale
  invariance, f(ax) = a^(−γ) f(x), "However, two systems displaying power
  laws are not necessarily in the same universality class, and a common
  distribution alone does not imply a common mechanism" (A3 §7). The
  record holds universality only in its Ising readings (THEORY-777,
  THEORY-789).
- **Read the dynamics** (A3 §5). For attachment: do "participants with
  twice as many existing connections receive roughly twice as many new
  ones"? For multiplicative growth: is growth "approximately proportional
  to current size", and are there "floors or reset mechanisms"? For
  self-organized criticality: "thresholds, cascades, correlations, slow
  driving, and whether the event-size cutoff changes systematically with
  system size."
- **Fit first.** "a straight line on a log-log plot is not sufficient
  evidence of a power law, much less evidence of a particular generating
  mechanism" (A3 §5). Clauset, Shalizi and Newman (LIT-tmpjai28) fit the
  tail by maximum likelihood and compare it with the lognormal and other
  alternatives. A3 §3 adds that a power law in earthquakes or fires "does
  not establish that they are self-organized critical; the empirical
  evidence and applicability remain debated." Broido and Clauset
  (LIT-tmp1cgul), whom A alludes to later (A10), carry the same caution
  over to networks.

## What the tests leave open (the assistant's)

- **The attachment test is confounded by fitness and age.** "Twice the
  degree, twice the new links" is also what a node of fixed high quality
  would show, if quality raises its degree and its future links alike.
  Age confounds too, since old nodes have both. A's "controlling for other
  relevant factors" names the problem and does not solve it. What
  separates attachment from fitness is within-node variation: gains
  tracking a node's own degree changes over time, or an exogenous shock
  to degree (a random boost) followed by the node's later gains. Without
  one of these, the test cannot tell cumulative advantage from
  heterogeneity, the same confusion A warns of at A5 §4 for mixtures.
- **The tests overlap.** Linear attachment is proportional growth
  (CLAIM-tmply70l), so the attachment test and the Gibrat test answer
  yes together. What separates them is entry and floors
  (CLAIM-tmpiervv), which the multiplicative test asks about.
- **The cutoff test** for criticality is LEAD-tmpp8z85.

## Not supported

A3 §4's table row "Key intervention" (change how new resources are
allocated / change growth risks, floors, or redistribution / change
thresholds, coupling, or stress accumulation) and A3 §2's policy
paragraph are A's speculation. The exchange gives no model of an
intervention, and no source. They are noted here and not filed.

## What it does not say

- Not that the shape of the distribution is uninformative. A lognormal
  body with a Pareto tail, or a cutoff that moves with system size, does
  narrow the field.
- Not A3 §6's further distinction, "**Statistical predictability and
  event-level predictability are different things**", which is general and
  left as a gloss.
