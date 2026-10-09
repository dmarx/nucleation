---
status: Read
paper: 'LIT-tmpuclkg'
title: 'Performative updates'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full from the Springer open-access PDF (Synthese 203:31, CC BY
    4.0, 31 pages), extracted with pdftotext. Sections 1–10, all numbered
    definitions (1)–(44) and the footnotes read. The figures (8)–(11),
    (13), (15), (16) and (40) are diagrams that did not survive
    extraction; they were read from their captions and the prose that
    describes them. The reference list was read for the works cited;
    none of the cited works was read for this note.
date: '2026-10-09'
summary: >-
  Makes the performative/constative distinction a difference between two
  operations on a context set: informative update eliminates indices,
  performative update changes them minimally so that a proposition holds.
  Declarations are purely performative; an assertion is a performative
  truth guarantee by the speaker plus a negotiable informative update; the
  same declarative sentence can be either. Argued from linguistic evidence,
  not tested.
---
<!-- inactive-ok-file: LIT-785 LIT-tmpnhioh LIT-tmpeftz9 — Deferred; unread here, named as the works this paper builds on and not leaned on -->
<!-- inactive-ok-file: THEORY-tmp5ncrn — Proposed; filed from this reading with two others -->
<!-- inactive-ok-file: CLAIM-tmpfbpte CLAIM-tmphg89g CLAIM-tmp471wm — Proposed; open, and cited as open: the claim is under test, not settled -->

# NOTE-tmp0w9bg: Performative updates

## Contribution

Dynamic semantics since Stalnaker had modelled what an utterance does to
the common ground only as adding information: removing the indices of a
context set at which the proposition is false. This paper adds a second
operation, taken from Szabolcsi (1982) and reworked: performative update,
which changes each index so that the proposition becomes true. With the two
it models declarations, assertions, other speech-act types, the locutionary
act and the adverb *hereby* in one framework. What is new is the
integration: Szabolcsi's index change placed in branching time and lifted
to context sets, a syntactic layer (ActP, ComP) that composes it, and an
analysis of assertion as a performative commitment followed by an
informative update.

## Key insight

Saying something can change what the world is like as well as what the
participants take it to be. "The meeting is adjourned" said as a report
narrows the possibilities; said by the chair it moves every possibility to
one where the meeting is adjourned. An assertion has both parts: the
speaker first makes it true that they vouch for φ (which the hearer cannot
undo), and only then proposes that φ be accepted (which the hearer can
refuse). The proposition is the same in a declaration and an assertion;
the update differs.

## Assumptions

- **Common ground as a Stalnakerian context set**: a set c of world–time
  indices. Discourse referents, attention, questions under discussion and
  individual attitudes are set aside on purpose.
- **Branching time**: a transitive order < on indices with backward
  linearity (fixed past, open future), and a map τ of indices onto
  linearly ordered times, so that a changed index i′ and the original i are
  cotemporaneous (τ(i) = τ(i′)) and start different histories.
- **Minimal difference** (6c, 12c): i′ differs from i in no "relevant"
  proposition other than φ, its consequences established in the current
  histories, and independent changes happening at the same moment. The
  paper does not define "relevant"; it works through cases.
- **Felicity as definedness**: authority and other preconditions are
  presuppositions that restrict where the update is defined (22). Their
  content is not modelled.
- **The commitment operator ⊢** (26) is taken as a primitive social
  relation, "x guarantees in i that φ is true", following the Peircean
  commitment theory of assertion. What a guarantee is is not analysed.

## Key results

The results are definitions and analyses, not theorems.

- **(1) Informative update**: c + inform(φ) = {i ∈ c | φ(i)}. Always ⊆ c;
  empty when φ holds nowhere in c.
- **(3)/(14) Performative update**: functional, {i + φ | i ∈ c}; relational,
  ⋃{i + φ | i ∈ c}. Not ⊆ c unless φ already holds throughout c; defined
  when φ is false throughout c, where informative update would give ∅ (16).
