---
number: 458
status: Read
formerly:
- NOTE-tmpgl8bl
paper: LIT-566
title: 'Defining Agency: Individuality, Normativity, Asymmetry, and Spatio-temporality in Action'
version: 1
history:
- version: 1
  date: '2026-10-03'
  note: >-
    Read in full: the authors' version 1.0 (July 2009) from
    barandiaran.net, 14 pp., §§1–6, Table 1, Figure 1, footnotes 1–4 and the
    references. The journal pagination was not seen. Equations (1)–(3) are
    read from the text layer, which renders Eq. (3) as "∆p = HT(S), p ⊂ Q";
    the subscript T is the interval named in the text.
date: '2026-10-03'
summary: >-
  Minimal agency needs a self-individuated system that is the source of
  modulations of its coupling with the environment and regulates them by
  norms it generates. An autonomous organization, a precarious network of
  mutually enabling processes, generates all three when it adaptively
  modulates its coupling for its own maintenance. Life is sufficient, not
  necessary. The definition is a proposal: the authors say asymmetry's
  formalization is incomplete and modeller-relative.
---
<!-- inactive-ok-file: THEORY-071 — Proposed; named as the THEORY filed for this note's candidate, nothing here rests on it -->

# NOTE-458: Defining Agency: Individuality, Normativity, Asymmetry, and Spatio-temporality in Action

## Contribution

Before this paper, "agent" in adaptive behaviour and robotics was defined
by lists (perceives and acts; pursues goals; acts on its own behalf) whose
terms presupposed what was to be defined. The paper replaces the lists with
three conditions and then a *generative* definition: a type of organization
from which the three conditions follow, stated without using "agent",
"action" or "goal".

## Key insight

Being an agent is not a relation between a pre-given system and its world.
The system has to make itself a system (individuality), and the norms its
actions answer to have to come from the same organization that makes it.
Asymmetry then follows: the organization modulates its coupling because its
own continuation depends on it.

## Assumptions

- **Intuitive adequacy is a constraint.** The conditions are tested against
  ordinary uses of "action" (Table 1: gas, osmosis, tremor, warmed kitten,
  chemotactic bacterium).
- **Coupling is symmetric at base.** dS/dt = F_Q(S,E), dE/dt = G_Q(S,E)
  (Eqs. 1–2); asymmetry is modulation of a subset p of the constraints Q
  over an interval T, Δp = H_T(S) (Eq. 3). The constraints may be
  non-holonomic, so they cannot be re-described as variables.
- **Autonomy in Varela's sense,** applicable beyond metabolism: component
  processes may be chemical, physiological, neurodynamic, sensorimotor or
  social habits.
- **Emergent regulation (footnote 3).** Modulation must not be attributable
  to a subsystem acting as a central controller with a fixed norm, which
  would be an external constraint on the system.

## Key results

- **Individuality (§2.1).** An agent must distinguish itself from its
  environment without an observer, or explanation regresses through
  observers (Jonas 1968: identity "owned by, not loaned to its subject").
- **Asymmetry (§2.2).** Energetic criteria fail for the gliding bird;
  statistical-correlational criteria (citing Lungarella et al. 2007, Seth
  2007) fail for diver versus faller. Asymmetry is defined as the capacity
  to modulate the coupling at some times, at the extreme "just capable of
  halting a coupling".
- **Normativity (§2.3).** Norms "cannot be deduced from universal laws
  alone"; failure must be possible. Tremors are not actions.
- **Joint necessity and sufficiency (§2.4).** Individuality is a
  precondition of the other two. The authors "find it very difficult to
  conceive of any system that jointly fulfills these three criteria and it
  is not an agent".
- **Definition (§4).** S is an agent for coupling C with E iff (1) S is an
  open autonomous system: a network in which every process depends on at
  least one other and enables at least one other, which would run down in
  isolation; E is the set of processes that affect and are affected by S;
  S depends on conditions in E; and (2) S modulates C adaptively, i.e. so
  that some of its constituent processes are maintained.
