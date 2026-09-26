---
number: 121
status: Read
formerly:
- NOTE-tmpe9tn1
paper: LIT-133
title: 'Elshatlawy et al. — Generalized theory of observers'
version: 2
history:
- version: 2
  date: '2026-09-26'
  note: >-
    Read in full (full text of arXiv:2504.16225v3 (7 Jan 2026), downloaded
    2026-09-26 to rawA/obs_v3.pdf. It is 50 pp. and is the Routledge chapter
    text: ch. 4 of *Quantum Gravity and Computation*, printed pp. 52–101,
    DOI 10.4324/9781003546139-6 on p. 52. That covers §§4.1–4.11, two
    endnotes (p. 97) and 70 references (pp. 97–101). pdftotext is not
    installed, so the text was extracted with PyMuPDF. Figures 4.1–4.11 were
    read from their captions and diagram labels only; the images were not
    viewed. v1 (22 Apr 2025, 47 pp.) was also downloaded (rawA/obs_v1.pdf),
    for its front matter, author list and theorem numbering only. Its body
    was not compared line by line with v3. Locations below are the chapter's
    printed page numbers.). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-26'
summary: >-
  The paper defines a "minimal observer" as a finite-state transducer with
  a boundary: a tuple O = (X, Y, Z, f, g, B) with |X| > 1, |Y| ≥ 1, |Z| ≥
  1 and feedback closure (Def. 4.1, p. 57). It then asserts, without
  derivation, that measurement outcomes, reference frames, coarse-graining
  and the quantum–classical cut are all defined by such observers. The
  paper's only formal results are that isomorphism of these machines is an
  equivalence relation ("Theorem 2", p. 93), and a complexity bound C(O) ≥
  log 2 (Prop. 4.1, p. 94) whose correction term Λ is never defined and
  whose proof supports only C(O) ≥ 0.
---

<!-- inactive-ok-file: LIT-177 — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-150 — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-102 — Deferred: a seed from the same 2026-09-26 philosophy sweep, cross-referenced by the citing work's dossier; lapses when the cited work is read -->
<!-- inactive-ok-file: LIT-133 — Deferred: the paper is placed by this reading; the directive lapses when its status changes; the directive lapses when its status changes -->

# NOTE-121: Elshatlawy et al. — Generalized theory of observers

## Contribution

The chapter proposes one cross-disciplinary definition of an observer as a cybernetic sensor–state–actuator loop with a boundary. It maps that definition, by analogy, onto quantum measurement (QBism, RQM, Copenhagen), onto Kant, Husserl and Wittgenstein, and onto relativistic "observer space". The definition itself is standard automata theory: a Moore machine (X, Y, Z, f, g) plus a boundary B that is not formalised. What is new is the claim that this object underwrites measurement, reference frames, coarse-graining and the quantum–classical cut. That claim is argued by analogy and never derived. The longest section (§4.10.3, pp. 75–92) is a survey of relativistic and categorical treatments of observers: the 7-dimensional observer space of Gielen & Wise, Crane's functor, Oziewicz's groupoid and Lachièze-Rey's foliations. These are not connected formally to Def. 4.1. The paper itself says that in §4.10.3 "observer" means a worldline with a frame, not the feedback-loop observer (p. 76).

## Key insight

An observer is defined as whatever keeps an internal record, updated by inputs that cross a boundary, and acts back on its environment. Observation and control are then the same loop, run in opposite directions (p. 53). Almost everything else in the chapter comes from reading "where the boundary B is drawn" as the answer to a foundational question: where the Heisenberg cut sits (pp. 73–74), when a fact becomes relative to an observer (p. 72), and how the world is coarse-grained (p. 59). None of those readings is derived from the definition.

## Assumptions

- **Classical, discrete observers.** X is a finite or countably infinite state space (Def. 4.1, p. 57). In the Copenhagen section X is "classical by design, consisting of stable states" (p. 74). The model is called classical at p. 58.
- **Deterministic update.** f : X × Y → X and g : X → Z are functions (p. 57). Stochastic or quantum update is only gestured at: endnote 2 suggests QBist belief states (p. 97).
- **Boundary as primitive.** B "demarcat[es] 'inside' … vs. 'outside'" (p. 57). It has no mathematical structure, so every claim that turns on "placing B" rests on an informal notion.
- **Feedback closure.** The observer's outputs must alter the environment, which then alters later inputs (p. 57). This is a condition on an environment that the formalism never models.
- **"Minimal" is structural.** Minimality means the fewest components. The paper says this "avoids complexity like memory" (p. 58), yet |X| > 1 is at least a one-bit memory. Of the seven features in the meta-model (p. 57), the definition keeps four. It drops the internal model, self-monitoring and, implicitly, adaptation.
- **Well-founded meta-observation.** Infinite regress is blocked by stipulation: "we forbid cycles of observation that do not converge" (pp. 95–96).

