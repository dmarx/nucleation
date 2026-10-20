---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpmscti](../notes.d/NOTE-tmpmscti.md)) in full, from arXiv:1506.03407v2; worth reading for successive refinement at second order (source dispersion): a sufficient condition, Corollary 6, that a source refinable at (D₁, D₂) throughout a neighbourhood of its law is also refinable with both dispersion terms, so that discrete sources under Hamming distortion and the Gaussian under squared error lose nothing even at √n precision; and for layered codes, which use a growing number L_n of refinement stages to trade encoding complexity against rate, with every stage on the rate–distortion curve. Read it knowing that it says nothing about logarithmic loss or the information bottleneck, though [NOTE-tmpyi9oi](../notes.d/NOTE-tmpyi9oi.md) recalled it as the source of a log-loss result (that result is No and Weissman, ISIT 2015, and No, Entropy 2019, and concerns direct log-loss, not the bottleneck's remote one); that its sufficient condition asks for refinability in a whole neighbourhood of the source, not at the source alone; that the layered-code results cover only binary-Hamming and Gaussian-quadratic sources; and that the abstract's "O(n^{log n}) algorithm" is an encoding search over codebooks shown to exist, not constructed, with the bound holding as stated only when the rate is below one nat.
title: 'Strong Successive Refinability and Rate-Distortion-Complexity Tradeoff'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Registered on 2026-10-20 as a follow-up named by the reading of Equitz and Cover (NOTE-tmpyi9oi), which recalled it as showing that every discrete memoryless source is successively refinable under logarithmic loss. Citation from the arXiv API and Crossref: arXiv:1506.03407, v1 submitted 10 June 2015 (v2 15 March 2016); published as IEEE Transactions on Information Theory 62(6):3618–3635, June 2016, doi:10.1109/TIT.2016.2549540 (Crossref gives month only for print and issue; its `created` date, 1 April 2016, is a deposit date and is not used). `published:` is the arXiv v1 date, the earliest full date, per ADR-002. The paper says it was "presented in part" at Allerton 2013 (doi:10.1109/ALLERTON.2013.6736709, "Complexity and rate-distortion tradeoff via successive refinement", October 2013) and ISIT 2014 (doi:10.1109/ISIT.2014.6875316, "Strong successive refinability: Sufficient conditions", June 2014). Those are partial precursors under their own titles, with month precision only, and are not taken as this work's first appearance, as LIT-tmp25otd did for its workshop abstract; the coordinator may rule otherwise under ADR-002's earlier-date rule. Not held in this record or in the Anthology of the SOTA: a grep of both record/ trees (the anthology clone at commit d1573d2) for the arXiv id, "Ingber", "Strong Successive" and "successive refin" found nothing.
- version: 2
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmpmscti) from arXiv:1506.03407v2. Status Deferred → Active. The reading finds that the paper does not treat logarithmic loss anywhere, so the attribution that prompted the registration was wrong; the log-loss result is No and Weissman, "Universality of logarithmic loss in lossy compression" (ISIT 2015, doi:10.1109/ISIT.2015.7282839, arXiv:1709.00134), and No, "Universality of Logarithmic Loss in Successive Refinement" (Entropy 21(2):158, 2019, doi:10.3390/e21020158), identified from their abstracts and not read. The summary is written from the reading.
tags:
- information-theory
- mathematics
date: '2026-10-20'
published: '2015-06-10'
arxiv: '1506.03407'
doi: '10.1109/TIT.2016.2549540'
first_author: 'No'
keywords:
- 'successive refinement'
- 'source dispersion'
- 'strong successive refinability'
- 'layered codes'
- 'rate-distortion-complexity tradeoff'
implementations: []
summary: >-
  No, Ingber & Weissman (2015; IEEE TIT 2016). Asks whether successive refinement loses anything at second order, the √n dispersion term, as well as at first. For finite alphabets it gives an achievable rate pair with dispersions (Theorem 5), from which a source is strongly successively refinable if every law in a neighbourhood of it is successively refinable at (D₁, D₂) (Corollary 6). Discrete sources under Hamming distortion and the Gaussian under squared error qualify. It then uses many refinement stages as a complexity device: with L_n stages the encoder searches L_n small codebooks instead of one exponential one, at a rate penalty of order L_n log n / n, shown for binary-Hamming and Gaussian sources. Nothing in it concerns logarithmic loss.
---
# LIT-tmpcwed2: Strong Successive Refinability and Rate-Distortion-Complexity Tradeoff

No, A., Ingber, A. & Weissman, T. (2016). Strong Successive Refinability and Rate-Distortion-Complexity Tradeoff. *IEEE Transactions on Information Theory* 62(6): 3618–3635. doi:10.1109/TIT.2016.2549540. arXiv:1506.03407 (10 June 2015).

Read in full in [NOTE-tmpmscti](../notes.d/NOTE-tmpmscti.md), from the arXiv copy.

## Why this is here

Registered as the source of a result the reading of Equitz and Cover
([NOTE-tmpyi9oi](../notes.d/NOTE-tmpyi9oi.md), [LIT-tmp25otd](LIT-tmp25otd.md)) recalled: that every discrete source is successively
refinable under logarithmic loss, the loss under which the information
bottleneck is a rate–distortion problem. That would bear on the stochastic half
of [QUESTION-tmpproc1](../questions.d/QUESTION-tmpproc1.md). The reading found the attribution wrong. This paper is
about second-order (dispersion) refinability and about layered codes, and it
stays in the record for those. Its bearing on [QUESTION-tmpproc1](../questions.d/QUESTION-tmpproc1.md) is indirect, and
[NOTE-tmpmscti](../notes.d/NOTE-tmpmscti.md) says what the log-loss result would and would not imply.