- **Life is sufficient, not necessary (§3–4).** Protocellular metabolism
  plus membrane plus metabolism-dependent chemotaxis satisfies the
  definition.
- **Spatio-temporality (§5).** Agency is temporally structured (actions have
  onset, acceleration, consummation and cadence, after Di Paolo 2005) and
  spatially situated; a situated reactive controller can solve tasks a
  non-situated one cannot. The agent's perspective, not the observer's,
  fixes its spatial and temporal world. This section is declared "less
  rigorous".

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Individuality, interactional asymmetry and normativity are jointly necessary and sufficient for minimal agency | moderate | conceptual analysis against cases, Table 1 |
| C2 | Neither energetic nor statistical-causal measures suffice to define asymmetry | moderate | counterexamples (gliding bird; diver vs. faller) |
| C3 | An open autonomous system that adaptively modulates its coupling generates all three conditions | moderate | §4 derivation from the definition |
| C4 | Minimal living organization is sufficient for agency; life is not necessary | moderate | §3 protocell and chemotaxis; §4 |
| C5 | Systems optimizing an externally fixed function are not models of agency | moderate as a consequence of C3 | §6, consequence (b) |
| C6 | Agency expands in complexity mainly through its spatial and temporal dimensions | weak | §5, declared less rigorous |

## Concepts

- **Individuality.** The system's own distinction of itself from its
  surroundings; used interchangeably with "identity".
- **Interactional asymmetry.** The system's capacity to modulate the
  constraints on its coupling at certain times.
- **Normativity.** Regulation against a condition that can be failed, with
  the condition set by the system's organization.
- **Autonomous organization.** A precarious network of mutually dependent
  processes; captures "both the emergence of a self (autos) and that of
  norms (nomos)".
- **Sense-making.** Interaction becoming significant for the agent because
  actions compensate deviations from a self-generated norm.

## Connections

It builds on Varela's autonomy, Jonas's biological individuality,
Ruiz-Mirazo & Moreno (2000) and Christensen & Hooker (2000), widening the
latter two beyond metabolism. Sense-making is Di Paolo's (2005) and
Thompson's, the notion De Jaegher & Di Paolo ([LIT-571](../literature.d/LIT-571.md)) extend to social
interaction. Normativity is grounded with "Mossio et al. 2009"
([LIT-570](../literature.d/LIT-570.md)). Later, Bruineberg et al. ([LIT-603](../literature.d/LIT-603.md)) use the paper's
"interactional asymmetry" to name the arrow structure in a Friston blanket.

## Bearing on the record

- **Agent versus individual ([ADR-024](../decisions.d/ADR-024.md)).** This is the record's cleanest source
  for keeping `agency` and `individuation` apart: individuality is
  necessary for agency and insufficient for it.
- **Markov-blanket individuation ([LIT-526](../literature.d/LIT-526.md)).** The paper's criteria imply
  that a partition read off statistical dependencies does not by itself make
  an individual, and C2 rejects correlational asymmetry. It does not
  discuss Friston, whose paper is four years later; the bearing is the
  record's, not the authors'.
- **THEORY filed** as [THEORY-071](../theory.d/THEORY-071.md) (Proposed): minimal agency is an
  autonomous organization adaptively modulating its coupling for its own
  maintenance; individuality without asymmetry and self-generated norms is
  not agency.
- No instruction for machine-learning practice; consequence (b) is a
  remark about what counts as a model of agency, not a training method.

## Limitations

- The authors call the modulation formalization incomplete: "what counts as
  a parametric modulation and what as a coupling between variables is often
  a matter of choice for the modeler".
- How a system can be "sensitive" to norms that emerge from holistic
  dependencies is left open, as is the status of reflexes.
- No model is analysed; the definition is checked only against intuitive
  cases.

## Open questions

- A modeller-independent criterion for interactional asymmetry, which the
  authors themselves ask for.
- Measures of individuality (closure, e.g. via category theory) and of
  normativity (homeodynamic stability) that would let the definition be
  applied "almost automatically" to a model, which is the test the authors
  set for their own definition.
