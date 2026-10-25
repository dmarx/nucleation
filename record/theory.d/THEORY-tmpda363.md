---
status: Active
title: 'For independent identically distributed observations, and neglecting how far the log-likelihood-ratio walk overshoots its boundaries, Wald''s sequential probability ratio test accepts the null hypothesis with probability (A^h − 1)/(A^h − B^h), where h ≠ 0 solves E e^{hz} = 1, and takes on average [(1 − γ) log B + γ log A]/E z observations; no sequential test with the same error probabilities needs fewer on average under either hypothesis than Wald''s lower bounds, which the test attains when the overshoot is zero, and for a normal mean it saves 47–63% of the fixed-sample test''s observations at error rates from .01 to .05; the overshoot-free formulas are exact for Brownian motion with drift, which the paper never mentions'
version: 1
history:
- version: 1
  date: '2026-10-25'
  note: >-
    Filed Active from NOTE-tmpxtksz, the reading of the copy the owner
    supplied on 2026-10-25. The operating characteristic is Wald's
    (3.32)–(3.35), the sample size (4.4)–(4.8), the savings Table 1 with
    (4.30)–(4.34), and the optimality theorem (4.80)–(4.81). They are
    re-derived below, Table 1 is recomputed, and the approximations are
    checked by simulation, which meets the condition for Active under
    ADR-047 v2. The coincidence with Brownian motion with drift, and the
    reading of the drift-diffusion limit through it, are the record's.
tags:
- mathematical-statistics
- probabilistic-modeling
date: '2026-10-25'
source:
- LIT-tmpcevhu
summary: >-
  Wald (1945), LIT-tmpcevhu, read in NOTE-tmpxtksz. The SPRT's operating
  characteristic and mean sample size follow from two identities of the
  stopped walk, and its optimality from Jensen's inequality, all exact
  when the walk stops on the boundary. Optimality with overshoot is only
  conjectured in the paper. The drift-diffusion limit that the record
  takes from Bogacz et al. (LIT-569, THEORY-068) is not stated by Wald. It
  is the case in which his approximations become exact.
---
# THEORY-tmpda363: For independent identically distributed observations, and neglecting how far the log-likelihood-ratio walk overshoots its boundaries, Wald's sequential probability ratio test accepts the null hypothesis with probability (A^h − 1)/(A^h − B^h), where h ≠ 0 solves E e^{hz} = 1, and takes on average [(1 − γ) log B + γ log A]/E z observations; no sequential test with the same error probabilities needs fewer on average under either hypothesis than Wald's lower bounds, which the test attains when the overshoot is zero, and for a normal mean it saves 47–63% of the fixed-sample test's observations at error rates from .01 to .05; the overshoot-free formulas are exact for Brownian motion with drift, which the paper never mentions

## Source

Wald (1945), *The Annals of Mathematical Statistics* 16(2): 117–186,
LIT-tmpcevhu, read in full in NOTE-tmpxtksz from the JSTOR scan the
owner supplied: §3.4 (operating characteristic), §§4.1, 4.3 and 4.4
(sample size, savings, distribution of n), §4.7 (optimality) and §5.4
(normal mean). The fundamental identity and termination are cited there
from Wald's "On cumulative sums of random variables" (1944). The
derivations below are the record's, following Wald's where he gives one.

## What was actually shown

Let zᵢ = log f₁(xᵢ)/f₀(xᵢ) be i.i.d. under the true distribution, with
nonzero variance, let Z_m = z₁ + … + z_m, and let the test stop at the first
n with Z_n ≥ a = log A or Z_n ≤ b = log B, where A > 1 > B. Let γ be the
probability of stopping at the upper boundary (accepting H₁).

