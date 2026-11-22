# Reader notes: shalizi2003 (LIT-2996)

Shalizi & Moore, "What Is a Macrostate? Subjective Observations and Objective Dynamics", arXiv cond-mat/0303625.

## Step 1: copies located (2026-11-22)

- https://arxiv.org/pdf/cond-mat/0303625 : arXiv preprint (the authors' own deposit), PDF, HTTP 200, fetched 2026-11-22. Only version v1 (29 Mar 2003). Read in full.
- https://arxiv.org/abs/cond-mat/0303625 : abstract page, HTTP 200. "15 pages, no figures".

No other copy was sought: the arXiv deposit is the authors' own full text and was read whole. No bot check, paywall or refusal met. No email address sent anywhere.

## Provenance

- Read: arXiv PDF, https://arxiv.org/pdf/cond-mat/0303625 (v1, the only version; submitted 29 Mar 2003 by C. R. Shalizi), extracted with pdftotext, 13 pp. plus references. Read in full: abstract, §§I–VI, footnotes 1–7, Appendices A–C. Reference list skimmed only.
- Oddity: the PDF's dateline reads "Begun 10 July 2000; last revised November 26, 2024". arXiv lists only v1 (36 KB, 2003); the 2024 date is almost certainly LaTeX's \today from arXiv's re-render, not a revision. Cite as v1, 2003.
- Venue: none stated on the arXiv page. The paper thanks a Jerusalem conference (May 2000) on the foundations of statistical mechanics; whether it appeared in print was not checked.

## Summary

The paper asks whether thermodynamic macrostates are objective or reflect our ignorance, and answers "both". An observer starts from observables f : Γ → Ξ (subjective: what we can and want to measure), which partition phase space. The observed process need not be Markov. One forms the causal states of the observed process (computational mechanics: classes of observation histories with the same conditional law of futures), refining or coarsening the observed partition until reaching "a set of states which predict their own future, i.e. which are Markovian" (abstract). The partition reached is fixed by the microdynamics (objective). Good macrostates are those that are their own causal states. §IV turns this into an account of levels of description and a definition of emergence by predictive efficiency E/Cµ; §V lists what is not explained.

## Contribution

1. Identifies macrostates with the causal states of the observed process, so macrostate choice is observer-relative at the input (the observables) and dynamics-fixed after it.
2. A four-way classification of how the causal partition relates to the observed one (equal, finer, coarser, incomparable), with physical examples of the first three.
3. A definition of emergence between two sets of causal variables: one a coarse-graining of the other, and predicted more efficiently (higher E/Cµ). The opposite is Crutchfield's "submergence".
4. Coexisting levels (thermodynamic, hydrodynamic) explained as answers to different questions.

## Key results (section, quote)

- Abstract: macrostates are "the unique maximal partition of phase space which 1) is consistent with our observations (a subjective fact about our ability to observe the system) and 2) obeys a Markov process (an objective fact about the system's dynamics)". §I words it as "a unique coarsest such refinement, given the initial set of observables". (The wordings disagree in letter, and the construction can also coarsen, §III.C.)
- §II, optimality (cited from Shalizi & Crutchfield 2001, not proved here): "the causal states form the coarsest possible prescient partition"; they are "the unique prescient states of minimal statistical complexity". The causal-state series "is a Markov process".
- §III.A, observables already causal: "the statistical complexity is just the amount of information about the microstate that is contained in the macrovariables" (Cµ = I[Q; S]). Example: P, V, T of an ideal gas near equilibrium.
- §III.B, causal finer than observed: memory effects; adjoin a "minimal factor partition" Z with G = F·Z; every such Z has the same H[Z|S]. Examples: ferromagnetic hysteresis (field history, or field plus magnetization), chaotic jets. §III.B.1: spin glasses, "An Apparent Counterexample"; the remedy is to take "as one's macrovariables the occupancy probabilities of the metastable local minima".
- §III.C, causal coarser than observed: irrelevant variables; "unphysical" distinctions (nematic director, n = −n); unpredictable variables that "wash out" (a litre of gas observed yearly: G becomes trivial).
- §III.D: "In the causal states we have arrived, so to speak, at objective explanations of subjective quantities." Markov macrostates carry a Gibbs distribution over sequences without assuming equilibrium.
- §IV: "the Markov property does not generally survive coarsening the states", but a coarse measurement can be its own causal states: "We then have two levels of description, and can give a coherent causal account at each level."
- §IV.A, argon (numbers from Shalizi 2001 thesis §11.2.3, not derived here): macro entropy 33.3 bits, hµ 4.4 bits per ms, E = 28.9; micro Cµ = 6.6·10^20 bits, E = 3.3·10^20 at 1 ns. Efficiency 0.87 vs 0.5. "This leads us to define a relation of 'emergence' between two sets of causal variables if (1) one is a coarse-graining of the other and (2) the coarse-grained variables can be predicted more efficiently."
- §IV.B: thermodynamic and hydrodynamic descriptions "coexist, because they are intended to answer different questions — not because one is more objective than the other." Local causal states form a Markov random field (fn. 6: "Whether they always form a Markov random field is currently an open question"); vortex lines read as local causal states: "if what we find doesn't look Gibbsian, it means we can do better."
- §IV.C: CA and lattice-gas modelling as tacit practice: "throw away as much detail as possible, while retaining information relevant to certain aspects of the large-scale dynamics".
- §V, not explained: why good macrovariables are extensive, derivatives of potentials, reusable (temperature); why a stochastic treatment is legitimate (they point to ergodic theory, not MaxEnt).
- §VI: "for every question we ask It, Nature has a definite answer; but Nature has no preferred questions."

