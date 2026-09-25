---
number: 15
status: Read
formerly:
- NOTE-tmpgpyfe
paper: LIT-008
title: 'Periodic vehicle routing and facility location for waste collection'
version: 2
history:
- version: 2
  date: '2026-09-25'
  note: >-
    Read in full (Full text of arXiv:2504.10648v1 (14 Apr 2025, math.OC), 35
    pp.: abstract, §1–§7, acknowledgements, declarations, Appendix A (the
    i.12.1 chromosome, Tables A1–A2, Figs. A1–A2) and the reference list.
    Text came from raw4/2504.10648.pdf via PyMuPDF. Figures 1–3 and A1–A2
    are plots or maps, so I read their captions and the prose around them,
    not the images. The main-effects plots (Figs. 2–3) are therefore
    unverified beyond what the text says about them. I did not compare
    against the journal version (Annals of Operations Research 350,
    979–1015, DOI 10.1007/s10479-025-06626-4). I did not open the GitHub
    instances.). Upgraded from `Skimmed` to `Read`: the claims table,
    assumptions and results are new, and the skim is corrected where the
    full text disagreed.
date: '2026-09-25'
summary: >-
  The paper couples bin-capacity choice with weekly periodic capacitated
  routing (Sunday off, cyclic). Service time depends on the chosen bin
  combination, which gives an MIQP; a Glover linearisation turns it into a
  MILP. It solves both with Gurobi 10 for 8 h, and also with a binary-mask
  + permutation GA (CX 0.8, EM 0.05, pop 100, 10,000 generations). On five
  12-point instances Gurobi stops at 26–32% optimality gaps. The
  best-of-30 GA overall cost is on average −0.08% vs the MILP incumbent
  and +1.70% vs the MIQP incumbent; the GA mean or median is +3.75% and
  +5.61%. The GA routes better (−5.75% and −5.74% routing cost) but buys
  much more bin capacity (+19.88% and +22.59%). On 40–163-point Bahía
  Blanca instances the GA returns feasible solutions in 0.72–5.58 h per
  run, with no bound to compare against.
---

# NOTE-015: Periodic vehicle routing and facility location for waste collection

## Contribution

The paper states and solves an integrated bin-allocation plus periodic capacitated vehicle-routing problem for community-bin municipal solid-waste collection. Two things separate it from Hemmelmayr et al. 2014, Mahéo et al. 2020/2023 and Gläser & Stücken 2021. First, visit frequencies are not chosen from predefined patterns: any weekly visit pattern is allowed as long as no collection point overflows its chosen bin combination. Second, service time depends on the bins installed (§2.1, §3). It gives an MIQP and a Glover-linearised MILP (§4.1), a GA with a two-chromosome encoding (a binary visit mask and daily permutations, §4.2), a nonparametric operator-tuning study (§5.2), and public instances derived from Bahía Blanca field data, up to 163 collection points (§5.1).

## Key insight

Once visit frequency is free, bin capacity is no longer an independent decision. The cheapest feasible bin at point i is simply the smallest combination with CAP_b ≥ w_i^max, where w_i^max is set by the longest gap between visits (Eqs. 2c, 2k–2m). The GA exploits this. It evolves only *when* and *in what order* points are visited, and derives the bins in the decoder (App. A). That also explains its signature trade-off: it finds shorter routes by visiting less often, which forces larger bins. It wins on routing cost and loses on bin cost against the exact incumbents (Table 6).

## Assumptions

