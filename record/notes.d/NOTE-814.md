---
number: 814
status: Read
formerly:
- NOTE-tmpv7vus
paper: LIT-955
title: 'Salter-Duke — Tangled webs'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the thesis PDF (189 pages) in the Victoria
    University of Wellington open-access repository, fetched through its
    Figshare file service (ndownloader.figshare.com/files/45559989) after
    the repository's own download link returned an empty 202 response;
    text extracted with pdftotext -layout. Read: abstract, Chapters 1–6
    in full, including every definition, lemma, corollary and proof in
    Chapters 2 and 3 and the sketched proof on lines in Chapter 5, the
    glossary and the bibliography. Appendix A (timing plots) was read from
    its headings and the Chapter 3 summary only. Figures were read from
    their captions and the surrounding prose, except Figure 4.31 (the
    summary of all networks), which was rendered and inspected. The
    individual metric values in the per-network plots were not read off.
date: '2026-10-14'
summary: >-
  An exact but exponential algorithm finds edge-connectivity tangles in
  graphs of up to about 200 vertices. On eleven small real networks,
  tangle communities resemble those of standard methods only where
  community structure is strongly delineated; three networks have no
  distinguishable tangles at the orders reached, and where tangles do
  distinguish regions, some hold only one to three vertices. On images, lines one pixel wide cannot
  be distinguished. The author concludes the tangle notion of cohesion
  "is not as compelling as I had hoped".
---
<!-- inactive-ok-file: THEORY-254 — Proposed; the theory filed from this reading -->
<!-- inactive-ok-file: CLAIM-157 CLAIM-172 — Proposed; the answer and entrainment mark this reading bears on, open -->
<!-- inactive-ok-file: CLAIM-010 — Rejected; cited as the permissiveness objection, not as standing -->

# NOTE-814: Salter-Duke — Tangled webs

## Contribution

The thesis implements a complete algorithm for edge-connectivity tangles,
which had been studied almost only in theory, and tests the claim that
tangles capture cohesive regions on two applied tasks. The algorithm
enumerates cuts in non-decreasing order (Vazirani–Yannakakis) and orients
them into tangles with a branching search, cut down by four proved
reductions. The empirical result is mostly negative: tangles find
strongly delineated communities and some objects, but the set of all
tangles is a poor partition of a network or an image.

## Key insight

A tangle defines a cohesive region by its relation to the whole graph,
not by its members: it is a consistent way of pointing every cut of order
below k at one side. "A region must be inseparable internally by cuts of
a given order, while being separable from the rest of the network by cuts
of that order." That is a strict, two-sided criterion. Where the network
has no such region at the orders computed, a tangle reports one
undifferentiated whole; where it does, tangles also report tiny regions
(single high-degree vertices, pairs of pixels in a corner) that pass the
same test.

## Assumptions

- **Edge-connectivity tangles only**: separations are bipartitions of the
  vertex set, the order is the (weighted) number of cut edges. Graphs are
  simple, undirected and connected (the giant component is taken).
- **The tangle axioms** for order k: (T1) exactly one orientation of each
  separation of order < k; (T2) no three small sides cover the vertex
  set; (T3) no big side is a single vertex.
- **Vertex assignment** is the author's rule, not part of tangle theory:
  a vertex belongs to a tangle's community if it lies on the big side of
  every *distinguishing* separation; vertices unassigned at an order
  inherit their community from a lower order.
- **Images** are grid graphs with edge weight δ(uv) = N − 1 − |π(u) − π(v)|
  for greyscale resolution N, departing from Diestel and Whittle so that
  a black-on-white boundary costs zero.
- **Scale**: networks up to about 280 vertices, images of a few hundred
  pixels, and only the lowest orders that finished in under a day.

## Key results

- **Lemma 2.2.1 and 2.2.2 (cited, proved for Lemma 2.2.1).** In a tangle
  of order θ, a separation whose small side lies inside a small side is
  also oriented the same way; the union of two small sides is small if
  its order is below θ.
- **Tangle–tree duality (cited, Diestel and Oum).** For each k a graph has
  either a carving of width < k or an edge-connectivity tangle of order
  k, not both. The number of distinguishable tangles is at most |V|, and
  they can be told apart by a linear number of nested separations.
