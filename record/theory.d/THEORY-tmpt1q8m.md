---
status: Active
title: 'On NIPS papers (1,557 training and 183 test documents, 100 topics, fixed hyperparameters), the author–topic model gave test documents lower perplexity than LDA while sixteen or fewer of their words had been observed and higher perplexity beyond that; one fictitious author per document improved on the author–topic model throughout and lost to LDA after about 64 words, and an author model without topics did worst'
version: 1
history:
- version: 1
  date: '2026-10-26'
  note: >-
    Filed Active from NOTE-tmpjg8xz, under ADR-047 v3: the title claims no
    more than §6.4 measured, the reading was in full, and nothing in the
    record contradicts it. The paper's general explanation of the
    crossover is in the body, as its explanation.
tags:
- probabilistic-modeling
- information-retrieval
date: '2026-10-26'
source:
- LIT-tmpnzjy3
summary: >-
  Rosen-Zvi, Chemudugunta, Griffiths, Smyth and Steyvers (2010),
  LIT-tmpnzjy3, §6.4 and Fig. 11, read in NOTE-tmpjg8xz. Pooling by
  member helps prediction of a document of which little has been seen and
  costs it once the document's own words are enough. One corpus, one
  split, one topic count. It is not evidence that member-level structure
  is real, only that it predicts in a regime of sparse evidence.
---
<!-- inactive-ok-file: CASE-tmplcm41 — Proposed; the construction whose private term is compared, open -->

# THEORY-tmpt1q8m: On NIPS papers (1,557 training and 183 test documents, 100 topics, fixed hyperparameters), the author–topic model gave test documents lower perplexity than LDA while sixteen or fewer of their words had been observed and higher perplexity beyond that; one fictitious author per document improved on the author–topic model throughout and lost to LDA after about 64 words, and an author model without topics did worst

## Source

Rosen-Zvi, Chemudugunta, Griffiths, Smyth and Steyvers (2010),
LIT-tmpnzjy3, §6.4 and Fig. 11, read in full in NOTE-tmpjg8xz.

## What was actually shown

The 1,740 NIPS papers were split into 1,557 for training and 183 for
testing, 102 of them single-authored, chosen so that every test author
also wrote a training paper. Four models were fitted with T = 100,
α = 50/T = 0.5 and β = 0.01 (0.01 for the author model): the author model
(authors as distributions over words), LDA, the author–topic (AT) model,
and AT with one fictitious author per document. For each, ten chains
from different starts, with the 2,000th sample of each. A number of a
test document's words, shown on the x-axis, was used for further training
on that document, and perplexity was computed on the rest.

- The author model "has by far the worst performance".
- "For relatively small numbers of observed words (up to 16), the
  author-topic models (with and without fictitious authors) have lower
  perplexity than the LDA model." Above 16, "the author-topic model is not
  as accurate as the LDA model".
- The fictitious author gives "a curve that is systematically better than
  the author topic model without a fictitious author", and is "not quite as
  accurate on average as the LDA (topic) model after 64 words or so."

What could have come out otherwise: AT could have beaten LDA everywhere,
because authors are extra information, or nowhere, because LDA has more
freedom per document. It did neither.

The paper's explanation: LDA needs a document's own words to tune its
mixture, while AT "performs better than LDA with few (or even zero) words
observed from a document, by making use of the available side-information
about the authors", and loses later because it "does not have a
document-specific topic mixture". The retrieval experiment of §6.5 (Fig.
12) agrees in direction: AT best with title and authors as the query, LDA
marginally best with full text.

## What this does not say

- **Not a general law.** One corpus, one split, one topic count, fixed
  hyperparameters, and no interval on the curves. The crossover at sixteen
  words is a property of this setting.
- **Not that authors' topic profiles are real.** Better prediction from
  sparse evidence shows that pooling by author carries information. It
  does not show that the pooled profiles are identified
  (THEORY-tmp7wy54) or that they are what the authors are.
- **Not about unobserved authorship.** Every test author was a training
  author.

## Connections

- **QUESTION-tmpixgs8.** T21 asked that structure be allowed "to lose if
  it doesn't provide useful explanatory compression". Here member-level
  structure wins and loses in a measured trade, by the amount of evidence
  per document. An organizational model of members' messages would face
  the same trade, and a comparison at one evidence level would mislead.
- **CASE-tmplcm41.** The fictitious author plays the part of that case's
  per-employee private map: a term outside any shared component. Here it
  helped prediction throughout.
