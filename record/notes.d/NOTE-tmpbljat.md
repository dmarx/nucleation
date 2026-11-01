---
status: Read
paper: 'LIT-tmppbuqq'
title: 'Bechtel & Abrahamsen — dynamic mechanistic explanation'
version: 1
history:
- version: 1
  date: '2026-11-01'
  note: >-
    Read in full from the published version, Studies in History and
    Philosophy of Science 41:321–333, the Elsevier PDF (13 pp.) on
    Bechtel's UCSD page
    (mechanism.ucsd.edu/bill/research/bechtel.dynamicmechanisticexplanation.2010.pdf),
    fetched 2026-11-01. Text extracted with plain `pdftotext`, for the
    two-column reading order, and with `-layout`; page numbers are the
    journal's. I read the abstract, §§1–5, footnotes 1–5, and the
    captions of Figs. 1–3. The reference list was skimmed. The figures
    (Hardin et al.'s loop, Goldbeter's limit cycle, the Drosophila
    oscillator) did not survive extraction, and the equations survived
    only partly. Goldbeter's mRNA equation and Leise and Siegelmann's
    two equations were reconstructed from the extraction and the prose;
    they are given below as the paper's, not checked against the cited
    originals.
date: '2026-11-01'
summary: >-
  A dynamic mechanistic explanation joins a mechanistic account of parts,
  operations and organization to a computational model whose variables
  are properties of those parts and operations. In circadian research the
  parts came first, from experiment, and six kinds of modelling result
  follow (C1–C6). In cognitive science the models posit their mechanisms
  and are checked only by fit to behaviour. That makes them how-possibly
  accounts, and leaves competing architectures underdetermined. Two of
  the paper's cases bear on the record: clamping a variable in a grounded
  model to test componency (C3), and the open question whether peripheral
  clocks are self-sustained or damped oscillators driven by the SCN (C6).
---
<!-- inactive-ok-file: CLAIM-519 CLAIM-515 QUESTION-086 QUESTION-093 CLAIM-tmpg57ci THEORY-tmpnzjca LIT-832 — Proposed, Open or Unavailable; claims, questions and an unread book this reading bears on, cited as open -->

# NOTE-tmpbljat: Bechtel & Abrahamsen — dynamic mechanistic explanation

## Contribution

It names and illustrates "dynamic mechanistic explanation": mechanistic
decomposition into parts and operations, joined to quantitative modelling
of how the organized operations unfold in time. It extracts six
contributions such models make from the circadian literature of
1990–2007. It then sets cognitive modelling beside them. Cognitive models
make the same kinds of contribution but rest on no independent
identification of parts, so their evidential standing is weaker in a
definite way.

## Key insight

The same equations can be a description of a mechanism or a conjecture
about one. Which they are depends on whether their variables were tied to
parts and operations found by other means before the model was written.
When they were, model experiments explore that mechanism's dynamics.
When they were not, fit to behaviour shows only that some mechanism of
the posited kind could produce it. "Empirical evidence can rule out
specific models, but usually cannot decide between competing
architectures" (p. 332).

## Assumptions

- **Mechanism, as the authors define it (p. 323):** "A mechanism is a
  structure performing a function in virtue of its component parts,
  component operations, and their organization. The orchestrated
  functioning of the mechanism, manifested in patterns of change over time
  in properties of its parts and operations, is responsible for one or more
  phenomena." The second sentence is the 2010 addition.
- **Models are ordinary differential equations in time.** Variables are
  chosen properties of parts or operations, and some quantities are
  parameters. "a property initially treated as a parameter may, as the
  model is further explored, become a variable" (p. 323).
- **Independent identification of parts is possible** for circadian clocks
  and, so far, mostly not for cognition (p. 329). The argument depends on
  the contrast, not on any claim that cognitive parts cannot be found.

## Key results

The six contributions, each with its circadian exemplar.

- **C1, sufficiency (pp. 324–325).** "A model can demonstrate that a
  mechanism, whose parts, operations, and organization have been at least
  partially identified, is able to exhibit the phenomenon of interest."
  The exemplar is Goldbeter (1995). Its five kinetic equations for
  per-mRNA and PER, with cytoplasmic mRNA
  dM/dt = v_s K_Iⁿ/(K_Iⁿ + P_Nⁿ) − v_m M/(K_m + M), give limit-cycle
  oscillations only in a parameter range. A degradation parameter v_d
  sets periods from 19.3 to 64 h. Mental simulation cannot find that
  range. The paper calls this, after Craver (2007), a "how possibly"
  explanation (p. 325). Footnote 2 (p. 324) gives a history: Griffith
  (1968) showed that negative feedback through one gene product gives
  undamped oscillation only for a Hill coefficient n > 9. Later models
  escaped this by adding nonlinearity elsewhere, in degradation.
