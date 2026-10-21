---
status: Read
paper: LIT-tmp5l842
title: 'Arthur — Competing technologies and historical small events (working paper)'
version: 1
history:
- version: 1
  date: '2026-10-21'
  note: >-
    Read in full, but not the article the LIT names. No lawful copy of the
    Economic Journal article (1989) was reached: Unpaywall and OpenAlex
    report it closed, Semantic Scholar has no open PDF, and the JSTOR page
    is paywalled. What was read is its precursor, W. Brian Arthur, "On
    Competing Technologies and Historical Small Events: The Dynamics of
    Choice under Increasing Returns", IIASA Working Paper WP-83-90
    (September 1983), the scanned copy in IIASA's repository
    (pure.iiasa.ac.at/id/file/4454), text extracted with pdftotext from
    the scan's OCR layer. Read: the abstract, the introduction, §I (the
    model), §II (the three regimes, Table 2, and the extensions), §III
    (examples, historical explanation, policy and prediction), §IV and the
    footnotes. The OCR garbled the displayed inequalities (1)–(2), the
    absorption probability and the figures. The inequalities and the
    probability are re-derived in THEORY-tmpxzls4 and the figures read from
    the text. The 1989 article was not seen, so where the two differ this
    note speaks only for 1983.
date: '2026-10-21'
summary: >-
  In a model where two types of agent arrive in random order and each
  adopts whichever of two technologies pays it more, with returns linear in
  the number of previous adopters, increasing returns make the difference
  in adoptions a random walk with absorbing barriers: one technology takes
  the market with probability one, which one is decided by the order of
  arrivals, it need not be the better one, and marginal subsidies cannot
  move it once it has locked in. Under diminishing returns the barriers
  reflect and the market shares predictably.
---
<!-- inactive-ok-file: THEORY-429 — Proposed; a held reading named for comparison, nothing here rests on it -->
# NOTE-tmpyyaar: Arthur — Competing technologies and historical small events (working paper)

## Contribution

It makes the indeterminacy of markets with increasing returns analysable.
Instead of saying that several equilibria exist and stopping, it adds
"historical small events", here the order in which agents arrive, to the
model and follows how they accumulate. It names four properties the
increasing-returns process lacks and the diminishing-returns one has:
efficiency, flexibility, predictability and ergodicity. It shows all four
failing in a model simple enough to settle with the theory of random walks.

## Key insight

"Small events" are whatever lies "outside the knowledge of the observer —
beyond the resolving power of his 'model'". Under diminishing returns they
average away, since the process "forgets its small-event history". Under
increasing returns each adoption raises the payoff to the next one, so an
early lead makes everyone choose the leader, and the process "remembers its
small-event history". Complete knowledge of supply and demand then says
that one technology will win and the odds of each, but not which.

## Assumptions

- Two technologies, A and B, open to all and "not subject to strategic
  influence or manipulation". An infinite pool of agents, each of whom
  adopts once, when his old equipment dies, and keeps what he chose.
- Two agent types, R and S, in equal numbers. Returns are linear in
  previous adoptions: for an R-agent a_R + r n_A for A and b_R + r n_B for
  B, for an S-agent a_S + s n_A and b_S + s n_B. a_R > b_R and a_S < b_S,
  so R prefers A and S prefers B at the start. Increasing, constant and
  diminishing returns are r, s > 0, = 0 and < 0.
- Agents are rational, fully informed of current returns, and myopic in
  structure: returns do not depend on future adoptions, so expectations
  play no part, and nobody can wait.
- The observer knows everything except the times of choice. To him the
  sequence of R and S agents is a fair coin.
- Definitions, verbatim in substance: the outcome is *predictable* if a
  forecast sequence comes ever closer to the market share with probability
  one; *flexible* if a change of either returns function by an arbitrarily
  small ε from any stage on can change future choices; *ergodic* if two
  sequences of small events lead to market shares whose difference goes to
  zero with probability one; *efficient*, as a search procedure, if no
  adopted option has lower returns to either agent type than an unadopted
  one.

