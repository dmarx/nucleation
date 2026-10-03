---
status: Active
status_note: 'read 2026-10-03 ([NOTE-tmpo6f5g](../notes.d/NOTE-tmpo6f5g.md)), main text and Appendix B in full, Appendix A (the derivations) by section only; worth reading as the paper that puts the two-choice decision models in one frame and ties them to the sequential probability ratio test. The pure drift diffusion model is the continuum limit of the SPRT, so it is the fastest for a given accuracy and the most accurate for a given time. Of six models, all but the race model reduce to it in some parameter range: the Usher–McClelland mutual inhibition model when leak equals inhibition and both are large, the feedforward inhibition model when its inhibitory and excitatory weights are equal. Each reward criterion has a unique optimal threshold, which gives testable optimal performance curves. The optimality results hold for the pure model with stationary evidence and two alternatives.'
title: 'The Physics of Optimal Decision Making: A Formal Analysis of Models of Performance in Two-Alternative Forced-Choice Tasks'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read from the published PDF posted on co-author Jeff Moehlis's UCSB
    page (https://sites.me.ucsb.edu/~moehlis/moehlis_papers/psych.pdf, 66
    pages, Psychological Review 113(4):700–765 with the APA copyright
    line). The main text (pp. 700–753) and Appendix B (experimental
    methods) were read in full through the PDF text layer. Appendix A, the
    mathematical derivations, was read only as far as its section titles,
    so its proofs are taken as the main text states them. Many displayed
    equations lose symbols in the text layer; those quoted below were
    checked against the surrounding prose. Crossref confirms title,
    authors, volume, issue, pages and DOI and gives the year only;
    `published:` is the first of October 2006, the issue month ERIC
    records. Not held in the Anthology of the SOTA: a grep of its record
    for "Bogacz", "physics of optimal decision" and the DOI found nothing.
tags:
- behavioral-integration
- cognition
- neuroscience
- probabilistic-modeling
date: '2026-10-03'
published: '2006-10-01'
doi: '10.1037/0033-295X.113.4.700'
url: 'https://sites.me.ucsb.edu/~moehlis/moehlis_papers/psych.pdf'
first_author: 'Bogacz'
keywords:
- 'drift diffusion model'
- 'sequential probability ratio test'
- 'optimal decision making'
- 'reward rate'
- 'speed-accuracy trade-off'
- 'mutual inhibition'
- 'Ornstein-Uhlenbeck model'
- 'optimal performance curve'
- 'two-alternative forced choice'
extends:
- LIT-tmp2p2lh
implementations: []
summary: >-
  Bogacz, Brown, Moehlis, Holmes & Cohen (2006), Psychological Review
  113(4):700–765. The pure drift diffusion model implements the SPRT and
  Neyman–Pearson test, so it is the optimal two-choice decision process.
  The O-U, mutual inhibition (Usher–McClelland), feedforward inhibition and
  pooled inhibition (Wang) models reduce to it for balanced parameters; the
  race model does not. For reward rate, Bayes risk and two accuracy-weighted
  criteria there is a unique optimal threshold, giving parameter-free
  optimal performance curves. With biased priors the optimal starting point
  is proportional to the log prior odds.
---

<!-- inactive-ok-file: THEORY-056 — Proposed; named only as the nearest theory of competing states, with no relation claimed -->

# LIT-tmp93b13: The Physics of Optimal Decision Making: A Formal Analysis of Models of Performance in Two-Alternative Forced-Choice Tasks

Rafal Bogacz, Eric Brown, Jeff Moehlis, Philip Holmes and Jonathan D. Cohen (2006), *Psychological Review* 113(4):700–765 — DOI-10.1037/0033-295X.113.4.700

## Key takeaways

- The sequential probability ratio test (SPRT) of Barnard and Wald is the fastest test for a given error rate, and its continuum limit is the pure drift diffusion model (DDM). So the DDM is the optimal two-choice decision process, both in free response (fastest for fixed accuracy) and under interrogation (most accurate at a fixed time).
- Biologically motivated models are optimal exactly when they reduce to the DDM. In the Usher–McClelland mutual inhibition model the difference between the two units is an Ornstein–Uhlenbeck process with λ = w − k. With leak equal to inhibition it is a diffusion process, and with both large, activity collapses fast onto a "decision line", so the two-dimensional model behaves like the one-dimensional DDM. The feedforward inhibition model is exactly the DDM when inhibition equals excitation. Wang's pooled inhibition model reduces to mutual inhibition when inhibitory neurons are fast. The race model never reduces.
- How cautious a decider should be is itself optimisable. For reward rate there is a unique optimal threshold, which depends on the delays only through their sum, and the resulting relation between error rate and normalised decision time is parameter-free: decision time peaks at about 20% of the inter-decision interval, at an error rate of about 18%. With unequal priors the optimal starting point is proportional to the log prior odds, which matches the prestimulus LIP activity reported by Platt and Glimcher.

## Standing in the record

Filed on 2026-10-03 at the owner's request, as the paper in the batch that
relates the models to each other and to the SPRT. It extends Usher and
McClelland ([LIT-tmp2p2lh](LIT-tmp2p2lh.md)): it takes their leaky, competing accumulator,
linearised as the "mutual inhibition model", and proves analytically what they
showed by simulation, namely that the difference of the two accumulators is an
Ornstein–Uhlenbeck process that becomes the diffusion model when leak equals
inhibition. It adds what they lacked: the balanced model is optimal only if
leak and inhibition are also large, and then it is optimal by every reward
criterion it considers. It also answers one of their arguments. Usher and
McClelland cited people's imperfect accuracy at long times as a challenge to
the DDM; Bogacz et al. reply (footnote 10) that Ratcliff's 1988 bounded
diffusion explains it. They state but do not develop that reply, so it is not
declared as a correction.

Ratcliff and McKoon ([LIT-tmpcmcw7](LIT-tmpcmcw7.md)), writing later, object that this paper's
account of threshold setting cannot explain humans who calibrate from verbal
instructions or without feedback.

For the record, this is the formal sense in which "integration" is a word
about optimality and not only about mechanism. A system that compares
evidence for competing options by accumulating the difference is doing
statistically the best that can be done, and the paper's last section
recasts cognitive control as the tuning of drift, starting point and threshold
to maximise a utility function. That gives `behavioral-integration` a
normative standard. It does not give a theory of how an organism's many
systems are integrated: the analysis is of one decision between two options.
Its multi-alternative extension (the MSPRT, which Bogacz and Gurney map onto
cortex–basal ganglia circuits) is pointed to, not developed.

It is not a model of emotion or motive, and it does not bear on the record's
theory of competing motive states ([THEORY-056](../theory.d/THEORY-056.md)) beyond the formal analogy noted
for [LIT-tmp2p2lh](LIT-tmp2p2lh.md). No instruction for machine-learning practice; nothing here
belongs in the anthology.
