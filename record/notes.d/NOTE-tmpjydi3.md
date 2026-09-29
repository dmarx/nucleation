---
status: Read
paper: LIT-327
title: 'Thermodynamics of Prediction'
version: 1
history:
- version: 1
  date: '2026-09-29'
  note: >-
    Read in full (The full text of arXiv 1203.3271 v3 (5 Oct 2012, the last
    revision; v1 15 Mar 2012), from the arXiv PDF, 5 pp. I read the
    abstract, the introduction, "Problem setup", "Dissipation out of
    equilibrium", "Predictive power, memory, and dissipation", "Lower bound
    on total dissipation", the Landauer refinement, the Discussion and
    Conclusion, footnote [24] (the one-line derivation of Eq. 14) and all 31
    references. Nothing was skipped. The text was extracted with PyMuPDF.
    Eq. (2) is garbled in extraction and was reconstructed from its
    surroundings. I re-derived Eq. (14) from footnote [24] and Eqs. (1),
    (8), (11) and (13). I did not read the PRL version of record (the PRL
    title drops the article) and have not compared it with v3.). The first
    NOTE on this paper, which was seeded from its abstract alone.
date: '2026-09-29'
summary: >-
  For a system driven by a stochastic signal through a fixed Markov
  kernel, the average work dissipated as the signal steps x_t → x_{t+1}
  equals, in units of k_BT, the system's instantaneous nonpredictive
  information, I[s_t;x_t] − I[s_t;x_{t+1}] (Eq. 14). Summed over a
  protocol, this total "nostalgia" lower-bounds dissipation and excess
  work (Eq. 18), and it adds to Landauer's bound: −β⟨Q⟩ ≥ I_e + I_mem −
  I_pred (Eq. 21). All three are averages over paths and protocols. None
  of them is a per-operation or per-bit floor on the cost of storing or
  using predictive information.
---

# NOTE-tmpjydi3: Thermodynamics of Prediction

## Contribution

Earlier nonequilibrium work relations assumed a known driving protocol, such as the Jarzynski and Crooks relations [3, 5] (p. 1). This paper averages over stochastic protocols drawn from an arbitrary P_X. Doing so identifies an information-theoretic quantity with a thermodynamic one. The dissipation incurred when the signal changes equals the part of the system's memory of the current signal that does not carry over to the next signal value. Summed over a protocol, this nonpredictive information lower-bounds total dissipation. Adding it to Landauer's erasure bound gives a tighter heat bound for systems that keep memory.

## Key insight

A driven system implicitly models its environment, because its state s_t correlates with the signal. When the signal moves on, whatever s_t "knew" about x_t that does not bear on x_{t+1} becomes, in expectation, work that is irretrievably lost. So energetic efficiency and predictive modelling are the same demand. A system that must keep memory can approach minimal dissipation only if that memory is predictive.

## Assumptions