- **Cost model.** The objective is weekly cost: Σ_b CIN_b Σ_i n_bi + C_CV Σ_t Σ_v TT_vt (Eq. 2). Bin cost is purchase plus 5%/yr maintenance amortised over a 10-year life, per week (Table 1: US$0.78 for the 1.1 m³ combination and US$1.56 for every other combination). C_CV = US$0.5764/min and unloading time T_U = 8 min.
- **Waste generation is deterministic and constant.** W_i m³/day at each point. Collection happens at the end of the day. Accumulation follows w_it = W_i + w_i(t−1)(1 − visited_{t−1}), cyclic over the week (Eqs. 2k–2l).
- **Routing.** Each vehicle makes at most one route per day (2g), and the fleet is homogeneous. Fleet size n_V = ⌈n_I/10⌉ (Eq. 7), and the shift length T_L is a formula in total pairwise travel time (Eq. 8). Both are set so the instances are not trivial, not from the real fleet. Vehicle capacity Q is 12 m³ for n = 12 and 21 m³ otherwise. There is no collection on Sunday (T′). Subtours are eliminated with load-flow constraints (2i–2j).
- **Bins.** Eight predefined combinations (Table 1, from Mahéo et al. 2023) with capacities of 1.1–5.6 m³ and service times of 0.66–2.10 min; one combination per point (2b). Bin locations are fixed: this is a capacity choice at given sites, not a location choice.
- **Instances.** The 12–120-point instances are random subsets of the 163-point Bahía Blanca instance (§5.1). There are five instances at n = 12 and one at each larger size.
- **GA constraint handling.** Permutations guarantee constraints (2a), (2d) and (2f). Mask repair (adding visits) enforces (2b), (2c) and (2i)–(2m). Fleet-size and shift-length violations (2g, 2h) are penalised in the fitness with λ = 100 and γ = 1000 (Eq. 6), where λ multiplies a normalised excess route count. λ is raised to 500–10,000 on larger instances.
- **Budget matching.** The time budget is 8 h for each exact solve, against 30 GA runs of ≈903–927 s each (≈7.5–7.7 h total) at n = 12 (Table 4). Only the n = 12 instances get an exact comparison.

## Key results

- **Tuning (§5.2, Tables 2–3).** Kruskal–Wallis is significant for all four factors, on cost (p < 2.2e−16 for crossover operator and rate; 0.0005 for mutation operator and rate) and on runtime. The best cost treatment is CX / 0.8 / EM / 0.05, statistically tied with CX / 0.8 / IM / 0.05. CX2 is fastest, followed by CX, but CX has significantly better cost.
- **GA on n = 12 (Table 4, 30 runs, 10,000 generations).** Min / median / mean overall cost in US$: i.12.1 194.6 / 205.1 / 205.1; i.12.2 198.5 / 203.8 / 204.2; i.12.3 196.5 / 206.2 / 206.2; i.12.4 187.5 / 195.8 / 195.6; i.12.5 192.8 / 196.0 / 196.7.
- **Exact on n = 12 (Table 5, 8 h Gurobi).** MILP overall cost 189.58–202.82 with gaps of 29.06–32.15%. MIQP 185.01–202.10 with gaps of 26.15–32.34%. Neither formulation dominates: the MIQP is cheaper on 3 of 5 instances (i.12.1, i.12.4, i.12.5) and worse on i.12.2 (191.21 vs 189.75) and i.12.3 (202.10 vs 196.65).
- **Comparison (Table 6; mean over the five instances of (C_GA − C_exact)/C_exact):**

  | | bin cost | routing cost | overall cost |
  |---|---|---|---|
  | GA best vs MILP | +19.88% | −5.75% | −0.08% |
  | GA mean/median vs MILP | +18.65% | −0.36% | +3.75% |
  | GA best vs MIQP | +22.59% | −5.74% | +1.70% |
  | GA mean/median vs MIQP | +21.24% | +1.37% | +5.61% |

- **Large instances (Table 7).** Min / mean overall cost (US$) and mean runtime per run: i.40.1 527 / 543, 0.72 h; i.80.1 1077 / 1106, 2.84 h; i.120.1 1658 / 1730, 4.09 h; i.163.1 2358 / 2395, 5.58 h. All 30 runs were feasible on every instance. There is no lower bound, alternative method or current-practice baseline.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | The integrated problem with free visit frequency and bin-dependent service time is formalised as the MIQP of Eqs. 1–2m, and linearised exactly as a MILP via Eqs. 3a–5 | strong | Formulation §3–§4.1 (Glover 1975 product linearisation; BigM = max CAP_b) |
| C2 | CX crossover at rate 0.8 with EM mutation at 0.05 is the best GA configuration for this problem | moderate | 108-treatment factorial × 30 runs, Kruskal–Wallis plus multiple comparisons (Tables 2–3), on a single 12-point instance. EM and IM are statistically tied |
| C3 | The GA "is able to match the results of exact solvers on small instances" (abstract) | weak | Five 12-point instances. Best-of-30 is within −4% to +5% of Gurobi incumbents, whose own gaps are 26–32%. Tuned on one of the five instances |
| C4 | The GA builds better routes but chooses costlier bins than the exact models | moderate | Table 6: routing −5.75% / −5.74% (best), with one MILP exception (+0.76% on i.12.2); bins +19.88% / +22.59% |
| C5 | The GA "consistently" beats the MILP on routing cost | weak | Contradicted by Table 6, i.12.2 (+0.76%) |
| C6 | The GA obtains feasible solutions on realistic instances (up to 163 points) in reasonable time | moderate | All 30 runs feasible on four instances (Table 7). Solution quality there is unmeasured |
| C7 | GA runtime grows linearly in the number of collection points, with slope ≈0.035 | weak | Four data points with different generation counts and λ values. Units not given |
| C8 | The size of the 163-point instance is "considerable" relative to prior integrated models (e.g. ≤ 50 points in Hemmelmayr et al. 2017; ≤ 7 in Mahéo et al. 2023) | moderate | Literature review (§2) |

