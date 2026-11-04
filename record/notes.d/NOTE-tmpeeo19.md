---
status: Read
paper: LIT-tmpd2pdj
title: 'Klyubin, Polani & Nehaniv — Empowerment (2005)'
version: 1
history:
- version: 1
  date: '2026-11-03'
  note: >-
    Read in full from the University of Hertfordshire Research Archive copy
    (uhra.herts.ac.uk/id/eprint/282/1/901241.pdf, reached from the handle
    hdl.handle.net/2299/1114), the IEEE CEC 2005 paper, pp. 128–135, 8 pp.:
    §§1–4 and the references. The PDF is a scan with a text layer; pypdf
    extracted it with the spaces between words lost and the figures as
    debris (Figures 3 and 5 are read from their captions and the numbers
    printed under them). Pages are the proceedings'.
date: '2026-11-03'
summary: >-
  The first statement of empowerment: the Shannon channel capacity from an
  agent's n-step action sequence to its sensor n steps later,
  max_{p(aⁿ)} I(Aⁿ; S_{t+n}), counted only as far as the agent can
  perceive. Used as a fitness function in a grid world with a signal
  source, it evolves sensors that switch from displacement-sensing blobs
  near the source to bearing-sensing arcs far from it, and actuators that
  vary more, with empowerment bounded by the sensor's capacity.
---
<!-- inactive-ok-file: CLAIM-354 — Proposed; the claim the reading bears on, cited as open -->

# NOTE-tmpeeo19: Klyubin, Polani & Nehaniv — Empowerment (2005)

## Contribution

A task-independent utility for adaptive agents, defined from the
perception–action loop alone: the information-theoretic capacity of the
agent's "actuation channel terminating at the sensor" (eq. 3, p. 130).

## Key insight

Count options, as mobility does in Othello, but count only those whose
results the agent can perceive. "We define what an agent does solely in terms
of what it perceives … it does not matter how much control or influence the
agent appears to have from a 'god's eye view'" (p. 129). The neurosurgeon
example: you may be able to make a neuron spike, "However, if you never
directly or indirectly perceive the result, you will never know that you
have control over the neuron" (p. 129), and it does not count.

## Assumptions

- The loop as a causal Bayesian network S_t → A_t → R_{t+1} → S_{t+1} with R
  the rest of the system, time-invariant (Figure 1, p. 130).
- For empowerment the actions are redrawn as chosen "freely", independent of
  the system's state (the agent with "free will", Figure 2): open-loop.
- Discrete variables; capacity computed by Blahut's algorithm to 10⁻⁴ bit.

## Key results

- **Definition (eq. 3, p. 130):** ℰ = C(p(s_{t+n} | aⁿ_t)) = max_{p(aⁿ)}
  I(Aⁿ_t; S_{t+n}), in bits; zero with no perceivable control. The sensor
  reading may be replaced by any function of variables downstream of A_t
  (the sensor sequence, or memory).
- **Context (p. 130–131):** the channel has state R; by the theory of
  channels with side information, "knowing the state of the channel may
  increase its capacity", so a compact context approximating R can raise
  empowerment and can be built "from the data available on-board". Not
  developed here.
- **Two ways to maximize it (§2.3):** go where p(s | aⁿ) is less noisy, or
  change the sensors and actuators.
- **Sensor evolution (§3.2, Figure 3).** 5 actions (stay or move to a von
  Neumann neighbour), sensors of ≤ 20 sampling points in a 21 × 21 square,
  fitness = 4-step empowerment − 10⁻³|S|. Best sensors: blobs near the
  source, arcs capturing bearing far from it; empowerment 4.322 bits at
  (0, 0) and (10, 0), 3.907 at (10, 10), 3.248 at (20, 0), 2.858 at (20, 10),
  2.807 at (20, 20).
- **Actuator evolution (§3.3, Figure 5).** Fixed 16-state bearing sensor,
  ≤ 10 actions within 4 cells: 4.000 bits near the centre, 2.807 farther out;
  "much larger" variety of optimal actuators than of sensors; with longer
  jumps all six places reach 4 bits, "constrained by the capacity of the
  sensor".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Empowerment is a universal, agent-centric utility | weak | definitional universality; utility argued from examples |
| C2 | Empowerment counts only control the agent can perceive | strong | definition: capacity to its own sensor |
| C3 | Empowerment as fitness switches the sensor's representation with the niche | moderate | one grid world, evolutionary search |
| C4 | Actuators are under less selective pressure than sensors | weak | one experiment; varied optima at equal fitness |
| C5 | Knowing the channel's state can raise empowerment | strong | standard side-information result (cited) |

## Concepts

- **Empowerment** — channel capacity from the agent's n actions to its later
  sensor state.
- **Actuation channel** — p(s_{t+n} | aⁿ_t), the agent's embodiment described
  by the effects of its actions on its sensors.
- **Context** — a variable approximating the channel's state.
- **Logical level** — actions identified by their effects on the sensor,
  sensors by how they see actions (§2.3).

## Connections

Ashby's law of requisite variety and Touchette and Lloyd's information
limits of control; Gibson's affordances; the authors' information-flow work.
Extended in Klyubin et al. 2008 ([LIT-tmp3h572](../literature.d/LIT-tmp3h572.md), [NOTE-tmpgoetm](NOTE-tmpgoetm.md)).

## Bearing on the record

- **[CLAIM-354](../claims.d/CLAIM-354.md).** Empowerment is a ready-made candidate for the claim's
  "viable reachability" dimension restricted to what the agent can tell
  apart: the capacity of the channel from its actions to its later sensor
  is the log of how many perceptibly different futures it can bring about,
  with noise priced in. Two points for the claim:
  - It is a scalar defined from the dynamics alone, with no task. That is the
    form the claim's defeater names. But the 2005 definition prices no
    control cost, imposes no viability set and is open-loop, so it agrees at
    best with one of the claim's dimensions; it does not collapse the
    profile. A neighbourhood empowerment that is equal for two agents whose
    reachable sets differ (the 4-bit ceiling set by the sensor, §3.3) is the
    claim's non-nesting in a single number: equal capacity, different sets.
  - The neurosurgeon point is the legibility restriction of the claim's note
    of 2026-11-02, built into the definition: control the agent cannot read
    does not count. Empowerment is legibility-limited reachability in exactly
    the sense [CLAIM-tmpkogzd](../claims.d/CLAIM-tmpkogzd.md) makes concrete, but measured by information
    rather than by sets.
- **A21's "controllability and observability together" (the registration
  of [LIT-tmp3h572](../literature.d/LIT-tmp3h572.md)).** Fair: the capacity is zero if the actions cannot move
  the sensor (uncontrollable) or the sensor cannot register the move
  (unobservable). It is an information measure, not a rank: a noisy channel
  with full rank has low empowerment.
- **[TERM-064](../terms.d/TERM-064.md).** "What it does not matter … what other agents perceive" (p.
  129) is legibility to oneself, not to a governing observer.

## Limitations

- Universality is by definition; whether empowerment tracks what organisms
  value is argued from examples (sugar, social status, money).
- One toy world; evolutionary search with a small arbitrary penalty.
- Open-loop only; contextual empowerment is named, not developed.

## Open questions

Whether closed-loop or context-dependent empowerment changes the sensor
result; how to compute it on-board without a world model, which the 2008
paper takes up.
