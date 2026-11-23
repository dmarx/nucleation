# LEAD-107 codebook (fixed before the outcome tables were computed)

Written 2026-11-23 by the lead worker (Claude), before running the
comparisons. The extraction cues were calibrated by reading grep hits for
restatement words in `record/workbench.d/` (that reading is why this coder is
not blind to the hypothesis; see "What blindness there is" below). Every rule
is implemented in `restatement.py`; the function name is given in brackets.

## Corpus [`is_exchange_reconstruction`]

A workbench entry is a reconstruction of an exchange when its title begins
`Session`, `Sessions`, `Exchange`, `The exchange` or `Branch`, and its body
has at least 10 turn labels (`U12`, `A125`, `T18`, `B37`) or names a shared
exchange. Status reviews, audits and owner reviews are excluded. The
reconstructions are read only.

**Exchange start date** [`exchange_date`]: the first `YYYY-MM-DD` in the
title; if none, the entry's `created` date, flagged `date_uncertain`.

## Unit [`extract_events`]

A **sentence** of the body (markdown links reduced to their bare code;
sentences split at `.`, `;`, `?` or `!` followed by space and a capital,
quote, bracket or asterisk, and at bullet boundaries).

A sentence is a **restatement event** when it carries a NEW cue, or a
RETRIEVED cue together with a RECURRENCE cue, or a RECURRENCE cue alone.

## Outcome Y [`classify`]

- **NEW cues** (re-derived as though new, not retrieved):
  `re-deriv*`/`rederiv*`; `as though new`, `as if new`, `as new`;
  `without citing`, `without citation`, `without its code`, `uncited`,
  `not cited`, `cited little`, `cited none`, `without (a) back-reference`;
  `rediscover*`; `re-propos*`; `reintroduc*`; `re-recommend*`; `re-ask*`;
  `unlinked`; `already held` when the sentence also has a turn label or a
  proposal verb (`propos*`, `recommend*`, `offer*`, `put forward`,
  `present*`, `suggest*`).
  A `re-deriv*` cue is void when the sentence is about checking a proof
  (`proof`, `by hand`, `checker`, `script`, `numeric*`, `.py`, `computed`,
  `step by step`): that is the filer re-deriving, not the exchange.
- **RETRIEVED cues**: `cites`, `cited`, `citing` not within three words after
  `without`, `not`, `never`, `un-`, and not followed by `little`/`none`;
  `by its code`, `with its code`, `pointing back`, `points back`, `recap*`.
- **RECURRENCE cues**: `restat*`, `came/comes/come back`, `recur*`, `again`,
  `already held`, `duplicat*`, `repeat*`, `second/third/fourth time`,
  `N times`.
- Y = `new` if NEW and not RETRIEVED; `retrieved` if RETRIEVED and not NEW;
  `conflict` if both; `neutral` if only RECURRENCE.

## Items and coded status [`items_of`, `coded_at_time`]

- The **items** of an event are the distinct codes it names of the kinds
  CLAIM, TERM, QUESTION, CASE, ARG, THEORY, LIT, NOTE (ADR and DP excluded:
  they are the record's procedure). An event naming none has one anonymous
  uncoded item.
- An item is **coded at the time** when its entry's top-level `date` is
  strictly before the exchange start date. Same day, later, or the code
  missing from the record: uncoded (primary); same-day counted as coded is a
  sensitivity reading.
- **Collapsed unit**: (reconstruction file, item). Y precedence: `new` >
  `retrieved` > `conflict` > `neutral`. Anonymous items are not collapsed.

## Distance [`distance`]

For an event with exactly one item code, at least one quotation (`"..."` or
`“...”`) of three or more content words, and the code's entry present:

- the restatement's wording = the quotations in the sentence, joined;
- the original = the entry's current `title` (primary) or title + summary;
- `d_jac` = 1 − Jaccard of crude-stemmed content-word sets;
- `d_chr` = 1 − cosine of character 4-gram counts;
- `d_cov` = 1 − share of the quotation's content stems found in the original.

The distance functions receive only the two strings, never Y; Y is computed
from cue words, never from the distance. That separation is the only
blindness to direction this study has.

## Comparisons [`analyse`]

1. Collapsed units: P(Y = new) for coded against uncoded items, among units
   with Y in {new, retrieved}; Fisher's exact test.
2. Within item, before and after its code: for each code with events, the
   events from exchanges starting on or before its date (pre) and after it
   (post), by Y; the later reconstructions as exposure.
3. Distance: d by Y (new against retrieved, and new against neutral);
   Mann–Whitney U and the AUC that a new event is further than a retrieved one.

## What blindness there is

The lead asks for raters blind to direction. There is one coder, the lead
worker, who knew the hypothesis and read grep hits before writing these
rules. The rules are mechanical, so a rerun gives the same codes, but the cue
lists were chosen by a coder who knew what they were for. A second, human
coder is a separate lead.
