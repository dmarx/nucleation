---
status: Read
paper: LIT-tmpfywhk
title: 'Spivak — Compositional dynamics in learning and mechanics'
version: 1
history:
- version: 1
  date: '2026-10-27'
  note: >-
    Read in full from arXiv 2606.28984v2 (stamped "[math.CT] 22 Aug
    2026"), 91 pp., the current version on 2026-10-27; v1 (27 June 2026)
    was not seen, so what changed between the versions is unknown. The
    text was extracted with `pdftotext -layout` and read from the
    abstract through the conclusion and reference list: §§1–7, every
    definition, theorem, proposition, remark and example, the footnotes
    and the 41 references. Definitions and theorem statements are quoted
    from the text; proofs were followed and are summarized, the ones in
    §§6.6 and 7 line by line. Pages are the PDF's own. The extraction
    loses diagrams (the wiring pictures (1), (4), (77) and the
    commutative diagrams) and garbles sub- and superscripts; formulas
    below are reconstructed where they had to be, and the two
    computations the record leans on (Proposition 7.4.1 and Remark 7.4.2)
    were checked numerically on a four-vertex path graph.
date: '2026-10-27'
summary: >-
  A category-theoretic syntax, the operad ArrSm of "smooth adaptive
  arrangements" (a responsive parameter space, a lens of output and input
  maps between manifolds, and a real potential), with two functorial
  semantics into polynomial coalgebras, i.e. discrete-time input-output
  machines. They differ only in the integrator: Φconf stores position and
  takes a descent step, Φphase stores position and momentum and takes a
  symplectic-Euler step. Φconf turns a parameterized map plus a loss into
  gradient descent with backpropagation, and a closed system with
  inverse-Hessian response into Newton's method. One arrangement of
  harmonic particles on a finite directed graph gives the discrete wave
  equation under Φphase and the discrete heat equation under Φconf, both
  governed by the symmetrized graph Laplacian. The main technical result
  is lens internalization, a lax symmetric monoidal functor Lens_C → C.
---
<!-- inactive-ok-file: CLAIM-tmpfw510 CLAIM-tmpdjt64 TERM-tmpjdel0 QUESTION-tmpubsi9 — Rejected, Proposed or Open; the record's neighbours, cited as open or as the conjecture answered -->

# NOTE-tmplvblh: Spivak — Compositional dynamics in learning and mechanics

## Contribution

A single compositional setting "in which gradient-based learning and
Hamiltonian-style mechanics appear as functorial semantics" (abstract, p. 1).
The syntax is an operad ArrSm whose objects are input-output interfaces
(pairs of manifolds) and whose morphisms are smooth adaptive arrangements.
The semantics are two operad functors Φconf, Φphase : ArrSm → PC into the
2-category of polynomial coalgebras, which the paper reads as "input-output
discrete dynamical systems" (p. 1). The author lists seven contributions
(p. 7): lens internalization (Corollary 3.3.4, Theorem 3.3.3); a vocabulary
of suboperads (stateless, potential-free, static, quadratic, linear,
unilateral; Definition 5.3.2, Proposition 5.3.3); a Lotka–Volterra example
(Example 5.4.4); the two functors (Corollary 6.4.1); exact symplecticity of
the phase step for a harmonic closed system (Proposition 6.6.1); Φconf
recovering gradient descent with backpropagation and Newton's method
(§§7.1–7.2); and one arrangement of harmonic particles giving the discrete
wave equation via Φphase and the discrete heat equation via Φconf (§7.4,
Remark 7.4.2). The abstract calls lens internalization "The main technical
result of the paper" (p. 1).

## Key insight

The coupling data and the dynamical regime are separated. An arrangement
fixes the wiring, the potential and the response; an integrator, chosen
afterwards, fixes what state is stored and how an incoming covector updates
it. "Thus the integrator is where the dynamical regime gets decided: one
smooth adaptive arrangement fed through different integrators can produce
qualitatively different behaviors" (p. 6). And: "the diagram fixes the
wiring, the potential, and the geometry of the parameter space, while the
integrator alone selects the dynamical regime, second-order or first-order"
(pp. 6–7).

