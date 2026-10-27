---
status: Read
paper: LIT-tmpp0mod
title: 'Deutsch & Marletto — Constructor theory of information'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the published version as JATS XML from Europe PMC
    (PMC4309123; Proc. R. Soc. A 471: 20140540; licence stated in the
    XML: "© 2014 The Authors. Published by the Royal Society under the
    terms of the Creative Commons Attribution License", CC BY 4.0). The
    text was extracted from the XML with a short Python script that strips
    tags and linearizes MathML. I read the abstract, all nine sections
    with every subsection of §6 and §8, the seven footnotes, the caption
    of figure 1, the acknowledgements, the funding statement and the 17
    references. Figure 1 is an image and was not seen; only its caption
    was read. Equations the XML renders badly, (1.1) and (8.1)–(8.3),
    were checked against the arXiv preprint 1405.5563 (a 30-page Word
    PDF dated "July 2014", extracted with `pdftotext -layout`), which
    numbers its equations (1)–(10) and its subsections 8.1–8.9. Both
    sources lose the slash of the not-distinguishable sign; it is
    restored here as ⊥̸ from context. The article has no page numbers in
    the XML, so locations are by section and equation.
date: '2026-10-27'
summary: >-
  A programme paper, not a theorem paper. It defines information without
  distinguishability: a set of attributes is an information variable when
  every permutation of it and its cloning are possible tasks, and
  distinguishability is then defined from that, which removes the
  circularity of (1.1). It conjectures principles III–IX for classical
  information, and shows informally that one extra prohibition, a union of
  two disjoint information observables that is not one, yields
  indistinguishable states, no-cloning, complementarity, deterministic
  unpredictability, irreducible measurement disturbance and locally
  inaccessible information. It calls instantiating information "an exact,
  intrinsic property of the substrate", so it supplies a modal, not a
  relational, account of what an information medium is.
---
<!-- inactive-ok-file: CLAIM-tmpmand1 CLAIM-tmpmx2ql CLAIM-136 THEORY-453 — Proposed; the entries the reading bears on, cited as open -->

# NOTE-tmpbcj9n: Deutsch & Marletto — Constructor theory of information

## Contribution

It states what information is in terms of which physical transformations
are possible and which impossible, without assuming distinguishability.
Information is defined from computation (possible permutations) and
cloning (§§3–4), and distinguishability and measurement are defined from
information (§5). That gives the recursive definition of "distinguishing"
in (1.1) a base. It then proposes principles III–IX as conjectured laws of
physics for classical information (§6). It shows that if a subsidiary
theory imposes one further prohibition, the result is "superinformation"
(§7), and that the characteristic features of quantum information follow
from that prohibition (§8). Quantum information is then "an instance of
superinformation" (§1).

## Key insight

What makes something information is counterfactual: a substrate in a state
"cannot be said to carry information unless it *could have been* in a
different state" (§1). Constructor theory turns the counterfactual into
exact statements about tasks. A set *S* of attributes is a computation
variable if every permutation of *S* is possible (with side-effects), and
an information variable if, in addition, it is clonable (§§3–4). Neither
definition mentions distinguishing. Distinguishability is then
"possible to map *X* onto an information variable" (5.1). The non-classical
content all flows through one loophole: "the union of two information
observables, even if their attributes are mutually disjoint, is not
necessarily an information observable. It is through that loophole that all
the non-classical content of constructor information theory flows" (§7).

## Assumptions

- **Principle I**, the basic principle of constructor theory: "All other
  laws of physics are expressible entirely in terms of statements about
  which physical transformations are possible and which are impossible, and
  why" (§2). The authors draw from it that fundamental laws cannot be
  stochastic. Generalized probabilistic theories "can at most be
  descriptions at an emergent level" (§2), and the theory "makes no mention
  of probability".
- **Principle II, locality**: "There exists a mode of description such that
  the state of the combined system **S**1⊕**S**2 … is the pair (*x*, *y*)
  of the states *x* of **S**1 and *y* of **S**2, and any construction
  undergone by **S**1 and not **S**2 can change only *x* and not *y*" (§2).
  In quantum theory the Heisenberg picture is such a mode (refs [9], and
  footnote 3: the local states there are the observables, and only
  "*changeable* quantities" need be local). This is what guarantees that
  "individual physical systems (and not just the entire physical world)
  *have* states and attributes".
- **Possible means approximable without limit.** "No perfect constructors
  exist in nature." A task is possible "if the laws of nature impose no limit,
  short of perfection, on how accurately *A* could be performed, nor on how
  well things that are capable of approximately performing it could retain
  their ability to do so again" (§2). Subsidiary theories must supply the
  measure of accuracy and the meaning of convergence of a sequence of tasks
  on **S**⊕**E** to a task on **S**.
- **Resource assumptions VI and VII**, which the authors call "simplifying
  assumptions rather than grand conjectures" (§6): unlimited preparable
  instances of any information medium from "generic resources", and the
  composition principle, that every regular (loop-free) network of possible
  tasks is possible. Cosmologies with finite resources violate them, and the
  authors argue no §§6–8 result needs them because none says a task must be
  possible.
- **No time.** "In constructor theory, the notion of time does not appear.
  There is a notion of input and output, but not of before and after" (§2).
- The paper is **not deriving quantum theory**: "So we are not trying to
  derive quantum theory, or any other existing law, from anything" (§1).

## Key results

### Constructor theory (§2)

- **Constructor and substrate.** A constructor is the agent of a
  transformation, "whose defining characteristic is that it remains
  unchanged in its ability to cause the transformation again"; substrates
  are transformed from one attribute to another (2.1). "Approximations to
  them, such as catalysts or robots, have non-zero error rates and also
  deteriorate with repeated use."
- **Attribute and variable.** An attribute is "the set of states in which
  the substrate has it". "Any set of disjoint attributes, we shall call a
  physical *variable*". It is sharp with value *x* when the substrate is in
  a state with attribute *x* ∈ *X*. Which groupings are natural "is for the
  subsidiary theories to say", so {'red', 'spherical'} is admissible.
- **Intrinsic attribute**: "one that does not refer to any other specific
  substrate". The distance between **S**1 and **S**2 is intrinsic to
  **S**1⊕**S**2 and to neither part. "Having a particular density operator
  is an intrinsic attribute of a system, whereas the rest of its quantum
  state … describes entanglement relationships with other systems."
- **Tasks** are sets *A* = {*x*1 → *y*1, *x*2 → *y*2, …} with legitimate
  inputs In(*A*) and outputs Out(*A*); the transpose *A*∼ reverses each
  arrow. Parallel composition *A*⊗*B* and serial composition *BA* (when
  Out(*A*) = In(*B*)) are defined. "A *regular network* of tasks is a network
  without loops … Loops are excluded, because a substrate on a loop is a
  constructor."
- **Constructor-theoretic statements** refer only to substrates and which
  tasks on them are possible: "Constructor theory is the theory that the
  (other) laws of physics can be expressed *without* referring explicitly to
  constructors." *A* is possible with side-effects (*A*✓ with subscript) if
  (*A*⊗*T*)✓ for some task *T* on a generic substrate.
- **Principles are testable.** "A principle *P* is refuted if some law
  violating *P* survives experimental tests, whereas all rival laws
  conforming to *P* are refuted" (§2; footnote 1 gives beta decay and the
  neutrino, and parity invariance, as the pattern).