## Method

- **Exact.** The MIQP and MILP are coded in Pyomo and solved with Gurobi v10.0.2 under an 8 h limit. The bilinear terms in the accumulation constraints (2k–2l) are removed by BigM constraints (3a–3c), and the x·n product in TT_vt by z_ibjvt with three linking inequalities (4a–4c).
- **GA (Algorithm 1).** Each individual is (pop, mask). pop holds one permutation of all n_I points per day. mask is a binary n_I × n_T matrix of visit decisions, with Sundays fixed to 0.
  - *Decoding.* w_it and w_i^max are computed from the mask, and the smallest adequate bin combination is chosen. Each day's permutation is filtered by the mask, and a new route starts whenever the next point's load would exceed Q (App. A).
  - *Operators.* Tournament selection of size 2. The binary part uses two-point crossover with uniform mutation at rate 1/n_I. The permutation part uses PMX, OX, CX or CX2 crossover and EM, IM or INM mutation.
  - *Settings.* Elitism of 2, population 100. Runs use 1,000 generations for tuning, 10,000 for n = 12 and n = 40, and 20,000 for n ≥ 80.
- **Statistics.** Shapiro–Wilk decides between a t-interval on the mean and a Wilcoxon interval on the pseudomedian (Tables 4 and 7).

## Concepts

- **Collection point** — a predefined urban site where a bin combination is installed. Locations are given; capacity is decided.
- **Bin combination** — one of 8 admissible sets of commercial bins at a point, with capacity CAP_b, service time S_b and weekly cost CIN_b (Table 1).
- **PCVRP** — the periodic capacitated VRP (Beltrami & Bodin 1974). Here the visit pattern per point is a free decision variable, not chosen from a menu.
- **w_i^max** — the maximum end-of-day accumulation at point i over the cyclic week. It sets the required bin capacity (2c, 2m).
- **Optimality gap** — |overall cost − Gurobi dual bound| / |overall cost| (Eq. 9).
- **Mixed GA** — this paper's name for a GA whose individual pairs a permutation chromosome with a binary mask.

## Connections

The paper builds directly on Mahéo, Rossit & Kilby 2020/2023: the bin combinations and the Benders-based integrated model with predefined frequency alternatives. It also continues the authors' own conference-stage model (Rossit et al. 2024), which it calls "substantially different". It positions itself against Hemmelmayr et al. 2014 (the first integrated bin-allocation/routing model, solved with LNS) and 2017 (periodic location-routing for recycling, ≤ 50 points); Cubillos & Wøhlk 2020 (single-day, uncapacitated vehicle); Gläser & Stücken 2021 (predefined frequencies, adaptive LNS); and Roy et al. 2022, Han et al. 2024 and Niu et al. 2024, which lack periodic scheduling or capacity decisions. It frames the problem as a variant of inventory routing (Archetti & Ljubić 2022) and a capacitated facility location problem (Cornuéjols et al. 1991).

## Bearing on the record

This paper carries nothing for ML practice. The GA has no learned component. Its operator tuning (a factorial design with Kruskal–Wallis tests) is ordinary metaheuristic parameter tuning, and even as that it is a cautionary example: it tunes on an evaluation instance. It supports or contradicts no THEORY document, and nothing belongs in the Anthology of the SOTA. It sits in the catch-all record as an operations-research reading on municipal waste logistics.

## Limitations