## Key results

- **One agent type.** With diminishing returns adoption follows the
  composite supply curve and the market is shared. With increasing returns
  the first agent's choice is chosen by all the rest: "A 'corners the
  market' and B is excluded." If returns rise at different rates, the
  winner can be the worse technology, and no marginal policy can close "the
  finite gap between the returns to A after n adoptions and the returns to
  B at the starting point".
- **Constant returns.** R-agents always choose A, S-agents B, so
  d_n = n_A − n_B is a fair random walk, d_n/n → 0 and shares go to one
  half.
- **Diminishing returns.** Agents switch to the technology that is behind
  once the gap is large enough. d_n is a random walk with reflecting
  barriers, trapped between constants, and shares go to one half.
- **Increasing returns.** R-agents switch to B once B is far enough ahead,
  and S-agents to A once A is. The boundaries "absorb" the process. d_n is
  absorbed with probability one, so "the two technologies cannot coexist
  indefinitely". The observer can give the probability that A wins (the
  OCR garbled the expression; re-derived as Δ_R/(Δ_R + Δ_S) with
  Δ_R = (a_R − b_R)/r and Δ_S = (b_S − a_S)/s in [THEORY-tmpxzls4](../theory.d/THEORY-tmpxzls4.md)), but not
  the outcome.
- **Table 2.** Necessarily efficient, necessarily flexible, predictable,
  ergodic: constant returns yes, no, yes, yes; diminishing returns yes,
  yes, yes, yes; increasing returns no, no, no, no.
- **Extensions.** The same holds for N technologies and unequal
  proportions of types (the walk drifts). With finite agents, absorption
  has probability less than one. With nonlinear "parallel" returns the
  barriers stay constant and the results hold. With returns that level off
  at different heights the case approaches constant returns, and both
  technologies can share the market.
- **Policy.** Subsidizing the technology that has fallen behind "pushes
  policy onto a razor-edge. Small subsidies to the excluded choice will not
  re-establish it; large subsidies, on the other hand, will swing the market
  and drive the dominant choice out." A planner with a favoured outcome
  should "'tilt' the process economically toward the favored technology at
  the outset". "With increasing returns ... timing becomes all-important."

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | In the model, increasing returns make the adoption process converge with probability one to the exclusion of one technology | strong | random walk with absorbing barriers; re-derived and simulated in [THEORY-tmpxzls4](../theory.d/THEORY-tmpxzls4.md) |
| C2 | Which technology wins is decided by the order of arrivals, so the outcome is not predictable from the returns functions, though its probability is | strong | gambler's ruin on the barriers |
| C3 | The locked-in outcome need not be the more efficient, and marginal changes to returns cannot dislodge it | strong in the model | one-type case (Fig. 1) and the absorbing barriers |
| C4 | Under constant or diminishing returns the outcome is predictable, ergodic and (with diminishing returns) flexible | strong | random walk without barriers or with reflecting ones |
| C5 | The results extend to N technologies, unequal type shares and parallel nonlinear returns, and weaken when barriers vary with n | moderate | stated, not proved in the paper |
| C6 | QWERTY, British rail gauge, US colour television and gasoline over steam are historical instances | weak | narrative examples, with a NASA study cited for steam |
| C7 | Historical explanation that looks for the winner's superiority is valid only under constant and diminishing returns | moderate | follows from C4 and C1 within the model |
| C8 | Exact economic prediction may be impossible in principle where increasing returns amplify events below a model's resolution | weak | speculation by analogy to weather forecasting |

## Concepts

- **Competing technologies**: ways of fulfilling one purpose, such that
  adopting one tends to displace or preclude another, competing "in the
  unconscious, passive sense".
- **Historical small events**: events or conditions "outside the knowledge
  of the observer", here the times of choice. Not "pure chance": "Randomness
  follows then from lack of knowledge."
- **Lock-in**: absorption of the process into a region where both types
  choose the same technology.
