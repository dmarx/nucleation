---
status: Read
paper: LIT-tmp1zkcf
title: 'Neural Tangent Kernel of Matrix Product States: Convergence and Applications'
version: 1
history:
- version: 1
  date: '2026-09-27'
  note: >-
    Read in full (Full text of arXiv 2111.14046 v1 (the only version), from
    the arXiv PDF: 19 pp. I read the abstract, §§1–5, the references, and
    Appendices A (the GP limit), B (the NTK limit, lazy training,
    positive-definiteness) and C (the Born-machine partition function). The
    one figure is a schematic, seen only as its caption. `pdftotext` was not
    available in this session, so I extracted the text with PyMuPDF. Some
    equations came through garbled. Where an exponent was ambiguous (e.g.
    "2n−1"), I resolved it from the surrounding derivation and say so where
    it matters. I checked the Born-machine ODE solution numerically myself.
    The paper contains no numerics.). The first NOTE on this paper, which
    was seeded from its abstract alone.
date: '2026-09-27'
summary: >-
  In the sequential infinite-bond-dimension limit, with tensor variances
  σ_i²/√(|α_i||α_{i+1}|) and per-tensor learning rates
  (|α_i||α_{i+1}|)^{-1/2}, the NTK of a periodic MPS tends to K(x,x′)=Σ_k
  φ(x_k)·φ(x′_k) Π_{l≠k} σ_l² φ(x_l)·φ(x′_l). By my reduction this is (Σ_k
  σ_k⁻²) times the MPS's own GP covariance, so gradient flow is kernel
  regression with a fixed product kernel. The Born-machine solution
  P_x(t)=1/m−(1/m−P_x(0))e^{−4mKt/Z} is correct (I checked it; Z is in
  fact conserved). The lazy-training lemma is heuristic, the
  positive-definiteness "proof" shows at most semi-definiteness, several
  constants are off by factors of n or 2^{−n}, and there are no
  experiments.
---

<!-- inactive-ok-file: LIT-tmp1zkcf — Rejected: the paper this note reads, placed by this reading; the directive lapses when its status changes -->

# NOTE-tmp6uhuc: Neural Tangent Kernel of Matrix Product States: Convergence and Applications

## Contribution

The paper carries the Jacot et al. NTK programme ([ANTH-LIT-360](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-360.md)) over to matrix product states (MPS, tensor trains with a periodic trace) used as learning models. It has four steps.

- **GP limit.** Following the authors' earlier "infinitely wide tensor networks as Gaussian process" (arXiv 2101.02333), it shows that an MPS with i.i.d. Gaussian tensors becomes a Gaussian process as the bond dimensions go to infinity one after another (Thm 2.1, App. A).
- **NTK limit.** It computes the limiting NTK at initialisation (Thm 3.1) and asserts that the NTK stays constant during training (Thm 3.4, Lemma 3.5).
- **Positive-definiteness.** It claims the NTK is positive definite (Prop. 3.3).
- **Two training problems.** It solves the linear ODEs for squared-error regression (§3.4) and the ODE for an MPS Born machine trained by negative log-likelihood on binary data (§4).

The new content is the MPS-specific scaling (a variance and learning rate both ∝ (|α_i||α_{i+1}|)^{−1/2}) and the Born-machine solution. Everything else is the Jacot template applied to a multilinear model.

## Key insight

An MPS is linear in each tensor and linear in the fixed feature map Φ(x)=⊗_i φ(x_i). The contracted core B_{s_1…s_n} becomes an i.i.d. Gaussian vector in the limit, so the infinite-bond MPS is a linear model in the tensor-product feature space. Its tangent kernel is therefore, up to a constant, the product kernel Π_l k_l(x_l,x′_l) with k_l = φ(x_l)·φ(x′_l). (The paper computes this but does not say it.)

Gradient flow then does what gradient flow on any fixed-kernel linear model does:

- **Regression.** Residuals decay as e^{−tK}.
- **Born machine.** The feature map is orthogonal on binary strings, so K is a multiple of the identity. Every training configuration's probability relaxes independently, at one common rate, to 1/m.

The model thus memorises the empirical distribution and puts zero mass everywhere else. The paper calls that avoiding over-fitting.

## Assumptions