The common thread between learning and mechanics is a map T*M → TM that
turns the differential of a potential into a state change: "the potential
energy in Hamiltonian dynamics or the loss in gradient descent—so it is the
potential that drives the state" (pp. 2–3). The paper calls vector spaces
with such a map responsive. A slogan for interfaces: "Your inputs are what
your interior can have preferences over, and your outputs are what your
exterior can have preferences over" (p. 5).

## Assumptions

- **Parameters are vector spaces, not manifolds.** RVect is
  finite-dimensional real vector spaces with a sharp map, and its morphisms
  are sharp-equivariant linear isomorphisms (Definition 5.2.1, p. 39). The
  extension to "responsive manifolds with connection" is conjectured
  (Remark 6.3.3, p. 56), not done.
- **Discrete time, explicit-Euler-type integrators.** Each tick emits a
  position, receives a direction and updates once (Remark 4.3.7, p. 35).
  Multi-stage integrators (Runge–Kutta, velocity Verlet) are left to future
  work; an ℓ = 2 case exists only in companion code written by Claude and
  "we have not independently audited it" (p. 36).
- **Couplings are potentials, never equations.** "every expression in ArrSm
  denotes a deterministic discrete-time system (Theorem 4.3.6), and
  correspondingly we do not express idealized constraints between systems;
  e.g. a "rigid" coupling can only be specified as a stiff potential, rather
  than an equation" (p. 9).
- **Smoothness is a convenience.** All statements are said to hold for C¹
  maps, with four listed exceptions (Remark 5.1.2, pp. 38–39).
- **The potential algebra is fixed at r = +1** (Lemma 6.2.1, (38), p. 53),
  which is what makes potentials contribute their ordinary differentials.

## Key results

### The syntax (§§3–5)

- **Theorem 3.3.3 (p. 26).** "Let (T, τ) be a monoidal monad on a symmetric
  monoidal closed category (C, I, ⊗, [−, −]), and let z = (z, e, m, α) be a
  T-monoid in C (Definition 3.3.1). Then there is a lax symmetric monoidal
  functor that acts on objects as follows: Θ_z : Lens^T_C → C,
  (c⁻, c⁺) ↦ [c⁻, z] ⊗ c⁺. It is normal if and only if e : I → z is an
  isomorphism." The proof is a diagram chase of sixteen tiles plus a
  pentagon (p. 27).
- **Corollary 3.3.4 (Lens internalization), p. 28.** "Let (C, I, ⊗, [−, −])
  be a symmetric monoidal closed category. There is a normal lax symmetric
  monoidal functor Θ : Lens_C → C, (c⁻, c⁺) ↦ [c⁻, I] ⊗ c⁺." In Poly a lens
  (Ay, By) internalizes to By^A, whose coalgebras are Moore machines
  (Example 3.3.5).
- **Definition 4.1.1 (p. 29).** An adaptive-arrangement datum
  D = (M, Q, J, R) is "a cartesian monoidal category M, objects are called
  spaces; a symmetric monoidal category Q, objects are called parameters; a
  strong monoidal functor J : Q → M; and a monoidal monad R on M, the
  potentials monad." Arr_D is "the operad underlying the symmetric monoidal
  category Para_Q(Lens^R_M)".
- **Definition 5.2.1 (p. 39).** "A responsive vector space is a
  finite-dimensional real vector space Q together with a smooth map
  ♯_Q : Q → Vect(Q*, Q), the sharp map". Constant, symmetric, quadratic
  (constant and symmetric) and nondegenerate responses are defined there.
  "Our theory does not privilege nondegenerate responses in any way"
  (p. 39).
- **An arrangement (35), p. 42**: f = (Q, f⁺, f⁻, U) with
  f⁺ : Q × M⁺ → N⁺, f⁻ : Q × M⁺ × N⁻ → M⁻, U : Q × M⁺ × N⁻ → ℝ. The
  potential reads the parameter, the inner outputs and the outer inputs,
  and "can read neither M⁻ nor N⁺" (p. 5).
