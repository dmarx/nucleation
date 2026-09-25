---
number: 3
status: Read
formerly:
- NOTE-tmp6ess1
paper: LIT-001
title: 'QM as stochastic optimization on spacetimes'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text, 8 PDF pp. (pp. 1–7 article incl. Conclusion and
    Discussion, 29 references, author contributions; p. 8 licence only).
    Nothing skipped. PDF from nature.com (open access, CC BY 4.0) saved as
    raw4/35.pdf; text extracted with PyMuPDF (pdftotext unavailable). The
    PDF extraction scrambles the equations, so every display and inline
    equation, Eqs. (1)–(43), was re-read from the LaTeX source in the
    nature.com HTML (raw4/35.html). The algebra of Eqs. (7), (17)–(27) and
    (34)–(36), (43) was checked by hand; results of those checks are marked
    "(reader's check)".). Upgraded from `Skimmed` to `Read`: the claims
    table, assumptions and results are new, and the skim is corrected where
    the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper derives a Stueckelberg-type equation i∂φ/∂τ = (1/2m)□φ − Vφ
  (Eq. 36) from an HJB equation, but only after putting the imaginary unit
  in twice by hand. The first i is a factor √g = i multiplying the
  Lagrangian; standard relativity uses √(−g) = 1. The second is a complex
  "variance" σ² = i/m (Eq. 29), chosen so that the Hopf–Cole substitution
  J = log φ linearizes the equation. The linearization itself is the
  standard λ = σ²·(control cost) condition. The Schrödinger equation (Eq.
  43) then comes from c → ∞ plus complex conjugation. The Dirac equation
  is not derived, and the "Klein–Gordon equation" (Eq. 40) has 2mV where
  m² should be.
---

<!-- inactive-ok-file: LIT-001 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-003: QM as stochastic optimization on spacetimes

## Contribution

The paper puts two derivations in sequence. The first is a textbook stochastic-control derivation: an HJB equation for the expected classical action under a Brownian perturbation. The second is a relativistic version of it. That version adds a diffusion in the time coordinate, multiplies the Lagrangian by i (taken as √det g), and sets the noise variance to i/m. The HJB equation then turns under J = log φ into a proper-time Schrödinger equation with a d'Alembertian: the Stueckelberg (1941) form, time-reversed. It is new to present the i as coming from a volume-form factor. The paper does not show that this works, because that factor is not the standard one. The linearizing step is the standard Hopf–Cole / path-integral-control condition, applied with complex coefficients.

## Key insight

