---
status: Active
title: 'Collaborative filtering and topic models: latent relational structure recovered from interaction matrices, up to gauge, or uniquely under anchor conditions'
version: 1
standing: documented
tags:
- representation-learning
- mathematical-statistics
date: '2026-10-10'
line: 'pragmatic-transport'
illustrates:
- CLAIM-tmpro4wi
- CLAIM-tmpi8p0d
- CLAIM-tmp59oav
summary: >-
  Proposed as a laboratory by the owner at U57 and conceded as prior art
  after the owner's U58. Collaborative filtering recovers a user–item
  matrix's predicted relations with latent coordinates fixed only up to an
  invertible change; topic models recover individual topics only under
  nonnegativity plus separability or anchor-word conditions. It shows that
  recovery is possible and limited, not that a recovered component is a
  communicative kind.
supports:
- CLAIM-tmp59oav
- CLAIM-tmpi8p0d
---
<!-- inactive-ok-file: CLAIM-tmp59oav CLAIM-127 CLAIM-tmp2i7yj — Proposed; open, and cited as claims this case bears on, not as settled -->
<!-- inactive-ok-file: LIT-677 THEORY-182 THEORY-156 THEORY-176 — Proposed; cited as readings the record already held that bear on the case -->

# CASE-tmptm6yt: Collaborative filtering and topic models: latent relational structure recovered from interaction matrices, up to gauge, or uniquely under anchor conditions

## The case

Two established practices recover latent organization from a matrix of
relations, with no feature of any row or column given in advance.

