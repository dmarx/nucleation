---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmpruoh7](../notes.d/NOTE-tmpruoh7.md)), from the PubMed Central author manuscript. Worth reading as the argument that Pavlovian prediction, usually modelled as purely model-free, is also model-based. In the "Dead Sea salt" experiment a lever that had predicted a disgusting salt solution became, on first presentation after a novel sodium appetite was induced and before any salt was retasted, nearly as attractive as a sucrose lever, with mesolimbic activation. A cached value cannot do that. The CS must predict the outcome''s identity, and its value must be recomputed against the current bodily state. The paper adds "defocusing" of outcome representations as a model-based route to apparent habit, and argues that dopamine can carry model-based evaluations.'
title: 'Model-based and model-free Pavlovian reward learning: Revaluation, revision, and revelation'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full from the author manuscript in PubMed Central (PMC4074442),
    retrieved as text through NCBI's BioC service. The publisher's version
    is open access on SpringerLink. The PMC text strips the author names
    from most in-text citations and drops the appendix equations (A1)-(A4),
    so cited studies are identified here only where the text names them, and
    the equations are described, not quoted. `published:` is the online
    date Crossref gives (20 March 2014); the print issue is CABN 14(2), June
    2014, pp. 473-492. Not held in the Anthology of the SOTA: a grep of its
    literature.d and theory.d for "Berridge", "Dayan" and the DOI found
    nothing.
tags:
- motivation
- neuroscience
- behavioral-integration
- emotion-and-affect
- cognition
date: '2026-10-03'
published: '2014-03-20'
doi: '10.3758/s13415-014-0277-8'
url: 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4074442/'
first_author: 'Dayan'
keywords:
- 'Pavlovian conditioning'
- 'model-based learning'
- 'model-free learning'
- 'incentive salience'
- 'revaluation'
- 'sodium appetite'
- 'Pavlovian-instrumental transfer'
- 'dopamine'
- 'defocusing'
implementations: []
extends:
- LIT-tmpk0t5p
summary: >-
  Dayan & Berridge (2014), Cognitive, Affective, & Behavioral Neuroscience
  14(2):473-492. Pavlovian prediction is not only model-free. A cue that had
  predicted disgusting salt became instantly "wanted" when a never-experienced
  salt appetite was induced, before the salt was retasted, which needs a
  prediction of the outcome's identity revalued against the current bodily
  state. Over-training may "defocus" outcome representations rather than
  hand control to a model-free system. Dopamine may carry model-based
  evaluations. No algorithm for the revaluation is given.
---
<!-- inactive-ok-file: THEORY-045 — Proposed theories and Deferred seeds, named as accounts this reading bears on; written from the lint report -->

# LIT-tmpmlzuo: Model-based and model-free Pavlovian reward learning: Revaluation, revision, and revelation

Peter Dayan & Kent C. Berridge (2014), *Cognitive, Affective, & Behavioral
Neuroscience* 14(2):473–492 — DOI-10.3758/s13415-014-0277-8

## Key takeaways

- **Pavlovian prediction can be model-based.** In the Dead Sea salt
  experiment, rats learned to turn away from a lever that predicted an
  intensely salty squirt. After drugs mimicking salt deprivation, a state
  they had never been in, the lever on its first re-presentation was
  approached and nibbled nearly as avidly as the sucrose lever. Engagement
  rose more than tenfold, before any salt was tasted. A model-free cache
  would still have held a negative value.
- **The model needs outcome identity and current state.** The cue must
  predict "saltiness", not just "bad", and that prediction must be revalued
  against the present physiological state. The authors call this the most
  basic expression of a model-based mechanism.
- **Defocusing is an alternative to habit.** Persistence of responding after
  devaluation need not mean model-free control. With extended training, the
  predicted outcome's representation may become generalized ("tasty food"),
  and so escape a devaluation that is specific to its identity.
- **Dopamine is not only model-free.** The ventral tegmental area and nucleus
  accumbens were strongly activated by the salt cue only in the new appetite
  state. The authors take this as evidence that dopamine release can reflect
  model-based evaluation, so mesolimbic dopamine is not only a
  temporal-difference teaching signal.

## Standing in the record

Filed on 2026-10-03 at the owner's request, for the record's coverage of
behavioural control and motivation. It carries Daw, Niv and Dayan's
distinction ([LIT-tmpk0t5p](LIT-tmpk0t5p.md)) from instrumental action to Pavlovian
prediction. That is why it declares `extends`. The paper takes the
model-based/model-free distinction and its uncertainty-based arbitration
from that work. It also reinterprets that paper's account of incentive
learning: the instrumental model-based system knows the new value but is
uncertain about it, because the state is novel. The paper builds on that
framework throughout and could not stand without it.

**The boundary.** The paper is about how brains predict reward and how
bodily state transforms motivation. Its computational content (temporal
difference learning, the κ transformation, model-based evaluation) explains
rats and dopamine, and it gives no instruction for machine-learning
practice. It belongs here.

What it adds to the record:

- **Value is computed against the body's current state.** This bears on the
  record's account of felt affect, [THEORY-045](../theory.d/THEORY-045.md), which holds that affect
  reports the body's regulatory state. Here the bodily state enters the
  computation of a cue's incentive value directly and instantly, without
  new experience of the outcome. The paper does not discuss felt affect.
  But its "liking" reactions to the cue itself (conditioned alliesthesia)
  are an affective response that follows the state.
- **Wanting and liking are separable.** The paper's incentive salience is
  "wanting", a motivational attribution distinct from hedonic "liking".
  Ainslie's précis ([LIT-tmpne8q4](LIT-tmpne8q4.md)) uses Berridge and Robinson's
  wanting-without-liking for its own model of urges, but rejects reading
  them as conditioned. This paper defends Pavlovian prediction as a distinct
  process with its own model-based form, so the two disagree on that point.

No instruction for machine-learning practice; nothing here belongs in the
anthology.
