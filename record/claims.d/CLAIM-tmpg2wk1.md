---
status: Proposed
title: 'A tier is priced by retrieval noise and recovery'
statement: >-
  The tier an entry is kept in can be chosen by its cost over a review
  horizon, the sum of maintenance, the attention it consumes in contexts
  that do not need it, the expected cost of recovering it, the expected
  loss when it cannot be recovered in time, and the cost of moving it,
  under hard constraints of accountability, reproducibility, protected
  dissent and obligation that no sum overrides; so that what saves most
  reconstruction, not what is used most often, earns easy reach, and an
  entry rarely needed but costly to lose is not cooled for its rarity
version: 1
role: thesis
warrant: interpretive
defeated_if: >-
  A record in which the tier that minimizes the stated cost, with its
  constraints met, is the one recency or frequency of use alone would
  choose for every entry; or one in which the retrieval-noise term cannot
  be assigned to entries one at a time, because an entry's noise depends
  on which others are in default retrieval, and no corpus-level form of
  the rule picks tiers better than use does.
tags:
- databases
- information-retrieval
- operations-research
date: '2026-11-26'
line:
- records-of-inquiry
- nucleating-argument
rests_on:
- CLAIM-303
- CLAIM-314
bears_on:
- QUESTION-tmpz8xkx
uses:
- TERM-tmp96b3g
summary: >-
  A27 §§4, 7 and 8 and A29 §§5 and 7 of the exchange "Alignment
  consequences brainstorm" (ChatGPT, 2026-11-26), extending CLAIM-303's
  pricing of filing to the pricing of a tier. A's cost profile is
  J_e(k) = maintenance + retrieval noise + expected reactivation + expected
  unavailability loss + transition; its five retention values are current
  utility, reconstruction value, dependency value, negative knowledge and
  developmental option value. A29 §7 cites CLAIM-308 correctly for the
  reconstruction-weighted rule. The assistant's check: A's per-entry sum
  sits uneasily with A27 §4's own point, held in CLAIM-314, that an entry's
  cost depends on the rest of the corpus; ARG-tmpedexz narrows the claim
  accordingly. The wording is A's (ChatGPT, in the exchange of 2026-11-26);
  adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-314 ARG-tmpedexz TERM-tmp96b3g CLAIM-tmp6tc1j CLAIM-1148 — Proposed; the held claim it rests on, the argument filed beside it, and entries cited from the same exchange -->

# CLAIM-tmpg2wk1: A tier is priced by retrieval noise and recovery

## The claim

A27 §7, for an entry e and a tier k:

  J_e(k) = C_maintenance(k) + C_retrieval noise(k) + E[C_reactivation(k)]
           + E[L_unavailability(k)] + C_transition(k).

| Cost | Interpretation |
|---|---|
| Maintenance | Work required to keep the entry coherent and current |
| Retrieval noise | Attention consumed when it appears in irrelevant contexts |
| Reactivation | Work required to recover the entry or resume inquiry |
| Unavailability | Valuable activity lost because it cannot be recovered adequately or in time |
| Transition | Cost of cooling, condensing, migrating or restoring the entry |

"The last two prevent the model from simply recommending deletion of
everything infrequently used." And the sum is not sovereign: "There are
also hard constraints involving accountability, reproducibility, protected
dissent, obligations, and deadlines."

A27 §8 lists what forgetting would lose: current utility, reconstruction
value, dependency value, negative knowledge, and developmental option value,
"the hardest to price". Hence: "I would not use PageRank, citation counts,
recency or access frequency as the sole criterion for forgetting."

## Reconstruction, not frequency

A29 §7. Entry A is used 20 times at 1 unit of reconstruction per use;
entry B twice at 100. "Frequency alone would favor A. A
reconstruction-cost-sensitive policy might favor B." Checked: 20 × 1 = 20
against 2 × 100 = 200 units of reconstruction avoided. This is CLAIM-308's
rule moved from filing to availability: recurrence weighted by
reconstruction cost. CLAIM-303 already quotes the same point about
filing: "a rare, expensive-to-reconstruct argument might deserve persistence
more than an often-repeated trivial observation."

## The externality, and the assistant's check

A27 §4 says retention "cannot necessarily be determined in isolation": with
S the working corpus, an entry's marginal cost is
ΔC(e | S) = C(S ∪ {e}) − C(S), which includes its effect on "the
retrieval, interpretation and verification of other knowledge". This is
held: CLAIM-314 shows that recognizing which stored answer covers a new
question grows with the store, so "per-item break-even decisions are not
independent".

*The assistant's (Claude, in this session).* A27 §7's J_e(k) then prices
each entry alone, with a retrieval-noise term that is a property of the
entry. The two do not fit unless noise is additive over entries. When it is
not, as CLAIM-314 says, the rule has to be stated over the working corpus:
choose the set of hot entries that minimizes total cost, not each entry's
tier one at a time. ARG-tmpedexz records this narrowing. A27 §4's own
illustration (20 relevant results among 100, 80 distractors moved out of
default retrieval in steps) is correct arithmetic, the relevant fraction
going from 20 % to 20/(100 − c), and 100 % at c = 80, checked with
`python3 -I`, but it assumes, as A says, that no relevant result is
cooled.

## The collector's own cost

A29 §5: "The collector's activity must itself satisfy Nucleation's
amortization criterion. A sophisticated retention apparatus that costs
more to operate than the retrieval work it saves would be another instance
of organizational overdevelopment." The transition term is where that
cost enters.

## What it does not say

That one score should decide. A29 V keeps tracing, compression and caching
apart because each establishes something the others cannot: "A tracing
algorithm cannot establish semantic redundancy. A compression algorithm
cannot establish normative importance. A caching algorithm cannot establish
which knowledge the institution has an obligation to preserve. Combining
all three into an opaque relevance score would recreate the optimization
pathology we have been discussing." The hard constraints above are where
the third enters.


That use is no evidence. Use is evidence of current utility; CLAIM-tmp6tc1j
is A's warning that in a record use is partly produced by availability, so
it is weaker evidence than in a cache. CLAIM-1148's maintained nuclei are
one way developmental option value can be kept without keeping everything
hot.