- **Non-ergodicity**: dependence of the limit on the sequence of small
  events.

## Connections

It cites Marshall's case of firms with falling cost curves, where the winner
is "whichever firm first gets a good start", Schelling (1978), David (1975)
for ergodicity in economic history, and Arthur, Ermoliev and Kaniovski (1983)
for the generalized urn schemes behind the heterogeneous-agent extension.
The 1989 article in the LIT is its published successor.

## Bearing on the record

- **[THEORY-tmpxzls4](../theory.d/THEORY-tmpxzls4.md).** Filed Active: C1–C4 in the 1983 model, re-derived
  and simulated.
- **[CLAIM-tmpptl3y](../claims.d/CLAIM-tmpptl3y.md).** A19 cited Arthur for "early contingencies can select
  durable technological advantages without an intrinsic superiority". That
  is C1–C3. The two models differ where the claim says its own result
  stops. In [CLAIM-tmpptl3y](../claims.d/CLAIM-tmpptl3y.md), restoring κ > α restores the equal allocation:
  no hysteresis in the constraint. In Arthur's model the lock-in is an
  absorbing state. Once it is reached, a marginal change in returns has no
  purchase, and only a large one reverses it, by driving the other side out
  (the razor-edge). So Arthur supplies, in a different model, the
  persistence that [CLAIM-tmpptl3y](../claims.d/CLAIM-tmpptl3y.md) says its pitchfork lacks, and the reason:
  the advantage is stored in accumulated adoptions, a state variable that
  does not decay when the conditions are reversed. Neither model has the
  advantaged party acquiring authority over the rule, the route
  [CLAIM-tmpptl3y](../claims.d/CLAIM-tmpptl3y.md) names. The comparison is the record's.
- **[CASE-112](../cases.d/CASE-112.md).** Arthur's planner who "tilt[s] the process ... at the outset"
  is [CASE-112](../cases.d/CASE-112.md)'s tilt h applied before the symmetry breaks. Arthur adds that
  the same small tilt has no effect after lock-in, which is [CASE-112](../cases.d/CASE-112.md)'s
  hysteresis in h.
- **Neutral rules, unequal outcomes.** Arthur's process is symmetric in the
  technologies when a_R − b_R = b_S − a_S and r = s, and still ends with
  one of them holding the whole market. That is A19's "The rules of motion
  remain symmetric. The realized organization does not", in a stochastic
  rather than a deterministic model.
- **[THEORY-429](../theory.d/THEORY-429.md)** (North) carries increasing returns from technologies to
  institutional matrices, which Arthur's 1983 paper does not do.

No instruction for machine-learning practice; nothing for the anthology.

## Limitations

- **Not the published article.** The 1989 *Economic Journal* version was
  not reached. Its framing, extensions and examples may differ, and the
  LIT's claims about it rest on this precursor.
- **A very special model.** Two types, equal numbers, returns linear in
  past adoptions, no expectations, no pricing, no strategic sponsors.
  Arthur names each of these as open.
- **"Efficiency" is weak.** It is a search criterion (no unadopted option
  better than an adopted one), and the paper notes that greedy choice does
  not maximize aggregate payoff even when it holds.
- **Examples are narrative.** The QWERTY and steam-car stories are offered
  as illustrations and are not analysed. Their history has since been
  disputed in the literature, which the record does not hold.
- **Extensions asserted.** The N-technology, unequal-proportion and
  nonlinear results are stated without proof.

## Open questions

- Arthur's own: which increasing-returns dynamics have these properties,
  and what changes with strategic sponsors, expectations, or agents who can
  wait?
- For the record: is there a model in which an advantage selected by
  symmetry breaking persists after the constraint is restored because the
  advantaged party stores it (in adoptions, resources or authority over the
  rule)? Arthur's accumulated adoptions are one such store. [CLAIM-tmpptl3y](../claims.d/CLAIM-tmpptl3y.md)
  names another and does not model it.