- **Collaborative filtering.** A user–item matrix is fitted as R ≈ PQᵀ.
  A207 §1, with its displayed formulas transcribed: "For any invertible matrix A, define p'_u = Aᵀp_u, q'_i = A⁻¹q_i.
  Then (p'_u)ᵀq'_i = p_uᵀq_i. Thus an entire family of distinct
  latent-coordinate systems predicts exactly the same relationship
  matrix." A218 §4.2: collaborative filtering "recovers predictive
  relational profiles of users and items without assigning unique
  ontological meaning to particular latent coordinates." The standard
  reference is Koren, Bell and Volinsky 2009 (doi:10.1109/MC.2009.263),
  which A207 names.
- **Topic models.** A document–term matrix is fitted as X ≈ WH with
  nonnegative factors (NMF), or by latent Dirichlet allocation
  ([ANTH-LIT-592](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-592.md)). A218 §4.1: "The reconstruction is not uniquely
  determined in general." And: "Under appropriate separability, support,
  or generative assumptions, topic components can become identifiable."
  The works behind this are Lee and Seung 1999 (doi:10.1038/44565);
  Donoho and Stodden 2003
  (url:https://proceedings.neurips.cc/paper/2003/hash/1843e35d41ccf6e63273495ba42df3c1-Abstract.html),
  whose uniqueness result needs separability and complete factorial
  sampling; and Arora, Ge and Moitra 2012 (arXiv:1204.1956), whose
  provable recovery needs an anchor word for every topic. None of the
  three is held in either record. Each is a methods work an anthology
  topic could hold.

The record already held readings that bear on the case, and the exchange
cited none of them. Zhang and Blei ([LIT-677](../literature.d/LIT-677.md)) find LDA's optima joined by
flat paths, a practical form of topic-model non-identifiability. Word
embeddings learned contrastively factorize a co-occurrence matrix's
deviation from independence ([THEORY-182](../theory.d/THEORY-182.md), [LIT-855](../literature.d/LIT-855.md); also [LIT-863](../literature.d/LIT-863.md)), and
[QUESTION-025](../questions.d/QUESTION-025.md) asks what such factorizations do with correlated attributes.
The nearest precedent for a human test of recovered structure is Chang et
al. 2009, "Reading Tea Leaves" ([ANTH-LIT-597](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-597.md)), in which human judges detect
intruding words and topics, and better held-out likelihood goes with less
interpretable topics.

## The laboratory proposed

The owner proposed the case as a method at U57: "I think collaborative
filtering via matrix factorization might give us a useful laboratory here".
A207 built it out. It is a design, not a study, and every number in it is
invented: its 4×4 matrix of jokes and rebukes is labelled "Hypothetical
ratings, not empirical data".

A207 §4 replaces preferences by communicative judgements in a tensor
Y_uiac, where u is an interpreter, i a communicative realization, a a
judgement task "such as teasing, condemnation, solidarity, authority", and
c a presentation or framing condition. It proposes three experiments.

1. **Recognition without surface similarity.** Realizations that perform
   one act in different wording, and realizations in near-identical wording
   that perform different acts. The hypothesis is that similarity of
   response profiles, Similarity(R_·i, R_·j), predicts shared-kind
   judgements "even after controlling for lexical or embedding
   similarity". It is to be scored on "new realizations and held-out
   interpreters", as [CLAIM-011](../claims.d/CLAIM-011.md) requires.
2. **Gauge transformation.** Transform the fitted factors by invertible
   changes that preserve the predicted matrix, and "Ask which proposed
   signatures remain stable."
3. **Intervention.** Estimate P(Y_uia | do(c)), keeping apart "actual
   situation changes from information supplied to the interpreter". In a
   vignette design the second is all that is available ([CLAIM-127](../claims.d/CLAIM-127.md),
   [CLAIM-tmp2i7yj](../claims.d/CLAIM-tmp2i7yj.md)).

A207 §5 adds the design rule that matters most. Observational ratings are
missing for non-random reasons, and "Missing-not-at-random exposure can
make learned factors reflect selection patterns rather than preferences or
communicative distinctions." The primary experiment is therefore to assign
realizations to interpreters at random and record nonresponse separately.

A207 §6 also calls a held-out comparison of decision risk between two
encodings "a direct Blackwell experiment". By the record's reading it is
not one. It compares a chosen family of losses, which [THEORY-176](../theory.d/THEORY-176.md) shows is
not Blackwell's order ([THEORY-156](../theory.d/THEORY-156.md)). A207 hedges ("The exact relationship to
Blackwell deficiency depends on which decision classes and statistical
experiments are included") but keeps the heading.

## What it can show

That restricted relational data support the recovery of latent structure,
and that the recovery has stated limits. A218 §4.3 gives both halves:
"Matrix factorization already demonstrates that restricted relational data
can support latent structure discovery." And: "Neither result alone
demonstrates that recovered components are constitutive kinds, that their
identities survive translation, or that they retain information for
independent communicative decisions."

So the case is evidence for what a factorization identifies and up to what
([CLAIM-tmpro4wi](../claims.d/CLAIM-tmpro4wi.md)), for the prior-art boundary ([CLAIM-tmpi8p0d](../claims.d/CLAIM-tmpi8p0d.md)), and for the
gap between identification and constitution ([CLAIM-tmp59oav](../claims.d/CLAIM-tmp59oav.md)). It is
evidence for A218's Recovery step, not for its Ontology step.

## What it does not show

- It does not show that a relational profile is the act. A207 §2: "If all
  interpreters share the same misconception, matrix factorization may
  recover a highly stable representation of that misconception."
- It does not show that any topic is a real kind. A210's own table answers
  "Every recovered topic is an objectively real kind" with "No".
- It does not bear on contextuality. A207 §7: "A low-rank factorization
  succeeding or failing does **not** establish contextuality" ([CLAIM-041](../claims.d/CLAIM-041.md)).
- Experiment 2 is not an experiment. Which quantities survive a change of
  gauge is settled by algebra before any data arrive: exactly the
  functions of the predicted matrix ([CLAIM-tmpro4wi](../claims.d/CLAIM-tmpro4wi.md)). Only its second half,
  whether different sparse completions support conflicting
  classifications, is empirical.
- No part of the laboratory has been run.