### Computation and information (§§3–4)

- **Reversible computation** C_Π(S) = ⋃_{x∈S} {x → Π(x)}, with or without
  side-effects, for a permutation Π of a set *S* of at least two attributes
  (§3). Swapping two non-orthogonal pure states can be possible (footnote 4
  gives the unitary). Because side-effects are allowed, the physical process
  need not be reversible.
- **Computation variable**: a set *S* of two or more attributes for which
  every C_Π is possible with side-effects; a computation medium has one.
- **Cloning task** (4.1): R_S(x0) = ⋃_{x∈S} {(x, x0) → (x, x)} on **S**⊕**S**,
  with *x*0 preparable from generic resources. *S* is clonable if R_S(x0) is
  possible with side-effects for some *x*0.
- **Information variable**: "a clonable computation variable"; an
  information medium has at least one (§4). **S** "*instantiates classical
  information* if some information variable *S* of **S** is sharp, and if
  giving it any of the other attributes in *S* was possible. Note that the
  constructor-theoretic mode of explanation has allowed this to be expressed
  as an exact, intrinsic property of the substrate." Capacity is the log of
  the cardinality of the largest information variable, additive by II.

### Measurement (§5)

- **Distinguishable** (5.1): *X* is distinguishable if
  (⋃_{x∈X} {x → ψ_x}) is possible with side-effects, where {ψ_x} is an
  information variable. *x* ⊥ *y* when {*x*, *y*} is distinguishable. "That
  provides the base for the recursive definition (1.1), because we have
  defined 'information variable' above without reference to
  distinguishability."
