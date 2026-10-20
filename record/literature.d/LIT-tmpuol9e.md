---
status: Active
status_note: >-
  read 2026-10-20 (NOTE-tmpnodc1) in full, from the published version in the University of Hertfordshire Research Archive; worth reading for the single-letter definition of successive refinement for the information bottleneck and its equivalent forms (Proposition 1: some pair of optimal encoders forms the Markov chain X → T₂ → T₁; Proposition 8: the coarse encoder is a Blackwell garbling of the fine one); for the convex-hull test (Proposition 4: with an injective fine decoder, refinement holds iff every decoder point q(X|t₁) lies in the convex hull of the q(X|t₂)), checkable by a linear programme; for proofs of refinability when X and Y are both binary, when Y is a function of X, and for jointly Gaussian variables (the last resting on Kline and Palmer's semigroup result); and for soft refinement measured by unique information. Read it knowing that the linear programme tests the particular optima a solver returns, so that a failed test certifies nothing unless the optima are globally optimal and unique, which the paper leaves as Conjecture 1 and calls its own figures "mere numerical proxies" (Appendix D); that its evidence that refinement fails is therefore numerical and uncertified, with no count of how many sampled distributions failed; that the unique information computed is an upper bound on the soft measure for the same reason; that the deep-learning reading of §4.2 is speculative; and that the commentary on Proposition 8 swaps its points (ii) and (iii).
title: 'Exact and Soft Successive Refinement of the Information Bottleneck'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Registered on 2026-10-20 as the lead named by the reading of No, Ingber and Weissman (NOTE-tmpmscti) for the stochastic half of QUESTION-tmpproc1: a linear-programming test for exact refinability of the information bottleneck. Citation from Crossref and the article itself: Charvin, H., Catenacci Volpi, N. & Polani, D., Entropy 25(9):1355, doi:10.3390/e25091355 (PMID 37761653, PMC10528077). The article gives received 25 July 2023, revised 8 September 2023, accepted 13 September 2023, published 19 September 2023. Crossref's published-online and issued dates are also 19 September 2023, and its `created` date (19 September 2023) is a deposit date and is not used. `published:` is 19 September 2023, the publisher's online date, per ADR-002. No arXiv version was found: the arXiv API was searched by author (Charvin; Charvin and Polani) and by the title phrases "soft successive refinement" and "successive refinement" with "bottleneck", and it returned the authors' other papers only. Not held in this record or in the Anthology of the SOTA: a grep of both record/ trees (the anthology clone at commit d1573d2) for "Charvin", "successive refin", the DOI and the PMC id found nothing. Flagged anthology-candidate because §4.2 reads the result as a statement about the layers of deep networks, which the anthology's representation-and-encoding topic could hold; the paper's subject is information theory.
- version: 2
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmpnodc1) from the published PDF in the University of Hertfordshire Research Archive (eprint 10690, 51 pages). The MDPI PDF and the PMC and Europe PMC PDFs returned access-denied or challenge pages to this client; the PMC HTML page was reachable but not needed. Status Deferred → Active. The reading re-derived Propositions 1, 3, 4 and 5 (filed as THEORY-tmpeu1u4 and THEORY-tmpkusod), and ran the paper's test on CLAIM-tmphan8l's four-state source with optima certified globally optimal and unique by a convex-envelope check: the optima at β = 8 and β = 12 are not refinable. That result is the record's, not the paper's.
tags:
- information-theory
- learning-theory
- anthology-candidate
date: '2026-10-20'
published: '2023-09-19'
doi: '10.3390/e25091355'
url: 'https://uhra.herts.ac.uk/id/eprint/10690/1/entropy-25-01355.pdf'
first_author: 'Charvin'
keywords:
- 'information bottleneck'
- 'successive refinement'
- 'unique information'
- 'incremental learning'
- 'coarse-graining'
- 'Blackwell order'
- 'deep learning'
implementations:
- 'https://gitlab.com/uh-adapsys/successive-refinement-ib/'
summary: >-
  Charvin, Catenacci Volpi & Polani (Entropy 2023). Defines successive refinement for the information bottleneck in single-letter form: a coarse optimum T₁ can be extended to a fine optimum (T₁, S). This holds iff some pair of optima forms the chain X → T₂ → T₁, iff the coarse encoder is a garbling of the fine one, and, when the fine decoder is injective, iff the coarse decoder points lie in the convex hull of the fine ones. That last form gives a linear-programming test. Refinability is proved for binary X and Y, for Y a function of X, and (from a cited semigroup result) for jointly Gaussian variables. Numerically, for 3×3 and larger random sources, the hull test on computed optima often fails, especially below the second bifurcation. The loss, measured by unique information, stayed under 5.4% of I(X; T₁, T₂). The failures are not certified, since global optimality and uniqueness of the optima are left as a conjecture.
---

# LIT-tmpuol9e: Exact and Soft Successive Refinement of the Information Bottleneck

Charvin, H., Catenacci Volpi, N. & Polani, D. (2023). Exact and Soft Successive Refinement of the Information Bottleneck. *Entropy* 25(9): 1355. doi:10.3390/e25091355. Open access (CC BY), also PMC10528077.

Read in full in NOTE-tmpnodc1, from the copy in the University of Hertfordshire Research Archive.

## Why this is here

Named by NOTE-tmpmscti as the direct reading for the stochastic half of
QUESTION-tmpproc1: when are the information-bottleneck optima at two budgets
nested, X → Z₂ → Z₁? The paper supplies the exact criterion and a test for it,
and proves nesting for three special cases. Its own evidence that nesting
fails in general is numerical and uncertified. The reading certified one
failure on the record's four-state example (NOTE-tmpnodc1), and THEORY-tmpeu1u4
and THEORY-tmpkusod hold what the paper proves.
