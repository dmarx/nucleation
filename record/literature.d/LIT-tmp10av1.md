---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' copy on Johan Håstad's KTH page (www.csc.kth.se/~johanh/prgfromowf.pdf,
  a 46-page typescript, linked from ~johanh/papers.html; not the typeset SIAM pages
  1364–1396, which were not checked). Unpaywall and OpenAlex report the DOI closed;
  OpenAlex lists two CiteSeerX records (10.1.1.35.3930, 10.1.1.36.6283), not needed
  once the KTH copy was found. Worth reading as the source of the uniform theorem
  "There are one-way functions iff there are pseudorandom generators" (Theorem 6.2.2)
  and of computational entropy: the Shannon entropy of a P-samplable distribution
  that no adversary of a given time-success ratio tells apart from the output, with
  pseudoentropy (more than the input's entropy) and false entropy (more than the
  output's own) as the intermediate primitives. All adversaries are uniform and
  every reduction is an oracle Turing machine; there are no circuits and no min-entropy
  in the paper, and the general reduction is only weak-preserving (seed length n^10
  even in the direct construction). For [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) and [CLAIM-tmpzk2fj](../claims.d/CLAIM-tmpzk2fj.md) it shows
  that "if pseudorandom generators exist" may be read "if one-way functions exist",
  and that the claims' rendering G(U_n) is a false entropy generator with false
  entropy at least n, which names the gap they construct. For [LIT-tmp5gb4p](LIT-tmp5gb4p.md) it states,
  in Section 8, that Goldreich's note [cited as ICSI TR-89-051, July 1989] shows
  pseudorandom generators equivalent to "a pair of P-samplable distributions which
  are computationally indistinguishable but statistically very different"; the one-way-function
  form follows only by combining that with Theorem 6.2.2, which the paper does not
  write out. For [QUESTION-tmprdpkh](../questions.d/QUESTION-tmprdpkh.md) its time-success ratio is a worked cost-of-recovery
  measure that folds the success criterion into the cost, and for [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md)
  its distinguishing advantage is hit rate minus false-alarm rate, described by
  the paper itself as "the computationally restricted adversary definition of statistical
  distance"; it says nothing about real observers.
title: A Pseudorandom Generator from any One-way Function
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: 'Filed, not read. Citation checked against Crossref on 2026-10-15: Crossref
    gives January 1999, so `published:` is the first of the month. Not held in the
    Anthology of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2)
    for the authors, title and identifier found nothing. Read the same day (NOTE-tmpscadg).'
tags:
- mathematics
- information-theory
date: '2026-10-15'
published: '1999-01-01'
doi: 10.1137/S0097539793244708
first_author: Håstad
keywords:
- pseudorandom generator
- one-way function
- pseudoentropy
- computational entropy
implementations: []
summary: >-
  Håstad, Impagliazzo, Levin and Luby (1999), SIAM Journal on Computing 28(4). There
  is a pseudorandom generator if and only if there is a one-way function (Theorem
  6.2.2), in the uniform setting: adversaries are algorithms, and every reduction
  is an oracle Turing machine that turns an adversary for the constructed generator
  into an inverter for the given function. The route runs one-way function → false
  entropy generator → pseudoentropy generator → pseudorandom generator, where "computational
  entropy" is the Shannon entropy of some P-samplable distribution that no adversary
  of the given strength tells apart from the output. The general reduction is only
  weak-preserving: composed literally it needs seeds of length n^34, and the paper's
  direct construction n^10. The paper attributes to Goldreich [G : 89] the equivalence
  of pseudorandom generators with P-samplable pairs that are computationally indistinguishable
  but statistically very different; with Theorem 6.2.2 that gives the one-way function
  form, but the paper never writes that combined sentence.
---
<!-- inactive-ok-file: LIT-tmp5gb4p — Unavailable; held without a reading, cited as such -->

# LIT-tmp10av1: A Pseudorandom Generator from any One-way Function

Håstad, J., Impagliazzo, R., Levin, L. A. and Luby, M. (1999). A pseudorandom generator from any one-way function. *SIAM Journal on Computing* 28(4), 1364–1396. DOI 10.1137/S0097539793244708

## Key takeaways

Read in full ([NOTE-tmpscadg](../notes.d/NOTE-tmpscadg.md)). There is a pseudorandom generator if and only if there is a one-way function (Theorem 6.2.2), in the uniform setting: adversaries are algorithms, and every reduction is an oracle Turing machine that turns an adversary for the constructed generator into an inverter for the given function. The route runs one-way function → false entropy generator → pseudoentropy generator → pseudorandom generator, where "computational entropy" is the Shannon entropy of some P-samplable distribution that no adversary of the given strength tells apart from the output. The general reduction is only weak-preserving: composed literally it needs seeds of length n^34, and the paper's direct construction n^10. The paper attributes to Goldreich [G : 89] the equivalence of pseudorandom generators with P-samplable pairs that are computationally indistinguishable but statistically very different; with Theorem 6.2.2 that gives the one-way function form, but the paper never writes that combined sentence.

## Why this is here

The owner asked whether material downstream of computational indistinguishability, or the signal detection literature, could help with [CLAIM-tmpvdl53](../claims.d/CLAIM-tmpvdl53.md) and the bounded-observer questions. Read for [QUESTION-tmpadry4](../questions.d/QUESTION-tmpadry4.md). It is the theorem behind the book's "if and only if one-way functions" ([LIT-tmp5gb4p](LIT-tmp5gb4p.md), [LIT-tmpfy61e](LIT-tmpfy61e.md)), and pseudoentropy is the computational counterpart of information content that [CLAIM-tmpzk2fj](../claims.d/CLAIM-tmpzk2fj.md) and [QUESTION-tmprdpkh](../questions.d/QUESTION-tmprdpkh.md) reach for.
