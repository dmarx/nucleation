---
number: 737
status: Skimmed
formerly:
- NOTE-tmp5ey9r
paper: LIT-945
title: 'Schmid, Selby & Spekkens — Unscrambling the omelette of causation and inference'
version: 2
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Partly read, from the arXiv PDF (2009.03297v3, 19 May 2021, 68 pp.),
    text extracted with pdftotext. Read in full: the abstract and §I's
    prose; the opening of §IV; §V (inferential equivalence, quotiented
    theories, "To make an omelette"); §VI (classical realist
    representations and Leibnizianity); §VIII (noncontextuality no-go
    theorems); §IX (nonclassical realist representations); §X.A–B; and
    Appendices A and B. §VII (Bell-like no-go theorems) and §X.C were read
    quickly. Not read: §I.A, §II and §III (the causal and inferential
    process theories and their rewrite rules), §IV.A–B (the operational and
    classical realist CI theories, prediction maps, normal forms), and
    Appendices C–G, which hold every proof. The paper's equations are
    string diagrams, which the text layer does not carry; definitions and
    results below are taken from the prose that states them. Hence
    Skimmed. Quotations were checked against the extracted text by script.
- version: 2
  date: '2026-10-14'
  note: >-
    Correction after the reading of LIT-980 (NOTE-tmp5bnaz): the bullet on
    the question's premise said the paper supports a single binary
    judgement showing preparation contextuality. It shows only that a
    prepare-measure scenario has no Bell-like test. A correction line
    added; the reading is unchanged.
date: '2026-10-14'
summary: >-
  In a process-theoretic framework that keeps causal and inferential
  structure apart, generalized noncontextuality becomes the demand that a
  realist representation preserve inferential equivalence. A Leibnizian
  classical realist representation implies a generalized-noncontextual one,
  so every noncontextuality no-go theorem is a no-go for Leibnizian
  representations; the converse is a conjecture. Bell-like theorems deny
  any classical realist representation, a weaker assumption, while
  noncontextuality theorems apply even to a prepare-measure scenario with
  no Bell-like constraint.
---
<!-- inactive-ok-file: THEORY-011 THEORY-015 QUESTION-067 CLAIM-142 CLAIM-046 — Proposed or Open; the theories, question and claims this reading bears on, open -->

# NOTE-737: Schmid, Selby & Spekkens — Unscrambling the omelette of causation and inference

## Contribution

The paper builds causal-inferential (CI) theories. Each is a causal
process theory (laboratory procedures, or functions between classical
variables) joined to a classical inferential theory (Bayesian probability
and Boolean logic), with rules for how the two interact and a prediction
map. In this frame it restates Bell-like and noncontextuality no-go
theorems as statements about which realist representations exist. It
introduces Leibnizianity, the preservation of inferential equivalence, and
proves that it implies the authors' rehabilitated generalized
noncontextuality. It then sets out what a nonclassical realist theory
would have to satisfy to escape both kinds of theorem.

## Key insight

Two processes are inferentially equivalent when they license the same
predictions in every scenario. Quotienting by that equivalence, which is
what GPTs and ontological models do, erases causal information. The
paper's example is a coin-flip mixture of the two constant bit functions
and a coin-flip mixture of identity and flip. One has no causal link from
input to output, the other has one, and both give the completely
randomising channel. Noncontextuality is then a question about the map
from unquotiented operational descriptions to realist ones. Does it send
inferentially equivalent processes to inferentially equivalent ones? Bell's
theorem asks only whether such a map exists at all.

## Assumptions

- **Classical inference.** The inferential theory is Bayesian probability
  plus Boolean logic, called "the classical theory of inference".
  Alternatives are discussed but not built.
- **Diagram preservation.** A classical realist representation ξ is a
  diagram-preserving map from the operational CI theory to the classical
  realist one, preserving predictions and ignorability (Definition VI.1).
  The operational diagram is taken to encode one's hypothesis about the
  fundamental causal-inferential structure, not the calculational circuit
  (Appendix B). Appendix B argues this costs no generality: a holist simply
  draws one system where the circuit has two.
- **Inferential equivalence quantifies over every tester in the theory.**
  "Two elements of P-S are inferentially equivalent if and only if they
  lead to exactly the same predictions, no matter which causally closed
  diagram they are embedded in" (Definition V.1).
- **The realist causal theory is functional dynamics** (structural-equation
  style), with states of knowledge as distributions over functions.
- **Finiteness** assumptions are mentioned as made, in §X.C, but were not
  located in the parts read.