- **Definition 5.3.2 (p. 42)** names the classes. "harmonic if it is
  quadratic, M⁺ and N⁻ are vector spaces, and its potential U is a quadratic
  form"; "unilateral if whenever f⁺(q, m⁺) = n⁺ and ξ ∈ T*_{n⁺}N⁺, we have
  ♯_q((∂_q f⁺)ᵀξ) = 0", i.e. nothing returned at the output can move the
  state. **Proposition 5.3.3 (p. 43):** "The stateless, potential-free,
  static, quadratic, and unilateral morphisms each span a wide suboperad of
  ArrSm, and the linear morphisms also span a suboperad". Harmonic ones do
  not, because composing through a nonlinear input map breaks quadraticity
  (footnote 19, p. 43).
- **Degeneracy and back-driving (pp. 39–40).** "Degeneracy is what allows
  things like controllers to act on their environment without being
  retroactively back-driven by it. We refer to this condition as
  unilaterality". The author links it to Del Vecchio, Ninfa and Sontag's
  retroactivity, "which they identify as an obstruction to modularity in
  biomolecular networks" (p. 40).

### The semantics (§§4, 6)

- **Definition 4.3.4 (p. 34).** "A p-integrator is a pair 𝔦 = (S, dyn) …
  where S : Q → Set, the state space functor, is strong symmetric monoidal
  and dyn : Store∘S ⇒ p, the dynamics map, is a monoidal natural
  transformation."
- **Theorem 4.3.6 (p. 35).** "Every polynomial interpretation datum
  𝔭 = (c, R′, θ, z) and (c∘J)-integrator 𝔦 induce an operad functor
  Φ_{𝔭,𝔦} : Arr_D → PC, which is normal (as a lax symmetric monoidal
  functor) when z ≅ y."
- **The cotangent functor (Definition 6.1.1, p. 51)** sends M to
  Σ_{m∈M} y^{T*_m M} and a smooth map to itself forward on points and its
  transposed differential backward on covectors; its functoriality "is the
  chain rule". It is strong symmetric monoidal (Proposition 6.1.2).
- **Corollary 6.4.1 (p. 62).** "Every cot-integrator 𝔦 induces an operad
  functor Φ_𝔦 : ArrSm → PC with Φ_𝔦(1,1) ≅ y; hence it carries closed
  systems to y-coalgebras."
- **The configuration integrator (41), p. 56**: state Q; an incoming
  covector ξ updates q ↦ q − ♯_q(ξ). "The minus is the integrator's … which
  is what makes the configuration dynamics descend rather than ascend"
  (p. 56).
- **The phase integrator (49)–(50), p. 61**: state T*Q ≅ Q ⊕ Q*; it
  presents q̃ = q + ♯_q(ξ) and updates ((q, ξ), ξ′) ↦ (q + ♯_q(ξ), ξ − ξ′),
  with ξ′ the gradient computed at q̃. "This has one step of Hamilton's
  equations as a special case" (p. 61).
- **The general update (58)–(59), pp. 64–65.** The state covector is the
  sum of three pullbacks: the outer covector along f⁺, the inner covector
  field along f⁻, and +1 along U (giving dU); its Q*-component is sharpened
  and subtracted. Both functors share this factor and differ only in where
  it is evaluated (stored q for Φconf, presented q̃ for Φphase) and how the
  state is updated (p. 68).
- **Proposition 6.5.1 (p. 65)** relates Φconf to the continuous-time
  open-energy-driven systems of Capucci, Lynch and Spivak (CLS24) through a
  category S of submersions. "neither their framework nor the one in this
  paper subsumes the other" (p. 8).
- **Remark 6.4.2 (pp. 62–63).** Naturality of an integrator can be weakened
  by shrinking the parameter category; "We conjecture that Adam [KB15] is an
  integrator when Q is restricted to the subcategory whose objects are
  Euclidean vector spaces ℝⁿ equipped with Euclidean sharp and whose
  morphisms are signed permutations." Monoidality cannot be weakened: "The
  monoidality of 𝔦 corresponds to the compositionality of the semantics,
  that each box can compute its own update."

### Closed phase steps and symplecticity (§6.6.2)

- For a closed system, Φphase is (q, ξ) ↦ (q + ♯_q(ξ), ξ − dU|_q̃), (65),
  p. 69. With constant symmetric sharp it is the symplectic Euler step of
  H(q, ξ) = ½ξ(♯₀(ξ)) + U(q) (p. 70). "The discrete step (65) need not
  conserve H exactly" (p. 70).
