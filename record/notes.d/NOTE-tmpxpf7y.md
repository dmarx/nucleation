---
status: Read
paper: LIT-tmp8mp1c
title: 'Yang & Abanin — Integrals of motion as slow modes'
version: 1
history:
- version: 1
  date: '2026-11-02'
  note: >-
    Read in full from arXiv:2506.02970v3 (26 August 2025), 19 pp.: the
    abstract, §§I–V (pp. 1–9), the acknowledgements, the reference list
    (pp. 9–12) and the supplementary material, Appendices A–G (pp. 12–19).
    Text was extracted with pypdf; the figures came through as captions
    and axis debris only, so every statement below about a figure is the
    caption's or the text's, not a reading of the plot. Equations were
    reconstructed from the extraction and checked against the equations
    they must agree with. The published PRB version was not compared.
    Nothing was skipped.
date: '2026-11-02'
summary: >-
  Under weak local noise an operator decays at a rate set by its size;
  chaotic dynamics makes generic operators grow, while small-sized
  integrals of motion do not, so they are the Lindbladian's slow modes.
  Exact diagonalization at L ≤ 9 bears this out for Ising and Heisenberg
  chains and finds approximate conservation laws, including some not put
  in by hand. The large-L footing is a perturbative argument through a gap
  of order min(γL, √(v_Bγ)), which the authors say hydrodynamic modes may
  close. Stronger noise reorders the slow modes in favour of approximate
  conservation laws.
---
<!-- inactive-ok-file: CLAIM-478 THEORY-tmpull8q — Proposed; the entries the reading bears on, cited as open -->

# NOTE-tmpxpf7y: Yang & Abanin — Integrals of motion as slow modes

## Contribution

It shows that the slowest eigenoperators of a weakly dissipative many-body
Lindbladian are, in the models studied, the small-sized integrals of motion
(IOMs) of the underlying Hamiltonian, exact and approximate, and gives the
mechanism: noise punishes size, and chaotic dynamics grows everything
except what it conserves. That turns the Lindbladian's low-lying spectrum
into a tool for finding conservation laws, and into a proposed measure of
how chaotic a model is (§III D). The authors place it "within the research
theme of identifying symmetries using superoperators" (p. 8).

## Key insight

Two facts combine (§II, pp. 2–3). Local noise makes an operator's norm decay
at a rate proportional to the number of sites it acts on: under depolarizing
noise, d‖O‖/dt = −γS(O)‖O‖ (eq. 5). And under chaotic unitary dynamics an
operator's size grows, typically ballistically, S(O(t)) ∼ v_B t, so its norm
falls superexponentially, ∼ e^{−γv_B t²/2} (p. 2). A conserved quantity
does not grow, so it decays only as e^{−γSt}. Decompose any operator as
O = O∥ + O⊥, its projection onto the IOMs and the rest: O⊥ dies fast, and
"O(t) ≈ O∥(t). It is in this sense that we call IOMs O∥ the slow modes"
(p. 3). Without noise nothing decays and the ranking does not exist; without
operator growth the conserved quantities would not stand out.

## Assumptions

- **Markovian, local noise.** Heisenberg-picture Lindbladian
  L†[O] = i[H, O] + Σⱼ γⱼ(Lⱼ†OLⱼ − ½{Lⱼ†Lⱼ, O}) (eq. 1), with local jump
  operators, "justified provided noise at different sites is uncorrelated,
  and a Markovian approximation can be applied" (p. 1).
- **Depolarizing noise by default**: jump operators Xᵢ, Yᵢ, Zᵢ, each at
  rate γ/4, so D[P] = −γS(P)P for a Pauli string P (p. 2). Dephasing–decay
  noise is checked in Appendix B.
- **Weak noise**: γ = 10⁻³ in the main numerics; γ = 0.1 in Figs. 6(b,c),
  8, 9.
- **Small systems**: exact diagonalization of the superoperator, L ≤ 9,
  periodic boundaries, zero-momentum sector (p. 3; Appendix C argues no
  slow modes live elsewhere).
- **Size, not locality.** "Small-sized" means few non-identity sites per
  Pauli string, weighted (eq. 6). Bi-local sums like Σ_{i<j}ZᵢZⱼ count as
  small, and products of small-sized operators stay small (p. 2), so
  powers of H count as IOMs.
- **Ballistic operator growth** for the perturbative argument (eq. 21),
  i.e. fully chaotic behaviour of the complement; relaxed in §IV's second
  comment to "some form of operator growth" (p. 8).

## Key results

