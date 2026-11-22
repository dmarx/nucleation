---
status: Proposed
title: 'One cost model prices a crew''s speed bugs, a filed argument and a LEGO bin with the same terms, once work is priced by the moment it is done and checked against the budget for each demand, not only summed; what carries each differs: the bugs are paid by moving work to a quieter moment or by fitting a busy one, more than by reuse, the filed argument by how forecastable its reuse is, how often it goes stale and what recognizing it costs in a growing store, and the bin by the search it replaces against a deadline, at a construction made nearly free by doing it when the brick is found'
version: 1
history:
- version: 1
  date: '2026-11-22'
  note: >-
    Filed 2026-11-22 by the assistant, carrying out LEAD-108. The model and
    the pricing are CASE-tmpo2iur, with code under scratch/studies/lead-108/.
role: thesis
warrant: interpretive
defeated_if: >-
  A case of stored work, one of the three or one of the four strategies of
  QUESTION-095's note of 2026-10-15, whose verdict on feasibility, on
  lifetime cost or on who pays turns on a quantity that none of the model's
  terms carries, so that pricing it needs a term the others lack; or a
  showing that one term means incompatible things in two of the cases, so
  that "the same terms" is an equivocation. Not defeated by different values
  of a term from case to case, which is what the claim expects, nor by the
  illustrative values proving wrong; that changes which terms carry a case,
  which the claim would then have to restate.
tags:
- cognition
- information-retrieval
- operations-research
date: '2026-11-22'
line:
- distributed-agency
- nucleating-argument
- realizability
rests_on:
- CLAIM-303
- CLAIM-761
- CLAIM-760
- CLAIM-307
grounds:
- CASE-tmpo2iur
- CASE-094
- CASE-088
- THEORY-351
complements:
- CLAIM-308
- CLAIM-310
- CLAIM-tmpn0u3a
uses:
- TERM-055
answers:
- QUESTION-114
bears_on:
- QUESTION-095
summary: >-
  [LEAD-108](../leads.d/LEAD-108.md)'s result. [QUESTION-095](../questions.d/QUESTION-095.md) asked whether leaving a result where it is
  cheap to read back is one trade across the cockpit, filing and reuse, and
  its note of 2026-10-15 listed what one account would need: predictability
  of the later demand, a retrieval cost that includes search, staleness, and
  erosion of the alternative. [QUESTION-114](../questions.d/QUESTION-114.md) asked for the test: one cost model
  that prices the bugs, a filed argument and a LEGO bin with the same terms.
  A model with those terms, [CLAIM-303](CLAIM-303.md)'s, [CLAIM-761](CLAIM-761.md)'s per-demand budget and
  [CLAIM-760](CLAIM-760.md)'s parties does price all three, in [CASE-tmpo2iur](../cases.d/CASE-tmpo2iur.md), without adding
  a term for any of them. The four listed terms alone do not: the cockpit is
  carried by the price of work at the moment it is done, which they lack.
  The wording is the assistant's (Claude, in this session); adopting it is
  the owner's call.
---
<!-- inactive-ok-file: CASE-tmpo2iur — new; filed in this run of 2026-11-22 -->
<!-- inactive-ok-file: THEORY-351 THEORY-343 CLAIM-314 CLAIM-295 — Proposed; cited as readings and open claims, nothing here rests on their being settled -->

# CLAIM-tmpeklli: One cost model prices a crew's speed bugs, a filed argument and a LEGO bin with the same terms, once work is priced by the moment it is done and checked against the budget for each demand, not only summed; what carries each differs: the bugs are paid by moving work to a quieter moment or by fitting a busy one, more than by reuse, the filed argument by how forecastable its reuse is, how often it goes stale and what recognizing it costs in a growing store, and the bin by the search it replaces against a deadline, at a construction made nearly free by doing it when the brick is found

## The claim

