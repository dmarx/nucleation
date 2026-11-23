<!-- scratch/manuscripts/governance-of-possibility/04-adaptive-readiness.md -->

# Part IV. Adaptive readiness

## 8. The viability of adaptive readiness

Sections 3 to 7 argued that an organization keeps its identity by conserving some relations selectively, and that how much to conserve depends on the timescales of its demands. This section asks what governance must maintain if the demands themselves may change. Its answer is that a regime must keep more than a working present. It must keep, over time, affordable routes to the arrangements that other demands would require.

The record holds the distinctions this answer needs as Active entries. It holds a construction that makes the answer a set of states, and that construction is ChatGPT's and Proposed. This section states the distinctions (§§8.1–8.3), then the construction (§8.4), then a case that separates its three levels (§8.5), and then the construction's limits (§8.6). It ends with what is and is not established (§8.7).

### 8.1 Stability is not viability

Two properties of a dynamical system are easily run together. A regime is **stable** when the system returns to it after small disturbances. A set of states K is **viable** under given dynamics "when from each of its states some evolution can stay in it" (THEORY-134, Active, the record's reading of Aubin's viability theory). Here K is the set of states in which the system's requirements are met. When K is not viable, its **viability kernel** "is the largest part that is, from the rest of which every evolution leaves in finite time" (ibid.).

THEORY-134 is precise about two points that matter below.

- **The constraint set is a separate input.** Viability is defined relative to dynamics and to a set K "that is given separately". "Everything depends on specifying the constraint set independently of the dynamics. For a cell or an organization, which constraints count as 'required' is the hard question, and viability theory takes the answer as given."
- **One evolution suffices.** Viability asks whether *some* evolution stays in K. "With a single deterministic evolution per state, viability and invariance coincide."

The source does not compare viability with stability. The record takes that step itself: "Stability does not entail viability: a system can occupy a stable regime while losing access to trajectories that keep satisfying its constraints" (CLAIM-079, Active, demonstrated). In the claim's words, "A system can currently satisfy the relevant constraints without possessing a trajectory that continues to satisfy them over the relevant horizon". THEORY-134 calls this "a correct consequence of the definitions, since nothing ties an attractor to K". CLAIM-079 also blocks the easy inference that more options are better: "A narrow path can be viable. A large option set can be nonviable."

### 8.2 Keeping a regime and governing among regimes

The second distinction concerns what is maintained. "Maintaining a regime of effective action and maintaining the capacity to govern among regimes are not the same achievement" (CLAIM-099, Active, interpretive). "An agent may succeed at the first while progressively losing the second." The claim is concluded from CLAIM-079 and from a three-part distinction: "An operative regime, the governing organization among regimes, and the capacity to transform that organization can persist or fail separately" (CLAIM-025, Active, interpretive). In CLAIM-025's own example, an organization "may become increasingly competent at operating inside the emergency regime while becoming less capable of changing the organization that keeps the regime in place".

These claims were filed for agents and organizations in general, long before the regulatory exchange. Their defeaters are cases in which the separation never opens:

- for CLAIM-099, "an agent's success at sustaining its operative regime always preserves its capacity to transition or transform";
- for CLAIM-025, degraded transformation capacity "always shows up as a failure of the operative regime or of its governing organization".

### 8.3 Readiness for a contingency

The third ingredient is a measure of readiness. The record defines **scenario-conditioned response readiness** as "the probability that an organization operating under a specified policy can deliver an effective response to a specified contingency within its deadline" (TERM-115, Active):

  R^π_O(c, τ | s) = Pr_π(effective response by τ | do(c), s),

where c is a contingency, τ its deadline, s the initial state and π "the response policy the organization actually follows". Two features of the definition carry weight here.

- **Readiness is defined under intervention.** "The do(c) is the point: this is readiness for a specified situation, imposed, not success conditional on the situations that happened to be observed. An organization that never met c has a value of R for it all the same." So "a record of what was done does not measure it".
- **It is not a single number.** The object is a family, one value per contingency and deadline, and "Two organizations' readiness profiles can be incomparable, each more ready for some contingencies than the other."

