<!-- scratch/manuscripts/governance-of-possibility/03-time.md -->

# Part III. Time

Part II read identity stabilization as a filter over the frequencies of change, and found that the reading breaks for one kind of demand: "Fourier spectra cannot fully characterize event-triggered obligations, irreversible harms, or response deadlines" (CLAIM-tmppqdnv, Active, demonstrated; §4). This part starts from that limit. §6 describes demands by their deadlines, and asks how organizations facing them can be compared. §7 turns to the governing arrangement itself, whose parts act and are revised at different speeds, and asks what those speeds must be for the arrangement to stay answerable.

Citation, standing and voice follow the conventions stated at the head of Part II. Joins continue from JB6 and gaps from GB5. The models cited here are models. Where this part uses the readiness model of §9, the numbers are invented and the model shows only which of the draft's stipulations hold, and on what assumptions.

## 6. Demands have temporal structure

### 6.1 Readiness for a contingency, under intervention

Some demands are naturally stated as deadlines rather than frequencies: a hazard to be interrupted before an irreversible threshold, a supply disruption that allows some days for substitution, a workforce transition that takes years. The record's term for an organization's standing against such a demand is **scenario-conditioned response readiness**: "the probability that an organization operating under a specified policy can deliver an effective response to a specified contingency within its deadline" (TERM-115, Active; the wording is ChatGPT's, adopted at the status review of 2026-11-06). Formally,

  R^π_O(c, τ | s) = Pr_π(effective response by τ | do(c), s),

with c an imposed contingency, τ its deadline, s the organization's initial state and π the policy it actually follows. Three features of the definition carry the argument that follows.

- **It is defined under intervention.** "The do(c) is the point: this is readiness for a specified situation, imposed, not success conditional on the situations that happened to be observed. An organization that never met c has a value of R for it all the same." So readiness is not utilization or realized performance: "It is defined under intervention, so a record of what was done does not measure it."
- **It takes the policy as followed.** It is not operational availability, the chance that a resource is deployed before the deadline under the best procedure available (TERM-055). An organization can have every resource available and low readiness, "because its dispatch policy fails to mobilize them".
- **It is a family, not a number.** "No single scalar. The object is the family {R^π_O(c, τ_c | s) : c ∈ C}, one value per contingency and its deadline. Two organizations' readiness profiles can be incomparable, each more ready for some contingencies than the other."

The first feature connects this section to §3.2 and §4.1. An organization's ordinary record does not show its readiness, just as passive observation does not show what an intervention would expose (CLAIM-407, Active, demonstrated).

### 6.2 Readiness curves, and when two organizations are ranked

The motivating draft lets the deadline vary and writes R_i(S, t) as a curve over t, for demand i and organization state S. It then says that organizations "need not admit a universal ranking" and stops there. The record's note on that passage gives the condition the draft lacks. It is the assistant's, written as a dated note and not filed as a claim, because it is close to definitional:

"Since R_i(S, ·) is the distribution function of the response time, two organizations are ranked the same way at every deadline exactly when one curve lies at or above the other at every time (first-order dominance); where the curves cross, which is more ready is fixed only by the deadline" (TERM-115, note of 2026-11-23, the assistant's).

The model of §9 shows both cases (analysis/results.md, run of 2026-11-23; the numbers are invented). The regime that keeps a reserve covering the original route (II) dominates the regime that holds only what it uses (I) at every deadline. Regime I and a redesigned regime with a smaller reserve (III-b) cross. At t = 2, I is ready with probability 0.025 and III-b with 0, because III-b's staged route cannot finish in fewer than three periods. At t = 3 the order reverses (0.081 against 0.118), and III-b stays ahead from then on. Which of the two is "more ready" is a fact about the deadline, not about the organizations alone.

Two further steps follow, and both are this paper's (join JB6: TERM-115's family with its note of 2026-11-23).

- **Across a family of contingencies, a ranking needs dominance in every one.** TERM-115's object is a family over contingencies. Two organizations are ranked the same way for every contingency and every deadline exactly when one's curve dominates the other's for each contingency in the family. If one organization dominates for some contingencies and is dominated for others, no ranking exists without weights on the contingencies. That is TERM-115's "No single scalar", restated with the deadline free.
- **Any ranking beyond dominance imports a commitment.** Weights on contingencies, a choice of deadline, or a loss function on lateness all rank organizations whose curves cross. None of them is supplied by the curves. In §9's model the cheapest regime by long-run cost changes with the deadline, under one set of costs. Regime I is cheapest at τ = 2, the full reserve (II) from τ = 3 to 8, and the redesigned regimes at τ = 12 and 20. The break-even for keeping a reserve depends on the probability and loss of the contingency against the reserve's cost (analysis/README.md, items 5 and 6; the parameter is recorded in a note on QUESTION-395).

### 6.3 Deadlines shrink what can be met together

Readiness concerns one contingency at a time. Regulation faces several demands at once, and §2 described what an organization can meet jointly as a compatibility complex: the sets of demands that some attainable history meets, closed under taking subsets (CLAIM-347, Active, interpretive). The record holds what deadlines do to that complex:

"When demands are predicates on histories with deadlines, the sets of them an organization can jointly meet under its response architecture and budget form a downward-closed complex contained in the complex of the same demands without deadlines, so two demands can be compatible statically and incompatible in time, and a change in the response architecture, faster actuation, different sequencing, staged capacity or a new method, can enlarge the temporal complex without weakening any demand" (CLAIM-tmpdvgrf, Active, demonstrated). The idea is ChatGPT's (A44 §8). The containment step, and so the possibility of static compatibility with temporal incompatibility, is the assistant's.

The derivation is short. Every history that meets a demand by its deadline meets the same demand with no deadline, so the temporal complex K_{θ,B} lies inside the deadline-free complex K⁰_B under the same budget and safeguards. The containment can be strict. ChatGPT's factory can cut emissions and keep production, but may "lack the capacity to complete the conversion within the regulatory deadline while meeting uninterrupted supply requirements". The pair is jointly attainable without the deadline and not with it. A change of response architecture θ that adds attainable histories can enlarge the temporal complex for the same demands. By the record's result on hard constraints, that needs a change in the dynamics, not a constraint added at fixed dynamics (CLAIM-tmpk4bou, Active, demonstrated). ChatGPT adds, and the claim keeps, that this is "one possible mechanism, not a guarantee of monotone expansion". The record also counts a deadline as a resource type of its own, distinct from a stock, a capacity, a rate limit, a cumulative expenditure or a reserve (TERM-105, Active). The motivating draft does not use either entry. The audit of the draft excluded CLAIM-tmpdvgrf from the work because the draft does not state it. This paper states it.

**Readiness and the temporal complex are two views of one object.** The complex asks whether some admissible policy meets a set of demands by their deadlines. Readiness asks with what probability the policy actually followed meets one demand by its deadline when the contingency is imposed. The record already pairs existence with probability for demands without deadlines: "its compatibility complex says which sets of public demands some attainable history meets, the probability of meeting them under a model of participants' behaviour says how reliably the regime selects such a history, and a regime can improve either without the other" (CLAIM-tmpx9nrj, Active, demonstrated). CLAIM-tmpdvgrf says the same holds with deadlines: "Under stochastic dynamics the existence test becomes a probability of joint satisfaction, as in CLAIM-tmpx9nrj." *Reading TERM-115's readiness as the one-demand, imposed-contingency case of that probability, and so as the realization side of CLAIM-tmpdvgrf's temporal complex, is this paper's join* (join JB7: TERM-115 with CLAIM-tmpdvgrf and CLAIM-tmpx9nrj). On that reading, a set of demands in the temporal complex can still have low joint readiness, and enlarging the complex by redesign does not by itself raise readiness. §9's redesigned route without a reserve (III-a) is a model case: the route exists and is never affordable when needed, a result the record holds as the assistant's (CLAIM-tmpg8yl2, Proposed, demonstrated).

### 6.4 No universal ranking, and no optimum, until commitments are declared

The motivating draft concludes that "temporal adequacy is therefore demand-relative". The record holds a stronger, and Proposed, form, as ChatGPT's objection to the owner's thesis that regulations "operationalize a demand specification, chosen so as to steer an industrial ecosystem optimally toward harmonious governance" (CLAIM-tmpz67ew, Proposed, interpretive, the owner's, U16):

"There is no optimal regulation until the demand specification, the instruments, the horizon and the trade-offs among demands are declared, and a regime is better judged by a profile of possibility, realization, resilience, accountability and cost than by a scalar, so steering an industrial ecosystem optimally is relative to commitments the mathematics does not select" (CLAIM-tmphjm0q, Proposed, interpretive, a counter, ChatGPT's).

The claim "qualifies the thesis and does not reject it". It does not say regulation cannot be optimized: "Once the objective and the hard constraints are declared, A31 §6's programme is well posed." A note of the assistant's fills a step ChatGPT asserted. Regimes whose complexes each contain a face the other lacks are unordered under inclusion, so "even before realization, resilience and cost are added, the regimes need not have a best element" (CLAIM-tmphjm0q, note of 2026-11-22, the assistant's).

§6.2 adds a temporal reason to the same conclusion. Even on a single dimension, readiness for one contingency, organizations are ranked independently of the deadline only under dominance. A declared deadline, or a declared weighting of deadlines, is one of the commitments CLAIM-tmphjm0q says the mathematics does not select. That this is a case of CLAIM-tmphjm0q is part of join JB6.

## 7. The temporal architecture of governance

### 7.0 Levels of response, schematically

The motivating draft lays out four levels of industrial governance by horizon:

- operational controls (shutdowns, hazard responses, routine adjustments);
- reconfiguration (replacing suppliers, reallocating production, retraining);
- institutional processes (revising standards, reallocating authority, reconsidering classifications);
- the slow reproduction of knowledge, competences, public commitments and ecological conditions.

It adds that these "need not be arranged as a single hierarchy of command". A slow rule may authorize an immediate intervention, and a fast event may reveal a problem that needs institutional revision.

No entry on the record holds this hierarchy as such (gap GB5: the levels of governance by horizon). The nearest are three, and each is weaker than a hierarchy.

- **Five demand horizons.** ChatGPT's table of "immediate, operational, developmental, institutional, intergenerational" horizons, each with its capacity and failure mode, is a step of CLAIM-tmph25dl (Proposed, interpretive, ChatGPT's).
- **Schematic levels of will.** A hierarchy of "effective volition" by timescale, recorded on CLAIM-331 (Active, interpretive) with its own caption: "Schematic levels, not a demonstrated RG hierarchy" (note of 2026-10-18).
- **Speed and authority.** A Proposed claim that, in a political collective, components that change at different speeds differ in "which forms of influence each can accumulate, exercise and keep, and so which of them holds authority over the others" (CLAIM-423, Proposed, interpretive). Against it the record notes that "Slowness alone supplies no authority or motivational hierarchy" (CLAIM-331, note of 2026-10-18). Whether the authority one process has over others goes "with the slower variable, the faster one, or neither" is open (QUESTION-440, Open).

So the levels in this section are a schema for the argument. They are not a result.

### 7.1 Execution speed and revision speed

The motivating draft's central distinction here is between **execution speed**, how fast a governing commitment is applied, and **revision speed**, how fast the commitment itself can be changed. It credits the distinction to CLAIM-711 as support, without saying that the claim is Proposed. The claim is ChatGPT's, from another exchange, and it is an objection to one of the owner's claims.

The owner's claim: "Automation reduces procedural friction, yet procedural friction is where an opportunity to intervene in a process is exposed and perhaps what such an opportunity consists in, so removing friction can remove the points at which an unfolding decision can still be interrupted" (CLAIM-710, Proposed, interpretive, the owner's). It keeps both strengths the owner gave, "exposes" and the hedged "characterizes".

