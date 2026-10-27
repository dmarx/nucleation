---
status: Active
status_note: >-
  read 2026-10-27 ([NOTE-tmp0rtz0](../notes.d/NOTE-tmp0rtz0.md)) in full, from the authors' copy of the
  Machine Learning article, checked against the publisher's PDF; worth
  reading as the origin of the factorial hidden Markov model, the
  parametric model of several independent hidden chains jointly producing
  each observation that the infinite factorial HMM makes nonparametric,
  for its account of why exact inference costs O(TMK^{M+1}), and for its
  structured variational approximation. Read it knowing that its
  comparison of inference methods is on small synthetic problems
  ([THEORY-tmptn4xd](../theory.d/THEORY-tmptn4xd.md)), that its Bach chorale result is read from charts,
  and that its footnote on when the chains decouple is wrong for a
  non-isotropic covariance.
title: 'Factorial Hidden Markov Models'
version: 2
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Filed, not read, at the owner's request of 2026-10-27 ("file the next
    readings"): the curation entry of 2026-10-27 02:06 lists it among the
    works the infinite factorial HMM names (LIT-1577). Checked on
    2026-10-27 against Crossref, Springer's article page and the PDF's
    header: Zoubin Ghahramani and Michael I. Jordan, "Factorial Hidden
    Markov Models", Machine Learning 29(2–3): 245–273,
    doi:10.1023/A:1007425814087; received 10 July 1996, accepted 14
    January 1997, final manuscript 28 July 1997. Crossref dates it
    November 1997 (published-print and issued, month only). An earlier
    version with the same title and authors appeared in Advances in
    Neural Information Processing Systems 8 (NIPS 1995; the proceedings'
    BibTeX gives 1995 and no month), 7 pages. The conference met at the
    end of November 1995; that month is from memory of the conference,
    not from a page checked on 2026-10-27. The
    journal version is the one registered, as the owner's request names
    it. Under ADR-002's ruling that the earlier date is taken when a
    version appeared before the journal's under its own title,
    `published:` is 1995-11-01, month precision, the NIPS paper's; the
    alternative is 1997-11-01, the journal's. A technical-report version
    has a DTIC DOI, 10.21236/ada307097, which Crossref dates 1996-01-01;
    it is later than the NIPS paper and was not read. The summary follows the abstract.
- version: 2
  date: '2026-10-27'
  note: >-
    Read in full (NOTE-tmp0rtz0): §§1–6, Appendices A–D, the ten notes,
    Tables 1–2, the figure captions and the references, from the authors'
    copy on Ghahramani's page, the journal's typesetting with its page
    numbers left as "?, 1–31"; numbers, footnotes and the received dates
    were checked against the publisher's PDF (Machine Learning 29:
    245–273), which agrees on every point checked. The NIPS 1995 version
    was downloaded and not read. Status Deferred → Active.
    THEORY-tmptn4xd filed (Active). The summary is checked against the
    reading and given the model's form.
tags:
- probabilistic-modeling
- representation-learning
date: '2026-10-27'
published: '1995-11-01'
doi: '10.1023/A:1007425814087'
url: 'https://mlg.eng.cam.ac.uk/zoubin/papers/fhmmML.pdf'
first_author: 'Ghahramani'
keywords:
- 'factorial hidden Markov model'
- 'distributed state representation'
- 'variational inference'
- 'mean field'
- 'EM algorithm'
- 'Gibbs sampling'
implementations: []
summary: >-
  Ghahramani & Jordan (1997), Machine Learning 29: 245–273 (first as
  NIPS 8, 1995). The hidden state of an HMM is factored into M chains of
  K states, a priori independent, which jointly set each observation's
  mean, Σ_m W^(m)S_t^(m). Given the observations the chains are coupled,
  so the exact E step costs O(TMK^{M+1}). Gibbs sampling, a completely
  factorized and a structured variational approximation (M uncoupled
  HMMs with fictitious observations) are compared with exact EM on
  synthetic data, and a factorial HMM models Bach chorale melodies better
  than an unconstrained HMM.
---

# LIT-tmpkxifq: Factorial Hidden Markov Models

Ghahramani, Z. & Jordan, M. I. (1997). Factorial hidden Markov models.
*Machine Learning* 29(2–3): 245–273. doi:10.1023/A:1007425814087. An
earlier version: *Advances in Neural Information Processing Systems 8*
(1995).

Read in full on 2026-10-27 ([NOTE-tmp0rtz0](../notes.d/NOTE-tmp0rtz0.md)). One account was drawn from it:
[THEORY-tmptn4xd](../theory.d/THEORY-tmptn4xd.md).

## Why this is here

The owner asked on 2026-10-27 to "file the next readings". The infinite
factorial HMM ([LIT-1577](LIT-1577.md)) is this model with the number of binary chains
left unbounded under a Markov IBP prior, and the record held it without
its parametric original. [CASE-165](../cases.d/CASE-165.md)'s model of members' features, each
feature a two-state chain over days and the output a sum of the active
features' contributions, is a factorial HMM in structure, so this paper's
account of why the chains couple given the data, and of what exact and
approximate inference cost, bears on what fitting that model would take.
