---
status: Read
paper: LIT-tmp57r0s
title: 'Rovelli — Relational quantum mechanics'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from the arXiv preprint, quant-ph/9609002v2 (24 Feb
    1997), 21 PDF pp., not from the version in the International Journal
    of Theoretical Physics 35 (1996), 1637–1678, which I have not seen.
    The text was extracted with `pdftotext`, with and without `-layout`;
    the two-column layout interleaves columns in the extraction, and I
    read the passages in their sense order. I read the abstract, §§I–IV
    with all subsections, the eight footnotes, the acknowledgments and the
    reference list. Locations are sections and PDF pages. Differences I
    cannot check: v2 postdates the journal issue (August 1996), so v2 may
    carry revisions the journal text lacks, and the acknowledgments thank
    readers "for discussions and comments on the first version of this
    work"; the footnote headed "Note added" (p. 16) is a likely candidate.
    The journal's pagination is not mapped. The PDF's date line, "November
    26, 2024", is arXiv's recompilation date, not the paper's. Some
    equation numbers are garbled in the extraction (§III.C), and the
    formulas there are read from the PDF's sense, not its numbering.
date: '2026-10-27'
summary: >-
  Rovelli proposes that the incorrect notion behind the measurement problem
  is the observer-independent state of a system, as absolute simultaneity
  was behind the unease with the Lorentz transformations. Two descriptions
  of one measurement, by the measuring system O and by an external P who
  treats S+O unitarily, are both correct, so "q = 1" is elliptic for "q = 1
  relative to O", any physical system can be the observer, and the theory,
  taken as complete, is about the information (correlation) systems have
  about one another. The relation between two observers' views is itself a
  quantum fact relative to a third, so no view can be deduced from another
  and there is no description in toto. Values are relational; systems are
  not: the world is assumed decomposed into systems, each characterized by
  its set of yes/no questions W(S) and an information capacity N. Two
  information postulates give an orthomodular lattice, and a third
  (superposition) postulate is needed for the Hilbert-space formalism; the
  reconstruction is, in the author's words, "not fully successful".
---
<!-- inactive-ok-file: CLAIM-136 CLAIM-137 CLAIM-tmpmand1 THEORY-621 THEORY-tmpwbcq0 TERM-tmp0est4 THEORY-tmpleurt — Proposed; the entries the reading bears on, cited as open -->
<!-- inactive-ok-file: LIT-tmplkyox — Unavailable; cited only as Rovelli cites it -->

# NOTE-tmptc0hl: Rovelli — Relational quantum mechanics

## Contribution

The founding statement of relational quantum mechanics. It turns one
textbook measurement, described twice, into the thesis that the state of
a system and the values of its variables exist only relative to another
system, and it makes that thesis the interpretation: no special observers,
no collapse mechanism, no hidden variables, and quantum mechanics taken as
complete. It also proposes a programme, to derive the formalism from a few
physical postulates as Einstein derived the Lorentz transformations, and
carries it part of the way with two information postulates and a third
that it does not motivate physically.

## Key insight

Velocity is a relation to a reference body, and the reference body "can be
a table lamp" (§I, p. 3). Rovelli asks that every quantum value be read the
same way: "the electron has spin up" is elliptic for "the electron has spin
up with respect to the Stern Gerlac apparatus" (§II.C, p. 7). O's account
(S collapsed to |1⟩, q = 1) and P's (S–O entangled, q without a value) are
"two distinct correct descriptions of the same sequence of events" (§II.A,
p. 4). What is relational is the *state* and the *value*; what bears them
is a system, given beforehand and characterized by the questions that can
be asked of it (§III.A, pp. 10–11).

## Assumptions

- **Hypothesis 1, all systems are equivalent** (§II.A, p. 4): "Nothing
  distinguishes a priori macroscopic systems from quantum systems." "Of
  course, I have no proof of hypothesis 1, only plausibility arguments."
- **Hypothesis 2, completeness** (§II.C, p. 7): "Quantum mechanics
  provides a complete and self-consistent scheme of description of the
  physical world, appropriate to our present level of experimental
  observations."
