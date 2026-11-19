---
status: Read
paper: LIT-tmpqj6ht
title: 'Stern and colleagues — Rethinking Pre-pretraining'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read on 2026-11-19 by a delegated reader from arXiv 2610.40051v1 (PDF):
    §§1–8, limitations, discussion and appendices B, C and E in full;
    appendices A and D skimmed. Running notes on the branch
    claude/readers/scheduling-followups (the procedure proposed in pull
    request 537). Quotations rechecked by the filer by script against the
    downloaded text.
date: '2026-11-19'
summary: >-
  Pre-pretraining tested at matched compute and with improved baselines:
  no natural-language gain at matched FLOPs; gains only at tiny additive
  budgets; earlier gains partly an initialization artefact; first-phase
  skill overwritten at the switch, kept under interleaving.
---
<!-- inactive-ok-file: THEORY-tmpk9cmk CLAIM-756 LEAD-tmpjdtrl THEORY-tmpbsmcq CLAIM-758 THEORY-tmpd6l4a — Proposed or newly filed; entries this reading bears on -->

# NOTE-tmph6c5h: Stern and colleagues — Rethinking Pre-pretraining

## Contribution

The first compute-matched test of pre-pretraining across regimes,
including the one where natural language runs out, with the baseline's
initialization and the natural-language control's schedule repaired.

## Key results

1. **Matched compute.** In the data-constrained regime "diverting any
   fraction of the budget to synthetic PPT increases validation BPB, with
   the effect leveling off beyond 5%" (§5); "repeated epochs over a
   100M-token corpus beat every synthetic curriculum on natural-language
   validation loss" (abstract). Data-unconstrained: "Every synthetic PPT
   method remains above the baseline at every budget, while C4,
   independent of percentage, is the same as the baseline." (Fig. 9)
2. **Scaling.** "no PPT method has either a lower multiplicative constant
   or a significantly larger scaling exponent than the baseline" (§5).
3. **Additive.** "At 50M and 100M natural-language tokens both PPT methods
   improve over the best no-PPT baseline"; gains "disappear by 1B tokens"
   under the improved initialization (abstract), and persist at 1B under
   the others (Fig. 8).
4. **Initialization confound.** Reproducing the cellular-automaton result,
   "we recover the effect, a 5.4% gain"; changing only the embedding scale
   "improves the baseline by 9.0%—more than the reported gain itself" (§4).
5. **Overwriting.** "at the PPT-to-PT boundary the BPB immediately starts
   increasing" on the first-phase distribution, code included; "the priors
   learned on code-specific data are not fully kept, and are instead
   progressively overwritten once the distribution shifts abruptly to
   natural language" (§8). Interleaving keeps them; on natural language,
   "Interleaving improves FineWeb BPB for the PPT methods, though not
   significantly for all" (§6).
6. **Controls.** Resetting the optimizer at the boundary hurt the
   natural-language control; they recommend one schedule, no reset (§3).

## Assumptions

Validation BPB measures the value of a first phase; spectral initialization
is the right baseline; 1 and 5 per cent stand in for the best share;
first-phase loss stands in for retained priors.

## Concepts

Pre-pretraining; additive against compute-matched allocation; data regimes;
initialization confound; forgetting at a phase switch; interleaving.

## Bearing on the record

- **THEORY-tmpk9cmk** (Hu and colleagues), qualifies its generality: at
  matched compute with a tuned initialization, k-Dyck never beats the
  baseline in any regime; under Hu's initialization family the additive
  gain persists at 1B (Fig. 8). The optimizer-reset point bears on Hu's
  natural-language first-phase control. Not a replication of Hu's setup,
  so it neither meets nor defeats that THEORY's promote_when; the authors
  cite a reproduction (Riazhskykh and colleagues) whose gain "did not
  consistently persist across all model sizes, tokenizers, and languages
  tested".
- **CLAIM-756**, qualifies its leading empirical instance: in a tuned
  regime the earlier acquisition does not repay its compute. The claim's
  derivational content is untouched. Argued in ARG filed with this change.
- **LEAD-tmpjdtrl**, the owner's code-first idea: answered negatively at
  these scales; a code first phase does not even clearly help held-out code
  loss at matched compute (Table 12).
- **THEORY-tmpbsmcq** (Aryabumi and colleagues): the positive instance this
  paper does not test; design differences listed in its NOTE.
- **CLAIM-758**, parallel: collateral forgetting at an abrupt shift counts
  as part of a phase's cost.
- **THEORY-tmpd6l4a** (Skill-it), parallel: interleaving keeps what
  front-loading loses.
- **QUESTION-495**, evidence and narrow: a case where investing in later
  learnability does not pay at matched compute.
- **THEORY-279**, **THEORY-2006**, **CLAIM-754**: analogies on earlier
  structure lost to later training.

## Limitations

Below 1B parameters; no full hyperparameter search above 9e18 FLOPs; shares
fixed, not tuned; untuned interleaving runs with unstated seeds; Hu's setup
not reproduced; a v1 preprint.
