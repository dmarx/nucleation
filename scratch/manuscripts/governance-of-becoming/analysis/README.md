<!-- scratch/manuscripts/governance-of-becoming/analysis/README.md -->

# Analysis for governance-of-becoming

Scripts the manuscript runs (write-manuscript step 4), each kept once,
with its outputs saved beside it under the date of the run. Every result
here is the assistant's (Claude) and Proposed-grade; the record entry that
holds it is named below.

## fallback_decay_bargaining.py (Article 9, §9.4)

**What it does.** It joins two held models the record kept apart:
CLAIM-605's capacity learned by doing, which decays under substitutive
supply, and the symmetric Nash split of CASE-264's arm A and
CLAIM-tmp2jhc1, in which a party's share moves with its outside option.
The party's outside option is valued from its decaying capacity, and the
script follows its Nash share over time. It then ends the supply before
and after CLAIM-605's deadline, runs five controls (capacity-first
supply; partial substitution below CLAIM-605's a*; CLAIM-602's model,
which has no threshold; CASE-264's arm B, with no exit; take-it-or-leave-it
with exit), and varies the discount rate. It asserts the components
(threshold, kept state, deadline, the held splits), the half-unit
property, and the shape of the results (the steepest fall at the deadline
for r ≤ 0.25 with a single crossing, restoration exactly before the
deadline, the controls). Its other figures, the table's values and the
percentages among them, are not asserted: a run that prints "checks pass"
reproduces them only when its output is compared with the dated output
below, which it matched byte for byte on 2026-11-25. (Corrected
2026-11-25 on the review of Part III, Part A 2.17, which found that the
first wording, "Every figure it prints is asserted", overclaimed.)
Deterministic; standard library only; about ten seconds.

**Run** from the repository root:

    python3 -I scratch/manuscripts/governance-of-becoming/analysis/fallback_decay_bargaining.py

**Parameters.**

| Parameter | Value | From |
|---|---|---|
| λ, μ, τ (learning, decay, practice per unit capacity) | 1, 0.3, 1.5 | CLAIM-605 (scratch/formal/capability_trap_toy.py) |
| S, o_R (joint value, R's stand-alone value) | 10, 2 | CASE-264, arm A |
| w (value per unit time of meeting the whole demand alone) | 4 | invented, set before the run |
| r (discount rate, baseline) | 0.25 | invented, set before the run; §4 of the output varies it over 0.02 to 0.5 |
| horizon of the stand-alone path | 80 | invented, set before the run |
| step dt (RK4) | 0.01 | numerical |

The expectation was set down before the run, in §9.4 of the draft: a step
in P's share at CLAIM-605's deadline. It held for where the fall is
steepest (r ≤ 0.25) and failed as a step except for a patient party.

**Outputs.**

- `fallback_decay_bargaining.2026-11-25.txt`: the run of 2026-11-25.

**Held as** CLAIM-tmp6nzs1 (Proposed, demonstrated in the model), with
dated notes of 2026-11-25 on LEAD-tmpeo8wq and CLAIM-tmp2jhc1.
Recomputed independently by the joins reader of the review of Part III
(REVIEW-2026-11-25-part-iii.md, Part B), from separate code written from
the claim's stated model: `../review-III-B-indep-check.py`.
