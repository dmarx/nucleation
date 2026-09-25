---
status: Read
paper: LIT-005
title: 'Adding causality to individuality'
version: 1
date: '2026-09-25'
summary: >-
  Of Krakauer et al.'s (2020) three mutual-information "individuality"
  terms (A* = I(S_{t+1}; S_t), A = I(S_{t+1}; S_t | E_t), nC = I(S_{t+1};
  E_t | S_t)), Bourrat argues that nC and A* are not individuality
  measures. He then proposes the interventional Â = I(S_{t+1}; Ŝ_t) (Eq.
  6) and two ETI criteria: C1, a normalised Â_{S2}/H(Ŝ2) ≥
  Â_{S1}/H(Ŝ1)|θ₀, and C2, low Var(Â_{S2} | Ê2 = ê2k). None of these is
  computed on any system. The paper's claim that Â ≡ I(S_{t+1}; S_t | E_t)
  = A in Krakauer's model is false in general.
---

<!-- inactive-ok-file: LIT-005 — Proposed by this reading; the note is the reading that placed it -->

# NOTE-tmpugtg1: Adding causality to individuality

## Contribution

The paper makes three moves, all conceptual.
- It argues that Krakauer et al.'s decomposition I(S_t, E_t; S_{t+1}) = A* + nC = Ei + A (Eq. 5) gives three candidate individuality measures, and that two of them fail to capture "propagating information through time":
  - nC concerns E → S, not S over time;
  - A* is purely associative and is confounded by E.
- It defines a causal replacement, Â = I(S_{t+1}; Ŝ_t), the mutual information under an intervention on S_t, following Griffiths et al. 2015 and Pocheville et al. 2017 (Eq. 6).
- It sketches how Â could diagnose an evolutionary transition in individuality (ETI) under Black et al.'s (2020) ecological-scaffolding model. There are two criteria: C1 (potential individuality, normalised Â compared across coarse-grainings) and C2 (endogenised scaffold, low variance of Â under interventions on the environment).

## Key insight

"Propagates information through time" is a causal claim. So an individuality measure must be causal as well. Consider an environment that fully determines S at every step (Fig. 2). It makes S_t and S_{t+1} correlated, and a mutual-information measure will score S as an individual when it is only "a reconstructed entity". Intervening on S_t removes that confound. Under intervention the Fig. 2 system scores Â = 0, while A* can be positive.

## Assumptions

- **Discrete random variables** throughout (§2, p. 2).
- **Krakauer et al.'s setting (§3):**
  - a discrete Markovian stochastic process over micro-variables, coarse-grained into two macro-variables S and E;
  - any of the 2ⁿ − 2 bipartitions is admissible;
  - the DAG of Fig. 1, in which S_t and E_t each influence both S_{t+1} and E_{t+1}.
- **An interventionist (Woodward/Pearl) account of causation.** A causal DAG is assumed known, so that do() can be emulated from observational data by an adjustment formula (§5, p. 8). The paper does not state the conditions an adjustment set must meet: "the exposition of which would go well beyond the scope of this paper".
- **An intervention distribution must be chosen** for Ŝ_t: uniform, the population distribution, or a "normal" range, "depending on the explanatory goals" (fn. 4). The value of Â depends on this choice, and the paper does not fix it.
- **For §6:**
  - A new level of individuality equals a new unit of selection (fn. 5).
  - The ETI follows the ecological-scaffolding scenario (Black et al. 2020), with the scaffold eventually endogenised.
  - The total number of micro-variable values stays constant through the ETI (p. 13).

## Key results

No theorems, no computations, no data.

- **Eq. 5.** The decomposition is taken from Krakauer et al.:
  - I(S_t, E_t; S_{t+1}) = A* + nC, where A* = I(S_{t+1}; S_t) and nC = I(S_{t+1}; E_t | S_t);
  - it also equals Ei + A, where Ei = I(S_{t+1}; E_t) and A = I(S_{t+1}; S_t | E_t).
  - High A* is Krakauer's "organismal individuality", high A their "colonial individuality", and high nC their "environmentally determined individuality".
