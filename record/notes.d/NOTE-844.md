---
number: 844
status: Read
formerly:
- NOTE-tmpmru91
paper: LIT-263
title: 'Budroni, Cabello, Gühne, Kleinmann & Larsson — Kochen-Specker Contextuality'
version: 1
history:
- version: 1
  date: '2026-10-14'
  note: >-
    Read from the arXiv PDF (2102.13036v5, dated 10 January 2023, 68
    pages), text extracted with pdftotext in reading-order and layout
    modes. Every section of the body was read, §§I–VII and Appendix A,
    with the figure and table captions. The reference list was consulted
    only to identify cited works. The passages the record's theories cite
    were read closely and their arguments checked: §III.A, §IV.A.1–5,
    §IV.B.2–3, §IV.C.5, §IV.E.1–4, §V.B.2 and §V.F.2. The rest was read
    once, at ordinary pace: the graph-theoretic §V.B.3–5, the simulation
    and resource-theory §V.D–E, and the applications in §VI. The figures
    are diagrams and plots and were read from their captions. The RMP
    version (94, 045007) was not compared. Replaces the seeded skim
    NOTE-237.
date: '2026-10-14'
summary: >-
  A review of Kochen–Specker contextuality. It defines noncontextual
  hidden-variable models minimally, as a global distribution whose
  marginals are the context distributions (Fine's theorem), with the
  sheaf, polytope, graph and hypergraph formulations called substantially
  equivalent. It argues that contexts need an operational definition
  stronger than joint measurability, which alone makes every
  nondisturbing correlation classically realizable. It surveys how
  disturbance is modelled in experiments, Kujala et al.'s maximally
  noncontextual models among them. Spekkens's generalized contextuality
  is covered only to mark the difference, and the review nowhere derives
  the relation between the two notions.
---
<!-- inactive-ok-file: THEORY-013 THEORY-174 THEORY-303 NOTE-237 — Proposed or Superseded; accounts this reading bears on, an account filed from it, and the skim it replaces -->

# NOTE-844: Budroni, Cabello, Gühne, Kleinmann & Larsson — Kochen-Specker Contextuality

## Contribution

A Reviews of Modern Physics survey of Kochen–Specker (KS) contextuality.
Most of it is synthesis, with three things of its own:

- a declared "minimal" mathematical structure for noncontextual
  hidden-variable (NCHV) models, the marginal problem;
- an argued operational definition of contexts for experiments, by
  sequences of outcome-repeatable, nondisturbing measurements, in
  place of joint measurability;
- a taxonomy of how experimental imperfections are modelled.

It proves few results of its own. Its arguments either adapt known
constructions (Fritz's one-dimensional joint measurements, §IV.B.2) or
restate cited proofs (KS sets, KCBS, Yu–Oh, Spekkens's qubit argument,
Mazurek et al.'s inequality).

## Key insight

KS contextuality is a marginal problem. Data from overlapping contexts
are noncontextual exactly when one joint distribution over all
observables reproduces them. Everything physical lies in what may count
as a context. Too weak a notion, joint measurability alone, makes
contextuality trivial. So the review ties contexts to ideal measurements
(repeatable, nondisturbing, as commuting projectors are), and models the
failure of ideality explicitly. Spekkens's notion moves the
noncontextuality assumption from outcomes to operational equivalence
classes. It is a different notion, and the review keeps it apart.

## Assumptions

- **Finite scenarios** throughout §IV.A and §V.A. Continuous variables
  are mentioned only (§V.A.3).
- **NCHV model (Eq. 15).** p_C({a_i}) = Σ_λ p(λ)Π_{i∈C} p(a_i|λ), the
  response functions independent of context. Local consistency of the
  marginals (Eq. 14) is "necessary but not sufficient" for a global
  distribution.
- **Ideal measurements** for KS contextuality (§II.B, §IV.B, App. A.5):
  outcome repeatability and nondisturbance, equivalent to commutativity
  for projective measurements (Heinosaari & Wolf).
- **Experimental analyses** need extra assumptions on the noise model:
  cumulative noise (§IV.C.1), context-independent evolution (§IV.C.2),
  ε-ontological faithfulness (§IV.C.3–4), maximal noncontextuality
  (§IV.C.5). "there is no general recipe that can be applied to all
  experiments" (§IV.C).
- **Spekkens's notion (§IV.E)**: prepare-and-measure scenarios only, and
  tomographic completeness of the sets used to infer operational
  equivalence (§IV.E.3).

## Key results

- **KS sets (§III.A).**
  - A KS set in dimension d admits no f: S → {0,1} with Σ_{ψ∈B} f(ψ) = 1
    for every orthogonal basis B ⊂ S.
  - "there is no KS set for d = 2", since noncontextual assignments exist
    for all projectors in C² (citing Kochen & Specker).
  - KS's method extends to every d > 3 (Cabello & García-Alcaine 1996).
  - The smallest set by vectors is Cabello et al.'s 18 vectors in d = 4,
    minimal per Xu et al. 2020. The smallest by contexts is Lisoněk et
    al.'s 21 vectors, 7 contexts, d = 6.
  - The Peres–Mermin square (Eqs. 1–10) and Mermin's pentagram are KS
    proofs by parity.
  - Yu–Oh's 13 vectors (Fig. 7) admit {0,1} assignments yet give
    state-independent contextuality: their noncontextual bound is 8
    (Eq. 19), and the quantum value is 25/3 for every state (Eqs. 20–21).
- **NCHV models and Fine's theorem (§IV.A.1, Eqs. 14–16).**
  - Formulations "despite their substantial equivalence" include the
    marginal problem, the polytope, "the sheaf-theoretical approach
    (Abramsky and Brandenburger, 2011)", the graph approach and the
    hypergraph approach.
  - Local consistency "is sometimes called the sheaf condition". It is
    no-signalling in Bell scenarios and "nondisturbance" in general.
  - Eq. 15 is equivalent to a global distribution p_G whose marginals
    are the p_C (Eq. 16). This is "known in the literature as Fine's
    theorem". Fine stated it only for CHSH. A complete proof is a
    corollary of Suppes & Zanotti 1981, and a proof "in the language of
    contextuality" appeared with Abramsky & Brandenburger 2011.
  - The review sketches the argument without proving it: stochastic
    response functions become deterministic ones of an enlarged hidden
    variable, because every probability measure on a finite set is a
    mixture of {0,1}-valued ones.
- **KCBS (§IV.A.2).** ⟨A₀A₁⟩ + … + ⟨A₄A₀⟩ ≥ −3 for NCHV. A qutrit reaches
  5 − 4√5 ≈ −3.94. The minimal dimension is 3. Vorob'ev's theorem makes
  cycles of length > 3 necessary. The n-cycle inequalities are tight for
  n ≥ 5 (Araújo et al. 2013).
- **Logical and strong contextuality (§IV.A.4).**
  - Possibilistic contextuality implies probabilistic contextuality (A&B
    Prop. 4.4).
  - Strong contextuality means no deterministic assignment consistent
    with the support. The PR box and GHZ/all-versus-nothing arguments
    are examples.
  - p = αp_NC + (1 − α)p_ND (Eq. 22), the maximal α being the noncontextual
    fraction. "a probabilistic model is strongly contextual if and only if
    it is maximally contextual" (A&B 2011).
  - Topological and cohomological follow-ups are named only, in one
    sentence.
- **Exclusivity and completeness (§IV.A.5, Eqs. 23–26).** An inequality
  derived under the extra exclusivity assumption becomes a general NCHV
  inequality once correlation penalty terms are added. For KCBS, Eq. 25
  becomes Eq. 26, with the bound 2 and the quantum value unchanged.
- **Contexts by joint measurability alone are trivial (§IV.B.2, Eqs.
  27–28).** Adapting Fritz (2012): given any nonsignalling p(ab|xy), set
  G^{xy}_{ab} := p(ab|xy)𝟙, A^x_a := Σ_b G^{xy}_{ab}, B^y_b := Σ_a G^{xy}_{ab}
  on a one-dimensional Hilbert space. Each pair is jointly measurable,
  and the correlations are reproduced. "by defining contexts simply in
  terms of joint measurability, all maximally contextual correlations
  … can be reached using one-dimensional (and hence classical
  simulable) quantum systems". I checked the construction, and it
  extends to any scenario with nondisturbing data. Liang et al. 2011
  avoid the triviality with a sharpness parameter.
- **Operational contexts (§IV.B.2, steps S.1–S.5).** Contexts are
  sequences of outcome-repeatable, statistically nondisturbing
  measurements, each repeated identically in every context, and
  deviations from ideality are measured.
- **Effect perspective and Spekkens (§IV.B.3, Eqs. 29–30).**
  - Effects are identified by equal statistics for all preparations.
  - If statistically identical effects must have identical response
    functions, then response functions of unsharp measurements cannot be
    made deterministic (Spekkens 2014). The reason: an unsharp effect is
    statistically identical to a post-processing of its spectral
    projective measurement.
- **Modelling imperfections (§IV.C).**
  - *Cumulative noise (Eqs. 31–41).*
    ⟨A₁B₂⟩ − 2p_flip ≤ ⟨AB⟩ ≤ ⟨A₁B₂⟩ + 2p_flip, and under the cumulative-noise
    assumption p_flip[AB] ≤ p_err[BAB]. This gives a testable CHSH-type
    inequality. Kirchmair et al. found 2.23(5) > 2.
  - *Evolving hidden variables (Eqs. 42–45).* A sequential CHSH can be
    violated to 4 unless each observable keeps its position in the
    sequence.
  - *Larsson's ε-bounds (Eq. 48, Table I).* Mε + Nε′ ≥ 1.
  - *Winter's ε-ONC bound (Eqs. 50–53).* The review notes that there is
    "no direct connection" between operator-norm imprecision and the
    ε of an ontological model.
  - *Maximally noncontextual models (§IV.C.5, Eqs. 54–55).* Kujala,
    Dzhafarov & Larsson (2015) give each observable a variable per
    context and require variables in different contexts to "be equal to
    each other with the maximum probability allowed by the observed
    marginals". For cyclic systems this gives Eq. 55, a KCBS expression
    minus Σ|⟨A_i^{(i)}⟩ − ⟨A_i^{(i−1)}⟩|, bounded by 3.
  - On Lapkiewicz et al.'s data, the 99.99999999% interval for the
    left-hand side of Eq. 55 is [3.127, 4.062], a violation. The review
    presents the model as one assumption about disturbance among
    several, "reasonable … if the noise is supposed to arise from some
    clumsiness of the measurements". It does not use the name
    Contextuality-by-Default, and it does not discuss behavioural data.
- **Experiments (§IV.D).**
  - Peres–Mermin with ions: ⟨PM⟩ = 5.46 ± 0.04 > 4, state-independent
    across ten states.
  - Peres–Mermin with photons: 5.4550 ± 0.0006.
  - KCBS with photons: −3.893 ± 0.006 against a corrected bound of
    −3.081.
  - The review groups experiments as sequential, joint, or with
    measurements implemented differently per context.
- **Spekkens's approach (§IV.E).**
  - *Definitions.* Operational equivalence of preparations and of
    measurement effects (Eqs. 64–65); ontological model (Eq. 66).
    Preparation noncontextuality is µ_P = µ_P′ for P ∼ P′, and
    measurement noncontextuality is ξ_{M,k} = ξ_{M′,k′}.
  - *Qubit proof (Eqs. 67–70).* Six pure states give five decompositions
    of 𝟙/2. Orthogonal pairs must have disjoint supports, so all six
    distributions vanish. Banik et al. extend this to any mixed state.
  - *Mazurek et al.'s inequality (Eqs. 71–74).* A ≤ 5/6. "the
    derivation of Eq. (73) uses both preparation noncontextuality …
    and measurement noncontextuality …. In fact, the inequality can be
    violated by models that violate at least one of the constraints."
    Quantum theory reaches 1.
  - *The experiment (§IV.E.3).* A = 0.99709 ± 0.00007. It is computed on
    secondary preparations and measurements, inferred within a GPT that
    assumes three measurements and four preparations are tomographically
    complete.
  - *Hidden-variable models (§IV.E.4).* Bell's and Kochen & Specker's
    qubit models are preparation contextual (Leifer & Maroney 2013). The
    definition is defended by "Leibniz's principle of the ontological
    identity of empirical indiscernibles", cited to Spekkens 2019, with
    the 2005 paper for its use as motivation.
- **Polytope and LP (§V.A).** The noncontextuality polytope is the
  projection of the simplex of global assignments onto the observed
  marginals. Membership is an LP, whose dual yields a violated
  inequality. The contextual fraction is an LP. Entropic inequalities
  are only necessary conditions.
- **Vorob'ev (§V.B.2).** "Any marginal scenario represented by an acyclic
  hypergraph admits a joint probability distribution". The text adds
  that the given marginals must coincide on intersections. Acyclicity is
  the running-intersection property, equivalently the clique hypergraph
  of a chordal graph. The theorem is stated and cited (Vorob'ev 1962;
  Kellerer 1964; Malvestuto 1988), and illustrated by gluing on a path
  A − B − C (Eq. 79), which is Fine's construction. For sharp
  measurements, compatibility graphs suffice (Specker's principle), so a
  chordal compatibility graph admits an NCHV model. The smallest
  contextual scenarios are the square (CHSH, needs d = 4) and the
  pentagon (KCBS, d = 3). App. A.6 restates this as an induced cycle of
  size > 3.
- **Graphs (§V.B.3–5).**
  - Classical, quantum and "consistent exclusivity" bounds for an
    exclusivity graph G are α(G), ϑ(G) and α*(G).
  - For ideal measurements the quantum set of probabilities is
    P(G) = TH(G) (Cabello et al. 2014).
  - χ_f(G) > d and χ(G) > d are necessary for state-independent
    contextuality with rank-1 projectors.
  - Yu–Oh is the minimal SI-C set in any dimension (Cabello et al.
    2016b). §VII nonetheless calls the smallest SI-C *scenario* unknown.
- **KS and Bell (§V.C, §IV.B.2, §V.F.2).** "Bell nonlocality can be
  considered a particular form of contextuality where the assumption of
  context-independence is identified with the locality assumption." In
  the probabilistic framework Bell nonlocality "can be seen as an special
  case of contextuality". The original KS and Bell notions are
  "logically independent" (Barrett & Kent). A maximally entangled state
  turns a state-independent contextuality inequality into a Bell
  inequality (Eqs. 91–94).
- **Simulation and resources (§V.D–E).**
  - Peres–Mermin needs a three-state Mealy machine for ⟨PM⟩ = 6, and
    four states for all its compatibilities. ε-transducers need
    log 24 ≈ 4.585 bits.
  - The full stabilizer subtheory, contextual behaviour included, has an
    efficient (quadratic) contextual hidden-variable simulation
    (Hindlycke & Larsson 2022).
  - The contextual fraction is a monotone under noncontextual wirings
    and Abramsky et al.'s operations. There is no catalysis.
- **Nullification debate (§V.F).** Meyer and Kent's KS-colourable dense
  rational sets fail to reproduce the quantum statistics: κ = 3.941 > 3
  on a KCBS configuration with rational vectors (Eqs. 100–104). Clifton &
  Kent's all-incompatible dense sets are recast as imperfect
  compatibility, handled as in §IV.C.
- **Applications (§VI).**
  - *Magic states.* For odd prime d, a state is contextual with respect
    to stabilizer measurements iff it lies outside the polytope of
    efficiently simulable states, i.e. iff its discrete Wigner function
    is negative (Howard et al. 2014; Eqs. 105–108; Delfosse et al. 2017
    for n > 1). This makes contextuality necessary for universal
    computation by magic-state distillation. Rebits and qubits were
    treated later.
  - *Shallow circuits.* Bravyi et al.'s constant-depth separation is
    read as a cost of simulating contextuality.
  - *QKD.* Svozil's KS-based protocol, and Horodecki et al.'s
    device-independent key from a distributed Peres–Mermin box.
  - *Randomness.* Abbott et al.'s value indefiniteness.
  - *Further.* Zero-error capacity with entanglement from KS sets,
    dimension witnesses, self-testing, and parity-oblivious multiplexing
    and state discrimination from preparation contextuality.
- **Outlook (§VII) and history (App. A).** The loophole analysis of
  contextuality has not reached that of Bell tests, and the smallest
  SI-C scenario is unproved. App. A.4 traces Spekkens 2005 to the
  Meyer–Kent debate. App. A.5 defines "KS contextuality" as outcome
  noncontextuality for ideal measurements, theory-independently.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An NCHV model (Eq. 15) exists iff a global distribution has the context distributions as marginals | strong | Fine / Suppes–Zanotti, cited with a sketch, §IV.A.1 |
| C2 | The marginal-problem, polytope, sheaf, graph and hypergraph formulations are substantially equivalent | moderate | asserted with citations, §IV.A.1; not shown |
| C3 | Contexts defined by joint measurability alone make every nondisturbing correlation realizable with one-dimensional quantum systems | strong | explicit construction, Eqs. 27–28, adapted from Fritz 2012 |
| C4 | A marginal scenario with an acyclic hypergraph and consistent marginals always admits a joint distribution | strong | Vorob'ev 1962, cited and illustrated (Eq. 79), not proved here |
| C5 | No KS set exists in dimension 2; KS sets exist in every d ≥ 3 | strong | cited, §III.A |
| C6 | Strong contextuality is equivalent to a noncontextual fraction of zero | strong | cited to A&B 2011, §IV.A.4 |
| C7 | Under measurement noncontextuality, unsharp response functions cannot be made deterministic | moderate | sketch of Spekkens 2014's proof, §IV.B.3 |
| C8 | A qubit admits no preparation-noncontextual model | strong | restated proof, Eqs. 67–70 |
| C9 | Mazurek et al.'s data violate the joint preparation-and-measurement noncontextuality bound 5/6 | moderate | experiment, §IV.E.3, assuming tomographic completeness and using secondary procedures |
| C10 | KCBS data remain contextual under Kujala et al.'s maximally noncontextual models | moderate | a cited reanalysis, §IV.C.5 |
| C11 | For odd prime d, stabilizer-measurement contextuality of a state coincides with negativity of its discrete Wigner function | strong | Howard et al. 2014, summarized, §VI.A.1 |

## Concepts

- **Marginal scenario** — a family of contexts M ⊂ 2^G over observables
  G.
- **Nondisturbance** — local consistency of context marginals (Eq. 14),
  i.e. no-signalling in Bell scenarios. Also "the sheaf condition".
- **OP / EP** — the observable and effect perspectives: a context as a
  set of compatible observables, or as a single measurement whose
  effects are identified across measurements.
- **Ideal (sharp) measurement** — repeatable and nondisturbing of every
  compatible measurement, with coarse-grainings ideal too (§V.B.4).
- **Maximally noncontextual model** — per-context copies of each
  observable, coupled to agree as often as their marginals allow
  (§IV.C.5).
- **Exclusivity graph** — events as vertices, edges between events
  that some measurement distinguishes, i.e. the same setting with
  different outcomes.
- **Noncontextual fraction** — the largest α in p = αp_NC + (1 − α)p_ND.

## Connections

The review places Abramsky & Brandenburger's sheaf formulation ([LIT-016](../literature.d/LIT-016.md))
among equivalent formulations, and attributes logical and strong
contextuality and the noncontextual fraction to it. The contextual
fraction LP ([LIT-265](../literature.d/LIT-265.md)) appears in §IV.A.4 and §V.A.3. Spekkens 2005
([LIT-266](../literature.d/LIT-266.md)) is restated in §IV.E. The Leibnizian defence is cited to
Spekkens 2019, a different paper from [LIT-945](../literature.d/LIT-945.md). Kochen & Specker 1967
([LIT-298](../literature.d/LIT-298.md)) is the primary source of §III.A. Kujala, Dzhafarov & Larsson
2015, cited in §IV.C.5, is the physics application of the criterion that
Dzhafarov, Zhang & Kujala apply to behavioural data ([LIT-264](../literature.d/LIT-264.md)). The
review does not discuss the cohomological witnesses ([LIT-277](../literature.d/LIT-277.md)) beyond
naming the topological follow-ups.

## Bearing on the record

- **[THEORY-011](../theory.d/THEORY-011.md) cites §IV.E.1–4, correctly, with one overreach.**
  - Confirmed: the six-state restatement (Eqs. 67–70); Bell's and KS's
    qubit models being preparation contextual (§IV.E.4); tomographic
    completeness assumed in the experiment (§IV.E.3); and "no KS set for
    d = 2" (§III.A; App. A.6).
  - The overreach: [THEORY-011](../theory.d/THEORY-011.md) cites "an experiment reporting a violation
    of the noncontextual bound" beside a claim about *preparation*
    noncontextuality. The review says the Mazurek et al. inequality is
    derived from preparation *and* measurement noncontextuality, and can
    be violated by models that keep either one. The experiment refutes
    their conjunction, universal noncontextuality, not preparation
    noncontextuality alone. It also rests on secondary procedures
    inferred in a GPT that assumes tomographic completeness.
- **[THEORY-012](../theory.d/THEORY-012.md) cites §IV.A.1 for the sheaf condition and the equivalent
  formulations. Confirmed in those words.** Three precisions:
  - The review asserts the formulations' equivalence ("substantial
    equivalence") with citations and does not show it.
  - It credits Fine's theorem to Fine (CHSH only) and Suppes & Zanotti,
    with A&B 2011 as the first proof in contextuality language.
  - [THEORY-012](../theory.d/THEORY-012.md)'s "negative probability does not mark contextuality"
    concerns signed global sections. It should not be read against §VI.A.1:
    for one fixed quasiprobability representation (the discrete Wigner
    function, odd prime d), negativity coincides with
    stabilizer-measurement contextuality. That is a statement about a
    particular representation and a restricted measurement set, and it
    is consistent with [THEORY-012](../theory.d/THEORY-012.md) and [THEORY-014](../theory.d/THEORY-014.md).
  - [THEORY-012](../theory.d/THEORY-012.md)'s summary still calls the review "seeded, not read". That
    is now stale.
- **[THEORY-013](../theory.d/THEORY-013.md) cites §IV.C.5 for the same criterion in physics.
  Confirmed with a qualification.** The review describes Kujala et al.'s
  maximally noncontextual models and reports that the KCBS data violate
  Eq. 55. It presents them as one noise model among four, motivated by
  "clumsiness" of measurements, not as a principled separation of
  context-dependent marginals from contextuality. It never names
  Contextuality-by-Default and says nothing about behavioural data. "The
  same criterion" is accurate for binary cyclic systems.
- **[THEORY-015](../theory.d/THEORY-015.md) cites the review as supporting, with no section. The
  support is thin.** The review does not state that KS noncontextuality
  is measurement noncontextuality plus outcome determinism. It does not
  state that preparation noncontextuality implies outcome determinism
  for sharp measurements, or that KS proofs refute universal
  noncontextuality. The nearest passages:
  - §IV.B.3: under measurement noncontextuality, unsharp response
    functions cannot be deterministic (Spekkens 2014). It is followed
    only by "one can then compare these assumptions with the usual
    assumptions of Kochen-Specker theorem", with citations.
  - §IV.E.1: the definitions.
  - §IV.E.4: KS's and Bell's qubit models are preparation contextual,
    which is consistent with [THEORY-015](../theory.d/THEORY-015.md)'s direction.
  [THEORY-015](../theory.d/THEORY-015.md) should cite those three passages, or drop the review as a
  source.
- **[QUESTION-067](../questions.d/QUESTION-067.md).** The review keeps the two notions apart and
  prefers ideal measurements for KS contextuality (App. A.5). It argues
  that joint measurability alone cannot define contexts, which bears on
  any test of pragmatic judgements: what makes two renderings "the same
  measurement in different contexts" must be argued operationally.
- **Two accounts filed from this reading.** [THEORY-309](../theory.d/THEORY-309.md): contexts
  by joint measurability alone trivialize contextuality (§IV.B.2).
  [THEORY-303](../theory.d/THEORY-303.md): acyclic compatibility structures cannot be contextual
  (Vorob'ev, §V.B.2). The rest of the review either restates results the
  record already holds from their primary sources ([LIT-016](../literature.d/LIT-016.md), [LIT-265](../literature.d/LIT-265.md),
  [LIT-266](../literature.d/LIT-266.md)) or surveys work the record does not hold.
- **Other readings that leaned on the skim.**
  - [NOTE-243](NOTE-243.md) says the review is "restricted to consistently connected
    models". That is true of §IV.A only. §IV.C treats context-dependent
    marginals explicitly, through sequence-dependent values and
    Kujala et al.'s per-context copies.
  - [NOTE-250](NOTE-250.md) asked whether the review discusses the cohomological
    witness. It does not. §IV.A.4 names topological and cohomological
    follow-ups in one sentence.
  - [NOTE-279](NOTE-279.md) suggests citing the review for KS sets in every dimension
    ≥ 3. That works: §III.A cites Cabello & García-Alcaine 1996 for every
    d > 3.
- **[LIT-007](../literature.d/LIT-007.md)'s stabilizer results.** §V.D.3 and §VI.A.1 sharpen them. The
  qubit stabilizer subtheory is contextual (it contains Peres–Mermin)
  yet efficiently simulable by a contextual hidden-variable model
  (Hindlycke & Larsson 2022). So contextuality is necessary for
  magic-state universality (Howard et al.) but not sufficient for
  computational advantage.
- No instruction for machine-learning practice. §VI.D.5 names
  "machine learning" only as a possible application.

## Limitations

- A review: most results are cited, with sketches at most. Its own
  arguments are the triviality construction (§IV.B.2), the conversion of
  NCHV+E inequalities (§IV.A.5), and the expository proofs.
- It favours sequential, ideal-measurement tests and says so (§IV.B,
  §IV.D.5). Spekkens's programme and the Liang–Spekkens–Wiseman approach
  are covered briefly or not at all.
- The loophole analysis is incomplete by the authors' own account (§VII):
  "a comprehensive description in a unified framework is missing".
- The relation between KS and generalized contextuality is described,
  not derived.

## Open questions

- Its own list (§VII): the smallest state-independent contextuality
  scenario; a family of graphs with ϑ(G)/α(G) approaching |V|; a unified
  treatment of experimental imperfections; whether contextuality yields
  a memory advantage in sequential simulation; and its role in the
  circuit model.
- For the record: whether an operational notion of context of the
  §IV.B.2 kind, repeatable and nondisturbing, can be stated for
  judgement or interpretation data at all ([QUESTION-067](../questions.d/QUESTION-067.md)).