## Assumptions

- Microdynamics q_{t+1} = Tq_t Markov on Γ (possibly stochastic), "no hidden variables"; discrete time.
- Observations exact and noiseless (fn. 2 waives the realistic case).
- Stationary or conditionally stationary observed process; conditional laws known exactly (reconstruction from data deferred to Shalizi et al. 2002).
- Stochastic treatment of coarse observations simply assumed (§V).

## Concepts

causal state; causal equivalence; prescient partition; statistical complexity Cµ; predictive information E; entropy rate hµ; predictive efficiency E/Cµ; emergence vs submergence; observed partition F and causal partition G; minimal factor partition; Salmon's statistical relevance basis; local causal states; levels of description.

## Verdict on the exchange's characterization

- A17 §11: causal states group histories "according to whether they imply the same probability distribution over possible futures. Shalizi and Moore developed an influential connection between such predictive states and the definition of macrostates." Accurate.
- A17's gloss just before, "Group together microscopic states that have equivalent... future consequences", is looser: the paper groups observation histories, not microstates, and starts from a chosen observable. The microstate is its own causal state (§IV.A); the grouping has content only relative to f.
- LIT-2996's summary, "fixed by the dynamics rather than by the observer": wrong as stated. The thesis is that they are "both": the observables are the observer's, the refinement the dynamics'. Should be corrected.
- LIT-2996's status note, "the coarse-grainings under which dynamics close": fair if "close" means the macro process is Markov in its own past. It is not closure relative to the micro past (informational closure, THEORY-820); the paper never compares the two.

## Bearing on named codes

