---
number: 338
status: Proposed
formerly:
- CASE-tmpkghqb
title: 'Audited governance against a router matched on audits, delay and cost, built in numpy: frozen low-rank specialist denoisers after a reversal of expertise, with one arm each for cycles, no common scale, capture, bandit feedback and continued training; governance wins only against a router weaker in a stated respect, and the best router matches or beats the best governance in every arm'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-077. The
    simulator, its tests and the results are committed under
    scratch/studies/lead-077/.
standing: documented
kind: executed-study
tags:
- self-governance
- learning-theory
- complex-systems
date: '2026-11-22'
line:
- distributed-agency
variant_of:
- CASE-158
bears_on:
- QUESTION-271
draws_on:
- THEORY-937
- THEORY-932
summary: >-
  [CASE-158](CASE-158.md)'s design, built and run for the first time in the record, with
  the router given the same audit records, the same one-episode delay and
  the same number of probes as governance, and one arm per failure of
  [QUESTION-271](../questions.d/QUESTION-271.md) plus continued training. Eight arms, 3 gate temperatures, 12
  paired seeds, held-out truth. Under full information governance beats the
  contextual router at two of three temperatures, but loses at the one both
  do best at, and a router that sees only the region id, as governance's
  grants do, beats it on 12 of 12 seeds at every temperature. The router
  wins the cycles and capture arms. Governance wins the no-common-scale
  arm only by standardizing each member against its own history; given the
  same standardization the router ties it. Under bandit feedback, a 10%
  floor on auditing lets governance beat a router with the same floor,
  not the router without one. Continued training entrenched neither. The
  wording is the assistant's (Claude, in this session); adopting it is the
  owner's call.
---
<!-- inactive-ok-file: CLAIM-906 — new; the claim this run grounds, cited for the owner's reading of the defeat condition -->

# CASE-338: Audited governance against a router matched on audits, delay and cost, built in numpy: frozen low-rank specialist denoisers after a reversal of expertise, with one arm each for cycles, no common scale, capture, bandit feedback and continued training; governance wins only against a router weaker in a stated respect, and the best router matches or beats the best governance in every arm

## What was done

[LEAD-077](../leads.d/LEAD-077.md) asks for [CASE-158](CASE-158.md)'s run "with the router matched on audit delay
and cost, adding one arm per failure [QUESTION-271](../questions.d/QUESTION-271.md) lists". [CASE-158](CASE-158.md)'s
software is not held, so the design was built anew in numpy
(scratch/studies/lead-077/, README there). It is a construction to the
case's description, not a reproduction of A47.

- **Content and specialists.** Four content types, each a rank-4 Gaussian
  in a 16-dimensional patch; four regions; region r holds type r, and type
  r+1 from episode 42 of 84 (the reversal). Specialist k's operator is the
  rank-4 eigenbasis of type k's training covariance with Wiener shrinkage,
  fitted beforehand and frozen.
- **One shared latent.** Five deterministic scheduler steps from noise 1.0
  to 0.1; at each step every specialist proposes and the allocation
  combines the proposals per region.
- **Audits.** 8 probes per region and episode: held-out patches with known
  injected noise; the record is each specialist's one-step error. Audits of
  episode e are usable from episode e+1 only, by governance and router
  alike, and both draw the same 2688 probes per run, so the audit cost is
  the same.
- **Allocators.** Fixed (uniform); governance (an exponential average of
  audited competence per region and specialist, and grants that move with
  inertia toward a softmax of it); conformity (the same update, scored by
  each proposal's distance from the combined proposal, unaudited); router
  (a linear predictor of each specialist's score from the region id, each
  specialist's captured energy of the noisy patch and the noise level,
  refitted on the same audit records with the same forgetting; gate by
  softmax, per item and step: a mixture of experts whose experts earn
  responsibility by fitting better, [THEORY-937](../theory.d/THEORY-937.md)). An oracle allocation
  gives a floor.
- **Choices the lead left open.** The gate temperature, shared by
  governance and router, was swept (0.03, 0.1, 0.3), and each was also
  compared at the temperature it does best at before the reversal, so
  neither is judged at a setting tuned for the other. The post-reversal
  window (episodes 42 to 83) is scored, never used for tuning.

The arms, each applied to governance and router alike:

| Arm | Failure of [QUESTION-271](../questions.d/QUESTION-271.md) | What changes |
|---|---|---|
| full | none | every proposal probed, independent probes |
| cycles | 1 | three specialists, each strong on one subtype and weak on the next; regions mix subtypes 0.4/0.3/0.3, so pairwise wins cycle (checked by test); audits are duels, win or loss only |
| scale | 2 | each specialist's score is reported in its own monotone units; governance standardizes each member against its own history; controls: governance without it, and a router given it |
| capture50, capture80 | 3 | that share of probe slots is chosen by the region's incumbent (the allocator's own top specialist) as the most favourable of 16 candidates, and entered twice |
| bandit | 4 | each probe audits one specialist, drawn from the allocator's own allocation; variants with a 10% floor on auditing |
| training | entrenchment | each specialist keeps training on the regions it is granted, in proportion to the grant |
| full_rr | none (a check) | the full arm with a router that sees only the region id and noise level, as governance's grants do |

## Results

Post-reversal held-out mean squared error, mean of 12 seeds, each at its
best pre-reversal temperature (0.3 unless noted); "G wins" counts seeds
on which governance had the lower error. The oracle floor is 0.1472 and
fixed allocation 0.2484 in every arm but cycles.

