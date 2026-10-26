---
status: Deferred
status_note: >-
  filed 2026-10-26, not read. Registered from the owner's exchange
  "Experimental Infrastructure Review", shared at
  https://chatgpt.com/share/6adfa6e4-a0b0-83e9-b3a0-0b53e6000277 and read
  from the saved copy the owner uploaded, which holds turns T18–T24 only. No
  NOTE is filed.
title: 'Learning author-topic models from text corpora'
version: 1
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
tags:
- probabilistic-modeling
- information-retrieval
date: '2026-10-26'
published: '2010-01-29'
doi: '10.1145/1658377.1658381'
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
  and retrieval experiments showing systematic differences from alternatives
  (abstract).
---

# LIT-tmpnzjy3: Learning author-topic models from text corpora

Rosen-Zvi, M., Chemudugunta, C., Griffiths, T., Smyth, P. & Steyvers, M.
(2010). Learning author-topic models from text corpora. *ACM Transactions on
Information Systems* 28(1): 1–38. doi:10.1145/1658377.1658381.

Not read. The summary is drawn from the abstract, and a reading should
check it first.

## Why this is here

Cited at T21 for the second component of the reply's combined model: which
employees take part in which interpretive themes, with overlapping
memberships. The record held the author–topic model only as the baseline of
[NOTE-008](../notes.d/NOTE-008.md) ([LIT-013](LIT-013.md)), in its nonparametric form. It bears on [QUESTION-tmpixgs8](../questions.d/QUESTION-tmpixgs8.md), as
the plain-text case of inferring members' overlapping participation from
what they write.
