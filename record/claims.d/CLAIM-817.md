---
number: 817
status: Proposed
formerly:
- CLAIM-tmpepx9m
title: 'Power law needs linear attachment plus entry'
statement: >-
  Cumulative advantage gives a power law only in a particular form:
  attachment linear in current size together with continual entry of new
  units; with no preference the tail is exponential, with sublinear
  preference stretched-exponential, and with superlinear preference one unit
  takes almost every new link
version: 2
history:
- version: 2
  date: '2026-11-22'
  note: >-
    Revised in place after the readings of 2026-11-22 of Krapivsky, Redner
    and Leyvraz (NOTE-2267), Barabási and Albert (NOTE-2272),
    Barabási's chapter (NOTE-2270) and Merton (NOTE-2268). Grounds
    move from the unread works to the readings THEORY-2181,
    THEORY-2180 and THEORY-2184 (ARG-184, ARG-179);
    Merton's essay leaves the grounds (ARG-180). The naming clause is
    corrected: the four names do not name one feedback, and Merton grounds
    the name only (TERM-145). Added: the tunable exponent
    ν = 1 + μ/a∞ for asymptotically linear kernels; Barabási and Albert as
    the source of A3's "both ingredients" sentence; the chapter's rival
    framing of the aside on hyperbolic geometry, as a contrast. Title and
    status unchanged.
role: thesis
warrant: demonstrated
defeated_if: >-
  A growing-network model in which attachment proportional to k^α with
  α ≠ 1 gives a pure power-law degree tail without some other
  ingredient (fitness, aging, a shifted kernel k + a); or one in which
  linear attachment without continual entry of new nodes gives one. A
  shifted linear kernel changing the exponent does not defeat it, since
  that is still linear attachment.
tags:
- network-science
- complex-systems
- probabilistic-modeling
date: '2026-11-21'
line:
- formal-apparatus
grounds:
- THEORY-2181
- THEORY-2180
- THEORY-2184
uses:
- TERM-145
summary: >-
  A's, from A1 §1 to §4 and §7 and A3 §1 of the exchange "Rich Get Richer
  Power Laws" (2026-11-20), answering the owner's U1 and U2. In the
  Barabási–Albert model, growth plus linear attachment gives
  P(K = k) ∝ k^(−3), and both ingredients are needed. The generalized
  kernel k^α gives an exponential, a stretched-exponential, a power-law or
  a winner-take-all degree distribution (Krapivsky, Redner and Leyvraz,
  unnamed by A), and within the linear case the exponent is tunable. So
  "having cumulative advantage is not enough to guarantee a power law",
  and unequal outcomes need no unequal ability. Checked by simulation in
  this session, and grounded on the readings of 2026-11-22. A also says
  the four names, the Matthew effect among them, name one feedback; read,
  Merton's Matthew effect is credit allotted by rank, not linear
  attachment, so that holds only in the formal sense (corrected
  2026-11-22, [TERM-145](../terms.d/TERM-145.md)). The wording is A's (the other assistant in
  the exchange "Rich Get Richer Power Laws", A1 and A3); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: THEORY-2169 THEORY-2172 THEORY-2181 THEORY-2180 THEORY-2184 THEORY-2178 TERM-145 ARG-184 ARG-179 ARG-180 — Proposed or Rejected; the readings of 2026-11-22 cited in the notes, the term and the arguments filed with them -->
<!-- inactive-ok-file: CLAIM-830 CLAIM-806 CLAIM-803 CLAIM-184 CLAIM-677 THEORY-1927 THEORY-188 — Proposed or new; claims filed from the same exchange and held entries cited as neighbours -->
<!-- inactive-ok-file: ARG-127 ARG-149 THEORY-2150 — new and Proposed or Rejected, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->

# CLAIM-817: Power law needs linear attachment plus entry

## The claim (A1, A3)

**One feedback, several names** (A's; corrected 2026-11-22). "The more
you already have, the easier it becomes to get more … this is called
*preferential attachment* or *cumulative advantage*", and "sometimes called
the *Matthew effect*, after sociologist Robert K. Merton" (A1 §1;
[LIT-3002](../literature.d/LIT-3002.md)). A1 §7 separates three things: "**Power law:** a statistical
description … **Rich-get-richer:** a dynamic mechanism … **Preferential
attachment:** a mathematical implementation of cumulative advantage."

