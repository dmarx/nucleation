---
status: Active
status_note: >-
  read 2026-10-20 ([NOTE-tmpydsd3](../notes.d/NOTE-tmpydsd3.md)) in full; worth reading for the only rate the record holds for Simon's near-decomposability: with contracting fast modules (rate β_f) and a contracting reduced slow system (rate β_g), and coupling perturbations bounded affinely in the off-manifold state, Lemma 3 and Theorem 1 keep the fast variables within O(ε) of their quasi-steady manifold and the slow variables within O(ε) of the reduced system, uniformly in time after a transient of (1/β_f + 1/(εβ_g)) log(1/ε), for every ε below an explicit critical timescale separation ε_c = β_f / [χ_f(α_f,x + χ_g α_f,y α_g,x / β_g)]; and for Remark 6, that the micro states act on the macro level through their quasi-steady values, "an aggregation in time", not an ensemble aggregate. Read it knowing that it is a five-page preprint, never published in a journal, whose proofs are sketches; that Remark 8 prints ε_c inverted (the worked example's value √2/7 is the reciprocal of the printed expression, and matches Hypothesis 2); that Lemma 3's O(ε) bound on the slow error needs d_g = 0, which the proof's last line assumes silently while the worked example lists d_g = 1; that it is deterministic throughout and bounds trajectory error only, not any information-theoretic dependence; that the slow coordinates and the partition are given, not found; and that ε_c is sufficient and in linear checks conservative by factors of 3 to 50.
title: 'A contraction based, singular perturbation approach to near-decomposability in complex systems'
version: 2
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Registered on 2026-10-20 as the open source of explicit error bounds for Simon's near-decomposability, wanted because the record cannot obtain Simon & Ando 1961 (LIT-1127) or Ando & Fisher 1963 (LIT-tmpl8e6l), and THEORY-661's open statement (LIT-1241, NOTE-977) gives no rate in ε. Wanted for QUESTION-221, THEORY-661, CLAIM-386, CLAIM-390, CLAIM-388 and QUESTION-218. Not previously held: a grep of record/literature.d for "1512.08464", "Bousquet" and the title found nothing. Citation from the arXiv abstract page: Bousquet, G. D. & Slotine, J.-J. E., arXiv:1512.08464 [math.DS], v1 submitted Mon, 28 Dec 2015 17:16:54 UTC, the only version; `published:` is 2015-12-28 per ADR-002. No journal version was found: the arXiv record carries no journal reference or DOI beyond its own (10.48550/arXiv.1512.08464); Crossref searches by title and by author (Bousquet, Slotine) returned only the authors' other papers; a web search found only the arXiv and ar5iv copies. OpenAlex and Semantic Scholar returned 429 (rate limit) to this client and were not consulted.
- version: 2
  date: '2026-10-20'
  note: >-
    Read in full (NOTE-tmpydsd3) from the arXiv PDF (v1, 14 pages, 11 of text), text extracted with pdftotext and every page with equations read from page images, since extraction dropped every ε. Status Active. The reading re-derived the key estimate (11) of Lemma 3, found Remark 8's ε_c inverted and an unstated d_g = 0 in Lemma 3's slow-error bound, and checked the bounds on two linear nearly decomposable systems (they held, with the predicted first order in ε). A Proposed THEORY files what the paper supports (THEORY-tmp5mn7l).
tags:
- complex-systems
- mathematics
date: '2026-10-20'
published: '2015-12-28'
arxiv: '1512.08464'
first_author: 'Bousquet'
keywords:
- 'near-decomposability'
- 'modularity'
- 'hierarchy'
- 'singular perturbation'
- 'contraction analysis'
- 'timescale separation'
- 'finite-gain L-stability'
implementations: []
summary: >-
  Bousquet & Slotine (arXiv 2015, unpublished). Recasts Simon's near-decomposability as a singularly perturbed system, fast module states x̃ and slow states y with ẏ = O(ε), and bounds the error of the reduced slow system with nonlinear contraction theory. If each module is contracting, the reduced slow system is contracting, and the coupling terms grow at most affinely in |x̃| and |y|, then below an explicit critical separation ε_c, after a transient of order (1/β_f + 1/(εβ_g)) log(1/ε), the fast states stay O(ε) from their quasi-steady values and the slow states O(ε) from the reduced trajectory, for all later time. A worked building example with a negative conductance shows multiple equilibria and instability above ε_c. Deterministic; bounds trajectory error, not dependence; proofs are sketches with a printed inversion in Remark 8.
---
<!-- inactive-ok-file: LIT-1127 LIT-tmpl8e6l — Unavailable; the works this one stands in for, nothing rests on them -->
<!-- inactive-ok-file: THEORY-tmp5mn7l — Proposed; the account filed from this reading -->

# LIT-tmpjuu33: A contraction based, singular perturbation approach to near-decomposability in complex systems

Bousquet, G. D. & Slotine, J.-J. E. (2015). A contraction based, singular perturbation approach to near-decomposability in complex systems. arXiv:1512.08464 [math.DS]. Preprint; no journal version found.

Read in full in [NOTE-tmpydsd3](../notes.d/NOTE-tmpydsd3.md).

## Key takeaways

- Simon's near-decomposability, cast as singular perturbation, has a
  first-order rate in ε for trajectory error, uniform in time, when both the
  modules and the reduced slow system are contracting (Theorem 1, Lemma 3).
- The admissible coupling has an explicit ceiling ε_c built from the
  contraction rates and the gains of the coupling terms (Hypothesis 2;
  Remark 8 prints it inverted). It is sufficient, not necessary.
- The micro level reaches the macro level through quasi-steady values,
  "an aggregation in time", not an ensemble sum (Remark 6, Remark 7).
- Nothing about information flow or dynamical dependence, and nothing about
  where the slow coordinates or the blocks are.

## Standing in the record

The open stand-in for Simon & Ando 1961 ([LIT-1127](LIT-1127.md)) and Ando & Fisher 1963
([LIT-tmpl8e6l](LIT-tmpl8e6l.md)), both Unavailable, on the one point [THEORY-661](../theory.d/THEORY-661.md) lacked: a rate
in ε. It supplies, under its hypotheses, the post-transient O(ε) estimate on
the fast variables that [CLAIM-386](../claims.d/CLAIM-386.md)'s numerical orders rested on unproved.
It does not answer [QUESTION-221](../questions.d/QUESTION-221.md), which asks about dependence, not
trajectory error.
