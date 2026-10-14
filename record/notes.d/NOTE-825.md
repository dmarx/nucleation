---
number: 825
status: Read
formerly:
- NOTE-tmp5bnaz
paper: LIT-980
title: 'Catani et al. — What is nonclassical about uncertainty relations?'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read in full from the arXiv PDF (2207.11779v2, 12 December 2022, 13
    pages), text extracted with pdftotext in reading-order and layout
    modes: the abstract, the whole letter, figure captions 1–7, and
    appendices A (the analytic proof of Eq. 12, step by step), B (the
    linear-program inequalities of Schmid, Spekkens and Wolfe), C (three
    measurements) and D (the qubit uncertainty relation in its several
    forms). Figures are state-space sketches and plots without a text
    layer and were read from their captions and the text that describes
    them. The arithmetic of Eqs. A28–A33 and the tightness construction
    A35–A38 were checked by hand.
date: '2026-10-14'
summary: >-
  For any state whose four-state reflection orbit is realizable (equal
  predictabilities with flipped signs, and ½s1+½s3 = ½s2+½s4),
  preparation noncontextuality forces |⟨X⟩| + |⟨Z⟩| ≤ 1, tight, without
  perfectly distinguishable states. In a theory where every state has
  such an orbit, the bound constrains the uncertainty relation itself: the
  qubit's circle violates it, up to √2, the stabilizer octahedron
  saturates it, and the simplicial theory escapes it because its jointly
  predictable states lack the orbit.
---
<!-- inactive-ok-file: THEORY-231 THEORY-010 CLAIM-009 CLAIM-037 THEORY-315 — Proposed; the theories and claims this reading bears on or files, open -->
<!-- inactive-ok-file: NOTE-737 — Skimmed; the partial reading of LIT-945, cited for what it says of prepare-measure scenarios -->

# NOTE-825: Catani et al. — What is nonclassical about uncertainty relations?

## Contribution

Before this letter it was known that a nontrivial trade-off between the
predictabilities of two measurements occurs in theories that admit a
generalized-noncontextual model (Gaussian quantum mechanics, odd-prime
stabilizer theories, the qubit stabilizer theory), so the mere existence
of an uncertainty relation is not evidence of nonclassicality. The letter
derives a noncontextuality inequality, |⟨X⟩| + |⟨Z⟩| ≤ 1, that bounds the
predictabilities of two binary measurements for any state with a certain
symmetry orbit. In theories where every state has that orbit it is a
bound on the *form* of the uncertainty relation, and the qubit's circular
trade-off violates it.

## Key insight

Noncontextuality cannot constrain a single state. It constrains states
through the operational equivalences among them. The trick is that a
state's predictabilities are shared by its reflections: the four states
with the same |⟨X⟩| and |⟨Z⟩| and all four sign patterns. When those four
also satisfy one equivalence of mixtures, the predictabilities of any one
of them are bounded by a linear diamond. So what is nonclassical about
the qubit is not that X and Z cannot both be predictable, but that they
can be *more* jointly predictable than any noncontextual theory with the
same symmetry allows.

## Assumptions

- **Prepare-measure scenarios only**, with a finite ontic state space
  ("it suffices to consider Λ finite").
- **Generalized noncontextuality for preparations only** (footnote 3):
  P ≃ P′ ⇒ μ(λ|P) = μ(λ|P′), where P ≃ P′ means "leading to the same
  statistics for all possible measurements" (Eq. 8). The term is used
  throughout in Spekkens's sense, "distinct from the Kochen-Specker notion"
  (footnote 1).
- **Binary measurements X and Z**, with predictability |⟨X⟩|, where
  ⟨X⟩ = (e₊₁|X − e₋₁|X)·s (Eq. A1).
- **The A²₁-orbit-realizability condition on a state s1**, which is two
  conditions:
  - *equal-predictability counterparts* (Eq. 10): states s2, s3, s4 with
    ⟨X⟩s1 = −⟨X⟩s2 = −⟨X⟩s3 = ⟨X⟩s4 and
    ⟨Z⟩s1 = ⟨Z⟩s2 = −⟨Z⟩s3 = −⟨Z⟩s4;
  - *an operational equivalence* (Eq. 11): ½s1 + ½s3 = ½s2 + ½s4.
  For two measurements the second does not follow from the first and
  must be imposed (Appendix C).
- **Outcome-deterministic response functions**, justified, not assumed:
  following Schmid, Spekkens and Wolfe, determinism is without loss of
  generality when there are no nontrivial operational equivalences among
  the measurement effects, "as is the case here" (Appendix A).