- **Architecture.** Ψ(x;A)=Σ_{s,α} A^{s_1}_{α_1α_2}⋯A^{s_n}_{α_nα_1} Φ_{s_1…s_n}(x) (eq. 2.1). This is a periodic ring (trace) with a scalar output and a factorised feature map Φ=⊗_i φ_{s_i}(x_i). The local dimensions |s_i| and the variances σ_i are finite (App. A, Prop. 1).
- **Initialisation.** A^{s_i}_{α_iα_{i+1}} ~ N(0, σ_i²/√(|α_i||α_{i+1}|)) i.i.d. (Thm 3.1, Remark 2.2). App. B's restatement has the typo σ_1²/√(|α_1||α_2|). This is a standard (not NTK) parametrisation: the 1/√ factor sits in the initial variance, not in the forward pass.
- **Learning rate.** The rate is scaled per tensor, η_{α_iα_{i+1}} = (|α_i||α_{i+1}|)^{−1/2} (eq. 3.5, Remark 5.1). The NTK is defined with η folded in (eq. 3.1). Without it the Gram matrix diverges like (|α_k||α_{k+1}|)^{1/2} (App. B, last line before 5.24).
- **Order of limits.** The bond dimensions go to infinity sequentially: α_2,…,α_n first, α_1 last (App. A). There is no joint or rate-controlled limit.
- **Training time.** Following Jacot, Thm 3.4 assumes that ∫_0^T ‖d_t‖ dt of the training direction is bounded on [0,T]. For MSE this is asserted as "easy to show" (§3.4). For the Born machine, Prop. 4.2 derives it from the further assumption that Z[Ψ] is bounded in probability. No proof of Prop. 4.2 is given.
- **Regression example.** The per-site kernel is Gaussian, exp(−(x_i−x_i′)²/2τ_i²) (Ex. 3.6). That needs infinite-dimensional φ, which is outside the finite-|s_i| assumption of the GP proof. The σ_i are set to 1 ("zero mean and unit variance", §3.4). All training points are assumed pairwise equidistant, so that off-diagonal kernel entries all equal r ∈ (0,1).
- **Born-machine example.** The data are x ∈ Ω={0,1}^n with φ(x_i)=(1/√2)[x_i, 1−x_i] (eq. 4.4). The loss is L=−Σ_i log|Ψ(x^(i))|² + m log Z, with Z=Σ_{x∈Ω}|Ψ(x)|² (eqs. 4.1–4.3). The paper implicitly treats the m samples as distinct. It also takes a length limit n→∞ in which Z/2^n is replaced by its mean (eq. 4.7).

## Key results

As stated, with my check of each.

- **Thm 2.1 / App. A Thm 1 (GP limit).** Ψ ~ GP(0, Σ) with Σ(x,x′)=Π_i |s_i| σ_i² φ_i(x_1)·φ_i(x′_1) (eq. 2.4 = 5.14). The derivation (eq. 5.19) gives Σ(x,x′)=Π_i σ_i² φ(x_i)·φ(x′_i). The |s_i| factor and the subscript x_1 in the statement are typos.
  - *Check.* I checked the variance bookkeeping of the induction (eqs. 5.7–5.10). An open chain with ends α_1,α_{n+1} has entry variance (α_1α_{n+1})^{−1/2}Π σ_i². Summing over α_n reproduces this, and the final trace over α_1 gives Π σ_i². The CLT step is the usual sequential one: at each stage the summands are uncorrelated and conditionally independent given the earlier core. That is standard in style (as in Jacot or Matthews et al.) but not written out.
- **Thm 3.1 / App. B Thm 2 (NTK at initialisation).** K_{ij} → Σ_{k=1}^n φ(x^(i)_k)·φ(x^(j)_k) Π_{l≠k} σ_l² φ(x^(i)_l)·φ(x^(j)_l) in probability (eq. 3.4 = 5.20). The derivation replaces the sum over (α_k,α_{k+1}) by |α_k||α_{k+1}| times an expectation (LLN). Before the rescale by η it gets Σ_k (|α_k||α_{k+1}|)^{1/2}(…).
  - *My reduction.* This equals (Σ_k σ_k^{−2}) · Σ_GP(x,x′). The NTK is a constant multiple of the GP covariance, as for any model linear in a Gaussian core. The paper never remarks on it.
