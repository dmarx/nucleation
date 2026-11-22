# LEAD-122: census of filing dispositions in the workbench reconstructions

Advances QUESTION-072 (part 1): in this record's workbench reconstructions,
for moves of comparable content, the share filed by contributor and by kind
of move.

## Rerun

    python3 -I scratch/studies/lead-122/census.py \
        --workbench record/workbench.d \
        --out scratch/studies/lead-122/results.json

    python3 -I -m pytest -q scratch/studies/lead-122/test_census.py

CPU only, no network, runs in well under a second. `results.json` holds the
tallies and one row per move; the script also prints the summary.

## What a "move" is here (operationalization)

The question's terms -- "move", "comparable content", "contributor", "kind of
move" -- are not defined by a field in the record, only in QUESTION-072's
prose. The reconstructions are free prose, but ~1/3 of them structure their
accounting with a small set of **bold labels** that are the record's own
disposition vocabulary. The choices made, each stated so the owner can
overrule:

- **move = one bold-label disposition span.** Each `**Filed:**`,
  `**Missed:**`, `**Not filed:**`, `**Struck:**`, `**Held, not filed:**`,
  `**Corrected:**` (and close variants) introduces a span describing one or
  more moves and what became of them. Each such span counts as one move,
  classified by its dominant scheme code. *Why:* it is the only
  machine-reliable unit; a span may bundle several codes, so a supplementary
  table (`code_mentions_by_scheme`) also counts distinct codes named in filed
  vs not-filed spans.
- **filed vs not-filed.** `Filed` is filed; `Missed`, `Also missed`,
  `Not filed`, `Struck`, `Held, not filed` are not-filed. `Corrected` is
  reported apart (it edits an existing entry, not a propose/file decision).
  Labels that are not filing decisions -- `Right`, `Wrong`, `Partly right`,
  `Already held`, `On file`, `Checked`, `Registered` -- go to `other` and are
  excluded from the shares.
- **contributor** from attribution tokens: **owner** (`owner`, or an owner
  turn `U\d+`), **assistant** (`A\d+`, "the assistant"), **reader** (the
  reconstruction's own deriving readers), **both** when owner and assistant
  tokens co-occur, else **unattributed**. Workbench convention numbers owner
  turns `U` and assistant turns `A`. Two windows are reported: the enclosing
  block (`by_contributor`) and the span alone (`by_contributor_span_only`), to
  show the result's sensitivity to how wide attribution is read.
- **kind of move** from the scheme the move names: claim, question, term,
  case, arg, note (a span saying "note(s) on ..."), work (a registered LIT),
  theory; `unclassified` when no code is named.

## Headline result

- 135 workbench files. **47 carry disposition labels; 88 are free prose and
  are not captured** -- the single biggest limit on coverage.
- 698 label-spans (moves); 454 are filed-or-not-filed (209 filed, 245 not),
  237 `other`, 7 `corrected`.
- **Share filed by contributor** (block context / span-only):
  owner 0.70 / 0.67, assistant 0.57 / 0.41, both 0.41 / 0.38,
  unattributed 0.65 / 0.55. Owner-attributed moves are filed at a higher rate
  than assistant-attributed ones, and the direction is robust to the
  attribution window. Most filed/not-filed spans are co-attributed ("both"),
  because reconstructions interleave an owner prompt and the assistant's
  working-out within one block.
- **Share filed by kind of move:** note 0.79, case 0.59, question 0.55,
  claim 0.44, term 0.39, work 0.26, theory 0.00. A note added to a held entry
  is far likelier to survive than a freshly proposed claim or term; THEORY
  (readings) are essentially never filed as a workbench move, which is
  expected -- readings enter through read-and-file, not the workbench.

## Limits (read before citing)

1. **Coverage.** Only the 47 label-bearing entries are counted. The 88
   free-prose entries (e.g. "What moved" bullet sessions) are not, and they
   may file differently.
2. **"Comparable content" is not verified.** The script cannot tell whether
   an owner move and an assistant move are of the same content. So it answers
   the marginal question ("what share of each contributor's labelled moves
   were filed?") but NOT QUESTION-072 part 1's counterfactual ("content held
   fixed, does who made it matter?").
3. **Kind confounds contributor.** The owner characteristically makes
   high-file-rate kinds (prompts, theses, corrections, notes); the assistant
   makes many candidate claims and terms of which fewer survive. The raw
   owner>assistant gap may be this composition, not a credibility asymmetry.
4. **"both" dominates**, so the owner-only and assistant-only cells are thin
   (27 and 37 spans in the block window), and their shares are noisy.
5. String-level parsing: attribution and kind are read from tokens, not
   understood. Spot-check `results.json`'s `moves` rows against the entries.

The finding is therefore descriptive evidence that the asymmetry
QUESTION-072 part 1 names is *visible* in the record's own accounting, while
leaving open whether it is a wrong, a bias, or an artefact of what kinds of
move each contributor makes.