- **Exact operational equivalence.** The proof uses Eq. 11 as an
  equality. The text says the inequality "is noise-robust, and can
  therefore be tested experimentally" with the techniques of Mazurek et
  al., but it does not carry out that analysis.
- **A 4-dimensional real vector representation** for all the foil
  theories compared. The general result does not need it.

## Key results

- **Main result (Eq. 12; Appendix A).** In any operational theory, if a
  state s1 is A²₁-orbit-realizable relative to X and Z, then any
  preparation-noncontextual model of these states and measurements
  satisfies |⟨X⟩| + |⟨Z⟩| ≤ 1.
  - The proof reduces to four ontic states (one per pair of X and Z
    outcomes), parameterizes μ2, μ3, μ4 from μ1 = (a, b, c, d) by single
    parameters ε, γ, δ (Eqs. A13–A27), imposes Eq. A6
    (½μ1 + ½μ3 = ½μ2 + ½μ4, from Eq. 11 and noncontextuality) to get
    a + d = b + c + (ε + γ + δ), and bounds
    ⟨X⟩ + ⟨Z⟩ = 2(b − c) = 1 − (ε + γ + δ) − 4c ≤ 1 − c ≤ 1 (Eq. A33).
  - Equivalently four linear inequalities, ±⟨X⟩ ± ⟨Z⟩ ≤ 1 (Eq. A34), a
    diamond (Fig. 4).
  - *Tight*: the explicit model μ1 = (1/4 + u, 1/2, 0, 1/4 − u) and its
    reflections (Eqs. A35–A38), u ∈ [−1/4, 1/4], reaches every point with
    ⟨X⟩ + ⟨Z⟩ = 1.
  - It also follows from the complete set of eight inequalities that
    Schmid, Spekkens and Wolfe derived by linear program for this
    equivalence (Appendix B, Eq. B1), which reduce to Eq. A34 under the
    A²₁ condition. The letter corrects a typo in that earlier paper (P12,
    not P21, in the sixth inequality).
  - *Holds when:* the orbit condition holds for the state. It needs no
    perfectly distinguishable pairs.
- **Constraint on the form of the uncertainty relation.** A theory in
  which every state is A²₁-orbit-realizable is said to have A²₁
  symmetry. There Eq. 12 is "a universal constraint on the predictability
  tradeoff", that is, on the ZX-uncertainty relation itself.
- **The qubit violates it.** The qubit's ZX-uncertainty relation is
  ⟨X⟩² + ⟨Z⟩² ≤ 1 (Eq. 1), the strongest one for X and Z (Appendix D,
  where it is also written ΔX² + ΔZ² ≥ 1 and Cx² + Cz² ≤ 3/2). It meets
  the bound only where |⟨X⟩| = 1 or |⟨Z⟩| = 1, and the largest violation
  is |⟨X⟩| + |⟨Z⟩| = √2 at |⟨X⟩| = |⟨Z⟩| = 1/√2.
- **The foils (Eqs. 3–6; Fig. 2a).**
  - *Qubit stabilizer theory* (octahedron): |⟨X⟩| + |⟨Z⟩| ≤ 1, which
    saturates the bound; it admits a noncontextual model.
  - *η-depolarized qubit* (ball of radius 1 − η):
    ⟨X⟩² + ⟨Z⟩² ≤ (1 − η)². It satisfies the bound if η ≥ 1 − 1/√2 ≈ 0.293.
    It admits a noncontextual model for η ≥ 2/3 (Marvian, cited).
  - *Gbit* (cube): |⟨X⟩|, |⟨Z⟩| ≤ 1, with A²₁ symmetry, so it reaches the
    algebraic maximum 2 and is "even further than the qubit theory from
    being classically explainable".
  - *Simplicial theory* (tetrahedron, two classical bits): the same
    relation as the gbit, but it does not have A²₁ symmetry. Its orbit-
    realizable states are exactly the embedded octahedron, which satisfies
    the bound. The vertices that reach |⟨X⟩| = |⟨Z⟩| = 1 have
    equal-predictability counterparts but fail Eq. 11. So no
    contextuality is witnessed, as it must not be, since this theory has
    a noncontextual model (the vertices as ontic states).
- **Three measurements (Eq. 13; Appendix C).** For an A³₁-orbit-
  realizable state, |⟨X⟩| + |⟨Y⟩| + |⟨Z⟩| ≤ 1 (an octahedron, Fig. 7).
  Here the equivalences (Eq. C6) follow from the equal-predictability
  condition alone, so the orbit condition is just Eq. C5. The qubit
  reaches √3 at |⟨X⟩| = |⟨Y⟩| = |⟨Z⟩| = 1/√3. *Not proved analytically*:
  "we do not provide an analytic proof here"; it was checked by
  computational algebra (acknowledgement to Elie Wolfe).