- **Prop. 3.3 / 5.2 (positive-definiteness).** The claim is that K is positive definite. The proof rewrites Π_l φ(x^(i)_l)·φ(x^(j)_l) as Π_l φ(x^(i)_l) Π_m φ(x^(j)_m) (eq. 5.30→5.31). That step treats the vector inner products as products of scalars. It then writes the quadratic form as Σ_k(Π_{l≠k}σ_l²)(Σ_i c_i Π_l φ(x^(i)_l))² and asserts that it vanishes "only when all c_i are zero".
  - *Correct statement.* The quadratic form is (Σ_kΠ_{l≠k}σ_l²)·‖Σ_i c_i Φ(x^(i))‖² ≥ 0. So K is positive semi-definite. It is definite if and only if the feature vectors Φ(x^(i)) are linearly independent. Since Φ lives in a space of dimension Π_i|s_i|, the rank of K is at most Π_i|s_i|. Mercer's condition is invoked but not used.
- **Thm 3.4 and Lemma 3.5 (constancy in training, "lazy training").** The claim is sup_{t≤T}|A(t)−A(0)| → 0 in probability, entrywise (eq. 3.8 = 5.26).
  - *The proof (eqs. 5.27–5.28)* writes dA/dt=⟨∂_AΨ,d⟩. It omits the learning rate η. It cites a nonexistent "Proposition 5" to say ∂_AΨ → N(0,(α_1α_{n+1})^{−1/2}…) → 0, then concludes.
  - *Three gaps.* (i) The gradient's distribution is taken at initialisation and used for all t, which assumes the tensors stay near initialisation, the thing to be proved. (ii) An entrywise bound does not control the NTK. K is a sum over |α_k||α_{k+1}| entries, so one needs the aggregate change of the Jacobian, which is what Jacot's Grönwall-type argument bounds. (iii) The training direction's bound is assumed, not derived.
  - *Scaling check.* The conclusion is plausible, and I checked its scaling. Gradient entries have standard deviation ~(|α_k||α_{k+1}|)^{−1/4}. With η ~ (|α_k||α_{k+1}|)^{−1/2}, an entry moves O((|α_k||α_{k+1}|)^{−3/4}) over [0,T], against an initial scale of (|α_k||α_{k+1}|)^{−1/4}. That is a relative change of O((|α_k||α_{k+1}|)^{−1/2}). But the paper does not prove the conclusion.
- **Regression (eqs. 3.10–3.16).**
  - The flow dΨ/dt = −K(Ψ−y) has the solution Ψ(t) = y + e^{−tK}(Ψ(0)−y) (eq. 3.13). That is correct, with the factor 2 from the square dropped.
  - With σ_l=1, eq. 3.11 gives K = n Π_l φ·φ. Under the equidistance assumption K = n[(1−r)I + r11ᵀ]. Then the mean response obeys Ψ̄(t) = ȳ + (Ψ̄(0)−ȳ)e^{−t·n(1+(m−1)r)}.
  - Eq. 3.16 states the rate as 1+(m−1)r. It drops the factor n, and §3.4 says "all the diagonal elements of the NTK matrix K_ij are one", which contradicts its own eq. 3.11.
  - The mean is an eigen-direction only because of equidistance.
