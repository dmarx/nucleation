---
status: Read
paper: 'LIT-tmpufhcl'
title: 'Gładziejewski — Real patterns, the predictive mind, and the manifest image'
version: 1
history:
- version: 1
  date: '2026-10-22'
  note: >-
    Read in full on 2026-10-22 from the publisher's open-access PDF
    (Springer, link.springer.com/content/pdf/10.1007/s11229-025-05311-0.pdf,
    CC BY-NC-ND 4.0, 22 pp., article 225), the version of record, with the
    text extracted by pdftotext. The first request was redirected to a
    cookie check; the PDF was fetched on a second request carrying the
    cookie it set. Read: abstract, Sections 1–5, all ten footnotes, Figure
    1's caption and the end matter. The reference list was skimmed. The
    equations were read from the extracted text, where the VFE
    decomposition is garbled, and checked against the standard form. None
    of the cited works was read (Dennett 1991 is held as LIT-220, read
    earlier, and not re-read). Page numbers are the article's, 1–22.
date: '2026-10-22'
summary: >-
  A philosophy paper with no data. It traces Dennett's compression
  criterion for real patterns through minimum description length and
  Bayesian inference to variational free energy, so that learning a
  generative model is extracting real patterns from sensory data. It
  concludes that the manifest image is a structural description of
  sensory data, veridical even in a matched vat. The self-model compresses
  self-generated regularities by positing one common cause, so selves are
  real as patterns and unreal as substances, and which verdict to give is
  a dispute over criteria, not facts. It says nothing about consciousness
  or illusion.
---
<!-- inactive-ok-file: CLAIM-355 CLAIM-tmpdga80 CLAIM-tmpjw8ev THEORY-036 THEORY-064 THEORY-691 THEORY-563 THEORY-tmphhvaa THEORY-tmpru19x THEORY-095 — Proposed; claims and readings cited as open, nothing here rests on them -->

# NOTE-tmp220h1: Gładziejewski — Real patterns, the predictive mind, and the manifest image

## Contribution

Dennett's real patterns were a criterion for the reality of entities the
manifest image already posits. This paper turns the criterion into a
genealogy: the processes that build the manifest image are themselves
pattern extraction. Predictive processing minimises variational free
energy, which balances complexity against fit as minimum description length
does, so perceiving and learning are compressing. Two philosophical
consequences are drawn: a structural, Kantian realism about the manifest
image, and a way to see the realist–antirealist dispute about selves as a
dispute over criteria. The applications are, in the author's words, "a
prolegomenon to a future cognitive-structuralist metaphysics of the
manifest image" (p. 15).

## Key insight

If the brain builds its model of the world by compressing sensory data,
then what the model posits (doors, cats, a self) are the high-level
regularities that make the data compressible. They are real in Dennett's
sense, as gliders are real in the Game of Life. They are real as structure
in the data, though, and the data underdetermine what realizes the
structure. A self is the common cause that best compresses the sensory
effects of one's own activity. There is such a pattern; whether that makes
a self depends on whether one asks for a pattern or a substance.

## Assumptions

- **A realist, representational reading of predictive processing.**
  Footnote 2 (p. 7) assumes that the theories describe actual neural
  computation and that the brain builds internal models. It grants that
  instrumentalist and enactive readings exist, and suggests the view
  survives on them "in a weaker (perhaps diluted) sense".
- **Optimal codes.** The equation of Bayesian inference with description
  length needs L(x) ≈ −log P(x). Footnote 4 (p. 8) calls whether the
  brain uses optimal codes "an open question", and argues that the core
  idea survives without them.
- **The substrate is sensory data.** Patterns are patterns in the signal at
  the sensory periphery, not in the world behind it (p. 11).
- **Individualism.** Footnote 7 (p. 14) restricts the account to
  early-developing capacities, object perception and minimal self-modelling,
  and sets aside the social construction of knowledge, perhaps except for
  the narrative self.
