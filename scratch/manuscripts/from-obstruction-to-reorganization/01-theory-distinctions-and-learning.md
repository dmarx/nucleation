<!-- scratch/manuscripts/from-obstruction-to-reorganization/01-theory-distinctions-and-learning.md -->

# Part I. A theory of learning and inquiry

Part I states a general theory of how systems learn and inquire. It is meant to apply to any system that draws distinctions and acts on them: a cell, a trained network, a person, an institution, a community, a research record. It is assembled from claims that the Nucleation record holds, most of them argued for and filed long before this paper was conceived, in lines of inquiry about formal apparatus, realizability, will-organization, distributed agency and transmission.

Each step cites the entry that holds it, with that entry's standing:

- **Active:** the record accepts it.
- **Proposed:** filed and argued, but not adopted.
- **Demonstrated:** shown by construction or proof.
- **Interpretive:** argued.
- **Empirical:** observed.

Where this paper joins steps that the record keeps apart, it says so; those joins are collected in §7 as the theory's implications. Since 2026-11-21 the record gathers the theory's parts as a line of their own, `learning-and-inquiry` (ADR-130, Active), whose account maps them without adding to them (SYNTHESIS-tmpt1te9, Proposed; §7.4). Steps added on 2026-11-21 from the exchange "Rich Get Richer Power Laws" are marked; they concern learned representations, and every entry they cite is Proposed or Open. The `background/` folder beside this draft holds cited digests of the five regions of the record the theory draws on, for readers who want each step's full context.

Part I has two limits, which it should state at the outset. First, the theory was developed largely in exchanges between the record's owner and AI assistants, and several of its formal results came from those assistants (§4.1). Second, Part II and Part III of this paper study the record in which the theory was developed. The theory is not independent of its demonstration, and §18 counts the cost of that.

## 2. Systems that draw distinctions

### 2.1 The apparatus

Begin with the most general object the theory needs: something that makes some differences in the world matter to what happens next. The record's term for it is an **apparatus**, in an operational sense that presupposes no observer: "a realized organization that selectively couples differences in one system to distinguishable outcomes in another" (TERM-089, Active).

An apparatus can do four things, and they come apart:

- **It differentiates:** some differences in its input produce different outcomes.
- **It retains:** it keeps those distinctions over time.
- **It enforces:** the distinctions change what happens next.
- **It revises:** it changes its own criteria of discrimination.

A thermostat differentiates, retains and enforces, but does not revise. A scientific community does all four, at different rates and with different reliability. The theory is about the fourth function, and about what the other three must be like for the fourth to work.

### 2.2 A distinction is relative to a target and a regime

No distinction is good or bad in itself. Any individuation built on sufficiency "is relative to the target it is sufficient for: fix the outcomes differently and a different partition wins, so no boundary drawn this way is universal" (CLAIM-152, Active, demonstrated). The record makes this exact in three results.

- **The judgment test.** A coarse-graining preserves a deterministic judgment exactly when the judgment is constant on each class the coarse-graining merges. "Otherwise two states the judgment tells apart have been merged" (CLAIM-350, Active, demonstrated).
- **The policy test.** An organization that acts on what it observes "has a policy acceptable in every circumstance exactly when, for each observation, the circumstances it cannot tell apart share an acceptable action" (CLAIM-535, Active, demonstrated). Every circumstance having some acceptable action does not give a policy. A finer observation never removes one. And where acceptable actions overlap, the coarsest adequate observations are several and incomparable, so "which distinctions must be made legible depends on which acceptable action the organization commits to."
- **Incomparable adequacy.** Two organizations facing the same circumstances with the same acceptable actions can each be minimally adequate while telling apart different and incomparable sets of circumstances (CLAIM-622, Active, demonstrated). A difference in the distinctions two perspectives draw is therefore not, by itself, evidence that either is deficient. Which is deficient can be judged only against the policy each commits to.

The target is not fixed by the description that serves it. A description adequate for an institution's performance "can merge states its members' claims must distinguish". Adequacy is fixed by the evaluative target, and the target cannot be justified solely by the description that preserves it (CLAIM-348, Active, interpretive).

To keep these relativities explicit, the record names the frame within which any description is judged, an **effective-description regime** (TERM-065, Active). It has six parts:

- the system;
- the questions asked of it;
- the interventions admitted;
- the resource bounds;
- a tolerance;
- a horizon.

A regime is kept apart from the description being judged, so that rival descriptions can be compared under one regime. Throughout this paper, "adequate" means adequate under a stated regime.

**The first principle of the theory follows.** A new distinction is *needed* exactly when two situations that a system currently treats alike call for different acceptable actions under the target it is committed to. It is *not needed* when merging them loses nothing for any target in the declared family. Whether to split is therefore never settled by data alone. It also depends on what the system commits to doing.