- **Born machine (Props. 4.1–4.3, eqs. 4.5–4.11).**
  - *NTK.* The NTK is stated as K(x^(i),x^(j)) = δ_ij Π_k σ_k² (eq. 4.5). Substituting eq. 4.4 into eq. 3.6 gives φ(x_l)·φ(x′_l)=½δ_{x_l x′_l}, hence K = 2^{−n}(Σ_kΠ_{l≠k}σ_l²)δ. So eq. 4.5 is inconsistent with eq. 3.6 by the factor 2^{−n}Σ_kσ_k^{−2}.
  - *Partition function.* In the same way, the proof of Prop. 4.3 uses Var Ψ(x)=Π σ_i², where the correct value is 2^{−n}Π σ_i². Given its own variance, the Gamma law Z ~ Γ(shape 2^{n−1}, scale 2Πσ_i²) (eq. 4.6, reading "2n−1" as 2^{n−1}) is right as a sum of 2^n i.i.d. scaled χ²₁. Eq. 4.7 then says Z/2^n → Π σ_i², a "constant" that itself depends on n. The meaningful statement is Z/E[Z] → 1.
  - *ODE solution.* It is Ψ² = Z/m + (Ψ_0² − Z/m)e^{−4mKt/Z} and P_x(t) = 1/m − (1/m − P_x(0))e^{−4mKt/Z} (eqs. 4.9–4.10). It is solved treating Z as constant, which the paper justifies only by a length limit and the WLLN. I checked it, and it is exact whenever K = κI on all of Ω and the samples are distinct. Z is conserved: L is invariant under Ψ→cΨ, so ⟨Ψ,∇L⟩=0, and a flow with K ∝ I preserves ‖Ψ‖². A direct Euler integration (16 states, 4 samples) matched eq. 4.10 to 4 significant figures, with Z constant to 10⁻⁴ relative. Off-sample states obey Ψ(x)² ∝ e^{−4mκt/Z}, so they go to zero. The paper does not state this, but it follows.
  - *Characteristic time.* It is T = Z/(4mK) → 2^{n−2}/m (eq. 4.11). With the paper's constants this follows. With the corrected constants and σ=1 it is 2^n/(4mn), and the "T=1/4 when m=O(2^n)" claim becomes 1/(4n). "Time" here is in units rescaled by η ∝ (|α||α|)^{−1/2}, so "converges in constant time" says nothing about step counts.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | An MPS with i.i.d. N(0,σ_i²/√(|α_i||α_{i+1}|)) tensors tends to GP(0, Π_iσ_i²φ(x_i)·φ(x′_i)) as the bond dimensions → ∞ sequentially | moderate | App. A induction with CLT at each stage; the variance bookkeeping checks out. The CLT/independence step is sketched, and the stated formula (eq. 2.4) has a spurious Π|s_i| and wrong indices |
| C2 | With per-tensor learning rate (|α_i||α_{i+1}|)^{−1/2}, the NTK at initialisation → Σ_kφ(x_k)·φ(x′_k)Π_{l≠k}σ_l²φ(x_l)·φ(x′_l) | moderate | App. B computation; the LLN over bond indices is asserted, not proved; limit interchange is not handled. The formula is right given C1 |
| C3 | The NTK stays constant during training ("lazy training", Lemma 3.5, Thm 3.4) | weak (informal argument) | The proof (eqs. 5.27–5.28) uses the initial-time gradient distribution for all t, omits η, bounds entries rather than the aggregate, and cites a nonexistent Proposition 5. The conclusion is plausible by scaling |
| C4 | The limiting NTK is positive definite, so gradient flow converges "without any extra assumptions of the data set" | weak; false as stated | Eqs. 5.29–5.32 conflate vector inner products with scalar products. Only semi-definiteness follows. Definiteness needs linearly independent Φ(x^(i)), which fails for m > Π|s_i| or duplicate inputs |
| C5 | MSE regression solution Ψ(t)=y+e^{−tK}(Ψ(0)−y) | strong (standard) | Linear ODE with constant K; correct given C2–C3 |
| C6 | With Gaussian per-site kernels, the mean response evolves at the top eigenvalue 1+(m−1)r | weak | Needs pairwise-equidistant data (m ≤ n+1). The rate misses a factor n relative to the paper's own eq. 3.11 |
| C7 | Born machine: K=δ_ijΠσ_k²; Z ~ Γ(2^{n−1}, 2Πσ_i²) | weak | Both are inconsistent with eqs. 3.6 and 4.4 by factors 2^{−n} and Σ_kσ_k^{−2}; the proof of Prop. 4.1 is not given |
| C8 | Born-machine probabilities obey P_x(t)=1/m−(1/m−P_x(0))e^{−4mKt/Z} | moderate | Derived treating Z as fixed. That turns out to be exact (Z is conserved when K∝I), which I checked analytically and numerically; the paper's own justification (WLLN in n) is not the reason |
| C9 | Characteristic learning time 2^{n−2}/m, constant when m=O(2^n); learning time grows exponentially with the number of tensors | weak | Follows from C7's constants, which are off; the time units absorb η |
| C10 | For the Born machine "over-fitting problem is naturally avoided" and "all the modes … are well preserved" (§4.2) | assertion; contradicted by C8 | C8 converges to the empirical distribution with zero mass off-sample, which the paper itself calls memorisation. No generalisation analysis or experiment |
| C11 | An MPS is "a weighted average of an ensemble of fully-connected [linear] ANNs" (Prop. 2.3), which become independent in the limit | assertion / reformulation | Re-indexing of the contraction; no proof of the independence remark |

## Method

