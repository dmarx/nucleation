---
status: Active
status_note: >-
  read in full 2026-10-24 (NOTE-tmpo0w02) from the NASA Technical Reports
  Server copy (document 20010066523, a 7-page scanned report marked public
  use permitted), not the version in the Intelligent Agent Technology
  proceedings; worth reading as the most compact statement the record
  holds of difference rewards. A member's private utility is factored when
  it ranks the member's own alternatives as the world utility does, the
  others held fixed; the Wonderful Life Utility, world utility minus its
  value with the member's effect set clamped, is factored and learns
  faster than the world utility itself. Clamping to the average action did
  better than clamping to the member's absence. The optimal clamp is only
  sketched ("too long to go through here") and the experiment is one bar
  problem.
title: 'Optimal Reward Functions in Distributed Reinforcement Learning'
version: 1
history:
- version: 1
  date: '2026-10-24'
  note: >-
    Filed and read 2026-10-24 as the lawful text of the difference-rewards
    programme, when the paper the lead named, Wolpert & Tumer's "Optimal
    Payoff Functions for Members of Collectives" (LIT-tmpkensg), could not
    be reached; the two share most of their abstract. Citation checked
    against Crossref: Wolpert & Tumer, in Intelligent Agent Technology
    (World Scientific, September 2001), pp. 365–374,
    doi:10.1142/9789812811042_0049. Read from the NASA Technical Reports
    Server, ntrs.nasa.gov/citations/20010066523 (NASA Ames; NTRS
    publication date 2000, year only; copyright determination
    GOV_PUBLIC_USE_PERMITTED), a 7-page scan with an OCR layer, extracted
    by pdftotext and, where the OCR failed (parts of pp. 3–7), read from
    page images. It cites a paper "to appear" at AAAI 2000, so it predates
    the proceedings. `published:` is NTRS's year, 2000, written as 1
    January for want of a month; the proceedings date (September 2001) is
    the alternative. Whether the proceedings text differs from the report
    is not known.
tags:
- complex-systems
- game-theory
- anthology-candidate
date: '2026-10-24'
published: '2000-01-01'
doi: '10.1142/9789812811042_0049'
url: 'https://ntrs.nasa.gov/citations/20010066523'
first_author: 'Wolpert'
keywords:
- 'collective intelligence'
- 'COIN'
- 'Wonderful Life Utility'
- 'factored utility'
- 'effect set'
- 'learnability'
- 'clamping parameter'
- 'El Farol bar problem'
- 'team game'
implementations: []
summary: >-
  Wolpert & Tumer: members of a multi-agent system each run a reinforcement
  learner, and the designer must give each a private utility such that
  their learning maximises a world utility G. A private utility is
  factored when it ranks a member's own alternatives, others fixed, as G
  does; the Wonderful Life Utility G(ζ) − G(CL(ζ)), with the member's effect
  set clamped, is factored and has higher learnability than G. A sketched
  approximation sets the clamp to the expected action rather than zero; in
  a 60-agent bar problem, clamping to the average action learned best
  across attendance levels, clamping to absence close behind, and G itself
  worst.
---
<!-- inactive-ok-file: THEORY-tmpomtdz — Proposed; filed from this reading, named -->
<!-- inactive-ok-file: LIT-tmpkensg — Unavailable; the paper this report stands in for, named -->
<!-- inactive-ok-file: CLAIM-436 CLAIM-tmp8z857 — Proposed; the claims this reading bears on, named, nothing here rests on them -->

# LIT-tmp8bczu: Optimal Reward Functions in Distributed Reinforcement Learning

Wolpert & Tumer (2000; Intelligent Agent Technology, 2001) —
ntrs.nasa.gov/citations/20010066523

## Key takeaways

- **Factored.** A system is factored if for each member η,
  γ_η(C(ζ₀)) ≥ γ_η(C(ζ′₀)) ⇔ G(C(ζ₀)) ≥ G(C(ζ′₀)) for initial states that
  differ only for η (p. 3). An ordinal condition: the member's private
  utility and the world utility order the member's own alternatives alike.
- **The characterisation.** Factored iff each γ_η is an increasing
  function of G given the components outside η's effect set (Theorem,
  Eq. 1, p. 3; proof deferred to the authors' earlier work).
- **The Wonderful Life Utility.** WLU_η = G(ζ) − G(CL_{S_η^eff}(ζ)), the
  world utility minus its value with η's effect set clamped to a fixed
  vector, conventionally zero. "To evaluate the WLU one does not need to
  know how to calculate the system's behavior under counter-factual
  starting conditions" (p. 3): it is computed on the actual worldline.
- **Learnability.** A factored utility can still be hard to learn when G
  depends on everyone; the WLU's subtraction removes noise from others
  (Eq. 2, p. 4).
- **The clamp.** Clamping to the average action (1/7 per night) did best
  across one to six nights; clamping to absence was close for few nights
  and dropped slightly as nights increased; clamping to attending every
  night did poorly for few nights; G did worst throughout (Figure 1a,
  pp. 5–6).

## Why this is here

Filed 2026-10-24 in place of LIT-tmpkensg, for difference rewards, which
the lead read as answering "what if this process had not acted"
(CLAIM-tmp8z857, QUESTION-tmponjie, QUESTION-tmpdicvf's fourth failure).
The reading corrects that in two ways (NOTE-tmpo0w02). The counterfactual
is not causal: the WLU is the world utility re-evaluated on the actual
history with one member's contribution replaced, the others' behaviour
held as it was, so it needs no model of how the system would have
responded. And "had not acted", clamping to zero, was not the best clamp;
the expected action was. Its factoredness condition, in turn, is an
ordinal alignment of each member's utility with the collective's, close to
QMIX's monotonicity (LIT-tmp3ztxf) and to CLAIM-436's distinction between
an ordering and a currency. Filed as THEORY-tmpomtdz. It carries
`anthology-candidate` as a multi-agent RL method and no instruction for
practice here.
