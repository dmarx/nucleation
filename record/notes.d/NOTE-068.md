---
number: 68
status: Read
formerly:
- NOTE-tmpna8bp
paper: LIT-050
title: 'Tembine et al., mean-field-type games with Rosenblatt noise'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2506.08025v1 (29 May 2025), 47 pp., all
    of it: §I–§XV, the acknowledgements, references [1]–[46] and the author
    biographies. Extracted with PyMuPDF into raw4/2506.08025.txt. The 17
    figures came through as captions only, so data plots (Figs 1–15) and the
    "noise approximation" plots (Figs 16–17) were read from their captions
    and surrounding text; I could not inspect the plotted data. I checked
    Theorem 4 (optimal gain and cost) by hand and numerically, including its
    H → ½ limit and the Riccati form (scratchpad, inline python). I did not
    look for the Springer chapter the dossier mentions.). Upgraded from
    `Skimmed` to `Read`: the claims table, assumptions and results are new,
    and the skim is corrected where the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper's control and game results use linear state feedback, and they
  depend on the Rosenblatt noise only through its covariance, which is
  exactly fBM's with the same H. They are therefore identical to the fBM
  results. The ergodic LQ gain (Thm 4), K̂ = −[b₁ + √(b₁² +
  4H(1−H)b₂²q/r)]/(2b₂(1−H)), is correct and reduces to the Brownian LQR
  gain at H = ½. But the paper's headline "suboptimality of noise
  approximation" (§VI-A, repeated for the variance-aware control,
  zero-sum, non-zero-sum and MFTG settings) holds only against surrogates
  with a different covariance; against fBM with the same H it is false.
  The ML claim that Rosenblatt "super-diffusion transformers"
  "significantly enhance the performance of generative machine
  intelligence models" (§XIV-C) has no model, training, dataset or
  experiment behind it anywhere in the paper.
---

<!-- inactive-ok-file: LIT-050 — Deferred: the paper is placed by this reading; the directive lapses when its status changes -->

# NOTE-068: Tembine et al., mean-field-type games with Rosenblatt noise

## Contribution

**New to this paper:**
- a survey-style argument that many engineered and socio-economic quantities are non-Gaussian (§II);
- the framing of Rosenblatt noise as a "baseline" for them;
- a restatement of earlier Rosenblatt-noise control and game results (Thms 1, 3, 4, 6, 7, 10 are from refs [27], [41]–[45]);
- a comparison of mean-field-type games with multi-population coalitional mean-field games in a Cournot energy market (§XIII, Table IV, Thms 12–19);
- a sketch of "Rosenblatt foundational diffusion models" (§XIV).

**What is actually established:**
- the ergodic LQ gain and cost under Rosenblatt noise for scalar linear feedback, and the analogous best-response and equilibrium formulas;
- the MFTG-versus-coalitional-MFG gap in a static variance-aware Cournot game (the "price of simplicity" is unbounded under scaling, Table IV).

Neither needs the noise to be non-Gaussian.

## Key insight

The intended one is that model noise as it is (skewed, heavy-tailed, long-memory), because optimising against a Gaussian surrogate is suboptimal. The mathematics shows something narrower. In the linear-quadratic, linear-feedback setting the paper works in, **only the noise covariance matters**. So the relevant misspecification is getting H (the memory) wrong, not getting the Gaussianity wrong. Non-Gaussianity would matter only with non-linear strategies, non-quadratic costs of the state, or risk measures beyond variance. The paper names these as open or leaves them unaddressed ("the extension to non-linear strategies is an open issue", pp. 30–31).

## Assumptions

