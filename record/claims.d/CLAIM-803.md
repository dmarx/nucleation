---
number: 803
status: Proposed
formerly:
- CLAIM-tmp8h6nt
title: 'A power-law distribution does not identify the mechanism that produced it, nor does a shared power law show a shared mechanism or universality class; the mechanism has to be read from the dynamics, whether gain scales with size, whether there are floors or resets, whether the cutoff grows with the system, after the tail has been fitted against alternatives such as the lognormal'
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Edited in place on 2026-11-22 after Newman's review, Clauset,
    Shalizi and Newman, and Broido and Clauset were read: the summary no
    longer calls those works unread, THEORY-tmpw4qgu replaces LIT-2987
    in grounds (ARG-tmps95tv) and THEORY-tmphcnj3 joins them (ARG-
    tmpmt4gj). The thesis and status are unchanged.
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
- CLAIM-795
grounds:
- LIT-2992
- THEORY-2150
- THEORY-tmpw4qgu
- THEORY-tmphcnj3
summary: >-
  A's, from A1 §4 and §7 and A3 §3 to §7 of the exchange "Rich Get Richer
  Power Laws" (2026-11-20). A power law is a description and a mechanism
  is a cause. Several mechanisms give the same tail, and they measure
  different things, entity sizes against event sizes. So identification
  needs dynamics, and Clauset, Shalizi and Newman's point that a straight
  log-log line is not evidence of a power law comes first. The
  assistant (Claude, in this session) adds a section naming the confound
  A's attachment test leaves open, and marks A's "key intervention" row
  as unsupported. Mitzenmacher's review was read on 2026-11-21, and Newman's review,
  Clauset, Shalizi and Newman, and Broido and Clauset on 2026-11-22 (see
  the dated notes); the other works are registered and unread. The wording is A's
  (the other assistant in the exchange "Rich Get Richer Power Laws", A1
  and A3); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmpw4qgu THEORY-tmphcnj3 ARG-tmps95tv ARG-tmpmt4gj CLAIM-841 CLAIM-817 CLAIM-806 — Proposed; the readings of 2026-11-22, their arguments, and neighbouring claims -->
<!-- inactive-ok-file: LIT-tmpvmrkv LIT-2992 — Deferred; registered and unread -->
<!-- inactive-ok-file: CLAIM-824 CLAIM-830 THEORY-777 THEORY-789 THEORY-2150 ARG-141 CLAIM-795 — Proposed or new; claims and the lead filed with this one, and held readings cited as neighbours -->

# CLAIM-803: A power-law distribution does not identify the mechanism that produced it, nor does a shared power law show a shared mechanism or universality class; the mechanism has to be read from the dynamics, whether gain scales with size, whether there are floors or resets, whether the cutoff grows with the system, after the tail has been fitted against alternatives such as the lognormal

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
  record holds universality only in its Ising readings ([THEORY-777](../theory.d/THEORY-777.md),
  [THEORY-789](../theory.d/THEORY-789.md)).
- **Read the dynamics** (A3 §5). For attachment: do "participants with
  twice as many existing connections receive roughly twice as many new
  ones"? For multiplicative growth: is growth "approximately proportional
  to current size", and are there "floors or reset mechanisms"? For
  self-organized criticality: "thresholds, cascades, correlations, slow
  driving, and whether the event-size cutoff changes systematically with
  system size."
- **Fit first.** "a straight line on a log-log plot is not sufficient
  evidence of a power law, much less evidence of a particular generating
  mechanism" (A3 §5). Clauset, Shalizi and Newman ([LIT-2987](../literature.d/LIT-2987.md)) fit the
  tail by maximum likelihood and compare it with the lognormal and other
  alternatives. A3 §3 adds that a power law in earthquakes or fires "does
  not establish that they are self-organized critical; the empirical
  evidence and applicability remain debated." Broido and Clauset
  ([LIT-2963](../literature.d/LIT-2963.md)), whom A alludes to later (A10), carry the same caution
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
  ([CLAIM-830](CLAIM-830.md)), so the attachment test and the Gibrat test answer
  yes together. What separates them is entry and floors
  ([CLAIM-824](CLAIM-824.md)), which the multiplicative test asks about.
