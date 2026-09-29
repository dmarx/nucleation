---
number: 289
status: Read
formerly:
- NOTE-tmpf2naq
paper: LIT-326
title: 'Sur une espèce de géométrie analytique des systèmes de fonctions sommables'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full note, *Comptes rendus* 144 (séance du 24 juin
    1907), pp. 1409–1411, from the Internet Archive's public-domain scan of
    the issue. It is a little over two pages of French prose, with no
    formulas displayed and no proofs. I read it in full in the original from
    the page images (the OCR layer is poor), and checked the two stated
    theorems word by word against the images. Nothing was skipped. I did not
    read the companion notes it refers to (C. R. 12 Nov. 1906, 18 Mar. and 2
    Apr. 1907; Göttinger Nachrichten 1907, p. 116), Fischer's two notes of
    13 and 27 May 1907, Fréchet's note in the same issue, or the promised
    *Mathematische Annalen* memoir.). The first NOTE on this paper, which
    was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  A priority note, not a paper of proofs. Riesz says his aim was an
  "analytic geometry" of square-summable functions, completed by his
  existence theorem (every square-summable coordinate sequence is the
  image of a square-integrable function). He states two consequences
  without proof. First, every linear operation U on square-summable
  functions that is continuous for convergence in mean is given by U(f) =
  ∫ f k for some square-summable k; uniqueness of k is not stated. Second,
  a completeness criterion for Schmidt's problem.
---

# NOTE-289: Sur une espèce de géométrie analytique des systèmes de fonctions sommables

## Contribution

The note sets down, for the record, results Riesz had announced in a Göttingen lecture on 26 February 1907 and in earlier notes, because Fischer had meanwhile published overlapping work. The programme is "to deepen the method of coordinates applied to the study of systems of summable functions" (p. 1409). A square-summable function is represented by its Fourier constants, i.e. by a point of the space of countably many dimensions whose coordinates have a convergent sum of squares. Distance between functions matches distance between points. Parseval's theorem ("the theorem on the integration of the product of two functions represented by their Fourier constants") makes the link. With Riesz's existence theorem, every such point is the image of a function. So the "synthetic" geometry of functions and the "analytic" geometry of ℓ²-points become one theory (pp. 1409–1410).

Two consequences are then stated "to fix my results" (p. 1410):

- **The representation of continuous linear functionals.** It is quoted in the key results below.
- **A completeness criterion for Schmidt's problem.** Also quoted below.

## Key insight

Once the correspondence f ↔ (Fourier coefficients) is known to be onto ℓ² (the existence theorem), function-space questions become questions about points in a space with a Euclidean distance. Continuous linear operations are then just inner products with a fixed point. The existence theorem, the Riesz–Fischer theorem, carries the weight. The functional theorem is presented as its immediate corollary.

## Assumptions

- The class is "the system of summable functions whose square is summable" (Lebesgue-integrable, square-integrable), on a domain the note does not specify.
- "Continuous operation" means a map f ↦ U(f) such that f_n → f in mean implies U(f_n) → U(f). This is sequential continuity in the L² metric.
- "Linear" means U(f₁ + f₂) = U(f₁) + U(f₂) and U(cf) = cU(f). The scalars are unspecified, and real in context.
- The Schmidt result assumes φ₁, φ₂, … continuous and the indefinite integrals of square-summable ψ₁, ψ₂, ….

## Key results

- **The existence theorem (p. 1410, stated by reference, not restated).** "Chaque point jouant un rôle dans cette géométrie analytique peut être regardé comme image d'une fonction sommable de carré sommable": every square-summable coordinate sequence is the image of some square-integrable function. This is the Riesz–Fischer theorem. Riesz says Fischer found "the particular case, relative to functions defined on an interval, of my fundamental theorem".
- **The first result (p. 1410), translated closely.** For the set of summable, square-summable functions, call a *continuous operation* any operation assigning a number U(f) to every f of the set, such that when f_n converges in mean to f, U(f_n) converges to U(f). The operation is *linear* if U(f₁ + f₂) = U(f₁) + U(f₂) and U(cf) = cU(f). "Then for every continuous linear operation there exists a function k such that the value of the operation for any function f is given by the integral of the product of the functions f and k." That k is itself square-summable is not said explicitly in the sentence, though it is implicit in the programme.
- **Its context.** Riesz says this result is "intimately linked to certain researches of MM. Hadamard and Fréchet".
- **The second result (pp. 1410–1411), Schmidt's problem.** Let φ₁(x), φ₂(x), … be continuous functions that are indefinite integrals of summable, square-summable ψ₁(x), ψ₂(x), …. For every function f(x) to be representable by a uniformly convergent series whose terms are linear combinations of 1, φ₁(x), φ₂(x), …, "it suffices that there be no summable, square-summable function orthogonal at once to every function ψ(x)". Note that this is stated as a sufficient condition, and "every function f(x)" is not qualified in the note.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Every square-summable coordinate sequence is the image of a square-integrable function (the existence theorem) | assertion here | Proof deferred to earlier notes and the promised Annalen memoir; only referred to on p. 1410 |
| C2 | Every linear operation continuous for convergence in mean on square-integrable functions equals f ↦ ∫ f k for some function k | assertion | p. 1410, called an "immediate consequence" of C1; no argument, and no uniqueness or norm statement |
| C3 | Absence of a nonzero square-summable function orthogonal to all ψ_i suffices for uniform approximation of every f by linear combinations of 1, φ₁, φ₂, … | assertion | pp. 1410–1411; no argument |
| C4 | Fischer's "convergence in mean" reduces to Riesz's notion of limit function (C. R., 12 Nov. 1906), and Fischer's theorem is the interval case of Riesz's | assertion (priority claim) | p. 1410 |

