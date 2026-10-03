---
status: Active
status_note: 'read in full 2026-10-03 ([NOTE-tmp9snke](../notes.d/NOTE-tmp9snke.md)), from the authors'' PhilSci-Archive preprint (March 2021); the Physics of Life Reviews version was not seen. Worth reading as the scope critique of the free energy principle: granted its premises the principle is true, but it applies only to "things" already given a Markov-blanket partition, the partition is placed where the model needs it, and relational properties and constitutive self-organization fall outside it. The blanket is a "trick" that lets any thing be modelled as a variational autoencoder. Active inference, as a process theory, presupposes perception and action in the generative model it is handed.'
title: 'The Markov blanket trick: On the scope of the free energy principle and active inference'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the preprint deposited at PhilSci-Archive (eprint 18831,
    deposited 22 March 2021, dated 19 March 2021, submitted version per
    Unpaywall), 52 pp., §§1–5, Figures 1–3 by caption, footnotes 1–20 and
    the references. Equations (1)–(20) were read in the text layer. The
    journal version (Physics of Life Reviews 39:49–72, December 2021) may
    differ and was not seen. `published:` is the PhilSci deposit date, the
    work's first public appearance; Crossref records the journal DOI from 14
    September 2021. Not held in the Anthology of the SOTA: a grep of its
    literature.d for "Raja", "Markov blanket" and the DOI found nothing.
tags:
- philosophy-of-science
- probabilistic-modeling
- individuation
- cognition
- complex-systems
date: '2026-10-03'
published: '2021-03-22'
doi: '10.1016/j.plrev.2021.09.001'
url: 'https://philsci-archive.pitt.edu/18831/'
first_author: 'Raja'
keywords:
- 'free energy principle'
- 'active inference'
- 'Markov blanket'
- 'Markov blanket trick'
- 'nonequilibrium steady state'
- 'generative model'
- 'affordances'
- 'constitutive self-organization'
implementations: []
summary: >-
  Raja, Valluri, Baggs, Chemero & Anderson (2021), Physics of Life Reviews
  39:49–72. Restating the FEP's derivation (Langevin dynamics, NESS,
  Helmholtz decomposition, Markov blanket, variational bound), the authors
  grant that it is true of things so defined. But blankets apply to every
  "thing", not everything (the candle flame is excluded); the partition is
  placed by modelling convenience; relational properties (heading,
  affordances) and constitutive self-organization (a membrane the cell
  makes) fall outside it. The blanket's real role is to supply the
  partition variational Bayes needs. Active inference presupposes
  perception and action in its generative models.
corrects:
- LIT-526
---
<!-- inactive-ok-file: LIT-tmpghan1 LIT-tmpp3m1q — Deferred; Kelso's book and the HKB paper, named because this paper cites them for coupled oscillators described by relative phase, not leaned on -->

# LIT-tmpumhsc: The Markov blanket trick: On the scope of the free energy principle and active inference

Vicente Raja, Dinesh Valluri, Edward Baggs, Anthony Chemero and Michael L.
Anderson (2021), *Physics of Life Reviews* 39:49–72.

The brief's citation (Physics of Life Reviews, 2021, five authors) is
correct.

## Key takeaways

- **True but narrow.** "Given these commitments, we think FEP is true." The
  dispute is over its scope as a principle, not its derivation.
- **Every thing, not everything (§3.1).** FEP's own literature excludes the
  candle flame, which "clearly" is a thing; blankets need boundaries more
  stable than the states they bound, which clouds and groups lack.
- **The partition is placed (§3.2).** Brain, bacillus and coupled pendulums
  get blankets wherever is convenient: for the pendulums the beam is the
  blanket and position and velocity are active and sensory states. Read
  strictly, the formalism makes the "thing" the whole system-plus-environment.
- **What falls outside (§3.3).** Relational properties (taller-than, heading,
  affordances) and constitutive self-organization: a cell's membrane is
  produced by the cell; a beam is not produced by the pendulums. The blanket
  formalism "has no tools to account for" the difference.
- **The trick (§3.5).** Blankets supply exactly the hidden/observed/system
  partition that variational inference needs, so any thing can be modelled
  "as if it were a variational autoencoder"; FEP was built after variational
  free energy was in use, not the other way round.
- **Active inference (§4).** Its generative models (A, B, C matrices) are
  designed by the experimenter; perception of the cue and control of
  movement are assumed, so the theory presupposes what it claims to explain.

## Standing in the record

Filed on 2026-10-03 at the owner's request, in the free-energy part of the
agency batch. No anthology topic holds it. It discusses variational
autoencoders and the reparameterization trick only as analogies for what
the blanket does, and carries no instruction for machine-learning practice.

**Relation to [LIT-526](LIT-526.md): `corrects`.** "Life as we know it" offers autopoiesis
as one of its four marks of the lifelike and claims its simulated soup shows
it: lesioning blanket states makes the structure disperse, so the system
"appear[s] to actively maintain its structural and dynamical integrity".
Raja et al. argue that the blanket formalism cannot represent constitutive
self-organization, a boundary the system itself produces, and say of
Friston 2013's simulations specifically that they "assume the existence of
all the particles from the beginning and, therefore it cannot be said that
their blanket states are the product of the activities of internal states"
(footnote 17). So the claim that the simulation exhibits autopoiesis, in the
sense of a self-produced boundary, is shown not to follow. The correction is
narrow: it is conceptual, it leaves [LIT-526](LIT-526.md)'s lemma standing (Raja et al.
grant the derivation), and [NOTE-421](../notes.d/NOTE-421.md) had rated that claim weak to moderate
(its C6). They also report Biehl et al.'s finding that some blanket
formalizations, Friston 2013 among them, are mathematically inadequate, but
do not develop it.

Where else it bears:

- **The candle flame.** Raja et al. accept [LIT-526](LIT-526.md)'s claim that a flame
  cannot have a blanket and turn it round: the flame is plainly a thing, so a
  principle that excludes it is not a theory of everything. Mossio,
  Saborido & Moreno ([LIT-tmp9gfzl](LIT-tmp9gfzl.md)) grant the flame organizational closure.
- **Bruineberg et al. ([LIT-tmpxq8pk](LIT-tmpxq8pk.md)).** Cited ("see also Bruineberg et al.
  2020") for the same conclusion, that blankets set up a boundary rather than
  find one. The two papers reach it by different routes and do not test each
  other.
- **Coordination dynamics ([LIT-tmpw3fkg](LIT-tmpw3fkg.md)).** The coupled pendulums are
  already "a thing measured by the relative phase between them (Haken et al.
  1985; Kelso 1995)", so a blanket partition adds nothing to their
  explanation but a Bayesian redescription. That is the HKB explanation read
  in this batch through Kelso 2021; the cited originals are [LIT-tmpp3m1q](LIT-tmpp3m1q.md) and
  [LIT-tmpghan1](LIT-tmpghan1.md), both Deferred.
- **Closure of constraints ([LIT-tmpksq6n](LIT-tmpksq6n.md)).** The "constitutive
  self-organization" the authors say blankets miss is what closure of
  constraints is built to describe. The paper cites autopoiesis and
  operational closure (Maturana & Varela, Di Paolo et al. 2017), not
  Montévil & Mossio.
- **Sophisticated Inference ([LIT-tmpe0pw4](LIT-tmpe0pw4.md)).** Its T-maze rat is the kind of
  simulation §4.2 criticises: the generative model is the experimenters'
  rationalisation of the task. Raja et al. analyse a different T-maze paper
  (Hesp et al. 2021) in the same family.
