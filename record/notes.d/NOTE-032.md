---
number: 32
status: Read
formerly:
- NOTE-tmp35dat
paper: LIT-041
title: 'Work capacity of channels with memory'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of arXiv:2504.06209v1 (8 Apr 2025, the only
    arXiv version; no journal-ref), 42 PDF pp. I extracted it with PyMuPDF
    into raw4/c49c.txt, because this host has no pdftotext. I read every
    page. Main text §I–VII is pp. 1–8, references [1]–[83] are pp. 8–10, and
    the Supplemental Material is pp. 11–42: App. A (information theory,
    Lemma 1), B (finite Markov chains, Lemmas 2–3, Cor. 1), C (hidden Markov
    channels, Defs 6–8), D (global Markov chain, Lemma 4), E (Bayesian
    networks and d-separation, Lemmas 5–7, Cor. 2), F (predictive agents,
    Lemma 8, Thms 6–7, Cor. 3), and G (work capacity; Thms 8–10, Lemmas
    9–10; this is the Landauer-efficient construction). I followed every
    proof step. The d-separation figures (Figs 13, 15, 16, 19, 22–25) came
    through only as node labels, so I checked each claimed d-separation
    against the DAG of Fig. 10 / Eq. (E13) myself. I recomputed the worked
    example numerically (optimal work rate, optimal action bias,
    random-action work rate). The Physical Review X version I could not
    read: the APS pages return 403, and only its Crossref/OpenAlex metadata
    was checked (see corrections).). Upgraded from `Skimmed` to `Read`: the
    claims table, assumptions and results are new, and the skim is corrected
    where the full text disagreed.
date: '2026-09-25'
summary: >-
  The paper models agent and environment as coupled finite hidden-Markov
  channels. It defines the environment's work capacity C_work = max over
  agent models of ⟨H(A_t|M_t) − H(S_t|M_t)⟩_t (in k_BT ln 2 per round) and
  proves two things. First, for unifilar environments whose percepts
  ignore actions, the efficient agents are exactly the
  randomize-and-forget ∩ maximally-predictive ones, and C_work = log|A| −
  h(S). Second, one binary memoryless environment exists where predictive,
  max-entropy-action and efficient agents form three nonempty,
  pairwise-disjoint sets: every predictive agent extracts ≤ 0,
  uniform-random agents extract 1 − h(3/4) ≈ 0.189 bits, and the optimum
  is ½·log₂(3/4 + 1/√2) ≈ 0.272 bits, reached by a memoryless agent that
  plays action 0 with probability 1/√2.
---

# NOTE-032: Work capacity of channels with memory

## Contribution

The authors give a framework for the stochastic thermodynamics of percept-action loops, which they themselves call the primary contribution (p. 2). Agent and environment are both finite-state hidden Markov channels, and the joint process (M, A, S, Z) is a homogeneous finite Markov chain (Lemma 4). Asymptotic work rates therefore exist as Cesàro limits.

On this framework they define the **work capacity** of an environment channel, by explicit analogy to communication capacity. They then prove three things:
1. The tape-setting design principle of Boyd, Mandal and Crutchfield, "randomize-and-forget your actions, predict your percepts", survives without stationarity, for unifilar product environments (Thm 4 / Thm 9).
2. The principle fails once percepts depend on actions (Thm 5 / Thm 10).
3. A definition of "(asymptotically mean) maximally predictive" that allows feedback reduces to the computational-mechanics definition in the stationary, feed-forward case (Thm 2 / Thm 6).

## Key insight

The agent's per-round work bound is ⟨H(A_t|M_t) − H(S_t|M_t)⟩_t: it gains from uncertainty in what it emits and pays for uncertainty in what it receives, both judged from its own memory. On a tape the two terms are independent. You maximize the first by forgetting your uniformly random outputs, and you minimize the second by predicting your inputs.

