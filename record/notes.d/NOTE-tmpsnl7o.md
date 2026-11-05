---
status: Skimmed
paper: 'LIT-tmptozb9'
title: 'Chou, Chua, Teo and Zheng — Efficiency of the long chain and sparse structure'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Skimmed on 2026-11-04, as the stand-in for Jordan and Graves (1995),
    LIT-tmpaku09, at the owner's request. Copy:
    https://web2-bschool.nus.edu.sg/wp-content/uploads/media_rp/publications/RGhEC1392617919.pdf,
    the publisher's typeset PDF on NUS Business School's publications page,
    distributed by INFORMS as a courtesy to the authors, 16 pages, extracted
    with pdftotext (the PDF's ligature glyphs restored in the text matched).
    Read: the abstract, §1 Introduction (pp. 43–45), §2 Literature Review
    (pp. 45–46), the opening of §3 and the statements of Theorems 1 and 2
    (pp. 46–49), §5 numerical study (pp. 55–57), §6 Conclusion (pp. 57–58)
    and the endnotes. Skipped: the derivations in §3 (the random-walk
    analysis, Lemma 1, Corollary 1), all of §4 on general demand and supply
    (Theorem 3, Corollary 2, the sampling proof), and the references. Page
    numbers are the journal's.
date: '2026-11-04'
summary: >-
  Analytical support for Jordan and Graves's chaining principle. Plants and
  products form a bipartite graph, and sales once demand is known are a
  max-flow. For balanced, identical systems with independent demand, the
  long chain keeps at least 89% (uniform) and 96% (normal) of full
  flexibility's expected sales as the system grows; in general a suitably
  sampled sparse structure comes within ε of full flexibility; with
  correlated demand a sparse structure can serve almost none of it.
---
<!-- inactive-ok-file: LIT-tmpaku09 THEORY-tmpgeseh THEORY-144 — Unfetched or Proposed; the unread original this work stands in for, the account filed from this reading, and a held account named as unrelated, cited as open -->

# NOTE-tmpsnl7o: Chou, Chua, Teo and Zheng — Efficiency of the long chain and sparse structure

## Contribution

Jordan and Graves found by simulation that a few well-placed flexibility
links do nearly as well as full flexibility; there were, in this paper's
words, "relatively few concrete analytical results" (abstract, p. 43). It
supplies some: the exact asymptotic efficiency of the long chain in
balanced, independent systems, and conditions under which a sparse
structure is nearly as good as full flexibility in general ones.

## Key insight

Flexibility pays off through the links that let unmet demand at one
product be served from spare capacity elsewhere, and a single chain
through all plants and products already gives almost all such routes:
adding more links buys little, unless demands move together.

## Assumptions

- A single period; demand is observed before production is allocated;
  unmet demand is lost; one unit of capacity makes one unit of any product
  the plant is linked to (§3).
- For the chain results: balanced capacity and i.i.d. demand symmetric
  about its mean (§3). §4 relaxes this, but was not read.

## Key results

- **Jordan and Graves, as reported** (§2, p. 45): "The landmark study was
  by Jordan and Graves (1995), who introduced the concepts of smart limited
  flexibility and chaining. They observe, through extensive simulation,
  that limited flexibility, configured the right way, yields most of the
  benefits (in terms of expected sales) of full flexibility."
- **Chaining** (p. 46): "every facility can produce two products and every
  product can be produced by two facilities", all linked in one chain; in a
  10×10 example "chaining achieves about 95% of the" benefits of full
  flexibility. In their second part "they propose a measure (later called
  the JG index)".
- **The long chain asymptotically** (§1, pp. 44–45): with normal demand of
  mean 100 and standard deviation 33, "the chaining system can still
  accrue close to 97% of the" expected sales of full flexibility as n → ∞;
  for uniform and normal demand it reaps "at least 89% and 96%,
  respectively". Theorem 2 gives the asymptotic chaining efficiency in
  closed form through solutions of linear systems (p. 49).
