---
status: Proposed
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
- LIT-tmpx3y6w
- LIT-tmp5cw2k
- LIT-tmp959qu
- LIT-tmpwdtfj
- LIT-tmpw4ye0
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
  this session. The works are registered and unread. The wording is A's
  (the other assistant in the exchange "Rich Get Richer Power Laws", A1 and
  A3); adopting it is the owner's call.
---
<!-- inactive-ok-file: LIT-tmpx3y6w LIT-tmp5cw2k LIT-tmp959qu LIT-tmpwdtfj LIT-tmpw4ye0 — Deferred; the works A cites or invokes, registered from this exchange and not read -->
<!-- inactive-ok-file: CLAIM-tmply70l CLAIM-tmp9a83b CLAIM-tmp8h6nt CLAIM-184 CLAIM-677 THEORY-1927 THEORY-188 — Proposed or new; claims filed from the same exchange and held entries cited as neighbours -->
<!-- inactive-ok-file: ARG-tmp2w77g — new and Proposed or Rejected, filed from the exchange "Rich Get Richer Power Laws" on 2026-11-21 -->

# CLAIM-tmpepx9m: Cumulative advantage gives a power law only in a particular form: attachment linear in current size together with continual entry of new units; with no preference the tail is exponential, with sublinear preference stretched-exponential, and with superlinear preference one unit takes almost every new link

## The claim (A1, A3)

**One feedback, several names.** "The more you already have, the easier it
becomes to get more … this is called *preferential attachment* or
*cumulative advantage*", and "sometimes called the *Matthew effect*, after
sociologist Robert K. Merton" (A1 §1; [LIT-tmpw4ye0](../literature.d/LIT-tmpw4ye0.md)). A1 §7 separates three
things: "**Power law:** a statistical description … **Rich-get-richer:** a
dynamic mechanism … **Preferential attachment:** a mathematical
implementation of cumulative advantage."

**The base case** (A1 §3; Barabási and Albert, [LIT-tmpx3y6w](../literature.d/LIT-tmpx3y6w.md), and the
*Network Science* chapter, [LIT-tmp5cw2k](../literature.d/LIT-tmp5cw2k.md)). A new node links to node i with
probability k_i/Σk_j. Then dk_i/dt = k_i/2t, so k_i(t) ≈ (t/t_i)^(1/2).
Uniform birth times give P(K ≥ k) ∝ k^(−2) and P(K = k) ∝ k^(−3).

**Both ingredients are needed** (A3 §1): "preferential attachment alone
does not guarantee this result. The combination of growth, the form of
attachment, and other model assumptions determines the distribution." And
"unequal outcomes can arise without unequal innate abilities", though
"observed success can reflect a mixture of quality, luck, timing, and
cumulative advantage". A3 cites Mitzenmacher's review ([LIT-tmpwdtfj](../literature.d/LIT-tmpwdtfj.md)). A3's
Alice and Bob make the point that under linear attachment the leader
gains more in absolute terms and not in percentage terms.

**The form of the kernel matters** (A1 §4). With P(i) ∝ k_i^α: α = 0
gives "Exponential-type", 0 < α < 1 "Stretched-exponential tail", α = 1
"Power-law", α > 1 "Strong concentration; potentially winner-take-all". A
does not name the source. It is Krapivsky, Redner and Leyvraz
([LIT-tmp959qu](../literature.d/LIT-tmp959qu.md)). Hence "**having cumulative advantage is not enough to
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
  which gives a spread of ages. [CLAIM-tmply70l](CLAIM-tmply70l.md) works this out. It is the
  "growth" half of A3's "growth plus attachment".
- **The test for attachment** that A proposes (A3 §5, does a node with
  twice the degree get twice the new links?) is taken up in
  [CLAIM-tmp8h6nt](CLAIM-tmp8h6nt.md), with its confound.
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
  note of 2026-11-21 on [THEORY-1499](../theory.d/THEORY-1499.md), and [ARG-tmp2w77g](../arguments.d/ARG-tmp2w77g.md) for why the
  cities example does not support this claim.
- Not the opposition A later draws between rich-get-richer and
  criticality ([CLAIM-tmp9a83b](CLAIM-tmp9a83b.md)).
