<!-- scratch/manuscripts/from-obstruction-to-reorganization/background/formal-apparatus-2.md -->

# Background digest: the formal-apparatus line, second half

**Update of 2026-11-21.** This digest is a snapshot read on 2026-11-20 and is left as read. Since then the record has gathered the manuscript's principle accounts as a line, `learning-and-inquiry` (ADR-130, Active), over SYNTHESIS-109 to SYNTHESIS-116, with a line account, SYNTHESIS-tmpt1te9 (Proposed). **Statuses changed since:** CLAIM-625, CLAIM-639, CLAIM-759 and CLAIM-761 are Active. **New material bearing on this digest:** SYNTHESIS-tmp69tyj (Proposed), a part account of `formal-apparatus` holding that a power law does not identify its mechanism; TERM-tmpol232 (separation, in three senses) and TERM-tmptiim0 (sloppy), Proposed; CLAIM-tmpjbee7 (near criticality, harder to separate into levels and easier to classify, Proposed); ARG-tmp09yqc (Rejected: a finite correlation length does not give near-decomposability); CLAIM-tmpcgvcp and CLAIM-tmpcg4uu (sloppiness against singularity, Proposed). SYNTHESIS-048 is now at version 2. Part I §§2.3–2.5 use them.

Scope: SYNTHESIS-081 through SYNTHESIS-089, SYNTHESIS-107 and SYNTHESIS-108,
with the CLAIMs and TERMs they rest on that matter most, and the
neighbouring entries on comparing experiments, coarse-graining,
identifiability and legibility that the brief named. Every account read
here is **Proposed**, and each says it "adds nothing of its own; its
standing is its components'" (SYNTHESIS-081, and the same clause in
082 to 089). Statuses below are as the files read on 2026-11-20. Quotes
are exact; paraphrase is marked by the absence of quotation marks.

The line account, SYNTHESIS-088, describes what kind of thing this region
is: "The line is a collection more than an argument. Its entries average
three linked pairs each, against about nine in distributed-agency and
pragmatic-transport, and a fifth of them link to nothing in it. They are
general results other lines use." It explicitly does not say "That the
eighteen parts are one inquiry" (SYNTHESIS-088).

---

## 1. Core concepts (TERMs)

- **TERM-069, observational equivalence under a probe family** (Active).
  "Two objects P and Q are **observationally equivalent under Φ** when
  (φ_i)#P = (φ_i)#Q for every i." It is "coarser than identity" unless
  the family is rich enough; "Rich families separate" (Cramér–Wold,
  Lovász, restricted Yoneda); and matching each probe's marginal "leaves
  the joint across probes unconstrained". It is "Not interventional
  equivalence unless the family contains the interventions" (TERM-069,
  citing CASE-125 and CLAIM-407), and "Not evidence that structure was
  preserved, unless the probes were chosen independently of the objects"
  (TERM-069, citing CLAIM-322).

- **TERM-064, legibility** (Active; first line distributed-agency). "whether
  the observer, with the rules, categories and resources it actually has,
  can recover the distinction from what it is given and bring it to bear on
  the task; a relation among a representation, an observer's rule class,
  its resources and a task, bounded above by what the source makes
  possible for an ideal receiver, and directed" (TERM-064 title). Its
  formal core is CLAIM-199's usable information; one operationalization is
  L_{o,𝒬,B}(T) = −inf_{π∈Π_{o,B}} E[ℓ_𝒬(J, π(T(X)))], with the caution
  that "the loss function and task family must be specified independently;
  otherwise whoever controls the scoring criterion also controls what
  counts as legible" (TERM-064). Legibility "need not be monotone in
  informational refinement for bounded observers, although ideal
  information sufficiency remains monotone for a fixed target" (TERM-064,
  quoting A22; the XOR witness is CLAIM-455). It distinguishes the
  "legibility regime", "the maintained organization of observation
  channels, classifications, attention and interpretive procedures",
  which is "wider than Π_{o,B}" (TERM-064). Its note of 2026-11-15 records
  that erasure is relative to a class of reader, and that "The term has no
  place for an observer that induces the distinction it reports"
  (TERM-064).

- **TERM-085, correctability** (Active; first line distributed-agency).
  "the chance that the arrangement, starting from the description of the
  problem it actually has, finds, authorizes, coordinates and carries out
  a plan achieving the objective before the deadline and within its
  resources": α_J(s, q, H, B; G) = sup over π in Π(G, q, B) of
  Pr_s^π(T_J ≤ H) (TERM-085). "Planning is not free", and "A sufficiently
  long search can make an otherwise available remedy unusable" (TERM-085).
  It is "A structured attainable set, not a single accountability score"
  (TERM-085). Its note of 2026-10-31 gives the bound tying it to
  legibility (see §3.6).

- **TERM-065, effective-description regime** (Active). ℛ = (X, 𝒬, ℐ, ℬ, ε, τ):
  "the system, query family, intervention family, resource bounds,
  tolerance and horizon under which a candidate description's adequacy is
  assessed", "kept apart from the description T it evaluates, so that
  rival descriptions are compared under one regime" (TERM-065).

- **TERM-068, closure, and which sense** (Active). Lists at least eight
  senses; sense 1, informational closure, is I(X⃗_t; Z_{t+1} | Z⃗_t) = 0,
  "and is no mark of a system" (TERM-068 summary).

- **TERM-098, concept, as realized by an organization** (Proposed; line
  learned-structure). "a reusable, systematically consequential pattern of
  distinctions, applicable across a stated range of contexts with
  inferential or operational consequences", with two marks, "Reuse" and
  "Systematic consequence and counterfactual reach" (TERM-098).
  "Conceptual corrigibility", "the capacity to find and revise
  inadequacies in a concept's application", is "a further capacity, and
  not part of the definition"; "An incorrigible concept is still a
  concept" (TERM-098). QUESTION-360 asks what would settle it.

- **TERM-077, ordinal potential** (Active). An ordering that every winning
  move climbs; it "exists exactly when the wins never cycle" and is "fixed
  only up to a class"; of four senses of "common currency", "They are not
  one chain of implications" (SYNTHESIS-089, reporting TERM-077).

- **TERM-046, notation** (Active): records "that δ/ε is used in two senses,
  a spectral gap against off-block coupling and a posterior effect against
  its uncertainty, and that treating them as one is an assumption carried
  over from [MOM-CLM-160]" (TERM-046).

