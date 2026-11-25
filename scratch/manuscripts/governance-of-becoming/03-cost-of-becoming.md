<!-- scratch/manuscripts/governance-of-becoming/03-cost-of-becoming.md -->

# Article 3. The Cost of Becoming

### Stored work, contractual lifecycles, and the resource-bounded geometry of possibility

**Abstract.** An organization that has stabilized some of its relations has done work that it need not do again. It pays to keep that work, to find and check it when it is used, and to change it. This article sets out what the Nucleation record holds about that trade, and with what standing. The owner's thesis, which the record holds as Active, is that a stabilized constraint can be stored work: by replacing later work with cheaper operations, it can move a task within a fixed per-task budget, so that amortization becomes an expansion of capability, with no new degrees of freedom or resources added. The record's demonstrated results then separate what forming, keeping and moving into an organizational form cost. They show that the budget needed to reach a configuration is the least peak along a path, and not the cost of holding the configuration, and that going and coming back can differ. So the affordability of a state does not establish the affordability of reaching it. A cost model run on three cases prices stored work with one set of terms, at illustrative values. The run (CASE-326) is Active and the claim drawn from it (CLAIM-891) is Proposed, and the model holds the store fixed between uses. The article then asks what changes when the store is a contract whose use can change it. The record's answer is a Proposed claim with a test that has not been run. ChatGPT, whose claim it is, expects richer state variables, not new cost terms, to cover most of the cases. The article separates work saved from work transferred, and keeps four predicates on a transition apart: whether it is physically feasible, affordable, authorized and permissible. The readiness, reserve and stored-work studies that this ground calls for have already been run (CASE-343, CASE-315, CASE-412, CASE-397, CASE-326), and the record already demonstrates that what one party can reach unaided shrinks under a supply that does its work (CLAIM-675, CLAIM-602). What the record lacks is the actor- and authority-indexed reach that the motivating draft makes its formal centre. That is an open lead, narrowed to the authority index and the four predicates, and this article does not use it as a result.

## Conventions and limits

**Citation.** Each step cites the entry of the Nucleation record that holds it, with its standing on 2026-11-24. **Active** means the record accepts the entry, and **Proposed** means it is filed and argued but not adopted. Questions and leads are **Open**. The warrant is **demonstrated** (by construction or derivation), **empirical** (observed) or **interpretive** (argued). Codes are bare. Entries with temporary codes (CLAIM-tmp…) were filed from the exchange "Memes, Contracts, and Systemic Normativity" (2026-11-24) or from this manuscript's gaps. All are Proposed or Open, except CLAIM-tmp8mpgs (Active, §3.6.3). Several entries that carry this article's model are not members of the work `governance-of-becoming`: CLAIM-303, CLAIM-567, CLAIM-582, CLAIM-591, CLAIM-891, CLAIM-892, CLAIM-1016 and CLAIM-1117, and, among those this revision adds, CLAIM-675, CLAIM-602, CLAIM-646, CLAIM-677, CLAIM-996, QUESTION-392 and CLAIM-tmp8mpgs (a gap fill, not a member (ADR-tmpenzcn)). The CASEs cited cannot carry the field. They are cited here where they are used, and whether to add them is the owner's call.

**Sections** are numbered by article: §3.*n* is this article's, and §2.*n* is Article 2's.

**Voices.** "The owner" is the record's owner, and their turns are U*n* of the exchange named. "ChatGPT" is the other assistant in those exchanges. The record's quotations call it "A", and A*n* are its turns. "The assistant" is Claude, which filed the exchanges and supplied some constructions and derivations. An Active entry is the record's whatever its origin. A Proposed entry is told in the voice of whoever proposed it. Where an entry's thesis is the owner's and a clause in it is not, the clause is credited to whoever wrote it. The owner's turns are numbered within each exchange, so U17 of "Topological protection explained" (2026-11-18) and U17 of the exchange of 2026-10-27 are different turns.

**Joins and gaps.** Where the first draft joined steps that the record keeps apart, it labelled the join J3.*n*. An independent reader then tested each join under ADR-075 (review of 2026-11-24, Part B). The closing section gives each verdict. None of this article's joins passed. Where a join failed, the text no longer asserts it. Where the argument needs a step that the record lacks, the gap is labelled G3.*n* and cites the entry that now holds it.

**Limits.** The argument was developed with AI assistants: ChatGPT in the exchanges, and Claude filing and checking them. Both assistants also study the record that holds the argument. Three consequences should be stated before the argument.

- *Standing granted under delegation.* Almost every Active entry this article stands on was made Active at a status review whose rulings the owner delegated (ADR-057). That includes CLAIM-761 and CLAIM-760 (2026-11-20), the demonstrated results of §3.2 and §3.6 (CLAIM-569, CLAIM-571, CLAIM-591, CLAIM-567, CLAIM-577, CLAIM-582, at the reviews of 2026-11-06), and CLAIM-303, CLAIM-679, CLAIM-675 and CLAIM-703 (2026-11-18). CLAIM-tmp8mpgs was made Active on 2026-11-24, the day it was filed, at the assistant's discretion, after an independent checker reproduced its computations. The owner had left the promotion of verified entries to that discretion.
- *Record wording written by this drafting.* CLAIM-569's note of 2026-11-24 and CLAIM-tmpsf9hp's bullet on TERM-116, both used in §3.6.3, were corrected on 2026-11-24 on a finding by this manuscript's drafter. QUESTION-tmpzhnqy and LEAD-tmple60r were filed from this draft's gaps. In these places the record and the manuscript are not independent.
- *Models, not measurements.* Most of what follows is formal. The constructions establish that certain things *can* come apart. They do not establish that they do come apart in any organization. CLAIM-571 says so of itself: "That organizations have such an r. The construction is formal; an organizational configuration space with a holding requirement is A's model, not something the record has measured" (CLAIM-571, "What it does not say"). The readiness account says the same of its own line: it does not say "That the readiness argument applies to any real organization; its constructions and models say their organizational readings are analogies" (SYNTHESIS-031, Proposed). The cost model's cases were priced "from the sources' numbers where they exist" and "from illustrative values, tagged as such, where they do not (Hutchins measured nothing)", and "Any measured cost" is the first thing it says it cannot show (CASE-326, Active). In what follows, a model is a model, and a lead is a study that has not been run.

---

## 3.1 Organization as stored work

### 3.1.1 The owner's thesis

The article begins with the owner. At U17 of the exchange "Topological protection explained" (2026-11-18), the owner read ChatGPT's sentence "Selective contraction can expand capabilities when the stabilization of some relationships reduces the resources needed to realize valuable alternatives" as "an excellent formalization of something else Nucleation has tried to develop: a theory of how constraint can relate to amortization of work, and the tradeoff between memory (amortizing a value) and computation (rederiving it just in time)". ChatGPT then stated the thesis (A39 §10), and the record holds it in ChatGPT's wording as the owner's thesis:

> "A stabilized constraint can be stored work: by replacing later work with cheaper operations it changes which activities are realizable within a fixed per-task budget, so amortization becomes capability expansion without any added degrees of freedom or resources; the expansion is conditional on the costs of constructing, keeping, retrieving, verifying and revising the constraint and on the distribution of later demands, and the persistence that buys it can entrench" (CLAIM-761, Active, interpretive).

The record already held the thesis's parts before U17. Three are in entries whose theses are the owner's, though not every clause the thesis uses is in the owner's words:

- **The owner's conjecture.** After reading Hutchins on the cockpit, the owner wrote that "amortized retrieval is actually a kind of amortized computation" (QUESTION-095, Open, 2026-10-15). The question asks whether leaving a result where it can be cheaply retrieved is the same trade as amortizing a computation.
- **Stored inquiry.** CLAIM-475 (Active, interpretive) is the owner's thesis, from U17 of the exchange of 2026-10-27: "resource constraints impact specification in exactly the same way as they impact realization. I can't interrogate a question that takes me more time than I have to even ask it." Its clause on stored inquiry, "a stabilized specification is past inquiry stored so that later questions become cheaper to ask, and it can make other questions harder", is a consequence that ChatGPT drew at A17 and A18. The claim's summary says so: "A17 and A18 drew a consequence … A stable specification amortizes the work that made it".
- **A guard.** CLAIM-443 (Active, interpretive) begins from the owner's question of 2026-10-23, "what if we just treat this as a kind of momentum term? or like a hebbian prior?". Its limit, "persistence is not amortization, which is shown only when earlier work replaces later computation, communication or recruitment", was kept when the idea was "Worked through the same day (workbench entry of 2026-10-24, U9–U12)". The limit is from that working-through, not from the owner's turn.

