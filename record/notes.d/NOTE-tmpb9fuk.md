---
status: Read
paper: 'LIT-tmpi254m'
title: 'Defaults in Update Semantics'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the author's copy on his University of Amsterdam
    staff page (43 pages, author's typesetting, extracted with
    pdftotext), not the journal's typeset text, so page numbers here are
    the copy's. Sections 1–6, all definitions, propositions and worked
    examples, the footnotes and the references read. The propositions are
    stated without proof in the paper (Lemma 2.5, Propositions 1.2, 1.3,
    2.6, 3.6, 3.7, 4.7, 4.10, 4.12, 4.14); the worked examples of §4–5
    were followed, not re-derived. The diagrams of expectation patterns
    survived extraction only as scattered world numbers and were
    reconstructed from the text.
date: '2026-10-09'
summary: >-
  Sets out update semantics (meaning as change of information state),
  proves a dynamic system reduces to static propositions exactly when
  updates are total, idempotent, persistent, monotone and strengthening,
  and shows epistemic "might" and "presumably" are tests that fail
  persistence. Gives a decidable non-monotonic logic of default rules in
  which specificity and other priorities follow from coherence and
  applicability conditions, with predictions that differ from Reiter's,
  Delgrande's, Asher and Morreau's and inheritance-net theories.
---
<!-- inactive-ok-file: LIT-tmpeftz9 — Deferred, no lawful full text; named as the origin of the dynamic view the paper credits -->
<!-- inactive-ok-file: THEORY-tmp5ncrn — Proposed; filed from this reading with two others -->
<!-- inactive-ok-file: CLAIM-tmphg89g — Proposed; open, and cited as open: the claim is under test, not settled -->

# NOTE-tmpb9fuk: Defaults in Update Semantics

## Contribution

