<!-- scratch/manuscripts/governance-of-possibility/05-model.md -->

## 9. A model of matched performance and divergent readiness

Sections 6 and 8 said that two organizations can look the same in ordinary operation and differ in what they can still become. This section makes that claim concrete in a small model and runs it. The motivating draft (ChatGPT's article) set out three regimes and stated their outcomes in a table, as "analytical outcomes under stipulated assumptions". Here the table is replaced by an executed study, in `analysis/` beside this draft. It has a model, a sweep, 21 tests with a negative control, and outputs dated 2026-11-23. Every number below comes from `analysis/results.md` or `analysis/results.json` from that run. The tests were rerun on that date and pass.

Three limits come first. The model is the drafting assistant's (Claude's), built on the record's entries and on an earlier simulator. All of its rates and costs are invented. And it is a model, so what it shows is what follows from its assumptions, not what happens in any industry (§9.9).

### 9.1 Where the model comes from

**The mechanism it runs is held.** The motivating draft's first regime is the record's CLAIM-577 (Active, demonstrated), which the record labels as the assistant's own proposition: "A budget set each period to the peak resource spent the period before never rises, so the configurations an organization can reach shrink monotonically, and any transition whose threshold exceeds the cost of holding the current configuration is lost after one period spent holding it, unless the budget is raised from outside by at least the difference". The threshold of a transition is CLAIM-571's (Active, demonstrated): "the least, over admissible transition paths, of the peak requirement along the path, and it is infinite when no admissible path joins the two". The claim's own scope matters for everything below: it holds "For a fixed architecture and one resource that must be held at each moment".

