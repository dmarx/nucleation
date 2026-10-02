---
number: 365
status: Read
formerly:
- NOTE-tmpxik42
paper: LIT-445
title: 'Integrated Information Theory 3.0'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full except the equations: the publisher's CC BY text from
    PubMed Central (PMC4014402), fetched as full-text XML from Europe PMC
    and converted to plain text. The equations in that text are images and
    were not viewed, so quantities are read from the prose definitions,
    Table 1 and Box 1. I read every section, all 22 figure captions (not
    the figure images) and Supporting Text S1 from the PLOS site. Text S2,
    the supplementary methods with the calculation details, and Text S3
    were not read. The exclusion passages were read closely and are quoted
    below. Schwitzgebel's paper was not re-read; what he argues is taken
    from NOTE-131 and NOTE-188.
date: '2026-10-02'
summary: >-
  The 2014 restatement of IIT. Five axioms of experience become five
  postulates about mechanisms in a state, and an experience is identified
  with the maximally irreducible conceptual structure of a complex.
  Exclusion is the anti-nesting rule: of all overlapping sets of elements,
  only the one with locally maximal Φ is conscious, so no subset or
  superset of a complex is. It is postulated from the axiom that
  experience has definite borders; Occam's razor is invoked only for
  exclusion within a mechanism. Logic-gate examples give minor complexes,
  a conscious inactive network, a minimally conscious photodiode and a
  feed-forward zombie. Nothing larger than about a dozen elements is
  computable.
---
<!-- inactive-ok-file: LIT-429 — Deferred, no lawful full text; named as the book whose agents fall under this paper's verdict, not leaned on for its content -->

# NOTE-365: Integrated Information Theory 3.0

## Contribution

IIT 3.0 sets out the theory's axioms and postulates explicitly and applies
each postulate twice, once to single mechanisms and once to systems of
mechanisms. Text S1 lists the changes from IIT 2.0. Information becomes "a
difference that makes a difference", requiring both causes and effects
within the system. The elements are mechanisms in a state, not
connections. A complex is found by partitioning its whole conceptual
structure, not only its top-order concept. The distance used is the earth
mover's distance, not KL divergence. And, item 8, "the exclusion postulate
is applied not only to systems of mechanisms but also to causes and
effects specified by individual mechanisms". The result is a definite
recipe that, for a small discrete system with a known transition
probability matrix, says which sets of elements are conscious, how much,
and with what quality.

## Key insight

Consciousness is a property of whichever set of elements is *most*
irreducible, judged against every set it overlaps. A set of elements has a
whole-level causal structure that partitioning destroys, measured by Φ. Of
any family of overlapping sets, only the one at a local maximum of Φ
"exists intrinsically". So the boundary of a conscious entity is fixed by
competition between overlapping candidates. A conscious system can have no
conscious parts and be part of no conscious whole, because its parts and
its wholes are exactly the sets it beats or loses to.

## Assumptions

- **The axioms are self-evident** and "do not need proof". The exclusion
  axiom reads: "each experience excludes all others – at any given time
  there is only one experience having its full content, rather than a
  superposition of multiple partial experiences; each experience has
  definite borders …; each experience has a particular spatial and
  temporal grain."
- **The postulates are "unproven assumption[s]"** about physical
  substrates, chosen to mirror the axioms. The paper's definition of
  "postulate" says so.
- **The identity**: the MICS of a complex "is identical to its experience".
  It is asserted, not derived.
- **The setting.** Systems are discrete in time and state, with a known
  transition probability matrix (TPM) obtained by perturbing the system
  into all its states. Elements outside the candidate set are background
  conditions, fixed at their actual values (Text S1, item 9).
- **The grain.** The examples assume that the binary elements and unit time
  steps are the grain at which Φ peaks. The theory says the grain should be
  searched over as well (refs 20, Hoel et al. 2013).
- **The distance** is the earth mover's distance, called "the current
  distance measure of choice". The extended EMD between constellations is
  defined in Text S2, which was not read.

## Key results