- **Discrete-time Markov dynamics** with a *fixed* kernel p(s_t | s_{t−1}, x_t) (p. 1; the kernel is held fixed except for the Discussion's speculation about adaptation).
- **Alternating work and relaxation steps.** Work is done only when the signal changes, W = E(s_{t−1}, x_t) − E(s_{t−1}, x_{t−1}) (Eq. 1). Heat flows only during relaxation (p. 2).
- **No feedback** from the system to the signal. P_X is otherwise arbitrary and need not be known to the system (p. 1).
- **Initial equilibrium**: p(s_0|x_0) = p_eq(s_0|x_0) = e^{−β(E(s,x_0) − F_0)}, with the system coupled to a single bath at temperature T (p. 1).
- **Nonequilibrium free energy** is defined relative to the *current signal value only*: F_neq[p(s|x)] = ⟨E⟩ + k_BT⟨ln p(s|x)⟩ (Eq. 8). The additional free energy k_BT·D_KL[p(s_τ|x_τ) ‖ p_eq(s_τ|x_τ)] (Eq. 6) is attributed to ref. [13] (Shaw, *The dripping faucet*), which looks like a mis-citation for [20–22].
- **Relaxation steps contract toward equilibrium** on average: ⟨ΔF_neq^relax⟩ ≤ 0 (Eq. 16). The paper justifies this in one sentence ("the system evolves toward equilibrium"). It needs p_eq(·|x_t) to be stationary under the kernel at fixed x_t, as for a detailed-balance thermal kernel, and the paper does not state this as an assumption.
- Every quantity is an **ensemble average**, over system paths and over protocols. There are no single-trajectory statements.

## Key results

- **Eq. (10).** The average dissipation for a given protocol is the excess work minus the final additional free energy: ⟨W_diss⟩ = ⟨W_ex⟩ − F^add_τ ≤ ⟨W_ex⟩.
- **Eq. (14), the first result.** β⟨W_diss[x_t → x_{t+1}]⟩ = I_mem(t) − I_pred(t), where I_mem(t) = I[s_t; x_t] and I_pred(t) = I[s_t; x_{t+1}]. Footnote [24] derives it in one line: the energy terms cancel and β⟨W_diss⟩ = H[s_t|x_{t+1}] − H[s_t|x_t]. I re-derived this, and it is an identity given the definitions (8), (11) and (13).
- **Eq. (17).** Summed over the protocol, β⟨W_diss⟩ = I_mem − I_pred − β⟨ΔF^relax_neq⟩, with I_mem = Σ_{t=0}^{τ−1} I_mem(t) and likewise for I_pred.
- **Eq. (18).** I_mem − I_pred ≤ β⟨W_diss⟩ ≤ β⟨W_ex⟩, using (16) and (10).
- **Eqs. (19)–(21), the refinement of Landauer's principle.** With I_e := H[s_0|x_0] − H[s_τ|x_τ] (conditional entropy removed from the system), −β⟨Q⟩ = I_e + β⟨W_diss⟩ ≥ I_e (Eq. 19). Hence −β⟨Q⟩ ≥ I_e + I_mem − I_pred (Eq. 21). Q is heat *into* the system, so this is a lower bound on heat released of k_BT·(I_e + nostalgia), in nats. Per bit erased that is k_BT ln 2, but only on the I_e term. The paper notes that I_e "is not mutual information about the driving signal" (p. 4).
- **Discussion (qualitative).** "Any system … with nonzero memory must conduct predictive inference, at least implicitly, to approach maximal energetic efficiency" (p. 4). The paper connects this to the information bottleneck for prediction ([11], Still 2009): maximise predictive power at a given memory.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Average dissipated work in the step x_t → x_{t+1} equals k_BT·(I[s_t;x_t] − I[s_t;x_{t+1}]) | strong (derivation) | Eq. (14), footnote [24]; an identity given the definitions; re-derived |
| C2 | Total nostalgia lower-bounds total dissipation and excess work | strong (derivation), with an implicit assumption | Eqs. (15)–(18); rests on ⟨ΔF^relax_neq⟩ ≤ 0, which needs p_eq(·\|x) to be stationary under the kernel (unstated) |
| C3 | Heat released ≥ k_BT·(I_e + I_mem − I_pred): Landauer "augmented by the total nostalgia" | strong (derivation) | Eqs. (19)–(21) |
| C4 | The results hold "arbitrarily far from equilibrium" for "a wide range of systems, including biomolecular machines" | moderate | Far from equilibrium, yes: nothing assumes near-equilibrium. The breadth claim is an assertion; no biomolecular system is modelled |
| C5 | Any system built to keep memory "has to be predictive" to operate at maximal efficiency | informal argument | Follows from C2 for the nonpredictive term; "maximal efficiency" is not defined beyond minimising the C2 bound |
| C6 | The result links nonequilibrium thermodynamics and learning theory | assertion | Conclusion; the only learning-theory content is the pointer to IB-for-prediction [11] |

## Method

This is analytic stochastic thermodynamics of a discrete-time driven Markov chain with separated work and relaxation steps (the Crooks 1998 setup, [17]). Free energies are generalised to arbitrary conditional distributions (Eq. 8), dissipation is decomposed step by step, and the information terms come from rewriting entropy differences as mutual informations. There are no examples, simulations or experiments.

## Concepts

- **Instantaneous memory** I_mem(t) = I[s_t; x_t]. **Instantaneous predictive power** I_pred(t) = I[s_t; x_{t+1}].
- **Nostalgia**: the nonpredictive information I_mem − I_pred, "useless nostalgia" (p. 3).
- **Nonequilibrium free energy** F_neq (Eq. 8), its additional part F^add = k_BT·D_KL(p ‖ p_eq) (Eq. 6), **dissipated work** vs **excess work** (Eqs. 9–10).
- **Erased information** I_e: the decrease in conditional entropy H[s|x] over the protocol.

## Connections

- [LIT-041](../literature.d/LIT-041.md) (Fiderer et al. 2025, work capacity of channels with memory) is the direct descendant, and it qualifies this paper's slogan. Once the system's actions feed back into the signal, which this paper excludes by its no-feedback assumption, maximal prediction is no longer necessary for efficiency. Read the two together: this paper is the feedback-free baseline that [LIT-041](../literature.d/LIT-041.md) breaks.
- [LIT-338](../literature.d/LIT-338.md) (Tishby, Pereira & Bialek, the information bottleneck) is the ancestor of the "maximise predictive power at fixed memory" objective the Discussion recommends, by way of Still 2009 [11]. The paper gives that objective a thermodynamic reading, though only for the *nonpredictive* remainder.
- [LIT-328](../literature.d/LIT-328.md) (Landauer 1961) is refined by Eq. (21). I_e is the Landauer term, and the nostalgia term adds to it.
- [LIT-308](../literature.d/LIT-308.md) (Goldt & Seifert 2017) is the companion "thermodynamics of learning" result. It bounds information *acquired* by total entropy production, where this paper bounds information *kept but useless* by dissipation.

## Bearing on the record

**What it supplies for map row 13.** The map files this paper as part of the field that "owns" the physics of the §5 floor: Q ≥ k_BT ln 2 · C_step per step, and more generally k_BT ln 2 per predicate bit (the owner's gradient-channel-thermodynamics §5B). The paper does own a thermodynamics-of-prediction physics, but not that physics. Specifically:

1. **It prices nonpredictive memory, not information.** Eq. (14) says a unit of *useless* memory costs k_BT of dissipated work, a nat not a bit. Predictive memory costs nothing in this accounting. A per-judgment floor charged on all the bits written, which is what "Q ≥ k_BT ln 2 · C_step" does, is not what the paper proves. If anything the paper says a well-adapted system pays *only* for the part of what it holds that fails to generalise to the next input.
2. **Its only per-bit heat floor is Landauer's**, on I_e, the conditional entropy *removed* from the system (Eq. 19). That applies to erasure or reset, not to acquiring or evaluating a bit. This matches the owner's own caveat in §5B, that the floor bites on erasure.
3. **Everything is an average** over paths and protocols in a fixed-kernel, feedback-free, initially-equilibrated model. There is no statement about an individual operation ("judgment").
4. **An unflagged limit on (14) as a floor.** By my own analysis, not stated in the paper, the per-step nostalgia I[s_t;x_t] − I[s_t;x_{t+1}] is guaranteed nonnegative only when the drive is Markov, by data processing on x_{t+1} – x_t – s_t. The paper's "P_X need not have specific properties" (p. 1) holds for the identities. But for a non-Markov drive a state that remembers x_{t−1} can predict x_{t+1} better than it tracks x_t, and then the step "dissipation" as defined (via free energies conditional on the current x only) comes out negative. So the lower bound (18) is not a nonnegative cost in general.

So the map's verdict should be adjusted. "The physics is textbook; the field owns it" holds for Landauer's erasure floor and for the nostalgia bound. It does *not* hold for a per-judgment k_BT ln 2 on every predicate bit written or evaluated. That bridge is not merely "synthesis": as stated it is stronger than what this paper, or [LIT-308](../literature.d/LIT-308.md), supports. A defensible version says that each bit of predicate *erasure* (overwrite or reset) costs at least k_BT ln 2 (Landauer), and that memory which fails to predict adds dissipation k_BT per nat of nostalgia (this paper, Eq. 21).

For ML practice: nothing. It is a physics result. Its nearest ML reading ("useless memorisation is energetically wasteful") is suggestive and unquantified for real hardware, which runs many orders of magnitude above these floors.

## Limitations

- It is a model-level identity with no worked example. The abstract's reach ("biomolecular machines") is not illustrated.
- The Markov-drive caveat on the sign of the per-step nostalgia is unstated (see Bearing, point 4). So is the kernel-stationarity condition behind (16).
- Mutual informations are in nats, and "k_BT ln 2 per bit" appears nowhere. Readers who port the result as a per-bit cost are converting units, not quoting the paper.
- The dissipation is defined through F_neq conditional on the current signal value only. It is the thermodynamically relevant dissipation only for an observer who knows x_t and nothing else about the history.

## Open questions

- Does the bound tighten or change sign under feedback? [LIT-041](../literature.d/LIT-041.md) answers part of this for percept-action loops.
- Is there a single-trajectory (fluctuation-theorem) version of Eq. (14)? The paper gives only averages.
- For learning systems, where the kernel itself changes as weights update, the fixed-kernel assumption fails. The Discussion raises adaptation but proves nothing about it.

## Corrections to the seeded skim

- Seeded from metadata; the text shows the seed summary is accurate as far as it goes ("nonpredictive information … equivalent to thermodynamic inefficiency measured by dissipation, … arbitrarily far from equilibrium"). It omits the paper's second result, the refinement of Landauer's principle (Eq. 21), which is what row 13 of the map actually needs.
- Identification: the arXiv abstract page lists v1 (15 Mar 2012) to v3 (5 Oct 2012). The arXiv title is "The thermodynamics of prediction" and the seed's PRL title drops the article, as its source-ok comment already records. The authors and affiliations on the PDF are Still (Hawai'i at Mānoa), Sivak and Crooks (LBNL) and Bell (Redwood Center, UC Berkeley), matching the seed. The seed's DOI and published date are taken as given (not checked against the PRL).
- Map row 13 cites this paper as owning the physics of a "per-step heat Q ≥ k_BT ln 2 · C_step" floor. The paper proves no such thing. Its per-step result (Eq. 14) is an *equality* for the dissipated work of a work step, and it is proportional to the *nonpredictive* information only. A system whose memory is fully predictive (I_mem = I_pred) has no nostalgia term at all. The only information-proportional *heat* bound in the paper is the Landauer term I_e, the decrease in the system's conditional entropy H[s|x] over a whole protocol (Eq. 19). It is stated in nats, as an average over paths and protocols.
