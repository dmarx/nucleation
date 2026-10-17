---
status: Active
status_note: 'read in full 2026-10-17 (NOTE-tmpvo3m6), from the authors'' preprint dated 12 May 2006; worth reading as the interventional counterpart of transfer entropy: information flow I(X_A → X_B | X̂_S) is conditional mutual information computed from do()-distributions instead of observational ones, it vanishes exactly under a graphical condition (ud-separation), and examples show it differs from transfer entropy and conditional mutual information in both directions. Read it knowing that it needs the full causal Bayesian network and its mechanisms, not data; that the examples are deterministic binary networks; and that its Example 6 claim of one bit holds, by the record''s calculation, only for k = 1 or when imposing X_k alone. The published version (Advances in Complex Systems 11(1), 2008) was not compared. Filed as THEORY-tmpkovi2.'
title: 'Information Flows in Causal Networks'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Filed at the owner's request as the interventional counterpart of
    transfer entropy, to pair with Eichler and Didelez (LIT-tmp7q0hf).
    Citation checked against Crossref on 2026-10-17: Advances in Complex
    Systems 11(1): 17–41, February 2008. Not held in the Anthology of the
    SOTA: a grep of its record/ (clone of 2026-10-12, d1573d2) for "Ay",
    "Polani" and the DOI found nothing. Read in full the same day
    (NOTE-tmpvo3m6) from the copy in the University of Hertfordshire
    repository (UHRA eprint 162, 902104.pdf), which is the authors'
    preprint, 15 pp., dated 12 May 2006 (MPI MiS preprint 47/2006), not
    the journal version. `published:` is that date: Crossref gives the
    print issue only as February 2008 and its one full date, an online
    posting of 20 November 2011, postdates print, so the earliest full
    date the work carries is the preprint's.
tags:
- causality
- information-theory
date: '2026-10-17'
published: '2006-05-12'
doi: '10.1142/S0219525908001465'
first_author: 'Ay'
keywords:
- 'information flow'
- 'causal networks'
- 'causal independence'
- 'intervention'
- 'transfer entropy'
- 'ud-separation'
implementations: []
summary: >-
  Ay & Polani (2008), *Advances in Complex Systems* 11(1): 17–41. In a causal Bayesian network, X_B is causally independent of X_A imposing X_S if setting x_A after setting x_S does not change the post-interventional distribution of X_B; this holds for every model on a DAG iff every directed path from A to B meets S (ud-separation, Theorem 2). Information flow I(X_A → X_B | X̂_S) is conditional mutual information with every probability replaced by its interventional counterpart, and is zero iff causal independence holds (under positivity of p(x_S)). Examples show it differs from mutual information and from transfer entropy: two binary chains that swap states have zero transfer entropy and nonzero flow, and an observationally identical pair of independent inverters has zero of both.
---

# LIT-tmpq33qh: Information Flows in Causal Networks

Nihat Ay and Daniel Polani (2008), "Information Flows in Causal Networks", *Advances in Complex Systems* 11(1): 17–41 — doi:10.1142/S0219525908001465

## Key takeaways

*From the reading of the 2006 preprint, [NOTE-tmpvo3m6](../notes.d/NOTE-tmpvo3m6.md).*

- **Causal independence (Eq. 4).** X_B ⫫ X_A | X̂_S if
  p(x_B | x̂_A, x̂_S) = Σ_{x′_A} p(x′_A | x̂_S) p(x_B | x̂′_A, x̂_S) for all
  x_A, x_S. Defined through mechanisms, so for every configuration, not
  only observed ones. Not symmetric.
- **Theorem 2.** B is ud-separated from A by S (every directed path from A
  to B meets S) iff X_B is causally independent of X_A imposing X_S for
  every G-causal model. The interventional analogue of Verma and Pearl's
  d-separation theorem. d-separation implies ud-separation (Prop. 1).
- **Information flow (§5).** I(X_A → X_B | X̂_S) is the observational
  conditional mutual information's formula with each conditional replaced
  by its interventional counterpart, averaged over the observational
  p(x_S). Zero under causal independence; the converse needs every x_S to
  have positive probability (Prop. 3).
- **It is not transfer entropy (Example 6).** Two binary chains that swap
  states each step have zero transfer entropy and one bit of flow (at
  k = 1; see below). Two
  independent inverters started from the same distribution are
  observationally identical and have zero of both. Imposing a node can
  raise flow (Example 3) or lower it (Example 4).
- **Markov chains (§6).** For a single chain, flow between time windows
  equals their mutual information.

## Standing in the record

Filed on 2026-10-17 and read the same day. Filed as [THEORY-tmpkovi2](../theory.d/THEORY-tmpkovi2.md).
It is the information-theoretic form of the interventional notion Eichler
and Didelez use ([THEORY-tmp4g68i](../theory.d/THEORY-tmp4g68i.md)). The reading's check of Example 6
found the paper's one-bit flow holds for k = 1, and for any k only when the
target's last value alone is imposed. Imposing the whole past X_[1,k]
fixes Y_k = x_{k−1} and gives zero for k ≥ 2 by the paper's own definition.
That is the record's calculation, not the authors'.