- **Pragmatics fixes the trade-off.** Among compressions of one signal the
  agent's goals pick the useful one (footnotes 5 and 6, pp. 10–13).
  Free energy fixes the accuracy–complexity trade-off, but the
  architecture of the generative model is not derived from it.

## Key results

- **From K-C complexity to free energy (§2, pp. 4–10).**
  - Kolmogorov–Chaitin complexity defines a pattern but is not computable,
    so the paper moves to total description length,
    TDL(M) = L(M) + L(D|M), and the MDL principle. The toy example: for
    the string 0110111001101110, model A (repeat 01 eight times) costs
    2 + 10, model B (repeat 01101111 twice) costs 8 + 2, and the verbatim string 16 + 0, so MDL prefers
    the second (pp. 5–6). *Checked:* the mismatch counts 10 and 2 are
    right.
  - Predictive coding is MDL with prediction error as the data term
    (pp. 6–7).
  - With optimal codes, maximising P(M|D) is minimising
    −log P(M) − log P(D|M), which is TDL, so "Bayesian inference is
    real-pattern extraction" (p. 8, footnote 3). *Checked:* this is the
    monotonicity of the logarithm, as footnote 3 says.
  - Variational free energy splits into a complexity term, KL(Q(M) ‖ P(M)),
    and an expected negative log-likelihood (p. 10). The first is
    "analogous to the model length term", the second to the data term.
    *Checked:* this is the standard decomposition. The analogy is the
    author's, and the complexity term is a divergence from the prior, not a
    code length for the model.
- **Structural realism about the manifest image (§3, pp. 11–15).**
  - Generative models "specify probabilistic and causal structural
    descriptions of sensory patterns" (p. 12). A perceived door is a
    hypothesis about sensory consequences and a place in a causal network.
  - Two senses in which the manifest image is "not freely constructed":
    compressibility is a mathematical fact, and the sensory signal is
    shaped by its external source, "at least unless the model is used to
    run fully off-line simulations, as may be the case in imagery or
    dreams" (pp. 12–13).
  - Veridicalism, after Chalmers. If two subjects' sensory streams match,
    one envatted, they are "necessarily ... equally compressible by
    equivalent higher-level (manifest) structural descriptions". "the
    door that your envatted twin opens to enter another room in her virtual
    world is as real as the door you open" (p. 13).
  - What lies outside: what realizes the structural roles (a door or a
    data structure on a supercomputer), purely intrinsic properties, and
    deeper structure not induced from the senses, which is noumenal only
    "in the limited sense" (p. 14).
  - Footnote 9 (p. 15): Dennett (2013) allows some manifest properties to
    be "projections". Spatial location sits nearer the descriptive end and
    a baby's cuteness nearer the projective.
- **The self (§4.1, pp. 15–17).**
  - Some sensory regularities are endogenous: tactile input from typing,
    vision from one's own eye movements, interoceptive hunger. "the self
    is inferred and represented as a common, single cause that underlies
    certain (endogenously generated) regularities in the sensory signal"
    (p. 16). The model "achieves compression by positing a single, stable
    entity as the common cause of many endogenous patterns" (p. 16).
  - The hierarchy gives a minimal self at fast timescales and a narrative
    self at slow ones (p. 16).
  - The glider swap. Exchange two cells between two gliders and the game
    runs on unchanged. Which glider is which has "no further fact within
    the GoL 'world'" to settle it (p. 17), as Parfit argued for persons.
  - The verdict: anti-realist about selves-as-substances (Letheby &
    Gerrans) and realist about selves-as-patterns (Hohwy & Michael). "The
    conflict between those positions is apparent, and arises at a
    meta-level discussion about which criteria of reality are more
    reasonable to use for this particular domain" (p. 17).
  - Footnote 10 (p. 17): the self is partly self-constituted, "a sort of
    self-fulfilling prophecy", since active inference makes behaviour
    conform to the self-model. In some dissociative states the patterns may
    be "better compressed by model that posits two or more narrative selves
    residing within one body".