- **TERM-088, individuation, and which sense** (Active): descriptive,
  dynamical, constitutive, and organizational autonomy; these "are neither
  four necessary stages nor four universally ranked degrees of existence"
  (TERM-088, quoting A18).

---

## 2. Central theses (CLAIMs), by part

Format: code, status, warrant, role; statement; what it rests on.

### 2.1 When a structure earns a name (SYNTHESIS-081)

- **CLAIM-154** (Active, demonstrated, thesis). Keep a candidate "if and
  only if d'² > Occam", since ln BF(keep) = ½(d'² − Occam) by
  Savage–Dickey; "The threshold is not a taste parameter"; "The rule
  prices a candidate; it does not find one." Narrowed to models "regular at
  the parameters that switch it off". Grounds THEORY-081, THEORY-087; uses
  TERM-046; no rests_on.
- **CLAIM-188** (Active, demonstrated, counter; objects to CLAIM-154). Where
  the model is singular at switch-off, the Gaussian Occam term
  "overcharges keeping the candidate by (d/2 − λ) log n + (m − 1) log log
  n", so "the rule prunes candidates the Bayes factor keeps"; "more data
  does not wash it out" (SYNTHESIS-081). Checked on CASE-152.
- **CLAIM-164** (Active, demonstrated, thesis). "the gap picks the object,
  and the object is a vector only when its own gap is wide"; core is
  Davis–Kahan. Complements CLAIM-154: "the Occam factor says whether the
  gap is big enough."
- **CLAIM-377** (Active, demonstrated, thesis). Fisher βJᵀJ and NTK Gram JJᵀ
  share non-zero eigenvalues (times β) and multiplicities.
- **CLAIM-388** (Active, demonstrated, thesis). In a uniform-coupling VAR(1)
  "the sum of all units is exactly dynamically independent at every stable
  coupling strength", while every partition "couples as strongly across
  its edges as within them"; "closure of a collective variable does not
  imply that it is the aggregate of a weakly coupled block" (SYNTHESIS-081).
- **CLAIM-307** (Active, demonstrated, thesis). Evidence and retrieval
  "move in opposite directions with copy count"; "the bins a deadline
  forces are often the ones the data least supports"; "Use frequency
  enters retrieval and not detection." Grounds CASE-094.
- **CLAIM-309** (Active, demonstrated, thesis). "a preference that rises and
  then falls with milk is over the ratio and cannot be a d′" (SYNTHESIS-081);
  case CASE-096.

### 2.2 Gluing and contextuality (SYNTHESIS-082)

- **CLAIM-131** (Active, demonstrated, granted). "In the ordinary event
  sheaf, a compatible family of local sections already glues to a global
  section"; the obstruction lies "in its supports or distributions"
  (CLAIM-131 title), and failure over supports "is a stronger obstruction
  than failure of the second" (SYNTHESIS-082).
- **CLAIM-037** (Proposed, interpretive, thesis; rests on CLAIM-374).
  Contextuality is "a failure of global extension, distinct from ordinary
  context dependence, and needs Contextuality-by-Default when marginals
  shift with context". It "goes Active on a comparison of a sheaf route
  with CbD 2.0 on one signalling data set" (SYNTHESIS-082).
- **CLAIM-374** (Active, demonstrated): "On a consistently connected system,
  Contextuality-by-Default and the sheaf criterion agree".
- **CLAIM-041, CLAIM-197, CLAIM-144, CLAIM-310** (all Active, demonstrated):
  order effects, disjoint contexts, frames and sortings of determinate
  objects are no failure of gluing; CLAIM-197: "A gluing failure needs an
  overlap", and "which families count as covers decides whether anything
  glues"; CLAIM-310 as narrowed by CLAIM-313 (Active, demonstrated,
  counter): "sortings conflict as arrangements only under a one-copy
  constraint" (SYNTHESIS-082).
- **CLAIM-141** (Active, demonstrated, granted): "A distributional fixed
  point exists even though no deterministic fixed point exists", while "a
  model with no global assignment consistent with its supports has no
  global distribution either"; "Always specify the domain of global
  realizability" (SYNTHESIS-082).
- **CLAIM-044** (Proposed, interpretive): ambiguity "admits several
  compatible global assignments, a contextual one admits none"; its own
  note finds the title fails under both readings of "admits none"
  (SYNTHESIS-082).
- **CLAIM-625** (Proposed, demonstrated): "gluing is about agreement on
  overlaps; continuation is about whether a history has an admissible
  future"; "a coherent history can be terminal" (SYNTHESIS-082).
- **CLAIM-623** (Proposed, demonstrated): forgetting a hidden mechanism can
  yield a presheaf of realizable observations that is not a sheaf, where
  "each local observation may have a valid hidden realization, while no
  single hidden realization supports the combined observed history";
  instance CASE-224; concluded by ARG-074 (Proposed).

### 2.3 Readouts and kernels (SYNTHESIS-083)

- **CLAIM-290** (Active, demonstrated): same centred Gram matrix means "a
  translation and an orthogonal map".
- **CLAIM-379** (Active, demonstrated; rests on CLAIM-290): for ridge b > 0
  readouts "cannot tell apart two centred representations of the same
  width exactly when one is an orthogonal transformation of the other";
  at b = 0 only the column space is seen.
- **CLAIM-385** (Active, demonstrated): a commuting symmetry forces
  degeneracy, but "the spectrum fixes neither the group nor a basis";
  "What a spectrum carries is the isotypic dimension count of whatever
  group is present, not the group" (SYNTHESIS-083).
- **CLAIM-269** (Active, demonstrated; rests on CLAIM-379, CLAIM-385): "no
  such readout supplies a distinction beyond that symmetry".

### 2.4 Coarse-graining and renormalization (SYNTHESIS-084)