- **C2, parameter exploration (p. 325).** Leloup and Goldbeter (1998), ten
  equations with TIM, simulate light by doubling TIM's degradation rate.
  This reproduces phase advances and delays, and in some ranges
  birhythmicity and chaos. Model experiments "do not show that the
  mechanism in fact could produce these effects". They show that "if
  particular parameter values and mode of organization were realized in
  the actual system, the effects should correspond".
- **C3, which parts belong (p. 326).** "A model can indicate which parts
  and operations of a system that have been identified empirically are
  essential for producing the phenomenon of interest, and therefore should
  count as components of the responsible mechanism." Smolen et al. (2001)
  fixed the concentration of CLOCK in a reduced model, and oscillation
  continued, robust to the other parameters. They concluded that the
  positive CLOCK loop "was not critical", and that the rhythm comes from
  the PER/TIM negative loops. Simplified models make it easier to see
  "which are components of the system but not of the responsible
  mechanism for that particular phenomenon". The same clamp in vivo would
  need a buffer, so it "is much easier to accomplish in a model".
- **C4, disorder (p. 327).** Altering the phosphorylation parameters of
  PER in Leloup and Goldbeter's mammalian model mimics advanced and
  delayed sleep phase syndromes. This was later matched by point mutations
  at the CKIδ/ε sites in families with ASPS.
- **C5, coupling (p. 327).** "A model can reveal conditions under which
  independent mechanisms, each with its own internally determined
  dynamical (oscillatory) behavior, can be coupled so as to exhibit
  coordinated collective behavior."
  - Gonze et al. (2005): a mean-field VIP term with coupling 0 leaves
    periods scattered, and with coupling 0.5 the oscillators synchronize.
    In the two-oscillator analysis, single neurons' oscillations may damp
    without VIP.
  - To et al. (2007): about 40% of model cells can sustain oscillation
    alone. Without VIP about 60% become arrhythmic and the rest
    desynchronize, matching Aton et al. (2005).
- **C6, restoring relations (p. 328).** "A model provides a means of
  exploring the space of possibilities for altering and restoring
  relations between multiple mechanisms."
  - The question it serves: peripheral oscillators were long thought
    "slaves" to the SCN, damping without its input. Newer evidence was
    that they keep oscillating but lose synchrony, so the SCN is "a
    conductor ... than ... a ringmaster" (Davidson et al. 2004).
  - Leise and Siegelmann (2006) use two-variable oscillators,
    dX/dt = r_X/(1 + Y²) − q_X X and dY/dt = r_Y X²(t − τ_lag) − q_Y Y,
    "whose biochemical interpretation they left unspecified". With these
    they model core, shell and periphery, with coupling by thresholds.
  - Under a simulated six-hour advance, damped peripheral oscillators
    regain their phase relation quickly. Self-sustained ones take longer,
    need strong coupling, and sometimes resynchronize by delaying fifteen
    hours rather than advancing six.
  - The paper's reading: modelling both kinds "can reveal the empirical
    signatures that each may leave ... and so guide empirical attempts to
    answer this question".
- **The cognitive comparisons (pp. 329–332).**
  - Rumelhart and McClelland's past-tense network (C1) led to a debate
    with Pinker and Prince. Without constraint from parts it was
    "irresolvable": "The relevant models are underdetermined" (p. 330).
  - McClelland et al. (1995) illustrate C3. They modelled no hippocampus,
    supplying "only the interleaved output it was presumed to send to
    neocortex". Stopping that training stands for a hippocampal lesion
    and gives graded retrograde amnesia (p. 331).
  - Hinton and Shallice's lesioned attractor network illustrates C4:
    deep dyslexia's mixed errors (p. 331).
  - van Leeuwen's coupled logistic-map lattice illustrates C5–C6:
    alternating groupings of a dot grid (pp. 331–332).
  - Each is, "At best", a suggestion of "how and why the actual
    mechanism behaves this way, if it in fact employs" the model's
    organization (p. 332).