- **The world is decomposable into systems** (§III.A, p. 10): "Assume that
  the world can be decomposed (possibly in a variety of ways) in a
  collection of systems, each of which can be equivalently considered as an
  observing system or as an observed system." Not argued.
- **Finite-dimensional Hilbert spaces** (§III.A, p. 11), "to simplify the
  mathematical treatment"; "Generalization to infinite systems should not
  be difficult" (p. 11), not done.
- **Information is Shannon's**: "a measure of the number of states in which
  a system can be –or in which several systems whose states are physically
  constrained (correlated) can be" (§I, p. 3); no meaning, storage or
  purpose (§II.E, p. 10).
- **The symmetry p(Q_b^(i), Q_c^(j)) = p(Q_c^(j), Q_b^(i))**, flagged "a new
  assumption! … I leave it here as an unjustified assumption at this stage"
  (§III.C, p. 13).
- **Probability is left uninterpreted**; the view is said to work on an
  objective or a subjective reading (footnote ‡, p. 13).

## Key results

### §I: the programme (pp. 1–3)

The thesis: the notion rejected is "the notion of absolute, or
observer-independent, state of a system; equivalently, the notion of
observer-independent values of physical quantities" (p. 1). The analogy is
Einstein's reading of the Lorentz transformations: their formalism existed,
the interpretation was the contribution, and it came by re-derivation from
"two postulates with terse physical content" (p. 2). The programme has
three steps: find experimentally true postulates, show they refute a common
assumption, derive the formalism from them (p. 2). "In this paper, I do
not achieve such a result in a satisfactory manner" (p. 2). Terminology:
an "observer" is any physical object; information is Shannon's, and "a pen
on my table has information because it points in this or that direction"
(p. 3).

### §II.A: the third-person problem (pp. 3–4)

O measures q on S in the state α|1⟩ + β|2⟩ and gets 1. O's description:
α|1⟩ + β|2⟩ → |1⟩ (eq. 1). P, who knows the initial states and does not
interact with S–O between t1 and t2, describes it unitarily:
(α|1⟩ + β|2⟩) ⊗ |init⟩ → α|1⟩ ⊗ |O1⟩ + β|2⟩ ⊗ |O2⟩ (eq. 2). Quantum
mechanics "requires us to distinguish system from observer, but it allows
us freedom in drawing the line that distinguishes the two" (pp. 3–4).
**Main observation**: "In quantum mechanics different observers may give
different accounts of the same sequence of events" (p. 4), credited also to
Zurek 1982 and Kochen 1979.

### §II.B: eight objections (pp. 4–6)

Special collapse-producing systems (gravity, minds, macroscopic objects)
violate Hypothesis 1 and predict interference discrepancies, small because
of decoherence but "different from zero, and thus observable" (p. 4).
Taking only outcomes as physical does not help: for P q has no value at
t2, for O it does (p. 5). "P is right, O wrong" would mean no measurement
has ever been made; "O right, P wrong" predicts unobserved discrepancies
(p. 5). Decoherence cannot make q = 1 absolute, because "decoherence
depends on which observation P will make" (p. 5). No-collapse without
values cannot match observation (Objection 6, p. 5). Everett's branching
needs a preferred apparatus and basis, violating Hypothesis 1, or turns
into histories (p. 5). Consistent histories make the probabilities
observer-independent but the frameworks available to O and P differ,
because "what is data for O is only a possible choice of framework for P"
(Objection 8, pp. 6–7).

### §II.C: the relational thesis (pp. 6–7)

"A quantum description of the state of a system S exists only if some
system O (considered as an observer) is actually 'describing' S, or, more
precisely, has interacted with S. The quantum state of a system is always a
state of that system with respect to a certain other system" (p. 6). "In
quantum mechanics all physical variables are relational, as is velocity"
(p. 6). With completeness: "Quantum mechanics is a theory about the
physical description of physical systems relative to other systems, and
this is a complete description of the world" (p. 7). So "a complete
description of the world is exhausted by the relevant information that
systems have about each other. Namely, there is neither an absolute state
of the system, nor absolute properties that the system has at a certain
time" (p. 7), and "the notion of a universal description of the state of
the world, shared by all observers, is a concept which is physically
untenable, on experimental ground" (p. 7).

