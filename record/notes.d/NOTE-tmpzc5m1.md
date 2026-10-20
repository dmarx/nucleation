---
status: Read
paper: LIT-tmpai9kc
title: 'Chorin, Hald and Kupferman — Optimal prediction and the Mori–Zwanzig representation'
version: 1
history:
- version: 1
  date: '2026-10-20'
  note: >-
    Read in full from the authors' copy on Chorin's Berkeley page
    (math.berkeley.edu/~chorin/CHK.ps), a 20-page PostScript file that
    dvips made from "paper.dvi" on 1999-12-16, the paper's acceptance date.
    It was converted to PDF with Ghostscript (-dSAFER), the text was
    extracted with pdftotext, and every displayed equation was checked
    against page images rendered at 150–200 dpi, because extraction lost
    signs and sub- and superscripts. Read: the abstract, §§1–5, every
    equation from (2.1) to (4.11), the Dyson formula, Figure 1 with its
    caption, and the references. The typeset PNAS version was not reached,
    and this copy was not compared with it. The PMC PDF is behind a
    reCAPTCHA. pnas.org returned 403. Europe PMC returned 403, and its
    full-text XML service returned 500. NCBI E-utilities returned the
    front matter only ("The publisher of this article does not allow
    downloading of the full text in XML form"). Equation numbers and small
    typos may differ in print. The general identities and three of the
    paper's claims were re-checked with numpy (see Bearing and
    Limitations).
date: '2026-10-20'
summary: >-
  Writes Zwanzig's nonlinear Mori–Zwanzig identity with the projection taken
  as conditional expectation on the resolved variables under an invariant
  measure: ∂ₜSᵗA = R(SᵗA) + ∫₀ᵗ K(s, S^{t−s}A) ds + S⊥ᵗF, with
  R(A) = E[LA|A], F = LA − E[LA|A] and K(s, A) = E[LS⊥ˢF|A]. First-order
  optimal prediction, dv/dt = R(v), is that identity with the memory and
  noise dropped, and for a canonical Hamiltonian system it is Hamiltonian
  in a renormalized 𝓗 = −log∫e^{−H}. In a perturbative nonlinear
  Schrödinger example with one resolved mode, a memory kernel cut off at a
  hand-chosen time recovers the decay of the conditional mean that the
  Markovian scheme misses. The paper states no fluctuation–dissipation
  relation and no criterion for when the Markovian term suffices.
---
<!-- inactive-ok-file: THEORY-257 CLAIM-327 CLAIM-331 — Proposed; open claims and readings this reading bears on, nothing here rests on their being settled -->
<!-- inactive-ok-file: LIT-tmple6xy LIT-tmpvihtb — Deferred or Unavailable; works not yet read, cited as open -->
# NOTE-tmpzc5m1: Chorin, Hald and Kupferman — Optimal prediction and the Mori–Zwanzig representation

## Contribution

It joins two literatures. One is the authors' own "optimal prediction" of
underresolved computations: averaging the unresolved variables against a
prior invariant measure, conditioned on the resolved ones. The other is the
Mori–Zwanzig projection formalism of nonequilibrium statistical mechanics.
It shows that first-order optimal prediction is the Markovian term of
Zwanzig's nonlinear generalized Langevin equation. The terms that optimal
prediction drops are a memory integral and a noise orthogonal to the
resolved variables. It derives the equation for any flow with an invariant
measure, not only a Hamiltonian one, and shows in one example that keeping
the memory term recovers a decay that the Markovian scheme misses. In the
authors' words: "The analogy between irreversible statistical mechanics and
underresolved computation is the main contribution of the present paper."

## Key insight

When you follow a few functions A of a large system's state and average
over the rest, the exact equation for A has three parts. The first is the
best function of A's present value: the conditional mean of A's rate of
change given A. The second is an integral over A's own past. The third is
a term that depends on the unresolved initial state and is uncorrelated
with every function of A's initial value. A Markovian reduced model,
however well chosen, keeps only the first. The error it makes over time is
the irreversible loss of information about the initial data, which the
memory term carries.

## Assumptions

