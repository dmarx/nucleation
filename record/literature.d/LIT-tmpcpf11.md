---
status: Active
status_note: 'read in full 2026-09-30 ([NOTE-tmpp9572](../notes.d/NOTE-tmpp9572.md)); worth reading as the founding psychophysics paper of signal detection theory: it is short, it is the first place d′ is named, and it is the first to put the observer on the ROC and to set the likelihood-ratio criterion β from priors and payoffs. For the ideal-observer mathematics it defers entirely to Peterson and Birdsall (1953), and its experiment is small (three observers) with some statistics asserted rather than shown.'
title: 'A decision-making theory of visual detection'
version: 2
history:
- version: 2
  date: '2026-09-30'
  note: >-
    Read in full (Full text, Psychological Review 61(6):401–409, from the
    Internet Archive's open microfilm scan of the whole November 1954 issue
    (item sim_psychological-review_1954-11_61_6; not a lending item). All 9
    pages read: text, all 16 figures and captions, equations [1]–[3],
    conclusions (a)–(f), both references and footnote 1. The OCR text layer
    was read in full, and pp. 404–406 and 408 were rendered to images to
    check the equations, the figures and the one garbled significance
    statement. Nothing was skipped. Copyright: The Online Books Page's
    serial record for Psychological Review says the first copyright-renewed
    issue is January 1963 (v. 70 no. 1) and that it knows of no renewed
    contributions, so this 1954 issue is in the US public domain. The paper
    prints "Vol. 61, No. 6, 1954" but no month; `published:` uses 1 November
    1954 because the Internet Archive dates issue 6 to 1954-11. The paper
    was received 29 October 1953. No existing entry in the Anthology of the
    SOTA (grep of its literature.d for the DOI, "Tanner", "signal detection"
    and "receiver operating": no hits). A DTIC copy of the related 1955
    technical report "The evidence for a decision-making theory of visual
    detection" (AD0064143) was tried first, but DTIC returned a block page
    and then a maintenance page. That report is a different, longer work and
    was not read.); the first NOTE on it, since it was seeded from the
    abstract alone. Status set from the reading: Active.
tags:
- cognition
- probabilistic-modeling
- neuroscience
date: '2026-09-30'
published: '1954-11-01'
doi: '10.1037/h0058700'
url: 'https://archive.org/details/sim_psychological-review_1954-11_61_6'
first_author: 'Tanner'
keywords:
- 'signal detection theory'
implementations: []
summary: >-
  Tanner & Swets (1954), DOI-10.1037/h0058700. Tanner and Swets model
  visual detection as testing a statistical hypothesis. The observer
  compares one sample of neural activity with a cutoff, and signal+noise
  and noise are Gaussian with equal variance, separated by d′ (the mean
  difference in noise-SD units, defined as the square root of Peterson and
  Birdsall's d). The cutoff moves along a curve of P_SN(A) against P_N(A)
  (the curve now called the ROC; for d′ = 1 it passes through (.16, .50),
  (.50, .84) and (.84, .98)). The optimal operating point is where the
  slope equals β = [(1−P(SN))/P(SN)]·[(V_N·CA+K_N·A)/(V_SN·A+K_SN·CA)].
  The 4AFC prediction is P(C)=∫F(x)³g(x)dx. With three paid observers, d′
  estimated from yes-no data predicted 4AFC accuracy. The "false alarms
  are guesses" (high-threshold) hypothesis is rejected: false-alarm rate
  correlated with chance-corrected thresholds (ρ = .30, .71, .67; combined
  p ≪ .001), and all 12 fitted yes-no scatter lines miss the point (1, 1).
---

# LIT-tmpcpf11: A decision-making theory of visual detection

Tanner & Swets (1954), *Psychological Review 61(6):401–409 (1954). Crossref (DOI 10.1037/h0058700) confirms title, authors, volume, issue and pages. Work done for the U.S. Army Signal Corps (Contract DA-36-039 sc-15358) at the University of Michigan Vision Research Laboratories.* — DOI-10.1037/h0058700

## Standing in the record

Filed on 2026-09-30 at the owner's request, as one of the sources registered to cover signal detection theory,
which the record lacked; its only detection-theory entry, Van Trees 1968 ([LIT-351](LIT-351.md)), is unreachable.
`published:` is the first appearance ([ADR-002](../decisions.d/ADR-002.md)).

It was filed `Deferred`, unread. [NOTE-tmpp9572](../notes.d/NOTE-tmpp9572.md) is the close reading of 2026-09-30, and it placed the work: **Active** — worth reading as the founding psychophysics paper of signal detection theory: it is short, it is the first place d′ is named, and it is the first to put the observer on the ROC and to set the likelihood-ratio criterion β from priors and payoffs. For the ideal-observer mathematics it defers entirely to Peterson and Birdsall (1953), and its experiment is small (three observers) with some statistics asserted rather than shown.
