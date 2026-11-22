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
    longer calls those works unread, THEORY-2173 replaces LIT-2987
    in grounds (ARG-172) and THEORY-2172 joins them (ARG-
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
- THEORY-2173
- THEORY-2172
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
<!-- inactive-ok-file: THEORY-2202 THEORY-2201 — Proposed or new; readings of 2026-11-22 -->
<!-- inactive-ok-file: THEORY-2169 THEORY-2173 THEORY-2172 ARG-172 ARG-170 CLAIM-817 CLAIM-806 — Proposed; the readings of 2026-11-22, their arguments, and neighbouring claims -->
<!-- inactive-ok-file: LIT-3041 — Deferred; registered and unread -->
<!-- inactive-ok-file: CLAIM-824 CLAIM-830 THEORY-777 THEORY-789 THEORY-2150 ARG-141 CLAIM-795 — Proposed or new; claims and the lead filed with this one, and held readings cited as neighbours -->
<!-- inactive-ok-file: THEORY-2176 THEORY-2175 THEORY-2177 CLAIM-857 LIT-3040 LIT-3005 — Proposed, Deferred or Unfetched; the readings of 2026-11-22, the assistant's condition on the spread, Miller's work, and Kesten's, read through neighbours -->

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
[THEORY-2173](../theory.d/THEORY-2173.md) replaces [LIT-2987](../literature.d/LIT-2987.md) in `grounds` and [THEORY-2172](../theory.d/THEORY-2172.md) joins
it. Version 2.

## Note of 2026-11-22: Newman, read

Newman's review ([LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-2261](../notes.d/NOTE-2261.md); the reading is
[THEORY-2169](../theory.d/THEORY-2169.md)) **supports the first clause** and **"fit first" in
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
holds the tail open ([QUESTION-506](../questions.d/QUESTION-506.md)), and its reading of Davis and
Weinstein ([THEORY-1499](../theory.d/THEORY-1499.md)) tells against size-dependent growth in the
ranking of cities. [THEORY-2169](../theory.d/THEORY-2169.md) `corroborates` the claim.

## Note of 2026-11-22: Clauset, Shalizi and Newman, read

Their paper ([LIT-2987](../literature.d/LIT-2987.md), read in [NOTE-2262](../notes.d/NOTE-2262.md); the reading is
[THEORY-2173](../theory.d/THEORY-2173.md)) **supports "fit first"**, **supports the first clause
indirectly**, and **leaves the dynamical tests open** ([ARG-172](../arguments.d/ARG-172.md)). The
claim cites it correctly for "a straight line on a log-log plot is not
sufficient" ("necessary but not sufficient", §4, p. 15) and for fitting
by maximum likelihood against the lognormal (Box 1, §5). It does not
state the first clause; it comes nearest where the lognormal "is not
ruled out for any of our data sets except the HTTP connections" and
undecided cases need "a mechanistic or other nonstatistical argument"
(p. 26). Where forms do separate, the cutoff for fires, quakes and web
hits, shape narrows the field, as "What it does not say" allows; the
authors hold that form "may matter greatly" for mechanism (p. 30).
[THEORY-2173](../theory.d/THEORY-2173.md) replaces the work in `grounds`.

## Note of 2026-11-22: Broido and Clauset, read

Their paper ([LIT-2963](../literature.d/LIT-2963.md), read in [NOTE-2263](../notes.d/NOTE-2263.md); the reading is
[THEORY-2172](../theory.d/THEORY-2172.md)) **supports** the claim for network degrees, as the claim
said it would ([ARG-170](../arguments.d/ARG-170.md)): the degree distribution "represents
relatively weak evidence when trying to distinguish generating
mechanisms"; the method fits against the lognormal, at least as good in
88%. It **qualifies** in the direction the claim allows: the absence of a
power law limits "any mechanism that necessarily produces power-law
degree distributions", so shape informs negatively. It adds a converse:
"some variations of preferential attachment do not produce power-law
degree distributions" (compare [CLAIM-817](CLAIM-817.md), [CLAIM-806](CLAIM-806.md)). It asks for a test
"that goes beyond static degree distributions" and names none. Its rarity
verdict is disputed ([LIT-3041](../literature.d/LIT-3041.md)), which does not touch what the claim
takes from it. [THEORY-2172](../theory.d/THEORY-2172.md) joins `grounds`. Status unchanged.

## Note of 2026-11-22: Beck and Cohen; Corominas-Murtra, Hanel and Thurner; Reed and Hughes, read