**Operating characteristic.** Let h ≠ 0 solve E e^{hz} = 1. Then e^{hZ_m}
is a martingale with mean 1. Stopping it at n (Wald's (3.32), from the
1944 paper) gives (1 − γ)E* + γE** = 1, with E*, E** the conditional means of
e^{hZ_n} at the lower and upper exits (3.33). Without overshoot E* = B^h
and E** = A^h, so γ = (1 − B^h)/(A^h − B^h) (3.35), and the probability of
accepting H₀ is (A^h − 1)/(A^h − B^h). Under H₀, E₀e^{z} = ∫f₁ = 1, so h = 1.
Under H₁, E₁e^{−z} = ∫f₀ = 1, so h = −1. Wald: "It is easy to verify that
h = 1 if H = H₀, and h = −1 if H = H₁." Then γ = α under H₀ and γ = 1 − β under
H₁, which recovers A = (1 − β)/α and B = β/(1 − α) as equalities
(THEORY-tmpeglfj).

**Expected sample size.** Z_m − mEz is a martingale. Stopping it gives
EZ_n = En·Ez (4.4), Wald's identity, proved in the paper by truncation at
N → ∞. So En = [(1 − γ)E*Z_n + γE**Z_n]/Ez (4.7), and without overshoot
En ≈ [(1 − γ) log B + γ log A]/Ez (4.8).

