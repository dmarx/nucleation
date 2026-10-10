---
number: 700
status: Read
formerly:
- NOTE-tmpnwh69
paper: 'LIT-900'
title: 'Floridi — The Method of Levels of Abstraction'
version: 1
history:
- version: 1
  date: '2026-10-10'
  note: >-
    Read in full (the author's accepted preprint for Minds and Machines,
    from the University of Hertfordshire repository, uhra.herts.ac.uk/id/eprint/2205;
    40 pp. including a cover page and three pages of references. I read the
    abstract, §§1–5, the acknowledgements, all 11 footnotes and the
    reference list. Text extracted with `pdftotext -layout`; pp. 14–16
    rendered with `pdftoppm` to check the GoA definition, eq. (1) and
    Figure 1 against the extraction. Page numbers are the preprint's
    printed ones, where the cover page is p. 1. The Springer version of
    record, pp. 303–329, was not seen.) The first NOTE on this paper.
date: '2026-10-10'
summary: >-
  Floridi drops ontological levelism and defends an epistemological one,
  the method of levels of abstraction. Observables are interpreted typed
  variables; an LoA is a finite non-empty set of them; a moderated LoA adds
  a behaviour predicate; a GoA relates moderated LoAs by mutually inverse
  relations Rᵢ,ⱼ with pⱼ ⇒ P_Rᵢ,ⱼ(pᵢ), and is disjoint or nested. An LoA
  fixes which questions are answerable and commits a theory to types (the
  LoA) and tokens (the model). Applied to Kant's antinomies and contrasted
  with Marr, Pylyshyn, Dennett and Davidson. It is a method stated in
  definitions, not a result. Its one formal claim (disjoint and nested
  GoAs interconvert) fails under its own definition of nestedness, and its
  "pluralism without relativism" ranks LoAs only once a purpose is fixed.
---
<!-- inactive-ok-file: LIT-215 — Rejected on its 2026-09-26 close reading: cited for its misreading of LoAs, which this paper contradicts -->
<!-- inactive-ok-file: LIT-430 LIT-832 — Deferred, unread: named as works this paper cites, not leaned on -->
<!-- inactive-ok-file: QUESTION-009 — Deferred; set aside, and cited to say what this method would and would not supply for it -->
<!-- inactive-ok-file: CLAIM-010 CLAIM-110 — Rejected; cited as the history the comparison is about -->
<!-- inactive-ok-file: THEORY-034 — Proposed; open, and cited to say this reading does not bear on it -->

# NOTE-700: Floridi — The Method of Levels of Abstraction

## Contribution

Floridi separates four kinds of "levelism" (epistemological, ontological,
methodological, and the Oppenheim–Putnam amalgam). He concedes the
ontological kind to Heil and Schaffer, and rebuilds the epistemological
kind as a method with definitions borrowed from formal methods in computer
science (typed variables, Z-style predicates, simulation between levels).
What is new after it is a single citable statement of the method, with its
claimed consequences for ontological commitment, relativism and realism.
Before this, the method lived inside Floridi & Sanders 2004 ([LIT-898](../literature.d/LIT-898.md))
and their Yearbook chapter. The paper does not prove anything about the
formalism. It defines it, illustrates it, and positions it.

## Key insight

A question about a system has no answer until the observables are fixed,
and fixing them is a choice made for a purpose. Many philosophical
disputes, Kant's antinomies being the model case, come from asking about
"the system in itself" while silently shifting between LoAs. "Trying to
overstep the limits set by the LoA leads to a conceptual mess" (p. 23).
The LoA is an interface, "the place at which (diverse) independent systems
meet and act on or communicate with each other" (p. 30). It is not a
layer of the world: "Nature does not know about LoAs either" (p. 35).

## Assumptions

- Knowledge of systems is indirect, mediated by an LoA. Direct knowledge is
  taken to be only knowledge of one's own mental states (fn. 9, p. 18).
- Systems may be empirical or "purely semantic", that is, domains of
  discourse (p. 6). The method is meant to apply to both.
- Naive set theory, and well-typed variables. Type-free systems, and the
  antinomies a typed theory exists to exclude, are outside its scope
  (pp. 7, 36–37). "Its limitations are those of any typed theory" (p. 36).