- **First-order correspondence (§III, p. 3).** If [H, Q] = 0, there is an
  eigenoperator V ≈ Q with λ ≈ (Q|D[Q])/‖Q‖² = −γS(Q). Conversely, a
  Hermitian eigenoperator with real λ has S = |Re λ|/γ, and
  ‖[H, V]‖² = γ²(⟨S²⟩_V − ⟨S⟩²_V) (Appendix A, eq. A7), so a low-lying
  eigenoperator is at least an approximate IOM, with ‖[H, V]‖ = O(1) × γ
  for "reasonable" size distributions.
- **Mixed-field Ising, J = 1, hx = 1.1, hz = 0.7, L = 7 (Fig. 2a).** The
  model is thermalizing with no local IOM but H; the first three
  eigenoperators are combinations of I, H, H².
- **Transverse-field Ising (Fig. 2b,c, L = 7 and 9).** The first five
  eigenoperators are combinations of the Majorana-bilinear IOMs Aₘ, Bₘ
  (eqs. 9–11; derived in full in Appendix E).
- **Heisenberg chains, L = 9 (Fig. 3; Appendix G).** In the XXX model the
  known IOMs and their products "account for the first 25 eigenoperators"
  (p. 5). In XXZ the listed IOMs are not enough: at Δ = 0.1 the spin
  current J = XY − YX appears, a remnant of the free-fermion XX point; at
  Δ = 1.5 an approximate S²ₓ + S²ᵧ, the SU(2) Casimir approximately
  conserved near Δ = 1; at Δ = 10 a domain-wall swap operator (Fig. 10a).
  The quasi-local IOM of XXX is not seen, perhaps because it is larger
  than size 3 (p. 19).
- **Approximate conservation laws found (§III D, Fig. 4).** For MFIM at
  hx = hz = 0.4, L = 8, the second and third eigenoperators are not powers
  of H but combinations of H and Wurtz and Polkovnikov's dressed
  particle number N (Appendix F, eq. F2).
- **A chaoticity measure (Fig. 4c).** R_Σ = Σ_{i=1}^{3}(1 − Rᵢ), the part of
  the first three eigenoperators outside span{I, H, H²}. MFIM is fully
  chaotic for hx > 1, hz ≠ 0, and not fully chaotic over large regions with
  0 < hx < 1, where no exact local IOM but H is known. The measure counts
  prethermal approximate symmetries that "the traditional measure" would
  call chaotic (p. 6).
- **Perturbation theory (§IV, eqs. 13–22).** Write L†[Q] = −γ_Q Q + ε₁J₁,
  with ε₁ ∼ γ for an exact IOM and ε₁ ∼ ‖δH‖ for an approximate one. The
  eigenoperator V = Q + V⊥ has ‖V⊥‖ ≲ |ε₁|∫₀^∞ e^{γ_V t}‖J₁(t)‖dt (eq.
  20). Under unitary dynamics the integral diverges; with dissipation and
  ballistic growth, ‖J₁(t)‖ ∼ e^{−γv_B t²/2} (v_B t < L) or e^{−γLt}
  (eq. 21), so ‖V⊥‖ ≲ ε₁/E_g^< with E_g^< ∼ min(γL, √(v_Bγ)) (eq. 22), which
  does not shrink with L and is ≫ γ for small γ and large L. Hence "we
  reasonably expect the perturbation theory to hold as long as ε ≲ γ ≪ 1"
  (p. 8). Fig. 5 checks the convergence of the integral numerically for
  MFIM with hz = 0.05, L = 9.
- **The authors' own caveat on the gap (p. 8).** Modulated energy densities
  H_k = Σₓ e^{ikx}hₓ have O(k) commutators with H, so in the Mori limit
  lim_{γ→0} lim_{L→∞} there is "a continuum of slow modes", and "the
  Mori gap must be defined in sectors that are orthogonal to all
  hydrodynamic modes, and might not exist at all".
- **Weak integrability breaking (p. 8, eq. 23).** For E_g^< < ε < E_g^>, Q
  is an approximate eigenoperator, and to lowest order its decay rate is
  −ε₁ε₂*∫₀^∞(J₂|J₁(t))dt, "consistent with" Fermi's golden rule; E_g^>
  stays finite as γ → 0.
- **Noise strength reorders the slow modes (Appendix B, Fig. 6).** An
  approximate IOM decays at roughly −λ = Aε² + Bγ, an exact one at a rate
  linear in γ. At γ = 10⁻³ in MFIM (hx = 1.5, hz = 0.1) V₃ ≈ H², V₄ ≈ A₁; at
  γ = 0.1, V₃ ≈ A₁ and V₄ ≈ H² + B₁, and the chaoticity diagram gains a
  non-chaotic region near hz = 0. The authors' gloss: "a noisy model with
  noise rate γ has similar physics with a noiseless model if we focus on a
  time scale t ≪ 1/γ … a model that looks chaotic on a long time scale may
  look less chaotic at shorter times" (p. 13).