## Key results

- **Inferential equivalence is a congruence** (Lemma V.7), so a theory can
  be quotiented by it (Definitions V.8, V.11). For causally closed
  processes it reduces to equality of the stochastic maps they predict
  (Lemma V.3). For classical realist processes it has an intrinsic form,
  equality of the associated substochastic map (Lemma V.10, proof in
  Appendix F, not read).
- **What quotiented theories are (§V.A.2, §V.B.2).** GPTs are argued to be
  subtheories of quotiented operational CI theories. The proof is
  deferred to a forthcoming paper. Traditional ontological models are the
  codomain of a quotiented classical realist CI theory.
- **Quotienting scrambles causation and inference (§V.C).** σ_c =
  ½[f_0] + ½[f_1] and σ_d = ½[f_id] + ½[f_flip] "refer to completely
  distinct causal relations" yet are inferentially equivalent.
- **Theorem VI.2.** Every classical realist representation is inferentially
  equivalent to one that maps states of knowledge about procedures to
  states of knowledge about functions by a stochastic map Ξ (proof in
  Appendix G, not read). Whether every representation has that form is
  left open, with an appeal to "autonomy".
- **Leibniz's methodological principle (§VI.C).** "If an ontological theory
  implies the existence of two scenarios that are empirically
  indistinguishable in principle but ontologically distinct … then the
  ontological theory should be rejected and replaced with one relative to
  which the two scenarios are ontologically identical." The authors say
  that "it is necessary to consider an epistemological generalization of
  Leibniz's principle" to motivate the rehabilitated notion.
- **Definition VI.5 (Leibnizianity).** ξ is Leibnizian if D ∼_p E implies
  ξ(D) ∼_p∗ ξ(E). Proposition VI.6: this holds iff there is a
  representation ξ̃ of the quotiented operational theory with ξ̃ ∘ ∼_p =
  ∼_p∗ ∘ ξ. So ∃ Leibnizian ξ ⇒ ∃ ξ̃ (Eq. 200). The converse is Conjecture
  1.
- **Definition VIII.2 (generalized noncontextuality, rehabilitated).** It
  constrains a different map, ζ, from the unquotiented operational theory
  to the *quotiented* realist theory. ζ is generalized-noncontextual if it
  preserves inferential equivalence: "inferentially equivalent states of
  knowledge about experimental procedures must be represented by the same
  stochastic map". ζ is "the closest counterpart in our framework to the
  pre-existing notion of an ontological model". Proposition VIII.3 and
  Eq. 214: ∃ generalized-noncontextual ζ ⇔ ∃ ξ̃. The notion covers every
  kind of process, combs and circuit fragments included, "a universal
  notion from the get-go". Old no-go proofs carry over, "since all that has
  changed is how one conceptualizes the mathematics".
- **Eq. 215.** ∃ Leibnizian ξ ⇒ ∃ generalized-noncontextual ζ ⇔ ∃ ξ̃.
  "Every no-go theorem for generalized-noncontextual classical realist
  representations yields a no-go theorem for Leibnizian classical realist
  representations." The converse is Conjecture 1′. If it is false, there
  may be new no-go theorems from Leibnizianity alone.
- **Context, and why Leibnizianity is not "noncontextuality" (§VIII.B).** A
  process's context is "information about a process which is irrelevant
  for making predictions". Under a Leibnizian ξ, an operational
  process's context may fix the context of its image, but not the image's
  equivalence class. Only for ζ, whose codomain has no contexts, is the
  demand a context-independence.
- **A quotiented theory is neither contextual nor noncontextual.** In the
  authors' words, "it is a
  category mistake to ask whether ξ̃ is generalized-noncontextual or not."
  An experiment that supports a noncontextuality no-go but no Bell-like
  one is always consistent with some ξ, given context-dependence. Its
  quotiented model may admit no representation.
- **Prepare-measure (§VIII.C).** For a preparation with setting X and
  outcome A, and a measurement with setting Y and outcome B, "the only
  restrictions on F-S-realizable distributions over X, Y, A and B are
  that Y must be independent of A and X". So there is no Bell-like no-go
  for this structure, but noncontextuality no-goes exist. Existence of a
  generalized-noncontextual representation coincides with
  simplex-embeddability and with a positive quasiprobability
  representation of the GPT. Both are cited, not proved here.
- **The comparison (§VIII.C).** "Bell-like no-go theorems are based on a
  weaker assumption", namely that some ξ exists. Noncontextuality no-go
  theorems "can be proven for a broader set of causal-inferential
  structures—even those involving just a single causal system".
