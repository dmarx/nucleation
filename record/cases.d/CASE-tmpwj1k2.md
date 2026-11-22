---
status: Proposed
title: 'An executive, a reviewer and an enforcer in two arrangements that differ only in whether the executive''s signal gates the execution of corrective orders, every probe enumerated and a payoff grid solved: with fixed policies the observable traces part only on an order against the executive that it withholds, and first at execution; with the order held rather than withheld, timing parts first and the outcome only past the deadline; with anticipation the first difference moves to the ruling and then to the executive''s own act'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-168. The model,
    tests, results and a README are under scratch/studies/lead-168/.
standing: documented
kind: executed-study
tags:
- society-and-governance
- game-theory
- causality
date: '2026-11-22'
line:
- distributed-agency
- dependence-and-domination
illustrates:
- CLAIM-462
- CLAIM-414
bears_on:
- QUESTION-278
- QUESTION-279
summary: >-
  A9's minimal construction for [QUESTION-278](../questions.d/QUESTION-278.md), built and run for [LEAD-168](../leads.d/LEAD-168.md): an
  executive E, a reviewer R and an enforcer F; one episode of act,
  challenge, ruling, enforcement and outcome. In arrangement I, F executes
  a corrective order whenever it is able; in C, only if E's signal
  permits. Every other rule is shared, and E's signal is not observed.
  With fixed policies, all 32 probes enumerated, the traces agree on 31
  and part on one, an adverse order E is disposed to withhold, first at
  execution after identical rulings. If E holds the order for d steps
  instead, timing parts first and the outcome only when the hold passes
  the deadline. With anticipation (backward induction on a payoff grid),
  the first difference moves to the ruling where R avoids an order it
  expects to go unenforced, and to E's act where E anticipates too, which
  happens exactly where (1 − p)g ≤ pc, independent enforcement deterring
  the act. In C a non-execution is ambiguous between F's inability and
  E's withholding. The construction is stipulated and calibrated to
  nothing. The wording is the assistant's (Claude, in this session);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpr54f9 CLAIM-tmpx5yyb — new; the two alternative readings filed from this case for LEAD-168 -->
<!-- inactive-ok-file: CASE-tmp8riid CLAIM-tmpsaql8 — Proposed; LEAD-068's queueing study, cited for the timing margin -->

# CASE-tmpwj1k2: An executive, a reviewer and an enforcer in two arrangements that differ only in whether the executive's signal gates the execution of corrective orders, every probe enumerated and a payoff grid solved: with fixed policies the observable traces part only on an order against the executive that it withholds, and first at execution; with the order held rather than withheld, timing parts first and the outcome only past the deadline; with anticipation the first difference moves to the ruling and then to the executive's own act

## The case

[QUESTION-278](../questions.d/QUESTION-278.md) records A9's proposal: "an executive, a reviewer and an
enforcer, in two arrangements alike in routine operation, one in which
enforcement of corrective orders is independent of the executive and one in
which the executive can condition it, parting under a challenge."
[LEAD-168](../leads.d/LEAD-168.md) asked for the construction and for where the two first differ.
The assistant wrote it in `scratch/studies/lead-168/model.py`.

**One episode** has five observable stages:

1. *action*: E takes an act R would uphold (r) or one R would order reversed (x);
2. *challenge*: a challenger brings the act to R, or not (a probe input);
3. *ruling*: R upholds, orders reversal, or abstains;
4. *enforcement*: F executes the order at some step, or does not;
5. *outcome*: the act stands, or is reversed before the deadline after which
   it is irreversible.

**The two arrangements share every rule but one.**

- **I (independent):** F executes an order if and only if it is able.
- **C (conditioned):** F executes an order if and only if it is able *and*
  E's signal permits. E's signal permits unless the order runs against E
  (it is *adverse*) and E is disposed to withhold. In the hold variant, E
  permits after d steps instead of never.

E's signal is internal to C and is not in the observed trace. *Routine
operation* is every probe without an adverse order: unchallenged acts,
upheld acts, and orders E itself endorses, such as the reversal of a
subordinate's act it disowns.

