---
number: 32
status: Skimmed
formerly:
- NOTE-tmp35dat
paper: LIT-041
title: 'Work capacity of channels with memory'
version: 1
date: '2026-09-25'
summary: >-
  When an agent's actions change what it later perceives, the maximum rate at which it can extract work from its environment (the environment channel's "work capacity") is in general reached neither by a maximally predictive agent nor by one that randomizes its actions and forgets them. Prediction and forgetting have to be traded off.
---

<!-- inactive-ok-file: LIT-041 — Deferred: this is the seeded skim of the paper, filed with it on 2026-09-25 -->

# NOTE-032: Work capacity of channels with memory

## Contribution

Prediction is widely treated as the organizing principle for adaptive systems, and earlier thermodynamic work on agents reading a fixed tape found that maximal prediction is required to reach the energetic limit. Real agents also act on their environment. The authors model agent and environment as coupled hidden-Markov (finite-state) channels forming a percept-action loop and analyse its stochastic thermodynamics. They define the work capacity of an environment channel as the maximum expected work per round that any agent can extract. They show that the two earlier design principles for work-efficient agents (maximize predictive power, and randomize and forget your own actions) stop being optimal once actions have observable consequences: remembering past actions improves prediction but lowers the free energy available. They conclude that prediction and energy efficiency can conflict in active learning systems.

## Skim

*Abstract, figures and selected sections, read when the work was seeded. Not enough to state its assumptions or results exactly; a `Read` note replaces this one.*

- Framework (§II, Defs 1–2, Fig. 2): agent and environment are causal finite-state channels. The joint process, including both hidden memories, forms a finite-state Markov chain, so Cesàro-limit asymptotics are well behaved. The agent's "algorithmic memory" (its transition matrix) is kept separate from its "adaptive memory" M.
- Predictive agents (§III, Defs 3–4, Thms 1–2): "maximally predictive" means I[A₀:t+1 S₀:t; S_t | M_t] = 0. For unifilar environments a finite asymptotically-mean predictive agent always exists. Otherwise a predictive agent may need countably infinite memory, a point the authors draw from computational mechanics.
- Work rate and capacity (§IV, eq. 15, Def. 5, Thm 3, Table I): the work rate is ⟨H(A_t|M_t) − H(S_t|M_t)⟩ in units of k_BT ln 2. C_work exists, lies between 0 and ln|S|, and is subadditive under channel cascade. Closed forms are given for noiseless channels (capacity 0), memoryless invariant channels, and unifilar product channels (log|A| − h(S)). The authors explicitly draw the analogy to communication capacity.
- Main results (§V, Thms 4–5, Fig. 6): without feedback (unifilar product environments), efficient agents are exactly those that both randomize their actions and predict their percepts, which extends Boyd et al.'s result beyond stationary inputs. With feedback, a binary memoryless invariant environment (Fig. 5) exists in which the predictive, max-entropy-action and work-efficient agent sets are all non-empty and mutually disjoint.
- Discussion (§VI): the authors connect the result to active inference, the free-energy principle and transformer and LLM next-token prediction, but only as framing. Open directions they list: agents with goals (reward encoded as low-entropy percepts), dissipation when the environment also pays to implement its channel, and quantum work capacity using quantum combs.

## Open questions

- The anthology's journal names this as its one scope decline by title. The skim supports the decline: this is information-thermodynamics theory. There are no ML experiments, no training recommendation and no evaluation method, and the cs.LG listing and LLM mentions are motivation only. It is not `analysis-and-evaluation` material. It fits a reading-list note under information-theory, with agency as a secondary tag.
- A deeper reading should check whether the PRX version (if 10.1103/7nds-tjr8 is it) changed any results or framing, and pin the DOI before filing.
- Check how strong the "prediction vs. efficiency" claim really is. The counterexample (Thm 5) is a small hand-built binary environment. It is worth asking whether the trade-off is generic or an edge case, and how it relates to the free-energy principle, which the abstract invokes but the paper never engages formally.