### 2.3 Observing splits, acting merges, and optimal categories reorganize

Distinctions depend on budgets, and two budgets pull in opposite directions. "More resource for observing splits what can be told apart, and more resource for acting merges what can be turned into one another, so a system's budgeted individuation runs in opposite directions from outside and from inside and is indexed by a pair of budgets, not one" (CLAIM-557, Active, demonstrated).

Each direction is orderly on its own:

- **Observing.** Along nested families of probes, distinctions only grow. Objects told apart at a lower budget stay apart at every higher one (CLAIM-574, Active, demonstrated).
- **Acting.** Under peak-capacity costs on reversible moves, the configurations a system can turn into one another within a budget nest into a single tree as the budget grows (CLAIM-581, Active, demonstrated).

The two partitions, what an observer can tell apart and what the system can reach, "agree exactly at partitions common to the observer's refinement chain and the system's merge tree". Which levels appear depends on the order in which the observer's probes become affordable (CLAIM-592, Active, demonstrated).

The record's formal results show four ways in which the tidy picture breaks:

- **Optimal categories reorganize.** For a learner optimizing a rate-limited objective, the best categories at a larger budget need not refine the best at a smaller one. In the record's worked example, the optimal partition of four states is {0,1,2 | 3} over one range of budgets and {0,1 | 2,3} over the next, and neither refines the other (CLAIM-387, Active, demonstrated). The same holds with noisy encoders (CLAIM-392, Active, demonstrated). Raising the budget can **re-carve** the categories rather than split them. Where distinctions come and go has a model on the record (CLAIM-770, Proposed, demonstrated). The tree of classes a chain can reach within a budget keeps its shape while the barriers between states move, and changes only where two barriers cross. A distinction between levels comes into being or passes away at such a crossing, and near it the two levels cannot be told apart. How much separation in rates a level needs before it shows is open (QUESTION-500, QUESTION-501). The review of 2026-11-21 revised the account that holds this region (SYNTHESIS-048, version 2, Proposed) to integrate CLAIM-770 with CLAIM-672 and CLAIM-781 (both Proposed). It filed no new claim there: that a level's creation and its stabilization are dated apart by one parameter is already CLAIM-770's.
- **Levels are not classes.** The "levels" of CLAIM-770 and the "what can be told apart" of CLAIM-574 are different senses of separation. The record now names three, which come apart (TERM-tmpol232, Proposed, the assistant's sorting of an exchange's uses): separation of *scales or levels*, a gap in rates, sizes or coupling over which a coarser description closes; separation of *classes*, an observer telling two states apart under its budget; and *spectral* separation, an outlier eigenvalue leaving a noise bulk. Near a critical point a system is "harder to separate but easier to classify" (CLAIM-tmpjbee7, Proposed, A's): no level separates, yet the class is easy to tell. And a finite correlation length does not by itself yield levels in Simon's sense (ARG-tmp09yqc, Rejected, the assistant's verdict on A's inference). This principle's two directions concern classes; CLAIM-770's crossings concern levels.
- **Closure is not ordered by refinement.** A deficiency of sufficiency for a fixed target can only fall as a description is refined, but informational closure "is monotone in neither direction" (CLAIM-409, Active, demonstrated). A finer description can lose a self-contained dynamics that a coarser one had.
- **Bounded observers trade tasks.** For one bounded observer, a transformation of a representation "can make one task's distinction legible and another's illegible at once" (CLAIM-455, Active, demonstrated).
- **Averages and non-nested probes lose the guarantee.** The monotone growth of CLAIM-574 holds only for nested probes compared probe by probe. An averaged comparison does not carry it.

**A budgeted telling-apart, in a learned representation (added 2026-11-21).** The filing of the exchange "Rich Get Richer Power Laws" (2026-11-20 to 21; all entries Proposed or Open) gives the observing direction a concrete case, and adds two qualifications. The entries are the owner's, A's (the other assistant in that exchange) or the assistant's (Claude, filing it), as marked; the record's part account of them is SYNTHESIS-tmpsejrp (Proposed, a part account of `learned-structure`).

- **The budget is the sample.** Sample PCA finds a planted direction of strength β only above the spectral threshold β > √(D/N), in D dimensions from N samples (CLAIM-tmp5y856, A's, demonstrated; CASE-tmp59xy5, A's construction, checked). The threshold falls as N grows: more observing resource tells apart what it could not. The papers behind the threshold (Baik, Ben Arous and Péché, and those that extend it) are being read.
- **The observer's kind matters as much as its budget.** At β = 0.4, below a threshold of 0.5, PCA finds nothing while a linear readout trained on the labels is about three-quarters accurate (CASE-tmp59xy5). What can be told apart is relative to the probe family as well as the resource, as CLAIM-455 already says for bounded observers. Geometric separation, decodability and spectral detectability are three qualities that need not agree, and the spectral threshold "marks when that estimator can see the signal, not when the network acquired it" (CLAIM-tmp5y856).
- **Thresholds of telling-apart are not transitions of the system.** On one scale of alignment strength the record places three thresholds: a cone's occupancy (order √D), spectral detectability (√D·(D/N)^(1/4)) and an alignment bifurcation (order D). Only the last is a transition of the system (CLAIM-tmpk33au, the assistant's, demonstrated, in a mean-field model). This supports the principle's separation of what can be told apart from what the system has, or keeps.
- **What a fixed number of variables can hold.** The record holds, as A's claim, that nearness to a dynamical transition redistributes a bounded computational capacity across tasks rather than raising it, the bound being the number of independent state variables (CLAIM-tmpask80, Proposed; ARG-tmpubyzo, Proposed, gives the conditions; CLAIM-tmpd1shn, the assistant's, finds the exchange's memory-noise tradeoff absent from its own model). Dambre and colleagues' bound is being read.
- **Distinctions resolved grow with data.** When past and future share a parameter, predictive information grows as (d/2) ln T with d resolved directions, and faster when the Fisher spectrum falls as a power law (CLAIM-tmpyxiwv, the assistant's, demonstrated). Bialek, Nemenman and Tishby's paper, which it reads against, is being read.

**Re-carving in a learner: two readings of the owner's suggestion (added 2026-11-21).** The owner suggested that singularity theory's account of "phase transitions in learning as resolutions of singularities" might be useful for progressive learning (CLAIM-tmpp83vc, the owner's, U23, Proposed). The record files two readings as alternatives, and the owner has not chosen:

- **(a)** Training itself carries out a resolution (CLAIM-tmp85eq8, Proposed, stated by the assistant). The assistant argues it fails: a blow-up "reparametrizes the states and adds no observation" (CLAIM-305, Active), so such a transition would change nothing the network computes (ARG-tmpbmruy, Proposed).
- **(b)** A transition is a change in which singular region of parameter space dominates as the sample grows, between regions that fit differently, with resolution as the tool that computes their coefficients (CLAIM-tmpgzb8v, Proposed, A's).

On reading (b), the best model at a larger sample need not refine the best at a smaller one. That would make a learning transition a case of this section's re-carving, with the sample as the budget. *The join is this draft's*: no entry ties CLAIM-tmpgzb8v to CLAIM-387. On reading (a) the section gains nothing. Beside both, A's claim that progressive learning is described by two partial orders, semantic entailment and Blackwell refinement among checkpoints, "neither of which need be a chain" (CLAIM-tmpr4k9z, Proposed), agrees with the principle that refinement is one case, not the general one.

**The second principle follows.** As a learning system's resources grow, its categories may need to split, merge, or be re-carved. What can be told apart only splits, along nested probes compared probe by probe. At a given budget it also depends on the kind of observer, and its thresholds are not transitions of the system observed. What is optimal to keep is a different object, and can re-carve. Some learners are guaranteed nested optima: the record holds a nesting result for the information bottleneck with side information (NOTE-676). So refinement is one case, with conditions of its own, and not the general one. "Separation" in this principle is separation of classes, not of levels (TERM-tmpol232).

### 2.4 What a system can see, and what it can certify about its own categories

A distinction can exist in the world and be unavailable to a particular system. The record's term is **legibility**: whether an observer, "with the rules, categories and resources it actually has, can recover the distinction from what it is given and bring it to bear on the task" (TERM-064, Active).

Legibility is bounded above by what the source makes possible. Blackwell's order bounds what any rendering makes possible for any receiver. A garbling can raise a particular receiver's usable information, but never above what the source makes possible (CLAIM-199, Active, interpretive). Deficiency in Le Cam's sense gives an ex ante, computable certificate of how much a rendering can lose across every bounded-loss decision problem (CLAIM-503, Active, demonstrated).

What a system can certify about its *own* categories is sharply limited, in four ways:

- **Agreement is coarser than identity.** Two objects can agree on every probe in a restricted family without being the same (CLAIM-264, Active, demonstrated). Agreement under a family of probes is coarser than identity unless the family is rich enough (TERM-069, Active).
- **Training probes cannot certify.** "A family of probes that supplies an optimized system's training signal cannot also certify what the system preserves", because optimization pushes toward whatever the probes reward, "including what they cannot see". Preservation must be shown under probes not used in training (CLAIM-266, Active, interpretive). A correspondence between two descriptions must be "anchored to independently measured distinctions and evaluated on tasks other than those it was estimated on" (CLAIM-011, Active, demonstrated).
- **Categories confirm themselves.** A category's predictive success warrants treating it as real "only when the evidence in those contexts does not pass through the category's own use, or when the effect of that use is modelled". "A category that speakers or institutions act on can produce the regularities that confirm it" (CLAIM-402, Active, interpretive).
- **Passive agreement hides differences.** Systems that agree under ordinary operation can differ in efficacy, in how it is allocated, and in how its enabling constraints are maintained. In two finite constructions, "a specified intervention exposes the difference that passive observation of the matched trajectories does not" (CLAIM-414, Active, demonstrated). A coarse-graining exactly closed under ordinary dynamics can still lose the system's response to an intervention on its mechanism (CLAIM-407, Active, demonstrated).

**Nulls, and measures built from the categories under test (added 2026-11-21).** The exchange "Rich Get Richer Power Laws" supplies four cases of the same limit, all Proposed:

- **A geometric null.** In high dimension, a thin radial shell, nearly orthogonal directions and nearly equal distances "arise with no interaction at all, so they are a null baseline and not evidence of learned attraction, order or collapse" (CLAIM-tmp41gfr, A's, demonstrated). The owner raised concentration of measure (CLAIM-tmpfwwfy, U19).
- **A measure that its own categories move.** Occupancy of entailment cones "rises when cone boundaries move as well as when representations flow, it rises under collapse", and nesting makes a coarse cone entered first by construction. So coarse-to-fine learning "needs an independent measure" of when each distinction becomes decodable (CLAIM-tmp6mjfc, A's, demonstrated).
- **A metric that ranks the other way.** Whether a direction is small depends on the metric, and metrics can rank directions in opposite orders: a label can sit wholly in the least-variance component (CLAIM-tmppkdjz, A's, demonstrated).
- **A distribution that does not name its mechanism.** Many routes produce a power law, and the distribution does not tell them apart. Which one is at work is read from dynamics, cutoffs and the response to a perturbing field (SYNTHESIS-tmp69tyj, Proposed, a part account of `formal-apparatus`; LEAD-tmpng7or, Open, the protocol). That is CLAIM-414's point about passive observation, in another domain. *The join is this draft's.*

Each supports the principle below. The first adds something it does not state: evidence must be scored against what the measure would show with no learning at all. Whether that is a fourth route to certification or a case of "a model of the effect" is the draft's question; no entry answers it.

Legibility bounds correction. The record's measure of **correctability** is the chance that an arrangement, starting from the description of the problem it actually has, finds, authorizes, coordinates and carries out a corrective plan in time (TERM-085, Active). If the description merges two failure modes that need different remedies, no better process downstream can choose between them until the description is refined.

**The third principle follows.** A system cannot certify the adequacy of its categories using the evidence its categories produce. Certification needs one of three things:

- evidence whose arrival or scoring does not pass through the categories under test (§6.3);
- a model of the effect of using them;
- an intervention.

The new cases of 2026-11-21 add that whichever is used must be scored against a null, what the measure would show with no learning (CLAIM-tmp41gfr). That addition is this draft's, not an entry's.

### 2.5 When a distinction earns a name

Suppose a candidate distinction is legible and useful. When should a system make it a unit, something it names, keeps and builds on? The record holds two priced criteria that pull in opposite directions, and asks whether a third ever agrees with them.

- **Evidence.** Name a candidate structure "when its effect-to-noise ratio outruns the Occam cost of keeping it" (CLAIM-154, Active, demonstrated). Where the model is singular at the parameters that switch a candidate off, the rule overcharges keeping it (CLAIM-188, Active, demonstrated). The candidates it names are blocks, sectors and couplings with hidden structure.
- **Retrieval under a deadline.** Evidence that a distinction exists grows with its copies, but the search a bin saves shrinks with them, "so the bins a deadline forces are often the ones the data least supports" (CLAIM-307, Active, demonstrated).
- **Survival under refinement and compression.** A third criterion, which the record has from the owner's earlier work rather than as a claim it holds. Whether the three ever pick the same categories is open (QUESTION-113, Open).

**The evidence criterion at a finite sample (added 2026-11-21).** CLAIM-188's correction is for a model *singular* where the candidate switches off. The record now keeps singularity apart from *sloppiness*, a Fisher spectrum spread over many decades with no gap between the combinations that matter and those that do not (TERM-tmptiim0, Proposed, at the owner's suggestion). A model can be "sloppy everywhere and singular nowhere or singular everywhere with no spread" (CLAIM-tmpcgvcp, A's, demonstrated). The two meet at a finite sample. A direction too sloppy for the data to resolve "contributes to the learning coefficient no more than a flat one", and in a regular sloppy model the coefficient rises by about ½ for each direction resolved (CLAIM-tmpcg4uu, the assistant's, demonstrated). *Read in CLAIM-154's terms, which is this draft's reading and no entry's*, the Occam cost of keeping a structure is charged only on the directions the sample resolves. So what earns a name depends on the sample, as what can be told apart does (§2.3). A's proposed duality points the other way: model reduction, toward the model manifold's boundaries where parameters stop mattering, would be unnaming, and differentiation, away from singular strata, naming (CLAIM-tmpnu4ar, Proposed, supposed, its ground unread). The readings of the sloppiness papers and of the local learning coefficient are being filed.

A fourth, systemic criterion is Proposed. A process that collapses differences that do not matter, identifying micro-states by what they do, comes to treat the classes it keeps as units of further computation and organization. On this proposal, a class becomes a unit when it is closed under the system's own operations and reused (CLAIM-762, Proposed, interpretive).

**The fourth principle follows, and it is provisional.** Naming is a separate decision from distinguishing. Whether to name a distinction turns on evidence, on the cost of retrieval and on reuse, and these can disagree. A system that names only what the data supports will under-name the structures it needs. A system that names whatever saves search will over-name what the data cannot support. And, on this draft's reading of CLAIM-tmpcg4uu, what the evidence supports naming moves with the sample.

## 3. Learning as the formation of maintained capacity

### 3.1 What learning is a response to

The theory's account of learning starts from difficulty, not from data. The record takes the primitive of an organization's regulatory difficulty to be **frustration**: "a relation between maintained, consequential demands and the incompatibilities, constraints or countervailing processes that limit their realization" (CLAIM-368, Active, interpretive). It is not distress or strain.

Frustration is ordinal before it is a quantity. The jointly satisfiable sets of a system's demands form a downward-closed complex, and its minimal non-faces are the minimal conflicts (CLAIM-347, Active, interpretive). **Relief** is strict enlargement of that complex for the same declared demands. "Dropping or suppressing a demand is not relief."

A *discrepancy*, in what follows, is such a conflict that the system cannot yet resolve. In a research record, a discrepancy is a move the record's categories cannot hold: a contribution that fits no type, a distinction no field can express, a status that lumps together situations that need different handling. This paper calls such a discrepancy, once noticed, an **obstruction**.

### 3.2 Self-formation: a new distinction or a new channel

The record's account of what a system can do about an unresolved discrepancy is CLAIM-532 (Active, interpretive, version 5 of 18 November). It says:

> An unresolved discrepancy is an occasion for self-formation … and not a guarantee of it; it suffices for self-formation that the agent's own activity on such a discrepancy produce a maintained capacity, either a new distinction, its policy coming to depend on a feature of its situation it did not depend on, or a new channel, the outcomes it can reach under its own policy growing, that outlasts the discrepancy and serves a class of later ones.

The defined term (TERM-099, Active) calls this **self-formation**. Six features of the account carry the rest of the paper:

- **Occasion, not guarantee.** "An agent may stay stuck on a discrepancy, or settle it another way" (CLAIM-532). Meeting an obstruction does not make a system learn. It may bear the discrepancy at a standing cost, suppress one of the conflicting demands, or reorganize.
- **Two products.** A *new distinction* refines the system's partition of its situations. That is what CLAIM-535 says a policy needs where acceptable actions differ. A *new channel* enlarges the outcomes the system can reach under its own policy. In the words of an assistant's turn quoted in CLAIM-532's note of 7 November, it is "changing what it can do, not only by improving what it can see" (A58). Either one enlarges what is jointly satisfiable, which is relief in CLAIM-347's sense.
- **Defined by behaviour, not mechanism.** The products are defined at the level of the policy, "whatever implements them". A learned readout over a frozen random projection is, counted in components, only a reweighting, "yet the readout can come to separate inputs it did not" (CLAIM-532). This is why the theory can apply to arbitrary systems: it does not care whether a new distinction is a new neuron, a new field in a schema, or a new word.
- **Maintained.** Where every capacity turns over and is produced only by others, with no basal production, a capacity that persists "needs a productive cycle among its ancestors". The cycle is necessary and not sufficient (CLAIM-516, Active, demonstrated). A distinction drawn once and then lost is not a capacity.
- **Class-serving, and tested by transfer.** The capacity must outlast the discrepancy that occasioned it and serve a class of later ones. The first test is transfer: remove the inducing conditions and present a new discrepancy of the same class.
- **Tested by intervention while it forms.** The second test is intervention on the processes that produce the capacity *while it forms* (CLAIM-532, after CASE-191). This is how own formation is separated from installation from outside (§3.4).

CASE-191 (Active) is a construction of self-formation. An agent's own frustration, at two demands that one shared output cannot meet, drives production of a sensor and a differentiating channel that then maintain each other. Past a threshold of discrepancy (D ≈ 0.645 at unit drive), the capacity forms, outlasts the conflict, and meets later conflicts of the same class. Below the threshold, discrepancies "are tolerated, at a standing frustration, and form nothing." The construction is fictional in the record's sense. Its threshold is a property of the model, and the general point it illustrates is that a discrepancy can be borne without anything forming.

The account has a classical ancestor in Ashby's ultrastability. A second feedback changes a system's parameters whenever, and for as long as, an essential variable is outside its limits, so that every equilibrium the whole can reach is an adapted one (THEORY-324, Active, from LIT-787). CLAIM-532 differs in three respects:

- it names the products, a distinction or a channel, where Ashby has only "parameters";
- it requires the product to be maintained and to transfer;
- it asks whose process produced the product (§3.4).

**The fifth principle follows.** An unresolved discrepancy is an occasion, and a sufficient condition, for one important kind of learning: the formation of a maintained capacity, a new distinction or a new channel. CLAIM-532 states a sufficient condition, not a definition. The record's proposed definition of learning is broader (TERM-131, Proposed): latent learning, such as an unrewarded exploration that forms a map used later, is learning with no discrepancy. A discrepancy may be borne without anything forming, as below the threshold in CASE-191's construction. A discrepancy can also be "settled" by giving up a demand, which is capitulation, not learning. And a new distinction can be active, and consequential, before a passive observer can see it (CLAIM-tmpqbo50, Proposed, in one model), so its tests need a stated date and an observer tied to the task.

**A case from interface learning (added 2026-11-21).** First Contact (Reddy, Levine and Dragan 2022; read on the record as NOTE-2236, THEORY-2147, Proposed) learns a control interface with no knowledge of the user's task, by maximizing the information between the user's command and the state change it induces. The record reads it as this section's second product (CLAIM-788, Proposed): the obstruction is a failure of information split between two parties, the interface that can act and the user who knows the task, and the repair forms a channel through which the party with the information steers, rather than supplying the information. Its one failure, an assistant that stabilizes the vehicle and so lowers the user's one-step influence while raising it over the episode, reads as a choice of level at which a channel is judged (CLAIM-787, Proposed). The paper runs neither of this section's two tests, transfer once the inducing conditions are gone and intervention on what produces the capacity, so it illustrates the route without certifying it; and whether help that stabilizes erodes the capacity it stands in for is open (QUESTION-504), §3.7's loss by support that does the work.

**A case from representation learning: how a new distinction is born (added 2026-11-21).** The exchange "Rich Get Richer Power Laws" built, and the record filed, a minimal model of the first product, a new distinction, in a trained network. Its part account is SYNTHESIS-tmpsejrp (Proposed). All of it is Proposed, demonstrated in toy models, and none of it is run on a trained network (LEAD-tmpfrw11, Open, is the proposed test).

- **A threshold below which nothing forms.** A factored feature under weight decay, ŷ = abφ, switches on only when its signal s exceeds the decay λ. Its strength is (s − λ)₊; at s = λ the origin loses stability through a pitchfork in the parameters, relaxation is algebraic, and the local learning coefficient dips from 1 to 3/4 (CLAIM-tmp9bp04, A's, checked by the assistant). Below threshold the signal is borne and nothing forms, as below CASE-191's threshold. *That parallel is this draft's*: the record does not read the model as self-formation, and nothing in it is a discrepancy among demands in CLAIM-347's sense.
- **Quiet but consequential.** Just above threshold the feature's variance is of order ε² while its gain in fit is of order ε (CLAIM-tmp9bp04). So it is active, and improves the fit, while sample PCA cannot see it. Onset and the singular point coincide at s = λ, but PCA detects the feature only once s − λ exceeds σ²√(D/N), a lag that narrows as the sample grows (CLAIM-tmpqbo50, the assistant's, demonstrated; it narrows a synthesis of A's that failed the admission test).
- **Formed distinctions gate later ones.** When a parent feature gates a child, ŷ = g·abφ, the child switches on only when gs > λ, so "acquisition follows a partial order of dependencies rather than a fixed coarse-to-fine chronology" (CLAIM-tmpl9zw4, A's, checked; the assistant corrected its delay formula). A distinction once formed lowers the threshold of the ones that depend on it. That is one way a capacity "serves a class of later ones", *on this draft's reading*.
- **Formation has more than one date.** In the same model, "the time a feature becomes unstable, the time it becomes visible and the time its information was first encoded can all differ" (CLAIM-tmpl9zw4).

What this does to the principle below. It **supports** the first product, a new distinction defined by behaviour and not by mechanism: the feature is a change in what the predictor depends on. It **qualifies** the tests in two ways. "Intervention while it forms" needs a stated date, and the model gives three (§3.4). And a passive observer sees the product late, so absence of a visible change is not absence of formation. It does **not** show that the formation is the system's *own*, in TERM-100's sense: a gradient learner's threshold is set by its objective and regularizer.

The singular geometry is a further reason for caution. The record separates sloppiness from singularity (CLAIM-tmpcgvcp; TERM-tmptiim0), and that a stage of learning is a transition among singular strata is held only as a question (QUESTION-tmpsy8qn, Open): does the order of the strata map onto the order in which representations refine? In the one worked model, the stages on either side of the threshold have the same local coefficient and only the threshold point is singular (SYNTHESIS-tmpsejrp, "Not stated on the record").

### 3.3 What does not count

Three things look like learning and are not, or are not yet:

- **An observer's posterior.** A run of selections from a fixed mixture looks persistent to an observer who updates on it: "an observed first choice raises the predicted chance of repeating it from 1/2 to 2/3, while the same choice forced leaves it at 1/2" (CLAIM-540, Active, demonstrated). Self-formation "requires a causal update, not merely a posterior update in the observer". The system must change because of what it did.
- **A response that does not transfer.** It solves the case at hand and leaves the system no better placed for the next case of its kind (TERM-099).
- **A uniform change of priority.** One regime now always prevails where another did. This refines no distinction and enlarges no reachable set, but it outlasts the conflict and governs later ones. CLAIM-532 does not cover it either way, and the record keeps it open (QUESTION-488, Open).
- **Geometry that arises with no learning** (added 2026-11-21). In a high-dimensional representation, a thin shell and near-orthogonal directions arise "with no interaction at all" (CLAIM-tmp41gfr, Proposed, A's). And coupled embeddings under gradient flow relax rather than act, so collective motion alone is not the activity of a learner (CLAIM-tmpet76z, Proposed, the assistant's). Such regularities are a null that learning has to beat (§2.4), not its product.

### 3.4 Provenance: whose learning is it?

The record separates three senses of a capacity's **provenance** (TERM-100, Active): *formation* (whose process produced it), *maintenance* (whose process keeps it in being now) and *source* (what it was made from). The first two come apart.

- **Recovery cannot show where maintenance comes from.** A system that maintains a capacity itself and a system whose capacity is maintained by an outside controller, which measures the capacity and supplies the production law as feedback, follow "the same trajectory under every perturbation of state, damage and recovery included, even with every capacity observed exactly". Only interventions on the production mechanisms, relative to a declared boundary, separate them (CLAIM-522, Active, demonstrated).
- **After the fact, installed and self-formed look the same.** In CASE-191's construction, a capacity installed by an outside pulse and then self-maintained is the same organization as one the agent formed itself. Only a knockout made during formation separates them.

This has a consequence that is easy to state and hard to honour. Whether a system learned something *itself* cannot be read off its learned state. It needs a record kept at the time of formation, or an intervention made then. "Then" needs stating: in the record's model of a gated feature, the times at which a capacity is first encoded, becomes stable and shows in behaviour can all differ (CLAIM-tmpl9zw4, Proposed, A's; added 2026-11-21). That is as true of a trained model or an institution as of a person, and it is the theoretical reason the research record studied in Part III keeps its provenance trails.

### 3.5 Three ledgers: building, keeping, moving

A capacity has at least three resource requirements: "to construct it, to maintain it, and to move into or out of it, and none fixes another" (CLAIM-569, Active, demonstrated). "Having enough to sustain it is not having enough to acquire it." The record supplies the mechanics:

- **Reach has its own threshold.** For a fixed architecture, the resource threshold for reaching a configuration is "the least, over admissible transition paths, of the peak requirement along the path, and it is infinite when no admissible path joins" the start to the target. It can exceed what holding either end requires (CLAIM-571, Active, demonstrated). The difference is **reconfiguration slack**: the temporary resources needed to move between two configurations a system can each hold (TERM-106, Active).
- **Budgets can ratchet.** "A budget set each period to the peak resource spent the period before never rises." The configurations an organization can reach shrink monotonically, and any transition whose threshold exceeds the cost of holding the current configuration is lost after one period spent holding it (CLAIM-577, Active, demonstrated). The loss leaves no trace in output.
- **Possible is not reachable is not reliable.** That a configuration is feasible, that it is reachable, and that the process reliably reaches it are three properties, "each implied by the next and none implying it" (CLAIM-567, Active, demonstrated).

**The sixth principle follows.** A theory of learning needs three ledgers: the cost of forming a capacity, the cost of keeping it, and the cost of changing it. A system can be rich in one and bankrupt in another. A system that sets its budget for change to its most recent spending, with nothing to raise it from outside, loses transitions that need slack after a quiet period, without any sign in what it produces.

### 3.6 What learning buys: reliability or reach

The record distinguishes two things a learned constraint can give a system:

- **Reliability.** Under a fixed dynamical model, "an added hard constraint cannot enlarge the set of admissible trajectories". It cannot enlarge what the system can reach. What it can improve is a property required of every path a disturbance may take, "such as robustness or reliability" (CLAIM-582, Active, demonstrated). Enforcing a distinction makes a system more reliable within its repertoire.
- **Reach, through stored work.** A *stabilized* constraint can be **stored work**. By replacing later work with cheaper operations, it changes which activities are realizable within a fixed per-task budget, "so amortization becomes capability expansion without any added degrees of freedom or resources". The expansion is conditional on the costs of constructing, keeping, retrieving, verifying and revising the constraint, and "the persistence that buys it can entrench" (CLAIM-761, Active since the promotion of 2026-11-20, interpretive).

The record proposes that what characterizes a constrained system is its **repertoire** of realizable processes, indexed by resources and dependent on its architecture. That repertoire can change in three ways an equivalence between systems must keep apart (CLAIM-576, Proposed, interpretive).

### 3.7 How capacities are lost

The record holds four distinct routes by which a learned capacity is lost. Each loss is invisible in ordinary operation and shows only under the contingency the capacity is for:

- **Disuse.** "A procedural capability that operation seldom calls on decays with the time since its last use." A capability kept for rare events "is maintained by practice outside operation, not by operation" (CLAIM-558, Active, interpretive). Recording the correction does not stop the decay. "A successful corrective act, an executable procedure and a maintained organizational capacity are three different things" (CLAIM-422, Active, interpretive).
- **Support that does the work.** "Where an organization's capacity is learned by doing the work it serves, and decays with disuse, outside supply that does the work first lowers the capacity kept." Supply "that covers only what the organization cannot yet do leaves its learning untouched" (CLAIM-602, Active, demonstrated). Where capacity is needed to grow capacity, such support "has a deadline after which withdrawal no longer restores capacity", and a slow taper is worse than an abrupt cut (CLAIM-605, Active, demonstrated). Two forms of support that give the same capabilities now can therefore leave different capabilities later (CLAIM-675, Active, demonstrated). An arrangement that does the work through which a collective governs it "can erode the capacity to govern it" (CLAIM-673, Active, interpretive).
- **Protective lock-in.** A disturbance activates a protective regime that reorganizes ordinary activity in ways that sustain the regime, so that "continued activation further reduces the practical capacity to leave or revise it" (TERM-020, Active).
- **Ratcheted budgets.** The budget ratchet of CLAIM-577 (§3.5).

A capacity for a rare contingency is defined under intervention, "so a record of what was done does not measure it" (TERM-115, Active).

**The seventh principle follows.** A learned capacity must be maintained, and its maintenance is known only by intervention or by the contingency it serves. A record of past correction is not evidence of present capacity. Where a capacity is learned by doing and decays with disuse, help that does the work it is learned from can erode the capacity it helps.

### 3.8 Stable, persistent, productive

Three further distinctions guard the account against confusing staying power with value:

- **Stability is not viability.** "A system can occupy a stable regime while losing access to trajectories that keep satisfying its constraints" (CLAIM-079, Active, demonstrated).
- **Assembling, persisting and regenerating are separate.** That a form assembles, that it persists over a horizon, and that the system regenerates it after turnover "are three properties with separate probabilities" (CLAIM-566, Active, interpretive).
- **Persistence is not productivity.** Two intermediates of an assembly "can have the same expected residence time and different chances of reaching the target before failure", and an intermediate can persist while lowering the target's chance of forming (CLAIM-595, Active, demonstrated). A **productive nucleus** is judged by what its establishment does to later development, against a declared target, horizon and comparator (TERM-117, Active), not by its size, age or persistence.

The record proposes two related learning results, both Proposed:

- **Three frontiers.** A learner's acquired organization fixes an operational, a developmental and an inquiry frontier, which move separately (CLAIM-754, Proposed).
- **Overconsolidation.** Continued stabilization can keep improving a learner's present objective while raising the budget it needs to learn what comes later. The record calls this a generalization of overfitting (CLAIM-758, Proposed).

The record's proposed general definition of **learning** collects these points (TERM-131, Proposed). Learning is an experience-dependent change in a system's retained organization that alters what it can later do, at what cost and with what reliability, judged against the counterfactual in which the experience did not occur, and distinct from *successful* learning, which is relative to a declared target.