ChatGPT's objection: "A process with no procedural friction can still be interruptible: standing constraints set slowly in advance and enforced by mechanisms faster than the process can foreclose alternatives keep it open to intervention without delaying it, so an opportunity to intervene does not consist in friction" (CLAIM-711, Proposed, interpretive, a counter, ChatGPT's). Its condition: "The slow authority must have fast enough *actuators*, even if its deliberative processes remain slow." It objects to the "characterizes" reading of CLAIM-710 and leaves the "exposes" reading standing. What carries the opportunity to intervene, on this account, is a relation of speeds: the enforcing mechanism must act before the process forecloses alternatives, "whatever the speed of the deliberation that set the limit."

The record's note on the exchange behind this paper finds ChatGPT's later uses of the claim faithful. A42: "the rate of executing a decision can be separated from the rate of revising the rules that authorize it". A44: "Preauthorize fast actions that remain within the jurisdiction of the slower governing structure. ... The commitment is slow; its application is fast." (CLAIM-711, note of 2026-11-23.) What holds the claim back is the owner's: whether an independent execution gate counts as procedural friction (TERM-125, Proposed) decides whether CLAIM-711's case removes friction or relocates it. Promoting CLAIM-711 "would also make its concession due on CLAIM-710, the owner's own claim" (CLAIM-711, note of 2026-11-23).