When the percept depends on the action, predicting S_t requires M_t to carry information about A_t, and whatever M_t knows about A_t is subtracted from the first term. In the extreme case of Lemma 10, perfect prediction forces H(A_t|M_t) → 0, so a predictive agent can extract nothing. Its rate is −⟨H(S_t|M_t)⟩_t ≤ 0.

"Predict everything you can" is therefore not a thermodynamically neutral goal for an agent that acts.

## Assumptions

- **Classical, discrete time, finite alphabets.** A = S, which is done by embedding the smaller alphabet into the larger (§II).
- **Finite-state channels.** Environment and agent are finite-state (hidden Markov) causal channels (Defs 1, 2, 6, 9). Both transition matrices are time-homogeneous. The agent's transition matrix Θ is fixed "algorithmic memory". Only M_t adapts; there is no learning of Θ.
- **The agent's model is given.** The agent's algorithmic memory is assumed to encode the whole loop, (Θ_agt, p_{A0M0}, ν_env) (§III, p. 3). Predictiveness is defined relative to the true process distribution, not a learned model.
- **Thermodynamic model.**
  - Information reservoir: a flat internal-energy landscape over metastable information-bearing degrees of freedom.
  - Isothermal protocols with τ_others ≪ τ_protocol ≪ τ_info.
  - Second-law bound W ≤ H(X_out) − H(X_in), in k_BT ln 2 (Eqs. 14, G1), assumed saturable by idealized protocols [16, 17, 19]. These need "arbitrary energy functions or infinite timescales" (App. G2).
- **What gets charged.** Only the agent's implementation of Θ is charged, per round, on the register (S_t, M_t) → (A_{t+1}, M_{t+1}) (Eq. G3). The environment's own thermodynamic cost is outside the model; the authors list it as future work.
- **Unifilarity** (Def. 4 / Def. 7): a deterministic initial hidden state, and Z_{t+1} a function of (A_t, S_t, Z_t). It is needed for the existence of finite-memory predictive agents (Thm 1) and for Thm 4.
- **Product channel** (percepts independent of actions) for Thm 4 and for Thm 2's second part.
- **Stationarity** of the joint process MAS for Thm 2 only.
- **Scope narrower than the title.** The separation result (Thm 5) is proved for one specific memoryless invariant binary channel (Fig. 5): φ(j|0) = δ_{0j}, φ(j|1) = ½. No channel with memory is shown to separate the sets.

## Key results

(Main-text numbering, supplement numbering in brackets. All work is in units of k_BT ln 2, i.e. bits.)

- **Lemma 4 (global Markov chain).** U_t = (M_t, A_t, S_t, Z_t) is a homogeneous finite-state Markov chain. Hence Cesàro limits of continuous functions of p(U_t) exist (Cor. 1(iii)).
- **Def. 3 / Def. 12 (predictive).** The agent model is predictive in round t if I[A_{0:t+1}S_{0:t}; S_t | M_t] = 0. It is asymptotically mean (a.m.) predictive if ⟨·⟩_t = 0.
- **Lemma 8.** An agent is predictive at every t iff I[A_{0:t+1}S_{0:t}; S_{t:∞} | M_t] = 0 for every t, i.e. it is predictive of all future percepts.
- **Theorem 2 [Thm 6].** Let MAS be stationary. Then a.m. predictive ⇔ I[A_{0:t+1}S_{0:t}; S_{t:∞}|M_t] = 0 for all t. For a product environment this becomes I[S_{0:t}; S_{t:∞}|M_t] = 0, the condition used in [17, 30]. Proof: under stationarity b_t := I[A_{0:t+1}S_{0:t}; S_t|M_t] is nondecreasing, so its Cesàro mean is 0 iff every b_t = 0.
- **Theorem 1 [Thm 7].** For a unifilar environment, every agent channel has an a.m. predictive finite model. The construction augments memory with a copy of the last symbol and a tracked environment state Z′_t = Z_t, via the unifilarity map. The constructed model is in fact predictive at every t, which is stronger than a.m.
- **Eq. (15) [G12], work rate.** W(agtM ↔ env) = ⟨H(A_t|M_t) − H(S_t|M_t)⟩_t. It is derived from the per-round bound H(A_{t+1}M_{t+1}) − H(S_tM_t) by telescoping in the Cesàro sum (Eqs. G5–G10).
- **App. G2 (saturability).** The bound is reachable with finite memory given idealized protocols. The agent adds a deterministic mod-d counter, where d is the asymptotic period of the global chain, and switches among d protocols tuned to the d limiting input distributions.
- **Definition 5 [Def. 13], work capacity.** C_work(env) := max over agent models of W.
- **Theorem 3 [Thm 8].**
  - (i) Existence, in the per-agent sense; see corrections.
  - (ii) 0 ≤ C_work ≤ log₂|S|. The paper prints ln; see corrections. The lower bound comes from a memoryless identity agent A_{t+1} = S_t: the per-round terms telescope to 0 in the Cesàro mean. The paper says "zero ... in each step", which is loose, but the conclusion holds.
  - (iii) Cascade subadditivity: C_work(env₂∘env₁) ≤ C_work(env₁) + C_work(env₂), via an alternating channel env₁₂.
