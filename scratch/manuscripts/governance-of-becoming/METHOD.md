<!-- scratch/manuscripts/governance-of-becoming/METHOD.md -->

# A note on method

## What the series is

*The Governance of Becoming* is written from a research record, the Luria record of the Nucleation project. The record keeps an argument as many small entries. Each entry holds one step: a definition, a claim with its argument, a construction or run, a reading of a published work, an open question, or a plan of work. Each entry has its own history, its evidence, and the objections filed against it.

The articles are a view over that argument, written for a reader outside the record. They add nothing to what the record holds. Each step an article takes cites, in parentheses, the entry that holds it. Where an article puts together two steps that the record keeps apart, the combined step was tested before the article could assert it. If it passed, it was filed as an entry of its own and the article cites that entry. If it failed, the article says the link is open. The joins and their verdicts are listed in each article's apparatus.

## How to read a code

A code names an entry: a scheme, a hyphen and a number, such as `CLAIM-605` or `CASE-161`. The schemes the articles cite are:

| Code | What the entry is |
|---|---|
| `TERM-` | a definition, in the record's own words |
| `CLAIM-` | an assertion, with its argument, its warrant and its defeaters; an objection is also a claim |
| `ARG-` | an argument between claims |
| `CASE-` | a construction, a simulation run, a proposed study or a documented specimen |
| `THEORY-` | a reading of a published work, with what it supports |
| `LIT-` | a published work registered in the record, read or not |
| `QUESTION-` | an open question |
| `LEAD-` | a plan to advance a question or claim |
| `SYNTHESIS-` | the record's integration of a line of its argument |
| `ADR-`, `DP-` | the record's decisions and design principles about itself |

A citation such as "(CASE-264; CLAIM-670)" means the step is held by those entries together. A quotation in a sentence that ends with a code is that entry's wording. Published work is cited as in a paper, through the entry that reads it, for example "(Hirschman 1970; THEORY-152)".

Codes that contain `tmp`, such as `CLAIM-tmp6nzs1`, are temporary. The record gives them permanent numbers when their batch is promoted, and the drafts will be updated to match. Turn labels such as "U17" or "A51" name a turn of an exchange, from the owner (U) or from ChatGPT (A). They appear in the articles only where an article quotes a motivating draft.

## Kinds of support

Steps rest on different kinds of support, and the articles signal which kind in their own words rather than with tags.

- **Derivation.** The step is a mathematical result about a stated object. The articles say "shows", "follows" or "exactly when", and they state the object: a cost model, a bargaining rule, a dynamical system. A derivation is true of its object. Whether a real organization has that structure is a further, empirical question, which the derivation does not answer.
- **A model with invented parameters.** The step is a construction or simulation whose population, laws and values the modeller chose. The articles write "in a model in which …" or "in a simulated population", and report figures as the model's. A model shows that a mechanism can do what is claimed, or that two descriptions can come apart. It is not a finding about institutions or minds. Where a run's results were read again from stored output rather than regenerated, or checked only by the session that ran it, the apparatus says so.
- **A reading of a published study.** The step rests on what the record has read of someone else's work. The article cites the author and the year, and it says when the reading is partial or the work is unread. A study the record has registered but not read is never cited as support.
- **Conjecture.** The step is argued but not shown: an interpretive proposal whose defeaters have not been tested, or a thesis facing an objection it has not answered. The articles say "conjecture", "proposal" or "on one proposal", and they give the strongest objection beside it.

A few steps are the record's own documentation of real records, such as coded testimony or a coding of public histories. The article names each one and its limits where it uses it. Where whose a step is matters to the argument, the text says so plainly, for example "a conjecture", "the author's computation", or "two readings held as alternatives". Otherwise the article names no voice.

Each article also says what its argument does not establish, and it states the strongest objection it knows of. A step's scope is kept as its entry states it. Where a paraphrase would move that scope, the article quotes the entry instead, and a sufficient condition is never turned into a definition.

## Where the apparatus is

The record's own bookkeeping is kept out of the argument and stored beside it.

- `apparatus/NN-….md`, one file per drafted article, holds:
  - the standing of every entry cited (status, warrant, kind), who made each Active entry Active, and the voices (the owner's, ChatGPT's, the filing assistant's);
  - the joins and their verdicts;
  - the gaps, with what was filed for them;
  - the sort of proposed studies into done, done in part and not done;
  - the points of contact not cited, with reasons;
  - the departures from the motivating drafts;
  - a numbering map from earlier drafts to the current one.
- `README.md` holds the series' provenance, the process history, the reviews and fact-checks, the series-level standing review, what the record had already done, the record filings this manuscript made, the open items for the owner, and the dated notes.
- `REVIEW-*.md` and `FACTCHECK-*.md` are the independent reviews and fact-checks, each as written. They cite the section numbers of the drafts they read, and the numbering maps translate them.
- `background/` holds the digests the drafts were written from. `analysis/` holds the scripts and dated outputs of the computations the articles report. `motivating/` holds the motivating drafts, verbatim. `superseded/` holds drafts kept for the citations that point to them.

## Standings move

An entry's standing can change after the articles cite it. Its status may be Proposed or Active, it may be rechecked, an objection may be filed against it, or it may be superseded. The articles therefore do not state standings, and a step's firmness is given only where the argument turns on it. Standings are given as of a date in the apparatus files and in the README's standing review, and the README's dated notes record when they were last read. To check a step, read its entry in the record: the entry is the authority, and the article is a view of it.

The argument was developed in conversations between the record's owner and AI assistants. The same assistants also file and study the record that holds it, so an assistant's agreement with an entry is not independent evidence for it. Where drafting this manuscript changed the record's wording, or filed an entry that an article then cites, the apparatus says so. Where it did, the record is not a second witness to that step.