- **§4.** nC is discarded because it measures E → S. A low nC fits both non-individuals and clear individuals, and the paper suggests it may instead track something like evolvability (fn. 3). A* is discarded because it is associative (Fig. 2 confounding).
- **Eq. 6.** Â = I(S_{t+1}; Ŝ_t). In the Fig. 2 world, Â = 0 while A* > 0 is possible.
- **Claimed equivalence (p. 9).** "Once this adjustment formula is applied to the model proposed by Krakauer et al., the minimal conditioning that yields an equivalence with Â from observations is E_t, so that Â = I(S_{t+1}, Ŝ_t) ≡ I(S_{t+1}; S_t | E_t) = A." The paper adds that "Â and A are not equal in general" because they come from different perspectives.
- **Fig. 3 example (p. 9).** This is a 2-time-slice DBN with E split into E_a and E_b and within-slice influences:
  - E_a → S;
  - S → E_b;
  - E_b → S across slices.

  Here conditioning on E_bT would block the mediated path S_T → E_bT → S_{T+1}. The paper says the "correct adjusted measure" is I(S_{T+1}; S_T | E_aT).
- **§6.** An ETI initiated by scaffolding shows up as I(E1_{t+1}; Ŝ1_t) increasing over time, and as Â rising for a new coarse-graining S2 that absorbs part of E1 (Fig. 4a–c). The two criteria:
  - **C1:** S2 is a *potential* level of individuality if Â_{S2} / H(Ŝ2_t) ≥ [Â_{S1} / H(Ŝ1_t)] evaluated at θ₀, a time before the ETI. The paper normalises because S2 may simply have more states. It notes that normalisation penalises few-state systems and proposes an observer-chosen floor on H(Ŝ_t).
  - **C2:** S2 *defines* a new level of individuality if Var(Â_{S2} | Ê2 = ê2k) is low across the possible interventions on E2_t. This is inspired by Woodward's (2000) notion of invariance. The paper notes that Â_{S2} | Ê2 = ê2k resembles Ay & Polani's (2008) information flow.
- **§7 (limitation stated by the author).** Â still cannot tell a genuine individual from a part of one (a tissue, half an organism). The proposed fix is to take individuals as "the coarsest grain of description in which Â is maximal", which is left for future work.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Krakauer et al. are concept-pluralists about individuality (A*, A, nC name different types) and give no reason to prefer one | informal argument (textual reading) | §4, p. 6, citing Krakauer et al. p. 215 |
| C2 | nC is not a measure of individuality because it concerns E→S, not S over time | informal argument | §4, p. 6 |
| C3 | A* can be positive with no causal S_t→S_{t+1} link when E is a common cause | informal argument (correct) | §4, Fig. 2 |
| C4 | Â = I(S_{t+1}; Ŝ_t) is a causal measure of individuality, zero in the Fig. 2 world | definition + informal argument | §5, Eq. 6 |
| C5 | In Krakauer's model, adjusting for E_t makes Â ≡ I(S_{t+1}; S_t\|E_t) = A | **assertion, false in general** | §5, p. 9. Counterexample (mine): S_{t+1} = S_t ⊕ E_t with S_t, E_t independent and uniform. Then A = I(S_{t+1}; S_t\|E_t) = 1 bit, but p(s_{t+1}\|do(s_t)) = Σ_e p(s_{t+1}\|s_t,e)p(e) = ½ for every s_t, so Â = 0 under any intervention distribution. Adjustment gives the do-distribution; a conditional MI averages within-stratum MIs, which is a different quantity. |
| C6 | In the Fig. 3 DBN the correct adjusted measure is I(S_{T+1}; S_T\|E_aT) | **assertion; incomplete by the paper's own DAG** | §5, p. 9, Fig. 3. The figure has E_b,T−1 → S_T and E_b,T−1 → E_bT → S_{T+1}. That backdoor path (and S_{T−1} → E_b,T−1 → …) stays open when conditioning on E_aT alone. {E_aT, E_b,T−1} would block it (my reading of the figure). The C5 point applies as well. |
| C7 | Conditioning on E_bT in Fig. 3 would remove the mediated effect S_T → E_bT → S_{T+1} | informal argument (correct) | §5, p. 9 |
| C8 | A scaffolding-initiated ETI shows as I(E1_{t+1}; Ŝ1_t) increasing and Â_{S2} increasing for an enlarged coarse-graining | assertion | §6, p. 11, Fig. 4; no model or computation |
| C9 | C1 (normalised Â comparison) is a criterion for potential individuality | proposal | §6, p. 12 |
| C10 | C2 (low variance of Â under interventions on E) indicates an endogenised scaffold, i.e. a completed ETI | proposal | §6, p. 13 |
| C11 | Â cannot by itself distinguish an individual from a part of one | author's stated limitation | §7 |

