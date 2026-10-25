---
status: Deferred
status_note: >-
  filed 2026-10-25, not read. Registered from the owner's exchange of
  2026-10-24/25 (the continuation of "Review PR 327 Improvements"), shared
  at https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824, where
  it is cited at turn U29 and its theory is used at U30 and U31. No NOTE
  is filed.
title: 'Partial Monitoring—Classification, Regret Bounds, and Algorithms'
version: 1
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
tags:
- learning-theory
- game-theory
- anthology-candidate
date: '2026-10-25'
published: '2014-06-27'
doi: '10.1287/moor.2014.0663'
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
  many actions and outcomes the minimax regret is zero or scales as T^1/2,
  T^2/3 or T, up to constants and logarithmic factors; computationally
  efficient algorithms attain it within a logarithmic factor, with
  individual bounds on expected regret for i.i.d. outcomes (abstract).
---
<!-- inactive-ok-file: CLAIM-tmp8z857 — Proposed; the claim the exchange applied this theory to, named, nothing here rests on it -->
# LIT-tmpwpq36: Partial Monitoring—Classification, Regret Bounds, and Algorithms

Bartók, G., Foster, D. P., Pál, D., Rakhlin, A. & Szepesvári, C. (2014).
Partial monitoring—classification, regret bounds, and algorithms.
*Mathematics of Operations Research* 39(4): 967–997.
doi:10.1287/moor.2014.0663.

Not read. The summary is drawn from the abstract or from what the work
is standardly cited for. A reading should check it first.

## Why this is here

The owner asked at U29 whether the exchange had turned up content that
would improve the record's mathematical toolkit, and the reply put partial
monitoring first, as the formal case of an organization whose feedback is
informative about some comparisons of its processes and not others. U30
used its global-observability condition for the channels an organization
can access, and U31 built experiments on it. The record had no work on
partial monitoring. It bears on [QUESTION-tmpdicvf](../questions.d/QUESTION-tmpdicvf.md) (bandit against
full-information evaluation of an organization's processes) and on
[CASE-124](../cases.d/CASE-124.md) (what responses can distinguish). The exchange applied it to
[CLAIM-tmp8z857](../claims.d/CLAIM-tmp8z857.md)'s avoid/approach example; read as a partial-monitoring game
that example is locally observable, so the failure lies in the policy's
not sampling approach, not in the feedback, as the dated note of
2026-10-25 on that claim says. The audited-governance study {{F-K-AUDIT}}
is the record's nearest construction.