**Optimality (§4.7).** For any test S of strength (α, β) that stops with
probability one, Wald's identity gives E₁(n|S) = E₁(log p₁ₙ/p₀ₙ)/E₁(z).
Split by the decision. On acceptance of H₁, E₁[p₀ₙ/p₁ₙ | accept H₁] =
P₀(accept H₁)/P₁(accept H₁) = α/(1 − β) exactly (4.71)–(4.74). Jensen's
inequality (Wald's Lemma 1, e^{Eu} ≤ Ee^u) then gives
E₁[log p₁ₙ/p₀ₙ | accept H₁] ≥ log((1 − β)/α), and likewise
≥ log(β/(1 − α)) on acceptance of H₀. Hence
E₁(n|S) ≥ [β log(β/(1 − α)) + (1 − β) log((1 − β)/α)]/E₁(z) (4.81), and
symmetrically (4.80) for E₀. For the SPRT without overshoot, log p₁ₙ/p₀ₙ is
exactly log A or log B on each exit, and these bounds are equalities. So
it is then "exactly an optimum test" (p. 157). With overshoot, the paper
proves only near-optimality and conjectures the rest (footnote 12).

**Savings for a normal mean (§4.3).** With f_i = N(θ_i, 1),
E₁(z) = E₀(−z) = ½(θ₀ − θ₁)² (4.33)–(4.34), and the fixed-sample test needs
n(α, β) = (λ₁ − λ₀)²/(θ₀ − θ₁)² (4.30). Both scale as 1/(θ₀ − θ₁)², so the
saving 100(1 − E₁(n)/n(α, β)) depends on α and β only.

**The diffusion case.** For Brownian motion X with drift μ and variance σ²
per unit time, e^{hX_t} is a martingale for h = −2μ/σ². Hitting the barriers
exactly, optional stopping gives P(hit a first) = (1 − e^{hb})/(e^{ha} − e^{hb}),
which is (3.35) with A = e^a and B = e^b. And X_T − μT is a martingale,
which gives E T = [(1 − γ)b + γa]/μ, which is (4.8). Wald's normal case has
h = −2Ez/σ_z² (4.39), the same exponent. With one boundary, his density
(4.51) for m = (Ez)²n/2σ_z²,
F(m) = c/(2Γ(½)m^{3/2}) e^{−c²/4m − m + c} with c = (Ez) log A/σ_z²,
becomes, after substituting back, a/(σ√(2πn³)) exp(−(a − μn)²/2σ²n) with
μ = Ez, σ² = σ_z² and a = log A. That is the inverse-Gaussian first-passage
density of Brownian motion with drift. So the overshoot-free formulas are
the diffusion's formulas exactly, and Wald's remark that the boundaries
would be exact "if fractional observations were possible" (p. 132) is
the same fact. Wald does not say "Brownian motion", "diffusion" or "limit"
anywhere in the paper.

**Checked** (numpy and scipy, when filed):

- **Table 1** recomputed from (4.30)–(4.32): 48 of its 50 entries agree
  exactly. The other two (α = .05, β = .02 in panel A, and its mirror in
  panel B) compute to 58.50, which Wald prints as 59.
- **Operating characteristic**, α = β = .05, μ from 0 to δ in quarters,
  accept-H₀ probability (3.35) against simulation: at δ = .5,
  0.950/0.813/0.500/0.187/0.050 against 0.961/0.830/0.487/0.169/0.035
  (10,000 runs each). At δ = .05, against 0.947/0.805/0.513/0.184/0.044
  (3,000 runs each). The overshoot makes (3.35) conservative at the
  extremes, and the gap closes as δ falls. The h of (3.35), 1 − 2μ/δ,
  equals Wald's (5.37), (θ₁ + θ₀ − 2θ)/(θ₁ − θ₀).
- **Sample size** (4.8) against simulation: 21.2 against 24.1 at
  α = β = .05, δ = .5; 132.5 against 140.9 at δ = .2; 2,120 against 2,167
  at δ = .05. The underestimate falls from 12% to 2%. The fixed-sample
  test needs 43.3, 270.6 and 4,329 respectively.
- **Lower bound** (4.80)–(4.81), evaluated at the SPRT's own realized
  errors, 400,000 runs: E₀n = 24.18 ± 0.03 against a bound of 23.84, and
  E₁n = 24.22 against 23.93 at α = β = .05, δ = .5. At α = .01, β = .10:
  20.42 against 20.27, and 34.22 against 33.81. The test is within 1.5%
  of the bound with a large overshoot.
- **Brownian motion**, drift 0.3, barriers 2 and −1.5, Euler step 10⁻³,
  4,000 paths: P(hit 2) = 0.686 (standard error 0.007) against (3.35)'s 0.676, and mean time
  2.890 against (4.8)'s 2.889. The density (4.51) integrates to 1 and has
  mean c/2, as the inverse Gaussian does.

What could have failed: Table 1 could have been unreproducible from the
stated formulas, the simulated test could have beaten the lower bound,
or the formulas could have stayed off for small steps. None did.

## What this does not say

- **Not exact optimality with overshoot.** That is footnote 12's
  conjecture, outside this paper.
- **Not anything for dependent or non-identical observations.** The OC,
  the sample size and the optimality all need i.i.d. zᵢ. Only the error
  bounds survive dependence (THEORY-tmpeglfj).
- **Not that the drift-diffusion model is Wald's.** The paper contains the
  discrete test and approximations that coincide with the diffusion's
  formulas. The limit statement is later work's, as the record has it
  through LIT-569.
- **Not that the saving is always about half.** Table 1 is for a normal
  mean with the fixed-sample test as the comparison. Under alternatives
  between θ₀ and θ₁, E(n) is largest and the saving smallest (§5.2.5,
  Fig. 4).

## Connections

- **THEORY-068.** It states, through Bogacz et al. (LIT-569), that the SPRT
  is the fastest test for a given error rate and that its continuum limit
  is the drift-diffusion model. Here the first is a theorem up to the
  overshoot, and the second is the case in which Wald's own approximations
  are exact.
- **CASE-155** (note of 2026-10-25). "Its drift is half its variance": for
  Gaussian evidence the log-likelihood-ratio increment has
  E₁z = ½(θ₁ − θ₀)² and variance (θ₁ − θ₀)², Wald's (4.33) and h = −1 under H₁.
- **CLAIM-tmpfd9lk.** Its replicator construction rests on THEORY-068's
  limit. This account gives that limit a primary-source reading: a
  coincidence of formulas, not a theorem of Wald's.
- **THEORY-tmpeglfj** holds the test's definition and error inequalities.
