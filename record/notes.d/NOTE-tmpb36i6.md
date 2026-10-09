---
status: Read
paper: 'LIT-tmppqrls'
title: 'Exact solutions to the nonlinear dynamics of learning in deep linear neural networks'
version: 1
history:
- version: 1
  date: '2026-10-09'
  note: >-
    Read in full on 2026-10-09 from the arXiv PDF of v3 (arXiv:1312.6120v3,
    19 February 2014, 22 pp.: 15 pages of main text and references, then
    Supplementary Appendices A–G), as text extracted with pdftotext and
    saved as paper.txt in the session's download directory. Main text
    §§1–5 read with every figure caption; figures were not seen, so plotted
    values are taken from captions and text only. Appendices A (unbalanced
    three-layer solution), B and B.1 (Hessian, optimal step size and the
    depth comparison), C and F (MNIST set-ups), D (the literature on
    pretraining), E (task-aligned input correlations) and G (the variance
    recursion for orthogonal tanh networks) read. The derivations of Eqs.
    10–12, 15–17 and 41–45 were checked; Eq. 26 and the general-depth
    integral of Eq. 15, which the paper does not write out, were not. The
    reference list read. v1 (20 December 2013) and v2 (24 January 2014)
    were not read; their arXiv abstracts were compared, and v1's lacks the
    orthogonal-initialisation and edge-of-chaos results. The authors' 2013
    Cognitive Science Society paper, cited for the semantic-development
    application, was not read. LIT-862 with NOTE-666 and THEORY-186, and
    LIT-855 and LIT-859 with NOTE-660 and NOTE-658, were read first, so that
    this note records what the 2014 paper adds.
date: '2026-10-09'
summary: >-
  Derives the coupled gradient-descent equations of a linear network with
  hidden layers and whitened inputs, and solves them exactly from
  decoupled starts: one sigmoid per singular mode of the input–output
  correlation, with conserved differences of squared layer strengths;
  balanced or not with one hidden layer, from equal layer strengths at any
  depth. Depth slows learning only through the
  initial end-to-end mode strength, so from strength of order one the
  iteration count stays finite as depth grows when the step size is
  scaled down with depth. Argues, with MNIST and random-matrix
  simulations, that orthogonal layers or suitable pretraining give such
  starts and scaled Gaussian layers do not, and that orthogonal tanh
  networks near gain 1 keep their Jacobians near-isometric.
---
<!-- inactive-ok-file: THEORY-186 — Proposed; the account of the three-layer result, which this paper first derived -->
<!-- inactive-ok-file: THEORY-tmp8wj5h — Proposed; the account this reading produced -->
<!-- inactive-ok-file: THEORY-182 THEORY-039 — Proposed; accounts this reading bears on -->

# NOTE-tmpb36i6: Exact solutions to the nonlinear dynamics of learning in deep linear neural networks

## Contribution

Plateaus followed by sudden improvement had been seen in simulations of
deep networks, and the slowness of deep training had been blamed on local
minima, saturation and exploding or vanishing gradients. Fukumizu (1998)
had solved a three-layer linear network for one class of initial
conditions, through a matrix Riccati equation. Baldi and Hornik (1989) had
shown that its error surface has saddles and no spurious minima. This paper
writes down the full coupled dynamics of a linear network with hidden
layers. It solves them exactly on an invariant set of decoupled initial
weights, for one hidden layer and for any depth. From the solution it
derives how learning time depends on the strength of each input–output
mode, on the initial weights and on depth. It then argues from the
solution and from simulations to claims about pretraining, random
orthogonal initialisation and signal propagation in nonlinear networks.

## Key insight

Learning time in a deep linear network is set by the product of the layer
strengths along each mode. Gradient descent on each factor is proportional
to the others, so a mode whose product starts small sits on a plateau and
then rises in a sigmoid. A strong mode rises sooner. Depth matters only
through that product. A deep network whose end-to-end map starts as a
near-isometry on every mode learns in a depth-independent number of steps.
One whose layers merely preserve norm on average does not, because its
product is far from isometric. The phrase "learns stepwise, strongest mode
first" covers only the small-initialisation corner of this picture. The
rest of the picture concerns how far from that corner a network can start.

## Assumptions

- **Linear network, squared error, batch gradient descent** with a small
  learning rate λ, passed to continuous time with τ = 1/λ and time
  measured in epochs (Eqs. 1–2, 13).
- **Whitened inputs**, Σ¹¹ = I, for all the solutions in the main text.
  Appendix E extends them to Σ¹¹ = V D Vᵀ, input correlations sharing the
  task's input singular vectors, and calls the generalisation
  straightforward without working it out.
