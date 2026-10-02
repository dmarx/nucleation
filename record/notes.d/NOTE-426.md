---
number: 426
status: Read
formerly:
- NOTE-tmpw8bm2
paper: 'LIT-521'
title: 'Information theory explanation of the fluctuation theorem, maximum entropy production and self-organized criticality in non-equilibrium stationary states'
version: 1
history:
- version: 1
  date: '2026-10-02'
  note: >-
    Read in full (arXiv cond-mat/0005382 v3, 13 Dec 2002, 21 pp., the
    version the author marks as the one to appear in J. Phys. A. Prose was
    extracted with PyMuPDF. The displayed equations are in a Symbol font
    that extraction drops, so the equation pages (9, 11, 13–15, 18) were
    rendered and read as images). I read §§1–5 and all 43 references. I
    re-derived the two-box optimum numerically and checked Eq. 28 against
    Eqs. 26–27, and I compared the SOC argument with Grinstein and
    Linsker's critique (LIT-525). The version of record and the 2005
    sequel were not seen.
date: '2026-10-02'
summary: >-
  Jaynes's maximum-entropy inference, applied to microscopic paths of an
  open stationary system, gives p_Γ = exp(A_Γ)/Z. The action is a symmetric
  end-point term plus τσ_Γ/2k_B. A fluctuation theorem p(σ) = e^{τσ/k_B}
  p(−σ) and ⟨σ⟩ ≥ 0 follow exactly. Maximum entropy production follows
  only in a mean-field approximation, and only if the number of paths
  increases with their irreversible action, which is assumed. The
  self-organized-criticality corollary is a mean-field divergence. As
  Grinstein and Linsker showed, it does not survive keeping the quartic
  term.
---
<!-- inactive-ok-file: LIT-520 — Deferred, no lawful full text; named as the survey of the MEP literature, not leaned on -->
<!-- inactive-ok-file: THEORY-026 — Proposed; named to say this reading has no bearing on it, not leaned on -->

# NOTE-426: Information theory explanation of the fluctuation theorem, maximum entropy production and self-organized criticality in non-equilibrium stationary states

## Contribution

The paper offers a statistical-mechanical derivation of the
maximum-entropy-production principle (MaxEP). Until then MaxEP had been
proposed empirically, from Paltridge's climate models onward, and argued for
qualitatively. Dewar applies Jaynes's maximum-entropy (MaxEnt) procedure to
microscopic *paths* instead of states, and reads off three consequences:

- the fluctuation theorem;
- MaxEP as the selection principle for stationary states;
- self-organized criticality (SOC) in slowly driven flux systems.

The aim is to make Jaynes's formalism a "common predictive framework" for
equilibrium and nonequilibrium statistical mechanics (p. 2).

## Key insight

Count paths, not states. Choose the path distribution that is broadest
given the macroscopic constraints, as Gibbs chose the broadest state
distribution. Then entropy production appears in the exponent of the path
weight, and the most probable macroscopic history is the one realised by
the most paths. If more paths go with more irreversibility, the most
probable stationary state is the one that produces entropy fastest. The
whole argument turns on that "if".

## Assumptions

- **MaxEnt as the method.** The macroscopic behaviour is reproducible, so
  it is characteristic of nearly all compatible paths. Maximizing path
  entropy under the imposed constraints discards irrelevant microscopic
  information (§2.2). "When applications of the Jaynes procedure fail …
  [it] signals the presence of new constraints" (p. 6).
- **Step 1 constraints** (Eqs. 2–4): normalisation, a fixed initial
  configuration ⟨d(x,0)⟩ of energy and mass densities in the volume V, and
  fixed time-averaged boundary fluxes on the boundary Ω. Local energy and
  mass conservation are imposed through Eq. 9.
- **Redundancy of the surface term.** After integration by parts, the
  surface multiplier "can be set to zero" because the flux information is
  "now also contained" in the volume term (p. 10). This is stated, not
  shown.
- **Step 2 logic.** The quantities fixed in Step 1 are, for a reproducible
  state, "ultimately determined only by the remaining constraints". So
  maximizing S_I over the multipliers λ(x) is the right second step (§2.3).
- **MaxEP needs two further assumptions** (§4.2):
  - a mean-field approximation that ignores fluctuations of the action
    about its mean (Eq. 23);
  - W(A^irr), the number of paths with irreversible action A^irr, is "an
    increasing function of A^irr" (p. 14).
