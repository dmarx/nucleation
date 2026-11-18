---
status: Active
status_note: >-
  skimmed 2026-11-15 ([NOTE-tmp88irq](../notes.d/NOTE-tmp88irq.md)). The paper, arXiv:2611.07071v1
  (82 pp.), was skimmed: the contributions list (pp. 2–3), the §4
  passage on behavioural control and monitorability (p. 19), the opening
  of §6 with Proposition 1 (pp. 24–25) and the matching appendix
  sentence. The lab's summary page, "Shaping and Monitoring Models
  Through Their Internal Representations", Goodfire, The Mechanistic
  Alignment Series, dated November 5, 2026,
  https://www.goodfire.ai/research/mechanistic-shaping, a blog post by
  Satchel Grant and Michael Byun that links the paper, was read in full;
  the five-level hierarchy and the vision results are taken from it.
  Worth reading here as an explicit ladder of readers for a concept
  trained against: in every experiment it stayed readable by some rung,
  and the toy theory says why it regrows along the readout's own core
  directions.
title: 'Shaping & Monitoring Models through their Internal Representations'
version: 1
history:
- version: 1
  date: '2026-11-15'
  note: >-
    Registered and read on 2026-11-15 from the owner's pasted continuation
    of the ChatGPT exchange "Explain String Theory", in A's turn on concept
    erasure and its limits, where A cites a Goodfire "research report"
    dated 2026-11-05. That item is the lab's summary page; the work is the
    arXiv paper of 2026-11-04, filed here as the paper, with the page named
    in the status note. Checked first: no LIT held the arXiv id, the title
    or Goodfire. Citation from the arXiv API and the PDF's first page:
    Thomas Fel, Matthew Kowal, Matt Feiszli, Satchel Grant, Andrew Lee and
    Chris Earls (core contributors), with Fatih Dinc, Vasudev Shyam, Usha
    Bhalla, Leon Bergen, Siddharth Boppana, Ching Fang, Michael Byun,
    Tristan Gallent, Nicholas Wang, Tal Haklay, Dron Hazra, Neehar
    Kondapaneni, Connor Watts, Ryan Panwar, Thomas Dooms, Jack Merullo,
    Atticus Geiger and Ekdeep Singh Lubana, and Thomas McGrath and Owen
    Lewis (equal senior contribution), 26 authors; arXiv cs.LG, v1
    submitted 2026-11-04, which is `published:`. No email was sent to any
    service. Read by a delegated reader; the filer rechecked every
    quotation used against the PDF's text and the page's text.
tags:
- representation-learning
- anthology-candidate
date: '2026-11-15'
published: '2026-11-04'
arxiv: '2611.07071'
first_author: 'Fel'
keywords:
- 'mechanistic shaping'
- 'reliance shaping'
- 'expression shaping'
- 'monitorability'
- 'circumvention'
- 'probes'
- 'regrowth'
- 'product code'
implementations: []
summary: >-
  Fel, Kowal, Feiszli, Grant, Lee, Earls et al. (2026), Goodfire, arXiv
  preprint. Mechanistic shaping penalizes, during training, a model's
  reliance on or expression of a concept found by interpretability tools,
  across vision, sycophancy, reward hacking and harmfulness. Training
  against a probe can break it (0.98 → 0.57 balanced accuracy in the worst
  reward-hacking variant), but a refitted probe recovers the concept
  (0.97–0.98), and in every experiment the concept stayed readable by the
  original, a refitted linear, a nonlinear or another layer's probe. In a
  linear toy theory the concept regrows along the directions the readout
  uses for core features. Bears on [TERM-064](../terms.d/TERM-064.md), [THEORY-281](../theory.d/THEORY-281.md) and [QUESTION-010](../questions.d/QUESTION-010.md).
---
<!-- inactive-ok-file: NOTE-tmp88irq THEORY-tmp2ly83 — Skimmed and Proposed; the reading of this work and the account filed from it -->

# LIT-tmp40uoi: Shaping & Monitoring Models through their Internal Representations

Fel, T., Kowal, M., Feiszli, M., Grant, S., Lee, A., Earls, C., et al. (2026). Shaping & Monitoring Models through their Internal Representations. arXiv:2611.07071. Summary page: Goodfire, "Shaping and Monitoring Models Through Their Internal Representations", 5 November 2026, https://www.goodfire.ai/research/mechanistic-shaping.

## Key takeaways

*From the reading, [NOTE-tmp88irq](../notes.d/NOTE-tmp88irq.md) (paper skimmed, page read).*

- **Monitorability survived** (page): "In all of our experiments, the
  concept being trained against remained monitorable, either with the
  original probe or a retrained one. A few cases required new probes with
  greater expressivity or at different layers."
- **Worst case** (paper, §4, p. 19): "When gradients flow through the
  probe score, its original balanced accuracy falls from 0.98 to 0.57 by
  update 150, whereas the other variants retain 0.87–0.90. Refitting a
  probe recovers 0.97–0.98 in every checkpoint".
- **Linear erasure leaves a nonlinear form** (page): repeated removal of
  the concept's linear form at an intermediate layer "left only a
  nonlinear form of the concept at that layer (L3). Two layers later,
  however, the concept was linearly readable again".
- **Regrowth along the core readout** (§6, Proposition 1): under a fixed
  projection "the ablated component receives no gradient"; a new encoding
  "starts to grow right away" along "the direction the head already uses
  to read the core features", and refits early in the rebuild remove core
  directions, so "accuracy falls close to chance".

## Standing in the record

Filed from A's turn on concept erasure. A says an old probe can stop
detecting a concept while a retrained one detects it, that linear
information can be transformed into a nonlinear encoding, and that in one
reward-hacking experiment the original probe fell from about 0.98 to 0.57
while a retrained linear probe recovered about 0.97–0.98 (paraphrased;
the exchange was not rechecked by the filer). The numbers hold exactly.
The reader's qualifications: 0.57 is the worst variant, when gradients
flowed through the probe, the others keeping 0.87–0.90; the
reward-hacking case is a linear refit (L2), whereas the nonlinear
re-encoding comes from the vision experiments and the toy theory (L3),
where the concept was linearly readable again two layers later, so the
two should not be joined; and A's "research report" of 2026-11-05 is the
summary page of a paper of 2026-11-04. This is a lab's own report of its
own method. [THEORY-tmp2ly83](../theory.d/THEORY-tmp2ly83.md) carries its central account.