### §II.D: the relation between descriptions (pp. 7–9)

- "The absolute state of affairs of the world is a meaningless notion …
  In particular, there is no way of deducing the view of one from the view
  of the other" (p. 8). The relation between views "must be addressed
  within the view of one of the two observers (or of a third one)" (p. 8),
  because "the process of comparison is always a physical interaction, and
  all physical interactions are quantum mechanical in nature" (p. 8).
- **That O has measured is a P-relative quantum property.** P can know
  *that* O knows q, not *what* O knows (p. 8). The operator M on H_S ⊗ H_O
  (eq. 3), M(|1⟩⊗|O1⟩) = |1⟩⊗|O1⟩, M(|2⟩⊗|O2⟩) = |2⟩⊗|O2⟩, and 0 on the
  mismatched products, asks "Is the pointer correctly correlated to q?";
  the state (2) is its eigenstate with eigenvalue 1 (p. 8).
- **No half-measurements.** If S–O is not an eigenstate of M, "there is no
  half-a-measurement; there is probability one-half that the measurement
  has been made!" (p. 8), because "whether or not O has measured S is not
  an absolute property of the S − O state, but a quantum property of the
  quantum S − O system" (pp. 8–9). The bi-orthogonal decomposition always
  supplies some such M, which Rovelli dismisses as of "null practical nor
  theoretical significance" (p. 9).
- **Consistency.** If P measures q and then O's pointer, the results are
  correlated, "as was first noticed by von Neumann, and as is clear from
  (2)" (p. 9).

### §II.E: information (pp. 9–10)

"q has a value relative to O" means "relative to P, there is a certain
correlation in the S and O states", or "O has information about q" (p.
10). Information "can be lost dynamically"; purposeful and accidental
correlation are not distinguished; and "any physical system may contain
information about another physical system", so two spin-½ particles with
equal spin have information about each other (p. 10). "Observers are not
'physically special systems' in any sense" (p. 10). The answer "only
shifts the problem by one step" (p. 10). "Physics is the theory of the
relative information that systems have about each other. This information
exhausts everything we can say about the world" (p. 10).

### §III.A–B: questions and the two postulates (pp. 10–12)

- A system S "viewed as an observed system, is characterized by the family
  of yes/no questions that can be asked to it", W(S) = {Q_i}, the
  observables (p. 10); "The general kinematical features of S are
  representable as relations between the questions Q_i in W(S), that is,
  structures over W(S)" (p. 11). O's information about S is a binary string
  (e1, e2, …) (eq. 4); the *relevant* information is the part that bears on
  future answers (p. 11).
- "A notion does not appear here: the state of the system. The absence of
  this notion is the prime feature of the interpretation considered here.
  In place of the notion of state, which refers solely to the system, the
  notion of the information that a system has about another system has
  been introduced" (p. 11). Footnote †: "The string (5) is essentially the
  state … The novelty is that this notion of state is relative to the
  observer that has asked the questions" (p. 11).
- **Postulate 1 (limited information)**: "There is a maximum amount of
  relevant information that can be extracted from a system" (p. 11). So
  "each system is characterized by a number N", the least integer with
  N ≥ log₂ k, k the Hilbert-space dimension (p. 11). Planck's constant is
  then "the transformation coefficient between physical units (position ×
  momentum) and information theoretical units (bits)" (p. 12).
- **Postulate 2 (unlimited information)**: "It is always possible to
  acquire new information about a system" (p. 12). With Postulate 1, a new
  undetermined question costs at least one old bit, and the answers "cannot
  be fully deterministic" (p. 12).

### §III.C: the reconstruction and the third postulate (pp. 12–14)