The fourth part is ChatGPT's, written at the owner's request for "content to the effect of computation-storage tradeoffs". It states the accounting: "Filing an argument moves work across time: it is paid for now … against reconstruction later, so it is worth its cost only when expected reuse covers it" (CLAIM-303, Active, interpretive). The claim is about the record's own filing. A dated note on it of 2026-11-24 flags a later citation of it for automation as a miscitation, since "this claim is about filing an argument in the record, not about automation" (CLAIM-303). This article cites it only for its accounting. CLAIM-761's summary says what it added: "No claim joined constraint, amortization and capability".

### 3.1.2 From amortization to capability

CLAIM-303 prices stored work by totals, so stored work is worth having when reuse covers its cost. CLAIM-761's step is different. A question costs 12 units to formulate and investigate from scratch, and 3 with an acquired framework. Under a per-task budget of 5, the first is out of reach and the second is within it. "This is the point where amortization becomes capability expansion" (CLAIM-761, after A39 §1). The stored work moves the task across the budget line "whether or not its construction has yet been repaid". The claim adds: "That is CLAIM-571's point that a threshold is a peak, not a total" (CLAIM-761). Reading a per-task ceiling as a peak in this way is the claim's own step (J3.1, a restatement).

The claim keeps two failures apart, and the article keeps them apart too.

- **An operational failure.** The stored work does not lower the least cost of the task, retrieval and verification included, enough to change what is feasible under the budget. That failure defeats the claim.
- **An economic failure.** The lifetime savings never repay construction and upkeep. That failure "defeats only the stronger reading that the investment was worthwhile, which the claim does not make" (CLAIM-761, defeat condition).

The claim's own example makes the point: "A procedure that costs 100 to acquire and cuts a task from 12 to 3 makes the task feasible under a budget of 5 whether or not the 100 is ever repaid" (ChatGPT's example, at its second review; CLAIM-761).

What "capability expansion" means here is narrow. The task was possible before and too dear for the budget. Whether such an intervention "create[s] a capability the system lacked, rather than make one it already had cheaper, faster or more reliable to reach, and how can the two be told apart" is an open question on the record (QUESTION-392, Open). CLAIM-761's "expansion" is the second, relative to a budget.

Two guards limit the thesis.

- **CLAIM-582.** "Under a fixed dynamical model an added hard constraint cannot enlarge the set of admissible trajectories, so it cannot enlarge what some admissible path reaches or lower the least cost of reaching it" (CLAIM-582, Active, demonstrated). A stabilized constraint that lowers a cost has therefore "changed the mechanism: it supplies cheaper operations (a procedure, an index, a framework) and not only a restriction" (CLAIM-761). The thesis is about constraints of that kind. It is not a claim that restriction as such enables.
- **CLAIM-443.** Its limit, as CLAIM-761 reads it, is that a constraint amortizes "only when keeping and using it costs less than re-solving" (CLAIM-761, reading CLAIM-443).

### 3.1.3 What the thesis does not support