*Correction of 2026-11-22.* Read ([NOTE-2268](../notes.d/NOTE-2268.md)), Merton grounds the name
and its link to cumulative advantage, and nothing more here. His Matthew
effect is credit for a given contribution allotted by the contributor's
rank, with a fixed number of top places and a ratchet among its
mechanisms, and cumulative advantage is "one institutional version" of it
(p. 62); he states no rule of growth in proportion to size. So the four
names do not name one feedback. They do in the formal sense, growth in
proportion to current size, the sense in which Newman lists "Matthew
effect" among the Yule process's names ([NOTE-2261](../notes.d/NOTE-2261.md)); [TERM-145](../terms.d/TERM-145.md)
keeps the senses apart, and this claim uses the formal one ([ARG-180](../arguments.d/ARG-180.md)).

**The base case** (A1 §3; Barabási and Albert, [LIT-3004](../literature.d/LIT-3004.md), read in
[NOTE-2272](../notes.d/NOTE-2272.md), and the *Network Science* chapter, [LIT-2968](../literature.d/LIT-2968.md), read in
[NOTE-2270](../notes.d/NOTE-2270.md)). A new node links to node i with probability k_i/Σk_j.
Then dk_i/dt = k_i/2t, so k_i(t) ≈ (t/t_i)^(1/2). Uniform birth times give
P(K ≥ k) ∝ k^(−2) and P(K = k) ∝ k^(−3). (With m links per node the
mean-field law is 2m²/k³; the simulated exponent is 2.9 ± 0.1, and the
exact distribution is 2m(m+1)/[k(k+1)(k+2)].)

**Both ingredients are needed** (A3 §1): "preferential attachment alone
does not guarantee this result. The combination of growth, the form of
attachment, and other model assumptions determines the distribution." And
"unequal outcomes can arise without unequal innate abilities", though
"observed success can reflect a mixture of quality, luck, timing, and
cumulative advantage". A3 cites Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md)) here;
read, the review does not say this (corrected 2026-11-21: see the note of
that date below). Barabási and Albert do: "both ingredients, namely growth
and preferential attachment, are needed for the development of the
stationary power-law distribution", and "simulations indicate that
scaling is present only for α = 1" ([LIT-3004](../literature.d/LIT-3004.md), preprint pp. 6 to 7;
[ARG-179](../arguments.d/ARG-179.md)). Without growth their Model B shows power-law scaling only
transiently, so "needed" is for a *stationary* power law. A3's
Alice and Bob make the point that under linear attachment the leader
gains more in absolute terms and not in percentage terms.

**The form of the kernel matters** (A1 §4). With P(i) ∝ k_i^α: α = 0
gives "Exponential-type", 0 < α < 1 "Stretched-exponential tail", α = 1
"Power-law", α > 1 "Strong concentration; potentially winner-take-all". A
does not name the source. It is Krapivsky, Redner and Leyvraz
([LIT-2974](../literature.d/LIT-2974.md), read in [NOTE-2267](../notes.d/NOTE-2267.md); [ARG-184](../arguments.d/ARG-184.md)): "A power law distribution
N_k ∼ k^−ν arises only for γ = 1" (p. 1). Within the linear case the
exponent is not fixed at 3: an asymptotically linear kernel A_k → a∞k gives
"ν = 1 + µ/a∞" (p. 2), and with A_1 = 1, A_k = a∞k it is
ν = (3 + √(1 + 8/a∞))/2, anywhere above 2 (a∞ = 1 gives 3, checked with
python3 -I). That is still linear attachment, as this claim's
`defeated_if` allows. Hence "**having cumulative advantage is not enough
to guarantee a power law**."

## Checked (the assistant, with python3 -I)

Simulated growing trees, one link per new node:

- **α = 1, N = 300,000.** The CCDF slope over k = 4 to 128 is −1.98,
  against A's −2. The 100 largest hubs were all born in the first 1% of
  the growth.
- **α = 0, 0.5, 1.5, 2.5, N = 100,000.** The largest degree is 17, 42,
  99,354 and 99,998. With α = 1.5 one node holds 49.7% of all edge ends, which
  is nearly every link, and the second largest has degree 12. With
  α = 2.5 the network is a star.

