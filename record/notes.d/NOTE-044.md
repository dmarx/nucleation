---
number: 44
status: Read
formerly:
- NOTE-tmpbtj0b
paper: LIT-077
title: 'Grangier & Auffèves, What is quantum in quantum randomness?'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:1804.04807v1 (13 Apr 2018), 9 pp. That
    covers the abstract, Introduction, "Contextual objectivity" (Postulates
    0–2), "Randomness in a contextual world", "Theories of randomness:
    thermodynamics vs. quantum physics", the Conclusion, the acknowledgments
    and 26 references. Nothing was skipped. Figures 1–2 are box diagrams;
    their text and captions survived extraction and were read. Text was
    extracted with PyMuPDF from raw4/1804.04807.pdf. Read side by side with
    c15 (arXiv:2302.10778v3). Not compared with the typeset Phil. Trans. R.
    Soc. A version. The cited derivations, refs [13]–[15], were not read.).
    Upgraded from `Skimmed` to `Read`: the claims table, assumptions and
    results are new, and the skim is corrected where the full text
    disagreed.
date: '2026-09-25'
summary: >-
  The paper argues informally, with no equations anywhere in it, that an
  "elementary" system with a fixed finite number N of exclusive
  modalities, placed in contexts that can change, must behave
  unpredictably when the context changes: a return to C1 after C2 cannot
  be certain, or there would be N² > N joint modalities (p. 4). It asserts
  that adding one condition, that the context can change continuously,
  makes the N×N modality-transition matrix unistochastic, i.e. Born-rule,
  but defers that proof to refs [14, 15] (p. 5). The anti-reductionist
  conclusion follows from Postulate 0, which declares contexts
  non-contextual by definition, not from an argument against decoherence.
---

<!-- inactive-ok-file: LIT-001 — Rejected; named in Connections only to say no specific link holds -->

# NOTE-044: Grangier & Auffèves, What is quantum in quantum randomness?

## Contribution

The paper is a compact statement of the Contexts-Systems-Modalities (CSM) ontology, applied to one question: what makes quantum randomness quantum. Its one argument of its own is a reductio on p. 4. Suppose an elementary system with N = 2 modalities per context, where the context goes C1 → C2 → C1. If the final outcome were certain, the pair {X_C1, X_C2} would give four exclusive modalities, contradicting Postulate 2. So return is unpredictable, the "questions" do not commute, and the randomness is "ontological": "There are less available answers than possible questions" (p. 4). Everything beyond that is asserted or cited. The paper asserts that continuity of context gives exactly quantum theory (p. 5, citing [14, 15]). It makes interpretive claims: no universal wave function, the Schrödinger equation only models a context change, and reductionism is "meaningless" (p. 6). It adds an essay contrasting thermodynamics (the "k_B dice") with quantum randomness (the "ħ dice") (Fig. 2), which ends in the proposal of measurement-fuelled "quantum heat" engines (pp. 7–8, citing [23]–[25]).

## Key insight

In CSM, quantum randomness is not ignorance of a hidden state. It is what happens when a system that can give only N mutually exclusive answers in any context is asked questions from more than one context. There are more questions than a single N-valued state can answer, so answers across contexts can relate only probabilistically. The paper's slogan is that the *cause* is quantization (finite N), the *place* is a contextual world, and the extra ingredient that makes the probabilities quantum-mechanical is that contexts vary continuously (Fig. 2 left/right columns, p. 7).

## Assumptions

- **Realism about a partitioned world (p. 2).** An objective natural world, analysable into finite systems each surrounded by a context. "Phenomena" are unique, actual and observer-independent.
- **Condition 1, the classical case (p. 2).** Repeating the same question gives the same answer regardless of intervening questions. The state is then non-contextual.
- **Postulate 0 (p. 3).** Contexts have, *by definition*, non-contextual states. This is stated to break the recursion and to eliminate Wigner's-friend problems "per se".
- **Postulate 1 (p. 3).** States ("modalities") belong jointly to system and context. Modalities within one context are mutually exclusive. Nothing may be concluded across contexts that cannot be jointly realized.
- **Postulate 2 (p. 3).** An elementary system has a discrete, finite number N of exclusive modalities, the same in every context. The paper stresses this is "given through their phenomenology". **This is the load-bearing assumption of the p. 4 reductio.** It must be read as a bound on the *ontology* (no hidden joint state finer than N), not just the phenomenology, for the conclusion "ontological, not epistemic" to follow. See Limitations.
- **Prescriptions (i)–(ii) (p. 4).** An elementary system with N modalities in a context, and a change of context C1 → C2. These yield "ontological randomness", described by an N×N matrix of jump probabilities from X_C1 to Y_C2.
- **Prescription (iii) (p. 4).** "The state of the context can change continuously". Asserted to single out Born-rule probabilities, with proof in [14, 15].