Two things. First, a compact statement of update semantics as a framework,
with a criterion for when it matters: an update system is equivalent to a
static, truth-conditional one exactly when it is additive, and additivity
fails precisely for sentences, like epistemic *might*, whose effect depends
on the state they meet. Second, a semantics for default rules ("P's
normally are Q", "if φ then normally ψ") in which conflicts between rules
are resolved by what the rules mean, not by a priority ordering added on
top, and which yields a decidable consequence relation with predictions
that differ, case by case, from every rival the author compares.

## Key insight

Some sentences do not tell you about the world; they ask your information
state a question. "Might φ" passes if φ is still open and fails otherwise;
"presumably φ" passes if φ holds in every most-normal world you cannot
rule out. Because they test rather than inform, they can be accepted now
and rejected after more is learnt, and that non-persistence, not any
special mode of reasoning, is where non-monotonic inference comes from.
Default rules themselves are ordinary persistent information, about
normality rather than fact.

## Assumptions

- **Finite propositional language**: a finite set A of atoms; worlds are
  subsets of A (W = ℘(A)), so every logic here is decidable. Lemma 2.5 and
  Proposition 2.6 show the choice of A does not matter.
- **Information states as elimination**: in §2 a state is a set of worlds;
  in §3 a pair ⟨ε, s⟩ of an expectation pattern (reflexive, transitive
  relation on W) and a set of worlds; in §4 a pair ⟨π, s⟩ of a frame (a
  pattern πd for every d ⊆ W) and a set of worlds.
- **No revision**: an update that would be inconsistent yields the absurd
  state 1; the system says when revision is needed but not how to do it.
- **Knowledge, not belief**: states are what the agent takes to be
  knowledge (fn. 3).
- **One situation**: s is knowledge of the actual situation at one time,
  so "normally it rains, but not today; tomorrow presumably it will" is
  outside the system (fn. 4).
- **Restricted syntax**: *might*, *presumably* and *normally* occur only
  outermost, over sentences of the base language.

## Key results

- **Proposition 1.2.** ⟨L, Σ, [ ]⟩ is additive iff Σ is an information
  lattice on which [ ] is total and Idempotence (σ[φ] ⊩ φ), Persistence
  (σ ⊩ φ and σ ≤ τ ⇒ τ ⊩ φ), Monotony (σ ≤ τ ⇒ σ[φ] ≤ τ[φ]) and
  Strengthening (σ ≤ σ[φ]) hold.
- **Proposition 1.3.** In an additive system valid₁ (from the minimal
  state), valid₂ (from every state) and valid₃ (acceptance-preserving)
  coincide. In general they do not; valid₁ satisfies Sequential Monotony,
  Sequential Cut and Reflexivity, which characterise it under
  Idempotence (citing van Benthem 1991).
- **Definition 2.3 and Examples 2.7.** σ[might φ] = σ if σ[φ] ≠ 1, else 1.
  "might ¬p, p" is consistent; "p, might ¬p" is not. Both right and left
  monotonicity fail. The base language without *might* is additive and
  its logic is classical (Lemma 2.8).
- **Definition 3.9.** σ[normally ψ] refines ε by ‖ψ‖ (removing pairs
  ⟨v, w⟩ with w ∈ ‖ψ‖, v ∉ ‖ψ‖), absurd if no normal world satisfies ψ;
  σ[presumably ψ] = σ if all optimal worlds of s satisfy ψ, else 1.
  Normally p ⊩ presumably p; normally p, ¬p ⊮ presumably p but ⊩
  normally p (Examples 3.10). Rules are idempotent, persistent and
  monotone (Lemma 3.12); *presumably* is neither persistent nor monotone.
  "normally" validates conjunction of rules and necessitation but not
  normally φ ⊩ φ or normally φ ⊩ normally (φ ∨ ψ).
- **§4.** "If q, normally ¬p" is not definable from unary *normally*
  (normally(q ⊃ ¬p) creates an ambiguous state). Restricted rules refine
  the pattern of their own domain (Definition 4.6); a frame is coherent iff
  every nonempty domain has a normal world (4.3), with Proposition 4.7
  giving when a refinement stays coherent. A set of defaults applies within
  s iff every domain above s has a normal world complying with all of them
  (4.9); Proposition 4.12 puts the existential quantifier over refinements
  outside the universal over defaults. Optimal worlds are those complying
  with a maximal applicable set (4.13); Proposition 4.14 restricts the
  search to the explicitly given defaults.
- **Worked consequences (4.11, §5).** Specificity: normally p, q ~> ¬p, q
  ⊩ presumably ¬p, and an exception to the exception restores p. Nixon
  diamond: neither presumably r nor presumably ¬r. Students/adults/employed:
  presumably adult and not employed (Reiter gives two extensions; this
  theory one). Defeasible modus tollens (p ~> q, ¬q ⊩ presumably ¬p), with
  modus ponens taking precedence over it in a cycle. Independence holds,
  which selection-function theories (Delgrande; Asher and Morreau) lose.
- **Failures for ~>.** Hypothetical syllogism, contraposition and
  strengthening the antecedent fail; of the variable-strict principles
  only Conditional Identity and Conjunction of Consequents hold, while
  Weakening the Consequent, ASC and Disjunction of Antecedents hold only
  defeasibly, defeatable by facts alone.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A dynamic semantics is reducible to a static one exactly when it is additive, characterised by totality and four structural principles | strong (stated proposition) | Proposition 1.2; proof not given |
| C2 | Epistemic *might* and *presumably* are tests on information states and are non-persistent, so their content is not a proposition | strong within the model | Definitions 2.3, 3.9; Examples 2.7, 3.10 |
| C3 | Default rules carry context-independent (persistent) information; only the conclusions drawn from them are defeasible | strong within the model | Lemma 3.12 |
| C4 | Priority between conflicting defaults, including specificity, is a consequence of the meaning of the rules (coherence and applicability), not an extra stipulation | moderate | §4 definitions and worked examples; argued by cases, not by a general theorem about priority |
| C5 | The theory's predictions differ from Reiter, Delgrande, Asher–Morreau and Horty–Thomason–Touretzky, and match intuition better | weak to moderate | a handful of benchmark examples (§5); "better" is the author's judgement |
| C6 | Selection functions cannot model knowledge of rules, because they lose Independence | moderate | §5 examples |

## Method

Definitions of states, updates and orderings over a finite space of
worlds, with propositions stated (mostly without proof) and checked
against small worked examples drawn as diagrams of normality orderings.
The comparison with other default logics is by benchmark examples.

## Concepts

- **update system**: ⟨L, Σ, [ ]⟩, a language, a set of information
  states, and for each sentence an operation on states (postfix, σ[φ]).
- **acceptance** (σ ⊩ φ): σ[φ] = σ. **acceptable**: σ[φ] ≠ 1 (the absurd
  state).
- **additive**: σ[φ] = σ + 0[φ] on an information lattice; the case where
  dynamic meaning reduces to static content.
- **test**: an update that returns the input state or the absurd state, as
  *might* and *presumably* do.
- **expectation pattern**: a preorder on worlds, "w ≤ε v" meaning w
  conforms to every rule v conforms to.
- **frame**: a pattern for every domain d ⊆ W, so rules can be restricted.
- **coherent**: every nonempty domain has a normal world.
- **applies within s**: no domain extending s has all its normal worlds
  violating the default(s).
- **optimal world**: a world of s complying with a maximal applicable set
  of defaults. An **ambiguous** state has more than one.
- **valid₁**: updating the minimal state with the premises in order
  yields acceptance of the conclusion.

## Connections

The dynamic notion of meaning is credited (fn. 1) to Stalnaker's work on
presupposition and assertion, Kamp's and Heim's work on anaphora, and
Gärdenfors's dynamics of belief; the direct inspiration is Groenendijk and
Stokhof's dynamic predicate logic. Presupposition as definedness of an
update is noted and referred to Beaver and Zeevat. The default theory sits
beside Reiter's default logic, Delgrande's conditional logic, Asher and
Morreau's commonsense entailment (all built on Lewis's conditionals) and
the skeptical inheritance of Horty, Thomason and Touretzky. Generics are
left to Carlson and Krifka (1987).