- GoAs are finite sets of LoAs, and only discrete systems are handled; the
  infinite case is said to apply to analogue systems and is not considered
  (fn. 7, p. 14).
- The interpretation that makes a typed variable an observable is left
  informal, by design (p. 33).
- Ontological levelism is "probably untenable" (pp. 3–4). This is taken
  from Heil 2003 and Schaffer 2003, not argued here.

## Key results

The paper's results are definitions (§2) and arguments about them (§§3–4).

- **Typed variable (p. 5):** a uniquely named variable with a type, the set
  of its possible values, written x:X. An **observable** (p. 6) is an
  interpreted typed variable: a typed variable plus a statement of what
  feature of the system it represents. It is *discrete* if its type is
  finite, else *analogue*. Equality of observables requires equal typed
  variables, the same feature, and co-variation (Peter's height in feet and
  Ann's in metres are the same typed variable but different observables,
  p. 7).
- **LoA (p. 10):** "a finite but non-empty set of observables", unordered;
  discrete, analogue or hybrid. Examples: tasting, purchasing and cellaring
  LoAs for wine.
- **Behaviour and moderated LoA (p. 11):** a behaviour at an LoA is a
  predicate whose free variables are its observables; the satisfying
  assignments are the system behaviours; a moderated LoA is an LoA with a
  behaviour (height: 0 < h < 9).
- **Translation (p. 13):** a relation R ⊆ A × C translates a predicate p on
  A to P_R(p)(c) = ∃a:A R(a,c) ∧ p(a).