CLAIM-711 also states its own limit: "That standing constraints suffice. They interrupt only the transitions anticipated when they were set. A novel failure still needs a channel through which someone can stop the process". A44 states the same residual case for an emergency outside the preauthorized categories, which needs "an escalation or revision pathway rather than merely faster execution of obsolete rules". The record also holds that the faithful use is about interruptibility, not lock-in. Its account of the exchange lists "'Stable governance against lock-in', cited to CLAIM-711 (A33 §6)" among what is "Not stated on the record": "CLAIM-711 concerns interruptibility, not lock-in or the means to revise constraints" (SYNTHESIS-tmp4zamw, Proposed). This paper keeps to the faithful use.

**Execution and revision as separately maintained capacities.** The record holds, Active, a family of separations that this distinction belongs to:

- "Maintaining a regime of effective action and maintaining the capacity to govern among regimes are not the same achievement" (CLAIM-099, Active, interpretive);
- "An operative regime, the governing organization among regimes, and the capacity to transform that organization can persist or fail separately" (CLAIM-025, Active, interpretive);
- "Stability does not entail viability: a system can occupy a stable regime while losing access to trajectories that keep satisfying its constraints" (CLAIM-079, Active, demonstrated);
- "An arrangement of institutions can keep, or increase, its capacity for effective action while its capacity to be effectively corrected by others degrades, because the two are maintained by different relations, so the first is no evidence of the second" (CLAIM-462, Active, interpretive).