| Arm | Governance | Router | G wins |
|---|---|---|---|
| full | 0.1557 | 0.1534 | 1/12 |
| full, router seeing the region id only | 0.1557 | 0.1478 | 0/12 |
| cycles | 0.2098 | 0.1949 | 0/12 |
| scale, raw router (τ 0.1) | 0.1609 | 0.2118 | 12/12 |
| scale, router given the same standardization (τ 0.1, 0.3) | 0.1609 | 0.1608 | 6/12 |
| capture 50% | 0.1711 | 0.1634 | 0/12 |
| capture 80% | 0.1827 | 0.1588 | 0/12 |
| bandit, no floor | 0.1664 | 0.1620 | 3/12 |
| bandit, both with a 10% audit floor | 0.1625 | 0.1666 | 12/12 |
| training | 0.1594 | 0.1553 | 1/12 |

1. **Full information turns on the temperature.** With a shared gate
   temperature of 0.03 or 0.1 governance beats the contextual router on 12
   and 11 of 12 seeds (mean differences 0.0062 and 0.0034); at 0.3, the
   best for both before the reversal, the router wins on 11 of 12. Before
   the reversal governance is the better of the two at every temperature:
   the contextual router gates each item from a noisy patch and pays for
   it in steady state, and recovers faster after the reversal. The router
   that sees only the region id has the same steady state as governance
   (pre-reversal difference under 0.0005) and beats it after the reversal
   on 12 of 12 seeds at every temperature (by 0.0042 to 0.0079).
   Governance's edge over the contextual router was the router's noisy
   context, not anything governance uses that a router cannot.
2. **Cycles.** Governance (duel win rates per region) does no better than
   fixed allocation (0.2098 against 0.2090), and the region's dominant
   specialist (0.2322) does worse than either. The router routes each item
   by its content and wins 12 of 12 at every temperature. Intransitive wins
   among specialists hurt an allocation per region, not one per item.
3. **No common scale.** A router trained on raw scores in incommensurable
   units chooses by unit, and loses 12 of 12 to governance that scores each
   member against its own history; governance without that
   standardization loses 12 of 12 to the raw router. Given the same
   standardization, the router ties governance (6 of 12, means 0.1609 and
   0.1608). What wins is the normalization, which either mechanism can
   carry: [QUESTION-271](../questions.d/QUESTION-271.md)'s "factored" regime, in which a member's own
   ranking is enough.
4. **Capture.** At 80% curated probes the router wins 12 of 12 at every
   temperature, and the gap widens (0.0200 to 0.0239). At 50% governance
   wins at the low temperatures (10 of 12 at 0.03), the steady-state edge
   of finding 1, and loses 12 of 12 at 0.3. A likely reading, not
   tested: governance's inertia and per-region averages hold the incumbent
   longer against curated evidence than the router's forgetting fit does.
5. **Bandit feedback.** Without a floor on auditing governance starves the
   unheeded specialists and loses (0 and 1 of 12 at 0.03 and 0.1). A 10%
   floor, protected access in the audit, cures it: governance with the
   floor beats the router with the same floor on 12 of 12 at 0.3. But the
   router without a floor (0.1620) does as well as governance with one
   (0.1625): its soft gate already explores, and the floor costs it.
   [THEORY-932](../theory.d/THEORY-932.md)'s point, that only the chosen option is updated, is what the
   floor answers, and it answers it for either mechanism.
6. **Continued training.** Specialists trained on the regions they are
   granted did not entrench under governance or router: weight on each
   region's pre-reversal specialist over the last ten episodes is 0.00 to
   0.05 for both. The incumbent learns the new content slowly at rate 0.1
   while the right specialist is already competent, so the access loop of
   [CLAIM-277](../claims.d/CLAIM-277.md) did not have time to bind. Conformity kept 0.06 to 0.14 of
   its weight there.

Conformity scoring was worse than fixed allocation in the full, bandit,
capture and scale arms (0.2656 to 0.2767 against 0.2484), as [CASE-158](CASE-158.md)
predicted; it collapsed onto whichever specialist the combined proposal
resembled. With continued training it did better than fixed (0.2140 to
0.2156), and far worse than governance or router.

## What it shows

[CASE-158](CASE-158.md)'s third prediction holds here in a stronger form than
[CLAIM-467](../claims.d/CLAIM-467.md) states: not only under full information, but in each arm built
for a failure of evaluation, the best router given the same audits, delay
and cost matches or beats the best governance. The comparisons governance
won were against a router weaker in a stated respect: a noisier context
(full, capture 50%, training, at low temperatures), a missing
normalization (scale), or an audit floor that the router does better
without (bandit). Each is a property a router can be built with or
without. The one win against a router matched in every respect built here
is the bandit arm with the floor imposed on both, and there the router
without the floor does as well. Whether the full-information comparison at a
shared low temperature meets [CLAIM-467](../claims.d/CLAIM-467.md)'s defeat condition is the owner's
reading: see [CLAIM-906](../claims.d/CLAIM-906.md).

## What it cannot show

- Anything about real diffusion models or organizations: the operators are
  linear low-rank denoisers on synthetic Gaussians.
- That no governance procedure beats a router in these arms: one procedure
  was built per arm, with Borda-like duel scores for cycles, and no
  α-Rank or Nash averaging ([QUESTION-271](../questions.d/QUESTION-271.md)'s candidates).
- Capture by duplication in the sense of the readings on Nash averaging:
  here the incumbent filters and doubles, and no game-theoretic score was
  tried.
- The entrenchment loop with competence that grows faster than the right
  specialist can be found; the training arm's rate and capacity were not
  swept.
- [CASE-158](CASE-158.md)'s counterfactual that resets only the learned grants was not
  run.