- A flow du/dt = R(u) on a phase space Γ of dimension n, "n may be
  infinite", with flow map φ(u, t). The derivation is formal: no domains,
  no regularity, and no proof that the exponentials or S⊥ᵗ exist.
- An invariant probability measure μ⁰ on Γ, with μᵗ = μ⁰. The initial data
  are drawn from it, so u and A(u) are random variables. Hamiltonian
  structure is not needed for §2. It is used in §3's reduced-Hamiltonian
  form and in §4.
- Resolved variables are a vector A = (A₁, …, A_m) of phase functions
  ("phase variables"). Often A = P_m u, the first m components.
- The projection is P B = E[B | A], the conditional expectation under μ⁰,
  read as the L²(μ⁰)-orthogonal projection onto all functions of A, not
  only linear ones. This is Zwanzig's nonlinear projection, not Mori's
  linear one.
- §4 only: the nonlinear Schrödinger equation iuₜ = −u_xx + ¼(3|u|²u + u*³)
  on [0, 2π], periodic, in Fourier modes, with the canonical measure
  ∝ e^{−H/T}. Everything is computed perturbatively in the quartic part
  H₁ about the Gaussian measure ∝ e^{−H₀/T}, by Wick's theorem.

## Key results

- **Phase-variable dynamics (2.2).** (SᵗA)(u) = A(φ(u, t)) satisfies
  ∂ₜSᵗA = LSᵗA with the Liouvillian L = Σᵢ Rᵢ(u) ∂/∂uᵢ, and SᵗL = LSᵗ,
  Sᵗ(AB) = (SᵗA)(SᵗB), Sᵗf(A) = f(SᵗA).
- **Conditional expectation (2.3) and properties 1–5.** E[B|A] is the
  best mean-square approximation of B by a function of A, and
  E[f(A)(B − E[B|A])] = 0. Cited to Chung.
- **Splitting (2.4).** ∂ₜSᵗA = SᵗE[LA|A] + Sᵗ(LA − E[LA|A]). With
  R(A) := E[LA|A] (a 𝔑 in the paper), SᵗR(A) = R(SᵗA).
- **Orthogonal dynamics (2.5)–(2.6).** S⊥ᵗ is defined by
  ∂ₜS⊥ᵗF = LS⊥ᵗF − E[LS⊥ᵗF|A], with S⊥⁰F = F. Then
  ∂ₜE[S⊥ᵗF|A] = 0, so if F is orthogonal to the functions of A, so is
  S⊥ᵗF for every t.
- **Dyson formula.** SᵗB = S⊥ᵗB + ∫₀ᵗ S^{t−s} E[LS⊥ˢB|A] ds. Symbolically,
  e^{tL} = e^{t(I−P)L} + ∫₀ᵗ e^{(t−s)L} P L e^{s(I−P)L} ds.
- **Generalized Langevin equation (2.7).**

  ∂ₜSᵗA = R(SᵗA) + ∫₀ᵗ K(s, S^{t−s}A) ds + S⊥ᵗF,

  with F = LA − E[LA|A] and K(s, A) = E[LS⊥ˢF | A]. "An identity between
  phase variables." The first term is Markovian. The second is memory,
  depending on SˢA for 0 ≤ s ≤ t. The third is "noise": it needs the full
  initial u, and E[S⊥ᵗF | A] = 0 for all t. The authors note that this is
  "a weaker property than statistical independence".
- **First-order optimal prediction (3.1).** It approximates E[SᵗA | A] by
  v(t), where dv/dt = R(v) and v(0) = A(u). That is (2.7) with the memory
  and noise dropped.
- **(3.2), resolved components.** For A = P_m u, R(P_m u) = E[P_m R(u) | P_m u],
  the ratio of integrals over u_{m+1}, …, u_n against the density. This is
  contrasted with Galerkin truncation, dv/dt = P_m R(v₁, …, v_m, 0, …, 0).