From Postulate 1, with the "(non-trivial) additional assumption" that ∨ and
∧ are defined for every pair, W(S) is an orthomodular lattice (p. 12),
containing Boolean algebras generated by the 2^N "complete questions" of
each family of N independent questions (eqs. 6–8, pp. 12–13). The
transition probabilities p_ij satisfy 0 ≤ p_ij ≤ 1 and row and column sums
of 1 (eqs. 10–12; the PDF prints "0 ≥ p_ij ≥ 1", a typo), which are met by
p_ij = |U_ij|² for a unitary U not fixed by p_ij (eq. 13). The phases are
fixed by composite questions, p_{i(jk)i} = |U_ij U_ji + U_ik U_ki|² (eq. 17),
"(experimentally!)" not the classical sum (p. 13). **Postulate 3
(superposition)**: the unitaries U_cb can be chosen with U_cd = U_cb U_bd
and composite questions given by eq. 17 (p. 14). Then "the conventional
formalism of quantum mechanics as well as the standard probability rules
follow completely from the three postulates" (p. 14); dynamics follows by
labelling questions by time, giving U(t) = exp{−i t H} (p. 14). The
reconstruction "is not fully successful" (p. 12), and Rovelli suspects that
inter-observer consistency "could be taken as the missing input" but has
"no definite result" (p. 14).

### §III.D: the observer observed (pp. 14–15)

"A statement about the information possessed by O is a statement about the
physical state of O", so it too is relative to a further observer (p. 14).
Knowing W(S) includes knowing the Hamiltonian, "because W(S) includes all
Heisenberg observables at all times" (p. 15). For P the measurement is a
unitary evolution with a non-vanishing interaction Hamiltonian; O's unitary
description of S breaks down "simply because O is not giving a full
dynamical description of the interaction", and "there is no meaning in
being correlated with oneself" (p. 15). Two rules, which if kept mean "there
is no way in which contradiction may develop" (p. 15): "(i) There is no
meaning to the state of a system or the information that a system has,
except within the information of a further observer"; "(ii) There is no way
a system P may get information about a system O without physically
interacting with it". The no-contradiction claim is left to the reader ("The
reader may convince himself"), not proved.

### §IV.A: summary (pp. 15–16)

"A physical system is characterized by the structure on the set W(S) of
questions that can be asked to the system" (p. 16). "The properties of the
systems are to be described by an interrelated net of observations and
information collected from observations" (p. 16). A description in toto by
a further observer is "deficient in two directions: upward, because an even
more general observer is needed to describe the global observer itself,
and –more importantly– downward, because the in toto observer knows the
content of the information that the single component systems possess about
each other only probabilistically" (p. 16). "Any observation requires an
observer", from Maturana and Varela (p. 16). The thesis restated: "Quantum
mechanics is the theoretical formalization of the experimental discovery
that the descriptions that different observers give of the same events are
not universal" (p. 16).

### §IV.B: other interpretations (pp. 16–19)

- **Dynamics** (GRW, Penrose): violate Hypothesis 2. "My effort here is not
  to modify quantum mechanics to make it consistent with my view of the
  world, but to modify my view of the world to make it consistent with
  quantum mechanics" (p. 16).
- **Bohr**, as one reading of Copenhagen, "assumes a classical world …
  physically distinct from the microsystems" (p. 17). Fixing a privileged
  system S_o, "The Observer", recovers Bohr's view: "Bohr's choice is simply
  the assumption of a set of systems (the classical systems) as privileged
  observers. This is consistent with the view presented here" (p. 17).
  "There is nothing incorrect in fixing the preferred observer S_o once and
  for all", and quantum mechanics is used "precisely as is it is currently
  used" (p. 17). Footnote **: why S_o admits a classical description is
  decoherence's question (p. 17).
- **The projection postulate** is explained: unitary evolution breaks down
  because S interacts with something its equations omit; after Ashtekar,
  the view prohibits an observer "to be able to give a full description of
  'itself'", and Breuer's no-complete-self-measurement theorem is named as
  related (p. 17).
- **Modal interpretations**: RQM keeps value assignment but makes it
  observer-dependent and lets it break unitarity relative to the observer,
  so "there is collapse in each observer-dependent evolution of expected
  probabilities", and "For a fixed observer, the eigenstate-eigenvalue link
  is maintained" (p. 17). "Actuality is observer dependent" (p. 17).
