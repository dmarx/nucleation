---
status: Active
status_note: >-
  read in full 2026-10-24 ([NOTE-tmp0qrjw](../notes.d/NOTE-tmp0qrjw.md)) from the authors' final
  pre-publication draft of 26 January 2005, on Paul Resnick's University of
  Michigan page; worth reading as the founding scoring rule for evaluators
  when there is no ground truth. Each rater reports a signal, the center
  turns it into a posterior over a reference rater's report, and the rater
  is paid a strictly proper scoring rule on that posterior against what the
  reference rater actually reported. Truth-telling is then a strict Nash
  equilibrium (Proposition 1), and scaling the payments buys effort. It is
  not the only equilibrium: everyone always reporting h, or always l, is
  an equilibrium too, and collusion is named as a limit the paper does not
  settle. The mechanism needs a common prior and a signal model the center
  knows.
title: 'Eliciting Informative Feedback: The Peer-Prediction Method'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24 for the owner's question of how the record
    stands on multi-agent learning, for its bearing on scoring without an
    objective metric (CASE-tmpw4r7u). Citation checked against Crossref:
    Management Science 51(9): 1359–1373, issue September 2005, which gives
    the month only, so `published:` is 2005-09-01, meaning September 2005
    (ADR-002). Read in full from the authors' final pre-publication draft
    dated 26 January 2005, 34 pp., linked from
    http://presnick.people.si.umich.edu/papers/elicit/ (PDF at
    .../FinalPrePub.pdf), extracted by pdftotext: sections 1–5 and
    appendices A (proofs) and B (effort). The reference list was skimmed.
    Unpaywall and OpenAlex list no open copy of the version of record, so
    differences from it are not known. Page numbers in the NOTE are the
    draft's.
tags:
- game-theory
- social-science
- epistemology
date: '2026-10-24'
published: '2005-09-01'
doi: '10.1287/mnsc.1050.0379'
url: 'http://presnick.people.si.umich.edu/papers/elicit/FinalPrePub.pdf'
first_author: 'Miller'
keywords:
- 'peer prediction'
- 'proper scoring rules'
- 'reputation systems'
- 'recommender systems'
- 'mechanism design'
- 'effort elicitation'
- 'stochastic relevance'
implementations: []
summary: >-
  Miller, Resnick & Zeckhauser (2005). A center with no independent
  information scores each rater by applying a strictly proper scoring rule
  to the distribution of a reference rater's report that her own report
  implies, given a common prior and signal model. Truthful reporting is a
  strict Nash equilibrium; scaling the scores induces costly effort and can
  outweigh bribes; three or more raters allow budget balance. Uninformative
  equilibria also exist, and collusion, risk aversion, unmodelled private
  signals and trust in the center are named limits.
---
<!-- inactive-ok-file: NOTE-tmp0qrjw THEORY-tmpx9mep CLAIM-tmp0qupq — filed from this reading, and the claim it bears on, named -->

# LIT-tmpu91up: Eliciting Informative Feedback: The Peer-Prediction Method

Miller, N., Resnick, P. & Zeckhauser, R. (2005). Eliciting informative feedback: The peer-prediction method. *Management Science* 51(9): 1359–1373. doi:10.1287/mnsc.1050.0379.

## Key takeaways

*From the reading, [NOTE-tmp0qrjw](../notes.d/NOTE-tmp0qrjw.md). Page numbers are the January 2005 draft's.*

- **Scoring without ground truth.** The center "has no independent
  information, so its scoring decisions can depend only on the information
  provided by other raters" (p. 4). A rater is scored "not on agreement
  between the ratings, but on a comparison between the likelihood assigned
  to the reference rater's possible ratings and the reference rater's
  actual rating" (p. 3).
- **The result.** With stochastic relevance and any strictly proper
  scoring rule, truthful reporting is a strict Nash equilibrium
  (Proposition 1, p. 8). A scale factor makes effort worth its cost
  (Proposition 2) and can be set to overwhelm a bribe; a second rater's
  base transfer balances the budget.
- **Not unique.** "There may be non-truthful equilibria" (p. 9): in the
  worked example, everyone always reporting the same signal is an
  equilibrium too. The authors call the truthful one focal and suggest the
  center punish detected uninformative equilibria.
- **Limits named.** Collusion (p. 23), risk aversion, raters' private
  information the center does not use (the "Yes-Man" case, p. 24), coarse
  reports beyond two types, and raters' trust that the scheme rewards
  honesty.

## Why this is here

Filed on 2026-10-24 for the record's governance line, as a mechanism that
scores evaluators when there is no objective metric. It bears on the
authority-dependent scoring term of [CASE-tmpw4r7u](../cases.d/CASE-tmpw4r7u.md) and on [CLAIM-tmp0qupq](../claims.d/CLAIM-tmp0qupq.md)'s
worry that what is rewarded entrenches ([NOTE-tmp0qrjw](../notes.d/NOTE-tmp0qrjw.md)). Filed [THEORY-tmpx9mep](../theory.d/THEORY-tmpx9mep.md).
