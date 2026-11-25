---
number: 123
status: Proposed
formerly:
- SYNTHESIS-tmp8j9h0
title: 'Response speed is set by chains, not slow parts'
statement: >-
  How fast an organization responds and revises, in the record: a
  first-order reference's time to meet a step times the noise it passes is
  fixed, so a deadline sets a floor on the noise; a slowly relaxing
  operation is proposed to be cheap to push and, kept within tolerance, slow
  to retune; a response's time is the longest chain of its stages still to
  be done, not its slowest part; slowness alone does not make a mode hard to
  redirect; and what counts as noise, where entrenchment sits and how far a
  readiness kernel reaches up the tiers of governance are not settled
version: 2
history:
- version: 2
  date: '2026-11-23'
  note: >-
    Two further readings of the manuscript governance-of-possibility,
    found by its integration pass, added under Not stated on the record,
    at the owner's ruling that what the manuscript states and no entry
    maps to is filed as an account: §4's one rate per relation (a recap of
    CLAIM-1152) and §4.1's reading of CLAIM-1149 for an
    institution (a carry). The third the pass found, §3.1's carriage of
    CLAIM-478 into institutions, is CLAIM-730's, held as a supposition,
    and needs no item.
defeated_if: >-
  A component misstated or misattributed here, with its scope conditions;
  an in-force entry of the record that states part of this theme left out
  without a reason given; a link this account states that no component
  states; or a join of the manuscript governance-of-possibility in this
  scope (JA3, JB3, JB4, JB5, JB10, JC8) placed as stated when no entry
  states it, or as not stated when one does. Its standing is its
  components': a component retired takes its clause with it.
tags:
- control-theory
- society-and-governance
- operations-research
date: '2026-11-23'
line:
- realizability
- will-organization
- distributed-agency
integrates:
- CLAIM-1152
- CLAIM-1010
- CLAIM-1137
- CLAIM-1051
- CLAIM-1192
- CLAIM-345
- CLAIM-1082
- CLAIM-589
- CLAIM-626
- CLAIM-679
- CLAIM-400
- CLAIM-1070
- TERM-164
- CLAIM-1040
- CLAIM-719
- QUESTION-522
- TERM-085
- CLAIM-1114
- CLAIM-711
- CLAIM-423
- CLAIM-705
- TERM-167
- CLAIM-025
- CLAIM-099
- QUESTION-528
summary: >-
  A thematic account, across lines, of the joins the manuscript
  governance-of-possibility makes on the timing of response and revision
  and that no entry maps (JA3, JB3, JB4, JB5, JB10, JC8). It was filed for
  that manuscript at the owner's ruling of 2026-11-23: "the manuscript is a
  view over the argument. preferably, nothing in it is new. restatements
  are fine. if they aren't directly mappable to anything already on the
  record, instead of throwing them away just file them as syntheses." Two
  joins are now stated by gap fills filed that day (JB3 by [CLAIM-1137](../claims.d/CLAIM-1137.md),
  the core of JC8 by [CLAIM-1114](../claims.d/CLAIM-1114.md)). One passes [ADR-075](../decisions.d/ADR-075.md)'s test and is filed
  as [CLAIM-1082](../claims.d/CLAIM-1082.md) (JB10). The rest are recaps, mappings or free
  parameters, and are listed under "Not stated on the record". The wording
  is the assistant's (Claude, in this session); adopting it is the owner's
  call.
---

<!-- inactive-ok-file: CLAIM-1137 CLAIM-1082 CLAIM-1070 TERM-164 CLAIM-719 CLAIM-711 CLAIM-423 CLAIM-705 TERM-167 SYNTHESIS-122 SYNTHESIS-124 SYNTHESIS-121 SYNTHESIS-086 — Proposed; components and neighbouring accounts, cited with their standing -->

# SYNTHESIS-123: Response speed is set by chains, not slow parts

*A thematic account, across lines, of the joins of the manuscript
governance-of-possibility (scratch/manuscripts/governance-of-possibility/,
§§4, 5, 7.3, 8.4 and 10.3) on the timing of response and revision that no
entry maps: JA3, JB3, JB4, JB5, JB10 and JC8. It was filed for that
manuscript at the owner's ruling of 2026-11-23 ("if they aren't directly
mappable to anything already on the record, instead of throwing them away
just file them as syntheses"), on the synthesis-review skill's stage 4.
Its components come from realizability, will-organization and
distributed-agency, and some also carry readiness, formal-apparatus and
organizational-normativity ([ADR-129](../decisions.d/ADR-129.md)). It adds nothing; its standing is its
components'.*