A's table holds. Its last row needs a sharper word than "potentially":
in these runs a superlinear kernel is a condensation onto one node, not a
heavy tail. Krapivsky, Redner and Leyvraz state the regimes (for α > 2 one
node links to all but finitely many), and read, they say "winner take all"
without hedging; the runs agree. α = 1.5 is itself one of their transition
points, γ = (m+1)/m with m = 2.

## Corrections and what the record already holds

- **A's derivation leaves out what separates the model from Gibrat
  growth.** A3 §4 says preferential attachment "itself involves
  proportional expected growth", yet A contrasts it with multiplicative
  growth, which gives a lognormal. The difference is continual entry,
  which gives a spread of ages. [CLAIM-830](CLAIM-830.md) works this out. It is the
  "growth" half of A3's "growth plus attachment".
- **The test for attachment** that A proposes (A3 §5, does a node with
  twice the degree get twice the new links?) is taken up in
  [CLAIM-803](CLAIM-803.md), with its confound.
- **Path dependence** (A1 §6: "The eventual winner need not be the
  intrinsically best option") is held for urn-type lock-in in
  [THEORY-1927](../theory.d/THEORY-1927.md), [CLAIM-184](CLAIM-184.md) and [CLAIM-677](CLAIM-677.md). A adds the link to heavy tails,
  which this claim carries.
- The record's one other route to power-law degree, hyperbolic geometry
  ([THEORY-188](../theory.d/THEORY-188.md)), needs no attachment at all. *A rival framing* (2026-11-22):
  Barabási's chapter reads geometric and optimisation models as
  *generating* linear attachment ("such rational decisions can lead to
  preferential attachment", citing Papadopoulos and others' "Popularity
  versus similarity in growing networks") and says "To date all known
  models and real systems that are scale-free have been found to have
  preferential attachment" ([NOTE-2270](../notes.d/NOTE-2270.md), §§5.9, 5.11). The aside is
  about the rule a model is given; the chapter's claim is about the
  attachment a model produces. A contrast, not a refutation.

## What it does not say

- Not that any real system's heavy tail comes from cumulative advantage.
  A1 §5's domain table (citations, social networks, cities, wealth,
  platforms, language) lists plausible feedbacks, "but they don't all
  necessarily exhibit a pure power-law distribution". On cities, see the
  note of 2026-11-21 on [THEORY-1499](../theory.d/THEORY-1499.md), and [ARG-127](../arguments.d/ARG-127.md) for why the
  cities example does not support this claim.
- Not the opposition A later draws between rich-get-richer and
  criticality ([CLAIM-806](CLAIM-806.md)).

## Note of 2026-11-21: Mitzenmacher, read

Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md)) was read in full ([NOTE-2237](../notes.d/NOTE-2237.md);
the reading is [THEORY-2150](../theory.d/THEORY-2150.md)). It **corroborates** one clause and the
history, and does not carry the sentence it was cited beside.

- **Supports.** The feedback's lineage, Yule (1925), Simon (1955) and the
  Web-graph models (§3). Its model, a uniform link with probability α and
  a link by indegree otherwise, with a new page every step, gives
  c_j ∼ c·j^(−(2−α)/(1−α)): linear attachment with entry, a shifted
  kernel moving the exponent, which this claim's `defeated_if` already
  allows.
- **Does not support.** A3's "preferential attachment alone does not
  guarantee this result". The review never varies the kernel's exponent,
  never removes entry, and has no such sentence. Its α is a mixing
  probability, not the exponent of k^α. The kernel regimes in the claim's
  title are Krapivsky, Redner and Leyvraz's ([LIT-2974](../literature.d/LIT-2974.md), unread then, read on 2026-11-22) and the
  filing's simulations; the need for entry is [CLAIM-830](CLAIM-830.md)'s
  derivation.

So [LIT-3003](../literature.d/LIT-3003.md) leaves this claim's `grounds`, and [THEORY-2150](../theory.d/THEORY-2150.md)
`corroborates` it; [ARG-149](../arguments.d/ARG-149.md) gives the reasons. The claim's status is
unchanged.

## Note of 2026-11-22: Newman, read