Three Open questions, no claims: QUESTION-185 (whether the information
bottleneck's first transition on a lattice slab is the bifurcation "only
under some further condition, perhaps a symmetry"), QUESTION-205 (whether
Kadanoff-family exactness "keeps the relevant operators, or still leaves
the coarse variables free"), QUESTION-232 (whether the mutual-information
maximizer agrees with renormalization "where renormalization's variables
are unknown") (SYNTHESIS-084).

### 2.5 Random projections (SYNTHESIS-085)

QUESTION-120 (Open), QUESTION-251 (Answered: "the two sufficiency proofs
are one argument over two families", while lower bounds use different
arguments), QUESTION-168 (Open: universality of the ℓ₁ recovery
transition) (SYNTHESIS-085).

### 2.6 Capture, legibility state, obstructions (SYNTHESIS-086)

- **CLAIM-340** (Active, demonstrated; rests on CLAIM-330): γ = 4ηs(κ′ − κ̄);
  "The order in time is necessary for learning. It does not make the
  scoring independent."
- **CLAIM-400** (Active, demonstrated; rests on CLAIM-330, CLAIM-340; uses
  TERM-064): a maintained legibility state shifts the threshold as β +
  νε/(1 − λ) and δ + με/(1 − λ), and away from it adds a slow mode: "for
  whether symmetry breaks, it is [renamed]; for how long a lean lasts and
  how the system returns, it is not" (SYNTHESIS-086).
- **CLAIM-346** (Active, demonstrated): feasibility, aggregation and
  epistemic coordination are independent obstructions: "Each can occur
  without the other two."

### 2.7 Delegation accounting (SYNTHESIS-087)

- **CLAIM-282** (Active, demonstrated, granted), **CLAIM-375** (Active,
  demonstrated; rests on CLAIM-282), **CLAIM-502** (Active, demonstrated;
  objects to CLAIM-282). Damped recursive delegation lets an operator
  amplify itself without self-grants; one-hop allocation makes authority
  "exactly independent" of own grants; leave-one-out keeps independence
  beyond one hop but "[CLAIM-375]'s guarantee does not carry over" (the
  decision moved toward the granter in 1,772 of 2,141 trials)
  (SYNTHESIS-087).

### 2.8 Ordinal potentials (SYNTHESIS-089)

- **CLAIM-434** (Active, demonstrated): a potential exists on a finite set
  "exactly when no chain of winning moves returns to where it began";
  "the gradient is not an ordinal potential"; "a record fixes a class of
  potentials rather than one".
- **CLAIM-436** (Active, demonstrated): "admitting an ordering is strictly
  weaker than admitting a currency".
- **CLAIM-369** (Active, demonstrated): Lotka–Volterra under A = UᵀU is
  multiplicative gradient flow on a convex objective; for a non-potential
  field "the split depends on a chosen metric and convention"
  (SYNTHESIS-089).

### 2.9 How an equivalence becomes a unit (SYNTHESIS-108, SYNTHESIS-107)

- **CLAIM-762** (Proposed, interpretive, thesis; the owner's U10; rests on
  CLAIM-478, CLAIM-154; uses TERM-098). "Collapsing differences that do not
  matter into equivalence classes is how those classes come to be reified
  as new distinctions"; "substantive only where the classes are closed
  under the system's own operations and are reused" (title). The condition
  is a congruence, "q∘F = F̄∘q", with the minimal automaton (Myhill–Nerode)
  as textbook case (CLAIM-762). Its completion: identification within
  basins plus differentiation between them, as in CLAIM-408's pitchfork
  (CLAIM-762). It declines A's rate condition ("selective contraction")
  because CLAIM-388 holds an exactly closed collective variable with no
  block (CLAIM-762).
- **CLAIM-478** (Proposed, interpretive; the owner's): "what is a
  realization at one scale works as a constraint at another".
- **CLAIM-408** (Active, demonstrated): a neutral constraint, by weakening,
  "can destabilize the equal allocation and make persistent unequal
  allocations stable" (pitchfork ḋ = (α − κ)d − βd³).
- **CLAIM-481** (Active, demonstrated, counter): "Coupling does not by itself
  separate time scales"; separation comes "where the coupling dissipates
  relative differences faster than collective ones".
- **CLAIM-402** (Active, interpretive; rests on CLAIM-342): predictive
  success warrants a real kind "only when the evidence in those contexts
  does not pass through the category's own use, or when the effect of that
  use is modelled".
- **CLAIM-759** (Proposed, demonstrated; the assistant's): data symmetry
  forces a balanced partition of units "only where the symmetry group acts
  on the units by permuting them"; for vocabulary above width, the
  relabelling group "cannot permute the units nontrivially at all".
- SYNTHESIS-107's chain links CLAIM-762 → CLAIM-761 (Proposed,
  interpretive: "A stabilized constraint can be stored work") → CLAIM-754
  (Proposed, interpretive: three frontiers "move separately") → CLAIM-475
  (Active, interpretive) and CLAIM-756 (Proposed, demonstrated), with
  separations CLAIM-443, CLAIM-755, CLAIM-760, CLAIM-352, CLAIM-758,
  CLAIM-605 (SYNTHESIS-107).

### 2.10 Coarse-graining, comparison of experiments, identifiability (neighbouring parts the brief named)

- **CLAIM-152** (Active, demonstrated, thesis). "Any individuation built on
  sufficiency is relative to the target it is sufficient for: fix the
  outcomes differently and a different partition wins". "In this record it
  is the standing caution on every boundary criterion" (CLAIM-152). Notes
  add that the target is relative to the instrument (Crutchfield and
  Shalizi's logistic map) and, after Carnap, to the vocabulary (CLAIM-152).
- **CLAIM-350** (Active, demonstrated, granted; complements CLAIM-152). A
  coarse-graining "preserves a deterministic judgment exactly when the
  judgment is constant on its fibres".
- **CLAIM-348** (Active, interpretive; rests on CLAIM-350, CLAIM-152,
  CLAIM-060): "adequacy is fixed by the evaluative target, and the target
  cannot be justified solely by the description that preserves it".
- **CLAIM-535** (Active, demonstrated; rests on CLAIM-350; uses TERM-064):
  a policy acceptable everywhere exists exactly when each observation
  class shares an acceptable action; "which distinctions must be made
  legible depends on which acceptable action the organization commits to".
- **CLAIM-407** (Active, demonstrated; rests on CLAIM-350): an exactly closed
  coarse-graining "need not preserve its responses to an intervention on
  the mechanism".
- **CLAIM-409** (Active, demonstrated; rests on CLAIM-407; uses TERM-068):
  fixed-target deficiency is refinement-monotone, closure is "monotone in
  neither direction".
- **CLAIM-497** (Active, **interpretive**, thesis): "A system's causes are
  found at the coarsest description whose interventions are unambiguous";
  "no coarse-graining carries more causal information than the micro
  description it supervenes on". Grounds THEORY-1167, THEORY-1169.
- **CLAIM-387** (Active, demonstrated) and **CLAIM-392** (Active,
  demonstrated; rests on CLAIM-387): information-bottleneck optima at two
  budgets "need not be nested", deterministically and stochastically.
- **CLAIM-264** (Active, demonstrated): "equivalence under a probe family is
  coarser than identity unless the family is rich enough". **CLAIM-574**
  (Active, demonstrated; rests on CLAIM-264; uses TERM-069, TERM-065):
  distinctions "only grow as nested probe families grow". **CLAIM-322**
  (Active, interpretive; rests on CLAIM-264): probe agreement is evidence
  only if the family "was chosen independently of the comparison".
- **CLAIM-380, CLAIM-503** (Active, demonstrated), **CLAIM-381** (Active,
  demonstrated; rests on CLAIM-011), **CLAIM-268** (Active, demonstrated):
  finite Blackwell order, Le Cam deficiency, stitching.
- **CLAIM-199** (Active, interpretive): "Blackwell's order bounds what a
  rendering makes possible for any receiver, and a given receiver's access
  is usable information relative to the rules it can apply". **CLAIM-225**
  (Active, demonstrated, counter): "Blackwell's order measures what an
  ideal decision-maker could do, not what a given receiver can
  reconstruct". **CLAIM-455** (Active, demonstrated): one transformation can
  make one task's distinction legible and another's illegible to the same
  observer.
- **CLAIM-148** (Active, demonstrated, granted): a factorization is
  identified only up to a gauge; "automorphisms of the data act on the
  factors only when the factorization is identifiable". **CLAIM-452**
  (Active, demonstrated): authority shares are identifiable "exactly when
  the processes' stacked profiles over those contexts are affinely
  independent".
- **CLAIM-011** (Active, demonstrated, granted): intertwining with an
  uninformative correspondence "is vacuous or lossy", so it "must be
  anchored to independently measured distinctions and evaluated on tasks
  other than those it was estimated on".
- **CLAIM-581, CLAIM-557, CLAIM-592** (Active, demonstrated) and **CLAIM-639**
  (Proposed, demonstrated): budgeted reachability merges, observation
  splits (§3.5).

---

## 3. Formal results, stated precisely

### 3.1 Coarse-graining a judgment, a target, a cause

- **Judgment factorization (CLAIM-350).** For C: X → Z and J: X → Y on one
  state set, J = j∘C for some j iff C(x₁) = C(x₂) ⇒ J(x₁) = J(x₂); j is
  "unique on the image, and free off it"; "C preserves J exactly when the
  partition of X into C's fibres refines the partition into J's level
  sets", so "The coarsest coarse-graining that preserves J is therefore J's
  own partition" (CLAIM-350). The probabilistic version (P(Y | X = x)
  constant on fibres) is "Checked here for the finite case only"; the
  decision-theoretic version "is Blackwell's order ([THEORY-156]), not this
  lemma"; the causal version "is a definition, not a theorem" (CLAIM-350).
  Edge: "it says when a description keeps a judgment, never whether the
  judgment is right" (CLAIM-350). The record declined to file two TERMs
  (identifiability relative to an observational regime; target-preserving
  coarse-graining) because "Both are this claim's condition" (CLAIM-350,
  note of 2026-10-21).

- **Policy under coarse observation (CLAIM-535).** With h: W → O and
  acceptable sets A(w), an everywhere-acceptable π exists iff
  ∩_{w ∈ h⁻¹(o)} A(w) ≠ ∅ for every o. "A(w) ≠ ∅ for every w does not give a
  policy." Refinement: if h = g∘h′, π∘g works for h′, "Blackwell's easy
  direction, [THEORY-1096]". Witness of non-uniqueness: W = {1,2,3}, A(1) =
  {a}, A(2) = {a,b}, A(3) = {b}; partitions {1,2}|{3} and {1}|{2,3} both
  suffice, "neither refines the other", so "there is no unique coarsest
  sufficient observation" (CLAIM-535). Randomized bound (note of
  2026-11-17): for one observation class with disjoint acceptable sets "the
  worse is at most 1/2" (CLAIM-535).

- **Fixed-target deficiency vs. closure (CLAIM-409).** With Γ(T) =
  I(S; Y^(I) | T(S), I), if T₁ = g(T₂) then Γ(T₂) ≤ Γ(T₁), with equality
  exactly when Y^(I) ⊥ T₂ | T₁, I. Informational closure Δ_X(Z) is
  "monotone in neither direction": in the chain A_{t+1}, C_{t+1} fresh,
  B_{t+1} = A_{t+1} ⊕ C_t, Δ = 0 for A, 1 for (A,B), 0 for the full state;
  1 for A⊕B (CLAIM-409). Why: "Refining Z enlarges the conditioning set and
  also changes the target Z_{t+1}"; and "Decision informativeness and
  dynamical closure are not order-compatible" (CLAIM-409, quoting A7). The
  marginal-vs-joint form: with Y₁ = U, Y₂ = U ⊕ K, "I(K; Y₁) = I(K; Y₂) = 0
  and I(K; Y₁, Y₂) = 1 bit" (CLAIM-409).

- **Closure without intervention adequacy (CLAIM-407, CASE-125).** "Γ = 0
  exactly when, for every intervention ρ charges, the response kernels are
  constant on T's fibres"; in the hidden governance bit, an exactly closed
  output has Γ = ρ(h = 1) bits (CLAIM-407 title; CASE-125).

- **Causal proportionality (CLAIM-497, interpretive).** Under one
  intervention distribution at both levels, no coarse-graining of a
  transition exceeds micro effective information (THEORY-1167, Active);
  it keeps all of it iff it "merges only causes with identical rows
  P(Y | do(x)) and only effects with proportional columns" (THEORY-1169,
  Active, via CLAIM-497). The step "the coarsest is the one at which the
  causes are found" is "the record's own step, which is why this is a CLAIM
  and its warrant is interpretive" (CLAIM-497). Defeater: no "stable
  plateau" on systems with estimated effects (CLAIM-497).