- **GoA (p. 14, "the main definition of the paper"):** a finite set
  {Lᵢ | 0 ≤ i < n} of moderated LoAs with relations Rᵢ,ⱼ ⊆ Lᵢ × Lⱼ
  (i ≠ j) such that (1) Rᵢ,ⱼ is the reverse of Rⱼ,ᵢ, and (2) the behaviour
  at Lⱼ is at least as strong as the translated behaviour,
  pⱼ ⇒ P_Rᵢ,ⱼ(pᵢ) (eq. 1); and, for each related pair of observables x:X
  and y:Y, a relation R_xy ⊂ X × Y between their types (added at
  Hughes's suggestion, fn. 8). The defining property is taken from
  simulation in computer science, "the conformity of behaviour between
  levels of abstraction" (p. 5). A one-element GoA is an LoA.
- **Disjoint and nested GoAs (p. 15):** *disjoint* if the LoAs share no
  observable and all relations are empty; *nested* if the only non-empty
  relations are between Lᵢ and Lᵢ₊₁ and the reverse of each Rᵢ,ᵢ₊₁ is a
  surjective function from the observables of Lᵢ₊₁ to those of Lᵢ. So every
  abstract observation has a concrete counterpart, and one abstract
  observable may be refined by many concrete ones (p. 16). Example: a
  traffic light's colour:{red, amber, green} refined to a wavelength wl
  with behaviour (λ_red ≤ wl ≤ λ_red′) ∨ … and colour = c ↔ λ_c ≤ wl ≤ λ_c′
  (p. 17).
- **Interconvertibility (p. 18):** disjoint and nested GoAs are said to be
  "interchangeable, at least theoretically", by passing between A, B and
  A ∪ B. See Limitations: the argument works for sets but not for the
  paper's definition of a nested GoA.
- **Four advantages (pp. 18–19):** an LoA specifies "indirect knowledge";
  it fixes the questions that "(a) can be meaningfully asked and (b) are
  answerable in principle"; it guards against level-shifting fallacies
  (metabasis, category mistakes, antinomies); and it makes ontological
  commitment explicit.
- **SLMS scheme and commitment (pp. 19–21):** system, analysed at an LoA,
  generates a model, which identifies a structure. The LoA is
  "O-committing" (types: a three-colour LoA commits one to a Roman, not an
  Oxford, traffic light) and the model "O-committed" (tokens).
- **Kant's antinomies (§3):** antinomies 1–2 (finitude, divisibility)
  mistake features of the interface for features of the system, so neither
  thesis nor antithesis holds. Antinomies 3–4 (freedom, necessary being)
  "come close to" a disjoint GoA, so both may hold (pp. 22–23). The method
  is "Kantian" and "transcendental" without Kant's mentalism, and
  "anti-metaphysical": "metaphysics is that LoA-free zone where anyone can
  say anything without fear of ever being proved wrong" (p. 24). Its
  realism is "liminal realism", between internal and external realism
  (p. 22).
- **Levels of organisation and explanation (§4.1):** LoOs are ontological
  (a hierarchy in the system de re); LoEs are pragmatic and epistemic; LoAs
  "provide a foundation for both" (p. 26). Marr, Pylyshyn and Dennett each
  give "GoAs with three LoAs", do not distinguish LoO, LoE and LoA, and,
  because they privilege explanation, their "ontological commitment is
  embedded and hence concealed" (pp. 27–28).
- **Conceptual schemes (§4.2):** LoAs differ from Davidson's schemes in
  being networks of observables usable by non-human "agents" (p. 29), and
  in standing to their systems by *design*, not discovery or invention
  (p. 29). Agents can change and expand their LoAs, but two LoAs can still
  be untranslatable, so agents "may inhabit only some types of information
  spaces in principle" (p. 31; Nagel's bat). Davidson's argument assumes a
  linguistic, representationalist view that LoAs do not share, so
  "Incommensurable and untranslatable LoAs are perfectly possible"
  (p. 31). Histories of science are comparable at some LoA: "do not ask
  absolute questions, for they just create an absolute mess" (p. 32).
- **Pluralism without relativism (§4.3, one paragraph):** LoAs are
  "mutually comparable and assessable, in terms of inter-LoA coherence, of
  their capacity to take full advantage of the same data and of their
  degree of fulfilment of the explanatory and predictive requirements laid
  down by the level of explanation" (pp. 32–33).
- **Realism without descriptivism (§4.4):** no circularity in defining
  "realistic" observables, by analogy with Tarski's truth definition; a
  regress arises only if a complete characterisation is sought (pp. 33–34).
  A GoA is judged by validation (external adequacy) and verification
  (internal coherence), like "a multidimensional crossword puzzle". GoAs
  "do not describe, portray, or uncover the intrinsic nature of the
  systems they analyse … Adequacy and coherence are the most we can hope
  for" (p. 34).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Ontological levelism is probably untenable | weak | deferred to Heil 2003 and Schaffer 2003 (pp. 3–4); not argued here |
| C2 | Epistemological levelism, as the method of LoAs, is a fundamental and, for discrete systems, indispensable method of conceptual analysis | weak | the four advantages (§2.7) and the analogy that the method does "for discrete systems what differential calculus has traditionally done for analogue systems" (p. 12). "Indispensable" is asserted (p. 36) |
| C3 | Fixing an LoA fixes which questions about a system are meaningful and answerable, and the amount of information a model can contain | moderate for the first half, weak for the second | the first follows from the definitions. "A quantified commitment to the kind and amount of information" (p. 19) has no measure behind it: information is not quantified anywhere in the paper |
| C4 | Adopting an LoA commits a theory to types and endorsing its model commits it to tokens | moderate | the SLMS scheme and the traffic-light example (pp. 19–21); a clean distinction, though stated rather than defended |
| C5 | Kant's first two antinomies come from treating features of an LoA as features of the system; the last two resemble a disjoint GoA | weak | an illustration by analogy, "assuming for the sake of simplicity that a LoA is comparable to an interface" (p. 23); no antinomy is formalised as a GoA |
| C6 | Marr's, Pylyshyn's and Dennett's three-level schemes conflate LoO, LoE and LoA and so conceal their ontological commitment | moderate | the diagnosis is argued from their own statements (pp. 26–28). The claim that each is "readily formalised" as a three-LoA GoA is asserted, not carried out |
| C7 | Davidson's argument against conceptual schemes does not touch LoAs, and untranslatable LoAs are possible | weak | argued by contrasting four features (pp. 28–31). The one example of untranslatability, tasting versus purchasing wine, shows two LoAs that do not overlap, not two that cannot be translated |
| C8 | Making the LoA explicit gives pluralism without relativism | weak | one paragraph listing ranking criteria (pp. 32–33). Each criterion is relative to "the level of explanation", so LoAs are ranked given a purpose, not across purposes |
| C9 | Defining realistic observables involves no vicious circularity or regress, and the method supports realism without naive realism | moderate | the analogy with Tarski's truth definition and the validation/verification account (pp. 33–34) |
| C10 | The method has settled problems elsewhere (the Gettier problem is unsolvable, zombies, structural realism, telepresence, the value of informational objects) | assertion | referred to other papers (p. 35) |

## Concepts

- **observable**: an interpreted typed variable, which need not come from
  measurement or perception (p. 6).
- **level of abstraction (LoA)**: a finite non-empty set of observables;
  the interface at which a system is accessed (pp. 10, 30).
- **behaviour / moderated LoA**: a predicate over an LoA's observables, and
  an LoA paired with one (p. 11).
- **gradient of abstractions (GoA)**: moderated LoAs related so that each
  level's behaviour is consistent with its neighbours' (p. 14); *disjoint*
  views are complementary, *nested* views successively more informative
  (p. 15).
- **method of abstraction**: making the commitment to an LoA or GoA
  explicit before elaborating a theory (p. 18).
- **SLMS scheme**: system, LoA, model, structure; the LoA is O-committing
  and the model O-committed (pp. 19–21).
- **level of organisation (LoO)** and **level of explanation (LoE)**:
  ontological and pragmatic levelisms respectively; an LoE is "an important
  kind of LoA" (p. 25).
- **liminal realism**: between internal realism and external or
  metaphysical realism (p. 22).
- **information space**: what an LoA generates and commits an agent to
  (p. 30).
- **agent**: used broadly and undefined in this paper. Agents are anything
  that "operate[s] and deal[s] with the world … at some LoAs", including
  computers, animals, plants, scientific theories and measuring
  instruments (p. 29). A thermometer is an agent with "hardwired" LoAs
  (p. 30).

## Connections

Floridi says the method was "forced" on him and Sanders by "the problem of
defining the nature of agents (natural, human and artificial)" in Floridi &
Sanders 2004 ([LIT-898](../literature.d/LIT-898.md), read in [NOTE-701](NOTE-701.md)) (p. 35). He calls Sanders
someone who "should really be considered a co-author of this paper"
(p. 37). Their joint "The Method of Abstraction" (Yearbook of the
Artificial, 2004) is the earlier statement, and is not held. This paper
generalises the method from defining agents to conceptual analysis at
large, and refines the GoA definition by relating types as well as
observables (fn. 8). The `extends` on the LIT records this. Floridi 2025
([LIT-897](../literature.d/LIT-897.md), read later in [NOTE-702](NOTE-702.md)) compares kinds of agency by this method.

**Informational structural realism.** Floridi's defence of ISR ([LIT-152](../literature.d/LIT-152.md),
read in [NOTE-099](NOTE-099.md)) restates these definitions in its §2.2. This paper lists
that work as an application, "to propose and defend an informational
approach to structural realism that reconciles forms of ontological and
epistemological structural realism" (p. 35, citing it as Floridi 2004b, the
2004 draft). [NOTE-099](NOTE-099.md)'s judgement that "the LoA formalism is rigorous in
isolation, but no result about it is used in the argument" holds here at
the source too. No result about GoAs is used here either, and the
definitions carry slips (see Limitations). [NOTE-099](NOTE-099.md)'s gloss of an LoA as "a
model-theoretic interface, not a metaphysical 'level of being'" is this
paper's own position (pp. 30, 35). That confirms [NOTE-096](NOTE-096.md)'s correction of
Karpenko ([LIT-215](../literature.d/LIT-215.md)), who reads information as what has "the highest level
of abstraction": here LoAs are interfaces, and ontological levels are
given up outright.