- **Ways out (§VII.B, §VIII.D, §IX).** The conventional exits from Bell's
  theorem are superluminal causation and superdeterminism. Both are
  criticised as fine-tuned. The conventional exit from noncontextuality
  no-goes "requires a renouncement of Leibnizianity". The proposed exit
  from both is a nonclassical realist CI theory XF-XS, which must meet five
  criteria (§IX.A):
  - actual rather than potential causal influence;
  - propositions attach to every system;
  - knowledge propagates through every causal mechanism;
  - a unique prediction map;
  - intrinsic and external inferential equivalence coincide.
  Leibnizianity is defined for such representations as before
  (Definition IX.2). No such theory is constructed.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Inferential equivalence is a process-theory congruence, so CI theories can be quotiented by it | strong (proof read) | Lemmas V.6–V.7 |
| C2 | Quotienting erases causal distinctions | strong | the σ_c / σ_d example, §V.C |
| C3 | A Leibnizian classical realist representation implies a generalized-noncontextual one | strong (follows from definitions as stated) | Proposition VI.6, Proposition VIII.3, Eq. 215 |
| C4 | The converse holds | conjecture | Conjecture 1, Conjecture 1′ |
| C5 | Every classical realist representation is inferentially equivalent to one built from a stochastic map on states of knowledge | strong (proof, not read) | Theorem VI.2, Appendix G |
| C6 | Prepare-measure structures admit no Bell-like no-go but do admit noncontextuality no-goes | moderate (stated, derivation not shown in text) | §VIII.C |
| C7 | GPTs are subtheories of quotiented operational CI theories | weak here (proof deferred to a forthcoming paper) | §V.A.2 |
| C8 | A satisfactory realist account of quantum theory may be nonclassical in its causation and inference | programmatic | §IX, by analogy with nonEuclidean geometry |

## Concepts

- **Causal-inferential theory.** A triple of process theories (causal,
  inferential, and their combination) with maps between them and a
  prediction map p (Eq. 65).
- **Operational CI theory (P-S).** Laboratory procedures (PROC) with
  classical inference (SUBSTOCH). Its processes describe only *potential*
  causal influence.
- **Classical realist CI theory (F-S).** Functions between classical
  variables (FUNC) with classical inference. Its processes describe
  *actual* causal influence, and it has a unique prediction map (Theorem
  IV.4).
- **Inferential equivalence (∼_p).** The same predictions in every
  causally closed embedding. It replaces the older operational equivalence
  of procedures, because it relates *states of knowledge about*
  procedures.
- **Context.** Information about a process that is irrelevant for
  prediction, that is, which member of its inferential equivalence class it
  is.
- **Leibnizianity.** A realist representation preserves inferential
  equivalence.
- **Generalized noncontextuality (rehabilitated).** A representation ζ into
  the *quotiented* realist theory preserves inferential equivalence.
- **Quotiented theory.** Processes taken up to inferential equivalence;
  GPTs and ontological models are of this kind.

## Connections

The definition of generalized noncontextuality it rehabilitates is
Spekkens 2005 ([LIT-266](../literature.d/LIT-266.md)), cited as [6]. Eq. 214 is presented as the
analogue of Proposition 1 of Schmid, Selby, Pusey and Spekkens's structure
theorem ([LIT-003](../literature.d/LIT-003.md), cited as [20]): an operational theory has a
generalized-noncontextual model iff its GPT has an ontological model. The
statement of Leibniz's principle is taken from Spekkens 2019
(arXiv:1909.04628, cited as [26], not held), which argues that Leibniz
proposed it and Einstein endorsed it. The causal side follows structural
equation models (Pearl). The fine-tuning arguments against the
conventional exits from Bell's theorem are Wood and Spekkens's (cited as
[21], not held). The paper does not mention Kochen–Specker or
sheaf-theoretic contextuality.

## Bearing on the record

- **[LIT-945](../literature.d/LIT-945.md)'s filing claim is accurate, with the direction stated.** The
  paper "characterizes generalized noncontextuality process-theoretically
  and derives it from a principle of Leibnizianity" in this sense:
  existence of a Leibnizian classical realist representation implies
  existence of a generalized-noncontextual one (Eq. 215). So a
  noncontextuality no-go refutes Leibnizian representations. Whether a
  Leibnizianity failure implies a noncontextuality failure is conjectured,
  not shown.