- **Optima at different budgets need not nest (CLAIM-387, CLAIM-392).** For
  X uniform on four states and P(Y=1|x) = (0, 0, 1/8, 3/8), the deterministic
  IB optimum is {0,1,2 | 3} for 6.91 < β < 9.26 and {0,1 | 2,3} for
  9.26 < β < 16.06; "neither is a function of the other", they "cross", "so
  no rooted tree on the four states has both as prunings" (CLAIM-387).
  "raising the budget can reorganize the optimal partition rather than
  split it" (CLAIM-387 summary). Stochastic optima at β = 8 and 12 "admit no
  Markov chain X → T₂ → T₁" (CLAIM-392). CLAIM-409 marks the contrast: that
  result "is about optima, not about one description's deficiency".

### 3.2 Comparison of experiments: Blackwell, garbling, deficiency

- **Directed risk gap (CLAIM-380).** D⁺_Q(U → V; π) = sup_q [r_q,π(V) −
  r_q,π(U)]⁺, losses in [0,1], finite states and outcomes. (a) "A garbling
  never gains"; (b) D⁺ = 0 for every finite problem and prior iff U is
  reproducible from V by a Markov matrix (Blackwell's Theorem 6,
  THEORY-717); (c) it is directed; (d) A86's D_Q is its symmetrization
  (CLAIM-380).