## Key results

- **Definition 4.1** (p. 57). O = (X, Y, Z, f, g, B) is a minimal observer if |Y| ≥ 1, |Z| ≥ 1, |X| > 1 and feedback closure holds. The worked example is a thermostat with X = {ON, OFF}, Y = {Cold, Hot}, Z = {HeaterOn, HeaterOff} (p. 58).
- **Electron verdict** (§4.7.1, p. 61). By Def. 4.1 an electron is not an observer: it has no internal state-update mechanism and no definable B. A thermostat and a Braitenberg vehicle are observers (pp. 55–56).
- **Definition 4.2 and "Theorem 2"** (pp. 92–94). A homomorphism is a triple (φ_X, φ_Y, φ_Z) with φ_X(f₁(x, y)) = f₂(φ_X(x), φ_Y(y)) and φ_Z(g₁(x)) = g₂(φ_X(x)). Bijective homomorphism is an equivalence relation. The proof is the usual one: identity, inverse, composition.
- **Proposition 4.1** (pp. 94–95). With C(O) = log(|X|·|Y|·|Z|) − Λ(O), the paper states C(O) ≥ log 2 for minimal observers, and says C(O) "can grow arbitrarily large" under learning. Λ is undefined and the lower bound is not established (see corrections).
- **Adaptation function** (p. 95). α_O : X × Y* → ℕ is defined as the number of steps needed to reach a stable configuration. It comes with no result. The paper notes that isomorphic observers share α_O, complexity and other invariants, which follows immediately from the definitions.
- **Seven "without observers" claims** (§4.6.2, p. 59). Without observers there is no internal/external distinction, no definite outcome, no reference frame, no hierarchical observation and no coarse-graining. Each is asserted. None is argued beyond pointing to Wolfram and to Fields.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A minimal observer is a tuple (X, Y, Z, f, g, B) with \|X\| > 1, \|Y\| ≥ 1, \|Z\| ≥ 1 and feedback closure. | definition | Def. 4.1, p. 57; B and closure are not formalised |
| C2 | Observer isomorphism is an equivalence relation. | proof (trivial) | "Theorem 2", pp. 93–94 |
| C3 | C(O) ≥ log 2 for every minimal observer. | weak: the proof does not establish it | Prop. 4.1, pp. 94–95; Λ undefined; the argument yields ≥ 0 |
| C4 | Without observers there are no definite measurement outcomes, reference frames or coarse-grainings. | assertion | §4.6.2, p. 59; the supporting citations are misnumbered |
| C5 | An electron is not an observer. | follows from Def. 4.1, given the informal B | §4.7.1, p. 61 |
| C6 | The model "operationalizes" RQM: a fact is relative to O iff it is recorded in X through an input crossing B. | assertion; in tension with RQM itself, where any system, inanimate ones included, is an observer (as the paper notes on p. 71) and C5 | §4.10.2.2, pp. 71–73 |
| C7 | The model provides "a mathematically rigorous criterion for the condition when quantum measurement occurs" and "identifies the exact moment and mechanism of quantum collapse". | assertion; unsupported | §4.10.2.3, pp. 74–75; X is classical by stipulation, and nothing says how a superposed system yields one y ∈ Y |
| C8 | Results on loop efficiency and adaptation speed are derived. | false as stated | p. 90 and p. 96 claim them; only a definition is given (p. 95) |
| C9 | The framework mediates between realism and constructivism and "enriches" Bhaskar's critical realism. | assertion | §4.10.1.2, p. 68 |
| C10 | Self-modification of f, g and B by AI systems "blurs traditional lines of accountability". | informal argument | §4.10.1.3, pp. 68–69 |

## Method

The method is conceptual analysis by analogy. The paper states a finite-state definition, gives one worked example (the thermostat), and then reads the definition's components onto positions in quantum foundations, phenomenology and relativity. Each comparison has a "phenomenological scenario": a quantum coin with QBism, Wigner's friend with RQM, Stern–Gerlach with Copenhagen. There are no simulations, computations or experiments. The cellular-automaton figures (Rule 110, Figs. 4.4–4.6) illustrate how a block of cells could be designated an observer. Nothing is computed from them.