- **Model.** A periodic MPS with a factorised local feature map, regarded as |s|^n "linear networks" N_i indexed by the physical configuration and weighted by Φ_i(x) (Prop. 2.3, Fig. 1).
- **Analysis.** Jacot's NTK template: define K = η ⊙ (∂Ψ(x)⊗∂Ψ(x′)) (eq. 3.1), take bond dimensions to infinity sequentially, and invoke CLT/LLN at each stage. Then assert lazy training and solve the kernel-gradient ODE for two losses: MSE (§3.4) and Born-machine NLL (§4).
- **No computation.** There are no simulations, finite-width checks or experiments of any kind.

## Concepts

- **Bond dimension limit.** This is the MPS analogue of infinite width. Each virtual index α_i → ∞, in sequence.
- **NTK of MPS.** The Gram matrix of the Jacobian with respect to all tensor entries, weighted entrywise by the learning rate η_{α_iα_{i+1}} (eq. 3.1). It differs from Jacot's definition, which has no η in the kernel.
- **Lazy training.** Here this means entrywise vanishing of sup_t |A(t)−A(0)| (Lemma 3.5). That is weaker than what constancy of the NTK needs.
- **Training direction d.** This is ∂_ΨL at the training points: Ψ−y for MSE, and 2(1/Ψ(x) − mΨ(x)/Z) for the Born machine (§4.2).
- **Born machine.** A generative model with p(x)=|Ψ(x)|²/Z, where Ψ is an MPS (Han et al. 2018).
- **Characteristic time.** T = Z/(4mK), the e-folding time of P_x(t) − 1/m (eq. 4.10).

## Connections

- **Jacot, Gabriel & Hongler 2018 ([ANTH-LIT-360](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-360.md)).** This is the template. The differences are these:
  - *Parametrisation.* Jacot uses the NTK parametrisation, with 1/√n in the forward pass and a constant learning rate. This paper uses a standard-style initial variance σ²/√(|α_i||α_{i+1}|) and moves the scaling into a per-tensor learning rate (Remark 5.1). That is the familiar standard-parametrisation-plus-scaled-learning-rate equivalent of the NTK regime.
  - *Proof of constancy.* Jacot proves NTK constancy by bounding the parameter trajectory's total movement, given ∫‖d_t‖dt bounded. This paper borrows that assumption but not that argument.
  - *Positive-definiteness.* Jacot proves it for inputs on the sphere with a non-polynomial Lipschitz activation. This paper's footnote 2 repeats the sphere condition for ANNs but never states its analogue for MPS.
- **Tensor Programs I–II ([ANTH-LIT-558](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-558.md), [ANTH-LIT-557](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-557.md)).** These give GP and NTK limits for architectures written as tensor programs, including multiplicative ones, with simultaneous limits. An MPS contraction is such a program. That general framework subsumes the GP and NTK statements here more rigorously. This paper cites neither.
- **Feature learning at infinite width ([ANTH-LIT-548](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-548.md)).** The result here is squarely in the kernel ("lazy") regime. The MPS NTK equals the GP kernel up to a constant, so nothing is learned about features. Tensor Programs IV's point, that the NTK limit cannot learn features, applies directly to the infinite-bond MPS. Lazy-versus-rich analyses such as [ANTH-LIT-537](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-537.md) frame the regime this paper sits in without naming it.
- **Kernel spectrum and learning curves ([ANTH-LIT-328](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-328.md)).** The regression result is the standard eigenmode-decay picture that those works develop, here specialised to a product kernel and equidistant data.
- **Stepwise SSL ([LIT-242](../literature.d/LIT-242.md)).** That paper uses an NTK-derived kernel for SSL dynamics. The connection here is only the shared use of NTK dynamics; there is no substantive link, so it is not cited as related.
- **Nucleation record otherwise.** Nothing in literature.d or theory.d treats tensor networks, MPS or Born machines. The quantum-geometric IR note ([LIT-262](../literature.d/LIT-262.md)) is about Hilbert-space models of retrieval, not trainable tensor networks, and is not connected.

## Bearing on the record

- **Theories.** No THEORY in nucleation is supported or contradicted.
- **ML practice.** It carries nothing. The one practice-shaped suggestion is that Born machines avoid over-fitting where early stopping is needed for ANNs (§4.2). It is untested and contradicted by the paper's own solution. The regression analysis says nothing a practitioner of tensor-network models could act on, since there are no finite-bond checks. It does not belong in the Anthology.
- **For filing.** `learning-theory` first: it is an infinite-width training-dynamics paper. `mathematics` fits the GP and NTK limit arguments. `quantum-foundations` is justifiably appropriate only as the home of the MPS/Born-rule formalism a browser of that topic might look for. The paper borrows the formalism and says nothing about foundations, so drop that tag if the topic is read strictly. `representation-learning` is not proposed: the result is that the infinite-bond MPS learns no representation, and the paper does not discuss representations. `anthology-candidate` is not proposed.

