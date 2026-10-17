---
status: Read
paper: 'LIT-tmpsbhb4'
title: 'Williams and Beer — Generalized measures of information transfer'
version: 1
history:
- version: 1
  date: '2026-10-17'
  note: >-
    Read in full from arXiv 1102.1507v1 (8 February 2011), 6 pp.: §§I–III,
    Figs. 1–6 from captions and prose, Appendices A (proof of Theorem 1)
    and B, references. Nothing skipped. Extracted with pdftotext. I
    recomputed the two-process family (SITE, SDTE, TE and TDMI at five
    values of d) and the three corners of the three-process family exactly
    with the I_min PID, with a script in the session scratchpad
    (te-checks/pid.py). I did not check the proof of Theorem 1 line by
    line, nor the sleep-apnoea analysis (Figs. 4–6), whose data and code
    are not given. The PID paper it applies (Williams and Beer 2010, arXiv
    1004.2515) was not read.
date: '2026-10-17'
summary: >-
  With the I_min partial information decomposition, transfer entropy
  T_{Y→X} = I(X_{t+1}; Y_t | X_t) is the unique information of Y_t about
  X_{t+1} (state-independent transfer, SITE) plus the synergy of X_t and
  Y_t (state-dependent transfer, SDTE). SITE alone suffices for perfect
  open-loop controllability (Theorem 1). Time-delayed mutual information
  is SITE plus redundancy. Two-source transfer splits into unique,
  redundant and synergistic parts. On a sleep-apnoea recording,
  heart→breath transfer is all SDTE.
---

# NOTE-tmpr176u: Williams and Beer — Generalized measures of information transfer

## Contribution

Before this preprint, transfer entropy gave the size and direction of an
influence but not its kind, and multivariate transfer entropy was built by
"conditioning out" other sources. After it, transfer entropy splits into
two kinds of transfer, and a multivariate version separates unique,
redundant and synergistic transfer. The split rests on one identity:
conditioning removes redundancy and adds synergy.

## Key insight

I(X; Y | Z) = Π(X; {Y}) + Π(X; {Y, Z}) for any decomposition satisfying
the PID consistency equations (Eqs. 4–6). Transfer entropy is a
conditional mutual information, so it carries a synergy term. The term is
the source's influence that only shows in combination with the target's
own state.

## Assumptions

- **The I_min redundancy** (Eqs. 2–3): the expected minimum, over sources,
  of the specific information about each target state. Every SITE, SDTE
  and multivariate number depends on it. The consistency equations, and
  hence the two-term split, do not.
- **Discrete processes with k- and l-step delay vectors** (Eq. 7). The
  examples use k = l = 1 on binary Markov chains.
- **Perfect controllability** in Touchette and Lloyd's sense for Theorem 1:
  for every initial x and final x′ some controller state c gives
  p(x′ | x, c) = 1.
- **Kernel density estimation** with Theiler-window exclusions for the
  physiological data (§III).

## Key results

- **Eq. 8.** T_{Y→X} = Π(X_{t+1}; {Y_t}) + Π(X_{t+1}; {X_t, Y_t}) =
  SITE + SDTE.
- **Theorem 1 (App. A).** A system is perfectly controllable with
  open-loop control iff it is perfectly controllable with only SITE from
  C to X′. Lemma 3: SDTE = 0 iff for each x′, p(c | x, x′) = p(c | x) for
  all x, c, or p(x | c, x′) = p(x | c) for all x, c.
- **Two-process family (Fig. 2).** Y fair coin; x_{t+1} = y_t if x_t = 0;
  if x_t = 1, x_{t+1} = y_t with probability 1 − d, else 1 − y_t.
  Stationary p(x, y) = ¼. *Checked exactly* (bits):

  | d | TE | SITE | SDTE | TDMI |
  |---|---|---|---|---|
  | 0 | 1.000 | 1.000 | 0.000 | 1.000 |
  | 0.25 | 0.594 | 0.456 | 0.138 | 0.456 |
  | 0.5 | 0.500 | 0.189 | 0.311 | 0.189 |
  | 0.75 | 0.594 | 0.046 | 0.549 | 0.046 |
  | 1 | 1.000 | 0.000 | 1.000 | 0.000 |

  TE = 1 − ½h(d), with redundancy zero throughout, so TDMI = SITE here. At
  d = 1, x_{t+1} = x_t ⊕ y_t, a controlled-NOT.
- **TDMI vs TE (Fig. 1).** I(X_{t+1}; Y_t) = SITE + redundancy. It counts
  shared history and misses SDTE.
- **Two sources (Fig. 3).** Redundant transfer is
  I_min(X_{t+1}; Y_t, Z_t | X_t); unique and synergistic transfer follow.
  *Checked at the corners:* (c, d) = (0, 0) gives 1 bit unique from Y;
  (1, 0) gives 1 bit redundant; (0, 1) gives 1 bit synergistic. The text
  labels the synergistic corner "(c = 1, d = 0)", a second time; by its
  own definitions it is (c = 0, d = 1).
