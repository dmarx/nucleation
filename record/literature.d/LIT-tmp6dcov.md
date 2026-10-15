---
status: Active
status_note: >-
  read in full 2026-10-15 from the authors' copy on the Gershman lab site (gershmanlab.com/pubs/GershmanGoodman14.pdf,
  6 pp.). The version of record is on eScholarship (escholarship.org/uc/item/34j1h7k5),
  whose PDF refused direct requests from this environment. The page range 517–522
  is from the authors' own later citation. Worth reading as the paper that named
  amortized inference for cognitive science. It defines amortized inference as caching
  ("memoizing") sub-inferences and reusing them on related queries. It gives the
  first behavioural evidence for this, from two small online experiments on one
  Bayesian network: with the sub-query first, answers to a complex query were predictable
  from a person's own sub-answer (r = 0.28, against −0.11 in the reverse order),
  and they were faster relative to a matched baseline. For [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md) it
  shows that the authors treat amortization as retrieval standing in for recomputation,
  which supports the question's unification for internal memory only. It does not
  touch external storage or distributed cognition. It supplies storage cost, decomposability
  and frequency as untested trade-offs, but no staleness term, and no directional
  bias toward earlier answers, which belongs to later work ([LIT-tmpt2ql7](LIT-tmpt2ql7.md)). For [CLAIM-tmpygqjz](../claims.d/CLAIM-tmpygqjz.md)
  it is consistent with the trade and with frequency being one consideration among
  several, and its error propagation is error preserved by reuse, not staleness.
title: Amortized Inference in Probabilistic Reasoning
version: 1
history:
- version: 1
  date: '2026-10-15'
  note: >-
    Filed 2026-10-15. Citation checked on eScholarship (ark:/13030/qt34j1h7k5, Proceedings
    of the Annual Meeting of the Cognitive Science Society, vol. 36, peer reviewed):
    no DOI, and eScholarship gives the year only, so `published:` is the first of
    January. Pages 517–522 are from the authors' own later citation (Dasgupta et
    al. 2017) and are not confirmed by the proceedings. Not held in the Anthology
    of the SOTA: a grep of its record/ (clone of 2026-10-15, commit d1573d2) for
    the authors and the title found nothing. Read the same day (NOTE-tmpw9lhz).
tags:
- cognition
- probabilistic-modeling
date: '2026-10-15'
published: '2014-01-01'
url: https://escholarship.org/uc/item/34j1h7k5
first_author: Gershman
keywords:
- induction
- Bayesian inference
- memory
implementations: []
summary: >-
  Gershman and Goodman (2014), Proceedings of the 36th Annual Conference of the
  Cognitive Science Society (pp. 517–522 by the authors' later citation). Proposes
  that people amortize probabilistic inference by caching (memoizing) sub-inferences
  and composing them for related later queries. In two Mechanical Turk experiments
  on a five-node network, answers to a complex query depended on the person's own
  earlier answer to a sub-query only when the sub-query came first (r = 0.28 against
  −0.11), and responses were faster when reuse was available. Costs of reuse are
  discussed, not measured.
---
<!-- inactive-ok-file: CLAIM-tmpygqjz — Proposed; open claims and accounts cited as open, nothing here rests on their being settled -->

# LIT-tmp6dcov: Amortized Inference in Probabilistic Reasoning

Gershman, S. J. and Goodman, N. D. (2014). Amortized inference in probabilistic reasoning. In *Proceedings of the 36th Annual Conference of the Cognitive Science Society*, 517–522. https://escholarship.org/uc/item/34j1h7k5

## Key takeaways

Read in full ([NOTE-tmpw9lhz](../notes.d/NOTE-tmpw9lhz.md)). Gershman and Goodman define amortized inference as the reuse of past inferences, cached as sub-computations, to answer related later queries. They report two small online experiments in which order alone made reuse available. When a sub-query came before a complex query on a five-node Bayesian network, a person's answer to the complex query could be predicted from their own answer to the sub-query (r = 0.28; r = −0.11 when the order was reversed). Answers to the complex query were also faster relative to a structurally matched baseline. Reuse in this paper is internal memory, and it is shown only through correlation and speed, within one task, with small effects. The paper does not measure costs. Storage cost and the choice of what to store are listed as open trade-offs. Bias, staleness and interference are not studied: reuse that may be "inaccurate" without modification, and interference and forgetting of stored inferences, appear only as questions.

## Why this is here

The source of the term "amortized inference" in cognitive science, which
the owner reached for: "amortized retrieval is actually a kind of
amortized computation". Read for [QUESTION-tmp1mkzc](../questions.d/QUESTION-tmp1mkzc.md).
