---
status: Active
status_note: >-
  read in full 2026-10-15 (NOTE for LIT-tmp7dffg) from the author's own copy on
  Kleinberg's Cornell page (www.cs.cornell.edu/home/kleinber/swn.pdf), a 14-page manuscript
  linked there under the STOC 2000 citation and footnoted as the version that is
  also Cornell CS Technical Report 99-1776; the ACM typeset proceedings (pp. 163–170)
  returned 403, and the Nature 2000 letter is a different work, not read. Worth
  reading as the source of the result that a network can have short paths that no
  searcher using local information can find: on an n × n lattice with long-range
  links drawn with probability proportional to d^(−r), greedy routing delivers in
  O((log n)²) expected steps at r = 2 (proved for one local and one long-range contact
  per node), every decentralized algorithm needs Ω(n^((2−r)/3)) steps for 0 ≤ r
  < 2 and Ω(n^((r−2)/(r−1))) for r > 2, and r = k in k dimensions is stated without
  proof. For [CLAIM-310](../claims.d/CLAIM-310.md) it shows that findability, with nodes, lattice and link count
  fixed, turns on how the links are arranged relative to a distance every node can
  compute, which supports the claim's "as arrangements" half; it narrows "only one
  distribution" to this family of inverse power laws and to polylogarithmic delivery,
  and it prices no cost of building the arrangement, so it adds nothing to [QUESTION-114](../questions.d/QUESTION-114.md)'s
  organizing cost.
title: 'The Small-World Phenomenon: An Algorithmic Perspective'
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed, not read. Citation checked on 2026-10-15: STOC 2000. Crossref gives May
    2000 only, so `published:` is the first of the month. Not held in the Anthology
    of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2) for
    the title and authors found nothing. Read the same day (NOTE-tmpyzlig).
tags:
- network-science
- information-retrieval
- mathematics
date: '2026-10-15'
published: '2000-05-01'
doi: 10.1145/335305.335325
first_author: Kleinberg
keywords: []
implementations: []
summary: >-
  Kleinberg (2000), STOC 2000. On an n × n lattice where each node also gets q long-range
  links drawn with probability proportional to d^(−r), short paths exist for r =
  0, but no algorithm that sees only the links of nodes the message has visited
  finds them faster than about n^(2/3) steps in expectation. At r = 2 the greedy
  rule (pass to the contact nearest the target in lattice distance) delivers in
  O((log n)²) expected steps (proved for p = q = 1); for 0 ≤ r < 2 every such algorithm
  needs Ω(n^((2−r)/3)) and for r > 2 Ω(n^((r−2)/(r−1))). So efficient decentralized
  search depends on how the long-range links are distributed relative to the lattice,
  not on the links' existence or on the graph's diameter. The k-dimensional version
  (r = k) is stated without proof, and the model is a lattice with a known distance
  that every node can compute to the target.
---

# LIT-tmp7dffg: The Small-World Phenomenon: An Algorithmic Perspective

Kleinberg, J. (2000). The small-world phenomenon: an algorithmic perspective. In *Proc. STOC 2000*, pp. 163–170. DOI 10.1145/335305.335325

## Key takeaways

Read in full ([NOTE-tmpyzlig](../notes.d/NOTE-tmpyzlig.md)). On an n × n lattice where each node also gets q long-range links drawn with probability proportional to d^(−r), short paths exist for r = 0, but no algorithm that sees only the links of nodes the message has visited finds them faster than about n^(2/3) steps in expectation. At r = 2 the greedy rule (pass to the contact nearest the target in lattice distance) delivers in O((log n)²) expected steps (proved for p = q = 1); for 0 ≤ r < 2 every such algorithm needs Ω(n^((2−r)/3)) and for r > 2 Ω(n^((r−2)/(r−1))). So efficient decentralized search depends on how the long-range links are distributed relative to the lattice, not on the links' existence or on the graph's diameter. The k-dimensional version (r = k) is stated without proof, and the model is a lattice with a known distance that every node can compute to the target.

## Why this is here

[CLAIM-310](../claims.d/CLAIM-310.md) (arrangements, not descriptions): within a family of inverse-power-law long-range links on a lattice, greedy routing finds short paths only at one exponent, so navigability depends on the arrangement of links. It also needs every node to compute its distance to the target in shared coordinates, and the proofs are for two dimensions.
