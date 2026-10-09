---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmp5zbie); worth reading as a short statement of semantic communication as indirect (remote) source coding with a perception constraint: the encoder sees only a noisy observation X of the semantic source S, the decoder must reproduce S within an expected distortion and within a total-variation distance of S''s distribution, and side information Y may help. It gives a rate region, a closed form for a doubly symmetric binary source, and an MNIST illustration. Read it knowing that it is a six-page workshop paper whose proofs are sketched or omitted, that the region as printed mixes channel and source terms and does not define the reconstruction, and that its "zero-rate recovery" is the familiar fact that a decoder with side information needs no bits once the tolerated distortion is what the side information alone achieves.'
title: 'Rate-Distortion-Perception Theory for Semantic Communication'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmp5zbie) from arXiv v1 (9 December
    2023, the only version, 6 pages), including both appendices.
    Identified from the exchange's cite marker (turn688832academia37
    resolves to arXiv 2312.05437, "Rate-Distortion-Perception Theory for
    Semantic Communication"): it is the "Chai et al." of CLAIM-tmpp8j04.
    Details checked against arXiv (four authors: Jingxuan Chai, Yong
    Xiao, Guangming Shi, Walid Saad; comment: accepted at the IEEE ICNP
    workshop, Reykjavik, 10–13 October 2023) and Crossref (2023 IEEE 31st
    International Conference on Network Protocols (ICNP), pp. 1–6, DOI
    10.1109/ICNP59255.2023.10355575, dated 10 October 2023, the first day
    of the conference). `published:` is the arXiv v1 date, per ADR-002's
    arXiv rule; the workshop presentation came first. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-09,
    commit d8b5ba5) for the title, the identifiers and the authors found
    nothing.
tags:
- information-theory
date: '2026-10-09'
published: '2023-12-09'
arxiv: '2312.05437'
first_author: 'Chai'
keywords:
- 'semantic communication'
- 'rate-distortion-perception'
- 'indirect source coding'
- 'side information'
- 'common randomness'
implementations: []
summary: >-
  Chai, Xiao, Shi & Saad (2023), IEEE ICNP 2023 workshop. Models a
  semantic source S seen by the encoder only through X, with Wyner–Ziv
  side information and common randomness, and states the rate needed to
  reproduce S within an expected distortion and a total-variation bound
  on its distribution. Closed form for a doubly symmetric binary source:
  recovering X exactly does not recover S, and with side information the
  rate reaches zero at a non-trivial distortion. Proofs sketched.
---

<!-- inactive-ok-file: THEORY-tmp3ijnj — Proposed; filed from the readings of this batch, under test -->

# LIT-tmpfnpwq: Rate-Distortion-Perception Theory for Semantic Communication

Jingxuan Chai, Yong Xiao, Guangming Shi and Walid Saad (2023), *2023 IEEE
31st International Conference on Network Protocols (ICNP)*, workshop —
[ARXIV-2312.05437](https://arxiv.org/abs/2312.05437)

## Key takeaways

- **The model** (Section III). A semantic source S, i.i.d.; the encoder
  sees k indirect observations X drawn through p(X|S); encoder and decoder
  may hold Wyner–Ziv side information (Y′, Y″) and share common
  randomness U; the decoder outputs Ŝ. Two constraints: expected
  distortion E d(Sⁿ, Ŝⁿ) ≤ D, and a perception constraint, the total
  variation between the laws of S and Ŝ, either per block ("strong") or
  on expectations ("empirical").
- **The region** (Definition 3, Theorem 1). Rate R ≥ I(X; Z|Y), with
  I(S, X; Z|Y) ≤ (k/m) I(M; M̂) for the channel, Z depending on X only;
  claimed achievable and tight, by a strong-functional-representation
  code. The proof is a sketch.
- **Binary case** (Theorem 2). For a doubly symmetric binary pair with
  crossover q, the distortion on S is linear in the distortion on X,
  d(S, Ŝ) = (1 − 2q) d(X, Ŝ) + q, so reproducing the observation exactly
  still leaves distortion q on the semantic source (Observation 3); and
  when the tolerated distortion reaches the level achievable from the
  side information, the rate is zero (Observation 5).
- **Illustration** (Section V). On MNIST with additive noise, a learned
  encoder and decoder trained on MSE plus a Wasserstein penalty: side
  information at the decoder lowers the rate at given distortion and
  perception, and indirect observation raises it.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request. It is the "Chai et
al." the exchange named when it conceded that task-sensitive information
preservation is established in semantic communication (CLAIM-tmpp8j04);
the manuscript did not keep it. It is read here on its own merits. See the
curation entry of that day.

The reading supports the concession in a specific form: preserving a
hidden variable S rather than the observation, with decoder side
information and a distributional constraint, is formalised here. What is
preserved is a single latent variable and its marginal law, not a family
of decisions or a distribution over interpretations. Zhao et al.
(LIT-tmp2w545) cite it and move the constraint to the posterior p(S|·).
With the survey (LIT-tmpmigxa) it is a source of THEORY-tmp3ijnj.