All results are either definitions or are computed on small logic-gate
networks with the authors' software. Nothing is computed for a brain.

- **Exclusion within a mechanism (Fig. 8, Fig. S1).** A mechanism's "core
  cause" is the purview with maximal φ, and "other causes and effects are
  excluded". The motivation is an infinite regress: strong synapses, plus
  weak synapses, plus stray glutamate receptors, plus cosmic rays. The
  exclusion postulate "represents a causal version of Occam's razor,
  saying in essence that 'causes should not be multiplied beyond
  necessity', i.e. that causal superposition is not allowed". Only the most
  irreducible cause is kept, because "something exists all the more, the
  more of a difference it makes". Ties go to the larger purview (Fig. S1
  caption). "Exclusion does not apply across mechanisms within a set of
  elements."
- **Exclusion between systems (Fig. 14).** "Of all overlapping sets of
  elements, only one set can be conscious." A complex is "a local maximum
  of integrated conceptual information ΦMax (meaning that it has maximal Φ
  as compared to all overlapping sets of elements)". "Because of
  exclusion, complexes cannot overlap and at each point in time, an
  element/mechanism can belong to one complex only." In the example, ABC is
  the complex, so "no subset or superset of ABC can form another complex".
  No separate argument is given for this level beyond the axiom. The
  Occam's-razor passage is attached to the mechanism level. No tie rule is
  stated for systems.
- **Integration requires two-way causation (Figs. 5, 7, 13).** An element
  with inputs but no outputs to the set, or the reverse, contributes no
  intrinsic information. A set is a whole only if every subset has both
  causes and effects in the rest. A one-way connected subset is an
  "appendix", like a minute-taker who cannot answer back to the board.
- **Condensation (Fig. 16).** A larger network condenses into a major
  complex ABC, a minor complex DE and an isolated minor complex FG. ABCDE
  is integrated but "excluded from forming a complex, since it overlaps
  with ABC". Extrapolated, not computed: the human brain has a dynamic main
  cortical complex and many "minimally conscious" minor complexes. After
  split-brain surgery there are two main complexes. Some unconscious
  semantic processing may be "paraconscious" minor complexes.
- **Architecture (Fig. 17).** A modular network of three COPY–AND pairs is
  not one complex but three, "each generat[ing] more Φ than the whole
  system". A homogeneous all-to-all network of OR gates has low Φ. A
  specialised network of majority gates has high Φ. The cerebellum and
  slow-wave sleep are offered as the neural analogues.
- **Inactive systems (Fig. 18).** Four COPY gates all off form a complex. An
  inactive but responsive main complex would be conscious, and no
  "broadcast" or "ignition" is needed.
- **Minimally conscious photodiode (Fig. 19).** A detector and a predictor
  feeding back to each other form a complex with ΦMax = 1 and two
  concepts. A thermistor with the same internal mechanism has the same
  experience.
- **Feed-forward zombies (Figs. 20–21).** A purely feed-forward system has
  no complex, by recursion on its input and output layers. A recurrent
  network (ΦMax = 0.76, 17 concepts in the depicted state) is matched over
  at least four time steps by an unfolded feed-forward network with no
  complex. "Whether a system is conscious or not cannot be decided based on
  its input-output behavior only."
- **Self-referential concepts (Fig. 22).** In a ten-element segment/dot
  network, every concept's purview lies inside the complex. Concepts are
  "self-generated, self-referential, and holistic", and experience is "an
  'awake dream' selected by the environment".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Experience is identical to the MICS of a complex; ΦMax is its quantity and the constellation's shape its quality | assertion (the central identity) | stated as an identity; motivated by the axiom–postulate parallel |