## Limitations

- **No experiments.** Nothing checks whether finite-bond MPS (bond dimension ~10–100, as used by Stoudenmire & Schwab or Han et al.) are anywhere near this limit.
- **Lazy training is not proved.** The entrywise argument is circular and does not control the kernel (see C3). The regression and Born-machine solutions inherit this gap.
- **Positive-definiteness is overstated.** Only semi-definiteness is shown. The rank of K is at most Π|s_i|, so "no extra assumptions on the data set" is false in the finite-|s_i| setting the GP proof assumes.
- **Constants are inconsistent across sections.** The Gaussian example drops a factor n (eq. 3.16 vs 3.11). The Born-machine NTK and variance drop 2^{−n} and Σ_kσ_k^{−2} (eqs. 4.5, 5.34 vs 3.6, 4.4). Downstream numbers (T_Learning = 2^{n−2}/m, "T = 1/4") change accordingly.
- **The limits are sequential, and time is rescaled.** The η scaling means "constant time" statements have no step-count meaning.
- **Headline results rest on special data.** The Gaussian-kernel result requires equidistant data (m ≤ n+1). The Born-machine decoupling depends on the particular orthogonal binary feature map.
- **The over-fitting conclusion is inverted.** The solved dynamics converge to the empirical distribution with zero off-sample mass. For a generative model that is maximal over-fitting, not its avoidance.
- **Presentation.** Several statements are garbled or mis-referenced: eq. 3.7, a missing "Proposition 5", Theorem 3.1 restated with σ_1 and α_1,α_2 only, and Jacot et al. cited for tensor-network approximations of quantum states (§1).

## Open questions

- **Rigorous lazy training.** Does the NTK of a periodic MPS stay constant during training under this scaling, with a proof that bounds the whole trajectory, e.g. via a Tensor Programs master theorem or a Grönwall bound? Does it hold for a simultaneous limit of bond dimensions?
- **Finite-bond behaviour.** How close are practical MPS models (bond dimension 10–100) to the kernel limit? One test would be to measure the relative NTK change during training against bond dimension, and to compare test performance with the product-kernel regressor that the limit predicts.
- **Is there a rich regime?** Is there a µP-style scaling of MPS tensors (cf. [ANTH-LIT-548](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/literature.d/LIT-548.md)) under which the infinite-bond limit learns features rather than collapsing to the fixed product kernel? Only such a limit could explain whatever advantage trained MPS models show over their initial kernel.

## Corrections to the seeded skim

- none (there was no seed or dossier for this work)
- Identification note for filing: the arXiv abstract page lists only v1 (28 Nov 2021, 196 KB; comment "19 pages, 1 figure"), with no journal-ref and no DOI beyond the arXiv DataCite DOI 10.48550/arXiv.2111.14046. A web search found no published version, only ResearchGate and aggregator copies of the preprint. No venue is known.
- The abstract says positive-definiteness guarantees convergence "without any extra assumptions of the data set". The body's proof (App. B, Prop. 5.2, eqs. 5.29–5.32) establishes at most positive semi-definiteness. Strict definiteness needs the tensor-product features Φ(x^(i)) of the training inputs to be linearly independent. That fails for repeated inputs, and whenever m > Π_i|s_i|, which is the finite feature dimension that the GP theorem itself requires (Prop. 1: "|s_i| … all finite").
- The abstract says, for regression with Gaussian kernels, that "the evolution of the mean of the responses of MPS follows the largest eigenvalue of the NTK". The body (Ex. 3.6, eq. 3.16) shows this only under the extra assumption that all pairwise distances between training points are equal. That is only possible for m ≤ n+1 points in ℝⁿ.
- The abstract speaks of "the orthogonality of the kernel functions in BM". In the body this is the specific feature map φ(x_i)=(1/√2)[x_i, 1−x_i] on binary data (eq. 4.4). It is not a property of Born machines in general.
- The paper has no experiments, which the abstract does not say. The only figure is a diagram of a three-site MPS.