- **Decoupled initial conditions.** For one hidden layer, W³² = U D_a Rᵀ and
  W²¹ = R D_b Vᵀ with R orthogonal. For depth N_l, orthogonal R_l such that
  R_{l+1}ᵀ W_l(0) R_l is diagonal, with R₁ = V and R_{N_l} = U. On this set
  the modes do not interact (Section 2). Hidden layers may be of any width,
  under- or over-complete.
- **Equal layer strengths** (a = b; aᵢ(0) = a₀ for all i) for the closed
  forms (Eqs. 10–12, 15–17). Appendix A drops this for one hidden layer.
- **Random small initial weights** are not covered by any derivation. The
  main text says the decoupled solutions are "excellent approximations",
  on the evidence of simulation (Fig. 3). Appendix A gives a heuristic for
  balance: |a·a − b·b| is small for random vectors of equal length.
- **The depth result** assumes a step size proportional to the inverse of
  the largest Hessian eigenvalue reachable on the equal-strength manifold
  (Appendix B). On MNIST each depth's step size was tuned by grid search.
- **The edge-of-chaos analysis** assumes random orthogonal weights, an odd
  saturating nonlinearity, large width, and Gaussian-distributed activity
  across a layer (Appendix G).

## Key results

- **Eqs. 2 and 5–6, the coupled dynamics.** In the SVD basis of Σ³¹ the
  connectivity modes obey τ daα/dt = (sα − aα·bα)bα − Σ_{γ≠α} bγ(aα·bγ),
  and symmetrically for bα. This is gradient descent on
  E = (1/2τ)Σα(sα − aα·bα)² + (1/2τ)Σ_{α≠β}(aα·bβ)². The pairwise term
  repels the modes of different α towards orthogonality.
- **§1.2, the endpoint** (from Baldi and Hornik). Fixed points satisfy
  aα·bβ = sα δαβ. Only the one that keeps the N₂ strongest modes is stable,
  so W³²W²¹ → Σ_{α≤N₂} sα uα vαᵀ, and every other fixed point is a saddle.
- **Eqs. 8–12, one hidden layer.** On the decoupled set, τȧ = b(s − ab),
  τḃ = a(s − ab), gradient descent on (1/2τ)(s − ab)², with a² − b²
  conserved. For a = b, τu̇ = 2u(s − u), t = (τ/2s) ln[u_f(s − u₀)/(u₀(s −
  u_f))], so learning from ε to s − ε takes about (τ/s)ln(s/ε), and
  u(t) = s e^{2st/τ}/(e^{2st/τ} − 1 + s/u₀). *Holds when:* decoupled,
  balanced start and Σ¹¹ = I. Exact.
- **Appendix A, unbalanced.** With a = √c₀ cosh(θ/2), b = √c₀ sinh(θ/2), or
  the reverse, τθ̇ = s − c₀ sinh θ, integrated in closed form (Eq. 26). The
  O(τ/s) timescale survives for small c₀ and θ₀. The paper separates this
  from Fukumizu's Riccati solution, which needs Σ aαaαᵀ = Σ bαbαᵀ.
- **Eqs. 13–15, any depth.** On the decoupled set each mode has scalars
  a₁, …, a_{N_l−1} descending (1/2τ)(s − Πaᵢ)². Every aᵢ² − aⱼ² is
  conserved, and from equal starts u = Πaᵢ obeys τu̇ = (N_l −
  1)u^{2−2/(N_l−1)}(s − u). For N_l = 3 this is Eq. 10.
- **Eqs. 16–17, infinite depth.** τu̇ = N_l u²(s − u), so
  t = (τ/(N_l s²))[log(u_f(u₀ − s)/(u₀(u_f − s))) + s/u₀ − s/u_f]. At a fixed
  step size this goes to zero with depth. The authors call that an
  artefact of continuous time.
- **Appendix B, step size.** On the equal-strength manifold the largest
  Hessian eigenvalue, at the optimum a = s^{1/(N_l−1)}, is
  (N_l − 1)s^{(2N_l−4)/(N_l−1)}/τ. The optimal step size therefore scales as
  O(1/(N_l s²)), and on MNIST the tuned rates fall as O(1/N_l) (Fig. 4).
- **Appendix B.1, the finite delay.** With that step size, three layers take
  c ln[u_f(s − u₀)/(u₀(s − u_f))] and infinite depth takes c[log(…) + s/u₀ −
  s/u_f]. The difference is about cs/ε. The delay depth adds is finite,
  but it is inverse in the initial mode strength ε where one hidden layer's
  is logarithmic.