- TERM-062 (causal state, relative to a target): supports. The paper uses the ε-machine case (the observed process's own pasts for its own future, §II) and adds the macrostate reading. Early statement of the target-relativity the term builds in: "A different set of initial variables will, generally, lead to a different set of causal states" (§VI).
- TERM-140 (sloppy): background only. No Fisher information or parameter spectra. Contrast: S&M reduce states by prediction, not parameters by sensitivity.
- CLAIM-820 (parameter vs behavioural complexity): parallel, in information terms. Micro Cµ 6.6·10^20 bits against a 33-bit macrostate predicted more efficiently (§IV.A); "Nature has no preferred questions" (§VI). Supports its clause 3 (simplicity as a response to observation) by another mechanism, state coarse-graining rather than stiff parameter combinations. No bearing on clause 1 (fitting).
- QUESTION-517 (do effective dimensions agree?): leaves open; supplies one datum on the predictive-state side. The paper reports entropies (Cµ), not a dimension, and they move with observation and time step: efficiency "essentially one" for macrostates at matched resolution, "essentially zero" for microstates at the macro time-scale (§IV.A). Fits CLAIM-825's "a function of resolution, not a number". No comparison with Fisher or RG counts.
- CLAIM-401 (A17 §9 is coarser than its split, per curation 2026/11/21/180128): qualifies. S&M fuse predictive sufficiency (prescience) and memory closure (Markov) in one criterion; for the observed process's own causal states the two coincide by construction (§II), relative to one chosen projection (f), consistent with CLAIM-401's "memory relative to a chosen projection".

## Recheck (held entries the first search missed)

- curation.d/2026/10/29/231831.md, "Named by the readings, not registered": lists "Shalizi & Moore 2003, 'What is a macrostate?'". Same work, now LIT-2996.
- NOTE-791 (Barnett & Seth, dynamical independence) l.203 and NOTE-978 (Crutchfield & Shalizi, thermodynamic depth) l.202: name Shalizi and Moore's causal states as a neighbour. Contrast: S&M condition on the macro past, dynamical independence on the micro past (NOTE-978 already says so).
- NOTE-935 (Seth, Granger emergence) l.136: compares itself with "Shalizi and Moore's predictive efficiency". Parallel: rival operationalizations of emergence. The record holds no entry for S&M's E/Cµ definition (grep for E/Cµ and "predictive efficiency" finds only this and NOTE-416's different, Still et al. sense). Possible gap.
- THEORY-257 (Proposed; dynamical independence "fixes emergent macroscopic variables by the dynamics rather than by a chosen query"): qualifies/contrast. For S&M the dynamics fix macrostates only given a query, the observables (§VI).
- THEORY-820 (informational closure as ε-machine = υ-machine): contrast; S&M's macrostates are the observed process's ε-machine only, with no υ-machine comparison.
- THEORY-756 (causal states the coarsest prescient partition, least entropy): supports; the same Shalizi–Crutchfield 2001 result restated in §II.
- CLAIM-152, CLAIM-348, SYNTHESIS-075 (adequacy relative to a target): support. §IV.B, the levels "coexist, because they are intended to answer different questions"; §VI.
- QUESTION-218 (unit as a function of the whole state, classes of histories): background; S&M's G is such a unit.
- TERM-068 (closure, which sense): S&M's sense is "the macro process is Markov in its own past"; the filer may map it to one of its senses.

## Limitations

- Mostly argument and examples. The theorems are cited (Shalizi & Crutchfield 2001) or elementary (§III.B's entropy identities). The argon numbers come from the thesis.
- My observation, not the paper's: §III says each causal state "corresponds to a region of phase space". That is well-defined if a microstate fixes its own past observations (deterministic, invertible T). For stochastic T, which the paper allows, a microstate does not fix its observation history, so G need not be a partition of Γ. Not addressed.
- §IV.B calls the hydrodynamic–thermodynamic relation "generally one of emergence", then says "Similarly, the hydrodynamic level itself emerges from the thermodynamic one", which by its own definition (coarse-graining plus higher efficiency) cannot hold both ways; likely a slip. Its "two points" also run to "Third".
- Noise-free observations; known conditional laws; the emergence verdict's time-scale dependence is acknowledged but not formalized.
- "Unique maximal" (abstract) vs "unique coarsest such refinement" (§I) vs a construction that may coarsen (§III.C): uniqueness is asserted, the characterization is loose.

## Candidate THEORY

Shalizi and Moore propose that, for a chosen set of observables of a system with Markov microdynamics, the macrostates are the causal states of the observed process, the coarsest partition of observation histories that predicts the observables' future as well as the whole history does and whose own dynamics is therefore Markov, so that which observables to start from is the observer's choice and the partition reached from them is fixed by the dynamics; and they define one causal description as emergent from another when it is a coarse-graining of it and is predicted with higher efficiency E/Cµ, arguing both through examples (argon fluctuations, hysteresis, spin glasses, the nematic director, hydrodynamics) rather than new theorems.

promote_when: an independent source, or a worked model in the record, takes a stated observation function on a stated Markov microdynamics, computes the causal states of the observed process, shows they are Markov and recover (or knowingly refine or coarsen) the system's accepted macrostates, and shows the E/Cµ comparison ranks that coarse-graining above the micro description.

Tags: keep complex-systems, thermodynamics; the filer may check luria.yaml for an information-theory or emergence topic.

No instruction for machine-learning practice.