- **Noise.** The Rosenblatt process R_H, H ∈ (½, 1): a double Wiener–Itô integral, self-similar with R_H(ct) =ᵈ c^H R_H(t), with fBM's covariance, and not a semimartingale (Def. 1, §III).
- **Calculus.** An Itô-type formula for x(t) = x₀ + ∫d₁dt + 2c̃∫d₂ dB^{H/2+1/2} + ∫d₃ dR_H, with f ∈ C² in t, C³ in x, and |f_xxx| ≤ c_t(1 + |x|^α) (Thm 1, from Čoupek–Duncan–Pasik-Duncan 2022 [27]).
- **Control.** Scalar linear dynamics dx = (b₁x + b₂u)dt + dR_H, ergodic cost lim sup (1/T)E∫(qx² + ru²), with the admissible set restricted to **u = Kx, K ∈ ℝ** (Thm 4). The same restriction to linear (and mean-field-type linear) feedback applies to Thms 5–18.
- **Games.** Scalar state; zero-sum requires an unexplained inequality on (b₁, b₂, b₃, q, r, s, H) (§IX). The finite-horizon MFTG (Thm 10) requires a Riccati-type ODE system with positive non-blowing-up solutions.

## Key results

- **Thm 4 (from [43]).**
  - Optimal gain: K̂ = −[b₁ + √(b₁² + 4H(1−H)b₂²q/r)]/(2b₂(1−H)).
  - Cost: L∞(K̂) = Γ(2H+1)(q + rK̂²)/(2[−(b₁+b₂K̂)]^{2H}) = Γ(2H)(−rK̂/b₂)/[−(b₁+b₂K̂)]^{2H−1}.
  - I verified the first-order condition (1−H)b₂K² + b₁K − Hb₂q/r = 0, that the chosen root is the stabilising one, the grid minimum, and that H → ½ gives the Brownian ergodic LQR gain −(b₁ + √(b₁² + b₂²q/r))/b₂.
- **Thm 5 (variance-aware).** It has the same K* and a mean-field gain K̄* = (b₂+b̄₂)q̄/(r̄(b₁+b̄₁)), stabilising iff b₁ + b̄₁ < 0.
- **Thms 6–7 (zero-sum, from [44]).** A value exists and saddle-point linear gains solve a quadratic, with no proof of Thm 6 here.
- **Thms 8–9 (non-zero-sum).** Best-response gains are of Thm 4's form with b₁ replaced by b₁ + Σ_{j≠i}b₂ⱼKⱼ. Equilibrium holds if the fixed-point system has a stabilising solution.
- **Thm 10 (MFTG, from [45]).** A linear-and-mean-field feedback Nash equilibrium for finite horizon with x̄^{2k̄} mean-field costs, given solvable ODEs. Thm 11 is the cooperative version.
- **Thms 12–18 (Cournot MFTG).** The payoff is (ηᵢ − rᵢηᵢ²/2)·Γ(2H+1)/(2[(1+Ση)/ε]^{2H}) plus a deterministic mean part. The best-response η*ᵢ is the root of a quadratic, and the mean equilibrium is p̄* = (a + D + Σcᵢ/(rᵢ+r̄ᵢ))/(1 + Σ1/(rᵢ+r̄ᵢ)).
- **Thm 19.** The coalitional-MFG equilibrium does not depend on r̄ₖ. Table IV: the "price of simplicity" is ½[1/(rᵢ+r̄ᵢ) − (rᵢ−r̄ᵢ)/rᵢ²](∫yμ − cᵢ)², unbounded under scaling.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Real data in e-commerce, power, water, mango supply, hardware, AI funding, onion prices, underwater channels and EV batteries are non-Gaussian | weak | illustrative figures and prose (§II). Most numbers carry no reference; the only reported fit (H ≈ 0.8, W-error ~10⁻⁶) has no method; the data are the author's startups', not released |
| C2 | These data follow "Rosenblatt" (or "two/three-mode Rosenblatt") distributions | unsupported | no fitting procedure, parameters, or comparison with alternatives (stable, other Hermite, mixtures). "Multi-mode Rosenblatt" is undefined |
| C3 | Itô formula for Rosenblatt-driven processes | strong (cited) | Thm 1, proved in [27] (SPA 2022), not here |
| C4 | Optimal ergodic LQ gain and cost under Rosenblatt noise (linear feedback) | strong | proof sketch in text + [43]; I verified the gain, stability and H → ½ limit |
| C5 | Optimising against Brownian, fBM, Gauss–Volterra or Poisson surrogates gives suboptimal control / non-equilibrium | false for fBM with matching H; true for mismatched covariance | assertion + Figs 16–17 (captions only). Contradicted by the paper's own cost formula, which depends only on H and the covariance |
| C6 | Optimal MSE predictor is x(t′) (Thm 2) | false as stated | contradicts the drift term and Thm 3 |
| C7 | Rosenblatt ARE link: (1−H)(b₂²/r)P² + b₁P − Hq = 0, K̂ = (b₂/r)P | wrong sign | my check: it gives the destabilising gain |
| C8 | MFTG ≠ multi-population coalitional MFG; freezing mean-field terms can be arbitrarily suboptimal | moderate | explicit static computation (Table IV, Thm 19); a scaling argument for unboundedness |
| C9 | Rosenblatt "super-diffusion transformers" significantly enhance generative models | unsupported | §XIV-C assertion; no model, training or experiment anywhere |
| C10 | The paper demonstrates turnpike properties | unsupported | contributions list only; absent from the body |
| C11 | Adaptive control under Rosenblatt noise | absent | §VII is an empty heading |

