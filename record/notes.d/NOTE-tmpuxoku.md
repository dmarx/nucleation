---
status: Read
paper: 'LIT-tmpagj3g'
title: 'Simoes, Dastani and van Ommen — Causal information bottleneck'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full from the arXiv preprint 2410.00535v5 (11 June 2025, "Accepted
    at UAI 2025"; v1 1 October 2024), 20 pp. with its appendix. Extracted
    with `pdftotext -layout`; page numbers are the PDF's pages, found per
    page with `pdftotext -f -l`, since the copy prints none. I read the
    abstract, §§1–10, the acknowledgements and references, and Appendices
    A–F (preliminaries, the Lagrangian and the macrovariable result with
    proofs, interventions on abstractions, equivalence of abstractions,
    the learning algorithms, and the supplementary experiments with Tables
    1–2 and Figs. 3–6), with all captions. The parallel-coordinate plots
    did not survive extraction; their captions did. Earlier arXiv versions
    and the PMLR version were not read. Check (numpy; my script, not the
    authors' code): on the Genetic Mutations SCM of Fig. 2b at the noise
    of Fig. 1c, I computed p(y | do(x)) by intervening in the SCM and by
    the backdoor formula over S (they agree), found four causal classes,
    the values of θ(x), against ten classes of p(y | x), and confirmed
    Proposition 20 there: the θ-encoder keeps all of Ic(Y | do(X)) =
    0.798 bits under the uniform protocol, no one of 20,000 random
    stochastic four-state encoders exceeded it (best 0.340), and merging
    two classes lowers it to 0.697.
date: '2026-10-29'
summary: >-
  The causal information bottleneck trades I(X; T), the information a
  variable abstraction T keeps about X, against Ic(Y | do(T)), the
  reduction in Y's entropy when T is set by intervention under a chosen
  protocol over X. An intervention on T is defined as a mixture of
  interventions on X, weighted by Bayes inversion of the encoder under a
  uniform prior, and is identifiable by a backdoor formula. At full weight
  on control, the optimum is the partition of X by p(y | do(x)), the
  causal macrovariables of Chalupka et al., which the ordinary bottleneck
  misses under confounding. Three toy SCMs confirm it; nothing larger is
  tried.
---
<!-- inactive-ok-file: CLAIM-259 CLAIM-348 — Proposed; the claims this reading bears on, cited as open -->

# NOTE-tmpuxoku: Simoes, Dastani and van Ommen — Causal information bottleneck

## Contribution

The paper defines an optimal causal variable abstraction (OCVA) of a set of
variables X for a target Y as a stochastic function T of X that keeps a
chosen amount D of causal control over Y, measured by causal information
gain, while keeping as little information about X as possible
(Definition 2, p. 3). It relaxes this to the causal information bottleneck
Lagrangian L_CIB = I(X; T) − βIc(Y | do(T)) (Definition 3, p. 4), defines
what an intervention on T means (Definitions 4–5, p. 4), derives a backdoor
formula that makes the Lagrangian computable from observational data and
a backdoor set (Proposition 6, pp. 4–5), shows that at full control the
optimum is the causal partition (Proposition 20, p. 14), and learns
abstractions by projected gradient descent and a simulated-annealing
variant on three toy SCMs (§8, pp. 5–7).

## Key insight

Compression relative to a target depends on whether the target is
prediction or control. The ordinary bottleneck keeps what X tells about Y;
under confounding that includes what X's correlates tell, so it keeps
distinctions no intervention on X could exploit and merges none that
matter only causally. The causal version keeps exactly what setting X does
to Y. "When X and Y are heavily confounded, the IB method will create an
abstraction T that preserves the information X has about Y, but a
significant portion of this information is spurious from a causal
perspective" (p. 2). At its extreme the causal version recovers Chalupka
et al.'s macrovariables: "the full-control OCVAs with |RT| = NC are exactly
the causal macrovariables from Chalupka et al. [2016a]" (p. 8).

## Assumptions

- **Discrete variables**; T has a chosen finite range R_T (p. 2).
- **A v-abstraction is a function of X and independent noise** (Definition
  1, p. 3), so T ⫫ Y | X.
- **Causal control** is causal information gain under an intervention
  protocol: Ic(Y | do(X ∼ X*)) = H(Y) − E_{x∼X*} H(Y | do(X = x))
  (Definitions 12–13, p. 12), with "a uniform protocol pX* = p* over the
  low-level variables X" (p. 12). It "can be negative, in contrast with
  mutual information" (p. 12). Compression, I(X; T), is computed under the
  observational p(x) (p. 4). The two terms use different distributions
  over X.
- **Interventions on T are stipulated.** The intervention decoder
  p*(x | t) ∝ q(t | x)p*(x) (Definition 4, p. 4), and
  p(v | do(T = t)) = Σ_x p*(x | t) p(v | do(X = x)) (Definition 5). The
  authors defend the choice: "our T is an artificial, conceptual
  abstraction of X. Thus, we can define the mechanism that propagates
  interventions on T to X. The key requirement is that it is applied
  consistently" (p. 15).
- **A backdoor set Z relative to (X, Y) is observed** (Assumption 8, p. 5).
  "The CIB method does not require access to the full DAG; it only
  requires that post-intervention distributions are either provided or
  identifiable" (p. 2).
- **β is fixed**, not solved for; the simplex constraint is imposed by
  projection, outside the Lagrangian (Remark 17, p. 13).

## Key results

- **Proposition 6 (backdoor formula for abstractions, pp. 4–5; proof
  p. 15):** p(y | do(T = t)) = Σ_z p(z) Σ_x p(y | x, z) p*(x | t). Immediate
  from Definition 5 and the ordinary backdoor formula. Checked on the
  Genetic Mutations SCM against direct intervention.
- **Proposition 18 (p. 14):** with γ = β/(1 + β), L^γ = (1 − γ)I(X; T) −
  γIc(Y | do(T)) is L^β/(1 + β), so the minimisers agree; γ = 1 stands for
  β = ∞. (The proof's first line writes I(Y; X) for I(X; T), a typo.)
- **Proposition 20 (pp. 14–15):** if p(y | do(x)) partitions R_X into n
  classes, then at γ = 1 an encoder that maps each class deterministically
  to its own value of T is optimal whenever |R_T| ≥ n, and when |R_T| = n
  every optimum is the causal partition. The proof uses only the strict
  concavity of entropy: for any encoder, Hc(Y | do(T)) = Σ_t p*(t)
  H[Σ_x p*(x | t) p_do(x)] ≥ Σ_t p*(t) Σ_x p*(x | t) H[p_do(x)], and the
  causal partition attains the right-hand side (eq. 15). Checked
  numerically (history).
- **Proposition 23 (p. 16):** variation of information zero implies
  equivalence up to relabelling (Definition 9, p. 5), with the converse
  when one abstraction is deterministic.
- **Experiments (§8, pp. 5–7; Figs. 1, 2, 5, 6):** three SCMs, each
  checked for (a) recovery of the ground truth at γ = 1 (VI = 0), (b)
  I(X; T) = 0 at γ = 0, and (c) causal information gain non-decreasing in
  γ (p. 6). Odd and Even (X uniform on 0–6, Y its parity with noise):
  ground truth found in 100% of runs at γ = 1. Confounded Addition (Fig.
  2a, with W confounding X₁ and Y): 98%. Genetic Mutations (Fig. 2b, with
  strain S confounding X₃, X₄ and Y, and an epistatic term
  (2 − X₃)X₁X₂): 95%. All three checks pass in every experiment and for
  other noise settings (Fig. 5, p. 18).
- **IB comparison (Appendix F.2, pp. 18–20):** the ordinary bottleneck at
  γ = 1 never finds the causal ground truth when there is confounding.
  On Confounded Addition it separates (X₁, X₂) = (0, 1) from (1, 0), which
  have the same effect on Y (Table 1, p. 19); on Genetic Mutations it
  misses X₃'s protective effect and is not invariant in X₄ (Table 2, p. 20).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | p(y | do(T = t)) is identifiable from observational data and a backdoor set, by Proposition 6's formula | strong | short proof from Definition 5; checked numerically |
| C2 | At γ = 1 with |R_T| ≥ n the causal partition optimises the CIB, uniquely up to relabelling when |R_T| = n | strong | Proposition 20, proof by concavity; checked on one SCM |
| C3 | The OCVA at γ = 1 coincides with Chalupka et al.'s causal macrovariables when |R_T| equals the number of causal classes | strong | follows from C2 and Definition 19 |
| C4 | Projected (simulated-annealing) gradient descent finds the CIB optimum in the three toy problems in 95–100% of runs at γ = 1 | moderate | §8, ensembles of 4–12 optimisers; a non-surjectivity penalty added for γ = 1 (p. 17) |
| C5 | The IB fails to learn the causal partition under confounding | moderate | Appendix F.2, two confounded SCMs; expected from the definitions |
| C6 | OCVAs give insight into causal interactions not clear from the input data and help select interventions | weak | argued from the Genetic Mutations example (p. 7); no comparison with direct inspection of p(y | do(x)) |
| C7 | Intermediate γ gives sensible trade-offs between compression and control | weak | check (c), monotonicity only; no ground truth for γ ∉ {0, 1} (p. 6) |

## Method

The CIB is minimised over encoders q_{T|X} constrained to a product of
simplices, by projected gradient descent with Euclidean projection onto
each simplex (Duchi et al.), or by a simulated-annealing variant that
sometimes accepts a random neighbour (Appendix E, pp. 16–17). Gradient
clipping, cycle detection and a penalty against encoders that leave some
value of T unused were added; the penalty "greatly improved the accuracy
of the optimizer" at γ = 1 (p. 17).

## Concepts

- **Variable abstraction (v-abstraction)** — a variable that is a function
  of X and independent noise, given by its encoder q(t | x) (Definition 1,
  p. 3). Distinct from causal abstraction of a whole model (footnote 1,
  p. 2).
- **Interventional sufficiency** — Ic(Y | do(T)) = D (Definition 2, C1).
- **Intervention decoder** — p*(x | t), Bayes inversion of the encoder
  under the protocol prior (Definition 4).
- **Causal class / macrovariable** — a class of x with the same
  p(y | do(x)) (Definition 19, p. 14).
- **Equivalent abstractions** — encoders equal up to a bijection of T's
  values (Definition 9, p. 5).

## Connections

- **Tishby, Pereira and Bialek** (the IB) and **Kolchinsky et al.** on its
  caveats; **Achille and Soatto** for the axiomatic optimal representation
  that Definition 2 extends (pp. 2–3).
- **Chalupka, Eberhardt and Perona** (causal macrovariables), subsumed at
  γ = 1 (p. 8). **Höltgen** and **Jammalamadaka et al.** used the ordinary
  IB for the same goal and are limited to unconfounded cases (p. 8).
- **Causal abstraction of models** (Rubenstein et al.; Beckers and Halpern;
  Beckers, Eberhardt and Halpern), and its learning by Zennaro et al.,
  Xia and Bareinboim and Felekis et al. (LIT-tmpdrddx): "In contrast, our
  method does not learn an abstraction of an SCM, but a an abstraction of a
  (set of) variable(s) X which is causally relevant" (p. 8).
- **Simoes et al. 2023, 2024** define causal entropy and causal
  information gain (p. 3).
- In the record, **THEORY-743** is the observational counterpart: every IB
  optimum is a stochastic coarsening of the minimal sufficient partition
  by p(y | x), reached as β → ∞ and in general not at finite β.
  Proposition 20 is the same statement with p(y | do(x)) for p(y | x), at
  γ = 1 exactly.

## Bearing on the record

- **CLAIM-152 and CLAIM-348: support, in a formal setting.** An OCVA is
  defined relative to a target Y and to a level D of control; change Y and
  a different partition is optimal. The paper's own example shows the
  record's point that adequacy is fixed by the target: the optimal
  abstraction of four mutation sites for body mass ignores X₄ entirely
  (p. 7). CLAIM-348's caution holds unchanged: the paper chooses Y and
  never argues that body mass is the outcome that matters. It adds a second
  relativity the record should note, to the intervention protocol: Ic is
  computed under a uniform distribution over interventions on X (p. 12),
  and a different protocol weights the classes differently.
- **CLAIM-259 and the record's Blackwell material: a single-task, single-
  protocol relative of the decision term, not an instance.** CLAIM-259's
  D⁺ is a supremum of risk increases over a family of decision problems
  and priors, vanishing exactly at Blackwell dominance. The CIB scores one
  target by one entropy-based quantity under one protocol. Proposition 20's
  proof is the concavity step that also underlies the easy direction of
  Blackwell's theorem (THEORY-1096): averaging the interventional laws over
  a cell cannot lower the expected entropy. So a coarsening of X never
  gains causal information over X (the inequality in the proof), which is
  CLAIM-409's refinement monotonicity for a fixed target, with
  "interventional" in place of "predictive" sufficiency.
- **CLAIM-455: compatible, and orthogonal.** CLAIM-455 is about a bounded
  receiver for whom a garbling can raise legibility. The CIB has no bounded
  receiver: Ic is computed from exact distributions. The two would meet
  if T were scored by what a bounded agent can do with it.
- **CLAIM-409: consistent, as above**, and the paper's check (c), causal
  information gain non-decreasing in γ, is the optimiser-level counterpart.
- **CLAIM-399 and THEORY-849: a different object.** The CIB abstracts a
  variable for a target, not a model, and its intervention on T is defined
  by fiat, so the question of whether high-level noise carries what the
  coarse state drops does not arise in CLAIM-399's form. The stipulated
  decoder means do(T = t) is a randomised intervention on X; nothing makes
  it the mechanism of any physical T (p. 15).
- **The difference between supporting prediction and supporting control**,
  which the LIT's "Why this is here" names, is shown here exactly: on the
  Genetic Mutations SCM the observational partition has ten classes and
  the causal one four (my computation), and the IB's γ = 1 abstraction is
  not the causal one (Appendix F.2).
- **Two THEORYs**: THEORY-tmp2fevr (Proposition 20, Active) and
  THEORY-tmppip5e (IB against CIB under confounding in the toy SCMs,
  Proposed).
- **No instruction for ML practice**; not an anthology candidate.

## Limitations

- **Toy problems only.** Seven, four and sixteen values of X; the authors
  say scaling "may require modifications to deal with local minima"
  (p. 8).
- **Ground truth only at γ ∈ {0, 1}.** Check (c) is monotonicity; the
  intermediate trade-offs have no external standard.
- **A stipulated intervention on T** and a uniform protocol. Both are
  choices, defended as consistent (p. 15), and the results depend on them.
- **A backdoor set must be known.** The causal knowledge the method needs
  is in Assumption 8; the full DAG is not needed, but an adjustment set is.
- **Mixed distributions.** Compression is under observational p(x),
  control under the uniform protocol, so the Lagrangian trades quantities
  defined on different distributions over X; the paper does not discuss
  this.
- **Optimiser tuning.** Learning rates up to 10⁴ and a penalty against
  non-surjective encoders were needed (pp. 7, 17).
- **Small errors**: "the Conditional Information Bottleneck (CIB)" for the
  causal one (p. 6); I(Y; X) for I(X; T) in Proposition 18's proof (p. 14).

## Open questions

- How does the optimum depend on the intervention protocol? An experiment
  with a non-uniform p*, or with the observational p(x) as protocol,
  would show whether the γ < 1 abstractions are stable.
- Does the CIB hierarchy over γ nest, each coarser abstraction a
  coarsening of the finer? THEORY-743 leaves the same question open for
  the IB.
- For continuous X, does a variational version keep Proposition 20? The
  authors propose variational autoencoders (p. 8); the concavity argument
  needs exact entropies.