Section 6 extends readiness to a curve over the deadline, and gives the condition under which two organizations are ranked the same way at every deadline (TERM-115, note of 2026-11-23, the assistant's).

From readiness, ChatGPT built a set-valued requirement, the **viability kernel of reorganization readiness** (TERM-tmpz28l1, Proposed). It enlarges the state to y = (x, g, c): the ecosystem, its operative governance, and "its reorganizational capacities, each with its own dynamics". For each declared contingency ω it takes the states from which "some admissible policy reaches" a viable post-contingency arrangement "by time τ, at cost within B", while staying within transition safeguards. The states ready for every declared contingency form a set M. The term is then V_reorg = Viab_{F_0}(M), the states from which ordinary operation can stay in M. The term calls itself TERM-115's "set-valued, worst-case-over-Ω counterpart, made a viability requirement". It cites CLAIM-099, CLAIM-025 and CLAIM-079 for the distinctions it formalizes. CLAIM-099's note of 2026-11-22 reads it as a formalization: "A system can maintain x_t and g_t while c_t degrades. This is a parallel and a formalization … the claim's standing is unchanged." The distinction is Active, and its formalization is Proposed.

### 8.4 The second-order kernel

The construction this section rests on extends the term from contingencies to changes of the demands themselves. It is recorded in a dated note on TERM-tmpz28l1 (note of 2026-11-23, ChatGPT's construction, under a Proposed term). The motivating draft restates it, and this paper states it again.

**The state.** The state is S = (x, θ, c):

- x is the operative configuration of the ecosystem: which plants run, which routes are used, which suppliers are engaged;
- θ is its governance architecture: the rules, the budget rules, the allocation of authority;
- c is "the capacities that make revising θ feasible": the reserve, the expertise, the institutional means of deciding and carrying out a change.

Each part has dynamics of its own. Ordinary operation acts mainly on x. Revision of governance acts on θ and draws on c. Both can build up or run down c. The record's note fixes the state and not the equations. The motivating draft writes them as three coupled equations, with an industrial input u, a revision input v and a disturbance w. Nothing below depends on their form.

**Three sets.** Let D be the current demand specification and 𝔇 a declared family of alternative specifications D′.

- **M_D** is "the states whose actual policies meet the current demands D with declared reliability". These are the states that are adequate now.
- **T_{D→D′}^{B,H}** is "the states with an affordable, safe route to M_{D′} within H". These are the states from which a revision, within budget B and horizon H and without breaching the transition safeguards, reaches readiness for D′.
- **M_adaptive** = M_D ∩ ⋂_{D′∈𝔇} T_{D→D′}^{B,H}. These are the states that are adequate now and keep a route to readiness under every declared alternative.

The kernel is V_adaptive = Viab_{F_aug}(M_adaptive), where F_aug is the dynamics of the whole state S. The note calls it "the viability kernel of the capacity to remain ready for current demands while retaining affordable routes to readiness under alternative demands" (TERM-tmpz28l1, note of 2026-11-23).

**Three achievements.** The construction separates three achievements, and the record's note on the manuscript names them in order of strength, "M_D ⊇ M_adaptive ⊇ V_adaptive" (TERM-tmpz28l1, note of 2026-11-23 on this work).

1. **Current adequacy**, S ∈ M_D: the present arrangement meets the present demands.
2. **Reorganization readiness**, S ∈ M_adaptive: it does so and also keeps an affordable, safe route to readiness for each declared alternative.
3. **Adaptive viability**, S ∈ V_adaptive: some continuation of ordinary operation keeps it in M_adaptive indefinitely, so the routes are not used up by the operation that does not need them.

The inclusions hold by construction. M_adaptive is an intersection with M_D. A viability kernel is a subset of the set it is the kernel of. So adaptive viability implies readiness, and readiness implies adequacy. Neither converse is guaranteed, and §8.5 shows a state for each gap.

The three achievements stand in a clear relation to CLAIM-025's three that "persist or fail separately". The relation is not an identity, and the paper marks it as its own (join JA3: TERM-tmpz28l1's three achievements read against CLAIM-025's three). Current adequacy is the operative regime working. Readiness is close to the governing organization keeping its routes among regimes. Adaptive viability is not CLAIM-025's third achievement, "the capacity to transform that organization". It is the second achievement *sustained under the first*. The construction's third set says whether operation erodes readiness. It does not say whether the organization can change the rules by which it governs among regimes, unless those changes are among the declared alternatives in 𝔇. So the construction formalizes CLAIM-099 directly, and CLAIM-025's third tier only as far as 𝔇 reaches.

ChatGPT also stated the design problem that uses the kernel: minimize "operating, maintenance and reconfiguration costs subject to TERM-115 readiness and this kernel" (TERM-tmpz28l1, note of 2026-11-23, reporting A42 §6). The design problem is Proposed with the term. Section 9 does not solve it. Section 9 shows how its terms trade off in one model.

### 8.5 A separating case: a state that is ready and not viable

The construction would be idle if no state lay in one set and not the next. The audit of the motivating draft found that the draft's §8 "passes by a separating case (a Regime I state is in M_adaptive and not in V_adaptive)", and that the case is the construction's own, nothing new being filed for it. The case is set out here because the paper's third claim turns on it.

**The model.** Take the configuration space of §2.4 and §9.

- Two production configurations, A and B, can each be held at a resource cost of 1.
- The only route between them passes through a transitional configuration M that costs 3 while it is crossed.
- The threshold of the transition, the least over admissible paths of the peak cost along the path, is therefore 3 (CLAIM-571, Active, demonstrated).
- The current demands D are met by holding A. The declared alternative D′ is met by holding B: a contingency, a new standard, or the loss of A's input.

**The regime.** The state's governance part θ is Regime I of §9. Each period's budget is set to the peak resource spent in the period before. Ordinary operation holds A and spends 1. Its capacity part c is the budget itself, the resource that can be brought to bear on a transition.

**The states.**

- **(A, budget 3) is in M_adaptive.** Holding A meets D, so the state is in M_D. The route A → M → B has threshold 3, which the budget covers, so the state is in T_{D→D′} for any horizon long enough to cross the route.
- **(A, budget 3) is not in V_adaptive.** Under Regime I, a period spent holding A spends 1. The next budget is therefore 1, and "any transition whose threshold exceeds the cost of holding the current configuration is lost after one period spent holding it, unless the budget is raised from outside by at least the difference" (CLAIM-577, Active, demonstrated). The successor state (A, budget 1) is still in M_D and no longer in T_{D→D′}. With the regime's policy fixed, each state has a single evolution, so the kernel is the largest invariant part of M_adaptive (THEORY-134). The state leaves M_adaptive after one period and is not in it.
- **(A, budget 1) separates the first gap.** It is in M_D and not in M_adaptive. It meets every present demand and has no affordable route to B.

**The contrast.** Change only θ. Under Regime II of §9 a floor holds the budget at 3. The state (A, budget 3) then stays at (A, budget 3), so it is in V_adaptive. The two ecosystems hold the same configuration and produce the same output in every period until the alternative is demanded. Section 9's model runs this and finds output identical across every regime before the first contingency. They differ only in θ and c, which is CLAIM-099's separation: "A system can maintain x_t and g_t while c_t degrades" (CLAIM-099, note of 2026-11-22).

**What the case depends on: which evolutions count.** The case uses the kernel of Regime I's *closed loop*, with the policy the regime actually follows held fixed. That matches the construction's own M_D, which is defined by the states' "actual policies", and TERM-115, which "takes the policy as followed, not the best one available". But a viability kernel asks whether *some* evolution stays in the set (THEORY-134). Suppose F_aug admits, as evolutions of ordinary operation, either of two things:

- an exercise that occupies the transitional configuration each period at the transition's peak, which the record calls a drill;
- a revision v of the budget rule to a floor.

Then the same state (A, budget 3) has an evolution that keeps the budget at 3, and it *is* viable. The record already holds the first mechanism. "a capability stays funded exactly as long as every period contains a mobilization at its cost, whether a use, a drill, a false alarm or a cancelled dispatch" (CLAIM-878, Proposed, demonstrated). CLAIM-tmpg8yl2 (Proposed, demonstrated, a counter) names a drill at the transition's peak as "a third mechanism" beside reserve and redesign. Section 9's model finds that, under the peak rule, a drill is a reserve by another name, at the same capacity cost.

So the separating case shows two different things, depending on the quantifier:

- with the policy followed fixed, the state is outside the kernel;
- with the policies the arrangement could adopt admitted, the state is inside the kernel, and the arrangement's actual policy carries it out.

The second reading is the one regulation can act on. The gap between the two kernels is exactly what a change of policy, a drill, a floor or a revised budget rule could save. The record's construction does not say which kernel it means. Its M_D uses actual policies, while its Viab uses some evolution (gap GA2: whether the second-order kernel is taken under the policy followed or under admissible revisions, and the claim that the difference between the two kernels is what governance revision can save).

### 8.6 Three limits of the construction

The record states three limits of the construction. The motivating draft does not state them, and each bears on how far the construction can carry the paper's third claim.

**1. It secures one retuning.** A state in V_adaptive keeps a route from D to each D′ in 𝔇. It does not keep a route onward from D′. In the record's note: "It secures one retuning: nothing in the construction requires readiness again after a switch to a new demand unless the family of demands is closed under retuning, which the manuscript leaves unstated" (TERM-tmpz28l1, note of 2026-11-23 on this work, the assistant's). An ecosystem that spends its whole reserve reaching readiness for D′ satisfies the construction and may arrive with no route anywhere else. Readiness that persists through a sequence of changes needs a stronger object. One candidate is a family 𝔇 closed under the move from D to D′, with M_{D′} itself required to be an M_adaptive for the family seen from D′. Another is a kernel defined recursively over sequences of changes. The record holds neither (gap GA3: a kernel of repeated readiness, readiness again after each retuning).

**2. The change must be observed in time.** The construction asks that for each declared contingency there be a policy that reaches readiness: for every ω there exists a π. "The ∀ω ∃π order assumes the contingency is observed in time. Under partial observation the policies must agree on contingencies that cannot yet be told apart" (TERM-tmpz28l1, Limits, which notes that ChatGPT said so too). The same holds for a change of demands. A regime that learns of D′ only after the deadline has passed has no use for a route that would have reached it in time. The term adds that "A contingency that recurs during recovery needs a robust kernel". Section 6 treats sensing as one of the rates governance must set. Section 13 treats the conditions under which evidence of a changed demand reaches the parts of a regime that can act on it.

**3. The constraint set must be fixed independently of the arrangement.** "K_ω must be fixed independently of the current arrangement, or every arrangement is viable by its own standards … This is THEORY-134's requirement that the constraint set be fixed independently of the dynamics" (TERM-tmpz28l1, Limits). For the second-order kernel this applies three times over, to D, to the family 𝔇 and to the safeguards. A regime that chooses its alternatives by what it can already reach will always find itself ready. This is the circularity §14 warns of. It is also the formal counterpart of §2.7. Changing the test by which success is judged changes the comparison, and it does not show readiness. The record has one proposed rule for fixing K: K is fixed "by the production dependencies of the constraints that realize the capacity to govern among regimes" (CLAIM-916, Proposed, as reported in CLAIM-099's note of 2026-11-22). It has none for fixing 𝔇.

A fourth point is not a limit of the construction. It concerns what the construction can be asked to do. Viability does not say which arrangements deserve to persist. "Viability does not establish what ought to persist" (CLAIM-075, Active, interpretive, filed as a disclaimer). The kernel is relative to a declared D and 𝔇, and who declares them, and with what right, is the question §§12–13 take up and the record leaves open (QUESTION-485, Open). Nor can 𝔇 contain what nobody has thought of. Section 9 models a harm that the specification does not name, and the kernel says nothing about it until the specification is revised to include it.

### 8.7 What this section establishes

The section's conclusion is a distinction between three achievements, with a construction that makes each a set of states. Its parts have different standing.

- **Active, and demonstrated.** That stability does not entail viability (CLAIM-079). That a utilization-matched budget forecloses every transition above the holding cost after one period (CLAIM-577). The latter supplies the separating case.
- **Active, and interpretive.** That keeping a regime and governing among regimes are different achievements (CLAIM-099). That the three tiers fail separately (CLAIM-025). That readiness is a family of probabilities under intervention (TERM-115).
- **Proposed.** The second-order kernel and its three sets (TERM-tmpz28l1 and its note of 2026-11-23). It is ChatGPT's construction, and by the term's own account an immediate consequence of its definitions, not an empirical theorem. The design problem that uses it is Proposed with it.
- **The paper's own.** The reading of the three achievements against CLAIM-025 (join JA3). The observation that the separating case depends on which evolutions the kernel admits (gap GA2).

What the construction adds to the distinctions it formalizes is a test that can be posed of a state. That test is: does ordinary operation, under the policy actually followed, keep the ecosystem ready for the declared alternatives? The opening of this paper asked it informally of two ecosystems with the same present. Section 9 asks it of a model, with the budget rules, reserves, redesigns and drills that decide the answer.