*Reading fast execution of standing rules as effective action, and the rule-revising level as the capacity to govern among regimes and to be corrected, is this paper's join* (join JB8: CLAIM-711 with CLAIM-099, CLAIM-025 and CLAIM-462). On that reading the four separations predict the failure the motivating draft warns of: an arrangement that gets faster and more reliable at applying its commitments while the relations through which they could be revised decay, with the first no evidence of the second.

### 7.2 When the slow level dominates the fast

The worry has a sharper form on the record, and it is *supposed*: held only on the condition that an analogy carries. It is ChatGPT's, filed after the owner pointed to the record's "timescale separation":

"Where a slowly revised governing level (a statute, an objective, a classification) constrains a fast process, the fast process can change the world before the slow level can be revised, so those it harms have no route to the rule as fast as its application reaches them, and the rule dominates them without anyone actively intervening; where the slow level is open to revision on demand, the same separation of timescales keeps the fast process accountable instead" (CLAIM-730, Proposed, interpretive, supposed, ChatGPT's).

It is supposed because "it carries CLAIM-478's scale separation, a dynamical result, into institutions by analogy". Its defeater names the weak point: "that a governing rule is not a slow variable in CLAIM-478's sense, because what it constrains does not settle relative to it". That is the same carriage §3.1 makes, and the same gap (GB3).

The record has one model of it (CASE-316, Proposed; its result is CLAIM-879, Proposed, demonstrated). In a queueing model, the overseer kept the same authority, information and reviewers while the acting institution's speed varied. At ten times the speed, "the share of objectionable actions stopped before they became irreversible fell from 0.99 to 0.40", and to 0.04 when speed also multiplied the volume of actions. Precommitted limits, CLAIM-711's arrangement, "brought back about the share they foresaw", keeping "0.92 to 0.99" of the speed's benefit. Outside what they foresaw nothing was won back unless the overseer detected it in time by the ordinary route. Pauses won back capacity only by giving up the speed, and none at all when volume rose (CASE-316; CLAIM-711, note of 2026-11-22).

What the model shows and does not show is recorded on CLAIM-730 (note of 2026-11-22). "The second clause is thereby shown possible in a model." The first is not tested: "the model has no affected party and never revises a limit". And where escalations saturated the fixed reviewers, "the slow level kept the fast process answerable only while it had the capacity to hear what it held." No lead on the record tests the first clause (gap GB7: a model with an affected party and limit revision, to test CLAIM-730's first clause).

### 7.3 How fast a governing reference must move

Two Active results bound how fast governance must be revisable to meet a demand by its deadline. Both are ChatGPT's in wording and checked by the assistant.

**A necessary half.** "If practice must stay within ε of a governing reference that can be revised at most at rate v, a demand to bring practice within δ of a target at distance 1 by deadline H can be met only if vH ≥ 1 − δ − ε, so the same rate of revision is adequate to a demand with a long horizon and inadequate to one with a short horizon, and a fixed reference (v = 0) meets no demand farther than δ + ε" (CLAIM-tmp2k3c5, Active, demonstrated). The bound is tight when the practice can track freely within its band. Its limit, already used in §4, is that "it says nothing of what a fast-revisable reference costs against transient fluctuations".

**A sufficient half.** "If an organization's operation relaxes at rate γ toward a configuration h(θ) set by a governance parameter θ that changes at rate at most V, with h Lipschitz with constant L, then its distance from the governed configuration stays within LV/γ once it starts within that, so a governance change of size Δθ by deadline H keeps the organization within a tolerance ε if LΔθ/(γH) ≤ ε; the condition is sufficient, not necessary" (CLAIM-tmp947v0, Active, demonstrated). It names four obstructions: the reference moving too fast for its realization; "operation slowing, so that the permissible retuning rate falls"; governance unable to change θ fast enough for the deadline; and the cases the inequality does not settle.

The record already notes ChatGPT's way around retuning, preauthorization, as CLAIM-711 (CLAIM-tmp947v0, "What it shows"). Two further consequences are this paper's.

- **What preauthorization leaves bounded.** Preauthorization replaces revision only for the transitions anticipated when the limits were set (CLAIM-711). For a demand outside them the response must go through revision, and CLAIM-tmp2k3c5's floor applies: no response is in time unless vH ≥ 1 − δ − ε. So the speed of the revision pathway, not the speed of execution, bounds readiness for unanticipated demands (join JB9: CLAIM-711's limit with CLAIM-tmp2k3c5). §9's novel-demand arm is a model of the same thing (analysis/README.md, item 7). There a review that needs capacity cannot start under the rule that holds only what is used, and the demand is excised by default.
- **A slow mode is cheap to push and slow to retune.** CLAIM-tmpx8csq (§5.2) says a slowly relaxing mode is cheaper to redirect by direct input through the same channel. CLAIM-tmp947v0 says that when operation relaxes slowly toward a governed configuration, the governing parameter may move only slowly if operation is to stay within tolerance: V ≤ εγ/L. Both hold. They concern different channels: pushing the mode directly, and moving the configuration it relaxes toward. An organization whose operation has slowed is easier to redirect by intervention and harder to govern by changing its rules (join JB10: CLAIM-tmpx8csq with CLAIM-tmp947v0). Which channel a regulator has is the question §5.2 put to entrenchment.

### 7.4 The design principle, in the record's terms

The motivating draft ends §7 with a principle: "Slowly maintained commitments should enable rapid legitimate action, while remaining connected to effective procedures for recognizing when the commitments themselves require change." It credits the first half to CLAIM-711 and calls the second "the crucial additional requirement".

In the record's terms, the principle has three parts with different standings, and it is no stronger than the weakest.

1. **Fast application of slow commitments keeps a process interruptible without delaying it,** for the transitions the commitments anticipate. This is CLAIM-711, Proposed and held on TERM-125, with CASE-316 showing it in a model.
2. **What it does not anticipate needs a revision pathway fast enough for the deadline.** This is CLAIM-711's own limit, bounded by CLAIM-tmp2k3c5 (Active, demonstrated) through join JB9. Without that pathway, the slow level can dominate those the fast process harms (CLAIM-730, supposed).
3. **The pathway must be able to recognize that a demand has arisen.** An organization whose filter classes objections to its categories as noise will not open the pathway at all (CLAIM-tmp76xaw, Active, interpretive; §4.1). The record holds no mechanism for revising that classification (gap GB2). CASE-316's saturated reviewers add a material condition: the slow level must have the capacity to hear what it holds.

The motivating draft's "crucial additional requirement" is therefore the record's limit on CLAIM-711, read through the Active bounds of §7.3 and the Active claim of §4.1. What the record does not supply is any case of a real institution in which these parts were observed together. §8 takes up whether the capacity to keep all three can itself be kept, and §13 the governance of the revising level.

---

*Joins in this part:* JB6, ranking by readiness across contingencies and deadlines needs dominance in each, and anything more imports a commitment (TERM-115 and its note of 2026-11-23, with CLAIM-tmphjm0q); JB7, readiness as the realization side of the temporal complex (TERM-115 with CLAIM-tmpdvgrf and CLAIM-tmpx9nrj); JB8, execution and revision as separately maintained capacities (CLAIM-711 with CLAIM-099, CLAIM-025 and CLAIM-462); JB9, the revision pathway bounds readiness for unanticipated demands (CLAIM-711's limit with CLAIM-tmp2k3c5); JB10, a slow mode cheap to push and slow to retune (CLAIM-tmpx8csq with CLAIM-tmp947v0).

*Gaps in this part:* GB5 (the levels of governance by horizon), GB7 (a test of CLAIM-730's first clause); GB2 and GB3 recur from Part II.
