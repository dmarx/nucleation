---
status: Proposed
promote_when: >-
  A study that varies how far two embedding spaces are from isometric
  independently of the languages, for instance by training one language's
  corpus with different domains, algorithms or controlled distortion, and
  runs several structurally different unsupervised aligners on each
  setting, adversarial, GW and OT with Procrustes, with restarts. It must
  measure the departure from isometry without the gold dictionary. The
  account is confirmed if that measure predicts the success of all the
  aligners alike, beyond what the language pair alone predicts. It is
  refuted if one aligner succeeds where the measure says the spaces are
  far apart, or if most failures disappear with restarts.
title: 'Unsupervised alignment of two monolingual word-embedding spaces recovers translations only where the spaces are close to isometric, and the distance from isometry depends on the corpora and the embedding algorithm as well as on the languages: adversarial alignment fails for English with Estonian or Finnish, across corpus domains, and between skip-gram and CBOW spaces of the same language pair, GW alignment is weakest on the same Finnish pair, and a spectral dissimilarity of small nearest-neighbour graphs tracks success'
version: 1
tags:
- translation
- representation-learning
date: '2026-10-29'
source:
- LIT-tmpqoytq
- LIT-tmpprsxm
summary: >-
  Søgaard, Ruder and Vulić (2018), LIT-tmpqoytq, read in NOTE-tmpi3f1e,
  with the GW results of Alvarez-Melis and Jaakkola (2018),
  LIT-tmpprsxm, read in NOTE-tmpgvlkv. Proposed: the evidence is single
  runs of one adversarial method, plus one GW table, and the authors
  themselves report that some seeds succeed where the method otherwise
  fails. What it does not support is a typological law about dependent
  marking, or the reading that a good fit establishes that the matched
  words mean the same.
---
<!-- inactive-ok-file: CLAIM-135 — Proposed; the distinction this account is kept inside, cited as open -->

# THEORY-tmpox88b: Unsupervised alignment of two monolingual word-embedding spaces recovers translations only where the spaces are close to isometric, and the distance from isometry depends on the corpora and the embedding algorithm as well as on the languages: adversarial alignment fails for English with Estonian or Finnish, across corpus domains, and between skip-gram and CBOW spaces of the same language pair, GW alignment is weakest on the same Finnish pair, and a spectral dissimilarity of small nearest-neighbour graphs tracks success

## Source

Søgaard, Ruder and Vulić (2018), LIT-tmpqoytq, §§2 and 4, Tables 2–3 and
Fig. 2, pp. 2–9 of arXiv 1805.03620v1; read in NOTE-tmpi3f1e. Alvarez-Melis
and Jaakkola (2018), LIT-tmpprsxm, Tables 1–2, pp. 7–8 of arXiv
1809.00013v1; read in NOTE-tmpgvlkv.

## What was actually shown

**Language pairs.** Conneau et al.'s adversarial method with Procrustes
refinement, on fastText Wikipedia embeddings, reaches P@1 81.89 for
English–Spanish and 0.00 and 0.09 for English–Estonian and
English–Finnish (Table 2). A 1.7-billion-word Finnish corpus does not
help (P@1 0.0, p. 5). Estonian–Finnish aligns at 29.62.

**Domains.** With every corpus capped at 1.1M sentences, English–Spanish
aligns when both corpora are from the same domain. Across EuroParl,
Wikipedia and EMEA, "performance is close to zero" (p. 6).

**Algorithms.** English skip-gram against Spanish skip-gram aligns at
80.15–81.89 under changes of window and n-gram range. English skip-gram
against Spanish CBOW aligns at 0.00–0.13 (Table 3), though the CBOW space
is of normal monolingual quality (footnote 9).

**A second method.** GW alignment, which has no adversarial step, is level
with the adversarial method on Romance and Germanic pairs. It reaches only
18.3 on English–Finnish in Dinu et al.'s data, against 33.5 for
self-learning, and 45.1 on English–Russian in Conneau et al.'s data
(LIT-tmpprsxm, Tables 1–2).

**The diagnostic.** Δ, the summed squared difference of the top Laplacian
eigenvalues of 10-node nearest-neighbour graphs, correlates with P@1 across
the eight pairs of Table 2. Recomputed from the table: Pearson −0.889,
Spearman −0.905. The paper reports ρ ≈ 0.89; the sign is negative because
Δ is a dissimilarity.

**What could have failed.** Finnish could have aligned once its corpus was
large. Spanish could have aligned across domains or across algorithms. Δ
could have been unrelated to success. None of these happened.

## What this does not say

- **That the failures are impossible alignments.** About 1 run in 10 on
  Estonian, Finnish and Greek is "on par with Turkish" (LIT-tmpqoytq,
  footnote 5). Part of what is reported is the adversarial optimiser's
  instability. The GW evidence is a single table, not a test on the
  paper's settings.
- **A typological law.** The claim about languages that are neither dependent-marking nor isolating rests on
  three failing languages, which differ from English in Wikipedia size and,
  for Greek, script. Hungarian, which is agglutinative, aligns.
- **That Δ is a usable predictor.** It is computed on gold-translated
  subgraphs (Table 2 caption), so it presupposes the dictionary that
  unsupervised induction was meant to produce, and it rests on eight
  points.
- **That a good fit establishes that matched words mean the same.** The
  account is about when a fit exists. Where the fit is good it is
  relational resemblance under the chosen similarity (CLAIM-135). Within
  that fit, symmetric structure is left undetermined (THEORY-tmpa43ta).
- **That isomorphism fails in the exact sense the paper tested.** Exact
  VF2 isomorphism of 10-node graphs fails almost always (p. 2). That is a
  different and much stronger property than the near-isometry the
  methods need.
