---
status: Active
status_note: 'read 2026-10-09 ([NOTE-tmpsmtp6](../notes.d/NOTE-tmpsmtp6.md)); worth reading as the formal version of "preserve the distribution over interpretations, not one meaning": the semantic distortion compares the posterior of the meaning S given the original observation with its posterior given the reconstruction, alongside an ordinary distortion on the symbols, and the paper proves the coding theorem for the resulting rate–distortion function and solves a binary case. Read it knowing three things the paper does not say. With Kullback–Leibler divergence its expected semantic distortion is exactly I(S;X) − I(S;Y), so its function is the information bottleneck; with total variation it bounds the extra Bayes risk of every bounded-loss decision about S. Its sequence distortion is defined as a maximum inside the expectation, while both proofs use the maximum of per-letter expectations, so the theorems hold for the latter. And its MNIST experiment trains with a classifier''s cross-entropy against the true label, not with the posterior distortion the theory defines.'
title: 'Semantic Rate-Distortion Theory with Applications'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmpsmtp6) from arXiv v1 (12
    September 2025, the only version, 34 pages), including Appendices
    A–D with every proof followed. Identified from the exchange's cite
    marker (turn688832academia39 resolves to arXiv 2509.10061, "Semantic
    Rate-Distortion Theory with Applications", 12 September 2025): it is
    the "Zhao et al., 2025" of CLAIM-tmpp8j04. Details checked against
    arXiv (six authors: Yi-Qun Zhao, Zhi-Ming Ma, Geoffrey Ye Li, Shuai
    Yuan, Tong Ye, Chuan Zhou; no journal reference). A Crossref title
    search found no published version (OpenAlex was over its rate limit
    and was not checked). `published:` is the
    arXiv v1 date. Not held in the Anthology of the SOTA: a grep of its
    record/ (clone of 2026-10-09, commit d8b5ba5) for the title, the
    identifier and the authors found nothing.
tags:
- information-theory
date: '2026-10-09'
published: '2025-09-12'
arxiv: '2509.10061'
first_author: 'Zhao'
keywords:
- 'semantic communication'
- 'semantic rate-distortion'
- 'conditional semantic probability distortion'
- 'rate-distortion-perception'
- 'ambiguity'
- 'polysemy'
implementations: []
summary: >-
  Zhao, Ma, Li, Yuan, Ye & Zhou (2025), arXiv. Defines semantic
  distortion as a divergence between the posteriors of a latent meaning S
  given the original and the reconstructed observation, proves that the
  information rate–distortion function under this and a symbolic
  constraint is the operational limit (given lower semicontinuity), and
  solves the doubly symmetric binary case with total variation and
  Hamming distortion. With KL divergence the function is the information
  bottleneck, which the paper does not note.
---

<!-- inactive-ok-file: THEORY-156 — Proposed; cited for the comparison of experiments the TV bound relates to -->
<!-- inactive-ok-file: THEORY-tmp3ijnj — Proposed; filed from this reading, under test -->

# LIT-tmp2w545: Semantic Rate-Distortion Theory with Applications

Yi-Qun Zhao, Zhi-Ming Ma, Geoffrey Ye Li, Shuai Yuan, Tong Ye and Chuan
Zhou (2025), *arXiv preprint* —
[ARXIV-2509.10061](https://arxiv.org/abs/2509.10061)

## Key takeaways

- **The model** (Section 2). A message is a pair (s, x): s the intrinsic
  meaning, relative to a task known to both ends, x the observable string.
  Coding acts on x only; the decoder outputs a reconstructed observation
  y. Since one string can support several readings ("orange", "several
  days"), what should survive is the conditional distribution p(S|x), not
  a single most probable meaning.
- **The distortion** (Definitions 1–8). Semantic distortion
  d_p(p_S|x, p_S|y), for any divergence (total variation and KL are
  named), where p_S|y is the posterior of S given the reconstruction under
  the joint law the code induces (S–X–Y Markov); and an ordinary symbolic
  distortion d_o(x, y). R^I(D_p, D_o) = min I(X; Y) subject to both
  expected distortions.
- **The theorems** (Section 3). The information function is achievable,
  by a Poisson functional representation code with common randomness
  (Theorem 1), and is the operational limit when it is lower
  semicontinuous (Theorem 2), which holds for finite alphabets and bounded
  or f-divergence distortions (Proposition 2).
- **Binary case** (Theorem 3). For S, X, Y binary, X a symmetric channel
  of S with crossover q, d_p = TV, d_o = Hamming: R = 1 − h₂((1 −
  √(1 − 2D_p/C))/2) when the semantic constraint binds (D_p ≤ a(D_o)),
  and the classical 1 − h₂(min(D_o, ½)) otherwise, with C = |1 − 2q|.
  Whichever constraint is tighter sets the rate.
- **Illustration** (Section 5). MNIST autoencoders trained on MSE plus γ
  times a classifier's cross-entropy reach far higher digit accuracy at
  the same bit budget (at 4 bits, 95% with γ = 0.1 against 15% with
  γ = 0).

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request. It is the "Zhao et
al., 2025" the exchange named as close to its interest in "preserving
distributions over interpretations rather than one purported intrinsic
meaning" ([CLAIM-tmpp8j04](../claims.d/CLAIM-tmpp8j04.md)); the manuscript did not keep it. It is read here
on its own merits. See the curation entry of that day.

The reading confirms the exchange's description: the constraint is on
posterior distributions over meanings, which is the preservation of
interpretations the manuscript wanted. It also finds that the KL version
of that constraint is the information bottleneck ([LIT-338](LIT-338.md)), so the idea is
older than this paper, and that the total-variation version is a
decision-relative fidelity in the sense of the record's account of
comparing experiments ([THEORY-156](../theory.d/THEORY-156.md)). Both are stated, with their scope, in
[THEORY-tmp3ijnj](../theory.d/THEORY-tmp3ijnj.md), sourced here. It cites Chai et al. ([LIT-tmpfnpwq](LIT-tmpfnpwq.md)) among
the rate–distortion–perception works it builds on.