- **Consistent histories**: the distinction between a probability-one
  property in a framework and a datum is what CH leaves unexplained; "there
  are no (observer independent) data at all" (p. 18).
- **Many worlds**: Everett's universal wave function "represents the
  perspective of a non-existent observer"; "There is no description of the
  universe in-toto, only a quantum-interrelated net of partial descriptions"
  (p. 19). The extra values are "'somehow perspectival' (but definitely not
  mental!)" and "'wholly a matter of physics'" as relativity of
  simultaneity is (p. 19).
- "Bohr's interpretation, consistent histories interpretations, as well as
  the many worlds interpretation, are all correct" from this view; the
  closest is Heisenberg's (p. 19). Zurek 1982 is quoted as having reached
  "identical" conclusions: "correlations between the properties of quantum
  systems are more basic that the properties themselves" (p. 19).
- Footnote ‡‡ (p. 19): Rovelli declines "to venture into philosophical
  terrains", cites Kant ("entirely made up of mere relations") and notes
  that observer-independence has become "almost a commonplace" from
  anthropology to continental philosophy.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | O's and P's accounts of one measurement are both correct, so values are observer-relative | moderate | the two-description analysis (§II.A) and the rebuttal of eight objections (§II.B); conditional on Hypotheses 1 and 2, which are assumed, the first with "only plausibility arguments" |
| C2 | Any physical system can be an observer | strong (as a definition) | information as Shannon correlation (§II.E, p. 10); it is the paper's stipulation, consistent with Hypothesis 1 |
| C3 | That O has measured S is a P-relative quantum property, which dissolves the "precise moment of measurement" problem | moderate | the operator M (eq. 3) and the probabilistic reading of non-eigenstates (§II.D, pp. 8–9) |
| C4 | No contradiction arises among observers' descriptions if rules (i) and (ii) are kept | weak | shown for the S–O–P correlation case (von Neumann, p. 9); in general left to the reader (§III.D, p. 15) |
| C5 | Two information postulates give W(S) the structure of an orthomodular lattice with Boolean subalgebras | moderate | sketch with "(non-trivial) additional assumption[s]" and quantum-logic results cited, not proved (§III.C, p. 12) |
| C6 | The Hilbert-space formalism and Born rule follow from three postulates | weak | Postulate 3 builds in the unitary composition and eq. 17; a symmetry is assumed unjustified; the author calls the reconstruction "not fully successful" (pp. 12–14) |
| C7 | Planck's constant converts phase-space units into bits | weak | dimensional argument from Postulate 1 (pp. 11–12) |
| C8 | Bohr, consistent histories and many worlds are all correct, each a special or partial case | weak | §IV.B, by redescription; no derivation |
| C9 | The theory is about systems already given: a system is characterized by W(S) and N, its values are relative | strong (textual) | §III.A, pp. 10–11; §III.D, p. 15; §IV.A, p. 16 |

## Concepts

- **Observer** — any physical system, in the sense of the reference body
  of Galilean relativity (§I, p. 3); "with more than one state" (p. 10).
- **Information** — Shannon's: correlation that reduces the joint
  alternatives of two systems (§II.E, pp. 9–10). "O has the information
  that q = 1" is the paper's "lexical move" for "q = 1 relative to O" (p. 9).
- **Relevant information** — the part of the record of answers that bears
  on future answers (§III.A, p. 11).
- **W(S)** — the family of yes/no questions that can be asked of S, which
  characterizes it (§III.A, pp. 10–11).
- **Information capacity N** — the maximal relevant information about S,
  N ≥ log₂ k (§III.B, p. 11).
- **Relative state** — the string of O's answers about S, "essentially the
  state" but "relative to the observer that has asked the questions"
  (footnote †, p. 11).
- **Main observation** — different observers may give different accounts
  of the same sequence of events (§II.A, p. 4).

## Connections