| C2 | Of all overlapping sets of elements only the local maximum of Φ is conscious: no subset or superset of a complex is conscious | postulate | the exclusion axiom ("definite borders", one experience at a time); no argument specific to the system level |
| C3 | A mechanism has exactly one cause and one effect, the maximally irreducible | postulate with an informal argument | infinite-regress example and "causal Occam's razor" (Fig. S1) |
| C4 | A system can condense into one major and several non-overlapping minor complexes; the brain has a main complex plus paraconscious minor ones | strong for the toy network (Fig. 16); assertion for the brain | computed example; neural extrapolation |
| C5 | Modular networks split into small complexes, which may explain why the cerebellum does not contribute to consciousness | moderate for the toy; suggestive for the cerebellum | Fig. 17 computation; anatomical analogy |
| C6 | Inactive but responsive systems can be conscious | strong within the formalism | Fig. 18 computation |
| C7 | Feed-forward systems are never conscious, and a conscious system can have an unconscious functional equivalent | strong within the formalism | recursion argument; Fig. 21 computation |
| C8 | Integrated architectures are favoured by evolution and are "autonomous, since [they] can act and react based on [their] internal states and goals" | assertion | listed benefits, no analysis |
| C9 | Ant colonies, octopuses and computers have definite IIT answers that are "in principle testable" | assertion | none; computing them is "not practically feasible" |

## Concepts

- **Mechanism** — "anything having a causal role within a system", for
  example a neuron or a logic gate, including higher-order combinations.
- **Cause-effect repertoire; cei** — the distributions over past and
  future states a mechanism in a state constrains; cause–effect
  information is the smaller of the two distances from the unconstrained
  repertoire.
- **φ (small phi)** — how far a mechanism's cause–effect repertoire is from
  that of its minimum information partition.
- **Concept (core concept)** — a mechanism with its maximally irreducible
  cause–effect repertoire (MICE), weighted by φMax.
- **Φ (big phi)** — how far a set's constellation of concepts is from that
  of its unidirectional minimum information partition.
- **Complex** — a set of elements at a local maximum of Φ against all
  overlapping sets. "Only a complex exists as an entity from its own
  intrinsic perspective."
- **MICS, quale sensu lato** — the constellation of concepts a complex
  specifies, identified with its experience.
- **Major and minor complexes; paraconscious** — non-overlapping complexes
  of high and low ΦMax in one system; a minor complex is "conscious 'on
  the side'".
- **Background conditions** — elements outside the candidate set, held at
  their actual states.

## Connections

- **Schwitzgebel ([LIT-159](../literature.d/LIT-159.md), [NOTE-131](NOTE-131.md); book version [LIT-216](../literature.d/LIT-216.md), [NOTE-188](NOTE-188.md)).**
  [NOTE-131](NOTE-131.md) records that the 2014 manuscript's §2 cites this paper with
  Tononi 2008–2012 and Tononi & Koch 2014. What it attacks matches this
  paper's system-level exclusion. The strict local-maximum comparison is
  what makes the one-ballot threshold sharp, and the "local maximum
  against all overlapping sets" wording does nothing to soften it. But the
  defence Schwitzgebel attributes to Tononi, Occam's razor plus the
  absurdity of a two-person group consciousness, is not this paper's
  system-level defence. Here Occam's razor appears only at the mechanism
  level, and groups of people are not discussed. [NOTE-131](NOTE-131.md) sources the
  threshold passage to Tononi 2010 (n. 9) and Tononi & Koch 2014 (n. xii);
  which Tononi text supplies the two-person example it does not say. The grain
  clause here ("the macro may emerge over the micro") is the hook the book
  version later uses, via this paper's ref. 20, to argue that a polity
  could out-integrate its citizens.
- **The IIT line in the record.** [LIT-185](../literature.d/LIT-185.md) ([NOTE-122](NOTE-122.md)) reads IIT 4.0, which
  keeps exclusion as one of six axioms. It turns this paper's
  non-overlapping complexes into a gapless "tiling" of space-time by
  non-overlapping substrates. That sharpens the anti-nesting reading
  without changing it, and [NOTE-122](NOTE-122.md) notes that it does not engage
  Schwitzgebel either. This paper's own limitations (discrete states, full
  TPM, a dozen elements, grain assumed) are the ones [LIT-185](../literature.d/LIT-185.md) presses in
  their later form.