- **A remark on axioms (Appendix C).** Taking A³₁ symmetry plus "one can
  realize all states consistent with noncontextuality" as axioms for a
  4-dimensional real representation yields the octahedral state space,
  the state space of Spekkens's toy theory. Stated as a suggestion, not
  developed.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Existence of an uncertainty relation is not evidence of nonclassicality | strong | prior results cited (Gaussian QM, odd-d stabilizer), and the qubit stabilizer theory exhibited here |
| C2 | For an A²₁-orbit-realizable state, preparation noncontextuality implies \|⟨X⟩\| + \|⟨Z⟩\| ≤ 1, and the bound is tight | strong | analytic proof and explicit saturating model, Appendix A; LP cross-check, Appendix B |
| C3 | In A²₁-symmetric theories the form of the ZX-uncertainty relation witnesses contextuality; the qubit's does | strong | C2 plus the qubit's A²₁ symmetry, shown geometrically (Fig. 3) |
| C4 | Nonclassicality grows with joint predictability, not with unpredictability | moderate | an interpretation of C2–C3 within A²₁-symmetric theories; the simplicial theory shows it fails without the symmetry |
| C5 | The three-measurement bound \|⟨X⟩\| + \|⟨Y⟩\| + \|⟨Z⟩\| ≤ 1 holds | moderate | computational verification only, Appendix C |
| C6 | Eq. 12 is noise-robust and experimentally testable | weak | asserted with references; no robustness analysis in the letter |

## Method

A noncontextuality inequality for a fixed prepare-measure scenario
(four preparations, two binary measurements, one equivalence among
mixtures), derived by hand: reduce the ontic space to the four
outcome-deterministic assignments, write each μi from μ1 and one free
parameter using the equal-predictability constraints, impose the
equivalence on the μi, and eliminate the parameters. Then reinterpret the
inequality, under a symmetry assumption, as a bound on the uncertainty
relation of a whole theory.

## Concepts

- **Predictability.** |⟨X⟩|, the absolute expectation of a ±1-valued
  binary measurement. Variance is 1 − ⟨X⟩² (Appendix D).
- **Equal-predictability counterparts.** Four states with the same
  |⟨X⟩|, |⟨Z⟩| and all four sign patterns (Eq. 10).
- **A²₁-orbit-realizability.** A state has equal-predictability
  counterparts that also satisfy ½s1 + ½s3 = ½s2 + ½s4 (Eqs. 10–11). The
  four form a rectangle parallel to the x̂ẑ-plane, the orbit of s1 under
  the reflection group of a rectangle.
- **A²₁ symmetry (of a theory).** Every state is A²₁-orbit-realizable
  relative to the chosen X and Z.
- **Foil theory.** An operational theory studied for its contrast with
  quantum theory.
- **Noncontextual (here).** Generalized noncontextuality for
  preparations, not Kochen–Specker noncontextuality.

## Connections

The definition is Spekkens's (2005, [LIT-266](../literature.d/LIT-266.md), read in [NOTE-748](NOTE-748.md)). The
eight-inequality polytope it specializes is Schmid, Spekkens and Wolfe's
(PRA 97, 062103, 2018), and the simplest scenario with a nontrivial
equivalence, four states, is Pusey's (PRA 98, 022112, 2018). Neither is
held here. The noncontextual model of the simplicial theory is cited from
Schmid et al. 2021 ([LIT-003](../literature.d/LIT-003.md)). The program it belongs to, asking which
aspects of a phenomenon resist a noncontextual model, is the one stated
in Catani, Leifer, Schmid and Spekkens ([LIT-019](../literature.d/LIT-019.md)), which the letter cites
as [6]. The octahedral state space is that of Spekkens's toy theory and
its epistemically restricted generalizations ([LIT-007](../literature.d/LIT-007.md) is one).

## Bearing on the record

- **[QUESTION-067](../questions.d/QUESTION-067.md): the filing claim is confirmed, with one precision.**
  The question's status note says the paper shows uncertainty-type
  trade-offs compatible with generalized noncontextuality. The letter
  cites that result (Gaussian QM, odd-prime stabilizer theories) and
  exhibits one more case (the qubit stabilizer theory). It proves the
  other half: the *form* of a trade-off can violate noncontextuality.