- **Correlated demand** (§1, p. 44): "If demands are correlated, the
  situation can be very different"; in the authors' extreme example a
  sparse structure with O(n) arcs serves only O(1) of n units of expected
  demand.
- **Open** (§6, p. 57): estimating expected max-flow in an arbitrary random
  bipartite network is "already an open problem".

## Concepts

- **Process flexibility**, after Jordan and Graves and after Sethi and
  Sethi: "a firm's ability to provide varying goods or services, using
  different facilities or resources" (p. 43).
- **Dedicated, chaining and full-flexibility systems**: one link per
  plant, the long chain (2-chain), and every plant linked to every product
  (p. 44; endnote 1).
- **Asymptotic chaining efficiency (ACE)**: the limit, as n → ∞, of the
  chain's expected sales as a share of full flexibility's (§3).

## Connections

Registered as the stand-in for Jordan and Graves (1995), [LIT-tmpaku09](../literature.d/LIT-tmpaku09.md),
whose copies could not be fetched. Of that paper's results it restates, in
attributed paraphrase: that Jordan and Graves introduced limited
flexibility and chaining; that by extensive simulation limited flexibility
configured right yields most of full flexibility's expected-sales benefit;
that chaining is the configuration, each plant making two products and
each product made at two plants; the figure of about 95% in a 10×10
example; and that they proposed a flexibility measure, the JG index. It
reuses their 16-plant data (§5, p. 55).

It does not restate Jordan and Graves's guidelines in their own words, the
definition or computation of the JG index, their simulation design or
demand model, their cost discussion, or their automotive data beyond the
16-plant numbers. It adds what Jordan and Graves did not have: an
analytical confirmation for balanced, independent demand, and the failure
case under correlation.

A second neighbour, Chen, Ma, Zhang and Zhou (arXiv:1806.02894), restates
Jordan and Graves only as the bipartite max-flow model and was set aside.
[LIT-1155](../literature.d/LIT-1155.md) (Linial, London and Rabinovich, the geometry of graphs) is
adjacent in method, through max-flow and expansion.

## Bearing on the record

- **[CLAIM-347](../claims.d/CLAIM-347.md)** (frustration among demands as an ordinal fact: the jointly
  satisfiable sets form a complex, and relief is its enlargement):
  qualifies, with a real structural echo. Adding plant–product links
  enlarges the set of demand realisations that can be met together, and
  the long chain is a cheap enlargement close to the full complex. This
  literature measures the enlargement in expected sales, not ordinally,
  and its correlated-demand example shows how much the measure depends on
  which realisations are likely.
- **[CLAIM-520](../claims.d/CLAIM-520.md)** (the value of a maintained capacity is conditional on cost
  and use): supports in kind. Full flexibility is costly, so the sparse
  design that keeps most of its value is preferred (p. 44).
- **[TERM-055](../terms.d/TERM-055.md)** (operational availability): weak. Fulfilled demand is
  capacity actually deployable to a product under realised demand, but
  nothing here concerns cues or deadlines.
- **[THEORY-144](../theory.d/THEORY-144.md)** (redundant defences erode unobserved): unrelated in
  mechanism.
- **A's characterization of Jordan and Graves**, a mathematical study of
  limited flexibility under variable demand: right that it concerns limited
  flexibility under variable demand; wrong on "mathematical", since this
  paper says Jordan and Graves worked "through extensive simulation" and
  that analytical results came later. A leaves out the principle itself
  and the correlation caveat. The flexibility here is standing capacity to
  re-route work, not a capability kept for rare events; the nearer analogue
  is cross-trained staff, which the paper mentions (p. 43).
- No instruction for machine-learning practice.

## Limitations

- The authors': balanced, i.i.d. symmetric demand for the chain results; a
  single period; lost sales; expected max-flow in general is an open
  problem (§6).
- This reading's: the proofs and §4 were skipped, and Jordan and Graves
  are known here only through this paper's report.

## Open questions

Whether Jordan and Graves state their principle as this paper reports it,
and how they define the JG index, needs [LIT-tmpaku09](../literature.d/LIT-tmpaku09.md) read from the MIT
working paper.