- **Table I [Lemma 9].**
  - Noiseless: C_work = 0.
  - Memoryless invariant: C_work = max_{pA}[H(A) − H(S)], with the sign corrected. It is attained by a memoryless agent.
  - Unifilar product: C_work = log|A| − h(S), where h(S) = lim H(S_{0:n})/n.
- **Theorem 4 [Thm 9].** For a unifilar product environment, A_eff = A_mea ∩ A_pred. Proof from W = ⟨H(A_t|M_t)⟩ − h(S) − ⟨I[S_{0:t}A_{0:t+1}; S_t|M_t]⟩ (Eq. G43). Both the first and the third term must be at their bounds.
- **Lemma 10.** For the Fig. 5 channel, ⟨I[A_t; S_t|M_t]⟩ = 0 ⇔ ⟨H(A_t|M_t)⟩ = 0. The step used: both rows are distinct from each other, so p(A,S|M=m) is not a product whenever A is nondeterministic given m.
- **Theorem 5 [Thm 10].** There is a channel (Fig. 5) for which A_pred, A_mea and A_eff are nonempty and pairwise disjoint.
  - Predictive agents (e.g. M_t = A_t) have W = −⟨H(S_t|M_t)⟩ ≤ 0.
  - Max-entropy-action agents have W = 1 − h(3/4) = 1 − ln(256/27)/ln 16 ≈ 0.1887.
  - C_work ≈ 0.2716 > 0.1887 > 0.
  - A_mea ∩ A_pred = ∅ because predictive forces H(A|M) = 0.