- **(6) and (12) Index change**: functional (unique i′) requires
  indeterminate indices once φ is a disjunction; relational (a set of
  minimal i′) keeps classical indices. The paper adopts the relational
  version.
- **(20)–(22) Declarations**: ⟦·⟧ = λpλc{i′ | ∃i ∈ c, i′ ∈ i + p}, with p
  replaced by a partial proposition defined only where the speaker is
  authorised. Explicit performatives (*I congratulate you*) are
  declarations of a proposition naming the act, with no lexical ambiguity
  between descriptive and performative verbs (against Szabolcsi).
- **(28)–(33) Assertions**: ⟦· [ComP ⊢ TP]⟧ performatively makes it true
  that s ⊢ φ; the informative update with φ follows as the primary
  perlocution. Composing them unconditionally (33) is rejected because the
  addressee can refuse φ; negotiation is delegated to Krifka's commitment
  spaces (2015, 2022), not developed here.
- **§5 Tense**: the illocutionary change is instantaneous (an achievement),
  so English uses the simple present and not the progressive. Perfect,
  perfective and future performatives in other languages fit if the
  proposition can include the evaluation index.
- **§7 Other acts**: commissives (*I will help you* as declaration vs
  assertion, 34), imperatives as obligations or as proposed future facts
  (35–36), exclamatives and optatives as displays, definitions, and
  "proxitives".
- **(41)–(42) Locution**: the utterance is a performative update with a
  SAY event over an interval; the illocutionary update applies at its
  final index, ⟪α⟫ ; ⟦α⟧.
- **§9 hereby**: marks that the host proposition becomes true as a result
  of the locutionary act; since an asserted proposition is true
  independently of the utterance, *hereby* does not occur with assertions,
  and it can occur in embedded clauses (44).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Performative and informative updates are distinct operations on a context set; the first can add indices, the second only removes them | strong (by definition) | (1), (3), (14), (15)–(16) |
| C2 | Index change is a coherent notion, functionally with partial indices or relationally with classical ones | moderate | §3, worked through cases; "relevant proposition" is not defined |
| C3 | Declarations and assertions with the same declarative sentence are distinct structures, the assertion carrying a commitment layer the declaration lacks | moderate | hedges, *certainly*, question–answer pairs (§6), Krifka 2023 |
| C4 | An assertion's illocution is the speaker's public guarantee, and the addition of φ to the common ground is a perlocution the addressee can refuse | moderate | argued from commitment theory and Moore-type examples; formal negotiation not given here |
| C5 | All speech acts, including the locutionary act, bring about a performative change | weak | §7–8 sketches, one example each |
| C6 | *hereby* marks a proposition made true by the locutionary act, which explains its absence from assertions and its presence in embedded clauses | moderate | §9, with counterexample discussion (fn. 22) |

## Method

Model-theoretic: define operations on sets of world–time indices,
compose them through a syntactic layer of speech-act heads (ActP for the
performative operator, ComP for the commitment operator), and test the
analysis against linguistic data, chiefly from English and German, with
typological evidence on performative tense (Fortuin 2019 and others) and
the author's fieldwork on Daakie.

## Concepts

- **context set**: the set of indices compatible with what the
  participants take to be shared (Stalnaker 1978).
- **informative update**: elimination of indices where φ is false.
- **performative update**: replacement of each index by its minimal
  φ-changed variant(s).
- **index change** (i + φ): the minimally different, cotemporaneous index
  (or set of indices) at which φ holds; a branching from i, not a later
  point on i's history.
- **declaration**: a speech act that is purely a performative update,
  needing authority.
- **assertion**: a performative update with the speaker's truth guarantee,
  plus a proposed informative update.
- **ActP / ComP**: the syntactic projections hosting the performative
  operator (·) and the commitment operator (⊢).
- **proxitive**: the author's term for signs that stand in for an act
  (*grins*, emoticons, lol).

## Connections