- **Fig. 4 (empirical).** Deep linear networks on MNIST, depths 3 to 100,
  hidden width 1000, decoupled starts at u₀ = 0.001, best of twenty step
  sizes per depth: learning times to a fixed training-error threshold
  saturate with depth.
- **Eq. 18, the pretraining condition.** Autoencoder pretraining from small
  weights ends near W²¹ = R M^{1/2} Qᵀ, with Q the input's principal
  components. This is a decoupled start for the supervised task only if
  Q = V, the task's input singular vectors. Checked on MNIST by eye on a
  submatrix of Vᵀ Σ¹¹ V (Fig. 5). A pretrained five-layer linear network
  beats one from N(0, 0.01²) weights even counting pretraining time, in one
  run as reported.
- **§3, Gaussian against orthogonal products (numerical).** For N = 1000,
  over 500 realisations, products of N_l − 1 Gaussian matrices with entry
  standard deviation 1/√N have singular-value distributions that grow
  kurtotic with depth. Their eigenvalues collapse towards the origin,
  which the paper reads as strong non-normality. Products of orthogonal
  matrices have every singular value equal to 1. On MNIST, learning time
  grows with depth from Glorot-scaled initialisation but not from random
  orthogonal initialisation or greedy pretraining, whose curves coincide
  (Fig. 6A).
- **§4 and Appendix G, edge of chaos.** For x^{l+1} = gWφ(x^l) with W
  random orthogonal, q^{l+1} = g²∫Dz φ(√(q^l) z)², so q^∞ = 0 for g < 1 and
  a stable q^∞(g) > 0 for g > 1 (tanh, g_c = 1). The theory matches
  simulated depth-30 networks (Fig. 8). The singular values of the
  end-to-end Jacobian, from simulation at N = 1000 and N_l = 100: tiny
  for g < 1, anisotropic for g > 1, and an O(1) fraction of order one at
  g = 1 for input variances from 0.2 to 4 (Fig. 7).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Gradient descent in a linear network with one hidden layer and whitened inputs is descent on an energy in which the weights of one mode cooperate and those of different modes repel | strong (derivation) | Eqs. 4–6 |
| C2 | From decoupled starts the modes evolve independently. With a balanced start each mode's strength is a sigmoid reaching s in about (τ/s)ln(s/ε), and a² − b² is conserved | strong (exact solution) | Eqs. 8–12 |
| C3 | The O(τ/s) timescale survives an unbalanced decoupled start when a² − b² is small | strong (exact solution) | Appendix A, Eq. 26 |
| C4 | Random small weights follow the decoupled solution closely, and a tanh network on the same task behaves similarly | moderate (simulation) | Fig. 3: one hierarchical dataset of 32 items, 100 random initialisations for the delay measure; the authors expect the nonlinear match to be problem-dependent |
| C5 | At any depth, decoupled modes evolve independently, every aᵢ² − aⱼ² is conserved, and the end-to-end strength obeys τu̇ = (N_l − 1)u^{2−2/(N_l−1)}(s − u) | strong (derivation) | Eqs. 13–15 |
| C6 | With the step size scaled to its stable maximum, the extra time an infinitely deep network needs over a three-layer one is finite, about cs/ε | strong within the analysis | Appendix B and B.1, on the equal-strength manifold; the step size is bounded by the Hessian at the optimum only |
| C7 | Deep linear networks from decoupled starts learn MNIST in a depth-independent number of iterations | moderate (one experiment) | Fig. 4, one threshold, a tuned step size per depth |
| C8 | Autoencoder pretraining gives a decoupled start for a task exactly when the input's principal components are the task's input singular vectors | strong for linear networks (derivation), weak as an account of pretraining in practice | Eq. 18; the authors expect it not to carry over to nonlinear networks |
| C9 | Products of scaled Gaussian layers preserve norm on average but are far from isometric at depth, while orthogonal products are exactly isometric | strong for the orthogonal case (trivial); moderate for the Gaussian case (numerical, no theory given) | Fig. 6B–C |
| C10 | Random orthogonal initialisation gives depth-independent learning times like pretraining, and scaled Gaussian initialisation does not | moderate (one MNIST experiment) | Fig. 6A |
| C11 | Dynamical isometry, not norm preservation, is the condition for fast learning at depth | weak (argued) | §3 discussion; the link from Jacobian spectrum to learning time is not derived |
| C12 | Orthogonal tanh networks have an order-to-chaos transition at g = 1, near which their Jacobians stay approximately isometric over 100 layers | moderate (mean-field theory plus one simulated network per setting) | Eqs. 47–49, Figs. 7–8 |
| C13 | The modest gain of pretraining in practice will grow at greater depths, even in nonlinear networks | not supported here (a prediction) | §3 |

