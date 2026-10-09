---
number: 236
status: Read
formerly:
- NOTE-tmphk2j0
paper: LIT-265
title: 'Abramsky, Barbosa & Mansfield, contextual fraction'
version: 2
history:
- version: 2
  date: '2026-10-09'
  note: >-
    Read in full from arXiv 1705.07918v1 (22 May 2017, 18 pages),
    extracted with pdftotext. The Letter was read throughout, and so was
    the supplemental material: A (proof of Theorem 1 by LP duality), B
    (computational explorations, Tables II–III, Proposition 4 with
    proof), C (proof of Theorem 2, including Lemmas 5–6 on gluing
    subprobability distributions), D (l2-MBQC definitions and proof of
    Theorem 3) and E (constraint systems, Theorem 4). Every proof was
    followed. Lemma 5's interval construction was checked step by step;
    its displayed sums were partly scrambled in extraction and were
    followed from the definitions. The plots of Fig. 1 were not seen.
    The reader re-ran the LP (3) on the CHSH scenario (scipy linprog):
    the Table I Bell–CHSH model gives CF = 1/4, its normalised CHSH
    violation, and the PR box gives CF = 1. The PRL text was not
    compared. Upgraded from `Skimmed` to `Read`: the assumptions, results,
    claims table and bearing are new, and the skim's bullets are kept in
    substance under Key results.
date: '2026-10-09'
summary: >-
  For any no-signalling empirical model, the contextual fraction CF (one
  minus the largest weight of a noncontextual sub-model) is a linear
  programme. Its dual gives a Bell inequality whose normalised violation
  equals CF, and no Bell inequality is violated more (Theorem 1). CF is
  invariant under relabelling, non-increasing under translation of
  measurements, coarse-graining and mixing, and NCF is multiplicative
  under products (Theorem 2). It lower-bounds the failure probability of
  Z2-linear MBQC (Theorem 3) and of k-consistent games (Theorem 4).
---

<!-- inactive-ok-file: THEORY-tmp8ly9g THEORY-tmpjdnxt THEORY-014 — Proposed; filed from or bearing on this reading -->

# NOTE-236: Abramsky, Barbosa & Mansfield, contextual fraction

## Contribution

LIT-016 had the non-contextual fraction only at its extreme value: zero
non-contextual fraction is strong contextuality. This paper makes the
fraction a graded measure for any scenario. It shows that the measure is a
linear programme, that it equals the best normalised Bell-inequality
violation (with the inequality computed by the dual), that it behaves as a
monotone under a set of operations that cannot create contextuality, and
that it bounds quantum computational advantage in two settings.

## Key insight

Ask what fraction of the data a noncontextual model can explain from below:
the heaviest subprobability on global assignments that fits under every
context's distribution. That is a linear programme with the data on the
right-hand side, and LP duality turns it into the statement that the
unexplained remainder is exactly how far the data violate the best Bell
inequality. One number therefore does three jobs: a decomposition weight, a
violation, and a resource.

## Assumptions

- A finite measurement scenario ⟨X, M, O⟩: finite measurements, finite
  outcomes, maximal contexts M covering X.
- Empirical models with compatible marginals: e_C|_{C∩C′} = e_{C′}|_{C∩C′}
  ("a generalisation of the usual no-signalling condition"). Data with
  context-dependent marginals are not empirical models, and CF is
  undefined for them.
- Bell inequalities ⟨a, R⟩ with R < ‖a‖ (the algebraic bound), so the
  normalisation is defined.
- For Theorem 3: (n, 2, 2) resources, Z2-linear pre- and post-processing
  and a strictly lower-triangular flow matrix. For Theorem 4: uniformly
  random formulae.

## Key results

- **Eq. (1)–(2).** NCF(e) = max λ over e = λe^NC + (1 − λ)e′. Every model
  decomposes as NCF·e^NC + CF·e^SC with e^SC strongly contextual (credited
  to LIT-016), not uniquely. The supplement's Table II gives two
  decompositions of one model with CF = ½ in the (3,2,2) scenario.
  Uniqueness holds when the no-signalling polytope has no face made only
  of strongly contextual vertices, as in (2,2,2).