## Bearing on the record

- The record held no account of dynamic semantics before the readings of
  2026-10-09. This paper, with Krifka's (LIT-tmpuclkg) and Heim's
  dissertation (LIT-tmpvhtrs), gives it one. Krifka's informative update
  is Veltman's propositional (additive) update; Krifka's performative
  update is a non-eliminative update of a kind Veltman's systems do not
  contain (every update here only shrinks s or refines the pattern).
- **CLAIM-tmphg89g** (proposition neither necessary nor sufficient). A
  weak, indirect bearing: *might φ* and *presumably φ* make a
  conversational contribution that has no propositional content at all,
  only a test, so what a sentence does in context is not fixed by a
  proposition it expresses. It does not speak to footing or force.
- A source, with the Heim and Krifka readings of the same day, of
  THEORY-tmp5ncrn: what an utterance does to a context is part of its
  meaning and is not fixed by its truth conditions. This paper supplies
  the tests and the additivity criterion.
- No instruction for ML practice; nothing for the anthology.

## Limitations

- Most propositions are stated without proof.
- Finite propositional language; the predicate reading of §5 treats
  "possible objects" as types, not as a first-order semantics.
- No revision: the theory says when an update is absurd, not how to
  recover.
- One time only (fn. 4), and modal operators only outermost.
- The author says the formalisation is not the only possible one and
  hopes for a more elegant one, and that it does not explain when a
  generic sentence gets a default reading (§6).
- The superiority over rival default theories rests on a few examples
  and on intuitions about them.

## Open questions

- Why ASC and Disjunction of Antecedents fail; the author says he has no
  intuitive explanation (§5).
- Whether a system can have normally p ⊩ normally (p ∨ q) together with
  the two intuitive inferences of fn. 7 without giving up Sequential Cut.
- How the default semantics relates to the semantics of bare plurals,
  definite and indefinite generics (§6).
