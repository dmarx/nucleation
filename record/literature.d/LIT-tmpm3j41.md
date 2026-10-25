---
status: Deferred
status_note: >-
  filed 2026-10-25, not read. Registered from the owner's exchange of
  2026-10-24/25 (the continuation of "Review PR 327 Improvements"), shared
  at https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824, where
  it is cited at turns U29 and U30. No NOTE is filed.
title: 'Online Learning and Blackwell Approachability with Partial Monitoring: Optimal Convergence Rates'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed, not read. Registered unread from the owner's exchange of
    2026-10-24/25 (the continuation of "Review PR 327 Improvements"),
    shared at
    https://chatgpt.com/share/6add7ae3-1a38-83ea-ac83-4f490e399824, where
    it is cited at turns U29 and U30 under the title "Online Learning and
    Blackwell Approachability with Partial Monitoring". The title on the
    proceedings page adds ": Optimal Convergence Rates", and that title is
    used here. Checked on 2026-10-25 against the PMLR page
    (proceedings.mlr.press/v54/kwon17a.html): Joon Kwon and Vianney
    Perchet, Proceedings of the 20th International Conference on
    Artificial Intelligence and Statistics (AISTATS 2017), PMLR 54:
    604–613, publication date 10 April 2017, which is `published:`. It has
    no DOI, and the arXiv API finds no copy under these authors, so it is
    filed by URL. The rates U29 gives, T^-1/2 for signals independent of
    the decision and T^-1/3 for general signals, match the abstract. The
    summary follows the abstract on the PMLR page.
tags:
- learning-theory
- game-theory
- anthology-candidate
date: '2026-10-25'
published: '2017-04-10'
url: 'https://proceedings.mlr.press/v54/kwon17a.html'
first_author: 'Kwon'
keywords:
- 'Blackwell approachability'
- 'partial monitoring'
- 'online learning'
- 'convergence rates'
- 'regret minimization'
implementations: []
summary: >-
  Kwon & Perchet (2017). Blackwell approachability generalizes regret
  minimization (multi-criteria optimization, online optimization of a
  convex loss, online linear optimization under a cumulative constraint).
  Under partial monitoring the decision maker does not see outcomes but a
  random signal correlated with the decision–outcome pair, or with the
  outcome only. The paper gives the first approachability algorithms with
  convergence rate O(T^-1/2) when the signal does not depend on the
  decision and O(T^-1/3) for general signals, and shows that these rates
  cannot be improved without further assumptions on the objectives or the
  signals (abstract).
---
# LIT-tmpm3j41: Online Learning and Blackwell Approachability with Partial Monitoring: Optimal Convergence Rates

Kwon, J. & Perchet, V. (2017). Online learning and Blackwell
approachability with partial monitoring: Optimal convergence rates. In
*Proceedings of the 20th International Conference on Artificial
Intelligence and Statistics*, PMLR 54: 604–613.
https://proceedings.mlr.press/v54/kwon17a.html.

Not read. The summary is drawn from the abstract or from what the work
is standardly cited for. A reading should check it first.

## Why this is here

Cited at U29, in reply to the owner's question about improving the
record's mathematical toolkit, as the work that already joins partial
monitoring (Bartók et al., [LIT-tmpwpq36](LIT-tmpwpq36.md)) with approachability for
vector-valued objectives, an organization that must meet several demands
at once while seeing only partial feedback. U30 used it again for the rate
at which such guarantees hold. The record uses approachability only as the
engine of Hart and Mas-Colell's proof ([LIT-tmpxtwxt](LIT-tmpxtwxt.md), [NOTE-tmp7qq6n](../notes.d/NOTE-tmp7qq6n.md));
Blackwell's 1956 paper is not held.