- **Measurable** (5.2): (⋃_{x∈X} {(x, x0) → (y_x, 'x')}) possible, with the
  output in an information medium; non-perturbing when *y*_x ⊆ *x*. A measurer
  of *X* also measures any subset or coarsening of *X*, by relabelling.

### Principles (§6)

- **III, interoperability**: two substrates with information variables *S*1
  and *S*2 combine into one with information variable *S*1×*S*2. "Perhaps
  the most fundamental", and it "cannot even be stated in the prevailing
  conception". It would rule out dark information media that cannot copy to
  normal ones.
- **IV**: pairwise distinguishable implies distinguishable. **V**: if every
  state with attribute *y* is distinguishable from *x*, so is *y*. Motivated
  as "a unifying explanation" for a regularity (the photon-number example).
  "None of our conclusions in §8 depends on their being universal."
- **VI** (generic resources) and **VII** (composition), as above. With III
  they imply that every function on a finite set of integers is computable.
- **Bar operation** (§6a): *x̄* is the union of all states distinguishable
  from *x*; *x̄̄̄* = *x̄*; {*x*, *x̄*} is a Boolean variable, always
  distinguishable and maximal.
- **VIII, consistency of measurement**: if one measurer of *X* gives a sharp
  output on {*a*} ⊆ *X̄̄*, all do. Hence for any measurable *X* there is a
  unique *Z* that every measurer of *X* measures; such variables are
  *observables* (§6a), characterized by *x* = *x̄̄* for every member (§6b).
  "Quantum-mechanical observables, in the Heisenberg picture, are indeed
  observables by this definition."
- **Testable prediction** (§6c): "a statement that the output variable of a
  certain possible measurement will be sharp, with a certain value"; the
  sharpness requirement is "entailed by the logic of testability".
- **IX**: "Any two disjoint, intrinsic attributes are ensemble
  distinguishable", where an experiment on an ensemble *S*(∞) is a sequence
  of experiments on **S**(*n*) as *n* grows without limit. Redundancy plays
  the role probabilities play in Shannon's theory.

### Superinformation (§§7–8)

A superinformation medium **M** has at least two information observables
with mutually disjoint attributes whose union *S* is not an information
observable (§7). In quantum theory, any two orthogonal states of a qubit
form an information observable, and no union of such sets does. From §8,
with *X*, *Y* such a pair:

- **8a**: some *x* ∈ *X*, *y* ∈ *Y* have *x* ⊥̸ *y*. Otherwise IV, VI, III and
  VII make *X*∪*Y* an information variable.
- **8b**: whether *X* or *Y* is sharp cannot be measured, though it is
  ensemble-measurable by IX.
- **8c**: *X*∪*Y* is not clonable: cloning a pair {*x*, *y*} repeatedly would
  prepare *z*(∞), and IX would then distinguish *x* from *y*.
- **8d**: *X* and *Y* cannot be sharp together, nor measured together.
- **8e**: deterministic yet unpredictable. If *X* is maximal and the
  substrate has *y*, no prediction "the outcome will be *x*" is true, yet the
  Boolean observable {χ̄̄_y, χ̄_y} is sharp, so "whether the outcome is one of
  the *x* with *x* ⊥̸ *y*" is predictable ("yes"). The quantum case is the
  projector |0⟩⟨0|+|1⟩⟨1|+|2⟩⟨2| on photon number. "It is up to the
  subsidiary theories to *explain* this", and the Everettian explanation is
  that the measurer differentiates into instances "not all perceiving the
  same one".
