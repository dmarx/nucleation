---
number: 923
status: Read
formerly:
- NOTE-tmpyzlig
paper: LIT-1103
title: 'Kleinberg — The small-world phenomenon: an algorithmic perspective'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Read in full from the author's own copy, linked from Kleinberg's Cornell publications
    page under the STOC 2000 citation (www.cs.cornell.edu/home/kleinber/swn.pdf,
    fetched 2026-10-15, saved here as swn.pdf). It is a 14-page single-column manuscript,
    not the ACM typeset proceedings (pp. 163–170), whose PDF at dl.acm.org returned
    403; Unpaywall and OpenAlex list only that ACM copy (bronze). Its first footnote
    says "A version of this work appears as Cornell Computer Science Technical Report
    99-1776 (October 1999)", so this copy is the full version that the STOC paper
    and the technical report share, and whether the 8-page STOC text differs in
    wording was not checked. The short Nature 2000 letter ("Navigation in a small
    world") is a different work and was not read. Text extracted with pdftotext
    -layout; the extraction garbles exponents and sums, so the statements of Theorems
    1, 2 and 3 were checked against the alt text of the formula images in the author's
    HTML rendering of the same paper (swn.d/swn.html on the same page). That rendering
    gives a different but equally valid constant λ in the proof of Theorem 3a ((2−r)2^(7−r)qp²
    against 2^(8−r)qp² in the PDF), so the two are not byte-identical versions;
    no theorem statement differs. Read: abstract, the introduction with the model
    and all statements, Section 2 (proof of Theorem 2), Section 3 (proofs of Theorem
    3a and 3b, Theorem 1 as the case r = 0), the conclusion and the references.
    Nothing skipped. Every quotation of the paper below was checked against the
    extracted text by script, with whitespace normalised; the phrases quoted from
    CLAIM-310 and from this LIT's filing, and the Nature letter's title, are not
    the paper's.
date: '2026-10-15'
summary: >-
  On an n × n lattice where each node also gets q long-range links drawn with probability
  proportional to d^(−r), short paths exist for r = 0, but no algorithm that sees
  only the links of nodes the message has visited finds them faster than about n^(2/3)
  steps in expectation. At r = 2 the greedy rule (pass to the contact nearest the
  target in lattice distance) delivers in O((log n)²) expected steps (proved for
  p = q = 1); for 0 ≤ r < 2 every such algorithm needs Ω(n^((2−r)/3)) and for r
  > 2 Ω(n^((r−2)/(r−1))). So efficient decentralized search depends on how the long-range
  links are distributed relative to the lattice, not on the links' existence or
  on the graph's diameter. The k-dimensional version (r = k) is stated without proof,
  and the model is a lattice with a known distance that every node can compute to
  the target.
---

# NOTE-923: Kleinberg — The small-world phenomenon: an algorithmic perspective

## Contribution

Milgram's experiment, the paper argues, shows two things: that short chains of acquaintances exist, and that people find them knowing little about the target. Earlier models (random graphs, Watts–Strogatz) explain the first. This paper asks the second question, "(∗∗) Why should arbitrary pairs of strangers be able to find short chains of acquaintances that link them together?", and notes that "one can imagine networks in which short chains exist, but no mechanism based on purely local information is able to find them." It defines a one-parameter family of lattice networks and decentralized algorithms, proves that the uniform (Watts–Strogatz) choice of long-range links defeats every decentralized algorithm, and proves that exactly one exponent of the link distribution, r = 2 on the two-dimensional lattice, permits delivery in polylogarithmic time.

## Key insight

A decentralized searcher makes progress only if its contacts carry information about the space it is searching. When long-range links are spread so that a node's links are about equally likely to land in each distance band 2^j to 2^(j+1) around it, then from any distance there is a fair chance, about 1/log n per step, of halving the remaining distance, and there are about log n halvings to make. The paper puts this as r = 2 being "the unique exponent at which a node’s long-range contacts are nearly uniformly distributed over all “distance scales.”" With r < 2 the links are biased toward far scales and rarely land near the target; with r > 2 they are biased toward near scales and the message cannot travel far per step. At r = 0 short paths are known to exist (the paper cites random-graph results; for r > 2 it says nothing about path length), so what is missing in the failing regimes is not routes but a gradient that local choices can follow.

## Assumptions

- **The network.** Nodes are the points of an n × n lattice with lattice (L1) distance d. Each node u has directed edges to every node within distance p (local contacts, p ≥ 1) and q directed long-range edges (q ≥ 0), each drawn independently with probability d(u, v)^(−r) / Σ_v d(u, v)^(−r), which the paper calls the inverse r-th-power distribution. p, q and r are constants independent of n.
- **The decentralized algorithm.** The message holder knows (i) the whole lattice of local contacts, (ii) the lattice position of the target t, and (iii) the locations and long-range contacts of all nodes the message has touched. "Crucially, u does not have knowledge of the long-range contacts of nodes that have not touched the message." The lower bounds are proved for a stronger model in which the algorithm may send the message to any contact of any node already reached, without counting backtracking steps. "our lower bounds will hold even for algorithms that are given this knowledge, while our upper bounds make use of decentralized algorithms that only require assumptions (i) and (ii)."
- **The measure.** Expected delivery time: the expected number of steps over the random network and a source and target drawn uniformly at random. All bounds are on this expectation, not on every pair or with high probability.
- **What each node can compute.** Every node can compute its contacts' lattice distance to the target. The lattice is the shared coordinate system that makes greedy routing possible at all.
- **Two dimensions in the proofs.** The k-dimensional lattice and "less structured graphs with analogous scaling properties" are claimed in the introduction and not proved in this paper.

## Key results

- **Theorem 1 (uniform links).** There is a constant α₀, depending on p and q but not on n, such that when r = 0 the expected delivery time of any decentralized algorithm is at least α₀ n^(2/3). The paper notes that for r = 0 "standard results from random graph theory" give paths of length polynomial in log n between every pair with high probability, so the bound is "exponential in the expected minimum path length." It is the case r = 0 of Theorem 3a.
- **Theorem 2 (inverse-square links).** There is a decentralized algorithm A and a constant α₂, independent of n, such that when r = 2 and p = q = 1 the expected delivery time of A is at most α₂ (log n)². A is greedy: each holder passes the message to the contact closest to t in lattice distance, and needs no memory of earlier holders. Proof: the normalizing sum is at most 4 ln(6n), so the chance of entering the ball of radius 2^j around t from distance at most 2^(j+1) is at least 1/(128 ln(6n)) per step; each of at most 1 + log n phases takes at most 128 ln(6n) expected steps. Only p = q = 1 is proved.
- **Theorem 3a (0 ≤ r < 2).** There is a constant α_r, depending on p, q and r, such that the expected delivery time of any decentralized algorithm is at least α_r n^((2−r)/3). Proof: within λn^δ steps, δ = (2−r)/3, the chance that any reached node has a long-range link into the ball of radius pn^δ around t is at most 1/4; source and target are at least n/4 apart with probability at least 1/2; so with probability at least 1/4 the message cannot arrive within λn^δ steps.
- **Theorem 3b (r > 2).** There is a constant α_r, depending on p, q and r, such that the expected delivery time of any decentralized algorithm is at least α_r n^((r−2)/(r−1)). Proof: with ε = r − 2 a link longer than m occurs with probability at most ε^(−1) m^(−ε); within λ′n^β steps, with β = ε/(1+ε) and γ = 1/(1+ε), no link longer than n^γ is likely, so the message covers at most λ′n < n/4 lattice distance.
- **The exponent profile.** The lower-bound exponent is (2−r)/3 for r < 2 and (r−2)/(r−1) for r > 2 (Figure 2); it is 0 only at r = 2 and approaches 1 as r grows. "r = 2 is the only value for which there is a decentralized algorithm capable of producing chains whose length is a polynomial in log n".
- **k dimensions (stated, not proved).** "In the k-dimensional case, a decentralized algorithm can construct paths of length polynomial in log n if and only if r = k."
- **Navigability is not diameter.** The paper names the minimum expected delivery time of any decentralized algorithm the network's "transmission rate" and observes that "minimizing the transmission rate of a network is not necessarily the same as minimizing its diameter."

## Bearing on the record

**On [CLAIM-310](../claims.d/CLAIM-310.md) (arrangements, not descriptions, do the work in retrieval).** The paper supports the owner's point in a precise form and narrows it in two ways.

- Supports: hold the node set, the lattice and the number of links per node fixed, and vary only how long-range links are distributed over distance. The cost of decentralized search changes from polylogarithmic (r = 2) to polynomial (any other r), while short paths exist at least at r = 0. What decides findability is how the links are arranged relative to the space the searcher can measure, which is [CLAIM-310](../claims.d/CLAIM-310.md)'s "as arrangements" half: a fact about the arrangement, not about what is arranged. The paper's own conclusion says "the correlation between local structure and long-range connections provides fundamental cues for finding paths through the network."
- Narrows: "only for one distribution" is true within this family (inverse power laws of lattice distance, constant p and q) and for polylog-time delivery. It does not say no other link structure is navigable; hierarchical and other constructions are outside the family. The exact exponent equals the lattice dimension only by the stated and unproved k-dimensional extension; the proof is for two dimensions, and Theorem 2 only for p = q = 1.
- Narrows: the arrangement works because every node can compute distance to the target in a shared coordinate system. The navigability is a joint property of the link distribution and that metric. [CLAIM-310](../claims.d/CLAIM-310.md)'s bins have no such metric between them; the analogy is to a collection whose items can be compared by a distance the searcher already knows.

**On [QUESTION-114](../questions.d/QUESTION-114.md) (sorting as amortized search).** It prices no organizing cost. The network is given, and the paper says nothing about the cost of building a navigable arrangement or keeping it current. What it adds is a lower bound showing that, for search with local information, an arrangement can make an existing short route impossible to find quickly, which is a cost of the wrong arrangement that no amount of path existence removes.

**On [CLAIM-309](../claims.d/CLAIM-309.md) (goodness vs discriminability).** No direct bearing. The only point of contact is the separation of an existential property (short paths exist; diameter) from an algorithmic one (a local searcher finds them), which is a separation of the same kind [CLAIM-309](../claims.d/CLAIM-309.md) draws, between a quantity and what an agent can use. It neither supports nor weakens that claim.

**On [THEORY-358](../theory.d/THEORY-358.md) (Treisman and Gelade search slopes).** A parallel in form, not in substance: in both, search cost moves from logarithmic or flat to polynomial or linear in the number of items depending on how the items are arranged relative to what the searcher can sense. The mechanisms are unrelated (graph routing with a known metric against attentional binding), and nothing in this paper bears on visual search.