- **Noise channel (Appendix B, Fig. 7).** With dephasing–decay noise the
  correspondence holds "albeit to some degree with a less perfect
  correspondence"; D is no longer Hermitian and the eigenoperators are no
  longer orthogonal at first order (V₁ ∥ V₂, V₄ ∥ V₅ in Fig. 7b). An
  exception: in XXX/XXZ chains with that noise, the projector onto the
  fully polarized state is a slow mode although its size scales as L,
  because both H and the noise leave that state alone (p. 14).
- **Finite size (Appendix D, Fig. 9).** The bulk of the spectrum moves to
  larger |Re λ| as L grows while the slow modes do not; IOMs larger than
  a threshold proportional to L, "around 3 to 4" here, are drowned in the
  bulk (p. 15).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Under local noise an operator's decay rate is proportional to its size; exactly γS(P) for a Pauli string under depolarizing noise | strong | eqs. 2, 5, exact; bounds for general local noise, eq. B1 |
| C2 | Each exact small-sized IOM has an eigenoperator near it with λ ≈ −γS(Q), and a low-lying Hermitian eigenoperator is an approximate IOM with ‖[H, V]‖ = O(γ) | strong (first statement, first order) / moderate (second, needs a "reasonable" size distribution) | §III argument; Appendix A |
| C3 | In the Ising and Heisenberg chains studied, the slowest eigenoperators are linear combinations of known exact and approximate small IOMs | strong at the sizes studied | exact diagonalization, L ≤ 9, Figs. 2, 3, 10 |
| C4 | The low-lying spectrum finds approximate conservation laws not supplied in advance | moderate | XXZ examples and MFIM's dressed N (Figs. 3, 4, 10a); each was identified by comparison with a candidate the authors then wrote down |
| C5 | The correspondence holds at large L, because the controlling gap is E_g^< ∼ min(γL, √(v_Bγ)), not the level spacing | weak to moderate | perturbative argument assuming ballistic operator growth (eqs. 20–22); numerical check of the integral at L = 9 (Fig. 5); qualified by the authors' hydrodynamic-mode caveat |
| C6 | R_Σ measures departure from full chaos, including approximate symmetries | weak | proposed; one phase diagram at L ≤ 9; noise-dependent (Fig. 6c) |
| C7 | Stronger noise favours approximate IOMs over exact larger ones | moderate | the Aε² + Bγ form from eq. 18, and one model at two noise strengths (Fig. 6) |
| C8 | The correspondence does not depend much on the noise channel | weak to moderate | heuristic rotation-averaging argument and one alternative channel (Fig. 7), with a named exception |

## Concepts

- **Integral of motion (IOM)** — an operator commuting with H; an
  *approximate* IOM is one whose commutator with H has small norm (p. 1).
- **Size S(O)** — the weighted mean number of non-identity sites in O's
  Pauli strings (eq. 6). Small-sized is wider than local.
- **Slow mode / low-lying eigenoperator** — an eigenoperator of L† with
  decay rate −Re λ = O(1) × γ, the factor not scaling with L (p. 3).
- **Operator growth** — the spreading of S(O(t)) under unitary dynamics,
  ballistic at butterfly velocity v_B in chaotic systems (p. 2).
- **Mori gap** — the gap of a weakly dissipative many-body Lindbladian in the
  Mori limit lim_{γ→0} lim_{L→∞}, finite where the level spacing is
  exponentially small (refs. 24, 25; p. 7).
- **Frobenius norm** — ‖O‖ = √((O|O)), with (A|B) = tr(A†B)/D; the only
  norm used (eq. 4).

## Connections

- **Mi et al. 2022** (ref. 13): Majorana zero modes found as the slowly
  decaying Pauli strings of a noisy superconducting chain; the experiment
  that suggested the method (p. 1).
- **Mori 2024; Jacoby, Huse and Gopalakrishnan 2025** (refs. 24, 25): the
  Lindbladian gap of chaotic channels at infinitesimal noise, read as the
  inverse thermalization time. The record holds neither.
- **Wurtz and Polkovnikov** (ref. 69): the dressed particle number used as
  MFIM's approximate conservation law (Appendix F).
- **Lian; Chen and Lian; Moudgalya and Motrunich** (refs. 81–83): other
  superoperator routes to conserved quantities, from entanglement
  Hamiltonians and as ground states of local superoperators. The record
  holds none of them.