- **Time-reversal pairing.** Every path has a reverse with the same
  end-point action and opposite irreversible action (§4.1).
- **SOC** (§4.3): a Landau–Ginzburg form H(F|F_ext) = rF² + gF⁴ with r > 0
  and g < 0 for the output-flux distribution (Eqs. 26–27), and a mean-field
  (quadratic) treatment of fluctuations.

## Key results

- **Eq. 5.** p_Γ = exp(A_Γ)/Z, with A_Γ = ∫_V λ·d(x,0)_Γ + ∫_Ω η·F^n_Γ (Eq. 6).
- **Eq. 14.** In terms of a local T and μ_i defined from the multipliers
  (Eq. 13), A_Γ = −½∫(H_Γ(0) + H_Γ(τ))/k_BT + τσ_Γ/2k_B. Here σ_Γ is the
  time-averaged entropy production rate of the path, the usual
  flux-times-force sum for a multicomponent fluid (Eq. 15). T, μ and σ are
  defined without local equilibrium (p. 12).
- **Eq. 18.** p_Γ/p_{Γ_R} = exp(τσ_Γ/k_B). From it, ⟨exp(−τσ/k_B)⟩ = 1 and
  ⟨σ⟩ ≥ 0 (Eq. 20). The fluctuation theorem is p(σ) = exp(τσ/k_B) p(−σ)
  (Eq. 21). These are exact given Eq. 14.
- **Eqs. 22–24, MaxEP.** S_I,max = ln Z − ⟨A⟩ ≈ ln W(⟨A^irr⟩), under the
  mean-field approximation. If W increases with A^irr, maximizing S_I
  over λ is maximizing ⟨σ⟩.
- **Two-box climate toy** (p. 15). With T_1 ∝ (f_SW − h)^{1/4} and T_2 ∝
  h^{1/4}, σ = h(1/T_2 − 1/T_1) peaks at h_opt ≈ 0.199 f_SW. I re-derived
  this numerically: the maximum is at h = 0.1991 f_SW.
- **Which σ is maximized.** For climate, it is the *material* entropy
  production (Eq. 15), horizontal and vertical. Radiative entropy
  production does not count (pp. 15–16). This answers Essex's objection to
  Paltridge.
- **SOC** (Eq. 28). In mean field the output-flux variance is
  ⟨(F − ⟨F⟩)²⟩ ≈ 1/(8|g|F_ext²), which diverges as F_ext → 0. I checked
  this from Eqs. 26–27 and it follows given them. The author calls it
  "likely to be only qualitatively correct" (p. 18).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | MaxEnt over paths under the stated constraints gives p_Γ ∝ exp(A_Γ), with τσ_Γ/2k_B in the action | strong given the constraints | Eqs. 2–14; the surface-term step (p. 10) is asserted |
| C2 | The fluctuation theorem and the second law on average follow | strong for the inferred distribution | Eqs. 18–21; exact given Eq. 14 |
| C3 | MaxEP is Step 2 of the Jaynes procedure | weak | needs mean field (Eq. 23) and the unargued assumption that W(A^irr) increases (p. 14) |
| C4 | In climate applications it is the material, not the radiative, entropy production that is maximized | moderate | follows from which balance Jaynes's procedure is applied to (pp. 15–16); argued, not tested |
| C5 | SOC emerges from MaxEP in the slow-driving limit | weak, and refuted as stated | Eq. 28 is a mean-field divergence; [LIT-525](../literature.d/LIT-525.md) shows keeping the quartic term gives a finite variance |
| C6 | Accumulating empirical evidence for MaxEP, FT and SOC supports Jaynes's formalism | assertion | §5; the evidence cited is for MaxEP fits in climate and elsewhere, not tests of this derivation |

## Concepts

- **Path information entropy** S_I = −Σ_Γ p_Γ ln p_Γ over microscopic
  phase-space paths Γ of length τ (Eq. 1).
- **Reversible and irreversible action.** The end-point part of A_Γ is
  symmetric under path reversal. The part τσ_Γ/2k_B is antisymmetric
  (p. 14).
- **MaxEP**: the selection principle that the stationary state realised is
  the one of maximum mean entropy production under the constraints. The
  paper's name for what later papers call MEP.

## Connections

- **Lineage.** Jaynes (1957, 1979) for MaxEnt and its near-equilibrium
  success with linear transport theory. Paltridge (1975–81) and successors
  for the empirical MaxEP in climate. Ziegler's maximum-dissipation theorem
  as a phenomenological route. Maes (1999) for the Gibbs-type path measure
  that gives the fluctuation theorem. Bak, Tang and Wiesenfeld for SOC.
