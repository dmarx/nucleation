---
status: Skimmed
paper: 'LIT-tmphy35q'
title: 'Guigues, Kleywegt and Nascimento — A Markov preparedness metric for ambulance selection and reassignment'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in part on 2026-11-04 from the arXiv preprint,
    https://arxiv.org/pdf/2605.05421v1, 34 pages, extracted with pdftotext.
    Registered and read at the owner's request as a stand-in for
    Nasrollahzadeh, Khademi and Mayorga (2018), LIT-tmpsdrz9, of which no
    lawful copy was found. Read: §§1–4 in full (overview, the two
    decisions, the literature review, contributions, the metric and the
    two policies), the set-up and first results paragraphs of §5, Table 2,
    §6 (code) and §7. Skimmed: Figures 1–9 and the per-figure commentary
    in §5. Not read: the reference list, beyond spot checks. Skimmed
    because the results section, which carries the comparison, was not
    read closely. Page numbers below are the preprint's.
date: '2026-11-04'
summary: >-
  Defines a station-level preparedness metric, the steady-state cost rate
  of a continuous-time Markov chain over a station's busy ambulances, and
  uses it inside one-step integer programs for choosing which ambulance to
  send (or whether to queue the call) and where a freed ambulance goes. In
  a Rio de Janeiro simulation the policy had lower mean allocation cost
  than nine published policies in most cases and was among the best on
  mean response time. Results skimmed; costs assumed; ADP policies not
  compared.
---
<!-- inactive-ok-file: LIT-tmpsdrz9 THEORY-tmpnqoln — Unavailable or Proposed; the unread paper this stands in for, and the account filed from this reading -->

# NOTE-tmp5y2s6: Guigues, Kleywegt and Nascimento — A Markov preparedness metric for ambulance selection and reassignment

## Contribution

A preparedness metric for an EMS that is nonlinear in supply relative to
demand and allows several emergency and ambulance types; two real-time
policies built on it, one for ambulance selection and one for
reassignment; and a broad review of how dispatch policies account for the
future consequences of a dispatch. The abstract: "We propose a new
preparedness metric that quantifies the ability of the emergency medical
service to respond to future emergencies" (p. 1).

## Key insight

Every dispatch spends readiness. Sending a unit now changes which calls
the system can answer later, so a good decision prices the change in
readiness alongside the immediate response cost. The paper makes that
price computable in real time by precomputing, per station, the
long-run cost rate of the station's own busy–free dynamics for every
supply level.

## Assumptions

- **Local metric.** One station at a time, with Poisson arrivals and
  exponential service; within the chain the most-preferred available
  ambulance type is dispatched.
- **Accuracy.** The approximation "may be inaccurate if demand is large
  relative to supply" (§2, p. 13).
- **Truncation.** Supply above 8 ambulances of a type at a station is
  treated as 8 (p. 19), the authors arguing the extra value is small.
- **Costs.** Allocation costs for the Rio data are assumed (Table 1), and
  the authors say the numerical results "serve as examples only, and not
  as guidelines for dispatching decisions" (p. 12).
- **A weight Γ** trades preparedness against immediate cost in the
  integer programs (§3).

## Key results

- **The trade-off (§1.2, p. 4).** An ambulance "may be dispatched to a
  current, less urgent, emergency", and "it may not be available for a
  future, more urgent, emergency".
- **Queueing as a choice (§1.1, p. 3).** Queueing "may be needed if no
  ambulances are available when the emergency call is received, or may be
  desirable if the emergency is not urgent".
- **Redirection (§1.1, p. 3).** "Any ambulance can be dispatched to an
  emergency, even if the ambulance is on its way to another emergency or
  on its way to an ambulance station".
- **Against myopia (§1.3.1, p. 7).** "Approaches that ignore operational
  consequences often perform poorly".
- **Novelty (§1.4, p. 12).** The metric "models how the number of
  available ambulances at a station vary over time" and "allows
  performance to be nonlinear in supply relative to demand, as is typical
  in queueing systems".
