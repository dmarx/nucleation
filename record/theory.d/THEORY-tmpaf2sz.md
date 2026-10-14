---
status: Proposed
promote_when: >-
  A comparison on networks with known ground-truth groups, large enough
  and many enough to fit the relation between how delineated the
  structure is and how well tangle communities match it, with an
  uncertainty, and repeated under a second vertex-assignment rule. It is
  promoted if the match tracks delineation under both rules and trivial
  tangles persist; it fails if a better assignment rule or higher orders
  make tangle communities match weakly structured networks as well as the
  standard methods do. What cannot settle it: more single networks
  inspected by eye, or tangle theory, which says what tangles are and not
  how they compare with communities.
title: "Tangle-defined cohesion matches network communities only where community structure is strongly delineated, and tangles of one to three vertices recur beside the ones that do"
version: 1
tags:
- network-science
- mathematics
- individuation
date: '2026-10-14'
source:
- LIT-955
summary: >-
  Salter-Duke (2024), [LIT-955](../literature.d/LIT-955.md), a PhD thesis read in full in
  [NOTE-tmpv7vus](../notes.d/NOTE-tmpv7vus.md). Edge-connectivity tangles, computed exactly at low order
  on eleven small real networks, give communities close to standard
  methods where structure is strong (yeast PPI) and none or almost none
  where it is weak (karate club, C. elegans, college football at the
  orders reached), and where tangles divide a network some hold only
  one to three vertices. The relation is read by eye from eight networks, and the
  vertex sets depend on the author's assignment rule.
---
<!-- inactive-ok-file: CLAIM-157 THEORY-tmpjvv0j — Proposed; the block answer and the companion reading's theory this bears on, open -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; cited as the permissiveness objection, not as standing -->

# THEORY-tmpaf2sz: Tangle-defined cohesion matches network communities only where community structure is strongly delineated, and tangles of one to three vertices recur beside the ones that do

## Source

Salter-Duke (2024), [LIT-955](../literature.d/LIT-955.md), PhD thesis, Te Herenga Waka—Victoria
University of Wellington, read in full in [NOTE-tmpv7vus](../notes.d/NOTE-tmpv7vus.md): Chapter 2
(definitions), Chapter 3 (algorithm and lemmas), Chapter 4 (community
detection, §§4.4.1–4.4.3 and Fig. 4.31), Chapter 5 (images), Chapter 6.

## What was actually shown

An edge-connectivity tangle of order k orients every cut of weight < k
towards one side, so that no three small sides cover the graph and no big
side is a single vertex. The author computed all such tangles, at the
lowest orders that finished in under a day, on eleven real networks of
23 to 281 vertices, turned each tangle into a vertex set (vertices on the
big side of every distinguishing separation, inheriting from lower
orders), and compared the result with standard community methods by NMI
and ARI.

- **Weak or diffuse structure.** Karate club, C. elegans neurons and
  college football have one tangle per order at every order reached, so
  no communities. B. subtilis PPI, jazz musicians and David Copperfield
  word pairs are left "largely undifferentiated", with similarity
  "extremely low" against the reference comparison of Infomap with
  Louvain.
- **Strong structure.** On yeast PPI component A the order-2 tangle
  communities match edge-betweenness except for two one-vertex
  communities, with scores near the reference.
- **The summary.** Across eight networks, similarity to Infomap rises as
  the map-equation length falls, and similarity to Louvain rises as
  modularity rises (Fig. 4.31); lower orders match better.
- **Trivial tangles.** A vertex of degree ≥ θ, cut off by cuts of order
  < θ, is a tangle of order θ (§4.4.2); groups of one to three vertices
  appear "often" at the periphery. In images, pairs of corner pixels form
  tangles while one-pixel-wide lines cannot form one (§5.4).

What could have come out the other way: tangle communities could have
matched one standard definition across all networks, or matched weakly
structured networks as well as strongly structured ones. The author had
hoped for the first and found neither.

## What this does not say

- **That tangles are wrong about cohesion.** They are a precise notion,
  and the thesis tests its fit to how communities are used, not its
  coherence. Tangle–tree duality still makes the verdict exact for each
  order.
- **That the trend holds at higher orders or larger graphs.** Only low
  orders on small graphs were computable, and the author says the trend
  "may only apply" there.
- **That the vertex sets are the tangles.** A tangle is a set of oriented
  cuts. The communities depend on the assignment rule, which the author
  chose and calls one option among several.
- **That the relation is measured.** Eight points per panel, sized by
  order, with no fitted relation or uncertainty.

## Connections

- **[QUESTION-035](../questions.d/QUESTION-035.md).** Tangles are a candidate test of the "where does its
  boundary lie" clause: one system means inseparable inside, and
  separable outside, by cuts below an order k. The thesis shows the
  verdict depends on k region by region, that it needs a further rule to
  give a boundary as a vertex set, and that it passes single high-degree
  vertices. That last is [CLAIM-010](../claims.d/CLAIM-010.md)'s permissiveness at the low end. No
  `answers:` is declared: this tests a criterion and reports its failure
  modes; it does not answer the question.
- **[CLAIM-157](../claims.d/CLAIM-157.md).** The same shape, strength inside against strength across,
  with a threshold. The finding that each region has its own best order
  says a single global threshold will split some forms and miss others;
  [CLAIM-157](../claims.d/CLAIM-157.md) sets its threshold per block, by the Occam factor, which is
  the kind of setting the thesis lacked. No relation is declared, as
  neither rests on the other.
- **[THEORY-tmpjvv0j](THEORY-tmpjvv0j.md).** On a connectome, misinformative macro transitions
  fall mostly between communities; here, tangles see communities only
  where the between-community cuts are cheap. Both locate the trouble at
  weak boundaries, by different measures. No relation is declared.
