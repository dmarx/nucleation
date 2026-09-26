---
number: 40
status: Read
formerly:
- NOTE-tmp87h10
paper: LIT-075
title: 'Dreyer et al. 2024, ants vs humans on a piano-movers puzzle'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (full text of the open-access version of record (Europe PMC
    XML of PMC11725855, saved as rawC4/c31.txt): significance statement,
    abstract, every Results section, "Comparing Ants and Humans", and all of
    Materials and Methods, including Eqs. 1–3 and the
    statistical-information paragraph. I also read the full 26-page SI
    Appendix (rawC4/c31_si.pdf, extracted to c31_si.txt from the Europe PMC
    supplementary bundle). That covers Notes 1–10, Tables S1–S5, all figure
    captions S1–S9, and the SI reference list. I viewed the Fig. 2 and Fig.
    4 images themselves (rawC4/pnas.2414274121fig02.jpg, fig04.jpg). I did
    not watch Movies S1–S7 or view the SI figure images; only their captions
    were read.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  On one T-shaped piano-movers puzzle, the CDF of solved attempts against
  normalized path length shows large ant groups (≈80 carriers, n=28) well
  ahead of small groups (≈7, n=48) and a 3-run composite single-ant
  series. An agent-based model with group-size-independent rules
  reproduces the difference. Human groups of 6–26 barred from talking or
  gesturing needed more attempted state transitions than single people
  (−32% relative to the individuals' median; n=48 groups vs 61
  individuals), and talking groups were only slightly better (+7%). No
  significance test is reported anywhere: "significantly" rests on
  overlapping-or-not ±1 SE bands.
---

<!-- inactive-ok-file: LIT-046 — Proposed by its close reading; named in Connections -->

# NOTE-040: Dreyer et al. 2024, ants vs humans on a piano-movers puzzle

## Contribution

- A physical piano-movers puzzle (a T-shaped load, three chambers, two slits) built at five scales (ant small and large, human small, medium and large). The ratio of body size to load size is held roughly constant, and human group members are restricted to pulling on assigned handles. This gives a same-task comparison across group sizes and across species (Fig. 1; Table S1).
- A shared performance metric: path length in the 3-D configuration space (x, y, r_av·θ), normalized by the corridor width d_cor (Eq. 2). For humans, a second metric counts attempted state transitions on a hand-built state graph (Table S3).
- For ants: evidence that group size turns persistence into effective search. Large loads keep speed and heading through wall contact and slide along walls (Fig. 3; SI Note 3). An existing agent-based transport model (informed/uninformed pullers and lifters; SI Note 1) reproduces the performance gap, with rules that do not depend on group size.
- For humans: a descriptive account of each condition, with one fitted parameter for the restricted groups.
  - Individuals behave like graph search, and 91 ± 1% of their transitions are consistent with DFS.
  - Groups barred from speaking choose the "greedy" edge more often, which is modelled as a majority vote with greediness P = 0.2.
  - Talking groups resemble a typical individual.

## Key insight

Whether grouping helps depends on how much individual cognition has to be aggregated. Ants bring almost none to this puzzle, so aggregation is purely mechanical. Mechanical alignment grows with group size, and a persistent collective heading acts like short-term memory, giving a wall-following heuristic. Individual humans bring a rich but idiosyncratic plan. Aggregating those plans without speech collapses onto the most obvious move, and with speech it roughly recovers one member's plan, not the best member's.

## Assumptions

- **Scale equivalence.** Normalizing path length by d_cor and rotation by r_av makes puzzles of different physical size comparable. Two known breaks:
  - Ant body length (~3 mm) does not scale, which the paper handles with a "skirt" finite-size correction in simulation (Table S2; Fig. S3).
  - Walking speed does not scale either, which the paper handles with per-scale smoothing windows (SI Note 8).
- **Restricted-communication humans are the fair analogue of ants.** The argument is that ants' pheromone trails are "practically useless" for load geometry here, leaving force-mediated communication. This is asserted from prior work (ref. 36) and is not measured in these experiments.
- **The human state graph (Fig. 1C; Table S3) is the representation people actually use.** Evidence: after pruning, people do not re-enter state b regardless of where in state a they return (SI Note 5; Fig. S6d).
- **Unsuccessful ant attempts.**
  - Small and large groups were stopped at about 30 min and counted as failures.
  - Single-ant runs were not stopped, and 2 of 3 spanned several days with the load re-placed, so they are "composite experiments".
  - The CDF construction drops unsuccessful attempts whose path length is below the largest successful one (Methods, "Cumulative Distribution Function").
- **Force meters.** Integrated luggage-scale force meters sampling at 2 Hz stand in for pulling forces. Only 8 and 5 experiments had reliable force data.

## Key results

- **Ant scaling (Fig. 2A).**
  - Large groups (n = 28) reach roughly 90–100% success by about 400 d_cor.
  - Small groups (n = 48) reach about 50% by 400 d_cor.
  - Single ants: one point at about 33% success near 220 d_cor, with an error bar spanning about 6–60% (n = 3), read off the figure.
  - The finite-size-corrected simulations overlay the experimental CDFs for both sizes.
- **Humans vs ants (Fig. 2A).** Single humans reach 100% within about 50 d_cor, against a minimum of about 10. The best ant runs overlap the worst human runs in about the 25–55 d_cor band.
- **Humans across conditions (Fig. 2B; SI Note 7).**
  - Restricted-communication groups (n = 48) are shifted right, with a change of −32% vs the individuals' median.
  - Communicating groups (n = 43) are +7%.
  - Medium and large groups behave alike (Fig. S4b).
- **Mechanism, ants.**
  - After a collision, large groups keep a higher fraction of their speed and turn less (Fig. S5a,b; 34/45 and 96/44 experimental collisions for small/large).
  - In simulation, alignment above M_dis = 0.3 persists 5.9 ± 0.4 s and 4.8 d_cor for large groups, vs 0.7 s and 1.9 d_cor for small groups in confinement (Table S4).
- **Mechanism, humans.**
  - Restricted groups start moving within about 1 s regardless of which option they take. Communicating groups take several seconds for greedy and tens of seconds for indirect moves (Fig. 4D; log scale).
  - Communicating groups stop 6.9 ± 0.7 times per attempt and restricted groups 4.3 ± 0.6 (Fig. S6e).
  - The talking-group gain comes from leaving dead-end state b: 91% of groups return to a after trying b→e, against 38% of individuals, and this accounts for 62% of the reduction in transitions (SI Note 7).

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Large ant groups solve the puzzle with much shorter normalized paths than small groups or single ants | strong (large vs small), weak (vs single ants, n=3 composite runs) | Fig. 2A CDFs with ±1 SE bands; no test statistic |
| C2 | Their advantage comes from collective persistence (alignment maintained through wall contacts), with ant rules independent of group size | moderate | collision statistics Fig. S5a,b; order parameter from simulation only (Table S4, Fig. S9); model–data CDF agreement Fig. 2A. The simulated carrier numbers fall short of the calibration targets (Table S2 vs S5) |
| C3 | This persistence amounts to "short-term collective memory", an emergent cognitive faculty | weak | interpretive relabelling of mechanical persistence (p. "Ant Solvers"; "analogous to ordered spins") |
| C4 | Human individuals search a mentally reduced graph of states, depth-first, pruning failed edges with long-term memory | moderate | 91 ± 1% of transitions consistent with DFS (a permissive definition that lets solvers pre-exclude edges); no return to state b (Fig. S7a) |
| C5 | Human groups without speech or gesture perform worse than individuals | moderate–strong | Fig. 2B CDFs, −32% (SI Note 7); n = 48 groups vs 61 individuals; no significance test |
| C6 | …because they converge on the greedy option through a fast one-shot majority vote with greediness P = 0.2 | weak–moderate | one hand-tuned parameter, 2,000 simulated groups per fork, "reasonably good" fit in 9 of 10 forks (Fig. 4C); the vote is among a random quarter at 3 of 5 forks; no alternative model compared |
| C7 | Talking groups follow a randomly chosen member and so match a typical individual, only marginally better | weak | decision probabilities resemble individuals' (Fig. 4C, large error bars); leader-following is from "personal observations" only, since voices could not be recorded (SI Note 6) |
| C8 | Following a random leader is "strictly superior" to majority vote when most individual choices are wrong | weak | 200-run stylized simulation (SI Note 10, Fig. S4c), not a proof |
| C9 | Simple minds scale easily while complex minds need rich communication to cooperate (abstract's closing line) | weak | generalization from one puzzle, one ant species and one human population |

## Concepts

- **solver** — any of the eight experimental conditions (single ant, small ant group, large ant group, single person, medium/large human group × communicating/restricted), treated as one problem-solving entity.
- **configuration space / states** — the permissible (x, y, r_av·θ) poses of the load, partitioned by hand into states a–h plus "transition regions", meaning parts of a state next to a geometrically adjacent but disconnected state (Table S3).
- **greedy option** — at a decision fork, the target that would push the load furthest toward the exit. The alternative is the **indirect option**.
- **order parameter M** — the mean over pullers of cos(pulling direction, local load velocity at the attachment site) (Eq. 1). It is measured only in simulation.
- **finite-size correction ("skirt")** — an impenetrable rim of 10% of an ant's length added to simulated loads to stand in for ant bodies.

## Connections

- The paper builds on the same group's model of ant cooperative transport, in which transiently informed leaders are followed by uninformed followers who align to the load's motion (Gelblum et al. 2015; Feinerman et al. 2018, Nat. Phys.). Here that model is re-parameterized for confinement, and its earlier rotation-inhibition rule is dropped (SI Note 1).
- The human-group analysis draws on the social-decision-scheme and "demonstrability" literature (Laughlin & Ellis 1986; Lorge & Solomon 1955) and on groupthink and pluralistic ignorance, but none of it is tested formally.
- In this record it sits beside [LIT-046](../literature.d/LIT-046.md) (Pilgrim et al.), which uses cooperative transport as an example of coordination constraints. This paper is an empirical case of that framework's "more resources, but coordination costs" trade-off.

## Bearing on the record

There is no instruction for ML practice here. The loose analogy is to ensemble or multi-agent aggregation, where majority vote over correlated, biased voters can underperform a single random member. The paper's only evidence for that is a stylized simulation (C8), which is not a basis for any anthology practice. No THEORY document in this record is supported or contradicted by name.

## Limitations

- **No inferential statistics.** The Methods give mean ± 1 SE, and the CDF error is sqrt(p(1−p)/n′). Every "significantly" in the text is unaccompanied by a test, and no effect is controlled for group composition, age (children aged 10 and up took part), or repeat exposure.
- **Unequal human metrics.** Human conditions are compared on attempted state transitions, and ants vs humans on path length. The +7%/−32% figures use one particular summary: the group mean vs the individuals' median.
- **Single ants.** n = 3 composite, multi-day runs. The single-ant claim is really "small groups ≈ single ants".
- **The mechanism models are post hoc.**
  - Greediness P is tuned by eye.
  - The leader-following account rests on unrecorded personal observation.
  - The "memory" framing is a relabelling of persistence.
- **Scope.** One ant species (*P. longicornis*), one puzzle geometry, and one human population, recruited in Israel through the Weizmann Institute. The authors' evolutionary "two trajectories" framing and the robotics implications are speculative (Discussion).
- **Calibration.** The simulated large-group carrier count (50.8) sits well below both the experiment (79.9) and the stated equilibrium target (64.6). It is unexplained.

## Open questions

- Would a formal model comparison (majority vote vs random dictator vs weighted confidence), fitted by likelihood to per-fork choices, pick the paper's mechanisms? The per-fork counts would allow it.
- Does the human deficit under restriction persist with a less spatially local assignment of members to handles? The paper's own "locality" hypothesis (p. "Human Solvers") predicts it would shrink.
- Does ant performance keep improving beyond about 80 carriers, or saturate? Only two group sizes were run.

## Corrections to the seeded skim

- Talking groups. The dossier says human groups "do no better than individuals when they can talk". The paper says communicating groups "marginally outperform individuals" (Fig. 2B), quantified in SI Note 7 as +7%, against −32% for the restricted groups. Both are measured as the distance of the group mean from the individuals' 50th percentile. The dossier's sentence is closer to the paper's own framing ("perform similarly to individuals", p. "Human Solvers") than to its figure, but it drops a stated effect.
- The majority-vote model is not the whole group. The dossier describes a "one-shot majority-vote model". In the simulation (Methods, "Simulations of Human Decisions") the vote covers the whole group only at forks 1 and 3. At forks 2, 4 and 5 it is taken among "a randomly chosen quarter of all agents", because only people on one side of the T can pull toward either option (SI Fig. S7c). P was set "by adjusting only parameter P". There is no fitting criterion or goodness-of-fit number, and the fit is stated to be "reasonably good … in nine out of ten decision forks". The Methods sentence cites "Fig. 4E" for the fit; it is Fig. 4C.
- SI Note 10 does not bear the weight the main text gives it. The main text says following a random leader "is strictly superior to majority decisions" when most individual choices are wrong. SI Note 10 is a 200-run simulation of two stylized solvers (a random member's choice vs a majority of 20), shown as CDFs in Fig. S4c, with no proof and no test. The probabilities for the indirect option are also written "Pi − 1" where 1 − Pi is meant.
- The "35% more edges than its best individual" figure (main text; SI Note 9) is computed as (a_group − a_ind)/a_group, which is the fraction of the group's attempts that are excess, not "35% more" than the best individual. Measured against the individual, the excess is 1/(1 − 0.35) − 1 ≈ 54% if the averages behave. That is my arithmetic, and the paper does not report it.
- Simulated ant carrier numbers do not match the stated calibration. SI Note 1 says k_on was tuned to match the average carrier occupation, and Table S5 gives ⟨N_att⟩eq = 8.08 (small) and 64.62 (large). Table S2 reports simulated carrier numbers of 3.8 ± 1.7 (small) and 50.8 ± 8.6 (large). The experiments (Table S1) have 7.4 ± 3.0 and 79.9 ± 12.1. So the simulated large group carries about 64% as many ants as the real one, and the small group about half. The paper does not comment on this. (The damping threshold is also written N_0 in the text and N_max/5 in the code, SI p. 6.)
- Numbers the dossier lacks: 1,251 human participants in total; experiments with five ant colonies over 3 years; mean group sizes of 7.4–7.5 (medium) and 18.8–21.1 (large) people (Table S1); force data from only 8 communicating and 5 restricted experiments (Methods, "Statistical Information"); and all human attempts succeeded within 30 min.