- **Within the record.** THEORY-158 (LIT-773) states, for classical Markov
  generators, when an observable is exactly conserved. This paper's
  quantities are conserved by the Hamiltonian part only, and under the
  full generator are slow, not conserved. Zurek's einselection (NOTE-1229)
  has a related shape: what the environment leaves alone persists. Here
  the environment acts on every site alike, and what persists is what the
  system's own dynamics keeps small.

## Bearing on the record

- **CLAIM-478: a mechanism of slowness its list lacks in this form.** The
  claim's "Not one mechanism" names near-decomposability, slaving,
  metastability, conservation and transport, and renormalization (A13),
  with broken symmetry (Toner–Tu, NOTE-1228) and dissipative coupling
  (CLAIM-481) added since. This paper's route is conservation, but the
  separation is made by two things together: weak local noise, which
  punishes size, and the system's own chaos, which grows everything it
  does not conserve. The fast side's rate is set by the chaos: the gap is
  of order √(v_Bγ), so the ratio to the slow rates (∼ γ) grows like
  √(v_B/γ) as the noise weakens (eq. 22). The H_k family is A13's transport
  branch arising in the same setting (p. 8). As for "separation makes a
  constraint": after O⊥ has decayed, O(t) ≈ O∥(t) (Fig. 1d), so over the
  window between the two rates the conserved sector is all that remains of
  an observable. That supports the first half. It does not bear on
  defeater (a), since an exact conservation law is the limit of slowness,
  not a constraint that works without it, or on the second half.
- **CLAIM-331: slowness as a mark, relative to an environment and a
  measure of size.** Without noise every eigenoperator of i[H, ·] has zero
  decay rate and slowness ranks nothing; the ranking exists only once a
  weak environment and a notion of size, fixed by the tensor-product
  split into sites, are given. And the ranking moves with the
  environment's strength: at γ = 0.1 an approximate IOM overtakes the exact
  H² (Appendix B, Fig. 6). The authors' "a model that looks chaotic on a
  long time scale may look less chaotic at shorter times" is the claim's
  point that slowness marks and does not define, in a case where what is
  marked depends on the observation window.
- **CLAIM-394: a non-reversible generator where slowest-decaying and
  eigen-directions nearly coincide, and where they come apart.** i[H, ·] is
  anti-Hermitian and depolarizing D Hermitian, so L† is not self-adjoint,
  yet the small IOM Q and the eigenoperator V near it agree to
  ‖V⊥‖ ≲ ε/E_g^<, small when ε ≲ γ ≪ 1 (§IV). With dephasing–decay noise D
  is not Hermitian either, and the eigenoperators lose orthogonality
  (Fig. 7b). CLAIM-394's linear Gaussian setting is not this one, so
  this is a parallel, not a test.
- **THEORY-158 and THEORY-160**: complementary, as above; nothing in them
  is changed.
- **No instruction for machine-learning practice.**
- **Two THEORYs filed:** THEORY-tmpggrkf (Active), what the diagonalization
  showed at the sizes studied; THEORY-tmpull8q (Proposed), the large-L
  claim.

## Limitations

- **Small systems.** Every spectrum is at L ≤ 9, and IOMs of size above
  about 3–4 cannot be seen (Appendix D). The large-L picture is argued,
  not computed.
- **Identification is by comparison.** Each slow mode is matched to a
  candidate IOM by overlap; the "new" approximate IOMs were recognized
  against operators the authors then wrote down (J, S²ₓ + S²ᵧ, N, H_D.W.).
  The method finds the subspace, not the name.
- **The gap argument assumes ballistic operator growth**, i.e. a chaotic
  complement, and the authors' own hydrodynamic caveat may remove the gap
  altogether (p. 8). In integrable models, where many tests are run, the
  growth assumption is not the obvious one; the paper does not say how the
  argument covers them beyond the second comment of §IV.
- **The chaoticity measure depends on γ** (Fig. 6c) and on the choice of
  three eigenoperators.
- **Depolarizing noise is the main case**, chosen for "mathematical appeal"
  and "not expected to characterize the actual dissipation in most
  realistic systems" (p. 14).
- The experimental protocol (shadow tomography of O(t), p. 9) is left to
  future work. The acknowledgements say ChatGPT was used to improve the
  manuscript.

## Open questions

- Does the correspondence hold at large L in chaotic models where the IOM
  is not an exact eigenoperator (H in MFIM)? Tensor-network
  diagonalization or long-time evolution of the Lindbladian, which the
  authors propose (pp. 8–9), would say (THEORY-tmpull8q).
- Is there a Mori gap at all once hydrodynamic modes are counted (p. 8)?
- Can the low-lying spectrum name an approximate conservation law nobody
  has written down, rather than confirm one?