- **Hamiltonian case.** With the canonical density Z⁻¹e^{−H}, the resolved
  pairs (Q, P) obey dQᵢ/dt = ∂𝓗/∂Pᵢ and dPᵢ/dt = −∂𝓗/∂Qᵢ, where
  𝓗(Q, P) = −log ∫ e^{−H} dp_{m+1}⋯dp_n dq_{m+1}⋯dq_n is the "reduced, or
  renormalized, Hamiltonian". This was re-derived here by differentiating
  under the integral.
- **§4, Markovian term (4.4).** It is truncation plus a frequency shift,
  ℜ_k ≈ −i(ω_k + C)u_k − (i/4) Σ (u*_{k₁}u*_{k₂} + 3u_{−k₁}u_{−k₂}) u*_{k₃}
  δ_{k,−k₁−k₂−k₃}, with C = (3T/2π) Σ_{|k|>m} 1/ω_k and ω_k = k². Checked:
  C ≈ 3T/(πm), "like 1/m", and C = π/2 at m = 0 and T = 1, which matches
  (4.11).
- **§4, noise and memory (4.5)–(4.9).** To leading order the noise is
  (I − P)S₀ᵗL₁u_k, using (I − P)L₀P = 0, so that S⊥,₀ᵗ(I − P) = (I − P)S₀ᵗ.
  The memory kernel is quadratic in L₁. It is a sum of terms linear,
  cubic and quintic in the resolved modes, with explicit oscillatory
  coefficients κ_q, φ_q and ψ_q. At m = 0, (4.11) keeps only the κ₀ and φ₀
  terms. Checked: ψ₀ ≡ 0, and the 3/16 terms need |k₃| > 0 with
  k₃ = −j₁ − j₂ − j₃ = 0, so they vanish.
- **Mean equation (4.10).** dv/dt = ℜ(v(t)) + ∫₀ᵗ K(s, v(t − s)) ds,
  obtained by averaging (2.7) conditionally, which removes the noise
  exactly, and then replacing E[ℜ(SᵗA)|A] by ℜ(v) and E[K(s, ·)|A] by
  K(s, v). The second step is a mean-field closure and is not controlled.
- **Figure 1.** m = 0, T = 1, with a Monte Carlo mean over 10⁴ solutions
  conditioned on u₀. First-order optimal prediction oscillates without
  decay at amplitude ≈ 0.03. The memory equation with κ₀ and φ₀ "truncated
  at t = 0.9", a cut-off "chosen so as to produce a reasonable decay",
  decays. It follows the Monte Carlo curve to t ≈ 2. After that it decays
  more slowly and drifts in phase: at t ≈ 6 it peaks near 0.012, while the
  Monte Carlo mean is near 0.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | For any flow with an invariant measure, the resolved variables obey the generalized Langevin identity (2.7), with conditional expectation as the projection | strong as a formal identity | Dyson formula "checked by differentiation"; the derivation in §2. No functional-analytic conditions are given. Invariance is assumed but is not used in deriving (2.7) itself (see Limitations) |
| C2 | The noise S⊥ᵗF has zero conditional mean given the initial A for all t, so it drops out of the conditional-mean equation | strong | (2.6) |
| C3 | First-order optimal prediction is (2.7) without memory and noise | strong | comparison of (2.7) with (3.1) |
| C4 | "No Markovian approximation of SᵗA by a system of m equations can be more accurate, in the mean square sense, than first order optimal prediction" | overstated | (2.3) gives this for the instantaneous rate of change, not for trajectories over time; a counterexample is in Limitations |
| C5 | For a canonical Hamiltonian system, first-order optimal prediction is Hamiltonian in the renormalized 𝓗 = −log∫e^{−H} | strong | derivation in §3, re-derived here |
| C6 | First-order optimal prediction works for short times, for m not too small and at low temperature, and fails for severely underresolved, hot, long runs | weak here | asserted; supported by earlier papers [2–4], not by this one |
| C7 | Including memory "is crucial" for capturing the relaxation of the mean, and gives means "faithful to the true means for longer times" | moderate for "captures the decay", weak for "faithful" | one example: m = 0, perturbative kernels, cut off at a time chosen to give a reasonable decay; Figure 1 shows phase and amplitude errors after t ≈ 2 |
| C8 | Loss of accuracy in underresolved computation is analogous to the loss of information in irreversible statistical mechanics, as the conditioned measure relaxes to the invariant one | interpretive | §5; the formal content is C1–C3 |