- **Proposition 6.6.1 (p. 70).** "Let f = (Q, ♯₀, !, !, U) : I → I be a
  harmonic closed system (Definition 5.3.2) whose potential is
  U(q) = ½(κq)(q) for a symmetric linear map κ : Q → Q*. Then, for the
  drift and kick of (66), Φphase(f) = kick ∘ drift. In particular, the
  update (65) is an endomorphism of the responsive vector space T*Q in
  RVect, i.e. a linear isomorphism preserving the canonical symplectic
  pairing (33)." Proof: drift and kick each preserve the pairing, by
  symmetry of the sharp and of κ (pp. 70–71).

### Applications (§7)

- **Newton's method (§7.1, pp. 71–72).** A closed system with response the
  inverse Hessian, ♯^U_q = (T_q(dU))⁻¹, under Φconf is
  q ↦ q − (T_q(dU))⁻¹(dU|_q), (67). It needs the Hessian invertible
  everywhere, and finds "any critical point rather than only moving
  downhill toward minima" (p. 72).
- **Gradient descent and backpropagation (§7.2, pp. 73–76).** A
  parameterized map F : Q × ℝᵐ → ℝⁿ, with zero potential, composed with a
  stateless loss arrangement, gives under Φconf, for ♯_q = η_LR♯_Euc,
  "ordinary gradient descent at rate η_LR: q ↦ q − η_LR(T_q F(◽, x))ᵀξ"
  (76), p. 75. "Backpropagation is thus the chain rule, packaged as the
  functoriality of Φconf" (p. 75). A weight-only potential (γ/2)‖q‖² gives
  weight decay (Proposition 7.2.3, p. 76). The training data are an
  environment coalgebra that may itself adapt to the returned covectors
  (Example 7.2.1, p. 75).
- **The wave equation on a chain (§7.3, pp. 76–83).** K particles with
  sharp ξ/m and harmonic potential (κ/2)(q − q′)², wired in series. With
  both ends pinned ((82), (83)) the phase dynamics give
  m q̈ᵢ = κ(qᵢ₋₁ − 2qᵢ + qᵢ₊₁), (78), with q̈ᵢ(t) = qᵢ(t+1) − 2qᵢ(t) +
  qᵢ(t−1) (Proposition 7.3.3, p. 81). §7.3.2 recomputes it by applying
  Φphase to the parts and composing in PC, "an explicit check on signs,
  indices, and the routing" (p. 81), and the two agree term by term (p. 83).
  Remark 7.3.2 (pp. 77–78) notes a stateless bond is "formally, the same
  construct as the training loss": "each bond is like a "training loss"
  provided to each mass by its neighbor."
- **The graph Laplacian (§7.4, pp. 83–87).** For a weighted finite directed
  graph G with masses m_v and spring constants κ_e, the composite potential
  is U(q) = Σ_{e∈E} (κ_e/2)(q_tgt(e) − q_src(e))², (89), and dU = L_G q,
  "the weighted (and symmetrized …) graph Laplacian of G" (p. 85). The
  orientation drops out: "what we recover is the symmetrized Laplacian, so
  G behaves like its underlying undirected multigraph" (p. 83).
  **Proposition 7.4.1 (p. 86):** "every trajectory of Φphase(wire_G) …
  satisfies m_v q̈_v(t) = −(L_G q(t))_v (v ∈ V, t ≥ 1)". The arrangement is
  harmonic, so the step preserves the symplectic pairing (p. 86).
- **Remark 7.4.2 (pp. 86–87), the heat equation.** "applying Φconf to the
  very same smooth adaptive arrangement wire_G of (88)—same graph wiring,
  same potential, and the same positive inverse-mass response—recovers the
  discrete heat equation on G": m_v(q_v(t+1) − q_v(t)) = −(L_G q(t))_v for
  t ≥ 0, i.e. M q̇ = −L_G q, "diffusion on G with the masses m_v serving as
  heat capacities". "Thus a single smooth adaptive arrangement gives wave
  dynamics under the phase integrator and heat dynamics under the
  configuration integrator: the second-order, symplectic regime and the
  first-order, descent regime are two semantics of one syntactic object"
  (p. 87). This is a remark with its computation, not a numbered result;
  the computation is short and checks.