- **Putnam.** Not cited. The system-level postulate does formally what
  Putnam's stipulation did by fiat: it rules out a pain-feeler with
  pain-feeling parts. The difference is that here which level wins is
  decided by a quantity, Φ. Putnam's stipulation says only that whole and
  part cannot both feel pain, and his stated motive, ruling out swarms of
  bees ([NOTE-131](NOTE-131.md)), favours the parts.
- **Group agency.** The paper says nothing about groups of people. Its
  zombie result is what lets an IIT theorist grant that a group is an
  agent while denying that it experiences anything. That is the move
  group-agency accounts make when they use IIT against group
  consciousness.
- **Minsky, Brooks, Levin.** Minsky's mindless agents ([LIT-429](../literature.d/LIT-429.md)), Brooks's
  behaviour layers ([LIT-436](../literature.d/LIT-436.md)) and Levin's nested Selves ([LIT-439](../literature.d/LIT-439.md))
  are all architectures of parts. Under this paper, none of them is
  conscious or unconscious by virtue of how it behaves. Two of its own
  conditions bear on them. A part with one-way causal links to the rest is
  only an "appendix". And the environment counts only as background
  condition, so feedback that runs through the world does not integrate a
  system. That second point is my observation, not the paper's, but it
  bears directly on Brooks's design, whose layers "interface directly to
  the world through perception and action, rather than interface to each
  other particularly much".

## Bearing on the record

For the Minsky–Schwitzgebel bridge, this is **the anti-nesting principle
itself**, in its most formal statement. Against [NOTE-131](NOTE-131.md)'s numbering:

- **C3: contests**, for any whole that overlaps a conscious part with
  higher Φ, and symmetrically for any part of a higher-Φ whole.
- **C4: neutral.** Putnam is not cited, though this is the formal heir of
  his stipulation.
- **C5: the target.** Nothing here answers the reductio. The strict
  local-maximum rule is what produces the sharp threshold. The grain clause
  is the one resource the paper offers for a whole to out-integrate its
  parts.

A THEORY drawing the bridge should cite it for three things: the statement
of exclusion, the fact that its system-level form is postulated from the
axiom, not argued, and the zombie result. The zombie result says that
agency composed from parts does not bring experience with it on IIT, and
that is the clearest answer any work on this list gives to the brief's
second question. A THEORY should not cite this paper for the Occam's-razor
or two-person-group defence of system-level exclusion, which are not in it.

It carries no instruction for machine-learning practice.

## Limitations

- **Toy systems only.** "The present analysis is unfeasible for systems of
  more than a dozen elements or so." The brain, cerebellum, split-brain and
  octopus claims are extrapolations.
- **The grain is assumed, not found.** The authors say the optimal
  spatio-temporal grain "needs to be established". Every example assumes
  it.
- **Exclusion at the system level is unargued.** It is the axiom restated
  as a postulate. Why the *maximum* and not, say, every integrated set is
  not addressed, and no tie rule for systems is given.
- **The identity is not tested** by anything in the paper. The empirical
  support mentioned (TMS–EEG in sleep, anaesthesia and brain damage)
  concerns integration as a correlate of the level of consciousness, not
  exclusion.
- **Incomplete by the authors' account.** The relation of the MICS to
  modalities and "feel", the origin of meaning, and "matching" to the
  environment are left to future work.

## Open questions

- Is there an argument for system-level exclusion that does not reduce to
  the axiom "each experience has definite borders"? The axiom is about one
  experience. It does not obviously forbid a second, larger experience that
  includes the first subject as a part. That is the gap Schwitzgebel
  exploits.
- What does the grain search do to a nested system? If a coarse-grained
  whole can beat its fine-grained parts, exclusion could favour the
  collective, as the book version of Schwitzgebel's argument suggests via
  Hoel et al. 2013. No calculation for a social system exists.
- Does feedback through a shared environment ever count as integration? It
  does not under the background-condition rule here. That matters for
  every behaviour-based or swarm architecture.
