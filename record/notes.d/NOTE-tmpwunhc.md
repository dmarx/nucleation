---
status: Read
paper: 'LIT-tmp8en4t'
title: 'Serván and Allesina — Tractable models of ecological assembly'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from the first author's dissertation in
    the University of Chicago's Knowledge repository
    (https://knowledge.uchicago.edu/records/2edva-h7b10/files/MarceloServn_uchicago_0330D_15458.pdf,
    doi:10.6082/uchicago.2656, August 2020), text extracted with
    pdftotext. Read: chapter 3, "Tractable models of ecological
    assembly" (pp. 59–91), abstract, §§3.1–3.4, the appendix §§3.5.1–3.5.4
    with its proofs, and the captions of Figures 3.1–3.5. No number was
    taken from a figure. The bioRxiv preprint (v1, 3 September 2020)
    returned 429 to this client, and the Ecology Letters version is
    closed; neither was compared. The journal abstract (Crossref)
    matches the chapter's content but not its wording, so the published
    text may differ. Checked: the Lyapunov derivative (3.11), the value
    V(x*) = Σγ_i x_i* at an equilibrium, the Hessian (3.14), and the
    acyclicity step the chapter leaves implicit, by hand and by a record
    script on 300 random symmetric systems (see Bearing on the record).
    The other chapters of the dissertation were not read.
date: '2026-10-29'
summary: >-
  For competitive Lotka–Volterra communities with A = D(v)BD(w), B
  symmetric with positive entries, assembled by rare, low-density,
  well-separated invasions, MacArthur's Lyapunov function V orders the
  feasible sub-communities, so the assembly graph is acyclic and every
  feasible sub-community can be assembled without extinctions; with the
  paper's Theorem 1 this makes sequential and all-at-once assembly reach
  the same end-points. One end-point when B is positive definite, several
  when it is not.
---
<!-- inactive-ok-file: QUESTION-083 QUESTION-132 — Open; the questions this reading bears on, cited as open -->

# NOTE-tmpwunhc: Serván and Allesina — Tractable models of ecological assembly

## Contribution

It turns community assembly into a graph problem and finds a class in
which the graph is simple. Vertices are the sub-communities that can
coexist; an edge S → S′ is an invasion by one species, at low density,
that moves the community from S's equilibrium to S′'s. Two ways of
assembling are compared: species arriving one at a time with the
community settling in between ("bottom-up"), and all species introduced
at once ("top-down"). The chapter proves that the two reach the same
end-points when the graph is acyclic and the attractors are exactly the
sub-communities no absent species can invade, and shows that symmetric
competitive Lotka–Volterra communities meet both conditions.

## Key insight

A directed graph is acyclic exactly when some quantity increases along
every edge (Lemma 1). In symmetric competition that quantity is
MacArthur's Lyapunov function, which at an equilibrium is the total
biomass when r = v. So assembly is an ascent: each successful invasion
raises V, no sequence of invasions can return to an earlier community,
and the end-points are the local maxima of V on the feasible set. Order
of arrival can still matter, but only by choosing among several maxima,
and only when the interaction matrix is not positive definite.

## Assumptions

- **Invasions are rare** (§3.2.2): the community reaches its asymptotic
  state between invasions. This rules out the rock–paper–scissors
  community's three-species state, which needs a third invader before
  the second has finished excluding the first.
- **Invaders arrive at low density**, so only local stability of a
  resident state matters.
- **Fixed-point attractors**, with Condition 1 of the appendix: each
  feasible state is globally attractive within its species set, and an
  invasion succeeds iff the invader grows when rare at the resident's
  (time-averaged) state.