- **Ordinary objects (§4.2, pp. 18–20).** Bird's (2023) criterion is that
  "the Xs compose an object Y when the Xs are a non-divisible maximal
  collection of objects such that relevant information about Y compresses
  corresponding information about the Xs in an efficient albeit possibly
  lossy way" (pp. 18–19). A cat compresses; "whiskers + crust + dust" does
  not. Perception parses objects by the same rule, so it is evidentially
  sensitive to whether ordinary objects exist, against the debunking
  argument for nihilism and universalism (Korman).
- **Caveat (§5, p. 20).** Cognition as compression is older than
  predictive processing (Barlow, Wolff), so the view may generalise beyond
  it.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under optimal codes, MAP inference is minimum total description length | strong: a one-line derivation | p. 8, footnote 3 |
| C2 | Free-energy minimisation balances complexity and fit as MDL does | moderate: an analogy between terms, the complexity term being a KL divergence | p. 10 |
| C3 | Learning a generative model is extracting real patterns from sensory data | moderate, conditional on a realist reading of predictive processing and the C1–C2 analogy | §2, footnote 2 |
| C4 | The manifest image is a structural description of sensory data, equally veridical in matched sensory streams, envatted or not | moderate as a conditional: it follows if content is structural; that content is only structural is assumed | §3, pp. 13–14 |
| C5 | The self is represented as a single common cause compressing self-generated regularities | weak to moderate: an interpretation of Hohwy & Michael and Letheby & Gerrans, not shown | §4.1, p. 16 |
| C6 | Realism and anti-realism about selves agree on the facts and differ on the criterion of reality | moderate as a diagnosis | §4.1, p. 17 |
| C7 | Compression-based composition vindicates ordinary objects and makes perception evidence for them | weak: a sketch, relying on Bird 2023 | §4.2 |

## Concepts

- **Real pattern**: a regularity in a substrate that admits a description
  shorter than the substrate itself, objective because compressibility is
  a mathematical fact (pp. 4–5).
- **Substrate**: the base level in which a pattern is found; here the
  stream of sensory data.
- **Total description length**: L(M) + L(D|M), the model's length plus the
  data's length given it.
- **Manifest image**: after Sellars, the ontology of experience and
  intuitive theories; normativity is set aside (footnote 1).
- **Structural veridicalism**: the manifest image's structural claims are
  true of whatever produces the sensory effects, in a vat or not (after
  Chalmers).
- **Self-as-pattern / self-as-substance**: the regularity a self-model
  compresses, against a persisting entity that grounds numerical identity.
- **Minimal and narrative self**: self-models at fast and slow timescales
  of the hierarchy.

## Connections

The paper builds on Dennett's Real Patterns (1991) and his later
endorsement of predictive processing, on Grünwald's MDL, on Friston's free
energy and its description-length reading (Hinton & Zemel; Graves), on
Chalmers's structuralism and veridicalism (2018, 2022), on Hohwy & Michael
(2017) and Letheby & Gerrans (2017) for the self, on Parfit for identity,
and on Bird (2023) and Petersen (2019) for composition. The record holds
Real Patterns (LIT-220, NOTE-190) and Li and Vitányi's MDL and Bayes
condition (LIT-225, NOTE-801). It does not hold Chalmers's structuralism,
Hohwy & Michael, Letheby & Gerrans, or Bird.

## Bearing on the record

- **CLAIM-355 (real binding, constructed owner).** The exchange cited the
  paper "for its treatment of the self as a real pattern whose
  representation can exaggerate its unity". The first half is right. The
  second is not in the paper. It never says the representation
  exaggerates. It says the self-model compresses by "positing a single,
  stable entity as the common cause" (p. 16), and that whether this
  makes a real self depends on the criterion. Read against CLAIM-355:
  - *It supports* the claim's structure. The pattern is real; the single
    substantial owner is not something the pattern supplies (C5, C6).
    Footnote 10's self-constitution through active inference is A26's
    point that self-representations are part of the organization they
    represent.
  - *It cuts against* the word "illusion". On this account the single
    common cause is a lossy compression, not a false report, so a
    self-model positing one owner need not misdescribe anything. That is
    Drayson's objection as CLAIM-355 states it, and the paper's
    "apparent" conflict (p. 17) puts the self's reality at the choice
    of criterion. CLAIM-355 survives only where a misdescription can be
    shown, as it says itself. The paper offers one candidate: dissociative
    states in which one self-model compresses worse than two (footnote
    10). That is where a single-owner model would be not just lossy but
    wrong.
  - Its self is an individual's, and it says nothing about distributed
    agents or collectives.