- **Describing against mirroring (p. 329, n. 5).** A circadian model is not
  itself a clock, because its variables track properties of parts rather
  than performing their operations. Cognitive models are often taken to
  think because their operations are posited to be the mind's.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Models of an empirically identified mechanism can show it suffices for the phenomenon, and in which parameter ranges | strong | Goldbeter 1995 and successors (pp. 324–325) |
| C2 | Clamping a variable in such a model can show that an identified part is not needed for the phenomenon, and so is not a component of the responsible mechanism | moderate | one case, Smolen et al. 2001 (p. 326); valid only as far as the model is faithful |
| C3 | Whether peripheral clocks are self-sustained or driven damped oscillators was open in 2010, and the two leave different modelled signatures under phase shifts | moderate as a report; the signatures are model outputs, not data | Davidson et al. 2004; Leise & Siegelmann 2006 (p. 328) |
| C4 | Cognitive models are de novo proposals checked by fit, so fit usually cannot decide between architectures | moderate | the past-tense debate (p. 330) and four further cases; an argument from examples |
| C5 | Modelling anchored in empirically identified parts is the path for cognitive science to follow | weak, a recommendation | conclusion (p. 332) |

## Concepts

- **Dynamic mechanistic explanation**: mechanistic decomposition plus a
  computational model of the real-time dynamics of the identified parts
  and operations (pp. 322–323).
- **Anchoring**: tying a model's variables and parameters to properties of
  identified parts and operations (p. 323).
- **Responsible mechanism**: the subset of a system's components needed for
  a given phenomenon. It is relative to that phenomenon, so a part can be
  a component of the system and not of the responsible mechanism (p. 326).
- **De novo model**: a model that posits a mechanism to account for
  behaviour, with no independent evidence for its parts (abstract, p. 321).

## Connections

It builds on Bechtel and Abrahamsen 2005's account of mechanism, here
extended to dynamics, and anticipates their "Complex biological
mechanisms: cyclic, oscillatory, and autonomous" (then in press). It cites
Craver 2007 ([LIT-832](../literature.d/LIT-832.md)) for "how possibly". The C3 test is a model-based
version of the interlevel experiments in Craver and Bechtel
([LIT-tmpgntir](../literature.d/LIT-tmpgntir.md)): an ideal intervention on a part, which the model makes
cheap. It does not engage the dynamicist challenge to mechanism (van
Gelder, Kelso). Its Beer and van Leeuwen examples show dynamical tools
used within a mechanistic project.

## Limitations

- **Six exemplars, one field each**, chosen to illustrate rather than to
  test. Nothing measures how often grounded models in fact outperform de
  novo ones.
- **C3 is only as good as the model.** Smolen et al.'s clamp shows that
  CLOCK oscillation is not needed in a reduced model that merged PER and
  TIM and replaced transport by a delay. The paper does not say whether
  later experiments confirmed this. Its own general caution under C2
  applies: equations "may even misrepresent or leave out critical
  components".
- **Grounding is treated as all or nothing** between the two fields. Beer's
  model is "less hypothetical" (p. 330), but no scale of anchoring is
  offered.
- **Same dynamics from different mechanisms is not discussed as such.**
  The paper's distinction implies it: de novo models can match behaviour
  and still differ in architecture. But it does not state when two
  anchored models with different parts give the same dynamics, or how
  that would be detected.

## Open questions

- Did isolation experiments settle whether peripheral clocks are
  self-sustained? The paper treats it as open. The answer bears on
  [THEORY-tmpnzjca](../theory.d/THEORY-tmpnzjca.md).
- Are Leise and Siegelmann's signatures (recovery time, a fifteen-hour
  delay instead of a six-hour advance) seen in tissue? Then a perturbation
  of state alone would tell the two arrangements apart, because they are
  not dynamically equivalent.

## Bearing on the record's own argument

- **[CASE-189](../cases.d/CASE-189.md) and [CASE-190](../cases.d/CASE-190.md) are de novo, how-possibly models in this
  paper's sense.** Their variables, "constraint capacities", a connector q,
  a copying catalyst, are posited to exhibit maintenance. They are not
  properties of parts found by experiment, which the cases themselves say
  ("Which terms are internal is stipulated", [CASE-189](../cases.d/CASE-189.md)). So they can make
  contributions C1 and C2: an organization of this kind can be maintained,
  is lost at a fold, and so on. They also make C3 and C5 inside the model:
  the knockouts and the coupling. What they cannot do, on this paper's
  account, is show that any actual system is organized that way. That
  needs anchoring. The record already says this in its own terms. This
  paper gives it a name and a precedent.