- **Remark 7.4.3 (p. 87).** A learner can be trained to predict a closed
  system. Observing positions alone, the wave system has no one-step map on
  the observations, "states with the same position and different momenta
  have different next positions"; observing two consecutive configurations,
  it does.

### Examples reported from code (Example 5.4.5, pp. 47–50)

Transistors, a NAND gate, latches, Black's feedback amplifier, an LC
circuit, a DC motor, molecular dynamics, impedance control, Kuramoto
oscillators, Petri nets, replicator dynamics and Hopfield networks. "Each
construction below is implemented in the companion code … by Claude …
The author understands the content of the claims as stated, and believes
them to be reasonable and to have been checked, but has not verified all of
them by hand" (p. 47). One is a timing claim: "a chain of K inverters takes
roughly K times as many ticks of the coalgebra to converge as one does,
whereas K side-by-side copies take the same number of ticks as one" (p. 47).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Lens internalization: every symmetric monoidal closed C has a normal lax symmetric monoidal Θ : Lens_C → C, (c⁻, c⁺) ↦ [c⁻, I] ⊗ c⁺, with a monad/monoid generalization | strong | Theorem 3.3.3 and Corollary 3.3.4, proved by diagram chase (pp. 26–28) |
| C2 | Every polynomial interpretation and integrator give an operad functor Arr_D → PC; in the smooth case Φconf and Φphase | strong | Theorem 4.3.6, Corollary 6.4.1, assembled from cited results on Para and actegories (pp. 33–35, 62) |
| C3 | Φconf of a parameterized map composed with a loss is gradient descent, with backpropagation as the lens backward pass; weight decay and Newton's method arise likewise | strong | explicit unpacking of (58)–(59) (§§7.1–7.2); the composite is per datum, deterministic, fixed sharp |
| C4 | One arrangement of harmonic particles on any finite directed graph gives the discrete wave equation under Φphase and the discrete heat equation under Φconf, both governed by the symmetrized graph Laplacian | strong | Proposition 7.4.1 (proved) and Remark 7.4.2 (computed in the text, not numbered); checked numerically here |
| C5 | For a harmonic closed system the phase step preserves the canonical symplectic pairing exactly, though it need not conserve H | strong | Proposition 6.6.1, short proof (pp. 70–71) |
| C6 | Unilateral (and stateless, potential-free, quadratic) arrangements are closed under composition | strong | Proposition 5.3.3, chain-rule proof (pp. 43–44) |
| C7 | The integrator alone selects the regime | moderate | true of the paper's two integrators by construction (the shared factor Φ′sm, p. 68); a general reading beyond those two is the author's framing |
| C8 | Adam is an integrator over Euclidean spaces with signed permutations | weak | stated as a conjecture (p. 62) |
| C9 | Phase semantics of a neural network gives momentum training | weak | "we expect" (Conclusion, p. 87) |
| C10 | The circuits, chemistry, ecology and neuroscience examples of Example 5.4.5 behave as described | weak | implemented and tested by Claude, not verified by hand by the author (p. 47) |

## Concepts

- **Smooth adaptive arrangement** — a morphism of ArrSm: a responsive
  parameter space, an output map, an input map and a real potential, (35).
  "adaptive" names that the parameter is a state the dynamics evolve
  (p. 3).
- **Responsive vector space** — a vector space with a sharp
  ♯_Q : Q → Vect(Q*, Q) turning covectors into state changes; the symplectic
  sharp in mechanics, a learning-rate-scaled metric in learning (p. 3).
- **Lens** — a forward map and a backward map, f⁺ : c⁺ → d⁺ and
  f⁻ : c⁺ ⊗ d⁻ → c⁻ (Definition 3.1.1); the wiring of boxes.
- **Polynomial coalgebra; PC** — a p-coalgebra S → p(S) is a deterministic
  system with state that emits a position and updates on a direction; PC has
  polynomials as objects and [p, p′]-coalgebras as morphisms, "called Org in
  [Spi21; SS22]" (p. 14).
- **Integrator** — a state-space functor and a dynamics map Store∘S ⇒ p
  (Definition 4.3.4): the semantic choice of what is stored and how it is
  updated.
- **Configuration vs phase** — state Q and a descent step, vs state T*Q and
  a symplectic-Euler step (§6.3).