- **Response time and survival (§1.3.2, p. 12).** Outside cardiac arrest,
  "studies often found no statistically significant relationship between
  response time and survival probability".
- **Computation (Table 2, p. 20).** Real-time decisions take milliseconds;
  the offline Markov computation grows from under a second for 6
  ambulances to 346,000 s for 16.
- **The comparison (§7, p. 29).** "In most cases, this policy performed
  better than the 9 policies in terms of mean allocation costs", and it
  was among the best of them on mean response time. The per-figure
  results (Figures 1–9) were skimmed, not checked.

## Concepts

- **Ambulance selection decision**: call-initiated; dispatch now and
  choose which ambulance, or queue the call.
- **Ambulance reassignment decision**: ambulance-initiated; send a newly
  available ambulance to a queued call or to a station.
- **Preparedness metric** ψ̄_b^m: the steady-state cost rate at station b
  given supply vector m; with a penalty when no ambulance can serve a
  call of a type, it is the weighted rate of arrivals that find no
  suitable ambulance.

## Connections

It builds on the ADP and preparedness literatures it reviews (§1.3),
including Andersson and Värbrand (2007) and Lee's preparedness-based
heuristics, which are among its nine comparators.

As a stand-in for Nasrollahzadeh, Khademi and Mayorga (2018),
LIT-tmpsdrz9:

- **It restates** that paper's problem class: selection of any available
  ambulance with the option to queue, joined to a reassignment decision,
  under the trade-off between a call now and readiness later. Of the paper
  itself it says only that it "proposed a number of basis functions to
  approximate the value function of the MDP" and that "The response time
  performance under the resulting policy was compared with a number of
  benchmark policies and with the lower bounds of Maxwell, Ni, et al.
  (2014)" (p. 7).
- **It does not restate** that paper's state space, basis functions or
  bound construction, its Mecklenburg County results (12% lower expected
  response time, 30.6% fewer late high-priority calls) or its breakdown
  by strategy. It leaves the ADP policies out of its comparison, and its
  own model, a per-station Markov metric in a one-step program, is a
  different one.

## Bearing on the record

- **The pasted bibliography on emergency readiness.** This work is not in
  A's list. On A's theme, the value of availability, it is more direct
  than the abstract of the work it stands in for: the metric is an
  explicit price on keeping units free for calls that may never come. It
  says nothing of provisional dispatch followed by cancellation en route,
  though it allows a unit in transit to be redirected (p. 3).
- **CLAIM-296 (has, knows it has, can deploy within a deadline).**
  Supports. Preparedness is defined over deployable supply at a station;
  a busy unit adds nothing to it.
- **TERM-055 (operational availability).** Qualifies. ψ̄ is a fleet-level,
  steady-state counterpart of α, the long-run rate at which calls find no
  suitable unit, not the chance that a given agent deploys a given
  resource before a deadline under a cue; the cue enters only as
  emergency type. Citing it as an instance would need a fleet extension
  of the term.
- **CLAIM-517 (viability at boundary contexts).** Qualifies, by analogy.
  The authors' caveat that the metric is inaccurate when demand is large
  relative to supply makes it least reliable in the high-load contexts
  that matter most.
- **CLAIM-535 (observation-relative acceptable policies).** Qualifies, by
  analogy. Selection is made on the emergency type as the dispatcher
  classifies it.
- **CLAIM-079, CLAIM-347, QUESTION-132.** Unrelated.
- Filed: THEORY-tmpnqoln. No instruction for machine-learning practice;
  nothing for the anthology.

## Limitations

- An unrefereed preprint, read in part; the results figures were skimmed.
- Assumed allocation costs; the authors call the results examples, not
  guidelines.
- A local approximation that the authors say can fail under heavy load.
- The comparison excludes the ADP policies (Schmid 2012; Nasrollahzadeh
  et al. 2018), so it does not test the metric against them.
- One city.