- **Rovelli's later account ([LIT-177](../literature.d/LIT-177.md), read in [NOTE-174](NOTE-174.md))**. The 1996 paper has
  no "facts" or "events" vocabulary and no sparse ontology: its primitives
  are systems, questions and information, and its relative state is the
  record of answers. The later chapter's "core idea", that amplitudes give
  probabilities only between facts relative to the same system, appears
  here as "For a fixed observer, the eigenstate-eigenvalue link is
  maintained" and "there is collapse in each observer-dependent evolution"
  (p. 17), not as a probability rule. The 1996 postulates are stated for
  finite-dimensional Hilbert spaces (N ≥ log₂ k), not for compact phase
  space; there are three, not two, and the third is admitted to lack a
  physical meaning. In 1996 Bohr's view is "consistent" with RQM, a
  privileged-observer special case (p. 17); the 2021 chapter's charge that
  Copenhagen and QBism build on an approximation is not here.
- **Faye and Jaksland ([LIT-tmpstodb](../literature.d/LIT-tmpstodb.md), [NOTE-tmpdn71t](NOTE-tmpdn71t.md))** cite this paper for the
  freedom in drawing the line (pp. 3–4) and for O's inability to describe
  its own interaction (p. 15); both are accurate. Their "sparse ontology"
  and "systems precede the interactions" are quoted from later texts; see
  Bearing.
- **Grangier and Auffèves ([NOTE-044](NOTE-044.md))** list this paper as a rival
  reconstruction (their ref. [11]).
- **Maturana and Varela** ([LIT-tmplkyox](../literature.d/LIT-tmplkyox.md), Unavailable): "Any observation requires
  an observer" is "freely taken" from them (p. 16). The in-text citation
  reads "1920"; the reference list gives 1980.
- **Zurek 1982 and Kochen 1979** are credited with the same conclusion (pp.
  4, 19); neither is held.

## Bearing on the record

- **[THEORY-tmpggk6i](../theory.d/THEORY-tmpggk6i.md): the attribution holds of the founding paper, as an
  assumption.** Faye and Jaksland's words, "a sparse ontology of
  (relational) quantum events" and "the systems precede the interactions",
  are not in the 1996 text, which has no ontology of events. But the 1996
  paper does keep systems prior to the values: "Assume that the world can be
  decomposed (possibly in a variety of ways) in a collection of systems"
  (p. 10), each "characterized by the family of yes/no questions that can be
  asked to it" (p. 10), with "a number N" (p. 11) and, through W(S), its
  Hamiltonian (p. 15). A state exists "only if some system O … has
  interacted with S" (p. 6): the interaction presupposes the two systems.
  Two qualifications: the priority is assumed, never argued; and the
  decomposition is not unique ("possibly in a variety of ways"), so the
  systems are prior to interactions without being uniquely given. Filed as
  [THEORY-tmpduhhr](../theory.d/THEORY-tmpduhhr.md).
- **[CLAIM-136](../claims.d/CLAIM-136.md): a physical case of relational properties with relata
  characterized, not individuated, apart from them.** All values are
  relational ("all physical variables are relational, as is velocity", p.
  6), but what characterizes a system, W(S) and N, is not relative to any
  observer. W(S) fixes a system's *kind* (a lattice of subspaces of a
  k-dimensional Hilbert space); nothing in the paper says what makes two
  systems of the same kind two. That is the claim's open question in a
  physical key, and the 1996 text neither poses nor answers it. RQM in 1996
  is non-eliminative, as the claim is, and closer to the weak version only
  by silence.
- **[CLAIM-tmpmand1](../claims.d/CLAIM-tmpmand1.md): W(S) is the set of questions that can be asked.** A
  system is characterized by the interactions it can enter as an observed
  system, its admissible questions and their lattice relations, which is
  near the claim's "partly fixed by the constraints on the configurations
  of entities and relations it can enter". Rovelli does not say the
  questions constitute the system; he says they characterize it, and the
  decomposition into systems is assumed first. The note's "Rovelli's
  relational quantum mechanics is a second non-eliminative case" stands on
  the 1996 text.