Newman's review ([LIT-2976](../literature.d/LIT-2976.md), read in [NOTE-2261](../notes.d/NOTE-2261.md); the reading is [THEORY-2169](../theory.d/THEORY-2169.md)) **supports the linear-plus-entry half**. His Yule process founds a new
unit each step and attaches in proportion to k, or k + c, giving
α = 2 + (k0 + c)/m (§IV.D, pp. 17–19); Barabási and Albert's c = m gives
3, "but again there doesn't seem to be a good reason for this assumption"
(p. 19). It **leaves open** the sublinear and superlinear kernels.
[THEORY-2169](../theory.d/THEORY-2169.md) `corroborates` the claim.

## Note of 2026-11-22: Broido and Clauset, read

Broido and Clauset ([LIT-2963](../literature.d/LIT-2963.md), read in [NOTE-2263](../notes.d/NOTE-2263.md); the reading is [THEORY-2172](../theory.d/THEORY-2172.md)): **a parallel**. The claim's "Not that any real system's heavy tail
comes from cumulative advantage" agrees with the paper's "generally
limited role for any mechanism that necessarily produces power-law degree
distributions", and its "some variations of preferential attachment do
not produce power-law degree distributions" is the empirical side of the
claim's sublinear and superlinear cases. The paper keeps attachment for
citation networks. No edge. Status unchanged.

## Note of 2026-11-22: Krapivsky, Redner and Leyvraz, read

Krapivsky, Redner and Leyvraz ([LIT-2974](../literature.d/LIT-2974.md), read in [NOTE-2267](../notes.d/NOTE-2267.md); the
reading is [THEORY-2181](../theory.d/THEORY-2181.md)) **support the kernel half** and leave the
entry half open. The four regimes are theirs, derived exactly; the last
row is "winner take all", a single "gel" site, with a cascade of
transitions at γ = (m+1)/m. The power law is the borderline case and its
exponent is tunable, ν = 1 + μ/a∞. Their rate equation always has entry
("the continuous introduction of new sites"), so the need for entry rests
on [CLAIM-830](CLAIM-830.md). [THEORY-2181](../theory.d/THEORY-2181.md) replaces [LIT-2974](../literature.d/LIT-2974.md) in the grounds
([ARG-184](../arguments.d/ARG-184.md)), as [ARG-149](../arguments.d/ARG-149.md) expected. Their warning that for 0.8 ≲ γ ≲ 1 a
stretched exponential and a power law are hard to tell apart up to
k = 1000 bears on reading the claim off data, not on the model.

## Note of 2026-11-22: Barabási and Albert, and Barabási's chapter, read

Barabási and Albert ([LIT-3004](../literature.d/LIT-3004.md), [NOTE-2272](../notes.d/NOTE-2272.md), [THEORY-2180](../theory.d/THEORY-2180.md)) and the
chapter ([LIT-2968](../literature.d/LIT-2968.md), [NOTE-2270](../notes.d/NOTE-2270.md), [THEORY-2184](../theory.d/THEORY-2184.md)) **support** the base
case, the need for both ingredients and the kernel's linearity
([ARG-179](../arguments.d/ARG-179.md)); both replace the unread works in the grounds. Barabási
and Albert's "irrespective of the nature and the origin of this
visibility" supports "unequal outcomes need no unequal ability". The
chapter adds measured attachment exponents (α ≈ 1 for citations and the
Internet, 0.9 ± 0.1 for co-authorship and actors) and the rival framing
recorded under the aside on hyperbolic geometry.

## Note of 2026-11-22: Merton, read

Merton ([LIT-3002](../literature.d/LIT-3002.md), [NOTE-2268](../notes.d/NOTE-2268.md), [THEORY-2178](../theory.d/THEORY-2178.md)) **qualifies the naming
clause**, corrected in place above; it grounds the name only, which takes
no edge, and it leaves the grounds ([ARG-180](../arguments.d/ARG-180.md)). It leaves open
everything the claim asserts formally.

## Note of 2026-11-22: Reed and Hughes, read

Reed and Hughes ([LIT-3007](../literature.d/LIT-3007.md)), as read in this round by another filer:
**a parallel**. Yule's genera, killed pure-birth processes with new genera
entering, have entry built in, the claim's second ingredient in a
non-network setting. They never mention preferential attachment. No edge.

