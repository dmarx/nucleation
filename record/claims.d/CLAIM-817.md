---
number: 817
status: Proposed
formerly:
- CLAIM-tmpepx9m
title: 'Cumulative advantage gives a power law only in a particular form: attachment linear in current size together with continual entry of new units; with no preference the tail is exponential, with sublinear preference stretched-exponential, and with superlinear preference one unit takes almost every new link'
version: 1
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
- LIT-3004
- LIT-2968
- LIT-2974
- LIT-3002
summary: >-
  A's, from A1 §1 to §4 and §7 and A3 §1 of the exchange "Rich Get Richer
  Power Laws" (2026-11-20), answering the owner's U1 and U2. Rich-get-richer,
  cumulative advantage, the Matthew effect and preferential attachment
  name one feedback. In the Barabási–Albert model, growth plus linear
  attachment gives P(K = k) ∝ k^(−3). The generalized kernel k^α gives an
  exponential, a stretched-exponential, a power-law or a winner-take-all
  degree distribution (Krapivsky, Redner and Leyvraz, unnamed by A). So
  "having cumulative advantage is not enough to guarantee a power law",
  and unequal outcomes need no unequal ability. Checked by simulation in
  this session. The works are registered and unread, but for Mitzenmacher's
  review, read on 2026-11-21 (see the dated note). The wording is A's
  (the other assistant in the exchange "Rich Get Richer Power Laws", A1 and
  A3); adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-tmp6jdas THEORY-tmpw4qgu THEORY-tmphcnj3 — Proposed; the readings of 2026-11-22 cited in the notes -->
<!-- inactive-ok-file: LIT-3004 LIT-2968 LIT-2974 LIT-3002 — Deferred; the works A cites or invokes, registered from this exchange and not read -->
<!-- inactive-ok-file: CLAIM-830 CLAIM-806 CLAIM-803 CLAIM-184 CLAIM-677 THEORY-1927 THEORY-188 — Proposed or new; claims filed from the same exchange and held entries cited as neighbours -->
<!-- inactive-ok-file: ARG-127 ARG-149 THEORY-2150 — new and Proposed or Rejected, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->

# CLAIM-817: Cumulative advantage gives a power law only in a particular form: attachment linear in current size together with continual entry of new units; with no preference the tail is exponential, with sublinear preference stretched-exponential, and with superlinear preference one unit takes almost every new link

## The claim (A1, A3)

**One feedback, several names.** "The more you already have, the easier it
becomes to get more … this is called *preferential attachment* or
*cumulative advantage*", and "sometimes called the *Matthew effect*, after
sociologist Robert K. Merton" (A1 §1; [LIT-3002](../literature.d/LIT-3002.md)). A1 §7 separates three
things: "**Power law:** a statistical description … **Rich-get-richer:** a
dynamic mechanism … **Preferential attachment:** a mathematical
implementation of cumulative advantage."

**The base case** (A1 §3; Barabási and Albert, [LIT-3004](../literature.d/LIT-3004.md), and the
*Network Science* chapter, [LIT-2968](../literature.d/LIT-2968.md)). A new node links to node i with
probability k_i/Σk_j. Then dk_i/dt = k_i/2t, so k_i(t) ≈ (t/t_i)^(1/2).
Uniform birth times give P(K ≥ k) ∝ k^(−2) and P(K = k) ∝ k^(−3).

**Both ingredients are needed** (A3 §1): "preferential attachment alone
does not guarantee this result. The combination of growth, the form of
attachment, and other model assumptions determines the distribution." And
"unequal outcomes can arise without unequal innate abilities", though
"observed success can reflect a mixture of quality, luck, timing, and
cumulative advantage". A3 cites Mitzenmacher's review ([LIT-3003](../literature.d/LIT-3003.md)) here;
read, the review does not say this (corrected 2026-11-21: see the note of
that date below). A3's
Alice and Bob make the point that under linear attachment the leader
gains more in absolute terms and not in percentage terms.

**The form of the kernel matters** (A1 §4). With P(i) ∝ k_i^α: α = 0
gives "Exponential-type", 0 < α < 1 "Stretched-exponential tail", α = 1
"Power-law", α > 1 "Strong concentration; potentially winner-take-all". A
does not name the source. It is Krapivsky, Redner and Leyvraz
([LIT-2974](../literature.d/LIT-2974.md)). Hence "**having cumulative advantage is not enough to
guarantee a power law**."

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
node links to all but finitely many). This is unread here, but the runs
agree.

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
  ([THEORY-188](../theory.d/THEORY-188.md)), needs no attachment at all.

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
  title are Krapivsky, Redner and Leyvraz's ([LIT-2974](../literature.d/LIT-2974.md), unread) and the
  filing's simulations; the need for entry is [CLAIM-830](CLAIM-830.md)'s
  derivation.

So [LIT-3003](../literature.d/LIT-3003.md) leaves this claim's `grounds`, and [THEORY-2150](../theory.d/THEORY-2150.md)
`corroborates` it; [ARG-149](../arguments.d/ARG-149.md) gives the reasons. The claim's status is
unchanged.

## Note of 2026-11-22: Newman, read

Newman's review (LIT-2976, read in NOTE-tmpa7yd2; the reading is THEORY-tmp6jdas) **supports the linear-plus-entry half**. His Yule process founds a new
unit each step and attaches in proportion to k, or k + c, giving
α = 2 + (k0 + c)/m (§IV.D, pp. 17–19); Barabási and Albert's c = m gives
3, "but again there doesn't seem to be a good reason for this assumption"
(p. 19). It **leaves open** the sublinear and superlinear kernels.
THEORY-tmp6jdas `corroborates` the claim.

## Note of 2026-11-22: Broido and Clauset, read

Broido and Clauset (LIT-2963, read in NOTE-tmpleyjh; the reading is THEORY-tmphcnj3): **a parallel**. The claim's "Not that any real system's heavy tail
comes from cumulative advantage" agrees with the paper's "generally
limited role for any mechanism that necessarily produces power-law degree
distributions", and its "some variations of preferential attachment do
not produce power-law degree distributions" is the empirical side of the
claim's sublinear and superlinear cases. The paper keeps attachment for
citation networks. No edge. Status unchanged.
