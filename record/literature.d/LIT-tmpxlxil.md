---
status: Active
status_note: 'read 2026-10-09 (NOTE-tmp2x9ot); worth reading here as the paper that makes guidance a combination of two scores from one network: train with the condition dropped at random, then sample with (1 + w)ε(z, c) − wε(z), extrapolating away from the unconditional estimate. Its own analysis is the point for this record: the combination is inspired by Bayes'' rule (an implicit classifier p(c|z) ∝ p(z|c)/p(z)) but, because learned scores need not be gradients of anything, it is in general the score of no density and the gradient of no classifier. The evidence is one proof-of-concept on class-conditional ImageNet: the guidance weight trades FID against Inception score as classifier guidance does, best FID at w = 0.1–0.3, best IS at w ≥ 4.'
title: 'Classifier-Free Diffusion Guidance'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 (NOTE-tmp2x9ot) from arXiv v1 (26 July
    2022, the only version, 14 pages): every section, both tables and the
    sample figures. Details checked against arXiv (title, the two
    authors, v1 date; the comment says a short version appeared at the
    NeurIPS 2021 Workshop on Deep Generative Models and Downstream
    Applications). `published:` is the arXiv v1 date. Held in the
    Anthology of the SOTA as ANTH-LIT-693 (clone of 2026-10-09, commit
    d8b5ba5), read there for what the guidance weight does to sample
    quality metrics; filed here as well under ADR-013 for this record's
    question.
tags:
- probabilistic-modeling
- compositionality
date: '2026-10-09'
published: '2022-07-26'
arxiv: '2207.12598'
first_author: 'Ho'
keywords:
- 'classifier-free guidance'
- 'diffusion models'
- 'conditional generation'
- 'implicit classifier'
- 'fidelity–diversity trade-off'
implementations: []
summary: >-
  Ho & Salimans (2022). One diffusion network learns both the conditional
  and the unconditional score by dropping the condition during training;
  sampling with (1 + w)ε(z, c) − wε(z) reproduces the FID/Inception-score
  trade-off of classifier guidance on ImageNet without any classifier.
  The combination is motivated by an implicit Bayes classifier, but the
  paper itself shows that learned scores need not be conservative, so the
  guided field is in general the score of no density.
---

# LIT-tmpxlxil: Classifier-Free Diffusion Guidance

Jonathan Ho and Tim Salimans (2022), *arXiv preprint* (short version at the
NeurIPS 2021 Workshop on Deep Generative Models and Downstream
Applications) — [ARXIV-2207.12598](https://arxiv.org/abs/2207.12598)

## Key takeaways

- **The method** (Section 3.2, Algorithms 1–2). Train one network on
  ε(z_λ, c) and, with probability p_uncond, on the null token, so that
  ε(z_λ) = ε(z_λ, ∅) is learned too. Sample with
  ε̃(z_λ, c) = (1 + w)ε(z_λ, c) − wε(z_λ). Two forward passes per step; no
  classifier, no classifier gradients.
- **What it is modelled on, and what it is not** (Section 3). Classifier
  guidance samples approximately from p̃(z|c) ∝ p(z|c)p(c|z)^w. With exact
  scores, ε* differences give the gradient of an implicit classifier
  p_i(c|z) ∝ p(z|c)/p(z), and guiding with it gives the same formula. But
  the learned ε are unconstrained networks, not conservative fields, so
  ε̃ "is not in general the (scaled) gradient of any classifier", and no
  scalar potential need exist for it. The tilted density is the
  motivation, not a guarantee about what is sampled.
- **The evidence** (Section 4, Tables 1–2). Class-conditional ImageNet at
  64×64 and 128×128, with architectures and hyperparameters tuned for
  classifier guidance and used unchanged. Raising w trades FID against
  Inception score monotonically: at 64×64 with p_uncond = 0.1, FID 1.55
  at w = 0.1 rising to 26.22 at w = 4, while IS rises from 66.1 to 260.2.
  At 128×128, w = 0.3 gives FID 2.43 at T = 256, below ADM-G's 2.97; at
  equal network evaluations (T = 128) it does worse. p_uncond = 0.5 is
  worse than 0.1 or 0.2 along the whole frontier.
- **Its explanation of guidance** (Section 5): guidance raises the
  conditional likelihood of the sample while lowering its unconditional
  likelihood, the second through a negative score term. Strong guidance
  saturates colours and cuts diversity, which the authors flag as a
  possible harm.

The reading (NOTE-tmp2x9ot) notes that the text says FID is
"monotonically decreasing" with w while its tables show it rising; the
anthology's entry (ANTH-LIT-693) flags the same sentence.

## Standing in the record

Filed on 2026-10-09 from the manuscript bibliography of 2026-10-09 (work
`what-survives-translation`) at the owner's request: the manuscript
considered it and dropped it from the final reference list. It is read here
on its own merits. See the curation entry of that day.

It is also held in the Anthology of the SOTA as ANTH-LIT-693, read there
for the guidance weight as a practice and for what it does to FID and
Inception score. The second question here, per ADR-013, is the reading on
this record's terms: what the combination of scores is as a probabilistic
object. That is the one-term case of the score addition by which Composable
Diffusion (LIT-770) composes concepts, and the paper's own
non-conservativeness argument applies to that sum as well
(NOTE-tmp2x9ot).