**Personal identity.** Floridi's informational account of the self
([LIT-136](../literature.d/LIT-136.md), read in [NOTE-130](NOTE-130.md)) deflates diachronic identity to purpose-relative
LoAs. It assumes the method from "Floridi 2008c"; I have not checked that
[LIT-136](../literature.d/LIT-136.md)'s reference list resolves that to this paper. [NOTE-130](NOTE-130.md) grades its
"this is not relativism: given a particular goal, one LoA is better than
another" as a one-sentence assertion, and asks how goals are adjudicated.
This paper's §4.3 is where that sentence comes from, and it does not answer
the question either. Its ranking criteria are all relative to "the level of
explanation", which is a purpose already fixed. [NOTE-374](NOTE-374.md) notes that the
encyclopedia entry on personal identity ([LIT-454](../literature.d/LIT-454.md)) rejects the view that
persistence is answerable by conceptual means, of which Floridi's deflation
is a version. That objection reaches the method, not only its use there.

**Watson.** [NOTE-172](NOTE-172.md) reads Watson ([LIT-187](../literature.d/LIT-187.md)) as building on "Floridi's
method of levels of abstraction (2008)". That is very probably this paper;
I have not checked it against Watson's references.

**Dennett.** The paper compares GoAs to Dennett's stances (p. 13) and
formalises the intentional, design and physical stances as a three-LoA GoA
(p. 27), citing "Intentional Systems" ([LIT-440](../literature.d/LIT-440.md)) and *The Intentional
Stance* ([LIT-430](../literature.d/LIT-430.md), unread). [LIT-440](../literature.d/LIT-440.md)'s reading ([NOTE-350](NOTE-350.md)) makes being an
intentional system relative to an observer's predictive strategy. The
method of abstraction generalises that relativity to any property, and
objects only that Dennett privileges explanation and so hides his
ontology (p. 28). Dennett's "True Believers" ([LIT-398](../literature.d/LIT-398.md)) later withdraws that
relativity, by [LIT-440](../literature.d/LIT-440.md)'s record; this paper does not engage the later
view.