- **Corollary 3.3.1 (proved).** A set built by repeatedly uniting small
  sides, with every partial union of order < k, is small.
- **Lemmas 3.3.1–3.3.2 (proved).** A side that is a hanging tree, or a
  forest, with all vertex degrees below k, must be the small side in any
  tangle of order k; so is a side of one vertex, or of two vertices of
  degree < k.
- **Lemmas 3.3.3–3.3.4 (proved).** Leaves isolated on one side of a
  separation can be treated as interchangeable without changing which
  orientations satisfy the axioms. (Lemma 3.3.4's statement says the
  violation is of "(T3)"; from the proof it is (T2).)
- **Cost.** Up to O(n^{3(k − x_min) − 1}) separations of order < k and
  O(|S_{x+1}| · 2^{|S_{x+1}|}) for orienting them; graphs over 200
  vertices ran "in reasonable time, taking less than a day".
- **No distinguishable tangles (§4.4.1).** Karate club (orders 2–10),
  C. elegans neurons (2–14) and college football (8–24) have one tangle
  per order, so no communities, though standard methods find structure in
  all three.
- **Largely undifferentiated (§4.4.2).** B. subtilis PPI, jazz musicians
  and David Copperfield word pairs: a few peripheral tangles, the bulk
  undivided; similarity to every method "extremely low" against the
  Infomap–Louvain reference.
- **Strong structure (§4.4.2).** On yeast PPI component A, order-2 tangle
  communities match edge-betweenness except for two single-vertex
  communities, and scores are near the reference; similarity falls as
  order rises. A tangle of order θ can be a single vertex of degree ≥ θ.
- **An order per region.** In the dolphin network the main group is
  distinguished only at order 7 and broken into trivial pieces at 9: "Each
  region within the network seems to have an optimum tangle order".
- **The summary (§4.4.3, Fig. 4.31).** Across eight networks, similarity
  of tangle communities to Infomap rises as the map-equation value falls,
  and to Louvain as modularity rises; lower orders score higher. No
  statistic is fitted. "Tangles do seem to correspond to
  strongly-delineated communities, but for the community structure over
  the whole graph, the way in which tangles define cohesiveness is not the
  most suitable."
- **Lines in images (§5.4, sketched proof).** In three-shade greyscale a
  one-pixel-wide straight line is not distinguished by any tangle, except
  a line spanning the whole image (for λ(A)/2 < k ≤ λ(A)) or a length-2
  line in a corner (k = 4); the argument is that any enclosing set has
  boundary at least λ(A), and a tree side with small degrees is small.
  Width-2 lines fail too except at a boundary, corner or full height.
- **Colour resolution (§5.5).** At 3 shades one tangle picks out the Mona
  Lisa's eye; at 32 shades the first tangle has order 60 and the first
  distinguishing tangle order 89; at 256 none is found in 25 orders, since
  the range of cut weights spreads the separations thin.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An exact algorithm finds all edge-connectivity tangles of low order on graphs of a few hundred vertices | strong | Ch. 3, Lemmas 3.3.1–3.3.4, validated against hand-computed examples |
| C2 | Tangle communities resemble standard communities where community structure is strong, and not otherwise | moderate | eight networks, Fig. 4.31, no fitted statistic |
| C3 | On networks with weaker structure, low-order tangles leave the network undivided | moderate | five of eleven networks, §§4.4.1–4.4.2 |
| C4 | Where tangles distinguish regions, some pick out only one to three vertices | moderate | yeast, dolphins and others; the single-vertex case explained in §4.4.2 |
| C5 | Each region has its own best tangle order | weak | dolphins, zebras, Iceland; observation |
| C6 | Lines one pixel wide cannot be distinguished by tangles, with stated exceptions | moderate | sketched proof with cases omitted, §5.4 |
| C7 | Higher colour resolution pushes meaningful tangles beyond computable orders | moderate | one image, six resolutions, §5.5 |

## Method