- **LP (3) and dual (4).** NCF = max 1·b subject to Mb ≤ v_e, b ≥ 0. Dual:
  min y·v_e subject to Mᵀy ≥ 1, y ≥ 0. Strong duality applies, because
  the primal is feasible (b = 0) and bounded.
- **Theorem 1.** (i) Every Bell inequality's normalised violation
  max{0, a·v_e − R}/(‖a‖ − R) is at most CF(e). The proof splits e into
  NCF·e^NC + CF·e^SC and bounds each part. (ii) If CF(e) > 0, then
  a* = |M|⁻¹1 − y* with bound 0 is a Bell inequality with algebraic bound
  1, violated by exactly CF(e). The change of variables makes the dual
  equivalent to max a·v_e subject to Mᵀa ≤ 0, a ≤ |M|⁻¹1. (iii) In any
  optimal decomposition, that inequality is tight at e^NC and maximally
  violated at e^SC.
- **Theorem 2.** CF is invariant under relabelling. It is non-increasing
  under translation of measurements (pulling e back along a
  context-preserving f: X → X′, which includes restriction) and under
  coarse-graining of outcomes. NCF(λe₁ + (1 − λ)e₂) ≥ λNCF(e₁) +
  (1 − λ)NCF(e₂); the printed CF form has a typo. CF(e & e′) =
  max{CF(e), CF(e′)}, using Lemmas 5–6, which glue two subprobabilities of
  equal weight into a joint one. NCF(e ⊗ e′) = NCF(e)·NCF(e′), by product
  primal and product dual solutions.
- **Theorem 3.** For an l2-MBQC ⟨K, e⟩ computing f: 2^m → 2^l,
  p̄_F ≥ NCF(e)·ν̃(f). Proof: split e. Each deterministic noncontextual
  part computes a Z2-linear function (Raussendorf), so it fails on at
  least a ν̃(f) fraction of inputs.
- **Theorem 4.** For a k-consistent set of n formulae and a valid strategy
  p, p_F ≥ NCF(p)·(n − k)/n, from Theorem 1 and Abramsky–Hardy's logical
  Bell inequalities.
- **Proposition 4.** Equatorial measurements at (φ₁, φ₂) =
  ((n + k)π/2n, kπ/2n), 0 ≤ k < n, on GHZ(n) give Mermin's strongly
  contextual model up to relabelling.
- **Computational findings** (supplement B). On |Φ⁺⟩ with two equatorial
  settings per qubit, CF depends on the absolute angles, not only on their
  difference. Its maxima are the Tsirelson-violating models, none strongly
  contextual. On GHZ(3) and GHZ(4), CF = 1 at the angles of Proposition 4.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | CF(e) equals the largest normalised violation of any Bell inequality by e, attained by an inequality computed from the dual LP | strong (proof) | Theorem 1, supplement A |