- **Prigogine.** Jaynes, commenting in 1980 on Prigogine's minimum
  principle, conjectured that Gibbs's method "might be closer in spirit to a
  principle of maximum entropy production" (p. 4). Dewar takes that as the
  programme. The paper does not engage the minimum principle further.
- **The dynamical fluctuation theorems.** Eq. 21 has the form of the
  theorems Crooks ([LIT-522](../literature.d/LIT-522.md)) and Seifert's review ([LIT-523](../literature.d/LIT-523.md))
  derive from Markovian, locally-detailed-balanced dynamics. Here it
  follows from an *inferred* path measure. So the paper explains why the
  fluctuation theorem holds if real path statistics are MaxEnt-distributed.
  It does not show that they are.
- **Critique and reception.** Grinstein and Linsker ([LIT-525](../literature.d/LIT-525.md)) refute
  the SOC corollary. Kleidon ([LIT-519](../literature.d/LIT-519.md)) relies on this paper for MEP's
  foundation and calls it work in progress. Martyushev and Seleznev
  ([LIT-520](../literature.d/LIT-520.md)) survey it, but could not be read.

## Bearing on the record

- **MaxEP vs Prigogine.** The paper is the record's text for the claim that
  MEP has a statistical foundation. On this reading the foundation is
  incomplete. The derivation of MaxEP is conditional on an assumption about
  path counting that is not argued and on a mean-field step. The 2005
  sequel, by Grinstein and Linsker's account, tried to remove the
  near-equilibrium restriction and did not.
- **Upstream: Jaynes's MaxEnt.** [LIT-114](../literature.d/LIT-114.md) and [NOTE-103](NOTE-103.md) record that the
  cogency of MaxEnt as a foundation of statistical mechanics is unsettled.
  Every doubt there transfers here, since this paper is MaxEnt applied to
  paths. [NOTE-103](NOTE-103.md)'s "MEP" means maximum entropy *principle*, not maximum
  entropy *production*. A reader should not merge the two acronyms.
- **[THEORY-026](../theory.d/THEORY-026.md) and the stochastic-thermodynamics line:** no bearing. The
  paper concerns stationary states of continuum open systems, not driven
  finite systems.
- **Life and dissipative structures.** Dewar's conclusion extends the
  procedure to "economies and biological populations" (p. 19). That is the
  hook the life-as-dissipation literature uses, and Kleidon
  ([LIT-519](../literature.d/LIT-519.md)) uses it for life and Gaia. The paper itself gives no
  biological argument.
- **No ML instruction.** The anthology does not hold it.

## Limitations

- **The MaxEP step is approximate and conditional.** The paper says so
  ("within the mean-field approximation", p. 15). The monotonicity of
  W(A^irr) is assumed with no argument or example (p. 14).
- **Reproducibility does the work.** The Step 2 justification, that fixed
  averages are "ultimately determined only by the remaining constraints",
  is the substantive physical assumption. It is stated as a methodological
  rule.
- **SOC.** The result depends on a mean-field quadratic expansion
  extended to all F. The author concedes it is "likely to be only
  qualitatively correct" (p. 18).
- **No new test.** The paper offers no new prediction checked against data.
  The empirical support it cites is for MaxEP fits, not for this
  derivation.

## Open questions

- Is W(A^irr) increasing in A^irr for any model where it can be computed?
  The paper gives none.
- Does the derivation survive outside mean field, and outside the linear
  regime? The 2005 sequel addressed the second. Grinstein and Linsker
  ([LIT-525](../literature.d/LIT-525.md)) show it did not succeed.
- Which constraints make a system "have enough degrees of freedom" for MEP
  to apply? Kleidon ([LIT-519](../literature.d/LIT-519.md)) states this condition. The paper's
  answer is only that a failure signals a missing constraint.

## Corrections

- none to a seeded skim (there was no seed)
- **Abstract vs Eq. 18.** The abstract states p_Γ ∝ exp(τσ_Γ/2k_B). The
  forward/backward ratio (Eq. 18) is exp(τσ_Γ/k_B). These agree, since the
  end-point terms cancel in the ratio, but readers comparing with Crooks's
  e^{ω} should use Eq. 18.
- **Extraction.** Text-extracted copies of this preprint lose every
  displayed equation (Symbol font). Quotations of equations in this note
  are from rendered pages.