Pre-process (collapse hanging trees to stubs), find the minimum cut
(Stoer–Wagner), enumerate cuts order by order (Vazirani–Yannakakis, which
outran Yeh–Wang–Su in the author's implementation), and grow a binary
tree of orientations, pruning any branch where three small sides cover
the vertex set. Pre-decide orientations by Lemma 3.3.2 and treat isolated
leaves as interchangeable. Assign vertices to communities by
distinguishing separations and compare with the standard disjoint methods by NMI
and ARI, and with clique percolation by overlapping NMI and the Omega
index.

## Concepts

- **Separation** — an unordered bipartition {A, B} of the vertex set; its
  **order** λ is the weight of the edges between A and B.
- **Tangle of order k** — a set of oriented separations, one per
  separation of order < k, satisfying (T1)–(T3); it "points to" a region
  without listing it.
- **Small side / big side** — the side a tangle orients away from and
  towards; "not based on the size of the component".
- **Distinguishing separation** — one oriented differently by two
  tangles.
- **Tangle community** — the author's vertex set for a tangle: the
  vertices on the big side of every distinguishing separation, with
  inheritance from lower orders.

## Connections

Tangles come from Robertson and Seymour's graph minors (X, 1991); the
abstract theory, tangle–tree duality and profiles are Diestel's
programme, and the image proposal is Diestel and Whittle's "Tangles and
the Mona Lisa". Grohe and Schweitzer's oracle algorithms are discussed
and not implemented. The community methods compared are modularity
(Newman and Girvan, Louvain, leading eigenvector, fast-greedy, exact
ILP), Potts models (Leiden, spinglass, label propagation), random walks
(Infomap, Walktrap), edge-betweenness and clique percolation.

## Bearing on the record

- **[LIT-955](../literature.d/LIT-955.md)'s seed claim needs correcting.** It files the thesis as "a
  rival criterion for when a combined form is one system and where its
  boundary lies". The thesis tests that criterion and finds it wanting in
  practice. Tangles find strongly delineated regions, but at low order they
  leave weakly structured networks undivided, where they do divide they
  also admit single vertices and pairs, and in images they cannot see thin
  shapes. A tangle also does not give a boundary by itself: it is a set of
  oriented cuts, and turning it into a vertex set needs an assignment
  rule, which the author supplies and admits is a choice.
- **[QUESTION-035](../questions.d/QUESTION-035.md) (one system and its boundary).** What the reading
  contributes is the shape of the criterion. "Cannot be pulled apart" is
  made two-sided and relative to an order k: inseparable inside by cuts
  below k, separable outside by cuts below k. Tangle–tree duality makes
  the verdict exact for each k: a tangle exists or a decomposition of
  width < k does. So the order plays the role of the record's threshold,
  and the thesis finds the verdict changes with it region by region. A
  single vertex of degree ≥ k passes, which is the permissiveness worry
  ([CLAIM-010](../claims.d/CLAIM-010.md)) at the low end.
- **[CLAIM-157](../claims.d/CLAIM-157.md) (block and threshold).** Both criteria compare strength
  inside with strength across an edge, and both need a threshold (τ
  there, k here). The thesis's finding, that each region has its own best
  order, says one global threshold will split some forms and miss others.
  [CLAIM-157](../claims.d/CLAIM-157.md) sets its threshold per block by the Occam factor, which is the
  kind of per-region setting the thesis lacked.
- **[CLAIM-172](../claims.d/CLAIM-172.md).** No bearing: tangles are static and see no timing.
- **New THEORY.** [THEORY-254](../theory.d/THEORY-254.md) holds the empirical finding. The
  duality and the lemmas are standard or technical and are not filed.
- No instruction for machine-learning practice. Community detection and
  image segmentation are applied, but nothing here tells anyone what to
  do; nothing for the anthology.

## Limitations

- Small networks and small images only; the author warns the trends "may
  only apply to the small networks and lower order tangles that could be
  calculated".
- Eight networks in the summary plot, with no fitted relation or
  uncertainty; the trend is read by eye.
- The vertex-assignment rule, with inheritance, shapes every comparison;
  a different rule could change the scores, though the author argues the
  trivial tangles exist whatever the rule.
- The line result is sketched, with cases "depend[ing] on whether the line
  touches the boundary" omitted.
- Table 4.1 lists the zebra network as 62 vertices and 159 edges, the
  same as the dolphins; §4.4.2 gives 23 vertices and 105 edges.

## Open questions

- Is there a principled way to choose the order region by region, rather
  than inspecting each?
- Would vertex-connectivity tangles, or profiles, behave differently on
  the same networks?
- Does the tangle–tree decomposition (a linear number of distinguishing
  separations) give a usable algorithm without enumerating all cuts?