- **The model class** (§3.2.3, §3.5.3). ẋ_i = v_i x_i(γ_i − Σ_j b_ij x_j),
  from A = D(v)BD(w) by x_j = w_j N_j and γ_i = r_i/v_i; r_i > 0, v_i,
  w_i > 0; B symmetric, b_ii = 1, all entries positive ("Assume that
  all parameters are positive"); every principal submatrix of B
  nonsingular, and (B^S | γ^S) of full column rank. The last two are
  genericity conditions; they exclude singular interaction matrices.
- **Top-down assembly** is the attractor reached from all species
  present at an arbitrary initial condition.

## Key results

- **Lyapunov function (3.4), (3.10)–(3.11).** V(x) = 2Σγ_i x_i −
  Σ x_i x_j b_ij, with dV/dt = 2Σ v_i x_i(γ_i − Σ_j b_ij x_j)² ≥ 0 for any
  symmetric B, positive definite or not (MacArthur 1970). At an
  equilibrium V(x*) = Σγ_i x_i*, the total biomass when r = v.
- **Attractors (§3.5.3).** Every attractor is a constrained local
  maximum of V: an equilibrium x^S that no absent species can invade,
  γ_k − Σ_j b_kj x_j^S < 0 (3.12), with B^(S) positive definite, from
  the Hessian −2B^(S) (3.14). Conversely such an x^S is a local maximum
  (3.15).
- **Theorem 1 (§3.5.2).** Under Conditions 1 and 2 (attractors are
  exactly the uninvadable sub-communities), (a) if the graph restricted
  to each feasible S is acyclic, the graph is accessible, and each S can
  be assembled from its own species with no extinctions; (b) if the
  whole graph is acyclic, bottom-up and top-down assembly have the same
  end-points.
- **B positive definite (§3.3).** The graph is accessible, has no
  directed cycles, and has a unique sink, the unique global attractor;
  "no historical contingency is possible", and when r = v the end-point
  is the feasible sub-community of greatest total biomass.
- **B not positive definite (§3.3).** "As in the stable case, the
  existence of V implies that G is acyclic." The graph is still
  accessible and acyclic, its sinks are the attractors of top-down
  assembly, and the two processes are equivalent, but there are several
  end-points and the one reached depends on the invasion sequence
  (Figure 3.3: three end-points for five species).
- **Consumer–resource models (§3.5.4).** With every resource kept
  present, the consumers' assembly strictly raises Marsland et al.'s
  ψ(Y) = ½Σ(Y_k − r_k)², which orders the states, so the graph is acyclic.
  If consumers can drive resources extinct, ψ falls when a resource
  reinvades, and assembly graphs with cycles exist (Figure 3.5).
- **Faster invasion (§3.3.1).** With invasions as a Poisson process of
  rate ρ, the fraction of sub-communities assembly can reach falls as ρ
  grows, toward the top-down attractors alone (simulated, Figure 3.4).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Bottom-up and top-down assembly share end-points when the assembly graph is acyclic and attractors are the uninvadable sub-communities | strong | Theorem 1, Lemmas 1–2, proofs read |
| C2 | For symmetric competitive Lotka–Volterra the assembly graph is acyclic, whether or not B is positive definite | strong, one step implicit | MacArthur's V (3.10)–(3.11); the step from V to edges is asserted and checks (see below) |
| C3 | With B positive definite there is one end-point, reachable from the empty community, and every feasible sub-community can be built without extinctions | strong | §3.3 with Theorem 1(a) and Proposition 1 |
| C4 | With B indefinite there are several end-points, so priority effects remain | moderate | §3.3, one five-species example (Figure 3.3) |
| C5 | Consumer–resource assembly is acyclic while every resource persists, and can cycle when resources can be excluded | moderate | §3.5.4 argument; cycles shown by example (Figure 3.5) |
| C6 | Acyclicity is sufficient, not necessary, for equivalence | weak | stated in §3.4 with a pointer to an appendix example that is not clearly marked |

## Method

Enumerate the feasible sub-communities (at most 2ⁿ), compute each one's
equilibrium and each absent species' growth rate when rare, draw an edge
for each successful invasion to the community the augmented system
settles in, and read accessibility, sinks and cycles off the graph. The
chapter notes that construction is exponential in n and is meant for
small communities.

## Concepts

- **Assembly graph G**: vertices are the feasible sub-communities (a
  globally stable interior equilibrium for those species, and ∅); an
  edge S → S′ labelled j when j ∉ S invades x^S when rare and the
  community settles in S′.
- **Accessible**: every vertex has a path from ∅ (an "assembly path").
- **Assembly end-point**: a strongly connected set of vertices whose
  invasions stay inside it and which is a sink of the condensed graph; a
  single sink vertex in the simplest case.
- **Assembly cycle**: a directed cycle of communities, the
  generalization of intransitive competition.
- **Equivalence**: the bottom-up end-points are exactly the top-down
  attractors.
- **Perfect addition ordering**: an assembly path for S along which no
  species goes extinct.

## Connections

The assembly-graph construction comes from Law and Morton (1993),
Hang-Kwang and Pimm (1993) and Capitán, Cuesta and Bascompte (2009); the
cycling example is Schreiber and Rittenhouse (2004). The Lyapunov
function is MacArthur's (1970), and the consumer–resource ordering is
Marsland, Cui and Mehta's minimum environmental perturbation principle
(LIT-1230, NOTE-1352). The chapter's graph differs from Hofbauer and
Schreiber's invasion graph (LIT-1233, NOTE-1379), which it does not cite.
There, an edge S → T needs every species in T but not S to invade S and
every species lost to be unable to invade T. Here an edge is one invasion
followed by the dynamics. Bunin (LIT-1234, NOTE-1397) gives the
multiple-attractor phase of random symmetric Lotka–Volterra models in
which the chapter's indefinite case lives.

## Bearing on the record

- **CLAIM-369, the note of 2026-10-29's open point.** The triage asked
  whether this paper shows that the symmetric case gives an acyclic
  invasion graph and order-independent assembly. **It shows the first
  for its own assembly graph, and the second only when the interaction
  matrix is positive definite.** For CLAIM-369's class, A = UᵀU and
  r = Uᵀb − c, the claim's objective is the chapter's V up to sign and
  a constant. With v = w = 1, L(n) = ½‖b‖² − (rᵀn − ½nᵀAn), and at any
  equilibrium nᵀAn = rᵀn, so L(n*) = ½‖b‖² − ½V(n*). Each successful
  invasion therefore lowers L, and since A = UᵀU is positive
  semidefinite, it is either positive definite (U of full column rank)
  or singular. When it is positive definite, the chapter gives one
  end-point, reached in any order of arrival, and every feasible
  sub-community assembled without extinctions. When it is singular,
  which CLAIM-369 allows ("With A singular there may be several"), the
  chapter's genericity assumption fails and it says nothing. The
  chapter's indefinite case, with acyclicity but priority effects,
  cannot arise from a Gram matrix. Two further limits on the transfer:
  the chapter needs positive entries in B, which is CLAIM-369's sign
  condition for the ecological reading, and its pool admits only
  species with r_i > 0.
- **Hofbauer and Schreiber's graph, closed here by derivation.** The
  chapter's "the existence of V implies that G is acyclic" is asserted.
  It holds, and it holds for the invasion graph of LIT-1233 too. At
  equilibria x_S and x_T of any symmetric system, V(x_S) = rᵀx_S and
  V(x_T) = rᵀx_T, and writing f_k(S) = r_k − (Ax_S)_k for a species' growth
  when rare at x_S,
  V(x_T) − V(x_S) = Σ_{j ∈ T∖S} f_j(S) x_{T,j} − Σ_{i ∈ S∖T} f_i(T) x_{S,i},
  because the cross terms cancel when A is symmetric. Hofbauer and
  Schreiber's edge S → T requires f_j(S) > 0 for j ∈ T∖S and f_i(T) < 0
  for i ∈ S∖T, so both sums make the difference positive: V strictly
  increases along every edge of their invasion graph, and the graph is
  acyclic. This needs only symmetry and an equilibrium for each vertex,
  not positive definiteness or positive entries. The same identity with
  a single invader gives the chapter's step. Checked by a record script
  (2026-10-29) on 300 random systems of three to six species, Gram,
  signed-indefinite and positive-entry symmetric matrices: 3,274
  feasible equilibria, 14,266 invasion-graph edges, V increased along
  every one and the identity held to 10⁻⁹. So CLAIM-369's class always
  meets LIT-1233's acyclicity hypothesis, and signs of invasion growth
  rates decide robust permanence there. Filed as THEORY-tmplmes0
  (Active); a dated note on CLAIM-369 is proposed.
- **QUESTION-083, entrenchment by order of arrival.** In the potential
  case with a positive definite Gram matrix, there is none: every order
  of arrival ends in the same community, and no invasion sequence
  returns to an earlier one. Order-dependence needs a non-positive-
  definite symmetric matrix, which a Gram matrix is not, or asymmetry.
  This agrees with Marsland, Cui and Mehta's monotone assembly (the
  question's note of 2026-10-29) and sharpens it: in this class an early
  entrant can be displaced, but the community it is displaced into is
  fixed by the pool, not by history.
- **QUESTION-132, "judged by invasion graphs".** In the potential case
  the invasion graph is always acyclic (above), so the question's second
  added condition, that signs decide only if the graph is acyclic, is
  met automatically there; cycles among roles need asymmetry or a
  resource that can be excluded (§3.5.4).
- **The triage's expectation.** The web summary the File tier rested on
  ("ends in the same communities whatever the order") is right only for
  positive definite B. The paper does show the graph acyclic, so by the
  owner's call it stays filed.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **The step from V to acyclicity is not written out.** Lemma 1 needs an
  h that increases along edges; §3.3 asserts that V is one. The step
  holds (above), but the chapter does not prove it.
- **Genericity excludes singular matrices**, which are common in
  consumer–resource reductions with fewer resources than consumers.
- **The slow-invasion regime is essential.** Equivalence is asymptotic,
  and the number of invasions needed to reach an end-point can be very
  large (§3.4).
- **The indefinite case is shown by one example**, and the probability
  of reaching each end-point is left open.
- **Slips.** Main-text equations (3.1) and (3.2) are typeset with the
  sum "ij" where j is meant; "top-assembly and assembly" (§3.3) drops
  "bottom-up"; "enpoint" in Figure 3.1's caption; (3.13) sums over j ≠ k
  while (3.12) sums over all j, which agree only because x_k^S = 0. The
  "example in Appendix" that acyclicity is not necessary is not clearly
  identified; Figure 3.5's left panel, with a cycle and an accessible
  top-down attractor, may be it.
- **Version.** The dissertation chapter, not the journal article, was
  read.

## Open questions

- With A = UᵀU singular (more components than features), how are the
  equilibria of a vertex chosen, and does the invasion graph stay
  acyclic once vertices are sets of equilibria?
- When B is indefinite, what is the probability that random invasion
  sequences end at each end-point (§3.4's random walk on G)?