CLAIM-761 names the reading it "invites and does not support": "That every emergent organization is such an investment". ChatGPT's closing sentence at A39 stated that reading, and the owner asked at U18 to develop it. "Some persistent structure saves no work" (CLAIM-761, citing CLAIM-443 and CASE-116's unread slow register). Nor is the expansion shown to be an expansion of freedom. Whether "newly affordable operations widen substantive freedom, and for whom, is CLAIM-352's question" (CLAIM-761; CLAIM-352, Active, interpretive, the owner's).

The record also separates amortization from slowness. "Dynamical separation of time scales … and economic separation (costly formation, cheap repeated use) are different and come apart both ways: a slow variable can save no work, and a result reused cheaply need not be an attractor of any dynamics" (CLAIM-755, Proposed, demonstrated; ChatGPT's, A39 §3). CLAIM-475's summary had identified the two, and its note of 2026-11-19 corrects that identification (SYNTHESIS-106). This article does not read "stored" as "slow".

### 3.1.4 Instances: accommodation, authorization, and the accounts

Two entries apply the thesis's logic to coordination and to permission.

**The owner's local accommodation.** "Learned local accommodation can reduce the amortized cost of recurrent arbitration: where a recurring conflict among an agent's processes admits a stable accommodation, settling it among the processes can cost less over repeated encounters than escalating each instance to a higher-level process" (CLAIM-358, Proposed, interpretive; the owner's, U45 of the exchange of 2026-10-17, in ChatGPT's conditional form). Its sharp edge: "it does not say local settlement is always cheaper". ChatGPT later counted a learned coordination structure as "A fourth kind of stored work", one that "stores neither an answer nor an index" (QUESTION-095, note, A39 §2, after CLAIM-358 and CLAIM-443). Reading CLAIM-358 as stored work is therefore a restatement (J3.11, of QUESTION-095's note). It is an amortization in CLAIM-303's sense, a lower total over repeated encounters. CLAIM-358 names no per-task budget that the accommodation lets a conflict fit within, so the article does not read it in CLAIM-761's sense either.

**Authorization paid once.** "Authorization granted question by question puts its cost between formulating a question and investigating it, on the same budget, while a standing grant pays it once for a domain before any question in it is formulated" (CLAIM-1016, Proposed, interpretive; the assistant's gap fill; not a member). The claim says it reads the standing grant "as stored work (CLAIM-761) amortizes a cost over the tasks it serves". Section 3.7 returns to it.

**The accounts.** The record's account of this region is SYNTHESIS-106 (Proposed), "Stored work and the cost structure of possibility". Its hinge is "the thesis the owner endorsed at U17 (CLAIM-761)", and it says of itself that it "maps the components and adds nothing". Its "Not stated on the record" section keeps one thing open that this article must not close. CLAIM-761 says what stored work does to a budget, but "no entry says that cheap retrieval and amortized computation are the same trade". The owner's conjecture, QUESTION-095, is still Open. SYNTHESIS-106 sits inside a wider account, SYNTHESIS-107 (Proposed), which runs "From equivalence to recursive capability, as a chain of separable achievements", one link of which is that "persistent organization replaces repeated work". It says that "the chain as a whole is a proposed sequence the record does not assert". SYNTHESIS-106 was written on 2026-11-19, before the cost model of §3.2 and before the contract entries of §3.3, and it integrates neither. It also gives CLAIM-761 and CLAIM-760 as Proposed, though both have been Active since 2026-11-20. No account maps the cost model as it now stands (G3.1).

---

## 3.2 The general cost model

### 3.2.1 Three requirements of a form

"A form has at least three resource requirements, to construct it, to maintain it, and to move into or out of it, and none fixes another: a capability can be cheap to keep and costly to acquire, so having enough to sustain it is not having enough to acquire it" (CLAIM-569, Active, demonstrated). The three requirements are ChatGPT's proposal, and the construction that demonstrates them is the filer's. An organization has a budget of 10 a year and spends 7 on what it already does, which leaves a surplus of 3.

- **Capability X** costs 24 to build and 2 a year to keep. X can be sustained, since its upkeep fits the surplus. It cannot be acquired within any one year, since its construction exceeds both the surplus and the whole budget.
- **Capability Y** costs 6 to build and 4 a year to keep. Y can be acquired from two years' surplus. It cannot be sustained, since its upkeep exceeds the surplus.

So "Construction and maintenance rank in opposite orders", and "Moving into a form is not building it": converting from a form whose staff carry over might cost 14, not 24 (CLAIM-569). The record's thematic account of these results, with CLAIM-571, CLAIM-567, CLAIM-577 and TERM-106, is SYNTHESIS-112 (Proposed): "Forming, keeping and moving into a capacity are separate resource requirements in the record, reaching a configuration can cost more than holding either end, feasible, reachable and reliably reached come apart, and a budget pegged to last period's peak loses transitions that need slack".

The claim's scope needs care, because the motivating draft reads more into it.

- It says "at least three", and it does not say "That these are the only three". Leaving a form "has costs of its own; A counts them with entry" (CLAIM-569, "What it does not say").
- It says that none of the requirements fixes another. It does not say that they move in opposite directions. A note of 2026-11-19 records ChatGPT's addition that "the same investment can lower the first while raising the second" ("An organization can be inexpensive to operate while expensive to revise", A43 §3.3). The same note records that ChatGPT hedged this "under some workloads" and called it "Not a universal inverse relationship". The note concludes: "That fits this claim, which says no requirement fixes another, not that they move oppositely" (CLAIM-569).

### 3.2.2 One model, three cases

The record's cost model is the result of LEAD-108, run by the assistant on 2026-11-22. The model has two routes for meeting a stream of demands: compute each time, or build a store once, keep it and read it back, falling back to computing when the store does not serve or is wrong. The terms were "fixed before any case was priced" (CASE-326, Active, executed study):

- F, construction, and λ_F, the price of work at the moment it is paid;
- U, upkeep;
- π, the chance that a demand is one the store serves;
- ρ, retrieval, and "miss", the cost of finding out the store does not serve;
- v, verification, and δ, the chance that verification catches a wrong result;
- σ, L and R: staleness, the loss from using a wrong result undetected, and revision when it is caught;
- ε, erosion of the on-demand route;
- spill, the added retrieval cost the store imposes on other demands;
- c, the on-demand route's cost;
- λ and B, the price of work at the moment of demand and the work available then;
- "party", who pays each item.

A served demand on the store route costs

  ρ + v + σ[δ(c(1+ε) + R + σ_A L_A) + (1 − δ)L].

The model reports three verdicts and keeps them apart. **Feasibility** is the chance that a demand is met correctly within B. **Lifetime** is the priced total. **Distribution** is the same totals broken down by party (CASE-326).

**What was expected before the run.** LEAD-108 was filed on 2026-11-19 and run on 2026-11-22. Before the run it stated one criterion and its falsifier, and no expectation about any case's verdict: "One model that prices all three with the same terms answers QUESTION-114 … A case it cannot price without a new term is a counterexample to the single trade" (LEAD-108, "What would count"). The three cases were not sampled. They are the three that QUESTION-114 (Open) named as the test. The per-case results below are therefore reported without expectations stated in advance. They are what the run found, not tests that it passed.

**What it found.** The criterion was met with the terms as fixed. A model with the four terms that QUESTION-095's note of 2026-10-15 listed and LEAD-108 named, together with "CLAIM-303's, CLAIM-761's per-demand budget and CLAIM-760's parties does price all three … without adding a term for any of them". The four listed terms "alone do not: the cockpit is carried by the price of work at the moment it is done, which they lack" (CLAIM-891, Proposed, interpretive; the assistant's; not a member). The claim drawn from the run is the assistant's: "One cost model prices a crew's speed bugs, a filed argument and a LEGO bin with the same terms, once work is priced by the moment it is done and checked against the budget for each demand, not only summed" (CLAIM-891). The run does not show that the terms suffice in general, and the case says so: "That the terms are complete" is among what it "cannot show" (CASE-326). Its results, at values that are illustrative except where a source gives them:

- **The cockpit's speed bugs.** As the approach's workload rises relative to the moment the bugs are set, "the bugs lose at 1 and 1.5 and win from 2". So the bugs pay by moving work to a quieter moment, more than by reuse (CASE-326, CLAIM-891).
- **A filed argument.** Pricing staleness "turns a saving of 11 into a loss of 1 at three uses" (CASE-326).
- **A LEGO bin.** For one copy of a brick among 200 similar ones, the bin "pays at its first use". For a brick that stands out, "a bin never pays" (CASE-326).

Three results do not depend on the illustrative values (CASE-326, "What it can show"):

- with π = 1 and a flat price of work, the bugs repay their setting only if F < 4(c − ρ − v);
- erosion is weighted by the chance of falling back, (1 − π) + πσδ;
- a construction at a quiet moment and a construction at the moment of demand are "the same term, λ_F F".

The second is stated as a claim: erosion costs, per demand, "εc[(1 − π) + π(σδ + φ)]", where φ is the share of the skill that checking the stored result repeats. So "it weighs little where demand is predictable, the store rarely wrong and checking cheap, as with a cockpit's speed bugs, and most where reuse cannot be forecast or checking re-derives, as with a filed argument" (CLAIM-892, Active, demonstrated; the assistant's; not a member). The run was repeated on 2026-11-24 by a session other than the filer's: "the 7 tests of `test_costmodel.py` pass, and `price_cases.py` regenerates `results.json` and `results.md` byte for byte" (CASE-326, note of 2026-11-24).

Two of the model's limits matter for what follows. "ε is a fixed fraction, not a function of how long the store has been relied on" (CASE-326, its choices). And "Anything about the record's own filings" is outside what it can show: its filing numbers are "A11's construction and illustrative values" (ibid.). The first limit is not a gap in the record as a whole. For a capacity learned by doing, the record already demonstrates erosion that depends on the history of reliance: outside supply that does the work "first lowers the capacity kept, and the longer it does all of it the longer recovery takes once it stops" (CLAIM-602, Active, demonstrated). That model is not CASE-326's, and no entry puts the one into the other.

### 3.2.3 The motivating draft's seven expenditures

The motivating draft lists "Construction, invocation, verification, upkeep, remediation, revision and dissolution" and calls them "independently variable expenditures distributed across participants and timescales" (A49, Article 3, abstract; ChatGPT's draft, not the record). The record holds the list, but not under those names and not with the clause "independently variable" (J3.3, a restatement of the mapping):

| The draft's term | Where the record holds it |
|---|---|
| construction | F (CASE-326); the first of CLAIM-569's three requirements |
| upkeep | U (CASE-326); CLAIM-569's maintenance |
| invocation | ρ, retrieval (CASE-326). For a contract, only part of the cost of invoking it is retrieval (§3.3.3) |
| verification | v and δ (CASE-326) |
| remediation | R, "revision when caught" (CASE-326) |
| revision | R; and, as a change of form, CLAIM-569's transition requirement |
| dissolution | no term of its own in the model: "A counts them with entry" (CLAIM-569). The nearest entry that treats dissolving as a capacity of its own is CLAIM-tmp0gs0t (§3.6.2) |
| erosion of alternatives (the draft's §2) | ε (CASE-326; CLAIM-892) |
| staleness (the draft's §2) | σ (CASE-326) |
| across participants | "party" and the distribution verdict (CASE-326, from CLAIM-760) |
| across timescales | λ_F and λ, the price of work by moment (CLAIM-891) |

The record demonstrates independence for two pairs only. Construction and maintenance can rank in opposite orders (CLAIM-569). Holding a configuration and reaching it can need different budgets (CLAIM-571, §3.6). That all seven terms vary independently is not stated on the record, and this article does not claim it.

---

## 3.3 Contracts as stateful stored work

### 3.3.1 The owner's question

The owner's question, at U21 of the exchange "Memes, Contracts, and Systemic Normativity", came after the owner's implicit contracts at U14 and U16 (Article 2, §2.3): "let's integrate contract formation, persistence, and modification in our cost model. It might actually already be in there already under other names like ambiguous invocation of relationship" (QUESTION-tmpb7fx7, Open; the owner's). The idea of an ambiguous invocation is the owner's. The name "relational invocation" is ChatGPT's (A30, A32) (curation entry of 2026-11-24 20:56, "Correction, 2026-11-24: who named 'relational invocation'"). The motivating draft lists "relational invocation" first among the programme's contributions and does not credit the owner's idea.

The filer checked the owner's suspicion and found it half right. "Formation, persistence and modification: held, for any form." But "Ambiguous invocation of a relationship: not held. No entry uses the phrase or a synonym" (QUESTION-tmpb7fx7).

### 3.3.2 The lifecycle is already priced

The held half is a restatement (J3.2). Read as a stabilized relational constraint, a contract has CLAIM-569's three requirements: "a construction (formation), a maintenance (persistence) and a transition (modification and exit) requirement, none fixing another". "The exchange supports and applies the claim; it adds nothing to it" (CLAIM-569, note of 2026-11-24, the assistant's).

ChatGPT made the same move for inquiry: "A contract can be a materialized answer to a historically recurring question about how processes should interact" (CLAIM-475, note of 2026-11-24, A18 §8). ChatGPT also read CASE-326's terms contractually (A30 §2): F as formation, U as maintenance of expectations, ρ as identifying and invoking the contract, v and δ as checking applicability and compliance, σ as the inadequacy of inherited arrangements, R as renegotiation, and ε as "the loss of independent capability through reliance". The record holds that reading as a formal application (ARG-tmpa5ped, Proposed; the inference is ChatGPT's, the answers to its critical questions the assistant's). CLAIM-303's break-even then reads n > F/(c − ρ − v − u), which is n > 4.8 at A30's values (F = 24, c = 8, ρ + v = 2, u = 1; checked in ARG-tmpa5ped). Where invocations do not change the arrangement, as with "an explicit, externally enforced agreement", "the assumption holds and the model applies as it stands" (ARG-tmpa5ped).

### 3.3.3 What is not priced: an invocation that changes the store

ChatGPT's point at A30 §7 is the article's hinge from stored work to contracts: "A cached result normally substitutes for a computation without intentionally changing the underlying problem. Contracts can change the problem." The record holds it as a Proposed claim, in ChatGPT's voice:

> "Invoking a relationship differs from reusing a stored result in that the invocation can change the relationship it invokes, so one operation can reproduce, form or transform a contract, and a stored-work cost model that holds the store fixed between uses prices a contract's lifecycle but not its invocation, which returns an act, a distribution of costs over the parties and the relationship's next state" (CLAIM-tmpsf9hp, Proposed, interpretive).

The invocation's formal objects are Article 2's (§2.8): Invoke(q, C_t) → (a_t, C_{t+1}) and the relational kernel K_C(q). What matters here is the cost model. CASE-326's store "is the same before and after a use, and σ and ε enter as fixed parameters" (ARG-tmpa5ped). For a contract, the erosion of the parties' alternatives and the inadequacy of the arrangement "are produced by its invocations". Where they are, "the per-demand cost is path-dependent and the fixed-parameter formula misprices it" (ibid.). CASE-326's own note of 2026-11-24 calls this "A qualification of scope, not of the case: for a store whose use changes it, σ and ε are not fixed."

The two halves fit together. CLAIM-569's note says the exchange adds nothing to the lifecycle. CLAIM-tmpsf9hp says the model misprices invocation. These claims concern different things, and this article claims only what each says: the lifecycle is held, with CLAIM-569 Active; the pricing of invocation is a Proposed claim.

The cost of resolving *which* relationship an act invokes is a further strain. "When an act could invoke more than one relationship, the uncertainty is of three kinds needing different remedies": epistemic ambiguity, "resolved by information"; relational disagreement, "resolved by negotiation or arbitration"; and constitutive indeterminacy, "resolved only by forming one" (CLAIM-tmp80ny9, Proposed, interpretive; ChatGPT's, at the owner's U21). ChatGPT mapped this cost to ρ. The assistant's answer to the critical question finds the mapping loose: "Only the first of CLAIM-tmp80ny9's three kinds is a retrieval or verification cost" (ARG-tmpa5ped). The other two are a negotiation and a formation.

### 3.3.4 Expectation, what is already done, and the test that has not been run

The record holds a test, and it has not been run. LEAD-tmp14n26 (Open, stage idea; ChatGPT's wording, the assistant's design) would make the store "a state updated by its own use", C_{t+1} = Φ(C_t, q_t, a_t, f_t), with ε and σ "functions of the history of invocations rather than fixed parameters". It would then:

1. build two relationships matched in per-use cost and output at the start, one whose invocations leave it unchanged and one whose invocations expand its practical jurisdiction and erode the recipient's alternatives;
2. price each over a horizon, per party, including revision and exit at the end;
3. ask whether "time-varying ε, σ and R suffice" or a term of a new kind is needed.

**What the record has already done (this revision's sort).** Part of the lead's role is played by held work. Erosion that depends on how long a supply has done the work is demonstrated for a capacity learned by doing (CLAIM-602, Active, demonstrated, §3.2.2). Two forms of support that give the same capabilities now "can leave it different capabilities later" (CLAIM-675, Active, demonstrated). That is step 1's matched pair, for a capacity rather than a contract. A state whose funding follows its own use is run in CASE-343 (Active, executed study, §3.5.2), and CLAIM-921's note of 2026-11-24 carries it to "rarely invoked guarantees": "The contract might remain formally recognized while its guarantee becomes unrealizable" (A32 §9). What no entry does is the lead's contract case: an invocation that expands a relationship's jurisdiction, priced per party, with the question whether a new term is needed. The lead is *done in part*. Its extension is the contract case and the per-party ledger, as the lead's note of 2026-11-24 says.

**The expectation, stated before any result.** ChatGPT, whose claim it is, expects richer state to cover most cases, not the null: "the critical test is whether these require genuinely new cost terms, or merely richer state variables and transition mechanisms within the existing model. I suspect the latter will cover most of the cases" (A30 §15, in CLAIM-tmpsf9hp). "Most of the cases" leaves a residue, and the lead's third outcome is that residue. The lead's outcomes are stated before any result:

- **CLAIM-tmpsf9hp is defeated** "if the two relationships' later costs never part, or part only by an amount the fixed-parameter formula with a re-estimated ε reproduces";
- **the "richer state" reading is confirmed** "if time-varying ε, σ and R suffice";
- **a new term is needed** "if a per-party cost of resolving or contesting the invocation does not reduce to them" (LEAD-tmp14n26).

If richer state suffices, an invocation that changes the store is CASE-326 with state-dependent parameters, and "relational invocation" names a reparametrization, not a new cost. The claim's own defeat condition anticipates this, citing A32 §21: "relational invocation" may be "only a vocabulary" (CLAIM-tmpsf9hp). Until the lead is run, this section offers a Proposed claim, a design and the held results above, and no result for contracts.

---

## 3.4 Distributed accounting

### 3.4.1 Work saved, transferred, or capability expanded

"That an organization makes an activity cheaper for those who perform it does not show that work was saved: the work may have been transferred, to an earlier time, to upkeep, or to other parties, and the efficiency an organization appears to have depends on the boundary of the system whose costs are counted; work saved, work transferred and valuable capability expanded are three separate achievements" (CLAIM-760, Active, interpretive). The claim is ChatGPT's (A62 §9), filed at the owner's request after the first filing had left it as a note.

The separating case is a claims office. The office's cost per claim falls from 3 to 1. Each claimant now spends 4 putting their case into the office's categories, where before they spent 1. "Counted at the office, the work fell by 2 per claim; counted over office and claimant, it rose from 4 to 5. No one can do anything they could not do before" (CLAIM-760). CLAIM-303's criterion, reuse covering cost, "is met for the office and says nothing of the claimants" (ibid.). The claim names the stronger reading it does not support: "That organizations which transfer work are wrongful" (ibid.).

The cost model carries the boundary as a term. "party" is CASE-326's term for who pays each item, and it comes from CLAIM-760. The run shows the boundary moving a verdict on the record's own filing. Counting only the session's work, the filing breaks even at 1.7 uses. Counting the owner's review at four times a session's price, it breaks even at 3.3 uses, "and three uses lose". "This is CLAIM-760's boundary, applied to the record" (CLAIM-891, "Choices that are the owner's"; CASE-326). These are alternatives that the run prices and that the owner has not chosen between. They are not theses of the owner's.

Three Proposed entries in the record hold cases where what a relationship saves falls unevenly on its parties. None of them cites CLAIM-760, and this article does not join them to it.

- **A regulatory surplus.** "Cooperation yields a regulatory surplus, the monitoring, verification, contingency planning and conflict resolution that reliance makes unnecessary, and the surplus can be captured asymmetrically", "under the same visible harmony as a relationship that shares it" (CLAIM-tmp8bimm, Proposed, interpretive; ChatGPT's, A24 §§8–9).
- **Compensation read as adequacy.** Where "members' conscientious compensation covers an organization's shortfall and the organization budgets to what it observes, the compensation and the quiet it buys are read as adequacy" (CLAIM-700, Proposed, interpretive; ChatGPT's, A33 of "Assess Depp Heard Abuse").
- **A commitment used as a resource.** "an institution can come to run on what it so avoids paying, with the burden falling hardest on its most conscientious members" (CLAIM-713, Proposed, interpretive; ChatGPT's). Section 3.7.2 returns to it.

### 3.4.2 The draft's four categories

The motivating draft asks the article to distinguish work "eliminated, transferred, deferred and embodied in acquired capacities" (A49, Article 3, §4). Three of the four map onto CLAIM-760 and CLAIM-761:

- work **eliminated** is CLAIM-760's work saved;
- work **transferred** is CLAIM-760's work transferred, "to an earlier time, to upkeep, or to other parties";
- work **embodied in acquired capacities** is CLAIM-760's "valuable capability expanded", which is "CLAIM-761's capability expansion" (CLAIM-760, "Rests on").

**Deferral** is different. Work moved to a *later* time, not done now and owed later, possibly at a higher price, is not among CLAIM-760's movements. CLAIM-760 lists only movement "to an earlier time". Four entries come close.

- ChatGPT's gloss reads technical debt as "an increase in the cost or decrease in the reliability of organizational transitions" (CLAIM-569, note of 2026-11-07, A32 §7 of "Individuation, Possibility, and Disposition").
- Deferring a reform imposes on each participant a cost ∫₀ᵀ L_i(t) dt, "substantial even if the decision-making institution incurs little immediate expenditure" (CLAIM-760, note of 2026-11-24, A40 §4.4). The note reads this as transfer to other parties.
- In a worked comparison, waiting a period while "the status quo erode[s] the capacity to transform" raises the transition cost from 40 to 70 (CLAIM-tmp8mpgs, Active, demonstrated; the assistant's gap fill under ADR-137, for A38 §3). This is a deferred cost that grows, in numbers, though the claim frames it as the price of delay and not as a movement of work.
- "Where the reactive work that restores a failing condition and the engineering that would remove its cause draw on one budget and the reactive work takes precedence, an organization can stay operationally viable while its capacity to transform itself is consumed" (CLAIM-tmpjoaj3, Proposed, interpretive; ChatGPT's, A34 §7).

No entry states deferral as a movement of its own. The question is held as QUESTION-tmpzhnqy (Open; G3.2).

### 3.4.3 The costs of contesting and of being heard

Three entries locate costs that an accounting at the organization does not see. Each is a cost the organization passes to those it affects.

- **The owner's friction thesis.** "Automation reduces procedural friction, yet procedural friction is where an opportunity to intervene in a process is exposed and perhaps what such an opportunity consists in" (CLAIM-710, Proposed, interpretive; the owner's, U11 of "Assess Depp Heard Abuse", keeping both the owner's "exposes" and the hedged "characterizes"). ChatGPT developed it at the owner's U12: "The cost of imposing a decision and the cost of questioning, suspending or reversing it are separate … friction moves from the exercise of power to its contestation" (CLAIM-731, Proposed, interpretive). CLAIM-760 itself says that "the contesting cost a transfer imposes is CLAIM-731's subject", so reading contestation cost as part of the accounting is a restatement. The entitlements whose costs these are, explanation, contestation and interruption, "are separate entitlements" (CLAIM-740, Active, interpretive).
- **The legibility tax.** "an institution can steer which questions are pursued by deciding who must pay to make them legible, with no rule against any idea" (CLAIM-1117, Proposed, interpretive; ChatGPT's, A56 §4 of "Explain First Contact RL"; not a member). It files a point that a note on CLAIM-303 had earlier left as "close to definitional".
- **Who pays to resolve an ambiguity.** "who resolves the ambiguity, when, and at whose cost can matter more than how ambiguous it is: a party that may treat the same accommodation as discretionary when asked to compensate it and as owed when it is withheld takes advantage through the ambiguity without changing any term" (CLAIM-tmpro73c, Proposed, interpretive; ChatGPT's, A30 §10). The cost it names is the cost of contesting an interpretation, which the claim maps to CLAIM-731. The ambiguity does not move the work of the accommodation, which the employee did all along. It moves whether that work is paid. So it is not work transferred in CLAIM-760's sense. The first draft read it so (J3.4), and the joins reader found that reading a misreading of CLAIM-760 (review of 2026-11-24, Part B).

Article 9 takes up whether any of these transfers is exploitation or domination. On the record's terms, that needs a declared standard (CLAIM-760, "The stronger reading"). This article only counts.

---

## 3.5 Timescale separation and readiness

### 3.5.1 Governance as allocation over time

"Organizational governance is partly the intertemporal allocation of scarce resources among inquiry, response and the upkeep of the structures that make both possible, slow organizational modes arise partly as ways of amortizing inquiry and coordination costs, and adaptive governance must keep the capacity to reallocate between answering existing questions and learning to ask and answer new ones" (CLAIM-1060, Proposed, interpretive; ChatGPT's, A52 §5). The claim's summary says its mechanism is already held, by CLAIM-475 and CLAIM-761. Its step to slow modes is ARG-238 (Proposed), "which CLAIM-755 narrows to the economic sense of slow". By §3.1.3, "slow" here means costly to form and cheap to use. It does not mean slow to relax.

### 3.5.2 Rarely exercised capabilities

Readiness is where the three requirements of §3.2.1 part most visibly, and the record has run the studies. The assistant's result from LEAD-036's study (CASE-343, Active, executed study) is:

> "Where competence decays without funded maintenance and a capability is committed only when competent enough, a budget that follows observed use has a state in which the capability is never used or funded again whenever the base budget alone sustains competence below that level … so at the same expected funding the chance of loss within a given time has a lower bound that rises as occasions grow rarer and does not depend on the payment per use, while maintenance funded apart from use, at a level that sustains the threshold, has no such state" (CLAIM-921, Active, demonstrated).

In the study, at the same expected funding, "the coupled rule lost the capability within thirty years in every run at one occasion in two and a half years and in 39 % at four a year, and the decoupled rule never did" (CLAIM-921). The result is demonstrated within the model, under its stated conditions ("whenever the base budget alone sustains competence below that level"). It is not an observation of any organization. Its title was narrowed to the lower bound on 2026-11-24 (version 4). CASE-343 was rerun on 2026-11-24 by a session other than the filer's and reproduced.

Two other executed studies show the same loss under a peak rule. "a heavy rescue squad whose budget is set to the last month's peak is lost for good in every run within months where it is sent only on confirmation … and never where it drills each month or the unspent budget rolls over" (CASE-315, Active, executed study; rerun 2026-11-24). And in "A matched-performance model of regulation run under six budget regimes … every regime produces the same output until a contingency arrives, while readiness at a deadline of six periods ranges from 0.147 to 0.894" (CASE-412, Active, executed study). The record already holds the readiness study the draft's programme would call for.

A capability lost this way is regained at its construction cost, not its upkeep: this is CLAIM-569's X, cheap to keep and costly to build. CLAIM-569 already says so in its own words: "That it is costly to rebuild is one reason to keep it; whether the reason is good depends on what it is for" (CLAIM-569, "What it does not say", pointing to QUESTION-395). This is a restatement (J3.8). The readiness account declines a broader form of it, "The three requirements of a form, each lost by its own mechanism", as "a conjunction" (SYNTHESIS-031, "Not stated on the record"). A reading on the record gives the same shape for knowledge: because absorptive capacity accumulates, "a firm that stops investing in a fast-moving field may be locked out of it even after major advances" (THEORY-1518, Active; Cohen and Levinthal, who "test only the static part").

### 3.5.3 Slack and the opportunity cost of the present

Reconfiguration slack is "the temporary resources a system needs to move between two configurations it can each hold, beyond what holding either one requires, while keeping specified commitments" (TERM-106, Active). Two demonstrated results say what immediate demands do to it.

- **Cutting toward holding.** "cutting the resource an organization holds toward what holding its present configuration requires leaves that configuration feasible and removes exactly the transitions whose threshold lies between the old holding and the new" (CLAIM-679, Active, demonstrated; ChatGPT's sentence, A20 §IV of "Analyze technological civilization trap": "A society can become more efficient at reproducing its current organization while becoming less capable of transforming that organization").
- **The ratchet.** "A budget set each period to the peak resource spent the period before never rises", so any transition costlier than holding "is lost after one period spent holding it, unless the budget is raised from outside by at least the difference" (CLAIM-577, Active, demonstrated; the assistant's). The claim's own limit: "real budget rules have floors, growth and discretion that weaken it".

How much slack there is does not settle whether it helps: "A reserve is described by where in a configuration space it can be applied, not only by how much there is" (CLAIM-579, Active, interpretive). The executed studies run the ratchet. In CASE-412, "a redesigned route is lost under the peak rule unless a reserve is also held, a drill each period holds the budget as a reserve does". In CASE-397 (Active, executed study), "under the peak rule a review that needs capacity can never start; and a reserve of 2 reaches the harm-free configuration while a redesign that let the reserve fall to 1 does not".

The companion manuscript `governance-of-possibility` develops these results at length (its §§9–11). This article uses them only to say that the cost of the present can be paid in future reach, and that no output measure records the payment.

---

## 3.6 Reachability and transition asymmetry

### 3.6.1 The threshold is a peak along a path

"For a fixed architecture and one resource that must be held at each moment, the resource threshold for reaching a target configuration need not equal the resource requirement of the target: it is the least, over admissible transition paths, of the peak requirement along the path, and it is infinite when no admissible path joins the two" (CLAIM-571, Active, demonstrated). Formally, B*(A, B) = inf over γ ∈ Γ(A, B) of max_t r(γ(t)). ChatGPT's example is r(q) = 0.7 + 2.4q(1 − q) on [0, 1]. Both endpoints cost 0.7 to hold, and every path between them passes q = ½, where r = 1.3. At a budget of 1.0, each endpoint is feasible and neither is reachable from the other. The gap of 0.6 is the transition's reconfiguration slack (CLAIM-571; TERM-106).

The claim's scope is "one resource that must be held at each moment". For a cumulative expenditure, "a path costs its integral, not its peak" (CLAIM-571, "What it does not say"). The two come apart completely: "two systems can have the same threshold between every pair of configurations … while the least cumulative cost of a transition differs between them by any factor" (CLAIM-646, Proposed, demonstrated; ChatGPT's proposal). The six resource types "bound different functions of a path and are not one budget" (TERM-105, Active).

### 3.6.2 Feasible, reachable, reliably reached; going and coming back

Two further results separate the geometry.

- **Three properties.** "That a target configuration is feasible, that it is reachable from the start under the admissible transformations, and that the process reliably reaches it are three properties, each implied by the next and none implying it" (CLAIM-567, Active, demonstrated; not a member).
- **Direction.** Connectivity "does not settle reachability among them: under directed moves a state can share a connected component with a target and have no admissible path to it, and the least budget for going from one configuration to another can differ from that for coming back" (CLAIM-591, Active, demonstrated; not a member). In the filer's construction, with r = 1, 1, 3 on u, v, w and moves u → v, v → w, w → u, "The least budget from u to v is 1; from v back to u it is 3, through w" (CLAIM-591). The claim says "can differ". It does not say that they usually do.

The record holds one organizational case in which entering is cheaper than leaving: "Recruiting an emergency regime, maintaining it and dissolving it are separable capacities, and an organization that can enter exceptional authority more cheaply than it can leave it has an asymmetric transition structure in which the regime can outlast its justification" (CLAIM-tmp0gs0t, Proposed, interpretive; ChatGPT's, A34 §6 and A36 §15, with a gap fill that "shows the asymmetry in the text of the National Emergencies Act since 1985"). It cites neither CLAIM-591 nor CLAIM-569, and its cost of leaving is argued, not priced.

The motivating draft's sentence "the affordability of an organizational state does not establish the affordability of reaching it" restates CLAIM-569's title, "having enough to sustain it is not having enough to acquire it", and CLAIM-571 (J3.6, a restatement).

### 3.6.3 Contractual lock-in without preference

ChatGPT applied the threshold to contracts at A30 §8. Replacing a critical service provider can require keeping two providers at once, rebuilding internal expertise and moving data, so "The new contract would be cheaper to maintain, but the organization cannot afford the transition. This produces contractual lock-in without requiring any preference for the existing arrangement" (CLAIM-571, note of 2026-11-24: "An application that supports the claim's reading; no change"). That is a peak threshold. Two providers held at once are the peak along the path. The same passage adds that "renegotiation readiness might itself need to be maintained as an organizational capacity", which ties this section back to §3.5.

A30 §8 also says: "A relationship may be easy to enter, inexpensive to maintain and extremely expensive to leave" (in CLAIM-tmpsf9hp). The record reads this passage two ways, and it does not define a directed revision cost.

- **As TERM-116's profiles.** TERM-116 (Proposed) defines the incoming profile, "the cost of producing it from each other configuration", and the outgoing profile, "the cost of turning it into each", with the reason for keeping both: "a system may be easy to assemble but hard to change once assembled". Its note of 2026-11-24 says that "A30 §8 applies the incoming and outgoing profiles to contracts", and that A30's party index "is an extension the term does not carry". TERM-116 is not additive by definition. It says that "Under additive costs either profile recovers d".
- **As a peak threshold**, by CLAIM-571's note above.
- **No revision cost is defined.** CLAIM-569's note, as corrected on 2026-11-24, reads: "A30 §8 asks for the revision cost to be directed (corrected 2026-11-24: TERM-116 defines relational profiles, not a revision cost, and no entry defines R(C → C′))". CLAIM-tmpsf9hp says the same: "The record defines none: TERM-116 defines relational profiles, not R". Both corrections were made on this draft's finding (see Limits).

What is open is which cost a contract's exit is: a profile of costs, which under additive costs is a cumulative quantity, or a peak along a path. CLAIM-646 shows that the two can differ by any factor, and which applies depends on which resource binds (TERM-105). No entry fixes that for contracts. That entry is cheap and exit dear then follows from CLAIM-591's "can differ" and adds nothing to it. The first draft joined these differently (J3.5), and the joins reader found that join failed (closing section).

The record holds other routes by which an arrangement is kept that need no budget shortfall and no preference for it. They are cited here as neighbours, not joined to the threshold.

- **Option value and erosion.** With uncertainty about an alternative's costs and an irreversible transition cost, "waiting to learn" has "an option value, so transforming can beat preserving in expectation while waiting beats both; when the status quo irreversibly erodes the capacity to transform, the ranking can reverse, so symmetric scrutiny requires pricing irreversibility on both sides" (CLAIM-tmp8mpgs, Active, demonstrated; the assistant's gap fill under ADR-137, made Active at the assistant's discretion as the Limits say). Its numbers are "illustrative" (150, 120, 111.5 and 126.5, reproduced by its checker).
- **Increasing returns.** In Arthur's model, increasing returns make adoption "a random walk with absorbing barriers", and "once it has locked in no small change in returns alters later choices" (THEORY-863, Active, a reading of one model).
- **Practical compulsion.** "A technology can become practically compulsory without any rule requiring it" (CLAIM-677, Proposed, interpretive; ChatGPT's).
- **Reliance on restraint.** Institutions can "stop maintaining alternatives" to another's "historically reliable restraint", so "the risk lies less in the departure than in the alternatives the encompassing organization no longer keeps" (CLAIM-tmpzas6q, Proposed, interpretive; ChatGPT's, A36).

---

## 3.7 Authority-sensitive cost landscapes

### 3.7.1 Four predicates, held in three places

ChatGPT set four predicates on a transformation apart, "Physically feasible", "Affordable", "Authorized" and "Normatively permissible", which "need not coincide" (A30 §11, in CLAIM-tmpdu9v6). The record holds each of them, but in different places:

| Predicate | Where the record holds it | Standing |
|---|---|---|
| physically feasible | the architecture's admissible processes P_z(q, q′) (TERM-114) | Active |
| affordable | resource-bounded reachability, q ⇝_b q′ ⟺ ∃p ∈ P_z(q, q′) : κ(p) ⪯ b (TERM-114) | Active |
| authorized | Θ, "whose changes of architecture are authorized, as distinct from which are feasible and at what cost": a note on TERM-114 of 2026-11-17, and not in its definition. "whether to add Θ is the owner's call" | a note on an Active term |
| permissible | Perm_N(p), "its permissibility under a declared normative standard" (CLAIM-tmpdu9v6) | Proposed |

The record's list of how a transition fails covers the first two predicates only: "a feasible path exceeds a resource ceiling, no path exists in the fixed configuration space, a path exists that no available input can execute, or a path exists that cannot be reliably followed" (CLAIM-568, Active, interpretive). No single object holds the four predicates together. The motivating draft's formal centre, R_i(S; B, H, W) = {S′ : S′ is reachable by i under B, H, W}, is named in the draft and defined nowhere. The record holds it as LEAD-tmpeo8wq (Open, stage idea), whose list of what the record holds is the table above (J3.9, a restatement of LEAD-tmpeo8wq, "The gap"). The lead's statement that "No entry defines reach per actor" overstates the gap, as its note of 2026-11-24 says (§3.7.4).

### 3.7.2 An obligation is a bar, not a price

"A genuine obligation enters a cost model of exit as a condition on which transitions are permissible, not as a cost: withdrawal can be feasible and affordable yet impermissible until alternatives are arranged or the duty is transferred, so a party who controls the circumstances that keep the restriction in place controls the other's exit without raising its price" (CLAIM-tmpdu9v6, Proposed, interpretive; ChatGPT's, A32 §13). ChatGPT puts it plainly: "The last should not simply be converted into a subjective penalty in a utility function."

The claim agrees with a held result. A normatively permitted path set Γ_N ⊆ Γ gives "b*_N ≥ b*", so a normative restriction on the path "can raise this claim's threshold and never lower it, as CLAIM-582 says of any added hard constraint" (CLAIM-571, note of 2026-11-17; the step is the assistant's, and ChatGPT does not state it).

The control over circumstances in its last clause has a held neighbour, which the claim itself cites. "One party can wrongfully bring about circumstances in which another incurs a genuine obligation, so that the second does right in discharging it and is still wronged" (CLAIM-703, Active, interpretive; ChatGPT's, A13 of "Assess Depp Heard Abuse", ruled Active at a delegated status review). CLAIM-tmpdu9v6 says that CLAIM-703 and CLAIM-713 "say a party can wrongfully bring about, or exploit, the circumstances that activate an obligation; this claim says where that control sits in a cost model".

The claim also has limits. It "does not answer QUESTION-472's second half", which asks what separates such control "from ordinary reliance on someone's conscientiousness" (QUESTION-472, Open; ChatGPT's, A30 §4 of "Assess Depp Heard Abuse", at the owner's U15). "Nor does it say that every obligation is a bar rather than a weight: defeasible obligations would need rules of priority" (CLAIM-tmpdu9v6). Neither it nor CLAIM-571's note supplies such rules. The record's nearest attempt at the second half is CLAIM-713 (Proposed, interpretive; ChatGPT's). Its defeat condition names "the four conditions A15 §8 names (imposed rather than accepted obligations, disproportionate burden, accountability without control, exit made to look like harming innocents)". The account that holds these entries, SYNTHESIS-099 (Proposed), keeps QUESTION-472 Open. It gives Keller's reading (THEORY-1917) as "evidence toward yes for fiduciaries, whose moral cost of striking does the work of a barrier to exit". The second half stays open, and this article does not close it.

### 3.7.3 Authorization: a predicate and a cost

CLAIM-1016 (§3.1.4) prices authorization as "a third cost on the shared budget" of inquiry, beside formulating and answering. Its antecedent holds that "Permission to pursue an inquiry is a second-order query, formulated by the proponent and evaluated by the authority within their own budgets" (CLAIM-996, Proposed, interpretive; ChatGPT's, A56 §§2–3 of "Explain First Contact RL", developing the owner's U29). The Θ of TERM-114's note treats authorization as a predicate instead. The lead combines the two readings: a transition is authorized when "i holding or able to obtain the grant W requires" (LEAD-tmpeo8wq, step 2), and the lead cites CLAIM-1016 among what the record holds. Reading authorization as both predicate and cost is therefore the lead's restatement and not this article's (J3.12). The record has not filed whether obtaining a grant is itself a costed transition.

### 3.7.4 Collective reach and independent reach

The draft asks "when recurrent successful coordination expands collective reach while contracting the independent reach of particular participants" (A49, Article 3). The record holds more of this than the first draft said.

- **In prose,** the mechanism: "A capability lost because another reliably supplies it is the Black Queen's loss" (CLAIM-603, Proposed, interpretive; the assistant's, on the owner's remark of 2026-11-05 that "assured help makes recipients lose skill" sounds "closely related to niche differentiation and specialization phenomena"). An arrangement "can produce the dependence through which it exploits" (CLAIM-670, Proposed, interpretive; ChatGPT's).
- **In reach, for one party, demonstrated.** "where capacity is learned by doing and decays with disuse, support that does the work shrinks what the party can reach unaided while support that covers only its shortfall does not, so support, or a technology, cannot be ranked by present capability sets" (CLAIM-675, Active, demonstrated). And "what decides dependence is the order in which supply and capacity are used, not the amount of supply" (CLAIM-602, Active, demonstrated). LEAD-tmpeo8wq's note of 2026-11-24 reads these as "step 3's construction for solo reach under supply, with its negative control (shortfall support), already demonstrated". The model is a scalar capacity, not a set of reachable states over TERM-114.
- **In values,** the bargaining shape. ChatGPT's model at A24 §4 has specialization raise joint production (10 + 16s) while it lowers B's independent capacity, 5(1 − s(1 − p)), where p is the protection of B's fallback. At full specialization and no protection, "the split is 14.75 to 11.25 in A's favour; with full protection, 12.25 to 13.75" (CLAIM-tmp2jhc1, Proposed, interpretive). The bargaining step that turns a fallback into terms is the assistant's: under the equal-weight Nash solution, u_B = (V − o_A + o_B)/2, so each unit of B's outside option moves half a unit of the split "whether or not B ever takes the outside option" (ibid., checked). ChatGPT's own caption limits the model: "Maintaining fallback capacity is not priced in this model, so it cannot establish an optimal degree of protection" (ibid.). The lead cites CLAIM-tmp2jhc1 only for its threat point. That the A24 §4 model already has the lead's shape in values is a pointer for a dated note on the lead, not a claim (J3.10, closing section).

**So the study is done in part.** "Collective reach grows while independent reach shrinks" is not new, and for one party's unaided reach it is demonstrated. The lead's note narrows what stays open: "the authority index W, the four predicates per transition, and whether solo reach's shrinkage, not a price, moves the terms the other can offer (CLAIM-tmp2jhc1)". This article states nothing further about it. **The expectation, before any result,** for that remainder is the lead's own null: "If R_i cannot shrink without some transition's price changing, the dependence is already priced by TERM-116's profiles, and the index adds notation only" (LEAD-tmpeo8wq). Whether CLAIM-675's shrinkage, a decline in the party's own capacity, counts as "no change in any single transition's cost" in the lead's sense is not settled by the note. It is for the lead to state.

CLAIM-tmp2jhc1 adds one more thing that bears on §3.5. A constitutional reserve "can matter without being used", and "efficiency measured on use will tend to remove it" (CLAIM-tmp2jhc1). The first draft read that removal as CLAIM-921's use-coupled loss (J3.7). The joins reader found the reading adds nothing to CLAIM-tmp2jhc1's own sentence. A reserve that is never exercised is CLAIM-921's limiting case, with no occasions, so its feedback loop is idle, and the reserve is simply funded at its base from the start. It keeps its threat value only if the base alone sustains credible competence. And CLAIM-921 excludes models where "use outside commitment counts as activity", which a reserve's effect on bargaining may be. The article does not assert the join.

---

## 3.8 Neighbouring theories

The motivating draft asks for a comparison "against transaction-cost economics, incomplete-contract theory, dynamic optimization and existing resource-bounded planning frameworks". The record holds little of this:

- **Incomplete contracts.** The record holds readings of Grossman and Hart and of Hart (LIT-2745, LIT-2776, both Active), read as "the right to decide what the contract leaves out, the residual control right, belongs to the owner of the relevant non-human assets" (THEORY-1979, Proposed). Behind them is CLAIM-728 (Proposed, interpretive; not a member): "a relationship fair in every specified term can still leave one party's terms at the other's discretion". CLAIM-tmpro73c sets itself apart from CLAIM-728: "This claim is different in kind: no contingency is uncovered; which arrangement covers the act is left open, and one party decides it case by case and inconsistently" (CLAIM-tmpro73c; Article 2, §2.7).
- **Institutions and path dependence.** North's essay (LIT-489) is read as saying that institutions "with technology … fix the costs of transacting" and that "increasing returns to the institutional matrix make frameworks path dependent" (THEORY-429, Proposed). Arthur's lock-in model (THEORY-863, Active) and Pierson's claim that "Politics is more prone than markets to increasing returns, and so to path dependence" (THEORY-885, Proposed) are held beside it (§3.6.3).
- **Absorptive capacity.** Cohen and Levinthal's lock-out of a firm that stops investing (THEORY-1518, Active; §3.5.2) is the record's one reading of the cost of rebuilding a capability.
- **Physical database design.** QUESTION-114's neighbour is held: index selection "is NP-hard", and the tools "choose … by searching configurations costed with the query optimizer's own estimates", with "no term for the one-time cost of building" (THEORY-345, Active). That last clause sets it apart from CASE-326, whose F is exactly that term.
- **Not found.** A search of the record found no reading of Williamson or Coase, and none of dynamic optimization or resource-bounded planning as frameworks to compare with.

The comparison the draft asks for is not on the record, and this article does not supply it from memory. Its reading is LEAD-tmple60r (Open, stage idea, priority low; G3.3).

---

## 3.9 What this article can rest on

| Step | Entries | Standing |
|---|---|---|
| A stabilized constraint can be stored work that moves a task under a per-task budget | CLAIM-761 (the owner's thesis, in ChatGPT's wording), CLAIM-303, CLAIM-475 (the owner's thesis; its stored-inquiry clause A17–A18's), CLAIM-443 (from the owner's question; its limit from the working-through) | Active, interpretive; each ruled Active at a delegated status review |
| An added restriction enlarges nothing at fixed dynamics | CLAIM-582 | Active, demonstrated |
| Construction, upkeep and transition are separate requirements | CLAIM-569 | Active, demonstrated |
| The threshold is a least peak and can be infinite; going and coming back can differ; feasible, reachable and reliably reached are three properties | CLAIM-571, CLAIM-591, CLAIM-567 | Active, demonstrated |
| Slack is lost by cutting toward holding, or by a peak ratchet | CLAIM-679, CLAIM-577, TERM-106; run in CASE-412, CASE-397, CASE-315 | Active, demonstrated; the cases Active, executed |
| Saved, transferred and expanded are three achievements | CLAIM-760 | Active, interpretive |
| One model prices three named cases with the same terms; erosion weighs by fallback | CASE-326, CLAIM-891, CLAIM-892 | CASE-326 and CLAIM-892 Active, CLAIM-891 Proposed; values illustrative; case results reported without prior expectations |
| Support that does the work shrinks unaided reach | CLAIM-675, CLAIM-602 | Active, demonstrated |
| A contract's invocation can change it, and the model does not price that | CLAIM-tmpsf9hp, ARG-tmpa5ped, CLAIM-tmp80ny9 | Proposed; LEAD-tmp14n26 not run, done in part; ChatGPT expects richer state to cover most cases |
| Use-following budgets lose rare capabilities | CLAIM-921, CASE-343 | Active, demonstrated in its model (a lower bound) |
| Obligation is a bar on transitions, not a cost | CLAIM-tmpdu9v6 | Proposed, interpretive |
| An unused fallback moves terms | CLAIM-tmp2jhc1 | Proposed, interpretive (derivation checked) |
| Reach indexed by authority, and the four predicates in one object | LEAD-tmpeo8wq | Open lead, stage idea; narrowed by its note |

The demonstrated core is Active. It is formal, and it is about configurations with holding requirements that no organization has been measured to have. The thesis that connects it to organization is the owner's, and it is interpretive. It was ruled Active on 2026-11-20 at a status review whose rulings the owner delegated, after the owner endorsed it at U17. Everything this article adds about contracts, actors and authority is Proposed or an unrun lead. Article 2 says what a contract is, and this article says what one costs. Why a contract is hard to modify, the motivating draft's "Connection", rests on the Active results of §3.6, applied to contracts by a dated note, with the choice between a peak and a cumulative cost left open (§3.6.3).

---

## Joins: the verdicts

The first draft closed with twelve joins. An independent reader tested each under ADR-075 (review of 2026-11-24, Part B), and SYNTHESIS-tmp4tvbr, section "The joins of the manuscript governance-of-becoming, Part I", places them. None of Article 3's joins passed, and none is filed as a claim.

**Restatements** (eight). Each cites the entry that states it, and adds nothing to place.

- **J3.1** Stored work moves a task under a per-task ceiling because a threshold is a peak, not a total (§3.1.2). CLAIM-761's body: "That is CLAIM-571's point that a threshold is a peak, not a total".
- **J3.2** A contract's lifecycle is CLAIM-569's three requirements and CASE-326's terms (§3.3.2). CLAIM-569's note of 2026-11-24, CLAIM-475's note of 2026-11-24, ARG-tmpa5ped.
- **J3.3** The motivating draft's seven expenditures mapped to the model's terms (§3.2.3). CASE-326, and ARG-tmpa5ped for contracts. The clause "independently variable" is not offered, since the record shows independence for two pairs only (CLAIM-569, CLAIM-571).
- **J3.6** A state's affordability does not establish that reaching it is affordable (§3.6.2). CLAIM-569's title, CLAIM-571.
- **J3.8** A capability lost to decay is regained at its construction cost (§3.5.2). CLAIM-569, "What it does not say", with CASE-210. It is consistent with CLAIM-921's model. SYNTHESIS-031 declines the broader form.
- **J3.9** The four predicates and where each is held (§3.7.1). LEAD-tmpeo8wq, "The gap", with TERM-114's note.
- **J3.11** CLAIM-358's accommodation as stored work (§3.1.4). QUESTION-095's note (A39 §2). That it is not stored work in CLAIM-761's sense is a reading note, not a claim.
- **J3.12** Authorization as both a predicate and a cost (§3.7.3). LEAD-tmpeo8wq, "The gap" and step 2.

**Failed** (four). The text no longer asserts any of them.

- **J3.4** An ambiguity's resolution cost read as work transferred. Stated two ways in the first draft. One restated the CLAIM-731 route that CLAIM-tmpro73c and CLAIM-760 both cite. The other misread CLAIM-760, since the ambiguity moves who is paid, not who works. §3.4.3 now says so.
- **J3.5** Contract exit read as CLAIM-591's directed thresholds. Its peak half is CLAIM-571's note of 2026-11-24, and its directed half is a trivial instance of CLAIM-591's "can differ". The draft also misstated TERM-116 as additive distances. §3.6.3 now states the open item, a peak or a cumulative cost for a contract's exit (CLAIM-646, TERM-105). That item is filed as a dated note on TERM-116 (2026-11-24).
- **J3.7** A constitutional reserve lost by CLAIM-921's use-coupled funding. It is trivial, and it restates CLAIM-tmp2jhc1's "efficiency measured on use will tend to remove it". The draft's reason for it was partly off. §3.7.4 now gives the reader's reason.
- **J3.10** The lead's shape is already in CLAIM-tmp2jhc1's A24 §4 model. The observation is accurate, but it fails as a claim because there is no route to one. It is filed as a dated note on LEAD-tmpeo8wq, its second of 2026-11-24 (§3.7.4).

## Gaps

- **G3.1** No account maps the stored-work cost model as it now stands. SYNTHESIS-106 (Proposed, 2026-11-19) predates CASE-326, CLAIM-891, CLAIM-892 and the contract entries, and it gives CLAIM-761 and CLAIM-760 as Proposed though both are Active. SYNTHESIS-tmp4tvbr names CASE-326 only as what ARG-tmpa5ped applies. A revision of SYNTHESIS-106 is needed, on the synthesis-review skill's stage 4. SYNTHESIS-106's note of 2026-11-24 records the gap.
- **G3.2** Work deferred, moved to a later time and possibly larger when paid, is not among CLAIM-760's movements of work. It is held as QUESTION-tmpzhnqy (Open; the assistant's wording). The question asks for a construction in CASE-326 in which deferring a task raises its later cost, against one in which the task is handed to another party at unchanged cost. That is *done in part*. CLAIM-tmp8mpgs (Active, demonstrated) already has a delay that raises a later transition cost from 40 to 70, though not in CASE-326's terms and not framed as a movement of work (§3.4.2). The question's note of 2026-11-24 says so.
- **G3.3** The comparison with transaction-cost economics, dynamic optimization and resource-bounded planning that the motivating draft asks for has no readings of Coase, Williamson or the planning literature behind it. It is held as LEAD-tmple60r (Open, stage idea, priority low). The record's readings of path dependence and lock-out (THEORY-863, THEORY-885, THEORY-1518, THEORY-429) cover part of the ground the lead's summary does not name (§3.8).