## Concepts

- **Minimal observer.** Def. 4.1: sense (Y), update (f), act (g), with a boundary B and feedback closure. Minimality is "structural" (p. 58). The paper also mentions functional and ontological minimality and leaves both undeveloped.
- **Boundary B.** The inside/outside partition. The paper uses it as the Heisenberg cut (p. 74), as the relational locus of facts (p. 71) and as the Kantian form of intuition (p. 64). Formally it is empty.
- **Observer homomorphism and equivalence.** Def. 4.2 and Theorem 2: structure-preserving maps and isomorphism of Moore machines. The paper likens this to bisimulation (p. 90).
- **Observational complexity C(O).** log(|X||Y||Z|) − Λ(O), where Λ is an undefined redundancy term (p. 94).
- **Adaptation function α_O.** Steps to a stable configuration (p. 95).
- **Hierarchical encapsulation.** The stipulation that meta-observation relations form a well-founded partial order (pp. 95–96).
- **Observer space O.** In §4.10.3 only: the unit timelike tangent bundle of spacetime, 7-dimensional for 4-dimensional M (p. 84). This is a different notion of "observer" from Def. 4.1, as p. 76 concedes.

## Connections

The definition is Ashby's and Wiener's feedback loop, restated as a Moore machine. The record-keeping reading comes from Everett's "servomechanisms" (via Bacciagaluppi) and from Hartle's IGUS (p. 54). The boundary reading follows Chris Fields (Fields 2014) (pp. 60, 62). The chapter is a companion to the authors' *Pregeometry, Formal Language and Constructivist Foundations of Physics* ([LIT-102](../literature.d/LIT-102.md), cited as [33]). It shares that paper's constructivist and ruliological programme and cites Rickles, Elshatlawy & Arsiwalla's *Ruliology* ([32]), which the record does not hold.

Against Rovelli's relational interpretation ([LIT-177](../literature.d/LIT-177.md)), the chapter says it operationalises RQM (pp. 71–73). Its electron verdict (p. 61), however, denies the observer role to the elementary systems that RQM grants it to. The paper records RQM's view that "even an inanimate object can be an 'observer'" (p. 71) and does not reconcile the two.

Against Carroll's Hilbert-space fundamentalism ([LIT-123](../literature.d/LIT-123.md)), the chapter's view that coarse-graining requires an observer is opposed in spirit. Carroll's programme selects factorisations from the Hamiltonian, with no observer. The chapter does not engage it.

On objective coarse-graining ([LIT-150](../literature.d/LIT-150.md)), the dossier asked whether the chapter's claim survives objective accounts. The chapter does not consider any, so its claim is untested rather than refuted.

The nearest held work on percept–action loops as physical systems is *The Work Capacity of Channels with Memory* ([LIT-041](../literature.d/LIT-041.md)). That paper derives quantitative results for the kind of loop this chapter only names.

**Account of agency.** The chapter treats the observer as "a feedback-driven agent or subsystem" (p. 53). Its components are a sensor, a processing unit "comparing [input] to a goal or reference", and an actuator (p. 55). Goals appear in that gloss and in the pendulum-robot example (p. 90), but not in Def. 4.1. The account is therefore cybernetic and goal-optional. Agency is action in a closed sensorimotor loop. Autonomy is added only as self-modification of f, g and B (p. 68), which the paper treats as the point where accountability becomes hard. It offers no account of goals, norms or ownership of action.

**Agency tag: justified, as a secondary topic.** The chapter's minimal observer is, in its own words, a minimal feedback-driven agent. It argues that observation and control are one loop, and §4.10.1.3 addresses "agency in AI and responsibility". Someone browsing agency would reasonably expect a work that sets a sensor–actuator threshold for being an observer or agent. The tag order (philosophy-of-science, agency, quantum-foundations) is right: the chapter is chiefly about observers.

## Bearing on the record

- It carries nothing for ML practice. The neural-network example (p. 57) labels weight updates "second-order cybernetics" and makes no claim about training. The citation of Amodei et al. is misplaced (see corrections). No anthology document is affected.
- The record has no THEORY documents for it to support or contradict.
- No other held document cites this work. A grep of literature.d and notes.d on 2026-09-26 found only its own LIT and NOTE. Its NOTE's cross-references to [LIT-177](../literature.d/LIT-177.md), [LIT-150](../literature.d/LIT-150.md) and [LIT-102](../literature.d/LIT-102.md) should carry the contrast with RQM as "denies observer status to elementary systems, while claiming to operationalise RQM", not as a clean opposition.
- The dossier's "theorems on observer equivalence and complexity" should not be repeated anywhere as a result.

