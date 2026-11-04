---
status: Read
paper: 'LIT-tmpnhw2v'
title: 'U.S. Fire Administration — Dispatched and canceled en route'
version: 1
history:
- version: 1
  date: '2026-11-04'
  note: >-
    Read in full on 2026-11-04 from the page itself,
    https://www.usfa.fema.gov/nfirs/coding-help/dispatched-and-canceled-en-route/,
    fetched as HTML (HTTP 200, no challenge) and converted to text. Read:
    the introduction, "Remember", the required features of a 611 report,
    Scenario 1, Scenario 2 and the closing reminder. Nothing skipped. The
    page is a short coding aid ("3 min read") with no section or page
    numbers; results are cited by its own headings.
date: '2026-11-04'
summary: >-
  NFIRS coding guidance: Incident Type 611 only when a department is
  dispatched and cancelled before arriving; units cancelled from an
  incident others reached are recorded with Actions Taken 93 in the
  Apparatus/Personnel Modules, and all assigned resources are recorded
  whether or not they arrived. Calls a department could not answer for
  lack of resources are not NFIRS incidents; recording them in a separate
  database outside NFIRS is recommended, not required.
---

# NOTE-tmpain0u: U.S. Fire Administration — Dispatched and canceled en route

## Contribution

A coding rule for the National Fire Incident Reporting System. It says
when an incident is coded 611, dispatched and canceled en route, how
cancelled units are recorded when other units did arrive, and which calls
are outside NFIRS altogether.

## Key insight

The unit of record and the unit of response differ. An incident is coded
by what was found by whoever arrived; each unit's own part, including a
cancellation before arrival, is recorded in the Apparatus/Personnel
Modules. So a reporting system can carry, for one incident, what was
assigned, what arrived and what was turned back, but only for calls the
department actually dispatched to.

## Assumptions

- The reporting department uses NFIRS, and the Basic and
  Apparatus/Personnel Modules; the page recommends the latter "for every
  incident" but does not require it.
- "Aid given or received calls require the arrival of 2 or more fire
  departments on scene", so a cancelled mutual-aid response is not aid.

## Key results

- **When 611 applies (introduction).** "This incident type should only be
  used when the fire department is dispatched to an incident but does not
  arrive on the scene because they were canceled prior to arrival."
- **Not NFIRS incidents ("Remember").** "It is not an NFIRS incident if:
  Your resources were not dispatched and did not leave the station. The
  fire department was not aware of the call. The fire department was
  aware of the call but did not have resources to respond." And: "While
  these situations are not reportable in NFIRS, it is recommended the fire
  department record them outside of NFIRS in a separate database."
- **Required features.** Incident Type 611; Arrival Date/Time blank;
  Actions Taken 93; Aid Given or Received N. "If the fire department
  arrives at the scene, completes an action on scene, and/or gives or
  receives aid, then the incident type should not be canceled en route".
- **Scenario 1 (mutual aid).** The first department arrives and finds
  "the situation no longer requires extra manpower"; it codes the
  building fire (111), and the mutual-aid department cancelled before
  arrival codes 611. Departments may use the District field (Block E2) to
  track this: "The fire department can analyze how often they were
  canceled en route to other districts using the results from this
  field."
- **Cancelled units at an attended incident.** "Apparatus and personnel
  can be dispatched and canceled en route, even if the fire department
  arrives on the scene to an incident." "The use of the
  Apparatus/Personnel Modules can show what resources were available, even
  though they never arrived on scene."
- **Scenario 2.** "Based on information provided by dispatch, the fire
  department sends an engine, a tanker/tender, a rescue vehicle and the
  fire marshal’s car." The engine arrives and "it is determined that the
  situation is a false alarm and no longer requires extra resources"; "The
  fire department cancels the tanker/tender and the rescue vehicle before
  their arrival on scene." The incident is coded as a false alarm (745);
  the two cancelled units carry Actions Taken 93 in the
  Apparatus/Personnel Modules, and "The engine and the fire marshal’s car
  would have the appropriate actions they took on scene".
