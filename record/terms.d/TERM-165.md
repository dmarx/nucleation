---
number: 165
status: Active
formerly:
- TERM-tmpwc4la
title: 'dispositional address'
statement: >-
  dispositional address, of a perspective under a declared probe family: the
  map from each admissible probe or intervention q to the law of the
  observed response, q ↦ P(Y | p, do(q)), taken up to observational
  equivalence under that family, so that a perspective is located by what it
  is disposed to do under the tests run and not by a label or a
  reconstruction of its goals; relative to the family, and so to the budget
  that affords it
version: 2
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 from A11 §§1–2 and A13 §4 of the exchange "Explain
    First Contact RL" (ChatGPT, shared 2026-11-22), at the owner's U5.
- version: 2
  date: '2026-11-24'
  note: >-
    Adopted (Active) at the owner's word of 2026-11-24 ("handle the
    fixes for the twelve ... use your best judgement", under the
    dialectic regime; ADR-057, status-review README section 2: a TERM is
    adopted when its definition is settled and every use says which
    sense it means). Its uses were checked: CLAIM-1044 (as A11's
    "relative to the tests we can afford to perform"), CLAIM-1095 (the
    relativity to a declared test family), CLAIM-1156 (the map q ↦ P(Y |
    p, do(q)) without the post-state, against which its kernel is set),
    CLAIM-1118 (a distance between the laws of the answers given),
    CLAIM-1175 (the address of probe sequences, the definition's second
    paragraph), CLAIM-1046, CLAIM-1196, SYNTHESIS-122, TERM-118,
    TERM-138 and QUESTION-531: all mean the one sense defined, the
    map from probes in a declared family to response laws, up to
    observational equivalence under that family. No change of wording;
    the definition has stood unrevised since 2026-11-22.
complements:
- TERM-116
- TERM-067
tags:
- individuation
- epistemology
- self
date: '2026-11-22'
line:
- distributed-agency
- formal-apparatus
summary: >-
  The owner's U5 asked after "Nucleation's account of addressing a
  perspective on a lattice by its dispositions (qua test functions)". The
  record holds the pieces and had no entry that puts them together for a
  perspective: dispositions ([TERM-118](TERM-118.md)), a profile of response kernels under
  declared interventions ([TERM-067](TERM-067.md)), observational equivalence under a
  probe family ([TERM-069](TERM-069.md)), the observational relational profile at a budget
  ([TERM-116](TERM-116.md)), and the result that the distinctions such profiles draw only
  grow along nested probe families ([CLAIM-574](../claims.d/CLAIM-574.md)). A11 assembled them as
  D_p: q ↦ P(Y | p, do(q)) and said itself that "This isn't a claim that
  Nucleation has formally identified perspectives with these functions.
  It's an operational construction from its existing account." Filed as a
  term so that a claim about where a perspective "is" can say under which
  family. The wording is A's (ChatGPT, in the exchange of 2026-11-22);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: TERM-118 TERM-116 CLAIM-052 — Proposed entries this definition is assembled from or sits beside, cited 2026-11-22 -->

# TERM-165: dispositional address

## Definition

Fix a perspective p (in the organizational sense of [TERM-072](TERM-072.md)), an admissible
family Q of probes or interventions, and an observable response Y. The
**dispositional address** of p under Q is the map

  D_p : q ↦ P(Y | p, do(q)),  q ∈ Q,

taken up to observational equivalence under Q ([TERM-069](TERM-069.md)): p and p′ have the
same address under Q when D_p(q) = D_p′(q) for every q in Q. The subsets of
the admissible probes, ordered by inclusion, index a family of such
addresses, one per resolution; along a nested chain of families the
addresses only split ([CLAIM-574](../claims.d/CLAIM-574.md)). This is the lattice in the owner's U5:
a lattice of probe families, and through it an ordered family of
observational partitions, not a lattice of perspectives (see [CLAIM-1046](../claims.d/CLAIM-1046.md)
for how far the two come apart).

When probing changes what is probed, so that p_{t+1} = F(p_t, q_t, Y_t)
(A11 §6, A13 §4), the address is of probe sequences, with their order kept,
not of single probes: the joint law across a sequence can separate what
each probe's marginal leaves equal ([TERM-069](TERM-069.md)'s last clause, [CLAIM-052](../claims.d/CLAIM-052.md)).

## What it is not

- **Not an identity criterion.** Equal addresses under every affordable
  family leave open whether p and p′ are one perspective: observational
  equivalence is coarser than identity unless the family is rich enough
  ([CLAIM-264](../claims.d/CLAIM-264.md)). Telling apart is descriptive individuation only ([TERM-088](TERM-088.md)).
- **Not the perspective.** A response profile can separate two perspectives
  without settling what organizes either ([CLAIM-454](../claims.d/CLAIM-454.md), [CLAIM-135](../claims.d/CLAIM-135.md); A11 §6:
  "identifying a perspective isn't constituting one"). A disposition read
  from responses can be masked, mimicked or finked ([TERM-118](TERM-118.md)).
- **Not [TERM-067](TERM-067.md)'s profile.** That one is of a state, for interventions on
  the mechanisms that govern efficacy, and its point is sufficiency of a
  description; this one is of a perspective, for any declared family, and
  its point is location.
- **Not [TERM-116](TERM-116.md)'s observational profile** exactly. That one records what the
  affordable tests tell a configuration from, with a minimum distinguishing
  budget; this one records the response laws themselves. The two agree on
  which pairs are told apart.