- **Le Cam deficiency equals uniform decision gap (CLAIM-503).** For finite
  Θ, X, Y: δ := min_K max_θ TV(KP_θ, Q_θ) equals D, the supremum over
  [0,1]-loss problems of the least uniform gap; proof by composing N's
  rule with the optimal kernel and by von Neumann minimax on a bilinear
  form; "At ε = 0 this is the finite Blackwell–Sherman–Stein theorem"
  (CLAIM-503). Simondon note: "an experiment within ε of an uninformative
  one improves no decision problem with losses in [0, 1] by more than ε",
  so the decision-theoretic notion has "an ex ante criterion of failure",
  at the price of "fixing the states and the receivers' problems in
  advance" (CLAIM-503).
- **Exact fit is a garbling; deficiency is an LP (CLAIM-381).** A constant
  kernel fits every item only if averaged target responses do not vary
  with the item; an exact fit "is the definition of a garbling, with the
  item as the common parameter"; deficiency "is one linear programme"
  (CLAIM-381).
- **Stitching (CLAIM-268).** Reconstruction-form stitching (s∘r = t) makes t
  "a deterministic garbling of r about Y" and certifies "one direction of
  sufficiency"; task-loss stitching "is a difference of two upper bounds,
  so it orders neither minimum"; a 1×1-stitcher construction gives
  "Equivalent representations get different penalties"; "a failure to
  stitch is no evidence against sufficiency" (CLAIM-268).
- **Ideal vs. bounded receiver (CLAIM-199, CLAIM-225, CLAIM-455).** A
  garbling can raise usable information for a given receiver "but never
  above what the source makes possible" (CLAIM-199). Witness: X = (X₁, X₂)
  fair independent, an observer reading one coordinate: XOR task 50% error
  from raw, 0% from V = X₁ ⊕ X₂, and the reverse for the first-bit task
  (CLAIM-455; TERM-064).
- **Correctability bound (TERM-085, note of 2026-10-31).** For two equally
  likely failures needing mutually exclusive remedies, with description
  laws P₀ and P₁, "no remedy, actuator or decision rule acting on that
  description picks the right remedy with probability above
  (1 + TV(P₀, P₁))/2"; "This is the two-point Bayes-risk identity of Le
  Cam, the record's [CLAIM-199] and [CLAIM-503] applied to correction, and
  it is not filed as a new claim" (TERM-085). "no improvement in the
  downstream corrective mechanism can recover that lost distinction from
  those observations alone" (TERM-085, quoting A25).

### 3.3 Probes, profiles, identifiability

- **Restricted Yoneda (CLAIM-264).** The restricted functor A ↦ Hom(−, A)|_𝒬
  is fully faithful exactly when 𝒬 is dense; in a category with finite
  limits it is conservative exactly when 𝒬 is a strong generator, which is
  weaker: (ℤ/p)³ and the Heisenberg group mod p (p odd) have isomorphic
  profiles through ℤ, "and one group is abelian and the other is not"
  (CLAIM-264). "Identifying objects up to isomorphism does not need
  density" (CLAIM-264). Distributions: matching every marginal "leaves the
  joint across probes unconstrained", while Cramér–Wold and Lovász give
  separating families (CLAIM-264).
- **Monotonicity in the probe family (CLAIM-574).** If P₁ ⊆ P₂, a natural
  isomorphism of profiles on P₂ restricts to one on P₁; so "Raising the
  budget can only split classes"; "an equivalence a richer regime breaks
  was relative to its regime, not false" (CLAIM-574). Conditions: families
  nested (physical probes may not be: AFM can "manufacture distinctions as
  well as reveal them", CLAIM-574 DNA-origami note), and comparison over
  every probe: with tolerance 0.6, averaging distortion 1 on p₁ with 0 on
  p₂ makes a split pair equivalent (CLAIM-574). Checked by brute force on
  finite sets and 3,000 random posets (CLAIM-574).
- **Feasible probes (CLAIM-302).** "Equivalence under feasible tests can be
  much coarser than statistical equivalence"; unconditional by counting,
  efficiently samplable witnesses need pseudorandom generators (CLAIM-302).
- **Gauge (CLAIM-148).** R ≈ PQᵀ is invariant under P ↦ PA, Q ↦ QA⁻ᵀ;
  invariants are the predicted matrix, rank, singular values, row and
  column spaces and R̂ᵀR̂; QQᵀ and latent cosines are not; weight decay fixes
  the gauge up to O(k); for NMF the freedom is "{A invertible : WA ≥ 0 and
  A⁻¹H ≥ 0}", data-dependent and "not a group in general", with a worked
  non-permutation A (CLAIM-148). "Gauge is not automorphism" (CLAIM-148).
  CASE-097 is its instance: a topic persistent by construction "persists as
  no eigenmode", the nearest eigenvectors "about 51° apart" (CASE-097).
- **Readout freedom (CLAIM-290, CLAIM-379, CLAIM-385, CLAIM-269).** As in
  §2.3; the account states as not filed that a readout cannot see a
  rotation inside a degenerate eigenspace, because it is "a trivial instance
  of [CLAIM-379]" (SYNTHESIS-083).
- **Mixture identifiability (CLAIM-452).** For p_π(·|c) = Σ πᵢ pᵢ(·|c), shares
  are identifiable iff stacked profiles are affinely independent; "local
  and global identifiability coincide"; "k processes need at least k − 1
  contexts" with binary outcomes; "a condition checkable before any data"
  (CLAIM-452).

### 3.4 Naming criteria

- **Occam rule (CLAIM-154)**: ln BF(keep) = ½ μ²/σ² − ½ ln(s²/σ²); exact in
  the conjugate Gaussian case, re-checked "to 9 × 10⁻¹⁶"; Laplace
  approximation elsewhere, requiring non-singular Fisher at w = 0
  (CLAIM-154). Not a description length except for hypotheses "random
  under that prior" (CLAIM-154). Singular correction λ log n − (m − 1) log
  log n (CLAIM-188; THEORY-087, Active); CASE-152's model Y ∼ N(ab, 1) has
  λ = ½, multiplicity 2 (CASE-152).