- **8f** (8.1): (⋃_{x∈X_y} {(x, x0) → (x, 'x')} ∪ {(y, x0) → (y, k)})✗ for all
  *x*0, *k*: no device measures *X*_y non-perturbingly when it is sharp and
  leaves *y* unperturbed, and the perturbation is irreducible.
- **8g** (8.2)–(8.3): two consecutive non-perturbing measurements of a
  non-sharp *X* agree, in that the measurement of whether they agree is
  sharp "true".
- **8h**: each information observable of a quantum system is discrete, but
  there is a continuum of them, no union of which is one: "classical
  information is discrete, and superinformation (quantum information) is
  continuous."
- **8i**: coherence is defined (a computation on *v* ⊂ *w* is coherent if it
  can be performed reversibly on *w*). For two coherent superinformation
  media, the controlled-not (8.4) with its coherent extension (8.5) yields an
  information variable {(0,1), ψ(1)} of **M**1⊕**M**2 that cannot be
  measured by measuring products of local variables: locally inaccessible
  information. "The failure of local distinguishability is possible, because
  superinformation media *obey* the principle of locality II, not disobey it
  as has been supposed."

### Concluding remarks (§9)

The theory "reconciles apparently contradictory features of information:
that of being an abstraction, yet governed by laws of physics; of being
physical, yet counter-factual. And it robustly unifies the theories of
quantum and classical information."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Information variable, distinguishability and measurement can be defined from possible tasks alone, without circularity | strong | definitional; §§3–5 and the order of the definitions |
| C2 | Instantiating classical information is an exact, intrinsic, counterfactual property of a substrate | strong as the paper's own statement (§4); its "intrinsic" is the §2 sense, no reference to another *specific* substrate | textual |
| C3 | Principles III–IX are laws of physics | weak | conjectured; IV and V motivated by a photon example and an appeal to unifying explanation; VI and VII called simplifying assumptions |
| C4 | Given II–IX, a superinformation medium has indistinguishable information attributes, unclonable and jointly unsharp observables, deterministic unpredictability, irreducible disturbance and consistent repeated measurement | moderate | informal proofs in §8a–g; each step is stated, but some lean on principles in passing (8c cites "assumption VII" where preparability is VI) |
| C5 | Quantum information is an instance of superinformation | moderate | exhibited for qubits, photon number and the controlled-not (§§7, 8e, 8i); no claim that every superinformation theory is quantum |
| C6 | Locally inaccessible information is compatible with locality II | moderate | the §8i construction, resting on II's pair form and the coherence assumption |
| C7 | Fundamental laws cannot be stochastic; GPTs are at most emergent | weak to moderate | follows from principle I as the authors read it (§2); principle I is itself the conjecture |

## Concepts

- **Task** — a set of input→output pairs of attributes of a substrate,
  with the constructor abstracted away (§2).
- **Possible task** — one the laws allow to be performed arbitrarily
  accurately by something that keeps its ability arbitrarily well; no
  perfect constructor is required to exist (§2).
- **Constructor** — what causes a transformation and "remains unchanged in
  its ability to cause the transformation again"; a substrate on a loop is
  one (§2).
- **Principle** — "a law of physics that constrains other laws rather than
  the behaviour of physical objects directly" (§1), testable through its
  rivals (§2).
- **Intrinsic attribute** — one that refers to no other specific substrate
  (§2).
- **Information variable** — a set of attributes all of whose permutations,
  and whose cloning, are possible (with side-effects) (§4).
- **Observable** — a variable each of whose attributes *x* satisfies
  *x* = *x̄̄*; whenever a measurer gives a sharp '*z*', the input had *z*
  (§6a–b).
- **Superinformation** — a medium with disjoint information observables
  whose union is not one (§7).
- **Ensemble distinguishable** — told apart by experiments on **S**(*n*) as
  *n* grows without limit (§6c).

## Connections

- **Deutsch 2013, "Constructor theory"** (ref. [7]), of which this is an
  application; the composition principle VII is cited from it. Not held in
  the record.
