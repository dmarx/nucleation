---
status: Skimmed
paper: LIT-tmpiroms
title: 'Debreu 1952, a social equilibrium existence theorem'
version: 1
date: '2026-09-25'
summary: >-
  In a "social system" where each agent's feasible set of actions depends on the others' actions, an equilibrium exists under topological conditions. Each agent must be a contractible polyhedron with a closed-graph constraint correspondence, continuous payoffs, a continuous max-value function, and a contractible set of maximizers. The proof uses the Eilenberg–Montgomery fixed-point theorem, and the result contains Nash equilibrium existence and underlies Arrow–Debreu.
---

<!-- inactive-ok-file: LIT-tmpiroms — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-tmp6uvet: Debreu 1952, a social equilibrium existence theorem

## Contribution

(No abstract.) In many social systems each agent picks an action from a range, but the other agents' actions determine the subset the agent may choose from. Each agent ranks outcomes by its own preferences. Debreu gives general conditions for an equilibrium: a profile in which every agent's action is feasible given the others' and no agent wants to switch. He notes that Arrow and Debreu used the theorem for competitive economies, and that it contains Nash's N-person equilibrium and von Neumann's zero-sum saddle point as special cases.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- §1 Topological concepts (pp. 886–887): convex cells, geometric polyhedra and polyhedra (homeomorphic images), contractibility, and the completed real line as the payoff range.
- §2 Equilibrium points (pp. 887–888): v agents with action sets 𝔄_ι and constraint correspondences A_ι(ā_ι), non-empty and compact. The definition is a* ∈ A_ι(ā*) with f_ι(a*) equal to the maximum over that set. The theorem conditions: 𝔄_ι is a contractible polyhedron, the graph G_ι is closed, f_ι is continuous on G_ι, φ_ι(ā_ι) = max f_ι is continuous, and the maximizer set M_{ā_ι} is contractible.
- Proof (p. 888): a lemma, a special case of Eilenberg–Montgomery (or Begle), says a semicontinuous (closed-graph) multi-valued map on a contractible polyhedron with contractible values has a fixed point. It is applied to the product of the best-response sets.
- §3–4 (pp. 889–893, glanced): saddle points as special equilibria with the MinMax operator, and a short history of saddle-point, multi-valued fixed-point and equilibrium results.

## Open questions

- A foundational result: the "abstract economy" or generalized Nash equilibrium, where constraints depend on others' actions. Generalized-Nash formulations appear in multi-agent learning, constrained games and market-design models.
- Contractibility is weaker than convexity. A deeper read of §3–4 would check how Debreu positions this against Kakutani and Nash.
- It is 70+ years old and later existence proofs generalize it, but it is still the standard citation. A reading note would record standing rather than advice.