The abstract says the paper will "illustrate how this measure can be implemented". The body gives no implementation or illustration with numbers. It offers DAG sketches and verbal criteria only. The one implementation-level statement, the adjustment in C5/C6, is the part that is wrong.

## Method

1. Coarse-grain the micro-variables into S and E (any bipartition).
2. Choose an intervention distribution for Ŝ_t (fn. 4).
3. Compute Â = I(S_{t+1}; Ŝ_t), either from interventions or from observational data through an adjustment formula under an assumed DAG.
4. For an ETI:
   - Fix a reference individual S1 at time θ₀.
   - Track I(E1_{t+1}; Ŝ1_t) and Â for enlarged coarse-grainings S2.
   - Apply C1: normalised Â_{S2} is at least normalised Â_{S1} at θ₀, with a floor on H(Ŝ_t).
   - Then apply C2: low Var(Â_{S2} | Ê2 = ê2k) over interventions on E2.

This is my note. A correct observational route to Â first forms the do-distribution p(s′ | do(s)) = Σ_z p(s′ | s, z) p(z) for a valid adjustment set Z. It then takes the MI of that channel under the chosen input distribution for Ŝ. That is not I(S′; S | Z), and the paper conflates the two (C5).

## Concepts

- **Informational individual** (Krakauer et al., as read here): an aggregate that propagates information from past to future and keeps temporal integrity. Bourrat reads "propagates" causally. A system passively reconstructed by its environment is "merely a reconstructed entity" (§3, p. 4).
- **A\*** — the observational autonomy I(S_{t+1}; S_t). In Krakauer's scheme it is "organismal individuality".
- **A** — the conditional autonomy I(S_{t+1}; S_t | E_t) ("colonial individuality").
- **nC** — non-closure, I(S_{t+1}; E_t | S_t) ("environmentally determined individuality").
- **Ei** — environmental influence, I(S_{t+1}; E_t).
- **Â** — the causal (interventional) mutual information I(S_{t+1}; Ŝ_t). The hat marks do().
- **ETI** — evolutionary transition in individuality: particles come to form collectives that become individuals in their own right.
- **Ecological scaffolding** (Black et al. 2020): external ecological structure first imposes Lewontin-like collective-level properties. The ETI completes when the scaffold is endogenised and collectives keep their integrity without it.
- **Concept vs measure pluralism** — many concepts of individuality, versus one concept with several partial measures (§4).

## Connections

- **Item 21 ([LIT-025](../literature.d/LIT-025.md), the ΦID review).** Its §IV A holds that information measures on p(X′|X) are interventional only if that conditional is a do()-distribution and faithfulness and the causal Markov condition hold. Otherwise they are predictive (reads/21, C4). Bourrat makes the same point for Krakauer's individuality measures, but neither paper cites the other. C5 above is exactly the confusion item 21's footnote warns against: treating an observational conditional quantity as the interventional one.
- **Item 22 ([LIT-027](../literature.d/LIT-027.md), Varley & Hoel).** Hoel's effective information is MI under a maximum-entropy *intervention* distribution (reads/22, Eq. 10). Take Bourrat's Â with the uniform option of fn. 4 and E marginalised at its natural distribution. Structurally that is EI of the S_t → S_{t+1} channel (my observation). Bourrat does not cite Hoel. His fn. 4 leaves open the choice that EI fixes by convention, and item 22's cross-scale comparisons are the kind his C1 needs.
- **Coarse-graining.** Items 21 and 22 and Bourrat all make the unit of analysis a partition or coarse-graining of micro-variables. Bourrat's 2ⁿ − 2 bipartitions (§3) is the same search space as the "parts" and macroscales there. His §7 "coarsest grain at which Â is maximal" is a scale-selection rule of the same kind as Hoel's "causal emergence".
- **Named lineage:**
  - Krakauer et al. 2020 (Theory Biosci. 139:209), extended;
  - Griffiths et al. 2015 and Pocheville et al. 2017 (causal-specificity MI), applied;
  - Ay & Polani 2008 (information flow) and Bertschinger et al. 2008 (autonomy), noted as prior causal versions by some of Krakauer's co-authors;
  - Black et al. 2020 (ecological scaffolding);
  - Bourrat 2023 (a coarse-graining account of individuality).