| C2 | CF is invariant under relabelling and non-increasing under translation of measurements and coarse-graining of outcomes | strong (proof) | Theorem 2, supplement C |
| C3 | CF is convex under mixing, max under choice, and NCF is multiplicative under product | strong (proof) | Theorem 2, supplement C, Lemmas 5–6 |
| C4 | The noncontextual / strongly contextual decomposition is not unique in general | strong (example) | Table II |
| C5 | Z2-linear MBQC failure probability is at least NCF·ν̃(f) | strong (proof, relying on Raussendorf's linearity lemma) | Theorem 3, supplement D |
| C6 | k-consistent games: failure at least NCF·(n − k)/n | strong (proof via Abramsky–Hardy) | Theorem 4 |
| C7 | CF allows meaningful comparison across scenarios | moderate (normalisation to [0, 1] and C1, not a theorem about maps between scenarios) | Introduction |

## Method

Everything is linear programming over the incidence matrix M, whose columns
are the deterministic noncontextual models. The primal finds the heaviest
noncontextual subprobability under the data. The dual, after a change of
variables, finds the most-violated normalised Bell inequality. The
monotonicity proofs transport an optimal primal solution, or for products
also an optimal dual one, along each operation.

## Concepts

- **empirical model.** A family of distributions e_C on O^C, one per
  maximal context, with compatible marginals.
- **non-contextual / contextual fraction.** NCF(e) is the largest weight of
  a subprobability b on O^X with b|_C ≤ e_C. CF = 1 − NCF.
- **normalised violation.** max{0, a·v_e − R}/(‖a‖ − R), where ‖a‖ is the
  sum over contexts of the largest coefficient.
- **free operations.** Relabelling, translation of measurements,
  coarse-graining, mixing, controlled choice (&) and product (⊗), named
  as the start of a resource theory to be given elsewhere.
- **ν̃(f).** The average Hamming-style distance from f to the nearest
  Z2-linear function.

## Connections

It is built on LIT-016's framework, and the decomposition into a strongly
contextual part is from there. It generalises the Elitzur–Popescu–Rohrlich
local fraction from Bell scenarios to all scenarios. Theorem 3 sharpens
Raussendorf (2013); Theorem 4 uses Abramsky and Hardy's logical Bell
inequalities. Its note 33 lists negative-probability measures (LIT-016),
Contextuality-by-Default measures and noise and inefficiency measures as
alternatives whose relation to CF is left for later.

## Bearing on the record

- **THEORY-012.** The theory says the graded version of its criterion is
  this paper's. The reading confirms it: CF = 0 exactly when the
  global-section criterion holds, and the LP is the relaxation of
  LIT-016's linear system. The inactive-ok directives citing LIT-265 as
  Deferred, in THEORY-012, LIT-777, NOTE-600 and CLAIM-tmpukbg3, are now
  stale.
- **THEORY-014.** The negative-probability measure appears only in note
  33. The paper's measure is the nonnegative side of that theory's
  pattern, the largest nonnegative part, rather than the least negative
  completion. It adds no instance and does not contradict it.
- **THEORY-tmp8ly9g** is filed from this reading. Its convexity is
  Theorem 2. Its piecewise linearity and Lipschitz continuity in v_e are
  the reader's derivation from LP (3)–(4): NCF(e) = min over the finitely
  many vertices y_k of the dual polyhedron of y_k·v_e.
- **THEORY-tmpjdnxt.** CF's non-increase under coarse-graining (C2)
  contrasts with Contextuality-by-Default, where coarse-graining a
  non-binary system can create contextuality (LIT-tmpsa1qj, Example 3).
  That theory states the contrast.
- **The manuscript (CLAIM-tmpukbg3, Δ_CF).** Three bearings, for the
  coordinator:
  (1) Δ_CF is defined only when both models in a step have compatible
  marginals. A reconstruction that introduces context-dependent marginals
  leaves CF undefined.
  (2) By Theorem 2, a step that is a free operation (relabelling,
  restriction or translation of measurements, coarse-graining of outcomes,
  mixing with a noncontextual model) cannot increase CF. Along such steps,
  Δ_CF ≤ 0, and an increase in contextuality needs a step outside the free
  operations. This supports "local meanings preserved, global structure
  changed" in the decreasing direction and constrains the increasing one.
  (3) The claim's quoted premise that CF is "a discontinuous contextuality
  measure" is not borne out within a scenario. CF is continuous, indeed
  Lipschitz, in the probability table (THEORY-tmp8ly9g, the reader's
  derivation). A drift bound on every context's distribution therefore
  bounds |Δ_CF| within a fixed scenario. What may jump is a change of
  scenario (cover), which is not a perturbation of the table.
- No instruction for machine-learning practice. Theorem 3 concerns
  quantum computation, not ML.

## Limitations

- Defined only for no-signalling (compatible-marginal) models.
- The resource theory is announced, not given. "Free operations" are a
  list, not a characterization.
- C7, comparison across scenarios, is motivated by normalisation, not
  proved for any map between scenarios beyond translations.
- Theorem 3 holds only for Z2-linear classical control and (n, 2, 2)
  resources.
- The decomposition is not unique, so e^NC and e^SC are not invariants of
  the model.

## Open questions

- The relation between CF and Contextuality-by-Default's total-variation
  measure (LIT-777) on consistently connected systems, which the paper
  defers. On those systems both are LPs over closely related polytopes,
  and whether they order models the same way is not known to the record.
- An explicit Lipschitz constant for CF in a given scenario, the largest
  ‖y‖₁ over dual vertices. A bound would turn drift bounds on context
  distributions into bounds on Δ_CF.