- **Corominas-Murtra, Hanel and Thurner** ([LIT-2997](../literature.d/LIT-2997.md), [NOTE-2266](../notes.d/NOTE-2266.md);
  [THEORY-2175](../theory.d/THEORY-2175.md)) **support the first clause**: a further route to Zipf's
  law in word frequencies, beside preferential attachment, Mandelbrot's
  optimization and Miller's random typing ([LIT-3040](../literature.d/LIT-3040.md)), with no feedback.
  Their own word example is an instance of what this claim warns against:
  λ = 0.9 is read off a fitted rank slope (p. 4, Fig. 4), with no
  independent measure of nestedness.
- **Reed and Hughes** ([LIT-3007](../literature.d/LIT-3007.md), [NOTE-2264](../notes.d/NOTE-2264.md); [THEORY-2177](../theory.d/THEORY-2177.md)):
  **background, illustrating the claim**. One mechanism is offered for six
  domains, against self-organized criticality and highly optimized
  tolerance, on log-log plots alone, with no fit or test against the
  lognormal.
- **Beck and Cohen** ([LIT-2962](../literature.d/LIT-2962.md), [NOTE-2265](../notes.d/NOTE-2265.md); [THEORY-2176](../theory.d/THEORY-2176.md)) **support
  it in kind**: their discriminant, the third-order term g(q) of the
  small-variance expansion (p. 9), separates one superstatistics from
  another, not a mixture from a feedback. The assistant's [CLAIM-857](CLAIM-857.md)
  adds a caution on the fitting step: a lognormal spread of rates gives a
  tail whose log-log slope steepens only slowly (about −2.6 to −10.4 per
  decade over four decades), which a finite sample may read as a power law.

No edge: these are cases of the claim, and it rests on [CLAIM-795](CLAIM-795.md), which
these readings ground.

## Note of 2026-11-22: readings filed in parallel

Bearings relayed from the readings filed in parallel this day; their
notes hold the detail, and no edge is written here.

- **Krapivsky, Redner and Leyvraz** ([LIT-2974](../literature.d/LIT-2974.md)) **support** the first
  clause: for degree exponents 0.8 ≲ γ ≲ 1 a power law and a stretched
  exponential cannot be told apart up to k = 1000, and their fit to the
  ISI citation data fits both.
- **Bak, Tang and Wiesenfeld** ([LIT-2992](../literature.d/LIT-2992.md)) are a **contrast**: they read a
  mechanism off a straight log-log line, the inference this claim denies.
- **Kesten, read through neighbours** ([LIT-3005](../literature.d/LIT-3005.md)) **supports** it: Grey's
  result that a power tail of the stationary law may come from the additive
  term B alone, so the same tail need not come from the multiplicative
  balance.
- **Barabási's chapter** ([LIT-2968](../literature.d/LIT-2968.md)): its §5.7 test of attachment from
  growth data **parallels** this claim's attachment test; its §5.11
  argument that growth and preferential attachment are necessary and
  sufficient for a scale-free network is a **contrast**, a mechanism
  claimed from the distribution's shape.

## Note of 2026-11-22: Kardar, Parisi and Zhang, and Takeuchi and Sano, read

Two readings of 2026-11-22 **support the claim**, one as evidence and one
as a parallel.

- **Evidence: a shared exponent, different classes.** In one dimension the
  KPZ interface has the same static roughness exponent as the linear
  ("ideal") interface, χ = ½, and strip simulations had read the one as
  the other, "a result of a peculiarity of one-dimensional interfaces";
  only the dynamics, z = 3/2 against 2, tell the classes apart (Kardar,
  Parisi and Zhang, [LIT-2978](../literature.d/LIT-2978.md), [NOTE-2287](../notes.d/NOTE-2287.md), p. 891). That is this claim's
  "a shared power law does not show a shared … universality class", and
  its "read from the dynamics". [THEORY-2202](../theory.d/THEORY-2202.md) `corroborates` the claim.
- **Parallel: the class identified beyond the exponents.** Takeuchi and
  Sano ([LIT-2982](../literature.d/LIT-2982.md), [NOTE-2284](../notes.d/NOTE-2284.md); [THEORY-2201](../theory.d/THEORY-2201.md)) go "beyond the scaling
  laws" (p. 1): the class is fixed by the whole fluctuation distribution
  and the correlation, and the distribution splits curved from flat
  fronts (GUE from GOE), which share the exponents. No edge: the two are
  sub-classes of one universality class, so it is a parallel, not a case
  of two mechanisms.