**An earlier simulator ran part of it.** LEAD-080 (Open) asked for a readiness simulator to be run under the peak rule and under carry-over. CASE-315 (Proposed) is that run. It modelled a heavy rescue squad, holding at 0.7 and 1.3 with the squad out, over 300 runs of ten years. Its title gives the result: the squad "is lost for good in every run within months where it is sent only on confirmation, in a fifth of runs within nine years where it is sent provisionally to each of six reports a month, and never where it drills each month or the unspent budget rolls over". Its caveat: "The model is the assistant's and its rates are invented." From that run the record took CLAIM-878 (Proposed, demonstrated, the assistant's): under the peak rule "a capability stays funded exactly as long as every period contains a mobilization at its cost, whether a use, a drill, a false alarm or a cancelled dispatch".

**The record already had an instance of redesign.** The motivating draft's third regime, a cheaper staging path, has a precedent the draft does not cite. CASE-198 (Proposed) is "An architecture-mediated transition: moving between two configurations by first switching to a staging architecture under which the path is cheaper, moving, then switching back, lowers the peak resource need from 1.3 to 1.0". In its numbers the reconfiguration slack falls "from 0.6 to 0.3", not to zero, so the staged route still needs a reserve. Its executed study, CASE-345 (Proposed), adds that "the budget saved is bought with time, and at a deadline of 2 the route is no remedy". CLAIM-922 (Proposed, demonstrated) generalizes this: "a deadline shorter than every route through the staging architecture takes that remedy away". The present study finds the same thing in its own numbers (§9.5).

**The disputed step.** ChatGPT's draft set reserve and redesign side by side as "different means". The record files that as ChatGPT's CLAIM-tmpf71gk (Proposed, interpretive): "Maintaining a reserve and redesigning a transition are distinct routes to readiness: one keeps enough capacity to cross an existing transition barrier, the other lowers the barrier itself". The assistant objected in CLAIM-tmpg8yl2 (Proposed, demonstrated, counter): "Under a budget set each period to the last period's peak use, a redesigned transition is lost like the original unless its threshold is at most the cost of holding the present configuration, so redesign lowers the reserve a transition needs by the fall in its threshold and replaces the reserve only where it leaves no reconfiguration slack". The draft's table gives the redesigned regime an "accessible transition capacity" of 2. CLAIM-tmpg8yl2 points out that this capacity "is a budget held at 2: a reserve of 2 − r(A) = 1", one unit above the holding cost that the text never states. It concludes: "Otherwise reserve and redesign are complements, not alternatives." CLAIM-tmpf71gk's own Standing section concedes the point: "the two are distinct in what they change but not alternatives". Both entries are Proposed, and choosing between them is the owner's call.

**The lead this study answers.** The draft's §9.6 proposed a computational study and gave no design for it. The assistant filed the design as LEAD-tmpnblsf (Open, stage idea): "Extend the readiness simulator with a redesign arm, a sweep of reserve sizes between holding cost and threshold, and a harm absent from the demand specification introduced mid-run". It asks for three things to be reported: "readiness curves over the deadline (TERM-115), reserve cost, and which regime ranks first at which deadlines". The study reuses CASE-315's budget accounting, its drill, its partial-rollover and CASE-200 rules, and its way of seeding runs, without changing that study's code. Putting CLAIM-571's paths, CLAIM-577's rule, CASE-200's carry-over, CLAIM-878's drill and CLAIM-tmpg8yl2's reserve into one model is this study's own work. The record keeps them as separate entries (join JC1: one model from five entries).

### 9.2 The model

**Configurations and paths.**

- Two production configurations, A and B, each cost r = 1 a period to hold.
- The original path runs A → M → B over two edges, with r(M) = 3, as in the draft.
- The redesigned architecture adds a staged path A → S1 → S2 → B over three edges, with r(S) = θ′. The reference value is θ′ = 2.
- Each edge is completed with chance q = 0.5 a period. While it is being crossed it occupies the larger r of its two ends.
- A path's threshold is its peak, and an architecture's threshold is the least over its paths (CLAIM-571).
- The graph is symmetric, so the same paths lead back.

Choosing a slower staged route, three edges to the original's two, is a stated assumption that the study does not vary (§9.9).

**Budget rules.** B is the period's capacity ceiling and s is the period's peak use.

- *Peak*: B′ = s (CLAIM-577).
- *Floor*: B′ = max(s, F), a held reserve of F − 1. In the control arms the commitment can lapse, with a hazard per period, and the rule then becomes the peak rule.
- *Carry*: B′ = min(3, B̄ + ρ(B − s)) with B̄ = 1.5 and ρ = 1. This is CASE-200's rule (Proposed), with a cap added. CASE-200's title states that rule's effect: "rolling over the 0.3 left unspent reaches it, while a rule that cuts or expires unspent funds forecloses it".
- *Drill*: under the peak rule, when nothing else is under way, the staging configuration is occupied at θ′ for part of the period, so that period's peak use is θ′. This is CLAIM-878's mobilization, done on purpose, and the "third mechanism" that CLAIM-tmpg8yl2 names under "What it does not say": "a drill each period at the transition's peak, keeps the route funded by the rule itself".

**Contingency, outside money, deadline.**

- Each period, with chance p, demand switches to the other configuration.
- The organization takes the fastest path it can afford.
- If no path is affordable, outside money arrives after a geometric wait, with chance g = 0.1 a period. It raises the budget to the least threshold, which is the minimum CLAIM-577's step 4 says is needed ("Only outside money restores it").
- A transition, once started, is funded to the end.
- A response later than the deadline τ costs L.
- A reserve costs c per unit of budget above holding, per period. The upfront cost of a redesign is not charged; it is reported as a break-even.
- Output is 1 in any period with no contingency pending, and 0 otherwise.

**Readiness.** Readiness is TERM-115's (Active), "the probability that an organization operating under a specified policy can deliver an effective response to a specified contingency within its deadline". It is measured under an imposed contingency, do(c), after 50 quiet periods. TERM-115 says why: "The do(c) is the point: this is readiness for a specified situation, imposed, not success conditional on the situations that happened to be observed." As in §6, R(t) is the chance of having reached B within t periods.

**Regimes and controls.**

| Regime | Path | Budget rule | What it stands for |
|---|---|---|---|
| I | original | peak | the draft's utilization-matched regime (CLAIM-577) |
| II | original | floor at 3 | the draft's reserve regime |
| III-a | redesigned | peak | the draft's redesign, read as having no reserve |
| III-b | redesigned | floor at θ′ | the draft's redesign with the reserve CLAIM-tmpg8yl2 says it needs |
| IV | redesigned | peak, with a drill each period at θ′ | CLAIM-878's mobilization as policy |
| V | original | carry | CASE-200's carry-over |

The controls are II and III-b with a reserve that lapses (hazard 0.005 a period), and IV drilling only every second period. The last is the negative control: the model predicts that it fails, and it can.

**The run.** Long runs use 8 seeds of 4,000 periods each. Imposed contingencies use 2,000 replications per regime. All regimes run on one seed see the same contingencies and, where their paths agree, the same step times.

### 9.3 Present output is matched

Before the first contingency, every regime produces 1.0000 per period, and with no contingency at all every regime produces 1 in every period (tested). This equivalence is built in, not found: in the model, output does not depend on the budget except through how quickly a contingency is met. That is exactly the situation the draft's argument needs. Ordinary output cannot tell the regimes apart. CLAIM-577's "What it adds" says the same: "The loss leaves no trace in output."

Once contingencies arrive, the regimes come apart. At the reference values (p = 0.02, θ′ = 2):

| Regime | output overall | capacity above holding | mean response (periods) |
|---|---|---|---|
| I | 0.7868 | 0.171 | 12.76 |
| II | 0.9183 | 2.000 | 4.13 |
| III-a | 0.7578 | 0.117 | 14.83 |
| III-b | 0.8820 | 1.000 | 6.11 |
| IV | 0.8820 | 1.000 | 6.11 |
| V | 0.9158 | 1.941 | 4.25 |
| II with lapse | 0.7924 | 0.241 | 12.47 |
| III-b with lapse | 0.7668 | 0.149 | 14.53 |
| IV, drill every second period | 0.7623 | 0.124 | 14.72 |

This is the draft's central sentence, "Current-performance equivalence does not imply adaptive-capacity equivalence", run as a model. The record already holds it in general form. CLAIM-079 (Active, demonstrated): "Stability does not entail viability: a system can occupy a stable regime while losing access to trajectories that keep satisfying its constraints". CLAIM-414 (Active, demonstrated) shows that matched ordinary trajectories can conceal differences that "a specified intervention exposes".

### 9.4 The exact conditions hold, and what the study adds to the dispute

**CLAIM-577 and CLAIM-tmpg8yl2 hold exactly in the model.** The tests check four things:

- under the peak rule the budget never rises;
- one holding period forecloses every route whose threshold exceeds 1;
- a redesigned route is kept under the peak rule exactly when θ′ ≤ 1, tested for θ′ ∈ {1, 1.25, 1.5, 2, 2.5, 3};
- a floor F keeps a route exactly when F is at least its threshold, tested for F from 1 to 3 in steps of 0.25.

These tests confirm that the model implements the two entries' conditions, and that their consequences follow there. They are a check on the model. They add no warrant to a claim that is already demonstrated.

In the draft's own numbers, its redesigned regime "with accessible transition capacity 2" is III-b, which holds a reserve of 1. Without that reserve the regime is III-a. Its route is lost after one holding period, as the original route is under I, and readiness falls to R(6) = 0.147 against III-b's 0.647. On this point the run sides with CLAIM-tmpg8yl2 against CLAIM-tmpf71gk as worded: within the model, redesign and reserve work together; neither substitutes for the other. One reading of CLAIM-tmpf71gk survives, the one its Standing section already concedes: the two change different things, the barrier and the capacity to cross it. The study takes no side on that reading.

**The study adds two findings that neither entry states.**

*The drill is a reserve by another name, under peak accounting.* Regime IV holds no reserve by commitment, yet its budget sits at θ′, because every period's drill sets that period's peak use. Its capacity cost equals III-b's (1.000 against 1.000), and its readiness curve is identical to III-b's at every deadline (the dominance test reports them "equal"). This follows from CLAIM-878: what the peak rule funds is whatever was mobilized, whatever the purpose. CLAIM-878's own words: "A drill each period holds the budget". So the "third mechanism" of CLAIM-tmpg8yl2's last clause is not a third route to readiness in cost or in effect. It is a way of holding the same reserve (join JC2: the drill as a reserve, from CLAIM-878 and CLAIM-tmpg8yl2; gap GC2).

The drill and the reserve differ in what can break them.

- *A reserve lapses when the commitment ends.* IV needs no commitment from whoever sets the budget, so a lapse does not touch it. Under a lapse hazard of 0.005 a period, II's R(6) falls from 0.894 to 0.752 and III-b's from 0.647 to 0.535.
- *A drill fails when a period is skipped.* Drilling every second period loses the route after the first undrilled period: R(6) = 0.147, the same as III-a. This is the negative control, and it fails as predicted. The novel-demand arm (§9.8) shows a second way the drill breaks: a review that crowds out the drill takes the route with it.

So a reserve depends on a commitment, and a drill depends on a schedule being kept. CLAIM-878 had said the same of its squad: "Monthly drills kept it in every run under either policy".

*Redesign halves the reserve only for the transition it was designed for.* In the draft's numbers redesign halves the reserve, from 2 to 1. CLAIM-tmpg8yl2 says so: "Not that redesign is worthless: it halves the reserve in A48's numbers." But the lower threshold belongs to one path, between A and B. II's reserve of 3 is capacity, and it can be spent on any transition with a threshold up to 3. III-b's reserve of θ′ − 1 = 1 covers only routes up to θ′. When a demand arrives that the specification did not name (§9.8), II can meet it from its reserve, and III-b and IV cannot (join JC5: a redesign is specific to one transition and a reserve is not, from CLAIM-tmpg8yl2 and the novel-demand arm).

### 9.5 Readiness curves, and the ranking by deadline

Readiness R(t) under an imposed contingency, θ′ = 2:

| Regime | t = 2 | t = 3 | t = 4 | t = 6 | t = 8 | t = 12 | t = 20 |
|---|---|---|---|---|---|---|---|
| I | 0.025 | 0.081 | 0.146 | 0.267 | 0.395 | 0.607 | 0.845 |
| II | 0.237 | 0.492 | 0.673 | 0.894 | 0.961 | 0.997 | 1.000 |
| III-a | 0.000 | 0.011 | 0.044 | 0.147 | 0.269 | 0.508 | 0.792 |
| III-b | 0.000 | 0.118 | 0.304 | 0.647 | 0.855 | 0.974 | 1.000 |
| IV | 0.000 | 0.118 | 0.304 | 0.647 | 0.855 | 0.974 | 1.000 |
| V | 0.237 | 0.492 | 0.673 | 0.894 | 0.961 | 0.997 | 1.000 |

Section 6 used a note the assistant added to TERM-115 on 2026-11-23, which the record does not file as a claim. It says two organizations "are ranked the same way at every deadline exactly when one curve lies at or above the other at every time (first-order dominance); where the curves cross, which is more ready is fixed only by the deadline". The study classifies every pair of regimes this way, for t from 0 to 40 with a tolerance of 0.02:

- II and V are equal, and they dominate every other regime.
- II dominates III-b and IV, which are equal to each other.
- III-a is dominated by every other regime, including I.
- I and III-b cross between t = 2 and t = 3. At t = 2, I with outside money (0.025) is ahead of III-b (0), because the staged route cannot finish in fewer than three periods. From t = 3 on, III-b is ahead.

The crossing is CLAIM-922's deadline effect (Proposed, demonstrated) seen in this model: the budget the staged route saves is paid for in time.

The worst result for redesign is III-a, below even I. On these assumptions, redesign without a reserve is worse than no redesign at all. The reason is that the minimum outside money of CLAIM-577's step 4 buys the cheapest route, and with redesign the cheapest route is the slower staged one (gap GC5: this depends on the modeller's choice, and the record does not hold it).