- **[QUESTION-067](../questions.d/QUESTION-067.md): what refuting Spekkens's notion commits the
  record to.**
  - Within classical realism, it commits the record to renouncing
    Leibnizianity, the conventional way out. The alternative is a realist
    account whose causation or inference is nonclassical (§VIII.D, §IX).
  - It does *not* show that no classical realist account exists. That is
    the stronger, Bell-like conclusion, and §VIII.C notes that
    noncontextuality no-goes rest on the stronger assumption.
- **Support for the question's premise.** For a prepare-measure structure,
  the only constraint on classical realist distributions is that the
  measurement setting is independent of the preparation's setting and
  outcome. So no causal-compatibility (Bell-like) test exists there, while
  a noncontextuality test can. This matches [QUESTION-067](../questions.d/QUESTION-067.md)'s claim that a
  single binary judgement can show preparation contextuality. The paper
  speaks of Bell-like and causal-compatibility constraints, not of sheaf
  covers. The step to the sheaf notion still rests on [LIT-266](../literature.d/LIT-266.md) and the
  record's own join in [THEORY-015](../theory.d/THEORY-015.md).
  *Correction (2026-10-14, [NOTE-tmp5bnaz](NOTE-tmp5bnaz.md)):* the paper shows only that a
  prepare-measure scenario has no Bell-like test, not that a single
  binary judgement suffices. Catani et al.'s witness ([LIT-980](../literature.d/LIT-980.md)) needs two
  binary judgements never made together and four preparations.
- **Two constraints on any pragmatic test.**
  - Inferential equivalence quantifies over every tester in the
    operational theory. A probe-relative equivalence, as in [CLAIM-142](../claims.d/CLAIM-142.md) and
    [CLAIM-046](../claims.d/CLAIM-046.md), is this relation only when the probe family exhausts the
    testers, that is, is tomographically complete for the renderings. The
    paper treats tomographic completeness as a defining feature of GPTs
    (§V.A.2).
  - The noncontextuality question can be put only of the unquotiented
    description. A model that already identifies equivalent renderings
    "is not the sort of thing that can be either
    generalized-noncontextual or generalized-contextual". The test must
    keep distinct renderings distinct and state their equivalences
    separately. This is the form [QUESTION-067](../questions.d/QUESTION-067.md)'s "What would answer it" asks
    for.
- **[THEORY-016](../theory.d/THEORY-016.md).** The paper restates, citing [LIT-003](../literature.d/LIT-003.md) and others, that
  existence of a generalized-noncontextual representation coincides with
  simplex-embeddability and a positive quasiprobability representation.
  It is a restatement, not an independent proof. It agrees with [THEORY-016](../theory.d/THEORY-016.md).
- **[THEORY-011](../theory.d/THEORY-011.md)'s "What this does not say".** It ascribes the choice of
  notion to "Spekkens's Leibnizian methodological principle". That wording
  belongs to this paper (§VI.C, after its [26]), not to [LIT-266](../literature.d/LIT-266.md). [LIT-266](../literature.d/LIT-266.md)
  argues from "ontological economy". This paper is the better citation for
  it. It also says the 2005 notion needs an *epistemological*
  generalization of Leibniz's principle to be motivated in its
  rehabilitated form.
- No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- Only classical inference is built. The nonclassical realist theory that
  is the paper's goal is specified by desiderata, not constructed.
- The converse of the Leibnizianity ⇒ noncontextuality implication
  (Conjecture 1 and 1′) and the uniqueness of the classical normal form are
  open. Whether all classical realist representations take the form of Eq.
  190 is also open.
- The identification of GPTs with quotiented operational CI theories is
  deferred to a later paper.
- Diagram preservation is harmless only given the authors' reading of
  operational diagrams as causal hypotheses (Appendix B). Under the usual
  calculational reading, it builds in assumptions such as ontic
  separability.
- The framework describes a single agent's reasoning (§X.C).
- No noise-robust or experimental treatment of noncontextuality is given
  here; §VIII.C defers to earlier work.

## Open questions

- Does a no-go for Leibnizian representations always yield a no-go for
  generalized noncontextuality (Conjecture 1′)? A Leibnizianity no-go
  with a generalized-noncontextual ζ would refute it.
- What axioms for a quantum realist CI theory (QF-QS) meet the five
  criteria of §IX.A and represent operational quantum theory
  Leibnizianly?
- For this reading: §II–IV and the proofs in Appendices E–G were not read.
  A Read note should check Theorem VI.2's proof and the prepare-measure
  realizability claim of §VIII.C, which is stated without a derivation in
  the text.
