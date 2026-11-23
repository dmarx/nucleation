<!-- scratch/manuscripts/governance-of-possibility/analysis/README.md -->
# Analysis: regulation as the governance of possibility

This is the executed study behind A48 §9 of the manuscript. The draft stipulates
three regimes and asserts their outcomes. This study runs them, as
LEAD-tmpnblsf asks, extending LEAD-080's readiness simulator (CASE-315,
`scratch/studies/lead-080/`). From that study it reuses the peak-accounting
budget, the drill that holds the budget, the partial-rollover and CASE-200
rules, and seeding by `default_rng([base, i])`. Its code is not modified.

## Files

- `model.py` is the model: configurations, paths with per-step resource costs,
  budget rules, regimes, the stochastic contingency, imposed-contingency
  readiness (TERM-115's do(c)), the exact readiness of a path, the
  first-order-dominance classifier, and the novel-demand experiment. The
  docstring states the model.
- `study.py` runs the sweep and writes `results.json` (everything) and
  `results.md` (tables).
- `test_model.py` holds 21 tests.
- `results.json` and `results.md` are the outputs of the last run.

## Running it

From this directory:

    python3 -I study.py                                   # about 10 s
    python3 -I -m pytest -q -p no:cacheprovider test_model.py   # about 1 s

Seeds are fixed. Long run `s` draws its contingencies from
`default_rng([20261123, s, 0])` and its organization from three further streams
(edge completions, outside money, reserve lapse). Regimes on one seed
therefore share common random numbers: they see the same contingency
opportunities and, where their paths agree, the same step times.

## The model in brief

- **Configurations and paths.** A and B are each held at r = 1. The original
  path runs A → M → B with r(M) = 3, over two edges. The redesigned
  architecture adds a staged path A → S1 → S2 → B with r(S) = θ′, over three
  edges. Each edge completes with chance q = 0.5 per period and occupies the
  larger r of its two ends while it is crossed. A path's threshold is its
  peak, and an architecture's threshold is the least over its paths
  (CLAIM-571). The graph is symmetric, so the same paths lead back.
- **Budget rules.**
  - Peak: B′ = s (CLAIM-577).
  - Floor: B′ = max(s, F), a reserve of F − 1. It can lapse to the peak rule
    with a per-period hazard.
  - Carry: B′ = min(3, B̄ + ρ(B − s)) with B̄ = 1.5 and ρ = 1, CASE-200's rule
    with a cap.
- **Regimes.**

  | Regime | Path | Budget rule |
  |---|---|---|
  | I | original | peak |
  | II | original | floor 3 |
  | III-a | redesigned | peak |
  | III-b | redesigned | floor θ′ |
  | IV | redesigned | peak, with a drill each period at θ′ |
  | V | original | carry |

  Controls: II and III-b with a lapsing reserve (0.005 a period), and IV
  drilling every second period.
- **Contingency.** Each period, with chance p, demand switches to the other
  configuration. The organization takes the fastest affordable path. If none
  is affordable, outside money arrives after a geometric wait (chance g = 0.1
  a period). It raises the budget to the least threshold, the minimum outside
  money of CLAIM-577 step 4. A transition once started is funded to the end.
  A response later than the deadline τ costs L.
- **Costs.** A reserve costs c per unit of budget above holding per period.
  The upfront cost of redesign is reported as a break-even, not charged.
- **Output.** Output is 1 in a period with no contingency pending, and 0
  otherwise.
- **Novel demand (CLAIM-361).** After 50 quiet periods, holding A causes a harm
  that the specification does not name. A configuration C, also held at 1, is
  free of the harm. It is reached over A → N → C with r(N) = 2.5.
  - *Excise* never enters the demand into the specification.
  - *Revise* first reviews for 3 periods. Each review period occupies 0.5 (or
    0) above holding and is granted only if the budget allows. After the
    review, the new demand is met like a contingency.
  - The run is scored three ways: against the original specification D0, the
    organization's own current specification, and the true demands.

Choices that change the results are made openly. The staged path is slower
(three edges to two). Outside money buys the cheapest route, not the fastest.
The review uses the same capacity as transitions. All rates and costs are
invented.

## Run of record

`results.json` and `results.md` were produced on 2026-11-23 by `python3 -I
study.py` with the code as committed in 28a3708c1, and re-run by the
coordinator before committing: the outputs reproduced exactly except
`runtime_s`. The tests (`test_model.py`, 21; `test_speed_noise.py`, 3) pass.

## What it establishes (within the model)

1. **Present output is matched and future capacity is not.** Every regime
   produces 1.0000 per period before the first contingency, and does so in
   every period when there is no contingency at all (tested). The match is
   by construction: output does not depend on the budget. What the study
   establishes is the divergence after a contingency, not the match. Once
   contingencies arrive, overall output ranges from 0.76 (III-a) to 0.92
   (II).
2. **CLAIM-577 and CLAIM-tmpg8yl2 hold exactly.**
   - Under the peak rule the budget never rises.
   - One holding period forecloses every route whose threshold exceeds 1.
   - A redesigned route is kept exactly when θ′ ≤ 1.
   - A floor F keeps a route exactly when F ≥ its threshold.

   These are tested for θ′ ∈ {1, 1.25, 1.5, 2, 2.5, 3} and F from 1 to 3 in
   steps of 0.25. The draft's Regime III, "accessible transition capacity 2",
   needs a reserve of 1. Without it (III-a), redesign is lost like the
   original.
3. **Readiness steps; it does not grow smoothly with reserve.** Every reserve
   strictly between two path thresholds gives exactly the readiness of the
   reserve below it (identical under common random numbers). The only
   reserves worth considering are therefore the thresholds less holding:
   0, θ′ − 1 and 2.
4. **Under the peak rule, a drill is a reserve by another name.** IV's budget
   sits at θ′, its capacity cost equals III-b's (1.000 against 1.000), and its
   readiness curve is identical. What differs is robustness:
   - IV needs no commitment from the budget-setter, so a reserve that lapses
     does not touch it. Under lapse, II's R(6) falls from 0.89 to 0.75 and
     III-b's from 0.65 to 0.54.
   - IV breaks under anything that skips a drill. Drilling every second
     period loses the route after the first undrilled period (the negative
     control). In the novel-demand run, a review that crowds out the drill
     takes the route with it (B_end = 1 when there is no outside money).
5. **The ranking: readiness has a leader at every deadline, cost does not.** II (≡ V) is most ready at every deadline; what depends on the deadline is the order of the others and which regime is cheapest.
   - On readiness: II ≡ V dominate everything, and II dominates III-b ≡ IV.
     I and III-b cross between τ = 2 and τ = 3. At τ = 2, I with outside money
     (0.025) beats III-b (0), because the staged route cannot finish in fewer
     than three periods.
   - III-a is dominated even by I. The minimum outside money buys the cheaper,
     slower route, so on these assumptions redesign without a reserve is worse
     than no redesign.
   - On long-run cost (p = 0.02, L = 50, c = 0.1):
     - τ = 2: I is cheapest. II is still the most ready (R_II(2) = 0.237 against
       R_I(2) = 0.025), but its reserve costs more than the lateness it saves
       (long-run cost 0.975 against 0.820).
     - τ = 3 to 8: II is cheapest.
     - τ = 12 and 20: III-b and IV are cheapest. Before any redesign cost they
       save 0.081 and 0.100 a period against II, which bounds the amortized
       redesign cost that would pay.
6. **The break-even of reserve against p·L.** The reserve (II against I) pays
   when p·L exceeds a break-even pL*, found from the long runs. The
   approximation c·Δcap/ΔR(τ), with Δcap ≈ 1.83 and ΔR from the imposed
   readiness curves, is loose: it gives 0.27 to 0.31 at τ = 6 where the long
   runs give 0.36 to 0.50, and 0.41 at τ = 3, p = 0.05, where they give 1.15.
   The long-run values are the ones reported.
   - At c = 0.1, pL* is 0.36 to 0.50 at τ = 6, 0.58 to 1.15 at τ = 3, and 0.57
     to 0.69 at τ = 12. It is linear in c.
   - The preferred set is upward-closed in p·L (tested).
   - pL* is not a function of p·L and c alone. It is U-shaped in τ: lowest
     where the deadline lies between the transit time and the wait for
     outside money. At τ = 3 and τ = 6 it rises with p, because frequent use
     keeps the peak rule's budget up for a period after each transition
     (CLAIM-878's recency); at τ = 12 it does not (0.625, 0.571, 0.565 and
     0.689 for p = 0.005, 0.01, 0.02 and 0.05).
7. **Novel demand (CLAIM-361).**
   - *Excision* scores zero violations on D0 and on its own specification,
     while the harm runs for all 120 periods. Revision shows violations on
     both, including the output lost while moving to C (4.1 periods under II
     and 13.3 under III-b). Only the true demand set ranks the two correctly.
   - Under the peak rule (I and III-a) a review that needs capacity can never
     start, so the demand is excised by default, not by choice.
   - A reserve can be used for other things and a redesign cannot. II's
     budget of 3 (a reserve of 2 above holding) covers C's threshold of 2.5 (harm about 6 periods). III-b's
     and IV's budget of 2 (a reserve of 1) does not, so they depend on outside money (harm
     about 15 periods, and harm without end when g = 0).
   - CLAIM-361 is about removing a demand that was in the specification. The
     harm here was never in D0, so "excising" it means never entering it:
     the arm carries CLAIM-361's distinction to a demand outside the
     specification, which goes past the claim's own case.
   - The model does not make the choice between excising and revising emerge
     from anything. That choice is an input. What it shows is how each choice
     scores and which budgets let a revision be acted on.

## What it does not establish

- Nothing about real industries or real budget rules. It is a model with
  invented numbers. Its value is that it makes the draft's stipulations
  executable and shows which of them hold and on what assumptions.
- It does not answer QUESTION-395's identification question: which
  observations distinguish a warranted reserve from waste. It shows what a
  decision would need if readiness were known, namely p, L, c, the deadline
  and the paths' thresholds and times. It also shows that readiness under
  do(c) and readiness observed in operation differ under the peak rule.
- Results that depend on choices made here:
  - The staged route is slower. If it were as fast as the original, III-b
    would match II at every deadline, at half the reserve.
  - Outside money buys the cheapest route. If it bought the fastest, III-a
    would match I.
  - The review uses transition capacity.
  - The carry rule is capped.
- One resource, one contingency type and one novel demand. CLAIM-585's
  several resources and A48 §9.5's several deadlines are not run.