- **Shannon 1948 and Weaver 1949** (refs [6], [1]): the paper's diagnosis is
  that Shannon assumes distinguishability and classical media.
- **Reconstructions of quantum theory** (Wootters 1981, Hardy 2001, Clifton,
  Bub and Halvorson 2003; refs [3]–[5]) and Wheeler 1989 [2] are cited as
  treating information as *a priori*, the opposite of this approach.
- **Generalized probabilistic theories** (Barrett 2007, ref. [12]) are
  placed at most at an emergent level. The record's introduction to GPTs is
  LIT-073; this paper is a rival frame to it on fundamentality, not a
  contribution to it.
- **Deutsch and Hayden 2000** (ref. [9]) for the Heisenberg-picture locality
  and for locally inaccessible information; Wallace and Timpson 2007 and
  Deutsch 2012 (refs [10], [11]) for the controversy footnote 3 sets aside.
- **Horsman et al. 2014, "When does a physical system compute?"** (ref.
  [15]) is cited only to say this paper does not take that question up (§3).
- **Bennett et al. 1999, nonlocality without entanglement** (ref. [17]),
  as a second effect of locally inaccessible information (footnote 7).

## Bearing on the record

- **CLAIM-tmpmand1: A11's two remarks, tested.** (i) *"Does not itself entail
  relational constitution."* That holds, and the text goes further. It
  calls instantiating classical information "an exact, intrinsic property of
  the substrate" (§4). Principle II exists to guarantee that "individual
  physical systems … *have* states and attributes" (§2). A relational
  attribute such as distance is an intrinsic attribute of the composite, not
  of either part. What an information medium is is fixed modally, by which
  tasks on it are possible, not by its relations to other entities. The
  cloning task does involve a second instance of the substrate, and
  measurement maps onto an information variable of some other medium
  (5.1, 5.2). But these are generic
  others, which is exactly what CT's "intrinsic" (no *specific* other
  substrate) allows. So constructor theory supplies a third option beside
  the claim's two: a dispositional or modal individuation of kinds that is
  neither relational constitution nor bare intrinsic natures. (ii) *"Could
  sharpen what Nucleation means by a constraint being real."* It can, by
  splitting the notion. In the paper "constraint" has two homes. A
  *principle* constrains other laws (§1) and is real in being testable
  through its rivals (§2). A *constructor* is a physical thing that keeps its
  ability to cause a transformation; it is only ever approximate, and it
  deteriorates. Constructor-theoretic statements abstract constructors away,
  and possibility requires no actual constructor: "No perfect constructors
  exist in nature" (§2). The claim's "realized and maintained by something"
  fits the constructor sense only. The individuating work in the paper,
  being an information medium, is done by possibility facts, which no
  particular thing realizes. That bears on the claim's defeater (b), a
  constraint "that does individuating work while realized by nothing". It is
  not a clean defeat, for two reasons. The work done is kind-level, which
  the claim's "partly" and A8 §5 already allow. And the paper treats the
  possibility facts as laws of physics, not as specifications prior to
  realization ("it only exists when it is physically instantiated", §1, of
  information). What the claim needs from this is a sentence saying whether a
  law of possibility counts as "something" that realizes a constraint. If it
  does, the recursion ends at the laws. If it does not, constructor theory
  is a candidate for defeater (b) at the level of kinds.
- **CLAIM-tmpmand1 and TERM-070: one line on loops.** "Loops are excluded,
  because a substrate on a loop is a constructor" (§2). Whether something is
  a substrate or a constructor depends on its place in a network. That is a
  role-relativity like A10 §7's "Constraint at level n ≈ realized
  organization at level n−1". The composition principle VII covers only
  loop-free networks. Montévil and Mossio's closure (TERM-070) is a cycle of
  dependencies among constraints, so on this reading it lies outside the
  network calculus the paper uses. The paper gives this one sentence and
  does not develop it; the comparison is the reader's.