I checked all three numbers: 0.2716 at p = 0.70711, 0.18872, and h(3/4) = 0.81128.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The joint agent–environment process (M, A, S, Z) is a homogeneous finite Markov chain, so asymptotic work rates exist per agent | strong | Lemma 4 (App. D), Cor. 1 (App. B) |
| C2 | The expected work per round is bounded by ⟨H(A_t\|M_t) − H(S_t\|M_t)⟩_t, and this is saturable in principle with finite memory | moderate | Eq. G1–G12 derivation (proof, given the assumed second-law bound). Saturability is a construction sketch (App. G2) relying on idealized protocols from [16, 17, 19] |
| C3 | For unifilar environments, a finite (a.m.) predictive model exists for any agent channel | strong | Thm 1 / Thm 7, explicit construction |
| C4 | Under stationarity, a.m. predictive ⇔ predictive of all future percepts at all times; with a product environment this recovers the Boyd et al. / ε-transducer condition | strong | Thm 2 / Thm 6, Lemma 8. Minor equation-reference typos in the proof ("stationarity (eq. (F25))" should be F23; "equivalent to eq. (F26)" should be F25) |
| C5 | 0 ≤ C_work ≤ log₂\|S\| | strong (with base corrected) | Thm 8(ii). As printed ("ln\|S\|"), the upper bound is false; see corrections |
| C6 | C_work is subadditive under channel cascade | moderate | Thm 8(iii): a short proof. Eq. G25 has a typo (the second pair should read H(A²\|X²) − H(S²\|X²)), and the ≥ step (G29) is stated informally |
| C7 | C_work exists as a maximum over agent models | weak | Only the per-agent Cesàro limit is proved (G17). Attainment of the max over the unbounded agent set is asserted, not proved |
| C8 | Noiseless channels have C_work = 0; unifilar product channels have C_work = log\|A\| − h(S) | strong | Lemma 9(i), (iii) |
| C9 | Memoryless invariant channels have C_work = max_pA[H(A) − H(S)], attained by a memoryless agent | strong (with sign corrected) | Lemma 9(ii) proof. The printed statement has the sign reversed |
| C10 | Without feedback (unifilar product), efficient agents are exactly those that randomize-and-forget actions and are predictive, extending [17] beyond stationarity | strong | Thm 4 / Thm 9 |
| C11 | With feedback, there exist environments where predictive, max-entropy-action and efficient agents are mutually exclusive | strong | Thm 5 / Thm 10 with Lemma 10, for one explicit binary memoryless channel. Numbers verified |
| C12 | "In the presence of feedback, maximally predictive agents are generally inefficient" (§I, p. 2) | weak | Only one existence example is proved. The Lemma 10 argument does extend to any memoryless channel whose action rows are pairwise distinct and whose C_work > 0 (my extension, not the paper's), but nothing is shown for channels with memory |
| C13 | "Work-efficient agents must balance prediction and forgetting" (abstract); "a tradeoff emerges between predictive memory and action forgetfulness" (§V) | weak | Informal argument. In the only proved example the efficient agent is memoryless: it forgets everything and has biased actions. No example of an interior optimum, and no trade-off curve, is given |
| C14 | "Prediction and energy efficiency may be at odds in active learning systems" (abstract) | weak | Hedged extrapolation. The model has no learning (Θ is fixed), and there are no experiments |
| C15 | Links to the free-energy principle, active inference, transformers and LLM next-token prediction (§I, §VI) | weak | Assertion and framing only (refs [47, 51, 57]); these are never engaged formally |

## Method

This is a theory paper, with the proofs given in the supplement.

1. **Model.** Represent both parties as finite hidden Markov channels (Φ_env on A×Z → S×Z, and Θ_agt on S×M → A×M), and compose them into the global chain (Eq. D8).
2. **Tools.** Use a DAG with auxiliary joint-output nodes V_t = (A_t, M_t) and W_t = (S_t, Z_{t+1}) (Fig. 10, Lemma 6). This makes the loop compatible with a Bayesian network, so every conditional-independence step can be discharged by d-separation. Asymptotics use the periodic decomposition of finite Markov chains (Lemma 2, Cor. 1), and information diagrams are used for multi-term identities (Figs 7, 14).
3. **Thermodynamics.** Apply the nonequilibrium second-law bound to the agent's per-round map (S_t, M_t) → (A_{t+1}, M_{t+1}) and Cesàro-average it.
4. **Optimisation.** Optimise over all finite agent models for special channel classes.
5. **Separation.** Separate the design principles with an explicit two-symbol example.

## Concepts

- **Percept-action loop** — agt ↔ env: an agent channel η_{A|S} and an environment channel ν_{S|A}. The agent emits A_t, then receives S_t.
- **Algorithmic vs adaptive memory** — the fixed transition matrix (likened to DNA) versus the state M_t that carries information about the past (§II, p. 3).
- **Maximally predictive (in round t)** — I[A_{0:t+1}S_{0:t}; S_t | M_t] = 0. Note that A_{0:t+1} includes the current action A_t. The memory is a sufficient statistic of the whole action–percept past (and current action) for the next percept.
- **Asymptotically mean (a.m.) predictive** — the Cesàro mean of that quantity is 0.
- **Work rate** — W = ⟨H(A_t|M_t) − H(S_t|M_t)⟩_t, in k_BT ln 2 per round.
- **Work capacity** — C_work(env) = max over agent models of W. The paper calls it an intrinsic information-theoretic property of the channel, analogous to Shannon capacity.
- **A_mea / A_pred / A_eff** — respectively:
  - agents with ⟨H(A_t|M_t)⟩ = log|A|;
  - a.m. predictive agents;
  - agents with W = C_work.
- **Unifilar** — the next hidden state is determined by the current state, input and output, from a known initial state.
- **Product channel** — output independent of input, i.e. an information source; also called a "completely random" channel.
- **Memoryless invariant channel** — ν(s|a) = ∏_t φ(s_t|a_t).
- **Noiseless channel** — S_t = A_t.
- **Landauer-efficient agent** — one that saturates the second-law bound (App. G2).

## Connections

- **Direct predecessor: Boyd, Mandal & Crutchfield, "Thermodynamics of modularity", PRX 8, 031036 (2018) [17].** It gave the tape-setting result: stationary input, no feedback, and efficient ⇔ predictive plus randomize-and-forget. Thm 4 extends it to nonstationary percept processes. Thm 2 shows the new definition of predictiveness coincides with [17]'s in the stationary product case. Footnote [35] says [17]'s second condition holds automatically by d-separation.
- **Thermodynamic ratchets and information engines on tapes** [9–22]: Mandal–Jarzynski; Barato–Seifert; Boyd–Mandal–Crutchfield 2016 [45], "information-processing second law", which gives entropy rate as the maximal work rate from a process; Garner et al. [16, 18]; Boyd–Crutchfield–Gu 2022, "Thermodynamic machine learning through maximum work production" [19].
- **Contrast with Still et al., "Thermodynamics of Prediction", PRL 2012 [34]**, which has a different notion of predictive agents.
- **Computational mechanics.** Barnett & Crutchfield's ε-transducers [30] supply the sufficient-statistic and unifilarity notions, and the fact that some channels need countably infinite memory to predict.
- **Information-theoretic sensorimotor loops.** Klyubin–Polani–Nehaniv [58], Tishby–Polani [80], empowerment [81] and Ay–Zahedi [82]. App. E3 relates their Bayesian networks to this one. They model internals with two matrices where this model uses one channel.
- **Quantum side.** The environment-side cost is related to the "thermodynamic capacity" of quantum channels (Navascués–García-Pintos [52]; Faist–Berta–Brandão [53]). Quantum agents [20–23] are the proposed extension, and Zambon–Adesso [23] is cited as the only prior work with feedback. The background thermodynamics (Landauer bound, nonequilibrium free energy, second law for information processing) is the material [LIT-010](../literature.d/LIT-010.md) (the quantum-thermodynamics review) surveys.
- **Free-energy principle / active inference** [47, 57]: invoked in the abstract and §VI as the "predictive paradigm" this result pushes against. There is no formal comparison. The "free energy" here is the physical nonequilibrium free energy, not the variational quantity.

## Bearing on the record

- **Does the full text change the anthology's decline? No.** Having read all 42 pages, including every proof, I find no instruction for ML practice and no evaluation method.
  - There are no experiments, no training or inference recommendation, no metric or benchmark, and no algorithm a practitioner could run.
  - The model has no learning at all: the agent's transition matrix is fixed and assumed to already encode the environment.
  - The ML content is confined to motivation: the energy cost of training large networks [5, 6] (§I), a single sentence that transformers and LLMs are next-token predictors [51] (§VI), and "active learning systems" in the abstract. The arXiv cs.LG primary listing does not reflect the body.
  - The "design principles for work-efficient agents" are statements about idealized thermodynamic optima in units of k_BT ln 2, not advice about building ML systems.
- **The anthology's stated reason for the decline is not the reason that holds.** Its curation entry of 2026-09-21 declined the paper because none of its topics "can express the claim". The anthology's own [ANTH-ADR-059](https://github.com/dmarx/anthology-of-the-sota/blob/main/record/decisions.d/ADR-059.md) (2026-09-23) now names that reason as the wrong one: a missing topic is a finding about the axis, not grounds to decline. The decline is still correct, for the other reason: this is a theory claim about physics and information, not a practice. There is also no ML-practice explanation for which it would source an ANTH-THEORY document.
- **The DOI field** should stay unverified until the PRX author list can be seen (see corrections). If it is confirmed, the note should add the published title.
- **This record.**
  - It fits information-theory (primary) with agency and natural-sciences. The existing [LIT-041](../literature.d/LIT-041.md) tags are right.
  - No THEORY document here is contradicted.
  - If the record ever carries a THEORY claim of the form "prediction is the organizing principle of adaptive agents", this paper is the counter-source. It shows that, for thermodynamic efficiency, maximal prediction can be strictly suboptimal once actions affect percepts.

## Limitations

- **The separation rests on one hand-built example.**
  - It is a 2-symbol memoryless channel. The abstract's generality ("neither ... remains optimal in environments where actions have observable consequences") is an existence claim, not a universal one.
  - My own extension of the Lemma 10 argument covers memoryless channels with pairwise-distinct action rows. The paper does not state it, and nothing is proved for channels with memory, despite the title.
- **The trade-off is not demonstrated.** The only proved optimum is memoryless, with biased actions. No environment is exhibited where the optimum is a partial-memory agent that trades some prediction for some action entropy.
- **There is no learning.** The agent is assumed to know the full loop. "Active learning systems" (abstract) is an extrapolation.
- **The accounting is one-sided.** Only the agent's computation is charged. Whether the agent's maximal work can equal the environment's minimal cost for channels with memory is left open (§VI). Idealized saturating protocols (infinite time, arbitrary energy landscapes) are assumed. Realistic constraints [38–41] are mentioned but not analysed.
- **Computability.** Computing C_work in general is a nonlinear optimisation over unbounded finite-memory agents. Closed forms exist only for the three classes in Table I, and attainment of the max in general is not proved.
- **Presentation errors.**
  - Table I / Lemma 9 has the sign reversed.
  - ln and log₂ are mixed (Thm 3(ii), Eqs. 17 and G64, Def. 14).
  - G44 uses "<" where "≤" is meant.
  - G25 has an H(A²|X²) − H(A²|X²) typo.
  - Several equation cross-references in App. F are wrong.
  - None changes a result, but Table I as printed would mislead a reader who uses it directly.

## Open questions

- **Channels with memory.** Is there a channel with memory, or a memoryless channel with a larger alphabet, where the efficient agent retains partial information about its actions? That is, is there an interior optimum that shows a genuine prediction–forgetting trade-off? One explicit example would settle whether "balance" is more than rhetoric.
- **How generic is the separation?** How large is A_pred ∩ A_eff across random unifilar feedback channels? The paper shows only that it can be empty.
- **Two-sided dissipation.** For channels with memory, does max agent work equal min environment implementation cost, or is there irreducible entropy production in feedback loops (§VI)?
- **Quantum work capacity** via quantum combs (§VI).
- **Goals.** Can goal-directed behaviour, with reward encoded as low-entropy percepts, be recovered as work maximisation (§VI)? The paper only proposes this.
- **Publication record.** Does the PRX version ("Information thermodynamics of agents: …", DOI 10.1103/7nds-tjr8, received 2025-04-23, published 2026-08-10 per Crossref) correct the sign and ln typos or change the framing? Unverified until the APS page or PDF is accessible.

## Corrections to the seeded skim

- **Table I prints the memoryless-invariant capacity with its sign reversed, and so does the dossier.** Table I, Lemma 9 (Eq. G30) and the dossier's "Skim" all give C_work = max_{pA0}[H(S0) − H(A0)]. The proof actually establishes max_{pA0}[H(A0) − H(S0)]: Eq. (G36) bounds by H(A0M0) − H(S0M0) and Eq. (G39) by H(A0) − H(S0). That is also the sign the work rate (Eq. 15) requires. The printed sign cannot be right. For the Fig. 5 environment, max[H(S) − H(A)] = 1 bit (at p(A=0) = 0), whereas max[H(A) − H(S)] = 0.2716 bits at p(A=0) = 0.70711 = 1/√2, which is the paper's own Eq. (17) value (my computation). This is a typo in the statement, not in the result.
- **"0 ≤ C_work ≤ ln|S|" (Thm 3(ii) / Thm 8(ii), repeated in the dossier) should read log₂|S|.** Work is measured in units of k_BT ln 2, so it is in bits, and entropies are defined with log₂ (Eq. A1). The proof (Eq. G19) derives log|Y|. Read literally, with ln as the natural log, the bound is false. A unifilar product environment emitting a deterministic binary sequence has C_work = log₂2 − 0 = 1 bit > ln 2 ≈ 0.693, by the paper's own Lemma 9. The same slip appears elsewhere: Eq. (17) and Eq. (G64) write "½ ln(3/4 + 1/√2) ≈ 0.272 bits". In nats that expression is 0.188; 0.272 is ½·log₂(…). Def. 14 writes ln|A| where Eq. (G50) writes log|A|.
- **The dossier's framing overstates what the counterexample shows. It calls it a "trade-off" between prediction and forgetting, and it says remembering *past* actions is the problem.**
  - The Thm 5 environment (Fig. 5) is memoryless. What a predictive agent must hold is the *current* action A_t, which is drawn jointly with M_t. Lemma 10 shows that predictive ⇔ ⟨H(A_t|M_t)⟩ = 0 there.
  - The efficient agent retains nothing at all: it is memoryless. It fails the "mea" principle only because its actions are biased (p(0) = 1/√2), not because it balances memory against randomness (footnote [83], Lemma 9 proof "≥").
  - So in the one example proved, the optimum is "forget completely, but do not randomize uniformly". A graded balance of predictive memory against action entropy is described in §V and §VI, but no example exhibits it.
- **The paper's title says "channels with memory", but the separation is proved on a memoryless channel.** The results that do use environment memory are Thm 1 (existence of predictive agents for unifilar environments) and Thm 4 (unifilar product environments, where there is no feedback).
- **"C_work exists" (Thm 3(i)) is weaker than it sounds.** The proof (Eq. G17) shows only that each agent's Cesàro work rate exists, via Cor. 1(iii). It does not show that the maximum over the infinite set of finite-memory agent models is attained. The text itself calls it "the supremum" (App. G3, p. 34) while writing max. Thm 10 opens by asserting that A_eff is nonempty "for any environment" without proof. For the Fig. 5 environment attainment does hold (by Lemma 9), so Thm 5 itself is unaffected.
- **Theorem numbering differs between the main text and the supplement.** Main Thm 1 = Suppl. Thm 7; Thm 2 = Thm 6; Thm 3 = Thm 8; Thm 4 = Thm 9; Thm 5 = Thm 10; Table I = Lemma 9. The dossier cites main-text numbers only.
- **PRX version: partly verified.**
  - Crossref (api.crossref.org/works/10.1103/7nds-tjr8), fetched 2026-09-25, has the following:
    - type journal-article in Physical Review X (ISSN 2160-3308, APS), titled "Information thermodynamics of agents: The work capacity of channels with memory";
    - published online, accepted and issued all dated 2026-08-10;
    - an assertion date_received = 2025-04-23;
    - author "Anonymous", no volume or article number, and reference-count 0.
  - OpenAlex (W7202124094) mirrors this: author "Anonymous", no biblio, gold OA, cc-by.
  - The APS landing pages (link.aps.org, journals.aps.org/prx/abstract/…) return 403.
  - arXiv shows only v1 with no journal-ref, and /abs/2504.06209v2 is 404.
  - The circumstantial case that it is this paper is strong: the subtitle is identical, and the received date is 15 days after the arXiv v1. But the authors, the content, and any changes to results or framing are **unverified**. Whether the PRX version fixes the sign and ln typos above is unknown. The doi field should stay unverified, or be entered with an explicit note, until the author list can be seen.