## Method

Average the updates over the batch, pass to continuous time, and rotate the
weights into the SVD basis of the input–output correlation. On the
invariant set where every layer's singular vectors chain through the next,
each mode reduces to a few scalars descending (s − product)². A scaling
symmetry of that energy gives conserved quantities (the paper invokes
Noether's theorem). These reduce each mode to one variable, integrated by
separation of variables, or in hyperbolic coordinates when the layers are
unbalanced. Depth enters through the exponent of the reduced equation. The
discrete-time step size is bounded by the top Hessian eigenvalue at the
optimum. Initialisations are compared through the singular-value spectra of
the product of layers, computed numerically. The nonlinear case uses a
mean-field recursion for the layer variance and numerical Jacobian
spectra.

## Concepts

- **connectivity mode** (aα, bα): the weights from input mode vα into the
  hidden layer, and from the hidden layer to output mode uα.
- **mode strength** u: the product of a mode's layer strengths, the
  network's current gain on that singular mode.
- **decoupled initial conditions**: weights whose singular vectors chain
  from Vᵀ through orthogonal R_l to U, an invariant set of the dynamics.
- **learning time**: the time for u to go from ε to s − ε, or in the
  experiments the iteration at which training error crosses a fixed
  threshold.
- **dynamical isometry**: the product of Jacobians that carries error
  signals back acts as a near-isometry, up to a global O(1) scale, on as
  large a subspace as possible. Many singular values sit near one constant.
  Stronger than norm preservation.
- **edge of chaos**: the critical gain g_c at which a deep orthogonal
  network with a saturating nonlinearity passes from decaying to
  persistent activity; g_c = 1 for tanh.

## Connections

It builds on Baldi and Hornik (1989) for the fixed points and on Fukumizu
(1998) for the earlier, Riccati-type solution. It sets itself against
Glorot and Bengio's (2010) scaled initialisation, and against the
explanations of hard deep training in Hochreiter, Bengio et al., and Erhan
et al. It takes the hierarchical dataset of Fig. 3, and the link to
semantic development, from the authors' 2013 Cognitive Science Society
paper. The edge of chaos is borrowed from recurrent networks. The
recurrent-network gradient regulariser of Pascanu, Mikolov and Bengio is
cited as partly promoting dynamical isometry.

In this record, [LIT-862](../literature.d/LIT-862.md) (2019) restates the three-layer solution of
Eqs. 10–12 as its Eq. 6, without citing this paper ([NOTE-666](NOTE-666.md)). It adds what
this paper lacks: the shallow-network comparison, b(t) = s(1 − e^{−t/τ}),
the transient non-monotone predictions, the data models (trees, rings,
coherence), and the minimum-norm result. This paper has what the 2019 one
leaves out: the coupled equations with the repulsion between modes, the
unbalanced solution, arbitrary depth, the step-size analysis, and
initialisation. [LIT-855](../literature.d/LIT-855.md)'s Lemma 3.1 is Eq. 12 for a symmetric
factorisation W Wᵀ. Its Result 3 addresses the random-initialisation gap
that this paper leaves to simulation. [LIT-859](../literature.d/LIT-859.md)'s per-mode logistic and
conserved ‖p₂‖² − ‖q₁‖² are Eqs. 8–10 and the conservation law here,
carried into the two blocks of a linear-attention layer. The loss
[NOTE-278](NOTE-278.md) calls "Saxe-style", feature benefit plus interference, is this
paper's Eq. 6.

## Bearing on the record

- **[THEORY-186](../theory.d/THEORY-186.md).** This is the first appearance of its result. The
  solution, the logarithmic timescale and the sigmoid are here; the
  comparison with a shallow network and the data models are not. Its
  `promote_when` asks for a proof that random, unbalanced small weights
  converge to the decoupled trajectory, and names this paper as a possible
  supplier. This paper does not supply one. It relaxes balance, exactly,
  for decoupled starts only (Appendix A). It gives a heuristic for why
  random weights are nearly balanced, and a qualitative reason, the
  repulsive term of Eq. 6, why modes decouple. Convergence from random
  weights rests on Fig. 3's simulations, as in the 2019 paper. [THEORY-186](../theory.d/THEORY-186.md)
  stays Proposed on that ground. **Recommendation:** add this LIT to
  [THEORY-186](../theory.d/THEORY-186.md)'s `source:` beside [LIT-862](../literature.d/LIT-862.md), and correct its Source section,
  which says neither record holds the 2014 paper. The three-layer result
  should not be filed a second time.
- **It produces [THEORY-tmp8wj5h](../theory.d/THEORY-tmp8wj5h.md).** The depth results are not held anywhere
  in the record: depth acts through the initial end-to-end mode strength,
  delay is finite with depth from strength of order one, and the plateau
  from strength ε grows as ε^{−(N_l−3)/(N_l−1)}, tending to 1/ε, instead of
  as ln(1/ε). The exponent is my integration of Eq. 15; the paper states
  only the one-hidden-layer and infinite-depth cases. Nor is the distinction between norm
  preservation and isometry of the product. The new THEORY states these as
  a finding about deep linear networks. The practical half, which
  initialisation to use, is left to the anthology.
- **[THEORY-182](../theory.d/THEORY-182.md).** Its sigmoids are Eq. 12 for a symmetric
  factorisation. Consistent. Its random-initialisation gap is the same
  gap, and it is not closed here.
- **[THEORY-039](../theory.d/THEORY-039.md).** The plateau-and-transition structure is derived here
  first. The depth result adds that plateau length depends on the initial
  scale in a way that changes with depth, from ln(1/ε) with one hidden
  layer towards 1/ε at infinite depth.
- **[THEORY-086](../theory.d/THEORY-086.md).** No direct bearing beyond what [NOTE-666](NOTE-666.md) records. This
  paper does not give the shallow, exponential case.
- **[NOTE-278](NOTE-278.md).** Its "Saxe-style" linear loss is Eq. 6 here, the source that
  the Toy Models footnote points to without naming.
- **[LIT-372](../literature.d/LIT-372.md)** (Saxe et al. 2018) uses deep linear networks too, for the
  information bottleneck. That is a different paper and a different
  question, with no bearing here.
- **ML practice.** The paper recommends random orthogonal initialisation,
  and gains just above the edge of chaos, as good regimes for training deep
  nonlinear networks. That is an instruction for practice, and the reason
  the LIT carries `anthology-candidate`. It is not carried into a THEORY
  here.

## Limitations

- **Exact only on an invariant set.** Every closed form assumes decoupled
  initial weights aligned with the SVD of Σ³¹ and whitened inputs. The
  correlated-input extension is stated, not worked.
- **Random initialisation is simulated.** That covers both the three-layer
  case (Fig. 3, one dataset) and depth: the MNIST runs of Fig. 4 start on
  the decoupled set, not from random weights.
- **Random orthogonal weights are not on the decoupled set.** They are not
  aligned with Σ³¹'s singular vectors. The theory of decoupled modes
  therefore does not cover the orthogonal-initialisation result. The
  explanation offered, isometry of the product, is a separate and informal
  argument.
- **The isometry link is argued.** No result connects the singular values
  of the Jacobian product to learning time. The Gaussian-product spectra
  are numerical, and the authors say no complete theory exists.
- **The nonlinear results concern propagation at initialisation**, not
  learning. Fig. 7 shows one network per setting, and the Gaussian
  activity assumption is unchecked beyond the variance match of Fig. 8.
- **Speed is measured in iterations**, not computation, and on training
  error only. Generalisation is set aside (Appendix D.2). Linear networks
  reach poor MNIST error.
- **Slips.** §1.3 gives the scaling symmetry as a → λa, b → λb, but it must
  be b → b/λ to conserve a² − b². The introduction repeats its sentence
  about gradient propagation in nonlinear networks. Neither changes a
  result.

## Open questions

- A proof that small random weights converge to the decoupled trajectory,
  with a rate, for one hidden layer and at depth. This is the open
  question [THEORY-186](../theory.d/THEORY-186.md) and [THEORY-182](../theory.d/THEORY-182.md) share. The silent-alignment analyses
  [LIT-855](../literature.d/LIT-855.md) cites are where it is claimed.
- A theory of the singular-value spectrum of products of Gaussian matrices
  at depth, and a derivation, not an argument, of learning time from the
  end-to-end Jacobian's spectrum.
- Whether a random orthogonal start, which is not decoupled, learns its
  modes in strength order. If it does not, what replaces the stepwise
  schedule when the initial mode strengths are of order one?
- Whether orthogonal nonlinear networks near g = 1 keep near-isometric
  Jacobians during training, and not only at initialisation.