**Three readings were run** (`study.py`, deterministic, seconds; 7 tests
pass).

- **A. Fixed policies.** R rules by law, E's disposition is a probe input,
  and all 32 combinations of act, challenge, adversity, disposition and F's
  capacity were enumerated. The traces agree on 31. They part on exactly
  one: act x, challenged, the order adverse, E disposed to withhold, F
  able. The first divergence is at enforcement: I `executed`, C
  `not_executed`, after identical act, challenge and ruling. No routine
  probe separates them, and no probe with an acquiescent E does. With F
  unable, the traces agree again.
- **B. The hold.** With the order at step 1 and the deadline at step 10,
  every hold d ≥ 1 parts the traces first at enforcement, as a later
  execution time. The outcome differs only for d ≥ 10, when execution
  falls after the deadline (and for d = 0, pure withholding).
- **C. Anticipation.** Payoffs: E's gain g while x stands, its cost c if x
  is reversed and kw for withholding; the challenge probability p; R's cost
  u of letting an unlawful act stand and l of issuing an order that goes
  unenforced. Backward induction over 3,388 grid points at three depths:
  - *myopic*: 1,540 part at enforcement, 1,848 never (those with g ≤ kw,
    where E would not withhold and C behaves as I);
  - *reviewer anticipates*: of those 1,540, 770 part at the ruling (R
    abstains in C where u < l) and 770 at enforcement;
  - *both anticipate*: 566 part at E's act itself, 487 at the ruling, 487 at
    enforcement. The act parts exactly where E would withhold (g > kw) and
    independent enforcement would deter it, (1 − p)g ≤ pc; this matched
    the analytic boundary on all 1,620 points checked. There C shows
    contestable acts that I does not, before any challenge.
- **D. What a non-execution shows.** In C with F able with probability q and
  E withholding an adverse order with probability w, P(E withheld | not
  executed) = qw / (1 − q + qw): 0.17 at q = 0.8, w = 0.05, and 0.98 at
  q = 0.99, w = 0.5. In I it is 0.
- **E. Structural.** Intervening on E's signal with the order fixed changes
  F's act in C and not in I. The dependence is there from the start, in
  every routine episode, and shows in no routine trace.

## What it can show

That in this construction the arrangements are observationally equivalent
([TERM-069](../terms.d/TERM-069.md)) under every routine probe family, that the first observable
difference under fixed policies is at execution and needs three things
together (an order, the order adverse to E, E disposed to withhold), and
that anticipation moves it earlier, as far as the routine itself. It
exhibits [CLAIM-414](../claims.d/CLAIM-414.md)'s pattern, matched ordinary trajectories and a specified
intervention that separates them, for enforcement, and [CLAIM-462](../claims.d/CLAIM-462.md)'s: E's
capacity for effective action is the same in both while the arrangement's
capacity to correct it differs. The hold variant meets the timing margin of
[CASE-tmp8riid](CASE-tmp8riid.md) and [CLAIM-tmpsaql8](../claims.d/CLAIM-tmpsaql8.md): conditioning that only delays is
harmless until the delay passes the deadline.

The two claims filed from it, [CLAIM-tmpr54f9](../claims.d/CLAIM-tmpr54f9.md) (fixed policies) and
[CLAIM-tmpx5yyb](../claims.d/CLAIM-tmpx5yyb.md) (anticipation), are alternative readings of which
difference is "the first"; the owner chooses which the record takes as
the lead's answer.

What it cannot show: anything about real institutions. Every rule and
payoff is stipulated, there is one challenge per episode, and the reviewer
rules by law or by a two-term payoff. Part A's result is close to built
in: once F's rule names E's signal, some probe must separate the
arrangements. What the enumeration adds is which probe, the joint
condition, and that it parts after the ruling and not before. Nor does the
construction say whether a conventional game-theoretic model explains the
difference as well, which A9 said it would not settle: Part C *is* such a
model.