- **The abstract claims more than the body shows.** "match the results of exact solvers" is measured against incumbents with ~30% gaps. It says nothing about distance from optimum for either method, and the GA's typical run (mean/median) is 3.75–5.61% worse.
- **The evidence is thin at small scale.** Five instances of 12 points, and one instance per larger size. The smaller instances are random subsets of the one real instance, so there is no independent test set. Tuning used i.12.1, which is also a test instance.
- **The large instances have no reference.** No lower bound, no alternative heuristic, and no comparison with Bahía Blanca's current practice. λ was changed per instance and the generation budgets differ, so the runtime-scaling claim is confounded.
- **The modelling simplifications are the paper's own choices.** Deterministic, constant daily generation; one route per vehicle per day; a synthetic fleet size and shift length (Eqs. 7–8) rather than real operational parameters; fixed candidate locations.
- **The GA's bin choice is derived, not searched.** Repair only adds visits. A solution that would be cheaper with *fewer* visits and bigger bins at some points, or vice versa, can be reached only through mask mutations. This may explain the systematic bin-cost deficit, but the paper does not analyse it.
- **There are textual slips.** The appendix says two routes run "on Mondays, Thursdays, Fridays and Saturdays" and one "on Wednesday and Thursday". Table A2 shows two routes Mon/Tue/Fri/Sat and one Wed/Thu. §6 misreports the bin-cost percentage direction (see corrections). "AG" appears for GA in places (§2.1, §6).

## Open questions

- How far from optimal are any of these solutions? Valid cuts or a decomposition that closes the ~30% gaps at n = 12 would give a real yardstick; the authors list valid cuts as future work.
- Would a decoder that also searches bin capacity (e.g. mutating toward fewer visits with larger bins) remove the GA's ~20% bin-cost deficit?
- Does the tuned configuration hold up on instances not used for tuning, or on other cities?
- How does the method compare, on the 40–163-point instances, with an adaptive LNS of the Hemmelmayr / Gläser & Stücken type, the established baseline for this problem family?
- The authors propose a bi-objective treatment separating installation and routing cost. Would it expose a Pareto front on which the GA and exact solutions simply sit at different points?

## Corrections to the seeded skim

- The dossier's §-map is accurate, but it leaves out the fact that most limits what "competitive" means. Gurobi's incumbents on all five 12-point instances carry optimality gaps of 29.06–32.15% (MILP) and 26.15–32.34% (MIQP) after 8 h (Table 5). The GA is being compared to feasible solutions whose distance from optimum is unknown, and both they and the GA may be far from optimal.
- The dossier says the exact models were "up to about 26–29% cheaper on bin cost". Table 6 reports the GA's excess relative to the exact solution, (C_GA − C_exact)/C_exact: up to +25.62% vs MILP and +28.78% vs MIQP (means +19.88% and +22.59%). So the exact bin costs are up to ≈20% and ≈22% *cheaper* than the GA's, not 26–29%. The paper itself makes the same slip ("obtaining up to 28.78% smaller cost", §6).
- The dossier says the best GA solution has "about 5.7% lower routing cost than both MILP and MIQP". The average figures are right (−5.75% and −5.74%), but the paper's word "consistently" (vs MILP) is contradicted by its own Table 6: on i.12.2 the GA's best routing cost is +0.76% *worse* than the MILP's. Against the MIQP it is better on all five instances.
- The dossier says "MIQP averages about 1.7% cheaper than the GA". That is true only for the GA's *best of 30 runs*. Against the GA's mean or median, the MIQP is 5.61% cheaper and the MILP 3.75% cheaper. Best-of-30 against the MILP is a wash (−0.08%; the GA wins on 3 of 5 instances).
- The dossier leaves out that the operator design of experiments (4×3³ = 108 treatments × 30 runs = 3,240 runs, §5.2) was run on i.12.1, one of the five instances then used to compare the GA with Gurobi. It also leaves out that the Kruskal–Wallis follow-up does not separate EM from IM (both "best"), so choosing EM is a tie-break.
- The dossier's linear runtime claim ("slope ≈ 0.035") repeats the paper, but the paper gives no units and the growth is confounded. The four large instances used different generation counts (10,000 for i.40.1, 20,000 for the rest) and different penalty weights λ (500, 1,000, 5,000, 10,000). The mean runtimes (0.72, 2.84, 4.09, 5.58 h at n = 40, 80, 120, 163) give ≈0.04 h per point end to end, and fitting four points does not establish linearity.