*Accounts checked first. [SYNTHESIS-122](SYNTHESIS-122.md) maps the exchange "Explain
First Contact RL" and integrates most of the exchange's components here.
Its scope is that exchange's filing, and its "Not stated" section tests
none of these joins. Three kinds of component lie outside it: the gap
fills of 2026-11-23 ([CLAIM-1137](../claims.d/CLAIM-1137.md), [CLAIM-1114](../claims.d/CLAIM-1114.md), [QUESTION-522](../questions.d/QUESTION-522.md),
[QUESTION-528](../questions.d/QUESTION-528.md)); the entries from other exchanges the joins use
([CLAIM-711](../claims.d/CLAIM-711.md), [CLAIM-423](../claims.d/CLAIM-423.md), [CLAIM-705](../claims.d/CLAIM-705.md), [CLAIM-400](../claims.d/CLAIM-400.md), [CLAIM-589](../claims.d/CLAIM-589.md), [CLAIM-719](../claims.d/CLAIM-719.md)); and
the new claim. No other account's scope is the timing of response, so this
is a new account rather than a revision. The manuscript's joins JB6 to JB9,
which the review of 2026-11-23 (Part B) found stated by entries, are not
repeated here.*

## The account

**Filtering against a deadline (JB3).**
- **The filter.** An organizational variable that adapts at rate k to a
  noisily observed demand tracks what is slower than k and ignores what is
  faster. Its tracking error grows as ω²/(k² + ω²) and the noise it passes
  as k²/(k² + ω²). The per-frequency optimum is S_d/(S_d + λS_n)
  ([CLAIM-1152](../claims.d/CLAIM-1152.md), Active, demonstrated; A's wording, checked).
- **The speed floor.** A reference revisable at rate v meets a demand at
  distance 1 by H only if vH ≥ 1 − δ − ε. That claim "says nothing of what
  a fast-revisable reference costs against transient fluctuations"
  ([CLAIM-1010](../claims.d/CLAIM-1010.md), Active, demonstrated; A's).
- **The two together.** For the first-order rule, the time to come within
  δ of a step, ln(1/δ)/k, times the stationary variance passed from white
  noise, kσ²/2, is σ² ln(1/δ)/2 whatever k is. So a deadline H sets a floor
  σ² ln(1/δ)/(2H) on the noise passed ([CLAIM-1137](../claims.d/CLAIM-1137.md), Proposed,
  demonstrated; the assistant's gap fill GB4). It sets [CLAIM-1152](../claims.d/CLAIM-1152.md)'s
  noise cost beside a deadline, as [TERM-115](../terms.d/TERM-115.md) poses deadlines. It complements
  [CLAIM-1010](../claims.d/CLAIM-1010.md) and says the two are "a different model, a rate limit
  rather than a first-order rule". **JB3 is stated by [CLAIM-1137](../claims.d/CLAIM-1137.md)**, for
  the first-order rule.

**Pushing a mode against retuning it (JB10).**
- **The push.** For ȧ = −γa + bu the least effort to move a by Δ within H
  is 2γΔ²/(b²(1 − e^{−2γH})), which falls as γ falls. "Persistence,
  redirection and the renewal of a mode's supports are three timescales
  that need not coincide" ([CLAIM-1192](../claims.d/CLAIM-1192.md), Active, demonstrated; A's idea
  and formula, the assistant's monotonicity). It is the one-mode case of
  [CLAIM-345](../claims.d/CLAIM-345.md) (Active, demonstrated): the least effort is set by the
  Gramian, not by controllability rank.
- **The retuning.** Operation relaxing at rate γ toward h(θ), with θ moving
  at rate at most V, stays within LV/γ of it. That condition is
  "sufficient, not necessary" ([CLAIM-1051](../claims.d/CLAIM-1051.md), Active, demonstrated; A's,
  checked). Among its obstructions it lists "operation slowing, so that the
  permissible retuning rate falls".
- **The two in one system.** With operation kept within ε of the
  configuration throughout, moving the configuration by D needs
  H ≥ (D/ε − 2)/γ. So a smaller γ makes the push cheaper and the
  tolerance-keeping retuning slower at once ([CLAIM-1082](../claims.d/CLAIM-1082.md), Proposed,
  demonstrated; the assistant's). **JB10 is that claim**, filed for this
  account; it passed [ADR-075](../decisions.d/ADR-075.md)'s test by derivation, with a discriminating
  prediction.

**Where entrenchment sits (JB5).**
- **Not in slowness alone.** A mode's slowness "says how it persists, not
  how hard it is to redirect", and "a mode with b = 0 cannot be redirected
  through it at any rate" ([CLAIM-1192](../claims.d/CLAIM-1192.md)).
- **In the control channel.** "Permitted directions, actuated directions
  and transitions achievable at acceptable cost are three objects"
  ([CLAIM-589](../claims.d/CLAIM-589.md), Active, demonstrated; A's). A small b makes control costly
  whatever γ is ([CLAIM-345](../claims.d/CLAIM-345.md)).
- **In the supports.** [CLAIM-1192](../claims.d/CLAIM-1192.md) names τ_reproduce, the renewal of a
  mode's supports, and reads [CLAIM-626](../claims.d/CLAIM-626.md)'s maintenance arm as τ_reproduce
  slowing. [CLAIM-626](../claims.d/CLAIM-626.md) (Active, demonstrated; A's): "when the maintenance of
  the coupling slows, the reduction stays good while the organization
  nears its fold". Cutting held resource toward the holding cost leaves the
  organization able to "hold where it is" and to reach "no configuration
  whose transition carries any reconfiguration slack" ([CLAIM-679](../claims.d/CLAIM-679.md), Active,
  demonstrated; A's sentence).
- **In feedback.** A maintained state with persistence λ adds terms in
  1/(1 − λ), "the slower it is the more it adds", so "a lean in the regime
  can outlast the advantages it was built from" ([CLAIM-400](../claims.d/CLAIM-400.md), Active,
  demonstrated). [CLAIM-1070](../claims.d/CLAIM-1070.md) (Proposed, interpretive; A's) already
  locates "Slow modes can entrench error" there: "[CLAIM-400](../claims.d/CLAIM-400.md)'s maintained
  legibility state adds terms in 1/(1 − λ)".
- **What the manuscript reconciles.** [TERM-164](../terms.d/TERM-164.md) (Proposed; A's)
  defines destructive lock-in. [CLAIM-1070](../claims.d/CLAIM-1070.md)'s "slow modes can entrench"
  is set against [CLAIM-1192](../claims.d/CLAIM-1192.md). **Each of the three places is stated by
  the entry named, and the denial that slowness alone entrenches is
  [CLAIM-1192](../claims.d/CLAIM-1192.md)'s.** That entrenchment must sit in one of the three is
  not stated (below).

**What counts as noise (JB4).**
- **The classification is governed.** "What an organization's filtering
  treats as noise is itself governed", and the capacity to recognize a
  demand "must stay open to correction" ([CLAIM-1040](../claims.d/CLAIM-1040.md), Active,
  interpretive; A's).
- **Second-order responsiveness.** An institution can be responsive within
  its governing mechanism and unresponsive to reasons for revising it
  ([CLAIM-719](../claims.d/CLAIM-719.md), Proposed, interpretive; A's). Its admission says ρ^(2) "is
  named, not defined".
- **The question that holds the join.** [QUESTION-522](../questions.d/QUESTION-522.md) (Open; the
  assistant's, gap GB2) asks by what mechanism the classification is
  revised and what would measure responsiveness to reasons for revising
  it. It records the join: "The manuscript reads the classification of
  noise as the object of that second-order responsiveness (its join JB4),
  so the two gaps are one." **JB4 is recorded there as a reading and held
  open**, not stated as a claim.

**The time of a response (JC8).**
- **Stages of correction.** [TERM-085](../terms.d/TERM-085.md) (Active; A's α_J) splits the time to
  correct into "discovery, verification, coordination and execution, which
  overlap and compete". Its note on Hutchins says preparation "moves the
  cost of search ahead of the deadline".
- **The route.** Where a response runs through stages that do not compete
  for a shared resource, stages in sequence add their times, overlapping
  stages contribute the longest, and a stage done before the contingency
  contributes nothing. "The slowest component sets the response time only
  when it is on the critical path at the time of the contingency"
  ([CLAIM-1114](../claims.d/CLAIM-1114.md), Proposed, demonstrated; the assistant's gap fill GC8).
  **The core of JC8 is stated by [CLAIM-1114](../claims.d/CLAIM-1114.md).** Its own "What it does
  not say" excludes the rest: "Not the manuscript's join JC8 as a whole:
  that a commitment set slowly can be applied fast ([CLAIM-711](../claims.d/CLAIM-711.md)), or that
  speed does not settle authority ([CLAIM-423](../claims.d/CLAIM-423.md))".
- **The neighbours.** "Standing constraints set slowly in advance and
  enforced by mechanisms faster than the process can foreclose
  alternatives keep it open to intervention without delaying it"
  ([CLAIM-711](../claims.d/CLAIM-711.md), Proposed, interpretive, counter; A's). Components changing
  at different speeds differ in which of them "holds authority over the
  others" ([CLAIM-423](../claims.d/CLAIM-423.md), Proposed, interpretive; the owner's). Where valid
  challenges arrive at rate λ and are resolved at rate μ < λ, "at most a
  share μ/λ can ever be resolved in time" ([CLAIM-705](../claims.d/CLAIM-705.md), Proposed,
  demonstrated; A's).

**Tiers of governance and the readiness kernel (JA3).**
- **The kernel.** [TERM-167](../terms.d/TERM-167.md) (Proposed; A's) is the viability kernel of
  reorganization readiness. In its note "a second-order version",
  M_adaptive = M_D ∩ ⋂ T_{D→D′} and V_adaptive = Viab(M_adaptive). Its
  "Against the record" pairs [CLAIM-099](../claims.d/CLAIM-099.md) and [CLAIM-025](../claims.d/CLAIM-025.md). Its note of
  2026-11-23 on the manuscript says the construction "secures one
  retuning: nothing in the construction requires readiness again after a
  switch to a new demand unless the family of demands is closed under
  retuning".
- **The tiers.** "An operative regime, the governing organization among
  regimes, and the capacity to transform that organization can persist or
  fail separately" ([CLAIM-025](../claims.d/CLAIM-025.md), Active, interpretive; the paper's, §6.2).
  "Maintaining a regime of effective action and maintaining the capacity
  to govern among regimes are not the same achievement" ([CLAIM-099](../claims.d/CLAIM-099.md),
  Active, interpretive; the paper's main result).
- **What secures readiness again.** [QUESTION-528](../questions.d/QUESTION-528.md) (Open; the
  assistant's, gap GA3) asks whether a family closed under retuning or a
  recursively defined kernel does, and whether the two coincide.

## The components

| Code | Voice | Status, warrant |
|---|---|---|
| [CLAIM-1152](../claims.d/CLAIM-1152.md) | A's (ChatGPT), checked | Active, demonstrated |
| [CLAIM-1010](../claims.d/CLAIM-1010.md) | A's, checked | Active, demonstrated |
| [CLAIM-1137](../claims.d/CLAIM-1137.md) | the assistant's | Proposed, demonstrated |
| [CLAIM-1051](../claims.d/CLAIM-1051.md) | A's, checked | Active, demonstrated |
| [CLAIM-1192](../claims.d/CLAIM-1192.md) | A's formula, the assistant's monotonicity | Active, demonstrated |
| [CLAIM-345](../claims.d/CLAIM-345.md) | A's, from the exchange of 2026-10-17 | Active, demonstrated |
| [CLAIM-1082](../claims.d/CLAIM-1082.md) | the assistant's, filed for this account | Proposed, demonstrated |
| [CLAIM-589](../claims.d/CLAIM-589.md) | A's | Active, demonstrated |
| [CLAIM-626](../claims.d/CLAIM-626.md) | A's | Active, demonstrated |
| [CLAIM-679](../claims.d/CLAIM-679.md) | A's sentence | Active, demonstrated |
| [CLAIM-400](../claims.d/CLAIM-400.md) | the owner's construction, with the record's additions | Active, demonstrated |
| [CLAIM-1070](../claims.d/CLAIM-1070.md) | A's | Proposed, interpretive |
| [TERM-164](../terms.d/TERM-164.md) | A's | Proposed |
| [CLAIM-1040](../claims.d/CLAIM-1040.md) | A's | Active, interpretive |
| [CLAIM-719](../claims.d/CLAIM-719.md) | A's | Proposed, interpretive |
| [QUESTION-522](../questions.d/QUESTION-522.md) | the assistant's | Open |
| [TERM-085](../terms.d/TERM-085.md) | A's α_J | Active |
| [CLAIM-1114](../claims.d/CLAIM-1114.md) | the assistant's | Proposed, demonstrated |
| [CLAIM-711](../claims.d/CLAIM-711.md) | A's, counter | Proposed, interpretive |
| [CLAIM-423](../claims.d/CLAIM-423.md) | the owner's | Proposed, interpretive |
| [CLAIM-705](../claims.d/CLAIM-705.md) | A's | Proposed, demonstrated |
| [TERM-167](../terms.d/TERM-167.md) | A's | Proposed |
| [CLAIM-025](../claims.d/CLAIM-025.md) | the paper's | Active, interpretive |
| [CLAIM-099](../claims.d/CLAIM-099.md) | the paper's | Active, interpretive |
| [QUESTION-528](../questions.d/QUESTION-528.md) | the assistant's | Open |

## Not stated on the record

Each item gives the join, what no component states, and its verdict under
[ADR-075](../decisions.d/ADR-075.md), step 5.

- **JB3, beyond the first-order rule.** That [CLAIM-1137](../claims.d/CLAIM-1137.md)'s conserved
  product carries over to [CLAIM-1010](../claims.d/CLAIM-1010.md)'s rate-limited reference is not
  stated. [CLAIM-1137](../claims.d/CLAIM-1137.md) says the two are different models. *Verdict:
  nothing filed.* The join as the manuscript states it, a speed floor from
  the deadline and a noise cost from the filter, is [CLAIM-1137](../claims.d/CLAIM-1137.md)'s.
  Carrying it to a rate limit would need a model of its own.
- **JB4, the classification of noise as the object of [CLAIM-719](../claims.d/CLAIM-719.md)'s
  second-order responsiveness.** No entry states it as a claim.
  [QUESTION-522](../questions.d/QUESTION-522.md) records it as a reading and holds it open. *Verdict:
  fails, a free parameter.* [CLAIM-719](../claims.d/CLAIM-719.md)'s ρ^(2) is "named, not defined", so
  reading the classification into that slot gives no measure. Any revision
  of the filter would count. [CLAIM-1149](../claims.d/CLAIM-1149.md) (Active, demonstrated; a
  forager that revises which features count only for a change on a
  feature it never attended to) is a model of revising a classification.
  It could ground a measure, which is [QUESTION-522](../questions.d/QUESTION-522.md)'s open part.
- **JB5, that entrenchment "must sit" in the control channel, the supports
  or feedback.** Each place is stated (above). That the three exhaust
  where entrenchment can sit is not. *Verdict: fails, a recap as a list,
  and not exhaustive as a disjunction.* The record holds other places:
  [CLAIM-1040](../claims.d/CLAIM-1040.md)'s classification of noise, and [CLAIM-423](../claims.d/CLAIM-423.md)'s authority over
  the faster components. The negative half is [CLAIM-1192](../claims.d/CLAIM-1192.md)'s own. The
  review of 2026-11-23 found the join "Partly S", and this is the part not stated.
  [SYNTHESIS-086](SYNTHESIS-086.md) also cautions that a regime varying only κ′ "moves no
  linear threshold". That bears on using [CLAIM-400](../claims.d/CLAIM-400.md) as the place without
  qualification.
- **JC8, [CLAIM-711](../claims.d/CLAIM-711.md) and [CLAIM-423](../claims.d/CLAIM-423.md) read as instances of the route.** That a
  slow commitment applied fast is [CLAIM-1114](../claims.d/CLAIM-1114.md)'s stage "done in
  advance", and that an authority stage can be the bottleneck, are not
  stated. *Verdict: fails, a recap by relabelling.* Each reading places a
  held entry under [CLAIM-1114](../claims.d/CLAIM-1114.md)'s construction and adds no inference.
  Neither has a case: [CLAIM-423](../claims.d/CLAIM-423.md) says "Speed confers nothing by itself" and
  holds no case. One distinction is also not stated in one entry: the
  route sets a single response's latency ([CLAIM-1114](../claims.d/CLAIM-1114.md)), while a slow
  resolving stage bounds the share of a stream resolved in time
  ([CLAIM-705](../claims.d/CLAIM-705.md)). *Verdict: fails, a recap.* Each half is stated, and the
  conjunction adds no link.
- **JA3, [TERM-167](../terms.d/TERM-167.md)'s three achievements read against [CLAIM-025](../claims.d/CLAIM-025.md)'s three
  tiers.** The tier mapping is not stated. Adaptive viability as the
  second tier sustained under the first, and [CLAIM-025](../claims.d/CLAIM-025.md)'s third tier
  reached "only as far as 𝔇 reaches", are the manuscript's. *Verdict:
  fails, an interpretive mapping and a recap.* The construction's
  definition gives the inclusions. Its separating content, one retuning
  secured unless the family is closed, is already [TERM-167](../terms.d/TERM-167.md)'s note,
  and [QUESTION-528](../questions.d/QUESTION-528.md) holds what would secure more.

- **The manuscript's §4: one rate per relation.** That a single
  first-order rule k/(s + k) can only approximate the per-frequency optimum,
  which is an arbitrary function of frequency set by the two spectra, so one
  adaptation rate per relation is in general not the optimum, is not stated
  beyond [CLAIM-1152](../claims.d/CLAIM-1152.md)'s "neither the slowest nor the fastest adaptation is
  optimal in general". *Verdict: fails, a recap.* It follows in one step
  from [CLAIM-1152](../claims.d/CLAIM-1152.md)'s own formula (a one-parameter family against an
  arbitrary target), and adds no case, derivation or prediction the claim
  leaves open.
- **The manuscript's §4.1: [CLAIM-1149](../claims.d/CLAIM-1149.md) read for an institution.** That
  revising an institution's classification of noise pays where a new demand
  arrives through a class of signal it does not attend to, and nowhere else,
  is not stated: [CLAIM-1149](../claims.d/CLAIM-1149.md) is shown for a simulated forager. *Verdict:
  fails, a carry.* No institutional case is held; [QUESTION-522](../questions.d/QUESTION-522.md) holds
  the question of how such a classification is revised.

## Cross-line audit ([ADR-129](../decisions.d/ADR-129.md))

Its 25 components come from six lines. Counted by script over their
`line` fields: realizability 14, will-organization 9, distributed-agency
8, readiness 5, formal-apparatus 5, organizational-normativity 2.

- **An unheld question.** Yes. "How fast must an organization respond and
  revise, and where does the time of a response sit?" No line's blurb names
  it. Readiness names response capability for rare circumstances.
  Realizability names reaching under bounds. Neither names rates of
  revision or noise.
- **Recurrence.** Yes. The theme recurs in [SYNTHESIS-122](SYNTHESIS-122.md)'s thread
  "the spectrum of response times", in this manuscript, and in a claim
  resting on several of these lines ([CLAIM-1070](../claims.d/CLAIM-1070.md)).
- **Findability.** Yes. A reader looking for response timescales would
  find them under none of the three main lines.

*Verdict: a candidate line*, put to the owner rather than made ([ADR-082](../decisions.d/ADR-082.md)).
A name could be "temporal organization of response", with the blurb "how
fast an organization detects, absorbs, retunes and corrects, and what
those rates cost: filtering against deadlines, pushing against retuning,
the time of a response's route, and who classes noise". It would gather
this account, [CLAIM-1070](../claims.d/CLAIM-1070.md), [CLAIM-1152](../claims.d/CLAIM-1152.md), [CLAIM-1010](../claims.d/CLAIM-1010.md),
[CLAIM-1051](../claims.d/CLAIM-1051.md), [CLAIM-1137](../claims.d/CLAIM-1137.md), [CLAIM-1082](../claims.d/CLAIM-1082.md), [CLAIM-1114](../claims.d/CLAIM-1114.md) and
[CLAIM-1040](../claims.d/CLAIM-1040.md). Most of them now sit in realizability, from one
exchange's thread. [CLAIM-1137](../claims.d/CLAIM-1137.md) and [CLAIM-1114](../claims.d/CLAIM-1114.md) also carry
readiness.

## What it does not say

That any of these models describes a real regulator or industry. Every
component is a model, an interpretation, or A's wording, and the
manuscript's own gap GD5 says the record holds no industrial case. The
manuscript's other joins are mapped by [SYNTHESIS-124](SYNTHESIS-124.md) (readiness under
budget rules, and lock-in) and [SYNTHESIS-121](SYNTHESIS-121.md) (correction,
answerability and harmony).