- **Sleep apnoea (Figs. 4–6).** SITE between breath and heart is
  consistent with zero both ways, so TE and TDMI measure disjoint things
  there. Heart→breath transfer depends bimodally on chest volume. With
  blood oxygen as a second source, unique transfer is mostly from heart
  rate and essentially none from oxygen. Not checked.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Conditional MI = unique + synergy, so TE = SITE + SDTE | strong | Eqs. 4–8, from the consistency equations alone |
| C2 | SITE measures open-loop, SDTE closed-loop, influence | moderate | Theorem 1, for perfect controllability only; the graded reading is an analogy |
| C3 | TDMI includes redundancy and omits SDTE | strong | Fig. 1, from C1's identities |
| C4 | Multivariate transfer splits into unique, redundant and synergistic parts | moderate | definitions; corners checked; values elsewhere depend on I_min |
| C5 | Redundant transfer means interventions are needed to find the driver | interpretive | (c, d) = (1, 0) example; cites Ay and Polani |
| C6 | Heart→breath transfer in the apnoea data is purely state-dependent | weak | kernel estimates at several bandwidths; no significance test reported |

## Concepts

- **SITE** — Π(X_{t+1}; {Y_t}), the part of Y's influence that does not
  depend on X's state.
- **SDTE** — Π(X_{t+1}; {X_t, Y_t}), the part that does.
- **Specific information** — I(X = x; R), the information R gives about one
  outcome x (Eq. 3).
- **I_min, I_max** — the expected minimum and maximum of the specific
  informations over sources.

## Connections

- **Builds on** Schreiber (2000, LIT-tmpz9o5z) and Kaiser and Schreiber
  (2002, LIT-tmpfgfsh) for transfer entropy and the physiological data,
  Williams and Beer (2010) for PID, and Touchette and Lloyd for
  controllability. Lizier et al. (2008, LIT-tmps1x9k) and Frenzel and
  Pompe are named as conditioning-based multivariate transfer.
- **James, Barnett and Crutchfield (2016, LIT-tmpa6og3, NOTE-tmpt2aw8)**
  cite this as [18] for associating flow with unique information. Their
  Example 1 is this paper's d = 1 process. Here its bit is
  "state-dependent transfer"; there it is synergy that is not flow. The
  identities are the same. My observation.
- **[THEORY-497](../theory.d/THEORY-497.md) and [NOTE-010](NOTE-010.md).** ΦID extends this PID to multiple
  targets. [THEORY-497](../theory.d/THEORY-497.md) records that ΦID verdicts can turn on the redundancy
  function, citing a case where minimum-MI redundancy gives 1 bit of
  synergy and an identity-respecting one gives 0. I_min is neither of
  those, and the same sensitivity applies to SITE and SDTE away from the
  corners. My connection.
- **[THEORY-568](../theory.d/THEORY-568.md)** holds for any redundancy measure satisfying the
  consistency equations, which is the property C1 needs.
- **[NOTE-799](NOTE-799.md)'s open question**, a ΦID of transfer entropy, is in this
  paper's direction: the multivariate split here is a PID of a transfer
  entropy with the target's past fixed.

## Bearing on the record

- Filed as [THEORY-tmpt4nh7](../theory.d/THEORY-tmpt4nh7.md). With [THEORY-tmpijy6i](../theory.d/THEORY-tmpijy6i.md) it grounds
  [CLAIM-tmpu9ivq](../claims.d/CLAIM-tmpu9ivq.md) and the "what it is not" section of [TERM-tmpj9z04](../terms.d/TERM-tmpj9z04.md).
- [NOTE-788](NOTE-788.md) defines TE_{x→y}(τ) = I(y_{t+τ}; x_t | y_t), conditioning on one
  past value of the target, the k = l = 1 case of Eq. 7 at lag τ. It is
  still a conditional mutual information, so the decomposition applies.
- **For the Anthology of the SOTA:** no instruction for ML practice.

## Limitations

- An unrefereed preprint.
- I_min is not argued for here, and the record holds neither the PID paper
  nor its later critiques. The two-term split survives a change of
  redundancy measure; the sizes of the terms do not.
- Theorem 1 is about perfect controllability. That SITE and SDTE grade
  open-loop and closed-loop influence in general is an interpretation.
- Parameter-setting typo in the three-process example (above), and
  "X_{i+1}" for X_{t+1} in Eq. 8.
- The physiological result has no significance test and no shuffled
  baseline reported for SITE.

## Open questions

- Which redundancy measure SITE and SDTE should use, and how much the
  apnoea result depends on I_min.
- Whether "transfer" is the right word for SDTE, which [LIT-tmpa6og3](../literature.d/LIT-tmpa6og3.md)
  denies.