## Method

Direct method: restrict strategies to a parametric linear class, compute the long-run cost in closed form via the Rosenblatt Itô formula (in practice, a second-moment computation), and minimise over the gains. Games are handled by best-response fixed points in the same class. The Cournot MFTG uses an orthogonal decomposition into a zero-mean fluctuation game (stochastic) and a mean game (deterministic). There is no numerical method, no estimation and no learning.

## Concepts

- **Rosenblatt process** R_H: a second-order Hermite process. It is non-Gaussian and self-similar with index H ∈ (½, 1), has fBM's covariance, has stationary increments, and is not a semimartingale.
- **Mean-field-type game (MFTG)**: payoffs and dynamics depend on the players' own state and action distributions, possibly non-linearly (variance, quantiles). The number of players can be finite. Contrasted with MFGs, where individual players are non-atomic and payoffs are linear in the individual mean field.
- **"Price of simplicity"**: the payoff gap from freezing mean-field terms (Table IV).
- **"Two-mode / three-mode Rosenblatt shape"**: used throughout §II and never defined.

## Connections

- **Control results.** These come from the authors' own earlier papers: Čoupek–Duncan–Pasik-Duncan, "A stochastic calculus for Rosenblatt processes" (SPA 2022, [27]); Čoupek–Duncan–Maslowski–Pasik-Duncan (CDC 2018, [43]); Duncan–Pasik-Duncan (CDC 2020, [44]; CoDIT 2024, [41]; JSSC 2025, [42]); Duncan–Pasik-Duncan–Tembine (CoDIT 2024, [45]; CDC 2024, [46]).
- **Rosenblatt process.** Rosenblatt (1961); Taqqu (1975, 1979); Dobrushin–Major (1979).
- **Real-data non-Gaussianity in control loops.** Domański (2015, [23]).
- **Diffusion models.** §XIV cites no diffusion-model or transformer literature at all: no score-based, DDPM or DiT references.

## Bearing on the record

- **No THEORY document should cite it.** The seed's summary sentence (the "noise approximation cascade") should not enter the record as a finding, since it is false for the fBM surrogate (C5).
- **For ML practice: none.** The "super-diffusion transformers" claim must not be cited as evidence for heavy-tailed or long-memory noise in diffusion models. There is no model or experiment (C9). If the Anthology of the SOTA ever files a practice or theory on non-Gaussian or fractional noise in diffusion models, it needs a paper that trains and evaluates such a model; this one does not.
- The [LIT-050](../literature.d/LIT-050.md) summary should be rewritten to reflect the Rejected standing and the covariance-only point.

## Limitations