- **Gap (CLAIM-164)**: subspace rotates by at most ‖δT‖/δ; "the dimension of
  the subspace this claim makes definite is not the number of slow
  variables" (CLAIM-164, note of 2026-10-20).
- **Copy count (CLAIM-307)**: d'² = cμ²/σ² vs. Occam ln(1 + cs²/σ²); search
  m/(c+1). "That the criteria disagree on every row is a fact of these
  parameters, not a theorem"; what is general is "the direction"
  (CLAIM-307).

### 3.5 Budgeted individuation: observe vs. act

- **CLAIM-581**: under peak-capacity costs on reversible moves the threshold
  is an extended pseudo-ultrametric, so "identifying configurations
  reachable within a budget is an equivalence relation at every budget and
  the identifications nest into one tree"; under additive costs
  "budgeted identification need not be transitive, and no such tree
  exists".
- **CLAIM-557**: "More resource for observing splits what can be told apart,
  and more resource for acting merges what can be turned into one
  another", so budgeted individuation "is indexed by a pair of budgets,
  not one".
- **CLAIM-592**: the two partitions agree "exactly at partitions common to
  the observer's refinement chain and the system's merge tree", and "the
  cost order decides which of those levels actually appear".
- **CLAIM-639** (Proposed): ε-knowledge of requirements fixes thresholds to ε
  but merges within 2ε can swap, so bringing a level into view "needs the
  requirement known to within half the gap between the merges that bound
  that level".
- **CLAIM-590**: "equivalence of possibilities is not equivalence of
  resource-bounded capabilities" (degree-4 vertex, 1.866 apart in the
  enriched category).

### 3.6 Gluing results

- CLAIM-374: on a consistently connected system, a maximally connected
  coupling exists "exactly when a global law has the contexts' laws as its
  marginals".
- CLAIM-623 / CASE-224: realizable (1, 0) and (0, 1) agree on period 2 and
  "no run realizes their pasting (1, 0, 1)"; ARG-074 adds that "a gluing
  failure need not show a disagreement on an overlap, and need not have an
  overlap" (SYNTHESIS-082).
- CLAIM-625: for time-invariant dynamics a viable history extends "exactly
  when its endpoint lies in the finite-horizon viability kernel"
  (SYNTHESIS-082).

### 3.7 Units, symmetry, potentials

- **CLAIM-388**: VAR(1) with uniform coupling; the eigenvalue gap "α +
  (n−1)β and α − β" is "a gap between modes, not between groups of members"
  (SYNTHESIS-081).
- **CLAIM-759**: (1) fixed weights under a permutation action give graph
  automorphisms; (2) automorphism orbits are balanced partitions, whose
  synchrony subspace is invariant (THEORY-1065, Active); (3) an action on
  inputs only, or by mixing, gives no partition; (4) for n ≥ 5, S_n into S_m
  with m < n has image of order at most 2 (CLAIM-759).
- **CLAIM-408**: equal allocation stable for κ > α; for κ < α unstable with
  stable ±√((α − κ)/β); restoring κ > α restores equality in this model.
- **CLAIM-481**: undamped coupled oscillators have modes ω₀ and
  √(ω₀² + 2k), neither decaying; dissipative coupling gives rates a and
  a + 2k; in a Laplacian flow "a spectral gap is where the separation comes
  from".
- **CLAIM-434** part 4: a complete transitive tournament leaves a Hodge
  cyclic share of (n − 2)/3n. **CLAIM-436**: lexicographic order on the
  unit square has no real representation.

---

## 4. How the accounts fit together, and what is not stated

**Where the parts meet.** SYNTHESIS-088 finds the parts "meet mainly where
an effective description's adequacy meets its response to intervention,
and where budgets meet joint satisfiability" (SYNTHESIS-088 title). Stated
links include: CLAIM-407 rests on CLAIM-350; CLAIM-574 rests on CLAIM-264;
CLAIM-535 rests on CLAIM-350 and complements CLAIM-152 (SYNTHESIS-088).
CLAIM-152 is "the standing caution on every boundary criterion filed beside
it ([CLAIM-154], [CLAIM-161])" (SYNTHESIS-081, quoting CLAIM-152). The
naming criteria complement one another: CLAIM-164 picks the object and
CLAIM-154 prices it; CLAIM-307 takes "d'² and the Occam term from
[CLAIM-154]'s own statement" (SYNTHESIS-081). Blackwell's order appears in
four roles: as the refinement CLAIM-535 uses (THEORY-1096), the ordering
CLAIM-409 shows does not order closure, the equivalence CLAIM-380 and
CLAIM-503 compute, and the ceiling CLAIM-199 and TERM-064 put above
bounded receivers. SYNTHESIS-108 hinges on CLAIM-762, which extends
CLAIM-478 "from constraints to units" and takes CLAIM-154's naming rule
(SYNTHESIS-108); SYNTHESIS-107 joins SYNTHESIS-108 to SYNTHESIS-105 and
SYNTHESIS-106 as a chain in which "each step is stated by its own entry,
each can fail without the next" (SYNTHESIS-107 title).

**A unifying thread the record states piecewise.** CLAIM-574 says its
monotonicity "is [TERM-065]'s regime with its probes ordered, and
[CLAIM-152]'s relativity to a target with the targets nested" (CLAIM-574).
CLAIM-564 is "the same shape on the side of demands: an implication valid
at a budget is valid at every lower one" (CLAIM-574). SYNTHESIS-088 tests
"Sufficiency and probe equivalence as one refining structure" and finds it
"Already stated by [CLAIM-574]" (SYNTHESIS-088).

**Not stated on the record** (each account's own list, tested by ADR-075
step 5 and not filed):

- That QUESTION-113's persistence criterion stated for CLAIM-164's subspace
  singles out persisting categories: "It fails on [CASE-097]'s own
  matrices", since the span contains the refined-away spaceship topic as
  wholly as castle (SYNTHESIS-081).
- That CLAIM-307's opposition survives CLAIM-188's singular penalty: "what
  plays d'² in a singular model is left open" (SYNTHESIS-081).
- That value (CLAIM-309) is a fourth naming criterion: "'Value' is a free
  parameter" (SYNTHESIS-081).