- **Assigned resources (closing reminder).** In Section G1, "all apparatus
  and personnel that were assigned to the incident for the reporting fire
  department should be recorded regardless of whether they arrived or
  were canceled before arrival."

## Concepts

- **Incident Type 611**: dispatched and canceled en route; a whole
  department's response that never arrived.
- **Actions Taken 93**: canceled en route, for a unit or a department; in
  the Basic Module only if no unit arrived.
- **Apparatus/Personnel Modules**: per-unit records within an incident.
- **Section G1, Resources**: the Basic Module's count of everything
  assigned to the incident.

## Connections

A page of USFA's NFIRS coding help, listed under its Basic Module, Coding
and Data Quality topics. It sits beside the record's other fire-service
material: CASE-135 (the Brookhollow Apartments fire), its review LIT-1374,
and the National Incident Management System, LIT-1365. It does not
mention NFIRS's successor system, which was not checked.

## Bearing on the record

- **The pasted bibliography on emergency readiness.** A uses the page as
  the case source for its running example. Verdict:
  - *Right* that it is official incident-reporting guidance, from 2023,
    and that its Scenario 2 is a multi-unit dispatch, made "Based on
    information provided by dispatch", cut back once the first-arriving
    engine sees the scene. The page does not use the word "provisional".
  - *Overstated.* A's "responding rescue and support vehicles are
    canceled" stands for one rescue vehicle and one tanker/tender; the
    fire marshal's car is not cancelled.
  - *Dropped.* The page's reason is that the call is a false alarm; A
    says only that "additional resources are unnecessary", A's paraphrase.
  - *Not on the page.* There is no heavy rescue squad. The squad of A's
    running example, dispatched provisionally and cancelled en route, is
    A's dramatization, not the page's case.
  - *Wrong in scope and force.* A says that "some situations in which a
    department lacks the resources to respond are not reportable as
    canceled-en-route incidents and should instead be recorded
    separately". The page says such calls are not NFIRS incidents at all,
    not merely not reportable as 611; and that recording them outside
    NFIRS in a separate database is recommended, not required.
  - *Missing.* The page's provisions for recording cancelled units
    (Apparatus/Personnel Modules, Section G1), which cut against any
    reading that the reporting system sees only units that were used.
- **A's proposition** (measuring maintained abilities solely by observed
  utilization can destroy them). The page bears on it both ways: NFIRS
  records committed but unused units, but a failure to respond for lack
  of resources, the case most relevant to readiness, is exactly the one
  it leaves out of the incident data.
- **CLAIM-296 (has, knows it has, can deploy within a deadline).**
  Supports, at the level of reporting: the page separates resources
  assigned, arrived and cancelled en route, and excludes resources the
  department did not have.
- **CASE-085 (the medication in the ambulance).** Supports the same
  distinctions, in a different domain and mechanism; not the same point.
- **TERM-055 (operational availability).** Qualifies. A cancelled unit
  was dispatched in time but its α was never tested by arrival; NFIRS
  records the dispatch, not α.
- **CLAIM-535 (observation-relative acceptable policies).** Supports, by
  analogy: the initial dispatch is chosen on the information dispatch
  provides and revised once the engine observes the scene, a coarser then
  a finer observation.
- **CLAIM-414 (matched ordinary trajectories conceal differences in
  maintained constraints).** Qualifies: a call cancelled en route is an
  ordinary trajectory in which the rescue capability was never exercised.
  The page itself claims nothing about capability.
- **CASE-135, LIT-1374, LIT-1365.** Related domain, not the same point. A
  CASE built on this page would sit beside CASE-135.
- **CLAIM-079, CLAIM-347, CLAIM-517, QUESTION-132.** Unrelated.
- **No THEORY filed.** The page prescribes how to record; it states no
  account of what is true about readiness or cancellation, and a THEORY
  restating its rules would only say that the page says them. It is better
  used as the source of a CASE. No instruction for machine-learning
  practice; nothing for the anthology.

## Limitations

- A coding aid: it says nothing of how often cancellations happen or what
  they cost.
- U.S. NFIRS-specific.
- Silent on NFIRS's transition to a successor system.