## Method

- Write the resolved variables' evolution in the Heisenberg form SᵗA.
- Split its rate of change by the conditional-expectation projection (2.4).
- Rewrite the orthogonal part with the Dyson formula. That gives (2.7).
- For a concrete system, expand L = L₀ + L₁ about an integrable quadratic
  part. Compute R, the noise and K to leading order with Wick's theorem
  under the Gaussian measure of H₀. Average (2.7) conditionally, close it
  by evaluating R and K at the conditional mean, and integrate the
  resulting integro-differential equation (4.10).

## Concepts

- **Phase variable**: a function A on phase space. SᵗA is its value along
  the flow.
- **Liouvillian**: L = Σᵢ Rᵢ ∂/∂uᵢ, the generator of Sᵗ = "e^{tL}".
- **Orthogonal dynamics**: S⊥ᵗ, the evolution generated by (I − P)L. It
  keeps functions orthogonal to the span of functions of A.
- **Memory function**: K(t, A) = E[LS⊥ᵗF | A], a function of A that varies
  in t.
- **Optimal prediction**: estimating the mean future of the resolved
  variables, E[SᵗA | A], under a prior invariant measure. "First-order" is
  its Markovian approximation (3.1). "Optimal" refers to (2.3): R is the
  best mean-square function of A for the instantaneous rate.
- **Renormalized Hamiltonian**: 𝓗(Q, P) = −log∫e^{−H} over the unresolved
  pairs, "minus the logarithm of the weighted phase space volume
  constrained by the known values".
- **Temperature**: T in the canonical density, which "specifies the
  variance of the samples".

## Connections

It rests on Mori (1965) and Zwanzig's nonlinear generalization (1980),
following Evans and Morriss's presentation of the Dyson formula. It
continues Chorin, Kast and Kupferman's first-order optimal prediction
(1998, 1999), Chorin, Kupferman and Levy's nonlinear Schrödinger study
(LBNL-44105), and Hald's rigorous analysis (1999), which is cited but not
reproduced. The "later work" it promises, on memory truncation with more
resolved variables and on sampling-based higher-order schemes, is the
programme of Chorin, Hald and Kupferman's "Optimal prediction with memory"
(LIT-tmple6xy, registered unread). Parish and Duraisamy (LIT-tmpvihtb,
unread) apply the formalism to large-eddy closure.

## Bearing on the record

This is the record's first reading of Mori–Zwanzig. What follows the first
item is the record's own derivation, not the paper's. The scripts are in
the session scratchpad. None of it is filed as a THEORY.

- **QUESTION-tmpxapb2, the general form.** A3's
  Ż = F(Z) + ∫K(t − s, Z_s) ds + η is (2.7). The paper fixes three things
  A3 left open. The projection is conditional expectation under an
  invariant measure, so it is not arbitrary once the measure and A are
  chosen. The noise is a deterministic function of the unresolved initial
  state, uncorrelated with functions of A(u) but not independent of them.
  And the kernel K(s, A) is in general nonlinear in A. A3's caution holds
  within the paper: change A or μ⁰, and R, K and F all change.