**Other cited work the record holds.** Nagel's bat ([LIT-096](../literature.d/LIT-096.md)) is used for
information spaces too far apart to translate (p. 31). Craver's
"forthcoming" *Explaining the Brain* (fn. 3; [LIT-832](../literature.d/LIT-832.md), unread) is cited for
ontological levelism in biology.

## Bearing on the record

It carries nothing for machine-learning practice. It is held here as the
source of a method the record's Floridi readings ([LIT-152](../literature.d/LIT-152.md), [LIT-136](../literature.d/LIT-136.md),
[LIT-898](../literature.d/LIT-898.md), [LIT-896](../literature.d/LIT-896.md), [LIT-897](../literature.d/LIT-897.md)) assume. I file no THEORY. The
paper's results are definitions and a stance, not a claim about the world
with evidence, and [NOTE-099](NOTE-099.md) filed none for the ISR paper that uses the same
machinery. [THEORY-034](../theory.d/THEORY-034.md), which places [LIT-152](../literature.d/LIT-152.md), is not affected: this paper
adds nothing on intrinsic natures beyond §4.4's statement that GoAs "do not
… uncover the intrinsic nature of the systems they analyse" (p. 34), which
agrees with [NOTE-099](NOTE-099.md)'s reading.

**The agency line (my pairings; the paper cites none of these).**

- *[QUESTION-009](../questions.d/QUESTION-009.md)* (when does a pattern of coordination constitute an
  additional agent?). The method gives the form of an answer, not an
  answer: something is an agent *at an LoA* if its observables there
  satisfy some criteria. The criteria are Floridi & Sanders's
  ([LIT-898](../literature.d/LIT-898.md)), not this paper's. What this paper adds is the condition
  under which "additional agent" questions are well posed, namely an
  explicit LoA. It also adds the warning that an LoA-free version of the
  question is the "metaphysics" it dismisses (p. 24). It does nothing about
  the permissiveness objection ([CLAIM-010](../claims.d/CLAIM-010.md), a thermostat has a will). The
  paper's own usage is more permissive still: a thermometer and a
  scientific theory are "agents" that operate at LoAs (pp. 29–30).