## Limitations

- **Nothing quantum is modelled.** The observer is classical by stipulation, and the claims about collapse and the Heisenberg cut (pp. 73–75) are restatements of the problem in terms of B, not answers to it.
- **The boundary does all the work and is never defined.** Every foundational payoff turns on it.
- **The formal results are definitional, and one is misproved.** Proposition 4.1 does not establish its bound.
- **The conclusion overclaims.** It calls the theory "comprehensive, rigorously formalized" (p. 96) and cites results on adaptation speed that do not exist.
- **Two notions of observer run in parallel.** §4.10.3 is a survey of relativistic observer space, using a different notion from Def. 4.1 (p. 76), and nothing connects the two.
- **The references are unreliable.** At least one citation cluster is misnumbered (p. 59), and two references are never cited.
- **No engagement with the obvious objection.** Critics say "observer" becomes vacuous if thermostats qualify. The reply (p. 95) is that minimal observers are "building blocks", which restates the thesis rather than defending it.

## Open questions

- Can B be formalised, for instance as a Markov blanket, a tensor factorisation or a Fields-style holographic screen, so that "placing the cut" becomes a mathematical choice with consequences? Until it is, the quantum claims cannot be assessed.
- Is there a non-trivial complexity measure here? Defining Λ(O), for example as the log-size of the minimal equivalent machine (Myhill–Nerode reduction), would make C(O) well defined and Proposition 4.1 checkable.
- How can the electron verdict and the claim to operationalise RQM both hold? The paper would need to say which it gives up.

## Corrections to the seeded skim

- Authorship. The dossier says that "neither arXiv nor Crossref lists" Alexander Blum. arXiv does list him for v1: the v1 abs page metadata and the v1 PDF both name "Alexander Blum, Max Planck Institute for the History of Science, Berlin" as fourth author. He was dropped in v3 and in the chapter. The tracker was right about v1, and the omission is right only for v3 and the book.
- The "theorems" are one theorem and one proposition, and neither is substantive. The dossier speaks of "theorems on observer equivalence and complexity". v3 has a single theorem, numbered "Theorem 2", and there is no Theorem 1. The numbering is an artefact: v1 calls the same result "Theorem 1". The theorem shows that bijective structure-preserving relabelling is an equivalence relation, which holds for any isomorphism (pp. 93–94). Proposition 4.1 (p. 94) does not follow as stated. Λ(O), the "redundancies" term, is never defined. The proof argues only that Λ "cannot push C(O) below zero", which gives C(O) ≥ 0, not C(O) ≥ log 2.
- "Non-trivial sensing" is not what the conditions say. The dossier restates Def. 4.1 as requiring "non-trivial sensing, action, internal dynamics". The stated conditions are |Y| ≥ 1 and |Z| ≥ 1 (p. 57). A one-element input set satisfies them and carries no information. Only |X| > 1 is non-trivial. The boundary B is given no mathematical content anywhere in the paper. Feedback closure is a property of the coupling to an environment, which the tuple does not contain.
- No adaptation-speed results. The paper claims results on "loop efficiency and adaptation speed" (§4.10.3.8, p. 90), and the conclusion claims "rigorous mathematical results on … loop adaptation speeds" (p. 96). These do not exist. The paper only defines α_O : X × Y* → ℕ and remarks that hitting-time or Lyapunov methods "may be invoked" (p. 95).
- "Definitive, self-contained" is quoted without its verb. The conclusion says the framework "aspires to be a definitive, self-contained theory of observation" (p. 96). The dossier drops "aspires".
- Citation errors the dossier passes on. The dossier links §4.6.2 to "Wolfram's foliation-choosing observer". The paper supports that sentence with "[60, 66–68]" (p. 59). Those references are Amodei et al., *Concrete Problems in AI Safety*; Lachièze-Rey; Crane; and Fuchs's "QBism, where next?". None of them is Wolfram, whose works are [12] and [32]. Elsewhere, [7] (Ashby) is cited for the hard problem of consciousness (p. 59). References [59] (Merleau-Ponty) and [61] (Friston) are listed but never cited.
- Page range. The v3 PDF ends on p. 101, not p. 102. The dossier's "pp. 52–102" may come from Crossref; that is unverified.