- **Fluctuation–dissipation (the record's derivation).** The paper relates
  K to the noise only by the definition K = E[LS⊥ˢF|A]. A sharper relation
  follows from its own assumption of invariance. If μ⁰ is invariant, L is
  skew-adjoint on L²(μ⁰), because E[fLg] + E[gLf] = E[L(fg)] =
  (d/dt)E[Sᵗ(fg)] = 0 at t = 0. Take G = S⊥ˢF, which is orthogonal to the
  functions of A for every s, and any test function h. Then
  E[h(A)K(s, A)] = E[hLG] = −E[G·Lh(A)] = −E[G ∇h(A)·F], since
  ∇h·R(A) is a function of A. With Mori's linear projection this gives
  K(s) = −E[S⊥ˢF Fᵀ] C_A⁻¹. That is the second fluctuation–dissipation
  theorem, checked numerically to 10⁻¹⁵ for a random skew-symmetric linear
  flow with m = 2 and n = 6, together with the Volterra form of (2.7). With
  h = Aᵢ it gives E[Aᵢ K_j(0, A)] = −E[Fᵢ F_j] for the nonlinear
  projection too.
- **So, in the paper's setting, memory and noise vanish together (the
  record's).** By the last identity, K(0, ·) ≡ 0 forces E[|F|²] = 0, and
  F = 0 makes K ≡ 0 and the noise ≡ 0. For a deterministic flow with an
  invariant measure, then: **zero memory ⇔ zero noise ⇔ F = 0 ⇔
  dA/dt = R(A) exactly**, which is closure. Whenever first-order optimal
  prediction is not exact, the memory kernel is nonzero. For a linear flow
  ẋ = Jx and A = Lx, F = 0 is LJ = BL. That is Shpak et al.'s ĀQ = QA
  (NOTE-tmpl2r9w) and the continuous-time form of THEORY-733's L A = B L.
  This was checked for an invariant 2-plane of a skew J (|F| ~ 10⁻¹⁵).
- **THEORY-733 and THEORY-257: MZ memory against dynamical independence in
  a linear Gaussian VAR(1) (the record's).** Barnett and Seth's setting is
  stochastic and in discrete time, so the paper's FDT does not carry over.
  Apply the discrete Dyson identity
  𝒦^{t+1} = Σ_{j=0}^{t} 𝒦^{t−j} P𝒦(Q𝒦)^j + (Q𝒦)^{t+1} to the transition
  operator 𝒦g(x) = E[g(X_{t+1}) | X_t = x]. Take P = E[· | Y] under the
  stationary law N(0, Π), with Y = LX and Q = I − P. On linear observables,
  𝒦 acts as c ↦ Aᵀc, and P is the Π-orthogonal projection onto row(L),
  which for Gaussians is the full conditional expectation. In a
  Π-orthonormal basis with row(L) first, write 𝒦 = [[K₁₁, K₁₂], [K₂₁, K₂₂]].
  Then the Markov term is K₁₁ = C_Y(1)C_Y(0)⁻¹, the memory kernels are
  M_j = K₁₂K₂₂^{j−1}K₂₁ for j ≥ 1, and the first orthogonal-dynamics term
  is K₂₁. The Volterra identity was checked to 10⁻¹⁷. Then:
  1. **Exact dynamical independence ⇔ K₂₁ = 0.** Q𝒦P = 0 iff Aᵀ maps
     row(L) into itself, iff LA = BL, which is THEORY-733's criterion. In
     words, E[Y_{t+1} | X_t] is a function of Y_t. In the MZ split, DI is
     the vanishing of the noise from the unresolved initial state, not of
     the memory.
  2. **DI ⇒ zero memory.** Every M_j contains K₂₁. Checked: a left
     eigenvector of A gives |K₂₁|, max|M_j| and T(X → Y) all ~ 10⁻¹⁶.
  3. **Zero memory does not imply DI.** Zero memory ⇔
     C_Y(t) = K₁₁ᵗ C_Y(0) for all t ⇔ Y is Markov in its own filtration.
     Counterexample: A = [[0.5, 0.4], [0, 0.3]], Σ = I − AAᵀ (so Π = I),
     L = e₁. Then C_Y(t) = 0.5ᵗ exactly and every M_j = 0, yet
     T(X → Y) = ½log((1 − a₁₁²)/(1 − a₁₁² − a₁₂²)) = 0.120 nats, in closed
     form and numerically. In the Π-orthonormal frame, K₂₁ is the inward
     leg (the rest driving Y), K₁₂ the outward leg, and the memory is the
     round trip Y → rest → Y. DI asks only that the inward leg vanish,
     which matches THEORY-257's reading ("dynamical independence asks only
     for none coming in"). Zero memory needs the round trip to vanish,
     which an absent outward leg also achieves. The legs are measured in
     Π-whitened coordinates, not in raw entries of A. Zero memory is
     non-generic: none of 200 random 3-dimensional models with m = 1 had
     it.
  4. **For VAR(p ≥ 2), DI does not imply zero memory either**, with the
     projection onto the current Y_t. In a VAR(2) where x₁ is an undriven
     AR(2), T(X → Y) = 0 and max|M_j| = 0.35. So A5's caution, that
     non-Markovianity is not a failure of dynamical independence, is right
     for p ≥ 2. For p = 1 it is half right: there nonzero memory does
     imply dependence.
  5. **QUESTION-tmpxapb2's own example shows item 3 in continuous time.**
     In ẋ = −ax + by, ẏ = cx − dy, K = bc e^{−dt}. With c = 0 and b ≠ 0
     the memory vanishes, but x is not closed: b e^{−dt} y(0) remains. That
     system is dissipative and has no invariant measure with a
     skew-adjoint L, which is why the paper's setting excludes it.
  6. **Reversible VAR(1) restores the paper's picture.** If the chain
     satisfies detailed balance (AΠ symmetric), 𝒦 is Π-self-adjoint, so
     K₁₂ = K₂₁ᵀ and M₁ = K₂₁ᵀK₂₁, with tr M₁ = ‖K₂₁‖²_F. That is the
     discrete counterpart of the FDT. There, M₁ = 0 forces K₂₁ = 0: zero
     memory ⇔ exact dynamical independence. Checked on three random
     reversible models with n = 5 and m = 2 (|K₁₂ − K₂₁ᵀ| ~ 10⁻¹⁵).
     Counterexample 3 is not reversible. The gap between memory and
     dependence is a feature of irreversible (driven, one-way) coupling.

  The precise relation for a stable VAR(1) with Gaussian innovations and a
  linear coarse-graining, by derivation and numpy check: **exact dynamical
  independence ⇔ the first MZ orthogonal-dynamics term Q𝒦P vanishes ⇒
  the memory kernel vanishes; the converse fails on a non-generic set; and
  for p ≥ 2, or with the projection onto the instantaneous Y, the two
  properties are logically independent. For a reversible VAR(1), zero
  memory and DI coincide.** In the paper's own setting, a
  deterministic flow with an invariant measure, memory, noise and
  non-closure vanish together.
- **QUESTION-tmpxapb2, augmentation (the record's, linear class).** There
  are two distinct "Markovian augmentations", and they differ in size.
  - Making Y's own law Markov needs k = rank of the Hankel matrix of
    (M_j) memory coordinates. That is the minimal realization of
    (K₂₂, K₂₁, K₁₂).
  - Making the augmented variable exactly dynamically independent needs
    the Krylov space of Aᵀ on row(L), that is, m plus the reachable
    dimension of (K₂₂, K₂₁).
  - Both are exact, and both are generically the whole eliminated
    dimension. A random case with n = 5 and m = 1 gave Hankel rank 4 and
    Krylov dimension 5. A driven chain gave 2 and 3, and the Krylov
    augmentation was checked to have T = 0. In counterexample 3 they are
    0 and 2.
  - So "add memory coordinates" answers the question only if it says
    which closure is meant. Controlled-error truncation, the question's
    real demand, is not touched by this paper.
- **QUESTION-tmpt64jh (a by-product, the record's).** In a VAR(1) whose block Y
  receives coupling A_{YR} from the rest:
  T(X → Y) ≤ ½ log det(I + (LΣLᵀ)⁻¹ A_{YR} Cov(R_t | Y_t) A_{YR}ᵀ). The
  reason is that conditioning on Y's whole past does no worse than
  conditioning on Y_t. So the dynamical dependence is O(ε²) in the inward
  coupling, whatever the outward coupling. Checked: T/ε² ≈ 0.53 for ε from
  0.2 to 0.025, under the bound throughout, with correlated noise. This
  answers the forward half of the question for linear Gaussian VAR(1)
  with Cov(R | Y) bounded. The MZ memory in the same runs is O(ε), not
  O(ε²), so memory is the coarser signal.
- **CLAIM-327 and CLAIM-331.** Reading 3 says how a variable members read
  from the past can be closed without being Markov in its own history, or
  Markov without being closed. The paper says nothing about timescales
  beyond "short times", "m not too small" and "low temperature". It gives
  no support to the idea that slower variables have less memory.
- **CLAIM-tmpkoi6k and THEORY-tmpj32n2.** They are consistent with readings 1 and
  2. An exactly closed collective mode, K₂₁ = 0, carries no MZ memory and
  no noise from the eliminated state. Only its own innovation Lε remains.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **C4 is overstated.** (2.3) makes R(A) = E[LA|A] the best mean-square
  function of A for the instantaneous rate LA. It does not make the
  integrated trajectory v(t) the best m-dimensional Markovian predictor of
  SᵗA. Counterexample, checked analytically and by Monte Carlo with
  2 × 10⁵ samples: a harmonic oscillator q' = p, p' = −q, with canonical
  measure N(0, I) and A = q. Then R(q) = E[p|q] = 0, so first-order
  optimal prediction gives v(t) = q₀. Its mean-square error is
  2 − 2cos t, which is 4 at t = π. The one-equation Markovian model
  v' = −cv with c large has error close to 1 at t = π. At t = 0.5 the
  best c ≈ 0.26 beats it too: 0.230 against 0.245. The claim holds at
  t → 0⁺ only.
- **Invariance is assumed more widely than it is used.** The Dyson
  formula and (2.7) are algebraic identities for any projection P,
  including conditional expectation under a non-invariant μ⁰. Invariance
  matters for reading E[SᵗA | A] as a prediction under the prior, for the
  noise's statistics, and for the fluctuation–dissipation relation above,
  which the paper does not state.
- **No validity criterion for the Markovian approximation.** "Conditions
  under which this is legitimate are discussed in [1–5]." Here the only
  conditions are short times, enough resolved modes and low temperature.
  The FDT above implies that K(0) is the size of the noise covariance, so
  memory is small exactly when F is. The paper does not say this.
- **The demonstration in §4 is thin.** It uses m = 0 only, a perturbation
  series the authors say is "not likely to be accurate for long times", a
  Markovian term "not likely to be accurate when m = 0", a mean-field
  closure in (4.10), and kernels cut off at t = 0.9, a time "chosen so as
  to produce a reasonable decay". The cut-off is fitted to the outcome it
  is then said to reproduce. Figure 1 shows the decay but not a faithful
  mean after t ≈ 2.
- **The base Gaussian measure is improper in the k = 0 mode.** ω₀ = 0, so
  the stated conditional variance (πω_k)⁻¹T is infinite there. Conditioning
  on u₀ when m = 0 makes this harmless for (4.11), but it is not remarked.
- **Typos in this copy.** "P = (P₁, …, Q_m)" in §3. "No general way of
  solving equation (2.6)", which should be (2.5). "From equation (4.8) it
  follows", which reads as (2.6). The print version may have corrected
  them.
- **Formal throughout.** No existence for S⊥ᵗ, no domain for L, and no
  treatment of n = ∞, which is deferred to Hald (1999).
- **Copy.** The authors' preprint, not the PNAS typeset text.

## Open questions

- When is the memory kernel short enough that a truncation, or a few
  augmented coordinates, gives bounded error over a stated horizon? The
  paper promises "later work" (see LIT-tmple6xy). For the linear class,
  balanced truncation of (K₂₂, K₂₁, K₁₂) would give an error bound in
  terms of Hankel singular values. That would answer QUESTION-tmpxapb2's
  demand for k and the error in terms of the eliminated spectrum.
- Does the record's VAR(1) relation (DI ⇔ Q𝒦P = 0 ⇒ zero memory) extend
  to near-independence? Is the dynamical dependence bounded by a norm of
  the orthogonal-dynamics term, as the O(ε²) bound suggests, while the
  memory norm only bounds it from one side?
- For an irreversible VAR(1), can the gap between zero memory and
  dynamical independence be bounded by the antisymmetric part of 𝒦 in the
  Π-whitened frame, which measures one-way coupling? Item 6 settles only
  the reversible end.