- **Harmonic** — quadratic response and quadratic-form potential
  (Definition 5.3.2).
- **Unilateral** — the output cannot back-drive the state (Definition 5.3.2,
  p. 42); realized by a degenerate sharp.

## Connections

- **Capucci, Lynch and Spivak (2024)**, open energy-driven systems, the
  "closest predecessor" (p. 8), continuous-time; Proposition 6.5.1 relates
  them. Not held by the record.
- **Fong, Spivak and Tuyéras, "Backprop as Functor"** (FST19, cited p. 6),
  held as LIT-827, read; THEORY-519 holds its theorem. Here gradient descent
  with backpropagation is again a functor, but the backward message is a
  covector pulled back by the transposed differential (71), not FST's
  requested input, and the loss is an arrangement in the same operad
  rather than a parameter of the functor. The paper does not compare the
  two beyond citing FST19 for lenses in backpropagation.
- **Shapiro and Spivak, dynamic operads** (SS22, p. 17): "a dynamic category
  is defined to be a category enriched in PC".
- **Coya on bond graphs** (Coy17, p. 9): relational semantics that "need not
  admit an evolution at all", against ArrSm's always-deterministic one; a
  comparison is left open (p. 88).
- **Del Vecchio, Ninfa and Sontag** on retroactivity (DNS08, p. 40).
- **Fong and Spivak, Seven Sketches**, held as LIT-803, is not cited. The
  paper's own background for wiring-diagram operads is §2.3, citing Spi13,
  Yau15, SSR17, FS19 and PSV21.

## Bearing on the record