- **THEORY-563 (consciousness as a real pattern, Taylor).** Same
  compression criterion, applied to selves and objects, not to
  consciousness. This paper does not say what makes a pattern a conscious
  one, any more than Taylor's does.
- **THEORY-036 (the real-pattern criterion admits too much).** The paper
  meets the worry in the way THEORY-036 predicts, by later additions: the
  agent's pragmatic trade-off (footnotes 5, 6) and Bird's maximality and
  non-divisibility. So it is a case for THEORY-036, not against it.
- **THEORY-064, THEORY-691 (the self as model, the self as abstractum).**
  It gives both a mechanism, compression of endogenous signals by a
  posited common cause, and sides with neither on whether such a self is
  real. It calls the choice a matter of criteria.
- **CLAIM-tmpjw8ev (grounding as a relation).** It cuts in an instructive
  direction. CLAIM-tmpjw8ev calls an envatted brain's tree experience
  "ungrounded with respect to the tree". The paper's veridicalism says the
  envatted door is "as real" as yours, because structure in matched
  sensory streams is the same. Both can be true, since they differ on the
  referent: the realizer, ungrounded, or the structural role, grounded
  in the sense of being constrained by an independent source. It also
  supports "ungrounded ≠ unconstrained". The signal constrains the model
  from outside "unless the model is used to run fully off-line
  simulations, as may be the case in imagery or dreams" (p. 13).
- **CLAIM-tmpdga80 (experience constituted by interpretive
  organization).** Indirect. The paper says the manifest image is
  constructed by inference, A3's thesis A, construction, and it says
  nothing about whether the construction is experience, thesis B. It
  uses "conscious experience" only to locate the manifest image (p. 3).
- **THEORY-095 (Inverted Earth).** The veridicalism is a structural
  internalism about manifest content, the side THEORY-095 leaves open.
- **THEORYs warranted.** Two are filed: THEORY-tmphhvaa (the self as a
  compression pattern, and the dispute as one of criteria), and
  THEORY-tmpru19x (manifest content as structure in sensory data,
  equally veridical in matched streams).
- No instruction for machine-learning practice; it uses language models
  only as an example of compression (p. 4).

## Limitations

- No data or model. The self and object sections are, in the author's
  words, "an initial sketch" (p. 15).
- The bridge to cognition rests on footnote 2's realist reading of
  predictive processing and on footnote 4's open question about optimal
  codes.
- The VFE–MDL correspondence is an analogy between terms, not an identity.
- Veridicalism holds only if manifest content is wholly structural. The
  paper assumes this and does not argue it against non-structural content
  (colour quality, for instance), which it puts in the noumenal.
- The self account assumes the predictive-processing self-model of the
  cited authors and does not test it.
- "Compression" does not separate the self as a pattern from any other
  pattern the same agent tracks. Why a self-model is a self, and not one
  more posit, is not addressed.

## Open questions

- When does a single-owner self-model stop being a lossy compression and
  become a misdescription? Footnote 10's dissociative case suggests a test:
  compare the description lengths of one-self and two-self models of the
  same behaviour.
- Does manifest content have a non-structural part, so that the envatted
  twin's door is real in structure but not in quality?
- Does the projective end of footnote 9 (cuteness) include the felt unity
  of the self? If so, the self-model would be partly projection, which is
  where an illusion in CLAIM-355's sense would sit.