## Concepts

- **Géométrie analytique / synthétique.** The "analytic" geometry is the geometry of ℓ²-coordinate points. The "synthetic" one is the geometry of functions under the L² distance (Fischer's approach).
- **Opération continue, linéaire.** A continuous linear functional in modern terms.
- **Convergence en moyenne.** L² convergence.

## Connections

- **[LIT-230](../literature.d/LIT-230.md) and [LIT-243](../literature.d/LIT-243.md).** These are the record's secondary accounts of the Riesz representation theorem, and they are what one should cite for its modern Hilbert-space form (uniqueness, isometry, arbitrary Hilbert spaces). This note is the first statement on L² only, with none of that.
- **Fréchet (not registered).** His note in the same issue (C. R. 144:1414–1416) is the simultaneous statement. The Riesz–Fréchet naming reflects this.
- **[THEORY-003](../theory.d/THEORY-003.md) and [THEORY-009](../theory.d/THEORY-009.md).** Those use and question "Riesz" in the RKHS/kernel-mean-embedding sense. That is the Hilbert-space generalisation, not what this note states. Nothing here bears on [THEORY-009](../theory.d/THEORY-009.md)'s point that spectral SSL gets self-adjointness from symmetry, not from Riesz.

## Bearing on the record

- **Map row 10 / R2, "Riesz-forced unique factorization".** The note does not supply this. It gives existence of a representing function k for a continuous linear functional on L², stated without proof. It says nothing about uniqueness, factorisation, low rank or convergence of representations. So the map's phrase cannot be sourced to this paper. Any "unique factorization" argument must bring its own uniqueness, e.g. uniqueness of the Riesz representer in a Hilbert space (from [LIT-243](../literature.d/LIT-243.md)), or the up-to-orthogonal-transformation uniqueness of [THEORY-004](../theory.d/THEORY-004.md). It also needs its own route from there to representations, which is where the map already flags overreach (R2).
- **Primary versus secondary.** If the owner's docs "already cite Riesz", [LIT-243](../literature.d/LIT-243.md) or a textbook is the better citation for any property used. This note is worth citing only for priority, alongside Fréchet's same-issue note.
- **ML practice.** It carries nothing, and does not belong in the Anthology.
- **For filing.** Keep `mathematics` alone. `probabilistic-modeling` or `representation-learning` would tag why the record wanted it, not what it is about.

## Limitations

- **No proofs at all.** Both results are asserted as consequences of a theorem proved elsewhere.
- **Uniqueness is not stated.** Neither is the fact that k is square-integrable, the norm identity, or complex scalars.
- **The domain is unspecified,** and the Schmidt result's "every function f(x)" is unqualified.

## Open questions

- Does the Annalen memoir promised here (Riesz, "Untersuchungen über Systeme integrierbarer Funktionen", Math. Ann. 69, 1910, if that is the one — unverified) contain the proof and uniqueness? That memoir, or Fréchet's same-issue note, would be the better primary if the owner wants one.

## Corrections to the seeded skim

- Seeded from metadata; the text shows the summary is right in substance but overstates it in two ways. (1) Nothing is "shown": the note states the functional-representation result as an immediate consequence of the author's existence theorem and gives no argument. (2) It says only that a function k exists ("il existe une fonction k"). Uniqueness of k, the norm identity ‖U‖ = ‖k‖, and any Hilbert-space language are not in the note.
- The title as printed capitalises "Géométrie": "Sur une espèce de Géométrie analytique des systèmes de fonctions sommables". The author is printed "M. Frédéric Riesz", and the note was presented by Émile Picard. Pages 1409–1411 are confirmed from the scan.
- The note's framing is a priority dispute. Riesz writes that Fischer's notes of 13 and 27 May "force me to change my plan" of publishing only in the Annalen memoir. Fischer, he says, developed the "synthetic" theory and rediscovered the interval special case of Riesz's fundamental theorem. Riesz also says Fischer's convergence in mean reduces to Riesz's own notion of limit function from his note of 12 Nov. 1906.
- The domain of the functions is never specified in this note. The remark that Fischer's case is "relative to functions defined on an interval" implies that Riesz's own statement is more general, but the note does not say how.