The model ([CASE-tmpo2iur](../cases.d/CASE-tmpo2iur.md), which gives it in full) compares, for a stream of
demands, computing each time with building a store, keeping it and reading
it back. Its terms: construction F and the price of work λ_F when it is
paid; upkeep U; predictability π, the chance a demand is one the store
serves; retrieval ρ, which includes recognizing and searching, and the cost
of a miss; verification v and its catch rate δ; staleness or bias σ, with
the loss L of an undetected wrong result and the revision R of a caught one;
erosion ε of the on-demand route; spill, the retrieval cost a store adds to
other demands; the on-demand cost c and its own error; the price λ and
budget B at the moment of each demand; and the party who pays each item. It
gives three verdicts apart, as [CLAIM-761](CLAIM-761.md) and [CLAIM-760](CLAIM-760.md) ask: feasibility
([TERM-055](../terms.d/TERM-055.md)'s availability within B), lifetime cost, and who pays.

Priced with it, the three cases differ in which terms carry the verdict.

| | cockpit's bugs | filed argument | LEGO bin |
|---|---|---|---|
| π | 1: fixed, mandated, known | low, often unforecastable | the builder's use, unknown but countable |
| F, λ_F | paid at a quiet moment, 25–30 minutes ahead | paid when filed | paid at a find, so nearly free |
| U | none: reset each approach | lint, link repair, dependency tracking | new bricks to set aside |
| ρ | a glance; the needle supplies the cue | recognition by search, growing with the store ([CLAIM-314](CLAIM-314.md)) | open a bin; one look if the brick stands out |
| σ, v | held as a bound, by mandated cross-checks | goes stale unpropagated; checked on reuse | a moved brick, noticed at once |
| ε | weighs little: almost never falls back | weighs most: falls back often | none to speak of |
| spill | none: four bugs | each filing on every other reuse | a bin to scan, if bins are scanned |
| λ, B | busy final approach, a glance's budget | flat; rarely a budget | the builder's patience |
| who pays | crew per approach; maker for the card booklet | session, owner's review, CI | one builder, or all who share the bins |
| what carries it | λ and B | π, σ, ρ(store), the boundary | c against B; λ_F F near zero |

At illustrative values (Hutchins measured nothing, [THEORY-351](../theory.d/THEORY-351.md)), the bugs lose on their
four flap calls at a flat price of work and win once the approach is twice
as busy as the moment they are set; with the salmon-bug checks counted as
further reads they win by reuse too. On final approach recall does not fit
the budget and the bugs do, whichever reading holds. The filed argument is
[CLAIM-303](CLAIM-303.md)'s arithmetic exactly when σ, ε, spill and the boundary are set
aside, and each of them, at plausible values, can take [CASE-088](../cases.d/CASE-088.md)'s saving of
11 to nothing. The bin is forced where the search through similar bricks
exceeds the deadline ([CLAIM-307](CLAIM-307.md)), pays over time even where it is not
forced, and never pays for a brick that stands out ([CLAIM-310](CLAIM-310.md) part 3).

## What it gives [QUESTION-095](../questions.d/QUESTION-095.md)

The four strategies of the note of 2026-10-15 become regimes of the one
trade, which is the owner's conjecture stated so that it can fail:

- **Precompute and leave a result** (the bugs): π near 1, F at a low λ_F, ρ
  perceptual, the store living one episode.
- **Maintain structure that makes search cheap** (Kirsh's grouping, a set
  of bins, an index): F and U lower ρ for a class of demands, π below 1 over
  a mix, with spill onto the rest ([CLAIM-310](CLAIM-310.md)'s one arrangement).
- **Offload at the moment of use** (Tetris rotation): a store that lives
  one demand, F paid at that demand (λ_F = λ), no U.
- **Defer and re-read** (Ballard's block copying): π near 0 for anything
  precomputed, so F = 0 and the world is the store, with ρ its re-reading.

Amortized inference is the first regime with the store in the head, ρ near
0 and σ its bias. The lead's four terms are not enough by themselves: a
model with them and [CLAIM-303](CLAIM-303.md)'s, summing work, misprices the cockpit, whose
saving is in when the work is done. The price of work by moment is the
term that [QUESTION-095](../questions.d/QUESTION-095.md)'s list lacked. It is also the one that joins the
cockpit to the bin: a construction done at a quiet moment and one done
while the brick is in hand are both a small λ_F F.

## What it does not say

- **That the terms are complete.** Two strains are left. Staleness in the
  cockpit is correlated across a whole approach (a wrong weight makes every
  bug wrong); an expectation per demand prices it right on average and wrong
  in the tail, which is why the cockpit's regime is a bound, not a price. And
  a bug prompts the demand as well as answering it, telling the pilot that a
  flap call is due; the model prices that only as a lower chance of error on
  the bug route. If either needs a term of its own, this claim is defeated
  for the cockpit.
- **Any measured cost.** The values for the bugs and for the parts of the
  filing are illustrative and tagged as such in the run. What survives a
  change of values is which terms can carry each case, not the savings.
- **That the record's filing pays.** [CLAIM-303](CLAIM-303.md)'s caveat stands, and the
  owner's choices below decide its sign at plausible values.
- **That informational value is left out.** A result that cannot be
  recomputed, such as the owner's verbatim words, has c without bound, so
  storing it pays whenever π > 0; [CLAIM-295](CLAIM-295.md)'s option value is π over demands
  not yet foreseen. Both are priced by the existing terms.

## Choices that are the owner's

For the filed argument the sign of the saving turns on three choices the
record has not made. The run prices each alternative; none is chosen here.

- **A. Whose costs count.** A1, the session's work only: [CASE-088](../cases.d/CASE-088.md)'s filing
  breaks even at 1.7 uses. A2, the owner's review counted at its price
  (illustrated as five units at four times a session's price): 3.3 uses,
  and three uses lose. This is [CLAIM-760](CLAIM-760.md)'s boundary, applied to the record.
- **B. Who reconstructs when a filing does not serve.** B1, a fresh
  session, which has no internal route to erode: break-even 3.0 when three
  demands in ten are not served. B2, the owner, whose own reconstruction
  costs more once the record holds it (Risko and Gilbert's erosion,
  [THEORY-343](../theory.d/THEORY-343.md)): 4.1.
- **C. Whether the record prices staleness or bounds it.** C1, priced, an
  undetected stale answer counted as a loss: break-even 3.1. C2, bounded,
  checking raised until few stale answers pass: 3.5. The cockpit is in C2
  by regulation; the record is in neither by any decision.

The LEGO case needs facts only the owner has: how often a kind is used and
whether bins are found by label or by scanning. The run prices both
arrangements, and the bin pays under either.