- **The cutoff test** for criticality is [LEAD-211](../leads.d/LEAD-211.md).

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

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md), read in [NOTE-2237](../notes.d/NOTE-2237.md); the reading is
[THEORY-2150](../theory.d/THEORY-2150.md)) **supports the first clause** and does not reach the
remedy. "Just because one finds a compelling mechanism to explain a power
law does not mean that there are not other, perhaps simpler, explanations"
(§6, p. 238) is nearly the claim's opening. It shows Zipf's law reached by
preferential attachment (§3), Mandelbrot's optimization (§4) and monkeys
typing at random (§6); and a lognormal "may appear linear on a log-log plot
for several orders of magnitude" (§2), so that "it is not clear that a
definitive answer is possible" (§8). It **qualifies** nothing here but
leaves the second half unsupported: §2 calls the log-log line "a simple
empirical test", and there is no fitting method and none of the three
dynamical tests. [THEORY-2150](../theory.d/THEORY-2150.md) replaces the work in `grounds`
([ARG-141](../arguments.d/ARG-141.md)). Random typing and optimization are also mechanisms
[CLAIM-795](CLAIM-795.md)'s catalogue leaves out (see its note of this date).

## Change of 2026-11-22

The summary no longer calls the works read on 2026-11-22 unread;
THEORY-tmpw4qgu replaces LIT-2987 in `grounds` and THEORY-tmphcnj3 joins
it. Version 2.

## Note of 2026-11-22: Newman, read

Newman's review (LIT-2976, read in NOTE-tmpa7yd2; the reading is
THEORY-tmp6jdas) **supports the first clause** and **"fit first" in
part**, and is **milder than the claim**. Many mechanisms, "different
ones ... applicable to different cases" (p. 5); "most experimentally
observed power laws are probably not the result of phase transitions"
(p. 12); Miller, Yule and multiplicative processes all reach similar
slopes. On fitting: a log-log histogram "is, in most cases, a poor way
proceed" [sic] (p. 3), least squares biases the exponent, and a
lognormal of large variance looks straight over orders of magnitude
(§IV.G). No comparison with alternatives and none of the dynamical tests.

**A counterweight.** Newman does assign mechanisms, by plausibility rather
than from dynamics: §V ranks the Yule process and criticality "perhaps the
two most important", and of the Yule process he writes, "For several of
the distributions shown in Fig. 4, especially citations, city populations
and personal income, it is now the most widely accepted theory" (p. 19).
That is a field's verdict from fit and plausibility, which this claim
holds cannot by itself identify the mechanism. For cities the record
holds the tail open (QUESTION-506), and its reading of Davis and
Weinstein (THEORY-1499) tells against size-dependent growth in the
ranking of cities. THEORY-tmp6jdas `corroborates` the claim.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

Their paper (LIT-2987, read in NOTE-tmphbwdu; the reading is
THEORY-tmpw4qgu) **supports "fit first"**, **supports the first clause
indirectly**, and **leaves the dynamical tests open** (ARG-tmps95tv). The
claim cites it correctly for "a straight line on a log-log plot is not
sufficient" ("necessary but not sufficient", §4, p. 15) and for fitting
by maximum likelihood against the lognormal (Box 1, §5). It does not
state the first clause; it comes nearest where the lognormal "is not
ruled out for any of our data sets except the HTTP connections" and
undecided cases need "a mechanistic or other nonstatistical argument"
(p. 26). Where forms do separate, the cutoff for fires, quakes and web
hits, shape narrows the field, as "What it does not say" allows; the
authors hold that form "may matter greatly" for mechanism (p. 30).
THEORY-tmpw4qgu replaces the work in `grounds`.

## Note of 2026-11-22: Broido and Clauset, read

Their paper (LIT-2963, read in NOTE-tmpleyjh; the reading is
THEORY-tmphcnj3) **supports** the claim for network degrees, as the claim
said it would (ARG-tmpmt4gj): the degree distribution "represents
relatively weak evidence when trying to distinguish generating
mechanisms"; the method fits against the lognormal, at least as good in
88%. It **qualifies** in the direction the claim allows: the absence of a
power law limits "any mechanism that necessarily produces power-law
degree distributions", so shape informs negatively. It adds a converse:
"some variations of preferential attachment do not produce power-law
degree distributions" (compare CLAIM-817, CLAIM-806). It asks for a test
"that goes beyond static degree distributions" and names none. Its rarity
verdict is disputed (LIT-tmpvmrkv), which does not touch what the claim
takes from it. THEORY-tmphcnj3 joins `grounds`. Status unchanged.