The quantity to track is the coefficient ratio in the HJB equation. The equation has the form ∂J − (1/2M)(∇J)² + ½σ²□J + … = 0. The substitution J = −λ log φ removes the quadratic term exactly when λ = Mσ² (reader's check; the standard condition). Take a real mass M = m and real σ². Then the substitution gives a real, heat-type (imaginary-time) equation. That is Feynman–Kac / Kappen path-integral control, a standard result not from the paper. A real-time Schrödinger equation needs the ratio to be imaginary. The paper gets that by setting M = im (the √g = i factor) and choosing σ² = i/m to match. So the paper does not explain the i: it moves it into a volume-form convention and a complex variance.

## Assumptions

- **Classical start (Eqs. 2–4).** A particle follows the diffusion dX_i = v_i ds + σ̃_i dW_i (i = 1,2,3), where W_i are independent standard Wiener processes. "Nature" minimizes E_tx ∫_t^T (½ m v² − V(X)) ds over Markov feedback velocities v(s, x). ħ = 1.
- **The HJB equation (Eq. 7)** is ∂J/∂t − V − (1/2m)(∇J)² + ½σ²ΔJ = 0, with optimal v = −(1/m)∇J (Eq. 8), and the paper sets σ² = σ̃₁² + σ̃₂² + σ̃₃². The reader's check finds this correct for isotropic noise with σ² equal to the per-component variance. Itô's formula gives the generator ½Σσ̃_i²∂_i², not ½(Σσ̃_i²)Δ, so defining σ² as the sum is off by a factor of 3 in the isotropic case and wrong in the anisotropic case.
- **Time diffuses too (Eqs. 10–11).** d(cX₀) = u₀ ds + σ̃₀ dW₀ and dX_i = u_i ds + σ̃_i dW_i, where s is "the proper time". X₀ is coordinate time. The paper never shows that s is the proper time of the diffusing path.
- **Volume form (Eq. 12).** dV = √g dcx₀dx₁dx₂dx₃, with Minkowski g_ij = diag(−1,1,1,1) (Eq. 13), so "√g = i". **This is the load-bearing assumption.** The standard invariant measure uses √(−g), which is real (standard result).
- **The action is a spacetime integral (Eqs. 15–16).** S = ∫_{M⁴}∫_τ^T (½ m g_ij u^i u^j − V) ds p(x, s) · i dcx₀dx₁dx₂dx₃, with the transition density p taken as a density against dV. This effectively replaces the Lagrangian with 𝓛 = i(½ m g_{μν}u^μu^ν − V) (after Eq. 17).
- **Hamiltonian by stationarity.** H = sup_u(−∇_μJ u^μ − 𝓛) (Eq. 17), with the optimum found from ∂H/∂u^μ = 0 (Eq. 18). The "sup" of a complex quantity is not defined, so only stationarity is actually used.
- **Metric sum of variances (Eq. 30).** The HJB diffusion term is ½σ²□J with σ² = −σ̃₀² + σ̃₁² + σ̃₂² + σ̃₃². The paper cites Fleming–Soner. The reader's check disagrees. With independent noises, Itô gives ½(σ̃₀²∂₀² + Σσ̃_i²∂_i²), which equals ½σ²□ only if σ̃₀² = −σ² and σ̃_i² = σ² for every i. The generator does not collapse a variance vector into one metric-signed sum.
- **Linearity demanded (Eq. 29).** σ² = i/m = −1/(im) is chosen "to couple the scaling factor" so that the HJB equation becomes linear. This is imposed, not derived.
- **Complex noise (Eqs. 31–33).** The paper sets σ̃₁² + σ̃₂² + σ̃₃² = R ∈ ℝ and σ̃₀² = R + 1/(im), so σ̃₀ = √(R + 1/(im)) is complex. The paper calls this "complex time", "a mathematical consequence and requirement to linearise the HJB equation" (p. 5). A Wiener process scaled by a complex constant is not a real diffusion. The transition densities of Eqs. (5)–(6), and the expectation defining S, therefore have no stated probabilistic meaning.
- **Hopf–Cole.** J = log φ (above Eq. 35). This needs φ ≠ 0 and a branch choice for log φ. The paper does not discuss either.
- **Proper-time substitution (Eq. 37).** dτ = √(1 − v²/c²) dt is used to replace ∂_τ with γ∂_t inside a field equation. Here v, a particle velocity, is treated as a constant parameter of the field.
- **Nonrelativistic limit.** c → ∞, so that τ → t and "the first term of the d'Alembertian goes to zero" (before Eq. 42).

## Key results

- **Eq. (24):** H(u*) = (1/2im)∇_μJ∇^μJ + iV(x), with u^μ = −(1/im)∇^μJ (Eq. 21). The reader's check confirms this algebra given the i-multiplied Lagrangian.
- **Eq. (25), the relativistic HJB equation:** ∂J/∂τ − iV − (1/2im)∇_μJ∇^μJ + ½σ²∇_μ∇^μJ = 0.
- **Eqs. (26)–(27):** the same equation written as ∂J/∂τ + i(K − V) + ½σ²□J = 0, with K = P_μP^μ/2m and P_μ = i∇_μJ. The reader's check finds a sign error here. With P_μ = i∇_μJ, K = −∇_μJ∇^μJ/2m, so −(1/2im)∇J·∇J = −iK and Eq. (26) should read −i(K + V). That form is consistent with Eq. (24) and with the paper's own sentence that the Hamiltonian is "kinetic energy … plus the potential energy".
- **"Operator substitution" (after Eq. 27):** m u_μ = i∇_μJ. The paper says this explains the postulate p → −i∇ ("the sign is reverted" because the HJB equation runs backward). This is an identification of symbols, not a derivation of an operator correspondence.
- **Eq. (34):** with σ² = i/m, ∂J/∂τ − iV − (1/2im)(∇_μJ∇^μJ + ∇_μ∇^μJ) = 0.
- **Eqs. (35)–(36):** J = log φ gives the linear equation i ∂φ/∂τ = (1/2m)□φ − Vφ. The reader's check confirms it: □ log φ + (∇ log φ)² = □φ/φ. The paper calls this the "(time-reversed) Stueckelberg wave equation".
- **Eqs. (38)–(39):** substituting ∂_τ = γ∂_t gives (1/2m)□φ − iγ∂φ/∂t − Vφ = 0, called a Telegrapher's equation. The concluding section more accurately calls it an "analytically continued Telegrapher's equation", since the first-order-in-time coefficient is imaginary.
- **Eq. (40):** setting ∂φ/∂τ = 0 gives □φ − 2mVφ = 0, called "the Klein-Gordon equation … manifestly Lorentz-covariant". It is KG form only if 2mV = m² (outside the paper: the free KG equation in this signature and these units is □φ − m²φ = 0). V is also not a Lorentz scalar unless stipulated; the paper stipulates it (after Eq. 16).
- **Eqs. (42)–(43):** as c → ∞, i∂_tφ = (1/2m)Δφ − Vφ (time-reversed Schrödinger), so φ* satisfies i∂_tφ* = −(1/2m)Δφ* + Vφ*. The reader's check confirms the conjugation step for real V.
- **Born rule (end of §"Obtaining the Schrödinger equation…"):** writing J = a + ib gives φφ* = e^{2a}, "the Born rule". This identity is trivial. The paper does not show that e^{2a} is the density of any process: no Fokker–Planck or continuity equation is derived.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The HJB equation for min E∫(½mv² − V)ds under dX = v ds + σ̃dW is Eq. (7), with v = −∇J/m | strong | Standard result (Fleming–Soner, ref. 11). Correct up to the σ² = Σσ̃_i² definition (reader's check). |
| C2 | The imaginary unit of QM comes from the invariant volume form on Minkowski spacetime, √g = i | weak | Assertion (Eqs. 12–16). It rests on √g rather than the standard √(−g), and a constant factor on a complex objective is not an optimization. |
| C3 | Coordinate invariance plus a demand of linearity yields the Stueckelberg equation, Eq. (36) | moderate for the algebra, weak for the "yields" | Hand-checkable derivation from Eqs. 25–35. But linearity is imposed by choosing σ² = i/m. The □ in Eq. 25 needs per-component variances the paper does not have (Eq. 30 vs Itô), and Eq. 26 has a sign error. |
| C4 | The linearizing choice σ² = i/m makes the time-coordinate noise complex ("complex time") | strong as a consequence | Eqs. 31–33. The paper states it openly, but does not note that it removes the probabilistic interpretation of Eqs. 5–6. |
| C5 | Stueckelberg reduces to a Telegrapher's equation (Eq. 39), which is "the missing link" to Dirac | weak | Formal substitution ∂_τ = γ∂_t with a particle velocity v inside a field equation. The Dirac equation is not derived, only referred to ref. 19. |
| C6 | The Klein–Gordon equation is the stationary (∂_τ = 0) case, Eq. (40) | weak | Eq. 40 is □φ = 2mVφ, not □φ = m²φ. The identification is unstated. |
| C7 | The Schrödinger equation follows in the nonrelativistic limit (Eq. 43) | moderate | Formal c → ∞ limit plus conjugation, both correct given Eq. 36. No rest-mass phase is factored out and no error control is given. |
| C8 | The momentum operator substitution is "derived … in a meaningful way" | weak | Identification m u_μ = i∇_μJ (after Eq. 27) of a function gradient, not an operator rule. |
| C9 | The Born rule is tied to the real part of the minimal expected action, p = φφ* = e^{2a} | weak | Algebraic identity only. No density of the process is computed. |
| C10 | The spacetime model is causal (finite propagation speed) and "superior to canonical stochastic control models in R³" | weak | Assertion citing ref. 20. No analysis of Eq. 36 or 39 is given. |
| C11 | The results do not support the PBR theorem's thesis, and QM is a statistical theory of a particle driven by a random spacetime force | weak | Assertion "in line with" Rizzi (ref. 1). There is no argument, and with a complex σ̃₀ the "random force" is not a real stochastic process. |
| C12 | (Abstract) "the classical relativistic and nonrelativistic equations of quantum mechanics can be derived in a straightforward manner" | weak | The body gives the Schrödinger equation and a KG-form equation with 2mV. There is no Dirac derivation, no spin, and no many-body case. |

## Method

1. Take the linear-quadratic stochastic control problem of Eq. (4) and write its HJB equation, Eq. (7).
2. Promote it to four dimensions (Eqs. 10–11): all four coordinates diffuse, indexed by the "proper time" s.
3. Require the expectation to be an invariant spacetime integral with dV = √g d⁴x. Set √g = i, which multiplies the Lagrangian by i (Eq. 16).
4. Build the Hamiltonian by stationarity (Eqs. 17–24) and write the HJB equation, Eq. (25), with □ as the second-order operator.
5. Choose σ² = i/m (Eq. 29) and split it as −σ̃₀² + R (Eqs. 30–33).
6. Apply J = log φ, giving Eqs. (35)–(36).
7. Substitute dτ = γ⁻¹dt (Eq. 37) to get Eq. (39), and set ∂_τ = 0 to get Eq. (40).
8. Take c → ∞ and conjugate, giving Eqs. (42)–(43).

## Concepts

- **Value function J(x, τ):** the minimal expected action. It is real in §"Stochastic Classical Mechanics" and complex (J = a + ib) from Eq. (16) on.
- **σ² (the paper's usage):** the scalar coefficient of the Laplacian or d'Alembertian in the HJB equation, *defined* as a metric-signed sum of per-coordinate variances (Eq. 30). This is not the standard Itô generator coefficient.
- **"Complex time":** the complex noise amplitude σ̃₀ = √(R + 1/(im)) on the time coordinate (Eq. 33). The paper reads it as time being "a two-dimensional object".
- **Stueckelberg equation:** i∂φ/∂τ = (1/2m)□φ − Vφ, a Schrödinger equation in 4-D spacetime with an invariant evolution parameter τ (ref. 15; parametrized relativistic dynamics, ref. 16).
- **Telegrapher's equation (paper's usage):** Eq. (39). It is second order in t through □ and first order in t with an imaginary coefficient, so it is not the real damped wave equation usually meant by the term.

## Connections

What the paper itself says: the stochastic-control approach starts with Nelson (1966, ref. 3), with Yasue (1981) and Papiez (1982) in the 1980s, Rosenbrock–Ding (2008) and Ohsumi (2019). The paper says what all of them lack is "a proper and physically meaningful explanation why the Schrödinger equation is the diffusion equation in imaginary time" (p. 2). Relativistic stochastic quantization (Roy 1980; Yasue 1977) is said not to explain the analytic continuation either. Papiez's 1981 relativistic free-particle stochastic-control quantization (ref. 14) is the direct source for the 4-D diffusion and the four-velocity invariant. The paper does not otherwise compare its derivation with Nelson's, beyond this lineage paragraph.

Comparison with Nelson's stochastic mechanics. **All of this is from outside the paper** (standard results, stated from general knowledge; citations not re-checked in this session):
- Nelson's diffusion is real: dX = b dt + dW with E[dW_i dW_j] = (ħ/m)δ_ij dt, so diffusion coefficient ν = ħ/2m. The magnitude |σ²| = 1/m in this paper (ħ = 1) is the same scale, but here σ² is imaginary.
- In Nelson's theory the i is not inserted. Write ψ = e^{R+iS}. Then the forward and backward drifts combine into the osmotic velocity u = (ħ/m)∇R and the current velocity v = (ħ/m)∇S. Nelson's stochastic Newton law (the mean of forward and backward accelerations equals −∇V/m), together with the continuity (Fokker–Planck) equation, is equivalent to the Schrödinger equation for ψ, with ρ = |ψ|² = e^{2R} the actual density of the process.
- Yasue (1981) and Guerra–Morato (1983, Phys. Rev. D 27, 1774) recover the same result from a *real* stochastic variational or control principle. The complex structure comes from combining the HJB-type equation for the phase with the continuity equation for the density: two real equations, with the Madelung form, give one complex linear one.
- In this paper, by contrast, the Hopf–Cole transform of a single HJB equation carries all the work, which needs complex coefficients. The analogue of R, the real part a of J with φφ* = e^{2a}, is never tied to a continuity equation.
- Known difficulties of Nelson's approach carry over and are not discussed. One is Wallstrom's (1994) objection: one must separately impose that ∮∇S is quantized, i.e. that ψ is single-valued, which here is the branch of log φ. Another is the nonlocality of the many-particle drift, which Nelson himself raised.

On the control-theory side (also outside the paper): the linearizing condition λ = σ²·(control cost) is the one from Fleming's logarithmic transformation and Kappen's (2005) path-integral control. With real coefficients it gives a Feynman–Kac (heat-type) equation, which is the correspondence the paper sets out to explain.

## Bearing on the record

In nucleation this is [LIT-001](../literature.d/LIT-001.md), whose skim is NOTE-003. This reading should replace that skim as `Read`, and it supports moving [LIT-001](../literature.d/LIT-001.md) from `Deferred` to `Rejected` on the grounds in lit_status. It answers the curation-journal question (2026-09-25) about auditing the linearization against Nelson: the linearization is the standard Hopf–Cole condition with complex coefficients, and the i is inserted twice, not derived.

For ML practice there is nothing to carry. The indirect link is the HJB/log-transform linearization, which also underlies path-integral control and the Schrödinger-bridge view of diffusion generative models. It is sourced better from Kappen (2005), Todorov's linearly solvable MDPs, or Léonard's Schrödinger-problem survey than from this paper, whose version runs on complex noise. A search of the anthology's `record/` for Kappen, path-integral control, Schrödinger bridges and Hopf–Cole found none of these, so the paper has no ANTH- code to point to.

## Limitations

- The central claim, that the i comes from spacetime geometry, rests on √(det g) where the standard invariant measure uses √(−det g). A constant complex factor on the objective also turns minimization into mere stationarity.
- Linearity is imposed through σ² = i/m, not derived. The resulting complex noise leaves the "stochastic process", its transition density (Eqs. 5–6) and the expectation defining S without a probabilistic meaning. The paper's realist, "random spacetime force" interpretation (Conclusion) therefore has no process to refer to.
- The metric-signed sum of variances (Eq. 30) disagrees with Itô's formula for independent noises (reader's check). The spatial σ² = Σσ̃_i² in Eq. (7) has the same problem.
- Eq. (26) has a sign inconsistency with Eq. (24) (reader's check). It does not affect Eq. (36), which is derived from Eq. (25)/(34).
- The ∂_τ → γ∂_t step puts a particle velocity into a field equation. The "Klein–Gordon" Eq. (40) is not KG without 2mV = m². The Dirac equation, spin and multi-particle systems are absent despite the abstract.
- Nodes of φ, where log φ is singular, and the single-valuedness/quantization condition are not addressed.
- The Born-rule and anti-PBR statements are assertions. The authors themselves offer curved spacetimes and random metrics as future work (Conclusion).
- The paper is 7 pages, with no figures, numerics or worked example.

## Open questions

- Is there a *real* diffusion on spacetime, and a real cost, whose HJB equation (possibly paired with a Fokker–Planck equation, as in Guerra–Morato) gives Eq. (36) without a complex variance? A construction that did this would support the paper's thesis. The standard Nelson/Yasue route suggests the forward–backward pairing, not the volume form, is what is needed.
- Does the √(−g) convention with the same steps give only the imaginary-time (Euclidean) Stueckelberg equation? The reader's check of the λ = Mσ² condition says yes for real M and σ². Were that confirmed, the thesis would be refuted as stated.
- How are the proper-time parameter s of the diffusion and the evolution parameter τ of the field related, and when is the ∂_τ = γ∂_t substitution legitimate?

## Corrections to the seeded skim

- The dossier says the imaginary unit arises "from the Minkowski metric". More exactly, it arises from writing the invariant volume form as √g d⁴x with g = det g_ij = −1, so √g = i (Eqs. 12–16). The standard invariant form on a Lorentzian manifold is √(−g) d⁴x = √|g| d⁴x, which equals 1 in Minkowski coordinates (standard result, not from the paper). A second i is also needed: the complex noise variance σ² = i/m (Eq. 29), with σ̃₀² = R + 1/(im) (below Eq. 32). The dossier mentions neither.
- The dossier says the paper recovers "relativistic wave equations" and gives Telegrapher's as the missing link "to the Dirac equation". The body derives only the Stueckelberg-form Eq. (36), a Telegrapher-like Eq. (39) and the ∂τφ = 0 equation (40). The Dirac equation appears only as a citation to Gaveau et al. (ref. 19). Eq. (40), □φ − 2mVφ = 0, is Klein–Gordon only if 2mV = m², a condition the paper never states.
- The dossier calls the method "stochastic optimization". Once the Lagrangian is multiplied by i, the objective is complex-valued and neither "min" (Eq. 16) nor "sup" (Eq. 17) is defined. The paper actually uses the stationarity condition ∂H/∂u^μ = 0 (Eq. 18). The optimization reading does not survive past §"The Hamiltonian and optimal feedback control".
- Dates. The PDF prints "Received: 9 September 2019; Accepted: 11 December 2019; Published: xx xx xxxx". The dossier gives online 2019-12-27 via Crossref. The LIT's `published: 2019-12-01` is a month-level placeholder, not a date printed in the paper.
- The rest of the dossier's skim is accurate: Eqs. 2–8, the lineage paragraph, the PBR remark resting on Rizzi (ref. 1) alone, and the Planck-scale speculation.