As stated by the authors:
- "the extension of a bigger class of strategies is still an open issue" (p. 30);
- non-linear strategies are open (p. 31);
- infinite horizon is used "in order to get explicit representation" and is not favoured in practice (p. 37).

Not stated by the authors:
- restriction to linear feedback makes every result covariance-only;
- no data, code or fits are released for §II;
- conflict of interest (data from the first author's companies);
- missing sections (§VII) and unproved theorems (Thm 6);
- the ML section has no content that could be evaluated.

## Open questions

These are the questions the paper raises but does not answer.
- **Does non-Gaussianity of Rosenblatt noise change optimal control** when strategies may be non-linear, or costs non-quadratic in the state or risk-sensitive (e.g. exponential-of-integral)? A result showing an optimal non-linear feedback beating the best linear one under R_H, but not under fBM with the same H, would be the first evidence that the non-Gaussian part matters for control.
- **Is any of the §II data actually better described by a Rosenblatt marginal** than by standard heavy-tailed or mixture alternatives? A released dataset with a likelihood or information-criterion comparison would settle it.
- **Do diffusion models driven by fractional or Hermite-process noise improve sample quality** on a standard benchmark? That needs a trained model and a metric, neither of which is here.

## Corrections to the seeded skim

- **The seed's summary sentence is the paper's own claim, and it is wrong in the form stated.** "Replacing Rosenblatt noise … with Brownian, fractional-Brownian or jump noise before optimising yields suboptimal controllers." For the fBM part:
  - Every optimisation in the paper is over **linear (state- or mean-field-type) feedback** of a **linear** system with **quadratic** or mean-only costs. Under linear feedback, x(t) = e^{at}x₀ + ∫₀ᵗ e^{a(t−s)}dR_H(s) is a Wiener-type integral of a deterministic kernel, so every cost term is a second moment or a deterministic mean.
  - The paper itself says R_H "shares" fBM's covariance ½(t^{2H} + s^{2H} − |t−s|^{2H}) (§III). Its variance formula in §XIV-C is literally the fBM one: H(2H−1)∫∫e^{θt′}e^{θt″}|t′−t″|^{2H−2}.
  - Hence Thm 4's cost L∞(K) = Γ(2H+1)(q + rK²)/(2[−(b₁+b₂K)]^{2H}) is exactly the stationary-variance formula of an fBM-driven Ornstein–Uhlenbeck process. The optimal gain for fBM with the same H is the same.

  The "∃ε > 0: |C_surrogate − C_true| ≥ ε" claim (§VI-A, Figs 16–17) is true only for surrogates with a different covariance: Brownian motion (H = ½), a different H, or a different scale. The same objection applies to the repeated claims for the variance-aware control (§VIII-A), the zero-sum (§IX-A) and non-zero-sum (§X-A) games, the Remarks after Thm 10 (MFTG) and Table III. No figure data or derivation for the "cascade failure" is given beyond Figs 16–17's captions.
- **The seed read the ML section only in part; the full text confirms and strengthens its flag.** §XIV (pp. 41–44), "Rosenblatt Foundational Diffusion Models", contains:
  - (A) an OU forward process under Brownian motion, with a "reverse" process whose drift uses the known clean signal x₀ (a bridge to a given point, which trivially recovers x₀, not a generative model);
  - (B) an fBM version with a stated reverse-time SDE driven by a "time-reversed fractional Brownian motion", given without derivation, and an "exact" Gaussian score valid only for a single deterministic x₀;
  - (C) the Rosenblatt OU SDE, its H → 1 limit and its variance.

  There is **no transformer, no network, no training objective, no dataset, no sample, no metric and no comparison**. The sentence "This approach incorporates longer-term context-awareness and non-Gaussianity which significantly enhances the performance of generative machine intelligence models" (§XIV-C) is an assertion. The variance formula offered in support is the fBM one, so it cannot show non-Gaussian benefit. The Index Terms list "Rosenblatt super diffusion transformers", and the contributions paragraph says the R-OU framework "underpins the design of super diffusion transformers, offering a rigorous foundation for advancements in machine intelligence" (p. 3). Neither is supported.
- **The seed says the data section shows no formal fit "in the parts I read". There is none anywhere.** §II (pp. 3–21) calls distributions "two-mode Rosenblatt", "three-mode Rosenblatt" or "Rosenblatt-like" throughout without any estimation procedure, parameters or goodness-of-fit, with one exception. The underwater ROV experiment on the Niger river (p. 19) reports "estimated Hurst parameter H ≈ 0.8" and "a Wasserstein error on the order of 10⁻⁶". That comes from 600 samples (1 s over 10 min), with no units, scale, method or comparison model.
  - The marginal of the Rosenblatt process is a single one-parameter (H) law up to scale. I believe it is unimodal, since it is self-decomposable (Maejima–Tudor 2013; I did not re-check this here), so "two-mode" and "three-mode Rosenblatt shape" can only mean unspecified mixtures.
  - Several quantitative claims carry no reference:
    - "Gaussian models underestimate tail risk by 60%" (Fig. 1);
    - "Traditional Gaussian-based models mispredicted grid stress events by 40%" (Fig. 4);
    - Punjab demand "20 BCM" vs "35 BCM", "12,000 farmers" (2021), "$500 million in losses in 2022";
    - "A 2023 and 2024 analysis of Germany's power grid found that net load … followed a two-mode Rosenblatt distribution".
  - The mango, shallot/onion, underwater and SoH data come from Guinaga and Timadie, which the author biography says the first author founded or co-founded. The data are not released.
- **Other errors the seed did not catch:**
  - **Theorem 2 is false as stated.** It says the optimal mean-square predictor of x(t), for dx = b₁x dt + dR_H, given the past up to t′, is x(t′). That fails whenever b₁ ≠ 0 (even for martingale noise the drift gives e^{b₁(t−t′)}x(t′)), and R_H is not a martingale. Theorem 3, on the next page, gives a different (memory-dependent) optimal linear predictor.
  - **The Riccati link after Thm 4 has a sign error.** "(1−H)(b₂²/r)P² + b₁P − Hq = 0, K̂ = (b₂/r)P" with P the positive root gives the *destabilising* root: for b₁ = 0.7, b₂ = 1.3, q = 2, r = 0.5, H = 0.75 it gives K = 2.55 and a closed-loop pole at +4.02. The correct form is (1−H)(b₂²/r)P² − b₁P − Hq = 0 with K̂ = −(b₂/r)P, which reproduces Thm 4's K̂ = −4.705 (my check). The printed identity "H(q + rK̂²) − (b₁ + b₂K̂) = −rK̂/b₂" should read H(q + rK̂²) = (rK̂/b₂)(b₁ + b₂K̂).
  - **Thm 5's mean gain K̄* = (b₂+b̄₂)q̄/(r̄(b₁+b̄₁)) is stabilising only if b₁ + b̄₁ < 0.** This condition is not stated, though the admissible set requires b₁ + b̄₁ + K̄(b₂+b̄₂) < 0. (I verified K̄* and the mean cost b̄₀²q̄r̄/((b₁+b̄₁)²r̄ + (b₂+b̄₂)²q̄) for the stable case.)
  - **Unfinished material:**
    - §VII "Adaptive control driven by Rosenblatt noise" is an empty heading;
    - §VI-B's two extensions state problems ending "(independent ? correlated ?)" with no result;
    - the contributions claim "Turnpike properties", which appear nowhere in the body;
    - Thm 6 (minimax = maximin) has no proof.
  - **Wrong cross-reference:** the proof of Thm 4 cites "Theorem 1 and Equation (1)" for the Itô formula, but (1) is the underwater path-loss equation; (3) is meant.
  - **Wrong date:** Einstein's Brownian-motion paper is dated 1908 in text and reference [3], but *Ann. Phys.* 322, 549–560 is 1905.