The informative half is Stalnaker's "Assertion" (1978), and the dynamic
tradition named alongside it is Hamblin, Kamp, Heim (1983), Rooth and
Groenendijk and Stokhof. The performative half is Szabolcsi's 1982
extension of Montague grammar. The speech-act categories are Austin's and
Searle's; the operator · is described as an instance of Searle's (1969)
F(p), with the difference that it yields a context change rather than a
truth-valued formula. The commitment theory of assertion is credited to
Peirce and to Brandom (1983), not to *Making It Explicit* ([LIT-tmp3t040](../literature.d/LIT-tmp3t040.md)). Portner's to-do
lists and Farkas and Bruce's table are named as rival or complementary
ways to model non-informative acts.

## Bearing on the record

- **Prior art for the manuscript `what-survives-translation`.** The paper
  is what the exchange said it is: an explicit model of speech acts with
  informative and performative updates. It says nothing about translation,
  equivalence between utterances, or comparing renderings.
- **[CLAIM-tmphg89g](../claims.d/CLAIM-tmphg89g.md) (proposition neither necessary nor sufficient).** The
  structural ambiguity of (19) and (28) is a formal case of the
  "not sufficient" half: one TP, one proposition, two different updates
  (a declaration and an assertion), distinguishable by hedges and by what
  responses are apt. It does not address the "not necessary" half.
- **[CLAIM-tmpfbpte](../claims.d/CLAIM-tmpfbpte.md) (interpretive and performative fidelity come apart).**
  Krifka separates, within one assertion, the performative update (the
  speaker's guarantee, not rejectable by the hearer) from the informative
  update (rejectable). That is a model in which the act and its content
  can succeed or fail separately, which is the shape the claim needs. But
  his "performative" is the speaker's commitment or a world change, not
  the speaker–audience relationship (complicity, solidarity) the claim's
  case is about; extending it there is the manuscript's step, not his.
- **[CLAIM-tmp471wm](../claims.d/CLAIM-tmp471wm.md) (Krifka–Blackwell pairing).** The paper gives a precise
  object for "which changes in conversational standing count": the set of
  propositions an update makes true (guarantees, obligations, declared
  facts). It gives no observables, response distributions or measurement
  procedure, so the claim's `defeated_if` is untouched by it. Note that
  the negotiation machinery the exchange may have had in mind
  (commitment spaces) is in Krifka 2015 and 2022b, not here.
- **[CLAIM-tmp7cc3w](../claims.d/CLAIM-tmp7cc3w.md) (disclaimed novelty).** Confirms the disclaimer is
  needed: "speech acts change contexts" is this paper's thesis, stated
  formally. The integration with translation and an information order is
  not anticipated in it.
- A source, with the Heim and Veltman readings of the same day, of
  [THEORY-tmp5ncrn](../theory.d/THEORY-tmp5ncrn.md): what an utterance does to a context is part of its
  meaning and is not fixed by its truth conditions. This paper's
  contribution is the declaration/assertion pair. No instruction for ML
  practice; nothing for the anthology.

## Limitations

- "Relevant proposition" in the minimal-change condition is left
  informal, and with it what an index change changes.
- The commitment operator is primitive; what a guarantee consists in, and
  how it is enforced, is gestured at (loss of reputation) and not
  modelled.
- The addressee's role in assertion is delegated to other papers; within
  this one the informative update is either an implicature or an
  unconditional composition, both rejected.
- §7 treats seven speech-act types in a page or two each, without the
  linguistic tests applied to declarations and assertions.
- The evidence is grammatical judgement and typology; no corpus or
  experimental data.

## Open questions

- Whether "minimal change" can be given a definition that does not
  presuppose which propositions are relevant, or whether it is
  conversation-relative.
- How performative updates interact with the addressee's uptake: whether a
  declaration can fail by non-uptake, as assertion can, and where that is
  represented.
- Whether two utterances that produce the same performative update (the
  same guarantee or obligation) can still differ in the relationship they
  set up, which the model as given cannot represent.