- **[QUESTION-021](../questions.d/QUESTION-021.md): Rovelli's relativity analogy refuses the invariant.**
  A18's first horn borrowed relativity's structure, "an invariant object
  underlying coordinate-dependent descriptions". Rovelli's analogy is the
  same one (simultaneity, velocity), and he breaks it at exactly that
  point: "there is no way of deducing the view of one from the view of the
  other" (p. 8), the relation between views is itself relative to a third
  system, and "There is no description of the universe in-toto, only a
  quantum-interrelated net of partial descriptions" (p. 19). What is
  frame-independent is the system's kind, W(S), not any state of it. That
  is the second horn for states and something like [CLAIM-137](../claims.d/CLAIM-137.md)'s
  frame-independent kind for systems. It bears on the question by analogy
  only. Filed as [THEORY-tmpleurt](../theory.d/THEORY-tmpleurt.md).
- **[CLAIM-150](../claims.d/CLAIM-150.md): the founding paper concedes the underdetermination.** The
  relational thesis follows from the main observation only "whatever view
  of quantum theory (consistent with hypothesis 1) one holds" (p. 6) and with
  completeness assumed (p. 7). Bohm's theory, which violates Hypothesis 2,
  is not refuted but set aside (p. 17), and "the considerations in this
  paper do not suggest any modification to the conventional use of quantum
  mechanics" (p. 17). So the paper's own form is an interpretive argument
  under two hypotheses, not an entailment from the predictions, which is the
  claim's point.
- **[THEORY-tmpwbcq0](../theory.d/THEORY-tmpwbcq0.md): what Barad cannot borrow is the relativization, not a
  disentangling.** In 1996 RQM, relative to P the S–O system stays
  entangled through the measurement (eq. 2), exactly as Barad says it stays
  (2007, 348, as Faye and Jaksland quote it). What RQM adds is that relative
  to O, q = 1, and that "whether or not O has measured S is not an absolute
  property of the S − O state" (pp. 8–9). The difference from agential
  realism is that Barad's entanglement is absolute and RQM's is relative to
  P. The theory's wording, "treatment of the wave function as bookkeeping",
  is compatible with the 1996 text ("A notion does not appear here: the
  state of the system", p. 11), but "bookkeeping" is the later vocabulary.
- **[THEORY-621](../theory.d/THEORY-621.md): the 1996 form of its rule, and of its gap.** The promote_when
  asks for a result that relative facts cohere. The 1996 paper supplies one
  case (P's later measurements of q and of O's pointer agree, p. 9) and
  asserts the general case under rules (i) and (ii) without proof (p. 15).
  It does not derive the rule from independent principles: it assumes it.
- **[TERM-tmp0est4](../terms.d/TERM-tmp0est4.md) and [THEORY-tmpixkwj](../theory.d/THEORY-tmpixkwj.md): Rovelli reads Bohr's cut as
  physical.** "Bohr declares explicitly that we must renounce giving a
  quantum description of the classical world" (p. 4); "In Bohr's view, this
  classical world is physically distinct from the microsystems" (p. 17),
  hedged "at least in one possible reading". That is the ontological
  reading of Bohr's fixed cut that Faye and Jaksland reject for an
  epistemic one. Rovelli's own cut is movable ("freedom in drawing the
  line", pp. 3–4) and, unlike Barad's, not ontological: it is the choice of
  which system's information is being described.
- No ML-practice content; nothing here bears on the anthology.

## Limitations

- Hypothesis 1 has "only plausibility arguments"; Hypothesis 2 is assumed
  (pp. 4, 7). The relational conclusion is conditional on both.
- The reconstruction is incomplete by the author's account: Postulate 3 is
  "the more modest step" (p. 14), and the symmetry of p is unjustified (p.
  13). The "derivation" of the formalism is a sketch.
- Inter-observer consistency is shown for one case and asserted in general
  (p. 15).
- The paper declines philosophy (footnote ‡‡, p. 19). What a system is,
  and whether the decomposition into systems is itself relative, are not
  discussed beyond "possibly in a variety of ways".
- Read in arXiv v2; the journal text is unchecked (see history).

## Open questions

- Is the decomposition into systems itself relative to an observer, as the
  states are? The paper allows several decompositions and says nothing of
  how they relate.
- Can inter-observer consistency replace Postulate 3, as Rovelli suspects
  (p. 14)?
- Does the information-capacity characterization survive the
  infinite-dimensional case, which "should not be difficult" (p. 11)?