- That pruning a latent dimension of a factorization (CLAIM-148) is the
  singular case of CLAIM-188: held only outside the line, by THEORY-079 and
  THEORY-087 (SYNTHESIS-081).
- "Persistence as evidence summed over scales": stated only as the open
  half of QUESTION-113 (SYNTHESIS-081).
- A taxonomy of where local-to-global failures lie (supports or
  distributions, a presheaf's gluing axiom, continuation, a different
  problem, or nowhere): "the grouping in this account's headings is the
  account's, not a claim" (SYNTHESIS-082).
- Whether a gluing failure of realizable observations persists for
  realizable distributions (CLAIM-623 against CLAIM-141); the hidden-mode
  failure as a lossy relational join (THEORY-1060 uncited); "Signalling as
  a forgotten mechanism"; unrolled loops as continuation problems
  (SYNTHESIS-082).
- What CLAIM-269 adds to its premises: read narrowly it "adds nothing";
  read as data-distribution symmetry "it adds content that no premise now
  grounds" (SYNTHESIS-083).
- "That the three are one finding" for SYNTHESIS-084's questions: in
  general form it is CLAIM-152's thesis, and "'Something further' is a free
  parameter" (SYNTHESIS-084).
- That capture is one of CLAIM-346's three obstructions: "Fails on a free
  parameter" (SYNTHESIS-086).
- That only one-hop allocation keeps both delegation conditions: true of
  the rules on record, open beyond them (SYNTHESIS-087).
- That community assembly has an ordinal potential: "renaming invasions as
  'winning moves' adds a word, not a result" (SYNTHESIS-089).
- "One nonexpansiveness behind three bounds" (CLAIM-245, CLAIM-260,
  CLAIM-270): a shared premise, not filed (SYNTHESIS-088).
- "That role abstraction is a case of the owner's U10 mechanism", and "That
  the closure test has been run. It has not." (SYNTHESIS-108).
- "The chain as a mechanism": "stated by no entry"; "That identification is
  where the chain starts" (CLAIM-408's differentiation is a second route);
  "That any step has been shown in one system end to end. No case on record
  runs through more than two steps." (SYNTHESIS-107).

---

## 5. Open questions, objections, defeaters

**Open questions.**
- QUESTION-113 (Open): evidence, retrieval and persistence: "do the three
  ever pick the same categories?", carrying the owner's objection "our
  definition of "object like" needs to apply to objects as well"
  (SYNTHESIS-081).
- QUESTION-104 (Open): "does the budget change which units are worth
  naming?"; CLAIM-574 "bears on the question without answering it"
  (CLAIM-574 history).
- QUESTION-244 (Answered, no) leaves to QUESTION-220 "What condition on
  P(X, Y) guarantees nesting" (QUESTION-244).
- QUESTION-031 (Open): when a probe family separates what a task needs;
  "The stochastic, decision-relative version is open."
- QUESTION-252 (Open): which conditions on an effective description can
  fail while the others hold; QUESTION-221 (Open): whether
  near-decomposability bounds dynamical dependence.
- QUESTION-218 (Open): can a closed mode that is not a block "be one
  system", and should a boundary test take "a subset of members or a
  function of the whole state?"
- QUESTION-491 (Open): whether domain walls, local causal states, local
  transfer entropy and intervention "pick out the same features".
- QUESTION-492 (Open): whether role abstraction coincides with
  balanced-partition structure; CLAIM-759 bears on it.
- QUESTION-360 (Open): when a learned distinction becomes a concept, "is the
  transition graded or categorical"; QUESTION-439 (Open): one concept or
  several under rival uses.
- QUESTION-379 and QUESTION-437 (Open): when a coherent family is
  representable by a realizable system; and "does the failure identify a
  capacity or constraint the reduction omitted", told apart from modelling
  error (SYNTHESIS-082).
- QUESTION-384, QUESTION-393 (Open): enriched profiles against bisimulation;
  which transformations preserve relational individuation.
- QUESTION-185, QUESTION-205, QUESTION-232 (Open; §2.4); QUESTION-120,
  QUESTION-168 (Open; §2.5).

**Objections and narrowings on record.**
- CLAIM-188 against CLAIM-154 (conceded; title narrowed).
- CLAIM-313 against CLAIM-310 (conceded; one-copy condition added).
- CLAIM-502 against CLAIM-282 (both clauses shown false; title narrowed)
  (SYNTHESIS-087).
- CLAIM-623 qualifies CLAIM-197: its "a failure needs an overlap carrying
  sections that disagree" "holds for sheaves and does not reach this
  presheaf"; CLAIM-197 accepts it (SYNTHESIS-082).
- A24's objection to CLAIM-762, "any equivalence relation partitions a
  set", answered by the closure-and-reuse condition (CLAIM-762).
- CLAIM-409 corrects A7's slogan: closure "is not reversed by refinement, it
  is unordered by it" (CLAIM-409 summary).
- CLAIM-225 (counter) against the line's access claims: an improvement in
  access is either impossible or "judged access is not Blackwell
  informativeness".

**Defeaters worth carrying** (as filed): CLAIM-152's — "A privileged target,
argued for independently of the partition it selects"; CLAIM-497's — "the
proportionate partition has no stable plateau"; CLAIM-762's — a new unit
"without any prior identification of states", or a showing that no
condition separates classes that become units from those that do not;
CLAIM-574's — not defeated by un-nested families or averaged comparisons,
"which the claim names as the exception".

**Caveats the entries state about themselves.** CLAIM-154: not "That the
threshold survives misspecification" (Safe Bayes changes the Occam cost).
CLAIM-264: "It does not say which probes to choose". CLAIM-535: not "That
the acceptable sets are the right ones", and A58 adds that "whoever controls
that standard can influence which distinctions the organization is required
to recognize". CLAIM-503: "Nothing for infinitely many states or infinite
outcome sets". CLAIM-409: "Nothing approximate."

---

## 6. Digester's notes (mine, not the record's)

*Everything in this section is my reading. Codes mark which entries a
remark draws on; none of these remarks is held by the record.*

### (a) Bearing on a general theory of learning and inquiry

1. **A distinction is a partition plus a target, and every adequacy verdict
   is a refinement test.** CLAIM-350 (fibres inside level sets), CLAIM-535
   (each observation class shares an acceptable action), CLAIM-407 (response
   kernels constant on fibres) and CLAIM-497 (identical interventional rows)
   are one schema with different targets: deterministic judgment, set-valued
   acceptability, interventional response, causal effect. CLAIM-152 is the
   general relativity; CLAIM-348 adds that the target cannot be justified by
   the description that preserves it. For a theory of arbitrary systems this
   gives a precise reading of "a distinction is warranted": a distinction
   is *required* when its absence merges states the declared target tells
   apart (CLAIM-350), and *not required* when merging loses nothing for any
   target in the declared family. The record does not choose the target;
   that is a premise every application must supply.

