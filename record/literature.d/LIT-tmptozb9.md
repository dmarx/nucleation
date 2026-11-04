---
status: Active
status_note: >-
  read in part 2026-11-04 (NOTE-tmpsnl7o, Skimmed) from the INFORMS
  author-courtesy PDF on NUS Business School's site; worth reading as the
  analytical backing for the chaining principle of process flexibility:
  for balanced, identical plants and products with independent demand, the
  long chain keeps at least 89% (uniform demand) and about 96% (normal
  demand) of full flexibility's expected sales as the system grows, and in
  general a suitably sampled sparse structure comes within ε of full
  flexibility, while with correlated demand a sparse structure can lose
  almost everything. Registered as the stand-in for Jordan and Graves
  (1995), LIT-tmpaku09, whose simulation findings it reports. Its main
  limits: a single period, lost sales, and the chain results only for
  balanced, independent, symmetric demand.
title: 'Design for Process Flexibility: Efficiency of the Long Chain and Sparse Structure'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Registered and read on 2026-11-04 as a stand-in for Jordan and Graves
    (1995), LIT-tmpaku09, whose copies could not be fetched, at the owner's
    request; that paper is cited in the pasted bibliography on emergency
    readiness, written by another assistant (A) and pasted by the owner on
    2026-11-04, which does not cite this one. Citation checked against
    Crossref (10.1287/opre.1080.0664): Mabel C. Chou, Geoffrey A. Chua,
    Chung-Piaw Teo and Huan Zheng, Operations Research 58(1), 43–58,
    journal article. Crossref gives the print issue only (2010-02); the
    PDF says it was published online in Articles in Advance on 30 March
    2009, which is `published:`. Not held before (no hit for the DOI, the
    title or "Chou, Chua"). Copy:
    https://web2-bschool.nus.edu.sg/wp-content/uploads/media_rp/publications/RGhEC1392617919.pdf,
    the publisher's typeset PDF on the publications page of NUS Business
    School, the institution of Chou and Teo, stamped as distributed by
    INFORMS as a courtesy to the authors; 16 pages, extracted with
    pdftotext. A second neighbour, Chen, Ma, Zhang and Zhou,
    arXiv:1806.02894, was opened (abstract and §1) and set aside: it
    restates Jordan and Graves only as the bipartite max-flow model.
tags:
- operations-research
- probabilistic-modeling
date: '2026-11-04'
published: '2009-03-30'
doi: '10.1287/opre.1080.0664'
first_author: 'Chou'
keywords:
- 'process flexibility'
- 'long chain'
- 'sparse structure'
- 'random walk'
- 'max-flow'
implementations: []
summary: >-
  Chou, Chua, Teo & Zheng (2010). Plants and products form a bipartite
  graph and sales, once demand is realised, are a max-flow. For balanced,
  identical systems with independent demand symmetric about its mean, a
  generalised random walk gives the long chain's efficiency as the system
  grows: at least 89% of full flexibility's expected sales for uniform
  demand, about 96% for normal. For general systems, a sparse structure
  sampled with suitable probabilities comes within ε of full flexibility;
  with correlated demand a sparse structure can serve almost none of it.
  The paper gives analytical support to the chaining principle that Jordan
  and Graves found by simulation, and reuses their 16-plant data.
---
<!-- inactive-ok-file: NOTE-tmpsnl7o THEORY-tmpgeseh LIT-tmpaku09 — Skimmed, Proposed or Unfetched, and new; the reading of this work, the account filed from it, and the unread original it stands in for, cited as open -->

# LIT-tmptozb9: Design for Process Flexibility: Efficiency of the Long Chain and Sparse Structure

Chou, M. C., Chua, G. A., Teo, C.-P. & Zheng, H. (2010). Design for Process Flexibility: Efficiency of the Long Chain and Sparse Structure. *Operations Research* 58(1): 43–58. doi:10.1287/opre.1080.0664.

## Key takeaways

*From the reading, NOTE-tmpsnl7o. Page numbers are the journal's.*

- **Jordan and Graves, as reported** (§2, p. 45): "They observe, through
  extensive simulation, that limited flexibility, configured the right way,
  yields most of the benefits (in terms of expected sales) of full
  flexibility."
- **The long chain, analytically** (§1, p. 45): chaining reaps "at least
  89% and 96%, respectively" of full flexibility's benefit for uniform and
  normal demand, even as the number of plants grows without bound.
- **The caveat** (§1, p. 44): "If demands are correlated, the situation
  can be very different"; in the authors' extreme example an O(n)-arc
  sparse structure serves only O(1) of n units of expected demand.
- **Still open** (§6, p. 57): estimating expected max-flow in an arbitrary
  random bipartite network is "already an open problem".

## Standing in the record

Registered as the stand-in for Jordan and Graves (1995), LIT-tmpaku09,
which the pasted bibliography on emergency readiness cites and whose
copies could not be fetched. It reports that paper's headline findings in
paraphrase and reuses its data, but does not give its guidelines,
flexibility index or simulation design. Filed from it: THEORY-tmpgeseh.
Flexibility here is standing capacity to re-route work under realised
demand, not a capability kept for rare events; its nearest echo in the
record is CLAIM-347, where adding links enlarges the set of demands that
can be met together.
