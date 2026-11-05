---
status: Active
status_note: >-
  skimmed 2026-11-05 ([NOTE-tmpec4ov](../notes.d/NOTE-tmpec4ov.md)) from arXiv v2: definitions, theorem
  statements, the easy side (§4.1–4.2) and the open problems in full, the
  proofs of the hard side and of Lemmas 4.8–4.13 skimmed, the SIAM version
  not compared; worth reading as the first worst-case classification of
  how hard it is to navigate a solution space, across Boolean constraint
  languages: for a "tight" language st-connectivity under single-variable
  flips is in P and components have linear diameter, otherwise it is
  PSPACE-complete and diameter can be exponential. The boundary properly
  contains Schaefer's tractable classes and, by the authors' account,
  cuts across Boolean clones, so finding and navigating come apart in both
  directions. Its main limits: Boolean domain, constants allowed and
  single-flip moves only; and the boundary is slightly wrong, since
  repeated variables in constraints were not considered, as Schwerdtfeger
  (2014), [LIT-tmp48lyf](LIT-tmp48lyf.md), shows and corrects.
title: 'The Connectivity of Boolean Satisfiability: Computational and Structural Dichotomies'
version: 1
history:
- version: 1
  date: '2026-11-05'
  note: >-
    Registered and read on 2026-11-05 in the filing of the owner's pasted
    synthesis on resource-bounded realizability, written by another
    assistant (A) and pasted by the owner on 2026-11-04. A does not cite
    this work. The lead added it, as a reading of an open question A
    raises: whether the algebra of a constraint language could predict the
    complexity of navigating its solution space. Citation checked by the
    reader against Crossref and the arXiv record: Parikshit Gopalan,
    Phokion G. Kolaitis, Elitza Maneva and Christos H. Papadimitriou, SIAM
    Journal on Computing 38(6): 2330–2355 (online 2009-03-04); extended
    abstract at ICALP 2006 (doi:10.1007/11786986_31). The arXiv version,
    cs/0609072, v1 of 2006-09-13, is the earliest exact date the reader
    found and is `published:` (ADR-002). The lead's citation was right. Not
    held before (no hit for the arXiv id, the DOIs or the title). Copy: the
    arXiv PDF, https://arxiv.org/pdf/cs/0609072, v2 of 2007-10-03, 23
    pages, extracted with pdftotext. Schwerdtfeger's correction is filed
    as LIT-tmp48lyf.
tags:
- mathematics
- operations-research
date: '2026-11-05'
published: '2006-09-13'
arxiv: 'cs/0609072'
doi: '10.1137/07070440x'
first_author: 'Gopalan'
keywords:
- 'Boolean satisfiability'
- 'computational complexity'
- 'PSPACE-completeness'
- 'dichotomy theorems'
- 'graph connectivity'
implementations: []
summary: >-
  Gopalan, Kolaitis, Maneva & Papadimitriou (2009). The solutions of a
  Boolean CNF(S)-formula, constants allowed, induce a subgraph of the
  hypercube, adjacent solutions differing in one variable. For a finite set
  S of relations: if S is tight (all componentwise bijunctive, all OR-free
  or all NAND-free), st-connectivity is in P, connectivity in coNP and
  component diameter linear; otherwise both are PSPACE-complete and
  diameter can be 2^Ω(√n). Tight sets properly contain Schaefer's
  tractable sets, so positive 1-in-3 SAT is NP-complete to satisfy but easy
  to navigate, while NAE-3SAT is hard for both. The hard side rests on
  faithful expressibility; the authors conjecture a trichotomy for
  connectivity.
---
<!-- inactive-ok-file: NOTE-tmpec4ov THEORY-tmpmcxbv CLAIM-tmp9jvpb — Skimmed, Proposed or new; the reading, the account filed from it and a claim it bears on, cited from the reading of Gopalan et al. (2009) as open -->

# LIT-tmpxpw0i: The Connectivity of Boolean Satisfiability: Computational and Structural Dichotomies

Gopalan, P., Kolaitis, P. G., Maneva, E. & Papadimitriou, C. H. (2009). The Connectivity of Boolean Satisfiability: Computational and Structural Dichotomies. *SIAM Journal on Computing* 38(6): 2330–2355. doi:10.1137/07070440x. arXiv:cs/0609072.

## Key takeaways

*From the reading, [NOTE-tmpec4ov](../notes.d/NOTE-tmpec4ov.md). Theorem numbers are arXiv v2's.*

- **st-connectivity** (Theorem 2.9): if S is tight, ST-CONN(S) is in P;
  otherwise it is PSPACE-complete.
- **Connectivity** (Theorem 2.8): if S is tight, CONN(S) is in coNP;
  otherwise it is PSPACE-complete; coNP-complete when tight and not
  Schaefer.
- **Diameter** (Theorem 2.10, abstract): linear for tight sets, possibly
  exponential otherwise; "small diameter and tractability of the
  st-connectivity problem are remarkably aligned."
- **Not the clone method** (§1): "This method, however, does not appear to
  apply to connectivity, as the boundaries discovered here cut across
  Boolean clones."
- **Both directions** (§2): positive 1-in-3 SAT is tight, "but not
  Schaefer": NP-complete to satisfy, st-connectivity in P; positive
  NAE-3SAT is not tight, and both connectivity problems are
  PSPACE-complete.
- **Corrected** by Schwerdtfeger (2014), [LIT-tmp48lyf](LIT-tmp48lyf.md): repeated variables
  in constraints move the boundary slightly toward the hard side, from
  tight to "safely tight".

## Standing in the record

The lead's addition, not A's. A asks, in the pasted synthesis on
resource-bounded realizability, whether the algebra of a constraint
language could predict the complexity of navigating its solution space.
This paper answers in part, for Boolean languages with constants and
single-flip moves: yes, the language fixes navigation complexity as a
dichotomy, but not through the polymorphism clone A names as the
algebraic component, since the boundary cuts across clones. Polymorphisms
predict one direction only: every Schaefer-easy language is also easy to
navigate (Lemma 4.1). Finding and navigating come apart in both
directions, 1-in-3 SAT against NAE-3SAT, which is A's point that
compatibility equivalence does not imply computational equivalence, made
exact. It bears on [CLAIM-347](../claims.d/CLAIM-347.md), [CLAIM-tmp9jvpb](../claims.d/CLAIM-tmp9jvpb.md) and [QUESTION-tmp5bi3h](../questions.d/QUESTION-tmp5bi3h.md).
Non-Boolean domains, other move sets and resource budgets are left open.
Filed from it: [THEORY-tmpmcxbv](../theory.d/THEORY-tmpmcxbv.md). No instruction for machine-learning
practice.
