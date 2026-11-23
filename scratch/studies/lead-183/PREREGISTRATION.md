# LEAD-183 pre-registration (written 2026-11-23, committed before any test run)

## The predictor

A **constraint architecture** is a graph G = (V, E), a finite state set D_v for
each component, a relation R_uv ⊆ D_u × D_v for each edge, and a target
configuration x* satisfying every relation. A **seed set** S ⊆ V is a set of
components established in their target states before assembly starts.

- **Island** of a seed set: I(S) = the components whose domain is reduced to
  the single state x*_v by arc consistency (AC-3) with S clamped to x*. It
  generalizes Stern, Pinson and Murugan's folding island: what the seed forces
  in the target branch, computed from the constraints alone.
- **Arrival**: d(s, v) is the hop distance in G. The first-arriving seeds of v
  are σ(v) = argmin_{s ∈ S} d(s, v) (all ties kept).
- **Predictor P1, Voronoi-island coverage (VIC)**:
  VIC(S) = (1/|V|) Σ_v [ fraction of s ∈ σ(v) with v ∈ I({s}) ], and VIC(∅) = 0.
  A component counts as covered only if the front that reaches it first is one
  whose own island forces it. Adding a seed can lower VIC: it takes over
  components that a farther seed's island forced, and forces fewer of them.
  This is the paper's mechanism for "adding another actuator with a very small
  folding island" stopping a successful fold, written as a race.
- **Alternative predictor P2, island coverage per nucleus (ICN)**:
  ICN(S) = (|I(S)| / |V|) / k(S), where k(S) is the number of connected
  components of the subgraph induced by I(S) that contain a seed; ICN(∅) = 0.
  Adding a seed whose island is disconnected from the rest raises k and can
  lower ICN.

Both are parameter-free and are computed from the architecture alone, with no
simulation of the dynamics.

**Monotone baselines.** B1 = |S|; B2 = UFI analogue = |∪_s I({s})| / |V|;
B3 = |I(S)| / |V| (joint arc-consistency coverage). All three are
non-decreasing in S, so none can predict a decrease.

## The out-of-sample system

Not Stern et al.'s self-folding sheet. A kinetic constraint-growth model in
the spirit of the kinetic tile assembly model:

- G is an L × L square lattice (L = 8), q = 4 states, target x* drawn at random.
- Each edge is **rigid** with probability p_r = 0.5: its relation is the graph
  of a random bijection through the target pair. Otherwise it is
  **ambiguous**: the target pair plus m = 2 distractor pairs drawn uniformly
  from the other q² − 1 pairs.
- Dynamics (Gillespie, no detachment, zero temperature): an unset component
  with n ≥ 1 set neighbours attaches at rate n, taking a state uniformly among
  those compatible with every set neighbour; if none is compatible the run
  jams (failure). An unset component with no set neighbour nucleates at rate
  ε = 0.002 into a uniform random state. Seeds start set at their target
  states.
- Success: every component set and equal to x*. V(S) is estimated by R = 300
  runs per seed set.
- Five architectures (random seeds 0..4). For each, a pool of 10 candidate
  seed components chosen at random; evaluated sets: the empty set, all
  singletons, all pairs, and 40 random triples.

Sensitivity (secondary, same metrics): p_r ∈ {0.4, 0.6}, one architecture each
size, fewer sets if time requires.

## Metrics and the criterion of transfer

- **M1**: Spearman correlation between each predictor and V̂ over all
  evaluated non-empty sets, pooled within each architecture, then averaged.
- **M2, harmful additions**: every pair (S, S ∪ {c}) among the evaluated
  sets. A pair is a significant decrease if V̂(S ∪ {c}) < V̂(S) by more than
  2 combined standard errors and by at least 0.05; a significant increase
  likewise. Over significant changes, AUC of −ΔP for classifying decreases;
  recall = share of significant decreases with ΔP < 0; precision = share of
  pairs with ΔP < 0 that are significant decreases.
- **Transfer** is declared for a predictor if, pooled over the five
  architectures, its M2 AUC ≥ 0.7, its recall ≥ 0.5, and its M1 is at least
  the best monotone baseline's M1 minus 0.05. Otherwise the result is
  reported as a failure of transfer, whatever else it shows.
- If the system shows no significant decreases at all, the test is void and
  says so: the system would not exercise the property.
