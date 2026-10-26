---
status: Active
status_note: >-
  read 2026-10-26 (NOTE-tmpjg8xz) in full, from the typeset article on
  Griffiths's lab page at Princeton; worth reading for the author–topic
  model as the plain-text case of members' overlapping participation in
  themes, for its factorization of the document–word matrix as ΦΘA
  (THEORY-tmp7wy54), and for the measured trade between pooling by author
  and per-document flexibility (THEORY-tmpt1q8m). Read it knowing that
  authorship is observed, never inferred, that the number of topics and
  the hyperparameters are fixed, that an author's topics are proportions
  summing to one, that identifiability is claimed only up to permutation
  when the likelihood allows a continuum, and that its readings of Enron
  employees' roles are by inspection.
title: 'Learning author-topic models from text corpora'
version: 2
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed, not read. At T21 the reply says "Rosen-Zvi and colleagues modeled
    authors as distributions over topics and applied the method to corporate
    email, among other corpora", linking "IBM Research" with no title. Of
    the author-topic papers by Rosen-Zvi and colleagues, only this journal
    paper includes corporate email (the Enron corpus); the UAI 2004 paper
    (arXiv 1207.4169) used NIPS papers and CiteSeer abstracts and the KDD
    2004 paper CiteSeer, so this one is registered. Checked on 2026-10-26
    against Crossref: Michal Rosen-Zvi, Chaitanya Chemudugunta, Thomas
    Griffiths, Padhraic Smyth and Mark Steyvers, ACM Transactions on
    Information Systems 28(1), 1–38, online 29 January 2010, which is
    `published:`. OpenAlex lists it closed. The summary follows the abstract
    on OpenAlex.
- version: 2
  date: '2026-10-26'
  note: >-
    Read in full at the owner's request (NOTE-tmpjg8xz). OpenAlex and
    Unpaywall list the work as closed; Semantic Scholar's green copy on
    psiexp.ss.uci.edu no longer resolves and its Wayback capture could
    not be fetched by this client, and the same typeset copy was found
    on Griffiths's lab page at Princeton, whose URL is added. Status
    Deferred → Active. Two THEORYs filed, THEORY-tmp7wy54 and THEORY-tmpt1q8m, both Active. The summary is checked against the reading
    and kept, without its "(abstract)" marker.
tags:
- probabilistic-modeling
- information-retrieval
date: '2026-10-26'
published: '2010-01-29'
doi: '10.1145/1658377.1658381'
url: 'https://cocosci.princeton.edu/tom/papers/AT_tois.pdf'
first_author: 'Rosen-Zvi'
keywords:
- 'author-topic model'
- 'topic models'
- 'Gibbs sampling'
- 'Enron email'
- 'unsupervised learning'
implementations: []
summary: >-
  Rosen-Zvi, Chemudugunta, Griffiths, Smyth & Steyvers (2010), ACM TOIS
  28(1). Each author is a probability distribution over topics and each
  topic a distribution over words; a multi-author document mixes its
  authors' topic distributions. Both are learned by MCMC and applied to
  CiteSeer abstracts, NIPS papers and 121,000 Enron emails, with perplexity
  and retrieval experiments showing systematic differences from alternatives.
---

# LIT-tmpnzjy3: Learning author-topic models from text corpora

Rosen-Zvi, M., Chemudugunta, C., Griffiths, T., Smyth, P. & Steyvers, M.
(2010). Learning author-topic models from text corpora. *ACM Transactions on
Information Systems* 28(1): 1–38. doi:10.1145/1658377.1658381.

Read in full on 2026-10-26 from the typeset copy on Griffiths's lab page
(NOTE-tmpjg8xz). The summary is checked against the reading.

## Why this is here

Cited at T21 for the second component of the reply's combined model: which
employees take part in which interpretive themes, with overlapping
memberships. The record held the author–topic model only as the baseline of
[NOTE-008](../notes.d/NOTE-008.md) ([LIT-013](LIT-013.md)), in its nonparametric form. It bears on [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md), as
the plain-text case of inferring members' overlapping participation from
what they write.
