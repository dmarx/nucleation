---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmpqbs2w](../notes.d/NOTE-tmpqbs2w.md)); worth reading as the model that reinterprets the readiness potential. A leaky stochastic accumulator with a weak constant input ("urgency"), fitted with three parameters to 14 participants'' waiting times in Libet''s task, reproduces the shape of the averaged readiness potential (r² = 0.96) because averaging epochs time-locked to threshold crossings recovers the noise that happened to carry the accumulator there. Its prediction, that fast responses to unpredictable clicks are preceded by a slow negativity, was confirmed (13 participants). On this account the "neural decision to move now" is the threshold crossing about 150 ms before movement, not the onset of the readiness potential, and Libet''s inference that the brain decides before awareness is "unfounded". The authors say plainly that this shows the readiness potential could reflect spontaneous fluctuation, not that it does.'
title: 'An Accumulator Model for Spontaneous Neural Activity Prior to Self-Initiated Movement'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from PubMed Central (PMC3479453,
    https://pmc.ncbi.nlm.nih.gov/articles/PMC3479453/), the PNAS Plus
    article: introduction, model, prediction, results, discussion,
    materials and methods, the figure captions and the reference list.
    Equation 1 is an image in the PMC page and was read from it. The
    supporting information (Figs. S1–S5) was not reachable (the PMC file
    link returned a challenge page) and was not read; claims the text
    makes from it are taken as stated. Crossref confirms title, authors,
    PNAS 109(42), issue date 16 October 2012, and DOI; it gives first
    online publication as 6 August 2012, which is `published:`. The
    article begins at E2904 (from the PMC supplementary file name);
    Crossref gives no page range, and the end page was not verified. Not held in the Anthology of the SOTA: a
    grep of its record for "Schurger", "readiness potential" and the DOI
    found nothing.
tags:
- free-will
- agency
- neuroscience
- behavioral-integration
- consciousness
date: '2026-10-03'
published: '2012-08-06'
doi: '10.1073/pnas.1210467109'
url: 'https://pmc.ncbi.nlm.nih.gov/articles/PMC3479453/'
first_author: 'Schurger'
keywords:
- 'readiness potential'
- 'self-initiated movement'
- 'volition'
- 'leaky stochastic accumulator'
- 'spontaneous neural fluctuations'
- 'Libet'
- 'resting state'
- 'autocorrelation'
- 'power-law'
extends:
- LIT-tmp2p2lh
implementations: []
summary: >-
  Schurger, Sitt & Dehaene (2012), PNAS 109(42). In Libet's spontaneous
  movement task, a leaky stochastic accumulator, δx = (I − kx)Δt + cξ√Δt,
  with weak constant urgency I and a threshold, fitted only to waiting
  times, reproduces the averaged readiness potential (r² = 0.96): time-locking
  to threshold crossings averages up the autocorrelated noise that
  produced them. Fast responses to random interruptions were preceded by a
  slow negativity, as predicted. The "neural decision to move now" is the
  late threshold crossing, about 150 ms before movement, so Libet's
  inference of an unconscious decision a half-second earlier is unfounded.
---

<!-- inactive-ok-file: THEORY-029 — Proposed; named to say this reading does not bear on it -->
<!-- inactive-ok-file: THEORY-040 — Proposed; named to say this reading does not bear on it -->

# LIT-tmpzrigj: An Accumulator Model for Spontaneous Neural Activity Prior to Self-Initiated Movement

Aaron Schurger, Jacobo D. Sitt and Stanislas Dehaene (2012), *Proceedings of the National Academy of Sciences* 109(42):E2904ff. — DOI-10.1073/pnas.1210467109

## Key takeaways

- The readiness potential that precedes self-initiated movements need not be the signature of planning. If the decision to move is a threshold crossing by a leaky accumulator driven mostly by ongoing noise, then averaging brain activity time-locked to the movement recovers a slow, exponential-looking buildup, because only the epochs that ended in a crossing are averaged. The buildup's causal role is "incidental".
- The model was fitted to behaviour only (waiting times in Libet's task, three parameters: urgency 0.11, leak 0.5, threshold at the 80th percentile), and with those parameters it fitted the readiness potential from −3 to −0.15 s (r² = 0.96). Its new prediction was tested and held: when participants were interrupted by a click at random, their fastest responses were preceded by a slow negative deflection beginning before the click, which the planning account does not predict.
- It relocates the decision. The "neural decision to move now" is the threshold crossing, about 150 ms before the button press, which coincides with the lateralised readiness potential and with participants' reported time of the urge (−152 ms here). So the conclusion that the brain decides to move well before the person is aware of deciding does not follow from the readiness potential.

## Standing in the record

Filed on 2026-10-03 at the owner's request, for the Libet readiness-potential
debate and its use against free will. It extends Usher and McClelland
([LIT-tmp2p2lh](LIT-tmp2p2lh.md)): its model is the leaky stochastic accumulator of that paper
(their reference 27), taken as a single unit with no competitor and fed with a
constant urgency plus noise, and the paper cannot stand without it. Its
evidence-accumulation framing is the one the other filings of the batch state:
Ratcliff and McKoon ([LIT-tmpcmcw7](LIT-tmpcmcw7.md)) for the diffusion model whose mean–SD
property it checks, and Bogacz et al. ([LIT-tmp93b13](LIT-tmp93b13.md)) for the regimes of the
leaky process.

What it bears on in the record:

- **Dennett and Kinsbourne ([LIT-431](LIT-431.md)).** The record's only other treatment of
  Libet. They argue that the timing of the reported intention is an artefact
  of confusing the time a content is represented with the time it represents.
  Schurger et al. attack a different premise, the timing of the neural
  decision, and reach a compatible conclusion: the gap between brain and
  awareness that Libet reported is not evidence that action is initiated
  unconsciously. The two critiques are independent, and the record now holds
  both. Schurger et al. set aside the clock method for the urge as "irrelevant
  to this experiment" (they note it has been criticised), so they do not
  depend on Dennett and Kinsbourne, nor answer them.
- **Free will ([THEORY-029](../theory.d/THEORY-029.md), [THEORY-040](../theory.d/THEORY-040.md)).** The record's free-will theories are
  about compatibilist conditions on ownership and manipulation. Neither rests
  on the Libet argument, so this paper neither supports nor tests them. What
  it removes is an empirical premise sometimes used against conscious will,
  that a neural decision precedes awareness by half a second or more. It does
  not show that the conscious urge causes the movement; the model is "silent
  with respect to the urge to move".
- **Agency.** Its picture of agency is specific: a task goal sets the
  baseline near threshold, and the exact moment of acting is left to
  spontaneous fluctuation. "The precise moment is not directly decided by a
  goal-directed operation."

No instruction for machine-learning practice; nothing here belongs in the
anthology.