- **CLAIM-tmpywecm: consistent, and an instance it does not state.** The
  exchange (A22 §6) cited the paper for "The same relational organization
  need not imply the same temporal hierarchy". The paper never speaks of
  time scales, separation or hierarchy. What it shows is narrower and
  exact: the same wiring, potential and response give a first-order descent
  dynamics M q̇ = −L_G q under Φconf and a second-order symplectic one
  m q̈ = −L_G q under Φphase (Proposition 7.4.1, Remark 7.4.2, pp. 86–87).
  Reading those through the claim (my derivation, not the paper's): per
  eigenmode of M⁻¹L_G with eigenvalue μ, the heat step multiplies by 1 − μ
  each tick, so the spectrum is a hierarchy of relaxation rates; the
  symplectic step preserves the pairing (Proposition 6.6.1), so no mode
  decays and the spectrum is a set of frequencies. That is the claim's two
  halves, a Laplacian flow whose spectrum sets the rates and a conservative
  coupling that splits modes without damping them, now as two semantics of
  one arrangement. One caution: what the paper varies is the integrator,
  which it calls "the semantics", a modeller's choice of whether momentum is
  stored. As a physical demonstration that coupling does not fix the
  hierarchy, it shows that the coupling data underdetermine the dynamics;
  the missing datum is inertia against dissipation, which is the claim's
  condition. "Almost a controlled demonstration" is fair if the control is
  understood as that.
- **CLAIM-tmpfw510 (Rejected): a further counterexample family, no
  change.** Under Φphase every harmonic network on a finite graph is coupled
  and symplectic, so its relative modes never decay (Proposition 6.6.1,
  §7.4). The rejection stands as filed.
- **CLAIM-tmpose3y: the composition is literal here, and constraints are not
  primitive.** In ArrSm an interior wired inside a box is a morphism, and
  the composite's potential is the sum of its parts' potentials pulled back
  through the wiring ((89), p. 85; Proposition 5.3.3's composite potential,
  p. 43). The paper does not eliminate an interior (no Schur complement, no
  memory kernel), so it neither confirms nor tests the claim's computation.
  It bears on the claim's reading in two ways. First, a constraint between
  parts is only ever a limit: "a "rigid" coupling can only be specified as a
  stiff potential, rather than an equation" (p. 9), and "A choice of
  degenerate ♯_Z = 0 is like a weld holding z fixed" (p. 45). Second, the
  composite's external behaviour is assembled functorially from its parts'
  (Corollary 6.4.1, and the §7.3.2 audit), which is the same shape as the
  black-boxing functor the claim cites, for dynamics rather than for static
  relations.
- **CLAIM-tmpdjt64.** Here interactions are potentials, not correspondences:
  the wiring (a lens) routes values, and the potential, which lives
  "interior to the outer box N and exterior to the inner box M" (p. 5),
  supplies the covectors that move the states. An interaction never fixes a
  relation exactly; it penalizes departures from one. If the claim's gluing
  conditions are exact restrictions, this framework realizes them only as
  stiff limits (p. 9).
- **TERM-tmpjdel0 and QUESTION-tmpubsi9: unilaterality is a formal version
  of selective coupling without back-action.** A unilateral arrangement's
  output cannot move its state (Definition 5.3.2), the amplifier is the
  worked case ("whatever is wired to the output cannot move the state",
  p. 48), and unilaterality is preserved by composition (Proposition 5.3.3).
  The author ties it to retroactivity as an obstruction to modularity
  (p. 40). This is a structural condition an apparatus in the term's sense
  could meet; the paper does not use the word or the idea of measurement.
- **LIT-803 (Seven Sketches): not cited; the same programme.** Operads as
  syntax and functors as semantics (§2.3), with the semantics now
  dynamical. The book's compositional reading of observation is not
  engaged.
- **Filed from this reading:** THEORY-tmp09707 (the heat and wave
  semantics of one arrangement) and THEORY-tmp3wlcq (gradient descent as a
  functorial semantics).
- **LIT-827 and THEORY-519: a second, different functorial account of
  backpropagation by an overlapping author**, with covectors in place of
  requested inputs and a fixed or position-dependent sharp in place of a
  step size (§7.2). Neither paper is defeated by the other; they formalize
  different backward messages.
- **No instruction for machine-learning practice.** The Adam conjecture
  (p. 62) and the momentum expectation (p. 87) are about what the formalism
  can express, not advice.

## Limitations

- **Read from v2 only.** The registration's v1 date is from the arXiv API;
  the differences between v1 and v2 are unknown.
- **Diagrams lost in extraction.** The wiring pictures and commutative
  diagrams were reconstructed from the surrounding prose; nothing in the
  results above depends on a picture alone.
- **Discrete time throughout.** "wave equation" and "heat equation" are
  difference equations in space and time, one tick per Euler step; the
  continuum limit is pointed to [Dem15] in footnote 31, not shown. Stability
  of either step (the heat step needs the eigenvalues μ of M⁻¹L_G in (0, 2),
  the symplectic one in (0, 4), by my derivation) is not discussed; the
  paper's only bound of this kind is for the LC circuit, "4LC > 1"
  (footnote 20).
- **"Dissipative" and "conservative" are not the paper's words** for the two
  regimes. It says "first-order, descent" and "second-order, symplectic"
  (p. 87), proves exact symplecticity for harmonic closed systems only, and
  says the phase step "need not conserve H exactly" (p. 70). That the heat
  step lowers U was checked numerically here, not shown in the text.
- **Much of §5.4.5 and the companion code are Claude-written and
  unaudited** by the author's own statement (pp. 36, 47, 71 n. 30). The
  acknowledgements also thank "Claude and Codex for assistance in editing
  the document" (p. 10).
- **Several statements are conjectures or expectations**: manifold
  parameters (Remark 6.3.3), multi-stage integrators (Remark 4.3.7), Adam
  (Remark 6.4.2), momentum training, the Φphase–Φconf relation on quadratic
  arrangements and a linear-stratum retraction (Conclusion, pp. 87–88).

## Open questions

- Is there, for every quadratic arrangement f, an arrangement g on T*Q with
  Φphase(f) = Φconf(g), functorially, as the conclusion expects (p. 88)? It
  would make the two regimes one semantics of two arrangements, which bears
  on whether the regime belongs to the syntax or the semantics.
- What does an integrator with damping look like? The damping 1-form exists
  (Example 6.3.14, p. 59: "it removes a fraction c of the momentum at each
  step") but "plays no further role". With it, the same arrangement would
  interpolate between the two regimes, and the separation of collective and
  relative modes could be read off as a function of c.
- Does a composite's external dynamics ever reduce to a smaller arrangement
  (an interior eliminated), as CLAIM-tmpose3y's elimination does for energy?
  The paper composes but never reduces.