**Ranking by long-run cost.** Cost is c × reserve + L × late rate, at p = 0.02, L = 50 and c = 0.1. The readiness ranking does not change between t = 3 and t = 12, but the cost ranking changes with the deadline:

| τ | cheapest | order |
|---|---|---|
| 2 | I | I < III-a < II < V < III-b < IV |
| 3 | II | II < V < I < III-a < III-b < IV |
| 4 | II | II < V < I < III-b < IV < III-a |
| 6, 8 | II | II < V < III-b < IV < I < III-a |
| 12 | III-b, IV | III-b < IV < V < II < I < III-a |
| 20 | III-b, IV | III-b < IV < I < V < III-a < II |

At τ = 2 nothing is in time, so the cheapest regime is the one that holds nothing. At τ = 12 and τ = 20, III-b and IV cost 0.081 and 0.100 a period less than II, before any redesign cost. Those numbers are the largest per-period amortized redesign cost at which redesign pays. So the draft's open question, whether reserve or redesign is better, has no answer independent of the deadline. This fits the record's no-optimum objection, CLAIM-tmphjm0q (Proposed, interpretive, counter; §14): "There is no optimal regulation until the demand specification, the instruments, the horizon and the trade-offs among demands are declared".

### 9.6 When a reserve pays, and what that does not settle