## Key results

- **Non-commutation from quantization (p. 4).** For N = 2 and C1 → C2 → C1, the final modality in C1 cannot be predicted with certainty, by the reductio above. This is the only result argued in the text.
- **Hard vs soft contextuality (Fig. 1, pp. 3–4).** Contextuality is "universal". It is "soft" (forgettable, classical) when N is effectively unbounded, and "hard" (quantum) when N is small enough for the system to be elementary. This is an informal classification with no threshold given.
- **Quantum formalism from (i)–(iii) (pp. 4–5).** The probability matrix at a context change is unistochastic, so it "involves the complex unitary matrices characterizing the quantum formalism", and "the continuity argument is essential". Cited, not shown.
- **Three reversed hierarchies (p. 5).** Randomness and non-unitarity before determinism and unitarity. Quantization before interference. Actual before potential. The wave function is a "calculation tool", and there are "stochastic jumps from modality to modality" instead of reduction. All asserted.
- **Scope restriction (pp. 5–6).** The quantum formalism applies only to system–context partitions. There is "no wave function of … the whole Universe". The search "to dissolve the context in systems is meaningless". These follow from Postulate 0.
- **Thermodynamic outlook (pp. 6–8).** Stochastic thermodynamics' methods depend only on stochastic trajectories, so they apply to quantum (measurement-induced) randomness. "Quantum heat" can fuel an engine "in the absence of any heat source" [24]. Cited.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | A system with a fixed finite number of exclusive modalities, probed in two contexts, cannot return predictably to its C1 modality after C2; quantization implies non-commutation | weak–moderate | Informal reductio, p. 4, for N = 2 only. Valid if Postulate 2 bounds all joint states, including unobserved ones. Not stated for general N |
| C2 | The resulting randomness is ontological, not epistemic | weak | Follows from C1 only under the ontological reading of Postulate 2. Epistemic toy models with the same phenomenology are not addressed (see Connections) |
| C3 | Adding continuity of context (iii) yields exactly the quantum formalism: unistochastic, Born-rule transition matrices | assertion (here) | "The mathematical demonstration is available in [14, 15] and will not be recalled here" (p. 5) |
| C4 | Complex numbers in interference are a consequence of quantized modalities | assertion | p. 5. No argument in text. Presumably rests on [14, 15] (unverified) |
| C5 | Unitary evolution is only a calculation tool; the wave function has no physical existence | assertion | p. 5. Interpretive |
| C6 | Rebuilding the classical world from many quantum systems (decoherence, quantum Darwinism) is precluded | weak | Follows from Postulate 0 by stipulation (p. 6). No argument engages decoherence theory |
| C7 | Postulate 0 eliminates Wigner's-friend-type paradoxes "per se" | assertion | p. 3 |
| C8 | Quantum measurement-induced "quantum heat" can fuel an engine with no heat source, so quantum randomness is a thermodynamic resource | moderate (by citation) | Refs [23]–[25] (the authors' own work). Not shown here |
| C9 | CSM, unlike Relational QM, deduces rather than postulates quantum randomness | weak | p. 6. The deduction is C1 plus the cited C3 |

## Concepts

- **Context.** The large set of systems surrounding a system. In practice it is the measuring apparatus's settings. Its state is non-contextual by Postulate 0 (pp. 2–3).
- **ID card.** The sequence of answers X_{C(t_i)}(t_i) collected as the context's settings vary (p. 2).
- **Modality.** A contextual state: an ID card upgraded to a state, valid only for a given context. It is objective, and modalities in one context are mutually exclusive (Postulate 1).
- **Elementary system.** A system with a fixed, finite, context-independent number N of exclusive modalities (Postulate 2).
- **Hard / soft contextuality.** Hard means the context cannot be forgotten, as for elementary systems. Soft means contexts exist but can be ignored, as when N is unbounded (Fig. 1).
- **Intrinsic / epistemic / ontological / quantum randomness.**
  - *Intrinsic*: postulated on metaphysical grounds.
  - *Epistemic*: ignorance of a hidden state.
  - *Ontological*: from quantization in a contextual world, "less available answers than possible questions".
  - *Quantum*: ontological randomness with Born-rule probabilities, singled out by (iii) (pp. 4–5).
- **Contextual objectivity.** The ontology in which the real is the modality, jointly a property of system and context (p. 3, after [13, 16]).
- **Quantum heat.** The energy fluctuations induced by quantum measurement, treated as heat in a stochastic-thermodynamics accounting (p. 8, after [24]).

## Connections

- **c15, Barandes, *The Stochastic-Quantum Correspondence* ([LIT-086](../literature.d/LIT-086.md)).** This paper predates c15 and does not cite it. c15 cites this paper's ref. [14] (footnote 7). The side-by-side reading gives three points.
  1. **Same algebra.** Both end at matrices of |U_ij|² for a unitary U.
  2. **Opposite logic.** Here, unistochasticity is claimed to be *forced* by postulates plus continuity (cited, not shown). In c15 it is *chosen* as a representation, after dilation, of an arbitrary stochastic Γ. The configuration-basis Born rule is then definitional.
  3. **Different object.** The matrix here relates the modalities of two *contexts*. c15's Γ relates configurations at two *times*. The CSM-shaped object in c15 is its hybrid matrix, Eq. (89), which at t → t′ is |ẽ_{α,i}|², a change-of-basis unistochastic matrix between an observable's eigenbasis and the configuration basis.

  Further points of contrast:
  - **Complex numbers.** This paper holds them to be derived (C4). c15 holds them optional, with reals, quaternions and other algebras admissible, and complex numbers only "generically" necessary because unistochastic ⊋ orthostochastic.
  - **Ontology.** CSM's is contexts plus modalities. c15's is configurations plus an indivisible law.
  - **Measurement devices.** Both deny them a fundamental status as "measurement", but in opposite directions. CSM makes the context primitive and irreducible (Postulate 0). c15 makes the device an ordinary subsystem whose status comes from a division event (c15 §4.4).
  - **Common ground.** Both treat the wave function as a calculation tool and say so in nearly the same words (here p. 5, c15 §5.1).
- **Quasi-quantization, Spekkens ([LIT-007](../literature.d/LIT-007.md); reading reads/14.md).** The only textual link is that Spekkens 2007 (the toy theory) appears as ref. [17] and is never cited in the text. The p. 4 "[? ]" may be where it was meant to go (unverified). The texts support one substantive point of tension. Per the reading of [LIT-007](../literature.d/LIT-007.md), the epistricted theory of bits is the Spekkens 2007 toy theory (asserted there, C6 of that reading). [LIT-007](../literature.d/LIT-007.md) files noncommutativity, complementarity and collapse as only *weakly* nonclassical (its Table II, asserted rather than derived). That is, they are reproduced by a classical ontological model with *epistemic* randomness and more ontic states than knowable answers.

  That is exactly the phenomenology this paper's p. 4 reductio uses to conclude *ontological* randomness. A toy bit has two exclusive answers per question, and certainty about one question is destroyed by asking another. So the reductio's step from "unpredictable on return to C1" to "ontological" goes through only if Postulate 2 forbids a finer hidden ontic state, which the paper defines phenomenologically (p. 3). Stated with the texts' support: the CSM argument does not engage the epistricted counter-model, and [LIT-007](../literature.d/LIT-007.md)'s programme locates the unavoidable nonclassical residue in contextuality and Bell violations, not in non-commutation. This paper also cites Bell violations (refs [2]–[8]) and Kochen–Specker [12] as its motivation. It never uses them in its argument.
- **Lindgren & Liukkonen ([LIT-001](../literature.d/LIT-001.md), Rejected; reading reads/35.md).** No citation and no shared method. [LIT-001](../literature.d/LIT-001.md) derives a Schrödinger-type equation from a stochastic-control HJB equation by inserting i by hand. This paper derives no equation of motion at all and holds the Schrödinger equation to have no "absolute meaning" (p. 6). The only common theme is taking randomness to be prior to the wave equation. The texts support nothing more specific.
- **Named lineage.** CSM [13, 16]. The formal reconstruction [14, 15]. Hardy 2001 and Rovelli 1996 as other reconstructions (ref. [11] is Rovelli; the contrast is on p. 6). Zurek's decoherence and quantum Darwinism [18, 20] as foil. Seifert's stochastic thermodynamics [22]. The authors' own quantum-heat work [23]–[26].

## Bearing on the record

- The nucleation record has no THEORY documents yet (theory.d holds only the README stub). This paper would not support one alone: its one argued claim (C1) is informal and N = 2 only, and its main claim (C3) is cited. Any THEORY on "Born-rule probabilities from continuity of context" should source Auffèves & Grangier 2017 (arXiv:1610.06164) after that is read. It should not cite this paper.
- [LIT-077](../literature.d/LIT-077.md)'s summary says adding the continuity condition "yields Born-rule, unistochastic probabilities". That is what the paper *asserts*, with the proof elsewhere. The summary should say the derivation is cited, not given.
- **ML practice: nothing for the Anthology of the SOTA.** The paper contains no method, model or experiment bearing on machine learning. The tag `probabilistic-modeling` on [LIT-077](../literature.d/LIT-077.md) reflects the subject ("randomness"), not any modelling content.

## Limitations

- **No mathematics in its own text.** The quantum formalism, unitarity and complex numbers are all delegated to [14, 15] (p. 5).
- **The reductio (C1).** It is given for N = 2 and one C1 → C2 → C1 sequence. The inference "certainty on return ⇒ 4 exclusive modalities" treats a predictable joint history as a joint modality, which is the point at issue. Its conclusion, *ontological* randomness, needs Postulate 2 as an ontic bound, while the paper states that postulate phenomenologically. Epistemic models with a knowledge restriction (Spekkens 2007, cited as [17] but not discussed) reproduce the same unpredictability.
- **Anti-reductionism by postulate.** It is built into Postulate 0 and into the "difference of status between system and context" (p. 6). The paper offers no criterion for which systems qualify as contexts beyond Condition 1, and no argument that decoherence fails to deliver such systems.
- **Condition (iii) is informal.** It is not said what topology or parameterization of context states is meant, nor why Stern–Gerlach angles are representative (p. 4).
- **The thermodynamics half is a survey of the authors' own work.** Nothing in it depends on CSM specifically. The paper itself says stochastic thermodynamics "solely rel[ies] on the notion of stochastic trajectory" whatever the source of randomness (p. 7).
- **Textual defects.** A broken citation "[? ]" on p. 4, and an uncited reference [17].

## Open questions

- Does the CSM derivation in [14, 15] actually need continuity of context for unistochasticity, or also further assumptions (e.g. a Gleason/Uhlhorn-type step)? That is unverified here, and settled only by reading arXiv:1610.06164 and 1801.01398.
- Can Postulate 2 be stated so that it excludes epistricted counter-models without assuming the conclusion? Equivalently, what empirical phenomenon, beyond non-commutation, does CSM claim is inexplicable epistemically? The candidates the cited literature offers are contextuality inequalities and Bell violations. The paper invokes them in its introduction but does not connect them to its argument.
- What distinguishes a "context" physically? That is, when does Condition 1 hold well enough for a system to count as one, and how does that compare with decoherence-based pointer stability?

## Corrections to the seeded skim

- **Seed (joint with c15): "both reach the Born rule through the same unistochastic transition matrices."** This paper does not reach the Born rule at all in its own text. It *defines* quantum randomness as the case "where the probabilities at the change of context follow Born's rule" (p. 4). It then asserts that condition (iii) singles that case out, "The mathematical demonstration is available in [14, 15] and will not be recalled here. It boils down to evidencing that the probability matrix is uni-stochastic" (p. 5). Where a matrix appears, it is an N×N matrix of conditional probabilities between the modalities of two *contexts* (p. 4), i.e. two measurement bases. It is not a time-transition matrix between configurations as in c15. Unistochasticity is the claimed *conclusion* here and a representational *choice* in c15. c15 itself says as much in its footnote 7, which points to Eqs. (3)–(6) of ref. [14] as "similar-looking formulas" used "for conceptually different purposes".
- The dossier says the paper states hierarchy reversals ("randomness and non-unitarity come first…; quantization comes first and interference second"). Correct, but all three reversals (p. 5) are assertions that rest on the derivation deferred to [14, 15]. That includes "complex numbers associated to interferences are a consequence of the quantization of exclusive modalities". The paper's own claim to have derived "probabilistic nature, non-commutation of the questions … without invoking any mathematical formalism" (p. 5) covers only the p. 4 reductio, not unitarity or complex numbers.
- The dossier treats the anti-reductionist claim as "strong and should be checked against decoherence-based accounts". The paper does not argue it against decoherence. It follows from Postulate 0 ("By definition, contexts are characterized by non-contextual states", p. 3), a postulate the dossier omits, and from the stipulation that "CSM postulates the difference of status between system and context" (p. 6). Decoherence and quantum Darwinism are named only as examples of the reductionist programme (pp. 5–6). No technical engagement is offered.
- The dossier does not record two textual defects. On p. 4, the sentence "This non-commutation is characteristic of hard contextuality." ends with an unresolved citation "[? ]". Ref. [17] (Spekkens 2007, the toy theory) is in the bibliography but cited nowhere in the text. Whether [17] was the intended target of the broken marker is unverified.
- The rest of the dossier's skim (sections, Postulates 1–2, the prescriptions (i)–(iii), the Relational-QM contrast, and the stochastic-thermodynamics section including quantum heat) is accurate.
