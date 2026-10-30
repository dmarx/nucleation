---
status: Active
status_note: >-
  read 2026-10-30 ([NOTE-tmp9x3x4](../notes.d/NOTE-tmp9x3x4.md)), Skimmed: §§1–3 and 5–8 in full, with
  Theorem 26 and its proof checked line by line, from arXiv's v2 (13
  October 2025, 23 pages); §4, on representing loss functions, was not
  read. Worth reading as a short, self-contained proof of Le Cam's
  randomization theorem for finite experiments against a fixed prior,
  after Torgersen: the least prior-averaged total variation between a
  garbling of e and e′ is at most ε exactly when e's minimum Bayes risk
  exceeds e′'s by at most ε‖L‖∞ for every action set and loss. Read it
  knowing that the result is for one prior, not uniform in the unknown;
  that its reverse implication, and so the theorem as stated for every
  loss, loses a factor of 2 for losses that take both signs (it holds for
  losses in [0, 1]); that the saddle point it invokes is more than Sion's
  theorem gives, though the proof needs only the minimising rule; and that
  Lemma 30's linear programme computes twice the directed deficiency.
title: 'On Experiments'
version: 1
history:
- version: 1
  date: '2026-10-30'
  note: >-
    Filed and read on 2026-10-30 from the copy the day's search found,
    for CLAIM-488. Citation checked against arXiv (2508.08288, stat.ML;
    v1 submitted 5 August 2025, which is the `published:` date; v2 of 13
    October 2025 was read): Brendan van Rooyen (Decisions 360), "On
    Experiments". No entry for it was found in literature.d by arXiv id,
    title or author.
tags:
- mathematical-statistics
- information-theory
date: '2026-10-30'
published: '2025-08-05'
arxiv: '2508.08288'
first_author: 'van Rooyen'
keywords:
- 'comparison of experiments'
- 'Blackwell-Sherman-Stein theorem'
- 'randomization theorem'
- 'deficiency'
- 'data processing inequality'
- 'proper losses'
- 'Markov transitions'
- 'linear programming'
implementations: []
summary: >-
  van Rooyen (arXiv 2025). Experiments are Markov transitions from a
  finite set of unknowns to a finite observation set. A general data
  processing theorem: any risk minimised over the strategies an
  experiment allows is monotone under garbling. Blackwell–Sherman–Stein
  follows. With a prior π fixed, the directed deficiency ξ^π(e, e′) is the
  least, over garblings f, of the π-average total variation between f∘e
  and e′; Theorem 26 (Le Cam's randomization theorem) says ξ^π ≤ ε exactly
  when e's minimum Bayes risk is within ε‖L‖∞ of e′'s for every action set
  and loss. The symmetrised deficiency is a metric for a prior of full
  support, and ξ^π is a linear programme.
---
<!-- inactive-ok-file: NOTE-tmp9x3x4 — Skimmed; this entry's reading, which says what was read -->
<!-- inactive-ok-file: CLAIM-488 — Proposed; the claim this reading was filed for, cited as open -->

# LIT-tmphckuv: On Experiments

van Rooyen, B. (2025). On Experiments. arXiv:2508.08288.

## Key takeaways

*From the reading, [NOTE-tmp9x3x4](../notes.d/NOTE-tmp9x3x4.md) (Skimmed: §4 not read).*

- **Fixed-prior randomization theorem (Theorem 26, pp. 18–19).** For a
  fixed prior π and finite sets, Risk^π_L(e) ≤ Risk^π_L(e′) + ε‖L‖∞ for all
  action sets and losses if and only if min_f E_{θ∼π} V(f∘e(θ), e′(θ)) ≤ ε.
  The proof of the forward implication fixes a rule d′ for e′, applies
  the minimax theorem to the risk gap as a function of the loss and of
  e's rule, and takes the action set to be e′'s observations and d′ the
  identity.
- **Its limits.** It is stated for a fixed prior, with the deficiency an
  average over θ, not a maximum. Its reverse implication is right for
  losses in [0, 1] and off by a factor of 2 for signed losses, since V is
  half the ℓ1 distance.
- **Data processing as a functor (Theorem 24).** Any risk minimised over
  the strategies an experiment can reach cannot fall under garbling.
- **Deficiency by linear programme (Lemma 30).** The programme as printed
  sums the absolute deviations, so its value is 2ξ^π.

## Standing in the record

Filed on 2026-10-30 for [CLAIM-488](../claims.d/CLAIM-488.md). Theorem 26 is the converse that claim
waits on, proved for a fixed prior. The uniform version that the claim's
first step needs, deficiency as a maximum over the unknown, needs one more
minimax exchange; the NOTE says what.
