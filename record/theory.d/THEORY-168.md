---
number: 168
status: Active
formerly:
- THEORY-tmpjdnxt
title: 'In Contextuality-by-Default, whether a fixed set of measurements is contextual depends on how the system is represented: which couplings are imposed, and which dichotomizations of the variables are included'
version: 3
history:
- version: 2
  date: '2026-10-19'
  note: >-
    At the owner's direction, carrying out the promotion audit's decision
    (record/promotion-audit/decisions/THEORY-168.yaml, batch 005, ADR-047),
    the proved part is filed apart as THEORY-722, Active: coarse-graining
    can turn a noncontextual CbD 2.0 system into a contextual one, and CbD 1.0
    and 2.0 agree on two-variable connections and on consistently connected
    systems. This THEORY extends it and keeps what is asserted or waiting on a
    second proof: the disagreement of maximal and multimaximal couplings on
    larger connections, and Theorem 4.6. The title, the promote_when and the
    status are unchanged.
- version: 3
  date: '2026-10-29'
  note: >-
    Promoted by the twelfth status review (ADR-057; ADR-047's ruling on
    re-derivations, and the owner's ruling of the tenth pass). The
    promote_when asked for "Two things together. First, a checked second
    proof of the nominal-dominance theorem for one pair of content-sharing
    variables, for example from later Contextuality-by-Default work.
    Second, a worked system that shows the remaining asserted case: an
    inconsistently connected system that is noncontextual under maximal
    (CbD 1.0) couplings and has a contextual subsystem." Both are in the
    note of this date, each checked by a numpy script the reviewing
    session ran. Item 1 names the worked case, and the summary says that
    binary connections first disagree at four contexts; it said "Maximal
    and multimaximal couplings disagree when a content appears in three or
    more contexts." Title unchanged.
tags:
- contextuality
- mathematics
date: '2026-10-09'
source:
- LIT-790
- LIT-831
- LIT-777
extends:
- THEORY-722
summary: >-
  Dzhafarov, Cervantes & Kujala (2017), [LIT-790](../literature.d/LIT-790.md), with Dzhafarov &
  Kujala's CbD 2.0 ([LIT-831](../literature.d/LIT-831.md)) and CbD 1.0 ([LIT-777](../literature.d/LIT-777.md)). The same
  measurements can receive different verdicts. Maximal and multimaximal
  couplings can disagree when a content appears in three or more contexts
  (four, for binary variables), and the record's worked case shows it.
  Multimaximal couplings of non-binary variables can be destroyed by
  coarse-graining. With every dichotomization kept, two content-sharing
  variables are contextual on their own unless one nominally dominates the
  other. The authors present the representation as the analyst's choice,
  not as a defect. What the record does not get from these papers is any
  rule for choosing it.
supports:
- CLAIM-069
---

<!-- inactive-ok-file: THEORY-013 — Proposed; its scope is what this theory bears on -->

# THEORY-168: In Contextuality-by-Default, whether a fixed set of measurements is contextual depends on how the system is represented: which couplings are imposed, and which dichotomizations of the variables are included

## Source

Dzhafarov, Cervantes & Kujala (2017), [LIT-790](../literature.d/LIT-790.md), Sections 1, 3–5 and the
supplement ([NOTE-640](../notes.d/NOTE-640.md)). Dzhafarov & Kujala (2017), [LIT-831](../literature.d/LIT-831.md),
Sections 1, 4 and 6 ([NOTE-643](../notes.d/NOTE-643.md)). Dzhafarov & Kujala (2016), [LIT-777](../literature.d/LIT-777.md),
Definition 3.4 ([NOTE-600](../notes.d/NOTE-600.md)).

## What was actually shown

Contextuality-by-Default gives each measurement a separate random
variable in each context. A system is noncontextual when some coupling of
the contexts restricts, on each content, to a prescribed coupling of that
content's copies. The verdict therefore depends on two choices: which
coupling is prescribed, and which variables are in the system. Each choice
has been made in more than one way:

1. **Maximal vs multimaximal couplings.** CbD 1.0 ([LIT-777](../literature.d/LIT-777.md)) prescribes a
   maximal coupling of each whole connection. CbD 2.0 ([LIT-831](../literature.d/LIT-831.md))
   prescribes a multimaximal one, with every subset (equivalently every
   pair) maximally coupled. The two agree for connections of two
   variables, hence for cyclic systems, and for consistently connected
   systems. The authors say they disagree on Kochen–Specker systems with
   more variables per connection. They state, without an example, that the
   1.0 definition is not hereditary; the note of 2026-10-29 gives one.
2. **Coarse-graining non-binary variables.** Under multimaximality,
   coarse-graining can turn a noncontextual system into a contextual one.
   This is proved by example: a 6-valued connection with two multimaximal
   couplings becomes, after lumping, a 3-valued connection with none
   ([LIT-831](../literature.d/LIT-831.md), Examples 1–3).
3. **Which dichotomizations to include.** The canonical representation
   ([LIT-790](../literature.d/LIT-790.md)) replaces each variable by binary splits, and the analyst
   chooses which coarsenings to add. With all splits of two
   content-sharing k-valued variables, the pair is noncontextual if and
   only if Pr[R = x] < Pr[R′ = x] holds for at most one value x, in one
   direction or the other (Theorem 4.6, proved in the supplement). With
   only the k one-value splits, the same pair is always noncontextual.
   For continuous densities with all splits, any difference in
   distribution is contextual (Section 5, an argument rather than a
   theorem).

What could have come out otherwise: Theorem 4.6 could have found that the
all-splits system of one pair is always noncontextual, as the unsplit pair
is. The proof shows instead that the maximal couplings of the 1- and
2-splits over-determine the k × k joint table.

## What this does not say

- **Not that CbD is inconsistent.** Each version is internally coherent.
  The authors adopt multimaximality and the canonical form deliberately,
  and present the expansion as the analyst's statement of interest.
- **Not that every verdict in the CbD literature changes.** Binary cyclic
  systems, which carry most published analyses, are judged the same under
  1.0, 2.0 and the canonical form (their variables are already binary,
  and each connection has two). [THEORY-013](THEORY-013.md)'s findings are of this kind.
  They are untouched for binary data. They do not carry over to
  multi-valued responses analysed canonically, where Theorem 4.6 makes
  contextuality easy to find.
- **Not a statement about the sheaf framework.** There, a model is
  no-signalling by definition, and coarse-graining outcomes cannot raise
  the contextual fraction ([LIT-265](../literature.d/LIT-265.md), Theorem 2). The contrast concerns how
  each framework handles coarse-graining, and the papers do not compare
  them.
- **Not a rule for choosing.** The papers suggest that intervals or cuts
  may be more natural for ordered values. They do not develop it.

## Note of 2026-10-19: the proved part filed apart

Item 2 above, the coarse-graining failure, and the agreement of CbD 1.0 and
2.0 stated in item 1 are now [THEORY-722](THEORY-722.md), Active, sourced to [LIT-831](../literature.d/LIT-831.md).
What keeps this THEORY Proposed is the rest of the title's first clause.
[LIT-831](../literature.d/LIT-831.md) asserts that maximal and multimaximal couplings disagree on larger
connections, with no worked example, and Theorem 4.6 is waiting on a second
proof. The promote_when says what would settle both.

## Note of 2026-10-29: Theorem 4.6 re-proved, and the CbD 1.0 non-heredity case worked

**Theorem 4.6, by a second route.** With all splits of R and R′ (values
1, …, k, with laws p and p′), a coupling is a joint table J. The split pair
for a set S is maximally coupled exactly when the probability that the
splits differ, J(S, Sᶜ) + J(Sᶜ, S), equals |p(S) − p′(S)| =
|J(S, Sᶜ) − J(Sᶜ, S)|, that is, when one of the two is zero. Call x → y,
with x ≠ y and J(x, y) > 0, a transfer. S = {x} forbids a value that both
sends and receives. Two transfers a → b and c → d with a ≠ c and b ≠ d are
forbidden by S = {a, d}. So any two transfers share a source or a target,
and then all of them share one source or all share one target. All from one
source x₀ means p(x) ≤ p′(x) except at x₀; all into one target means
p(x) ≥ p′(x) except at one value. Conversely, if p > p′ at most at x₀, the
table with diagonal min(p, p′) and x₀'s excess sent to the deficits
satisfies every split, and symmetrically. With only the one-value splits,
sending each surplus value's excess to the deficit values always works, so
the pair is always noncontextual. The proof does not go through the 1-2
subsystem or Eq. (23), as the supplement's does. For k = 3 one of the two
conditions always holds, so the effect needs four values. Checked by brute
force (numpy, run by the reviewing session: every choice of forbidden
direction per split, feasibility by maximum flow) on 400, 300 and 12 random
pairs for k = 3, 4 and 5. It agreed with nominal dominance on all of them,
and found 89 and 5 contextual pairs for k = 4 and 5.

**A CbD 1.0-noncontextual system with a contextual subsystem.** A binary
content q is measured in contexts c₁, …, c₄ with Pr[V = 1] = 0.1, 0.4, 0.6
and 0.9. A binary content s is measured in c₂ and c₃, with W₂ = V₂ in c₂,
and W₃ distributed as Bernoulli(0.4) independently of V₃ in c₃. The
s-connection is consistent, so its maximal coupling is W₂ = W₃, which forces
V₂ = W₃ and so makes V₂ independent of V₃: Pr[V₂ ≠ V₃] = 0.52. Under CbD 1.0
the whole q-connection needs only Pr[all four equal] = 0.1 + 0.1 = 0.2, and
a coupling attains it with V₂ and V₃ independent, V₁ = 1 on a 0.1 sub-event
of V₂ = V₃ = 1 and V₄ = 0 on a 0.1 sub-event of V₂ = V₃ = 0. So the system
is noncontextual under 1.0. Under CbD 2.0 the pair (V₂, V₃) must be
maximally coupled, with Pr[V₂ ≠ V₃] = 0.2, so the system is contextual; and
the subsystem without V₁ and V₄ is contextual under 1.0 as well. With binary
variables a connection of three has a unique maximal coupling, the staircase
of [LIT-831](../literature.d/LIT-831.md)'s Theorem 1, so 1.0 and 2.0 first disagree at four contexts.
