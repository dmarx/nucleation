---
status: Read
paper: LIT-tmpx7zhl
title: 'Dynamic Semantics'
version: 1
history:
- version: 1
  date: '2026-10-08'
  note: >-
    Read in full from the Stanford Encyclopedia of Philosophy entry as
    served on plato.stanford.edu ("First published Mon Aug 23, 2010;
    substantive revision Tue Jul 12, 2016"), about 12,000 words: the
    preamble, §§1–5 and every subsection, end to end. The bibliography was
    read as a list. None of the cited works was opened.
date: '2026-10-08'
summary: >-
  The entry presents dynamic semantics as the view that a sentence's
  meaning is an update on a context. Its central instance, dynamic
  predicate logic, makes ∃x a random reset whose effect extends past its
  scope. That gives cross-sentential and donkey anaphora a compositional
  analysis without adding expressive power over first-order logic. The
  same idea is extended to plural and modal subordination, presupposition
  projection, vagueness, epistemic update and non-at-issue content.
  Whether it explains presupposition, rather than describing it, is left
  contested.
---
<!-- inactive-ok-file: LIT-208 — Proposed: the record's other account of linguistic meaning, compared in Connections, not relied on -->

# NOTE-tmpefif9: Dynamic Semantics

## Contribution

A survey, not a new result. It separates two senses of "dynamic
semantics". The first is a framework: meanings are actions on contexts. It
is abstract and makes no empirical claim alone. The second is a set of
positions within it. For anaphora, these are that pronouns are variables
and that indefinites are not quantifiers but updates to an assignment
(§2.1). The entry then shows the framework at work, mostly through
dynamic predicate logic (DPL).

## Key insight

Compositionality is what forces the move. "Mary met a student yesterday.
He needed help." means what "Yesterday, Mary met a student who needed
help" means. But interpreting the sentences one at a time in classical
logic leaves the pronoun's variable free (§2.1). If the existential is
instead an action that resets x and leaves it reset, the scope problem
disappears, and ∃x(ψ) ∧ φ and ∃x(ψ ∧ φ) come out equivalent. The meaning
of a sentence becomes what it does to the context. Its truth conditions
are recovered as the precondition of that action, so nothing is lost.

## Assumptions

- **Compositionality is a requirement.** Interpreting a discourse only as
  a whole is rejected as "counter-intuitive" (§2.1).
- **Contexts can be modelled in several ways**: sets of worlds
  (Stalnaker's common ground, Heim's presupposition rules), sets of
  assignments (DPL), sets of sets of assignments (plural information
  states), or multi-agent Kripke models (dynamic epistemic logic). The
  framework does not choose among them (§1).
- **DPL's setting**: total assignments from a fixed set of variables to a
  fixed non-empty domain. Meanings are binary relations on assignments
  (§2.2).
- **The pronoun-as-variable route is a choice.** The E-type alternative,
  in which pronouns are disguised definite descriptions (Evans, Heim 1990,
  Elbourne), is acknowledged and not pursued (§2.1).

## Key results

- **DPL clauses (§2.2).** Atoms are tests: α[P(x̄)]β iff α = β and
  ⟨α(x̄)⟩ ∈ I(P). The reset: α[∃v]β iff α and β differ at most at v.
  Conjunction is relational composition. Negation: α[∼φ]β iff α = β and φ
  has no output from α. Truth: α ⊨ φ iff φ has some output from α.
- **Defined operators.** φ → ψ := ∼(φ · ∼ψ), true at α iff every output
  of φ from α satisfies ψ. ∀x(φ) := (∃x → φ). Dynamic entailment, after
  Kamp 1981: φ ⊨ ψ iff every output of φ supports ψ.
- **First-order logic embeds in DPL** compositionally, with
  (∃x φ)* := ¬¬(∃x · φ*). The image of every first-order formula is a
  test.
- **No added expressive power.** Every DPL formula translates into a
  first-order formula giving its domain. The translation is a weakest
  precondition calculus in the style of Floyd–Hoare (van Eijck and de
  Vries 1992). In a weak sense, "nothing new happens in DPL" (§2.2).
- **Donkey sentences (§2.3).** "If a farmer owns a donkey, he beats it"
  translates to ∃x · Fx · ∃y · Dy · Oxy → Bxy. Its first-order
  precondition is ¬∃x(Fx ∧ ∃y(Dy ∧ Oxy ∧ ¬Bxy)), the universal reading.
  So the problem was never expressibility but compositional derivation.
- **Dynamic generalized quantifiers (§2.4).** Universal quantifiers block
  singular anaphora ("#He wrote ...") but allow plural anaphora to the
  set and to the dependency ("Each of them submitted it"), after van den
  Berg 1996. Both follow if contexts are sets of assignments and
  quantifiers quantify over assignments. Modal subordination ("A wolf
  might come in. It may eat you.") gets the same treatment, with worlds
  in place of individuals.
- **Presupposition (§3.1).** Karttunen and Heim make local contexts part
  of the connectives' meaning: C[S1 and S2] = (C[S1])[S2], and
  C[S1 or S2] = C[S1] ∪ (C[not S1])[S2]. This explains why "John is late
  and Mary knows he is late" presupposes nothing.
- **Dynamic epistemic logic (§3.2).** A public announcement of φ restricts
  a pointed multi-agent model to the φ-worlds. A presupposition P can be
  modelled as announcing that P is common knowledge: vacuous when it is,
  inconsistent when it is not.
- **Typed logic (§4).** Dynamic Montague grammar and most higher-order
  systems inherit DPL's destructive reassignment, which DRT avoids by
  taking fresh discourse referents. Muskens's compositional DRT is
  called the de facto standard. Stack semantics (Vermeulen) and van
  Eijck's incremental typed logic, where contexts are finite lists
  extended at the end, avoid destructive reassignment.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Dynamic semantics generalizes truth-conditional semantics rather than replacing it | strong as a formal point | §2.2: the precondition of a DPL meaning is its classical truth condition, and FOL embeds as tests |
| C2 | DPL gives cross-sentential and donkey anaphora a compositional analysis that classical predicate logic does not | strong for the formal fragment | §2.1–2.3, the clauses and worked translation |
| C3 | DPL adds no expressive power over first-order logic | strong | §2.2, the precondition translation (van Eijck and de Vries 1992) |
| C4 | Plural, quantificational and modal subordination call for contexts that are sets of assignments | moderate: argued from examples, implementations cited | §2.4 (van den Berg; Nouwen; Brasoveanu) |
| C5 | Dynamic connectives explain presupposition projection | contested: Soames's objection that unattested connectives are not ruled out is reported, Rothschild's definedness constraints are offered as the answer, and static rivals are named | §3.1 |
| C6 | Muskens's compositional DRT is the de facto standard for compositional dynamic semantics | assertion | §4 |
| C7 | The cross-linguistic range of dynamic analyses is growing fast | assertion, unsupported in the entry | §5 |

## Concepts

- **context change potential**: a sentence's meaning taken as a function
  or relation from input contexts to output contexts.
- **test**: an update that passes an input through unchanged if it meets a
  condition and drops it otherwise. Predications in DPL are tests.
- **random reset**: DPL's ∃x, written [x := ?] in programming terms. It
  changes at most the value of x.
- **local context**: the context against which a sub-clause is
  interpreted, as distinct from the global context of the whole sentence
  (Karttunen).
- **destructive assignment**: resetting a variable loses its old value. It
  is a property of DPL and its typed descendants, and not of DRT or stack
  semantics.
- **at-issue against non-at-issue content**: what an utterance proposes
  for the common ground, against what it imposes directly, such as an
  appositive (AnderBois, Brasoveanu and Henderson 2015).

## Connections

Distributional semantics, read holistically in [LIT-208](../literature.d/LIT-208.md), is the only
other account of linguistic meaning in the record. The two answer
different questions. [LIT-208](../literature.d/LIT-208.md) is about what fixes a word's meaning and
how stable it is. This entry is about how sentence meanings combine
across a discourse. Neither tests the other.

## Bearing on the record

No THEORY in the record concerns formal semantics, so this reading
supports or contradicts none. The entry is a map, well suited to source
one if the record comes to need an account of meaning in context. There
is no instruction for machine-learning practice. Anaphora resolution and
discourse modelling have counterparts in language-model work, but the
entry does not mention them, so nothing here belongs in the anthology.

## Limitations

- It is an encyclopedia entry by proponents. Its alternatives get a
  paragraph each: E-type anaphora in §2.1, static presupposition accounts
  in §3.1.
- The worked formal material is almost all DPL. DRT and file change
  semantics are introduced but not defined.
- §1's opening frames the framework as "abstract", and the entry never
  states which empirical claims, if any, separate the dynamic framework
  from a static theory with the same coverage.
- The last substantive revision is from 2016, so later work on static and
  dynamic anaphora is not covered.

## Open questions

- Is dynamic semantics an empirical thesis or a notation? The entry's own
  result that DPL defines nothing first-order logic cannot sharpens the
  question. The answer has to come from compositionality, or from the
  plural and presupposition data, not from expressive power.
- Can definedness constraints of Rothschild's kind make the dynamic
  account of presupposition explanatory, or do the static accounts cover
  the same data with fewer stipulations? A comparison on a shared data
  set would decide it.