The draft warns that "we should not simply maximize reserve capacity" and gives no criterion. QUESTION-395 (Open) asks: "Beyond what records kept of each capacity bound, what observations, interventions, or models can distinguish a warranted reserve of specialized capability from wasteful redundancy when ordinary operation seldom exercises it, and how is that evidence weighed against the capability's cost?" A dated note on QUESTION-395 (2026-11-23) names the parameter the draft leaves free: "The missing parameter is the contingency's probability times its loss against the reserve's cost per period". The study computes the break-even.

A reserve (II against I) pays when the contingency's probability times its loss exceeds a threshold:

  p·L > pL* ≈ c·Δcap / ΔR(τ),

where Δcap ≈ 1.83 is the extra capacity the reserve holds and ΔR(τ) is the gain in readiness at the deadline. In the study, pL* is the value at which c times the extra capacity equals L times the reduction in late contingencies per period (join JC3: the break-even, from QUESTION-395's note, TERM-115's curves and CLAIM-577's rule).

| p | τ = 3 | τ = 6 | τ = 12 |
|---|---|---|---|
| 0.005 | 0.579 | 0.363 | 0.625 |
| 0.01 | 0.630 | 0.394 | 0.571 |
| 0.02 | 0.701 | 0.401 | 0.565 |
| 0.05 | 1.15 | 0.502 | 0.689 |

The table is at c = 0.1. pL* is linear in c: at τ = 6 and p = 0.02 it is 0.200 at c = 0.05 and 0.802 at c = 0.2. The set of p·L at which the reserve is preferred is closed upward (tested). Three features matter.

- **pL* is not a function of p·L and c alone.** It is U-shaped in the deadline. It is lowest where the deadline falls between the reserve's transit time and the wait for outside money. There the reserve makes the most difference: at a short deadline nothing is in time, and at a long one outside money arrives anyway.
- **It also moves with p, through the rule itself.** Under the peak rule, a transition just made leaves the budget at the transition's peak for one period. So frequent contingencies keep I readier in operation than it is under do(c). This is CLAIM-878's mechanism: a use is a mobilization. As a result, pL* rises with p at τ = 3 and τ = 6. At τ = 12 it does not move monotonically (0.625, 0.571, 0.565, 0.689).
- **The formula is an approximation.** The formula with imposed readiness gives 0.27 to 0.31 at τ = 6, where the long runs give 0.36 to 0.50, and 0.41 to 0.48 at τ = 3, where the long runs give 0.58 to 1.15. The difference is the gap between readiness under do(c) and readiness observed in operation.

**What this does and does not do for QUESTION-395.** It gives a decision rule *if readiness is known*. To use it, a decision-maker needs p, L, c, the deadline, and the paths' thresholds and transit times. It does not answer the question's identification problem, which is which observations tell a warranted reserve from waste. The study sharpens that problem instead. Under the peak rule, readiness observed in operation and readiness under an imposed contingency differ, and the difference depends on how often the capability is used. CLAIM-517 (Active, demonstrated) holds the general point: "fidelity measured in ordinary operation certifies nothing about viability". QUESTION-395 stays Open. The decision rule is not on the record (gap GC4).

### 9.7 Reserve size is a step function

The study sweeps reserves from 0 to 2 in steps of 0.25, for each architecture. Readiness does not grow smoothly with the reserve. Any reserve strictly between two path thresholds gives exactly the readiness of the next lower threshold: in the original architecture, every reserve from 0 to 1.75 gives R(6) = 0.269, and a reserve of 2 gives 0.907. In the redesigned architecture, R(6) is 0.151 from 0 to 0.75, 0.664 from 1 to 1.75, and 0.907 at 2. Under common random numbers these values are identical, not merely close. So the only reserves worth considering are the path thresholds less the holding cost: 0, θ′ − 1 and 2. A reserve between them is paid for and buys nothing.

This is the converse of CLAIM-679 (Active, demonstrated), ChatGPT's sentence in the record: cutting the resource held "removes exactly the transitions whose threshold lies between the old holding and the new". Adding resource that reaches no new threshold reaches no new transition. The step function holds for one capacity resource and a finite set of paths. Under several resources (CLAIM-585) or cumulative costs (CLAIM-646) it need not hold (§9.9; gap GC3).

### 9.8 A demand the specification does not name

The draft's §9.6 asks the study to separate two things: an organization getting better at meeting its original demands, and an organization changing which demands it is judged by. It cites CLAIM-361 (Active, interpretive) for the distinction: "a demand excised or suppressed has changed the comparison and has not been satisfied, an endogenous revision of what the organization maintains is a transformation of it and not relief". CLAIM-361 makes that decidable against "A fixed reference set D₀ of the original demands".

**The arm.** After 50 quiet periods, holding A begins to cause a harm the specification does not name. A configuration C, also held at 1, is free of the harm. It is reached over A → N → C with r(N) = 2.5. The organization follows one of two policies.

- *Excise*: never enter the new demand into the specification.
- *Revise*: first review it for 3 periods. Each review period occupies 0.5 above holding, and is granted only if the budget allows. Once revised, the new demand is met like any other contingency.

Each run is scored three ways: against the original specification D₀, against the organization's own current specification, and against the true demands. The horizon is 120 periods and there are 400 replications.

**What it finds.**

- **Excision scores perfectly on two of the three scorecards.** It has zero violations against D₀ and against its own specification, while the harm runs for all 120 periods. Revision shows violations on both, including the output lost while moving to C: 4.1 periods under II and 13.3 under III-b, both with outside money. Only the true demand set ranks the two correctly. This is CLAIM-361's warning, met in a model: a score kept on the original or on the organization's own demands rewards the organization that never admits the new one.
- **Under the peak rule, excision happens by default.** When the review needs capacity (0.5 above holding), it can never start under I or III-a: the review is blocked in all 120 periods and the harm runs throughout. The organization has not chosen to excise. Its budget rule has left it unable to revise.
- **A reserve is general; a redesign is not.** II's reserve of 3 covers C's threshold of 2.5, and the harm lasts about 6.1 periods. III-b's and IV's reserve of 2 does not cover it. They depend on outside money, and the harm lasts about 15.3 periods. With no outside money (g = 0), III-b and IV revise their specification and never reach C, so the harm runs for all 120 periods. IV is worse: the review uses the capacity the drill used, so the drill cannot run, the budget falls, and the staged route is lost too (its budget ends at 1, against III-b's 2).

**The model's limit here.** The choice between excising and revising is an input to the model. Nothing in the model makes it. What the model shows is how each choice scores, and which budgets let a revision be acted on.

**A join, and a question the record lacks.** CLAIM-361 concerns a demand that was in D₀ and was removed. The study's new harm was never in D₀. Reading "never entering a new demand" as excision carries CLAIM-361 past its own case (join JC4: CLAIM-361 applied to a demand outside D₀). It also exposes a step the record does not hold. Scoring against "the true demands" needs a reference set that is neither D₀ nor the organization's own, and CLAIM-361 says it "does not say how to choose D₀, H or B" (gap GC6). Who holds that third reference set, and how it is revised, is the subject of §13.

### 9.9 What depends on the modeller's choices

Four choices change the results, and each is stated in `analysis/README.md`:

- **The staged route is slower**, three edges to two. If it were as fast as the original, III-b would match II at every deadline with half the reserve, and the crossing in §9.5 would disappear.
- **Outside money buys the cheapest route**, not the fastest. If it bought the fastest, III-a would match I, and redesign without a reserve would stop being worse than no redesign.
- **The review uses transition capacity.** That is why the drill and the review compete in §9.8.
- **The carry rule is capped at 3.** Without the cap, V's budget would grow without bound in quiet periods.

Other parts of the analysis do not depend on these choices: CLAIM-577's and CLAIM-tmpg8yl2's conditions (§9.4), the step function (§9.7), the equivalence of drill and reserve under peak accounting, and the way excision scores (§9.8). Each follows from the budget rule and the thresholds.

### 9.10 What the model establishes and what it does not

**What it establishes, within the model:**

1. Ordinary output can be matched exactly while readiness differs by a factor of three or more at moderate deadlines: R(6) is 0.894 for II and 0.267 for I.
2. CLAIM-577's and CLAIM-tmpg8yl2's conditions hold exactly, so the draft's redesigned regime needs a reserve.
3. Under peak accounting, a drill holds a reserve without a commitment. It costs what the reserve costs, and it fails when the schedule is broken rather than when the commitment is withdrawn.
4. Which regime is best depends on the deadline. On these assumptions, redesign without a reserve is worse than no redesign.
5. A reserve pays above a break-even pL* that depends on the deadline and on how often the capability is used, not on p·L and c alone.
6. Readiness is a step function of the reserve.
7. Scorecards kept against the original specification, or against the organization's own, reward excision. A budget held at the peak of its use can leave revision unfundable.

**What it does not establish:**

- **Anything about real industries or real budget rules.** The account of the readiness line, SYNTHESIS-031 (Proposed), says it does not claim "That the readiness argument applies to any real organization; its constructions and models say their organizational readings are analogies." The account of reaching and paying, SYNTHESIS-024 (Proposed), says it does not claim "That organizations have configuration spaces with such costs", and quotes CLAIM-579: "No organizational case in the record shows slack present in total and absent at the bottleneck." CLAIM-577 says real rules are "rarely pure spend-matching". CLAIM-921 (Proposed, demonstrated) shows that a rule with a floor can lose a capability too, through decaying competence, which this model does not represent.
- **Anything about cumulative or multiple resources.** The model has one capacity resource. CLAIM-646 (Proposed, demonstrated): "Peak-capacity thresholds do not fix cumulative transition costs". CLAIM-585 (Active, demonstrated): with several resources the sufficient budgets form a set that "need not be convex, so no threshold on a weighted total of the resources describes it". CLAIM-878 itself says its drill accounting fails for "budgets in money or hours", which count how long a capability is out. The draft's §9.5 calls for several contingencies with different deadlines, a "multidimensional temporal response profile", and none of that is run here (gap GC7).
- **Whether a redesign creates a capability or only cheapens one.** QUESTION-392 (Open) asks it. CLAIM-922 answers it in another model, according to whether the home configuration space is connected. Here the space is connected, so the redesign only cheapens.
- **QUESTION-395's identification problem** (§9.6).

The study's results are not yet on the record. A result that bears on entries goes back to the record as a CASE, with dated notes on the entries it touches, and the manuscript should then cite that CASE rather than the script (gap GC1).
