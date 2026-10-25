---
status: Active
status_note: >-
  read 2026-10-25 ([NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md)) in full, from the authors' preprint of March 2013 on Alexander Rakhlin's MIT page; worth reading for the complete classification of finite partial-monitoring games by minimax regret (0, Θ̃(√T), Θ(T^2/3), Θ(T); [THEORY-tmpz3a05](../theory.d/THEORY-tmpz3a05.md)), for the linear-algebra conditions, global and local observability, that decide the class ([THEORY-tmpwtj3m](../theory.d/THEORY-tmpwtj3m.md)), and for the algorithms CBP and NeighborhoodWatch. Read it knowing that the adversarial classification covers non-degenerate games only, that Lattimore and Szepesvári (2019) later completed it and corrected errors in the earlier analyses, that the classification concerns the best policy in a fixed, known game, and that the copy read is the preprint, not the journal text.
title: 'Partial Monitoring—Classification, Regret Bounds, and Algorithms'
version: 2
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed, not read. Registered unread from the owner's exchange of
    2026-10-24/25 (the continuation of "Review PR 327 Improvements"),
    shared at
    https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824, where
    it is cited at turn U29. Citation checked against Crossref on
    2026-10-25: Gábor Bartók, Dean P. Foster, Dávid Pál, Alexander Rakhlin
    and Csaba Szepesvári, Mathematics of Operations Research 39(4),
    967–997, issue November 2014 (Crossref gives no day). OpenAlex gives
    2014-06-27, the online date of the journal's advance article; under
    ADR-002's earlier-date rule `published:` takes it. The INFORMS article
    page returned 403, so that date was not seen on the publisher's site.
    The authors' arXiv papers on the same programme (1102.2041, 1108.4961,
    1206.6487) are earlier, different works and are not this paper.
    OpenAlex lists it closed, with CiteSeerX records only. The summary
    follows the abstract on Crossref.
- version: 2
  date: '2026-10-25'
  note: >-
    Read in full (NOTE-tmpupizd), from the authors' preprint dated March 27, 2013, on Alexander Rakhlin's MIT page; the appendix proofs were read at the level of their statements and main steps. Status Deferred → Active. The open-copy URL is added. The summary is checked against the reading and narrowed: the adversarial classification holds for non-degenerate games only. THEORY-tmpwtj3m (Active, re-derived) and THEORY-tmpz3a05 (Proposed) are filed from it.
tags:
- learning-theory
- game-theory
- anthology-candidate
date: '2026-10-25'
published: '2014-06-27'
doi: '10.1287/moor.2014.0663'
url: 'https://www.mit.edu/~rakhlin/papers/partial_monitoring.pdf'
first_author: 'Bartók'
keywords:
- 'partial monitoring'
- 'minimax regret'
- 'online learning'
- 'feedback signal'
- 'classification of games'
implementations: []
summary: >-
  Bartók, Foster, Pál, Rakhlin & Szepesvári (2014). In a
  partial-monitoring game the learner picks an action, the environment an
  outcome, and the learner suffers a loss and receives a feedback signal,
  both fixed functions of action and outcome. For every game with finitely
  many actions and outcomes (against adversarial opponents, every
  non-degenerate one) the minimax regret is zero or scales as T^1/2,
  T^2/3 or T, up to constants and logarithmic factors; computationally
  efficient algorithms attain it within a logarithmic factor, with
  individual bounds on expected regret for i.i.d. outcomes (abstract).
---
<!-- inactive-ok-file: CLAIM-446 — Proposed; the claim the exchange applied this theory to, named, nothing here rests on it -->
<!-- inactive-ok-file: THEORY-tmpz3a05 — Proposed; the classification as the paper states it, filed from the reading -->
# LIT-tmpwpq36: Partial Monitoring—Classification, Regret Bounds, and Algorithms

Bartók, G., Foster, D. P., Pál, D., Rakhlin, A. & Szepesvári, C. (2014).
Partial monitoring—classification, regret bounds, and algorithms.
*Mathematics of Operations Research* 39(4): 967–997.
doi:10.1287/moor.2014.0663.

Read 2026-10-25 in full ([NOTE-tmpupizd](../notes.d/NOTE-tmpupizd.md)), from the authors' preprint of
March 2013, not compared with the journal text. The summary was checked
against it and narrowed to non-degenerate games for adversarial
opponents.

## Why this is here

The owner asked at U29 whether the exchange had turned up content that
would improve the record's mathematical toolkit, and the reply put partial
monitoring first, as the formal case of an organization whose feedback is
informative about some comparisons of its processes and not others. U30
used its global-observability condition for the channels an organization
can access, and U31 built experiments on it. The record had no work on
partial monitoring. It bears on [QUESTION-271](../questions.d/QUESTION-271.md) (bandit against
full-information evaluation of an organization's processes) and on
[CASE-124](../cases.d/CASE-124.md) (what responses can distinguish). The exchange applied it to
[CLAIM-446](../claims.d/CLAIM-446.md)'s avoid/approach example; read as a partial-monitoring game
that example is locally observable, so the failure lies in the policy's
not sampling approach, not in the feedback, as the dated note of
2026-10-25 on that claim says. The audited-governance study [CASE-tmpjmerx](../cases.d/CASE-tmpjmerx.md)
is the record's nearest construction.