- **For [QUESTION-067](../questions.d/QUESTION-067.md)'s "What would answer it".** The question asks for
  the operational equivalences a pragmatic experiment would assume and
  the inequality they imply, separate from the sheaf criterion. This
  letter is a worked template. Four renderings with equal
  predictabilities on two binary probes and flipped signs, plus one
  equivalence of equal mixtures, give |⟨X⟩| + |⟨Z⟩| ≤ 1. The two probes
  are never made together, so in the record's own join (not the
  paper's), the measurement cover is {X}, {Z} with no overlap, and a sheaf
  or Kochen–Specker test is vacuous there. Filed as [THEORY-315](../theory.d/THEORY-315.md).
- **On [QUESTION-067](../questions.d/QUESTION-067.md)'s four conditions (note of 2026-10-14).**
  - *Exact equivalence:* still needed. Eq. 11 is used as an equality,
    and the claimed noise robustness is asserted, not shown.
  - *Perfectly distinguishable decompositions:* **not needed here.** The
    note says a pragmatic version "needs such pairs or a noise-robust
    inequality, which neither reading supplies". This letter supplies an
    inequality with no distinguishability condition; s1 and s3 can be
    any states with the orbit. The note should name it.
  - *Equivalence over every probe:* still needed. Eq. 8 quantifies over
    "all possible measurements".
- **[QUESTION-067](../questions.d/QUESTION-067.md)'s "single binary judgement".** The question's "Why the
  record needs it" says preparation contextuality "can show even with a
  single binary judgement". This letter does not say that, and its
  witness needs two binary measurements and four preparations. The
  letter's own scenario is the simplest it knows, citing Pusey. On the
  reader's argument (not the paper's), data from one binary measurement
  always admit a preparation-noncontextual model: take the two outcomes
  as ontic states and μ(+|P) = P(+|M, P), which depends on P only
  through its statistics and respects mixtures. [THEORY-231](../theory.d/THEORY-231.md) and [NOTE-737](NOTE-737.md)
  repeat the phrase as supported by [LIT-945](../literature.d/LIT-945.md), which shows only that a
  prepare-measure scenario has no Bell-like test. The phrase should read
  "two binary judgements never made together".
- **[THEORY-011](../theory.d/THEORY-011.md) and [THEORY-015](../theory.d/THEORY-015.md).** Consistent. The letter is another
  qubit-dimension preparation-contextuality proof, one that needs no
  perfectly distinguishable pairs and no Kochen–Specker structure.
- **[THEORY-016](../theory.d/THEORY-016.md).** Its noncontextual models of the stabilizer and simplicial
  theories are the ones that saturate or escape the bound. Nothing here
  extends it.
- **[THEORY-010](../theory.d/THEORY-010.md).** It says unpredictability after a change of context is
  reproduced by an epistemically restricted model. This letter agrees and
  sharpens it: the qubit stabilizer (octahedral) theory has a nontrivial
  trade-off and a noncontextual model. What resists such a model is too
  much joint predictability, given A²₁ symmetry.
- **[CLAIM-009](../claims.d/CLAIM-009.md) and [CLAIM-037](../claims.d/CLAIM-037.md).** Both are stated in the global-extension
  sense. A violation of Eq. 12 is not a failure of global extension, so
  it would not support either as worded. It would support a preparation
  version that neither states.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- **The symmetry does the work.** Outside A²₁-symmetric theories the
  bound covers only the orbit-realizable states, and a theory can have
  any trade-off at all, as the simplicial theory shows.
- **Exact equivalence.** The proof assumes Eq. 11 exactly. No
  robustness analysis is given.
- **The three-measurement bound is verified by computer**, not proved.
- **A gap left open.** The η-depolarized qubit satisfies the bound for
  η ≥ 0.293 but is cited as having a noncontextual model only for
  η ≥ 2/3. Satisfying this one inequality is necessary, not sufficient,
  and the letter does not discuss 0.293 ≤ η < 2/3.
- **Typos.** Appendix C says the depolarized qubit satisfies the
  three-measurement bound "if η ≤ 1 − 1/√3"; the geometry (radius
  1 − η, maximum √3(1 − η)) gives η ≥. Appendix A refers to "Fig. 7" for
  the saturating distributions, which are in Fig. 5.

## Open questions

- Does the bound survive inexact equivalences, and with what correction
  term? A robustness analysis in the style of Mazurek et al. would
  answer it.
- For the depolarized qubit with 0.293 ≤ η < 2/3, is there a
  noncontextual model, or another inequality that the bound misses?
- Does the axiomatic remark (A³₁ symmetry plus maximal noncontextual
  state space gives the octahedron) generalize past dimension 4?