2. **Two monotonicities, and where they break.** Fixed-target sufficiency is
   refinement-monotone (CLAIM-409, CLAIM-380, CLAIM-535), and nested probe
   families only split classes (CLAIM-574). But the record has four distinct
   ways that "more" does not mean "finer, better": optima at different
   budgets reorganize rather than refine (CLAIM-387, CLAIM-392); closure is
   unordered by refinement because the target moves with the description
   (CLAIM-409); bounded observers can do better with a coarsening and worse
   on another task (CLAIM-199, CLAIM-455); and averaged comparisons or
   non-nested physical probes can lose distinctions (CLAIM-574). This is the
   formal content behind *split, merge and re-split*: a learner optimizing a
   rate-limited objective will, on the record's witness, re-carve its
   categories non-hierarchically as its budget grows (CLAIM-387), while an
   ideal observer with nested probes only ever splits (CLAIM-574), and an
   actor with peak-cost moves only ever merges (CLAIM-581, CLAIM-557). A
   theory could take the pair (observing budget, acting budget) of CLAIM-557,
   plus the objective's budget of CLAIM-387, as the three indices of a
   system's categories.

3. **When a new distinction earns a name.** The record holds three priced
   criteria that disagree by construction (CLAIM-154 evidence, CLAIM-307
   retrieval under deadline, persistence via CLAIM-164 / CASE-097), and
   QUESTION-113 is open on whether they ever coincide. CLAIM-188 shows the
   evidence criterion overcharges exactly the structured candidates (blocks,
   hidden units, couplings) a learner most needs. CLAIM-762, if it holds,
   adds the systemic criterion: a class becomes a unit when it is a
   congruence for the system's own operations and is reused. My reading is
   that a general theory needs all four, and that CLAIM-307's copy-count
   opposition is the cleanest statement of why "warranted by data" and
   "warranted by use" are different warrants.

4. **What a system can certify about its own categories.** The record
   supplies sharp negative limits: categories visible through probes are
   fixed only up to probe-equivalence (CLAIM-264, TERM-069), through
   readouts only up to an orthogonal or linear freedom (CLAIM-379,
   CLAIM-269), through factorizations only up to a gauge (CLAIM-148), and
   through spectra not even up to the symmetry group (CLAIM-385). Agreement
   is evidence only with independently chosen, held-out probes (CLAIM-322,
   CLAIM-011). Stitching failure certifies nothing (CLAIM-268). Positively,
   Le Cam deficiency gives an ex ante, computable certificate of how much a
   representation can lose for every bounded-loss task (CLAIM-503,
   CLAIM-381), and CLAIM-452 gives a design-time identifiability test. And
   CLAIM-402 bounds self-certification by use: a category that the system
   acts on can manufacture its own confirmation. TERM-085's bound
   (1 + TV)/2 says that a distinction lost at the description stage cannot
   be recovered by any downstream corrective mechanism.

5. **From equivalence to unit is not automatic.** SYNTHESIS-107 is
   careful that each step can fail without the next (CLAIM-443, CLAIM-755,
   CLAIM-760, CLAIM-758, CLAIM-605). CLAIM-388 and CLAIM-481 show that the
   intuitive mechanism (weakly coupled blocks, time-scale separation) is
   neither necessary for closure nor produced by coupling alone. A theory
   that says "systems learn by reifying equivalence classes" would, on this
   record, be a Proposed interpretive hypothesis (CLAIM-762) with an
   untested closure test (CASE-296) and no end-to-end case (SYNTHESIS-107).

### (b) Operationalizing in a record whose schema is revised by governed decisions

1. **Treat a proposed schema change as a coarse-graining or refinement and
   test it against declared targets.** CLAIM-350's fibre test and
   CLAIM-535's intersection test are directly checkable: a merge of two
   vocabulary terms or entry types is admissible relative to the decisions
   the record must make from them only if no declared decision tells the
   merged items apart; where acceptable actions overlap, CLAIM-535 predicts
   several incomparable minimal schemas, so the choice among them is a
   policy commitment to be recorded, not a fact to be found. TERM-065's
   regime tuple is a ready template for stating the targets of such a
   decision in the decision itself.

2. **Expect re-carving, and record it as such.** CLAIM-387 implies that a
   schema optimized at one budget of curation effort need not be a
   refinement of the one optimized at a smaller budget. A record that
   "retires by status, never by deletion" can keep both partitions and the
   map between them; when no garbling links them (CLAIM-392), the decision
   should say so rather than present the new schema as a refinement.

3. **Distinguish what the record's probes can see from what the record is.**
   The record's own lint, indexes and synthesis reviews are probe families
   (TERM-069); CLAIM-574 says adding checks can only split classes, provided
   comparisons are every-probe, not averaged. SYNTHESIS-088's community map
   is an example of a coarse probe whose verdict reading revised ("Read, two
   of the seven parts held two inquiries each"), an instance of a finer
   probe splitting what a coarser one merged.

4. **Guard against self-confirming categories.** CLAIM-402 and CLAIM-322
   suggest that a schema category should be evaluated on entries that were
   not filed under it, or with the effect of its use modelled; CLAIM-011's
   remedy (estimate on one set of tasks, evaluate on another) applies to any
   correspondence a decision imposes between old and new schema.

5. **Correctability of the schema itself.** TERM-085 and its legibility
   bound suggest measuring a governance process by whether, starting from
   the description the record actually holds, it can find, authorize and
   execute a schema correction before it matters; the (1 + TV)/2 bound
   implies that if the current schema merges two failure modes needing
   different remedies, no better review process can choose between them
   until the schema is refined. TERM-098's separation of a concept from its
   corrigibility suggests tracking separately which of the record's own
   categories have a revision path.

6. **Name a unit only when it is closed and reused.** CLAIM-762's closure
   condition, q∘F = F̄∘q, gives a concrete admission test for new schema
   units: the operations the record performs (linking, rests_on, status
   promotion, synthesis) should be well defined on the new class, and the
   class should be reused across decisions. CLAIM-154 would then price
   whether the evidence for it beats its cost; CLAIM-307 warns that the
   units a deadline forces will often be those the evidence least supports.