- *Two roles for an LoA.* §4.2 uses "the agent's LoA", what an agent can
  itself observe (a thermometer's hardwired LoA). Floridi & Sanders, and
  the later agency papers, use "the LoA at which a system is analysed", the
  theorist's interface. The paper does not separate the two. A claim that
  something is an agent "at a given LoA" needs to say which is meant, and a
  reading of [LIT-897](../literature.d/LIT-897.md) should check.
- *[CLAIM-045](../claims.d/CLAIM-045.md) and [CLAIM-110](../claims.d/CLAIM-110.md).* The record's correction at A10, that
  differences in explanatory emphasis between Brooks, Kelso and Levin do
  not imply competing ontologies, is this paper's distinction between
  levels of explanation and levels of organisation (§4.1). "By structuring
  the explanandum, LoAs can reconcile the explanans" (p. 32). [CLAIM-045](../claims.d/CLAIM-045.md)'s
  "complementary components … each answering a different sub-question" is,
  in this vocabulary, a GoA whose LoAs are disjoint or partly overlapping,
  with the sub-questions as levels of explanation. The vocabulary
  could state [CLAIM-045](../claims.d/CLAIM-045.md) more exactly, but it does not argue for it.

Nothing in the record cites this paper for something it does not say.
[NOTE-172](NOTE-172.md)'s line distinguishing it from [LIT-152](../literature.d/LIT-152.md) is accurate. Now that the
paper is held, that line could name [LIT-900](../literature.d/LIT-900.md).

## Limitations

- **The interconvertibility argument fails under the paper's own
  definitions (p. 18).** Disjoint to nested: the inclusion of A in A ∪ B,
  reversed, is not total on A ∪ B, so it is not the surjective *function*
  nestedness requires (p. 15). Nested to disjoint: "if A and B are
  increasing sets with the former embedded in the latter, then A and the
  set difference A \ B are disjoint sets". With A ⊆ B, A \ B is empty; the
  intended set is B \ A. The claim survives for sets of observables, not
  for GoAs as defined. The hedge "at least theoretically" does not cover
  this.
- **Index and orientation slips in §2.6.** "If one LoA Lᵢ extends another
  Lⱼ by adding new observables, then the relation Rᵢ,ⱼ is the inclusion of
  the observables of Lᵢ in those of Lⱼ" (p. 14) is consistent with the rest
  of the sentence only if Lⱼ extends Lᵢ. The nested definition says the
  only non-empty relations are the Rᵢ,ᵢ₊₁, but condition 1 makes each
  Rᵢ₊₁,ᵢ non-empty too. Figure 1 draws L₀ as the widest band, while the
  traffic-light example makes L₀ the coarser LoA, and the figure does not
  say what width means. Two different figures are both numbered "1"
  (pp. 16, 20). None of this damages the method. All of it is in the
  preprint, and I have not seen whether print corrects it.
- **"Quantified commitment" without a quantity.** The paper says an LoA
  gives "a quantified commitment to the kind and amount of information"
  extractable (p. 19), and that a lower LoA's model "contains more
  information" (pp. 18–19). No measure is defined. It is resolution in the
  sense of a finer type, not Shannon information.
- **Relativism is answered within a purpose, not across purposes.** The
  §4.3 criteria rank LoAs relative to "the explanatory and predictive
  requirements laid down by the level of explanation". So two parties with
  different purposes can each be right at their own LoA, which is the
  pluralism claimed. But nothing here says when a purpose is the wrong one.
  Every use of the method that deflates a question (identity in [LIT-136](../literature.d/LIT-136.md),
  the antinomies here) inherits this gap.
- **The tripartite formalisations are promised, not done.** Marr's,
  Pylyshyn's and Dennett's schemes are "readily formalised in terms of
  GoAs" (p. 27), but no relations or behaviours are written down. The
  claim that the formalism adds rigour to them is untested here.
- **Scope, by the author's own account (p. 36).** The method is that of a
  typed theory. Floridi does not know whether every complex system can be
  approximated at finer LoAs, and allows that "the mind or society" may
  not be susceptible. He does not commit to exporting the method to
  ontological or methodological contexts.
- **The interpretation of observables is informal** (p. 33). The method's
  claim to make ontological commitment explicit rests on a step it leaves
  unformalised.

## Open questions

- Is there a principled way to rank purposes, or levels of explanation,
  that would make §4.3's "pluralism without relativism" hold across
  purposes and not only within one? Without it, the deflationary uses
  (identity, agency) stay purpose-relative all the way down.
- Does the GoA consistency condition (eq. 1) do any work in the papers that
  cite the method? [NOTE-099](NOTE-099.md) found none in the ISR paper. A reading of the
  agency papers should check whether any argument there uses a relation
  between LoAs, or only the choice of one.
- Which LoA does an agency claim name: the system's own (what it can
  observe) or the analyst's (what it is observed by)? The two come apart
  for a thermostat or an LLM, and this paper uses both without marking the
  difference.
- Does the Springer version of record correct the §2.6 slips?