## Bearing on the record

- In nucleation this is [LIT-005](../literature.d/LIT-005.md). Its summary is accurate on the proposal. It should add two things. First, the measure is never computed. Second, the paper's stated equivalence between Â and Krakauer's A, and its adjustment set in the Fig. 3 example, do not hold as stated (C5, C6). So [LIT-005](../literature.d/LIT-005.md) should not be cited as showing how to estimate causal individuality from observational data.
- It supports and contradicts no THEORY document in the Anthology of the SOTA.
- It carries no instruction for ML practice. The contrast between association and intervention in information measures is a familiar point in causal inference and in causal-representation-learning work. The paper makes no ML connection, and the analogy is the reader's. Nothing here warrants an ANTH- document.

## Limitations

- **No worked example.** Â, C1 and C2 are never evaluated on any model or data, and the "implementation" in the abstract is verbal.
- **C5 is false in general.** Â ≡ A in Krakauer's model does not hold (XOR counterexample above). What adjustment licenses is replacing p(s′|do(s)) with Σ_e p(s′|s,e)p(e). The MI of that averaged channel is generally different from the conditional MI I(S′; S | E). The paper's own caveat, "Â and A are not equal in general", is given the wrong reason ("different perspectives") when the real issue is mathematical.
- **C6 is incomplete.** Judged by the paper's own Fig. 3, adjusting for E_aT alone leaves a backdoor path through E_b,T−1 open.
- **Â depends on the intervention distribution (fn. 4), which is left open.** That makes C1's cross-coarse-graining comparisons ill-defined until it is fixed. C1's normalisation H(Ŝ_t) is itself a function of that choice.
- **C2 is qualitative.** "Low" variance has no threshold, and there is no account of which interventions on E2 are "possible".
- **The author's own limitation (§7):** Â cannot separate individuals from their parts.
- **Two notation slips:** p. 3 labels H(X|Y) as "the entropy of Y conditioned on X"; p. 9 writes I(S_{T+1}; S_t | E_aT, Eb_bT).

## Open questions

- Is there a worked ETI model (for example a simulated ecological-scaffolding population) in which C1 and C2 can be computed? Would they classify the transition as the verbal account predicts?
- What is the right observational estimator of Â in Krakauer's DAG? Under what conditions, if any, does it coincide with A? Resolving that would decide whether Krakauer's "colonial individuality" is a proxy for causal individuality or a different quantity.
- Which intervention distribution should Â use, and does the choice change which coarse-graining is "the" individual? Item 22's maximum-entropy convention is one answer; the population distribution is another.
- How does Â relate to the ΦID decomposition (item 21) when S is itself composed of parts? Would "individuality" be better read as synergistic or as redundant self-prediction?

## Corrections to the seeded skim

- The dossier's details came through a summariser. The full text confirms the formula Â = I(S_{t+1}; Ŝ_t) (Eq. 6, hat = do()). It also confirms the section list and the two ETI criteria. The dossier did not report the following:
  - the argument "against pluralism" (§4), which rejects nC and A* as individuality measures;
  - a third quantity, I(E1_{t+1}; Ŝ1_t), whose rise over time the paper proposes as the signal that a scaffolding-type ETI has started (§6, p. 11);
  - the normalisation caveat on C1: normalised Â penalises systems with few states, so the paper proposes an observer-set floor on H(Ŝ_t) (p. 13).
- The dossier reports the "reported" Krakauer measures as organismal, colonial and environmentally determined individuality. The text maps them as A* ↔ organismal, A ↔ colonial and nC ↔ environmentally determined (§3, p. 5).
- The dossier's summary line ("Replacing the observed past state with an intervened-on one gives a causal … measure") is right about the move. It omits that the paper then asserts an equivalence it does not justify: that Â equals Krakauer's A in their model. By my own counterexample below, that equivalence fails. The body shows less than the dossier implies.
- The dossier gives the year as 2024 and the venue as vol. 14 no. 1 art. 9. The article page header confirms "(2024) 14:9", received 2 Jul 2023, accepted 19 Dec 2023, online 16 Feb 2024.