- **TERM-070: a neighbour, not a correction.** The constructor's defining
  characteristic, that it "remains unchanged in its ability to cause the
  transformation again", with catalysts as the approximation (§2), is
  Montévil and Mossio's constraint (conserved in its relevant aspects at the
  time scale of the process it acts on) with the time scale idealized away.
  Constructor theory has no time (§2), and its persistence condition is a
  limit over repetitions, "including its own maintenance". If the TERM grows
  a "What it is not" for constructors, the difference is that one is
  relative to a time scale and the other is not.
- **CLAIM-tmpmx2ql: nothing in support; a contrast.** The paper has no
  time scales and no dynamics, so it neither supports nor bears against
  scale separation as a mechanism. Its constructor–substrate split is by role
  (unchanged ability versus transformed attribute), and the limit "no limit,
  short of perfection" stands in for what the claim would get from ε → 0.
  The paper does not draw that comparison. A constructor's persistence is
  consistent with the claim's defeater (a), which asks for constraints
  without anything more persistent, and supplies no instance of it.
- **CLAIM-150: the paper keeps the guard itself.** Its definitions identify
  (computation, information and distinguishability defined by possible
  tasks), and it says plainly that they do not carry the substance: "the
  most important properties of information do not follow from the
  definitions we have given" (§6). It also says "our claims in no way depend
  on" the defined notions matching the intuitive ones (§3). The substance is
  in the conjectured principles, offered as testable laws. It is a case, in
  physics, of the claim's separation between identification and what is
  asserted of the world. Nothing in CLAIM-150 changes.
- **THEORY-609: the question set aside.** Chalmers asks when a system
  implements a computation, with counterfactual-supporting transitions. The
  paper declines that project explicitly: "we are not taking computation to
  be an *a priori* concept and seeking necessary and sufficient conditions
  for a physical process to instantiate it (cf. [15])" (§3). Its computation
  variable is modal (every permutation is possible), but it is a property of a
  substrate under the laws, not an implementation condition for a given
  system. The two do not conflict; they answer different questions.
- **THEORY-030: consistent, at a different level.** The paper allows
  side-effects so that a logically reversible task "does not require the
  physical processes instantiating" it "to be reversible" (§3), and its
  cloning onto a fixed *x*0 is Bennett's copying onto a blank register. It
  says nothing about entropy or cost.
- **THEORY-453 and CLAIM-136: a physical framework that gives subsystems
  states.** Esfeld and Lam need primitive diversity where "nothing discerns"
  entangled systems. The paper's principle II gives each subsystem a state
  in the Heisenberg picture, and it treats entanglement as locally
  inaccessible information that obeys locality (§8i). In that picture the
  local states are observables (footnote 3). This is a non-eliminative
  frame for entangled relata, but it says nothing about their numerical
  identity. It is a neighbour to the record's choice, not support for it.

## Limitations

- Principles III–IX are conjectures. IV and V rest on a photon-number
  example and an appeal to unifying explanation, and VI and VII are
  idealizations the authors say they do not need.
- The §8 proofs are informal and depend on several principles at once.
  §8c cites "assumption VII" for repeated cloning where the preparability it
  uses is VI. §8e cites "the properties of observables (§6)", meaning §6b.
- The paper does not show that every superinformation theory is quantum
  theory, only that quantum information is an instance. Superinformation
  is defined by one prohibition, and the paper does not ask what else it
  admits.
- "Intrinsic" means no reference to another *specific* substrate. Clonability
  and distinguishability are defined using generic other substrates, so the
  intrinsicness of C2 is a modal intrinsicness, and a reader who means "not
  involving anything else" will find the claim weaker than it sounds.
- Figure 1 was not seen, only its caption. The not-distinguishable sign is
  lost in both sources and restored here from context. The arXiv copy (July
  2014) differs in wording from the published text, for instance in the
  abstract and in (1.1), where the receiver starts in *x*0 rather than *b*.

## Open questions

- Whether a law of possibility counts as something that realizes a
  constraint, or as a constraint that nothing realizes (CLAIM-tmpmand1's
  defeater (b)).
- What the constructor-theoretic counterpart of a closed set of constraints
  would be, given that loops make substrates into constructors and the
  composition principle covers only loop-free networks.
- Whether superinformation, defined by the single prohibition, singles out
  quantum theory or admits other theories, and which.