- **[CLAIM-522](../claims.d/CLAIM-522.md): the dynamics underdetermine the mechanism, and grounding is
  the remedy.** [CLAIM-522](../claims.d/CLAIM-522.md)'s pair has identical equations, so no model of
  the dynamics alone can choose between them. This paper's answer is the
  one [CLAIM-522](../claims.d/CLAIM-522.md) gives: identify the parts and intervene on them. Two cases
  in the paper have [CLAIM-522](../claims.d/CLAIM-522.md)'s structure. Same structure, not shown same
  mechanism:
  - **McClelland et al. (p. 331).** The hippocampus is not modelled. Its
    output is supplied from outside the model as a training schedule.
    Stopping the schedule "corresponds to" a hippocampal lesion. Within
    the model nothing distinguishes a training signal produced by an
    internal part from one supplied by the modeller. Whether the
    hippocampus is a component of the memory mechanism is settled by
    anatomy and lesion, outside the model, just as [CLAIM-522](../claims.d/CLAIM-522.md)'s boundary
    is declared.
  - **The peripheral clocks (p. 328).** "Slave" against "conductor" is
    exactly the question where an oscillation is maintained: by the
    peripheral cell itself, or by its drive from the SCN. The direct
    test, by definition of the two kinds, is to remove the drive, which
    is the intervention [CLAIM-522](../claims.d/CLAIM-522.md) names. The paper does not say what the
    evidence it reports was.
  - The modelled phase-shift signatures show the limit of [CLAIM-522](../claims.d/CLAIM-522.md)'s
    ideal case. A driven damped oscillator is not dynamically equivalent
    to a self-sustained one, so a perturbation of state can separate
    them. [CLAIM-522](../claims.d/CLAIM-522.md) holds where the outside supplier reproduces the
    production law exactly, and a damped oscillator plus its drive does
    not.
  - That is [THEORY-tmpnzjca](../theory.d/THEORY-tmpnzjca.md), which bears on [QUESTION-086](../questions.d/QUESTION-086.md)'s search for an
    intervention short of removal.
- **[CLAIM-519](../claims.d/CLAIM-519.md): the cognitive half of this paper is [CLAIM-519](../claims.d/CLAIM-519.md) at the level
  of practice.** [CLAIM-519](../claims.d/CLAIM-519.md) says competent behaviour does not establish an
  internal world model, and that establishing a mechanism needs evidence
  that discriminates implementations. This paper says the same of
  cognitive models in general: fit is "indirect evidence" (p. 330), and
  architectures stay underdetermined. Footnote 5's contrast between
  describing and mirroring bears on [CLAIM-519](../claims.d/CLAIM-519.md)'s two readings of "contains
  a model". A model that tracks variables of a mechanism is not thereby a
  component that performs the operations.
- **[CLAIM-515](../claims.d/CLAIM-515.md): its "realized" question needs anchored evidence.**
  [CLAIM-515](../claims.d/CLAIM-515.md)'s third question, which mechanisms realize a capability, is
  the question this paper says cognitive modelling cannot answer by fit.
  Its fourth question, maintenance, is the one circadian models of damage
  and recovery (C4, C6) approach.
- **[CLAIM-521](../claims.d/CLAIM-521.md): a contrast, not a counterexample.** [CLAIM-521](../claims.d/CLAIM-521.md)'s
  dissociation needs "no feedback from the coupled units to the
  maintaining core". In To et al.'s SCN model the coupling signal (VIP)
  is itself what sustains oscillation in about 60% of the cells (p. 327).
  There, losing the coupling loses the maintenance, so coupling strength
  would not stay high up to a fold of maintenance. The record's
  dissociation is a property of one-way architectures. Same structure,
  not shown same mechanism.
- **Clamping is the ideal intervention on a part that a construction
  makes free.** In [CASE-189](../cases.d/CASE-189.md), [CASE-190](../cases.d/CASE-190.md) and the record's knockouts, removing
  a production pathway is C3 in this paper's sense. It decides whether
  that pathway is a component of the mechanism responsible for
  maintenance, relative to the phenomenon and the model
  ([THEORY-tmp7jall](../theory.d/THEORY-tmp7jall.md)). Which pathways count as inside is not decided by
  the clamp. That is [CLAIM-tmpg57ci](../claims.d/CLAIM-tmpg57ci.md)'s point.
