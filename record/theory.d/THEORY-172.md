---
number: 172
status: Active
formerly:
- THEORY-tmprknoj
title: 'In Frank and Goodman''s one-shot reference games, listeners'' mean bets matched a parameter-free listener inverting a speaker who chooses among true utterances by informativeness, with a separately measured salience prior, and not salience alone; and in Bergen, Goodman and Levy''s signalling games with novel symbols, listeners read a signal as excluding what the available alternative would have conveyed'
version: 4
history:
- version: 2
  date: '2026-10-16'
  note: >-
    Its precursor, Frank, Goodman, Lai and Tenenbaum 2009 (LIT-824, read in
    NOTE-627), is now filed as THEORY-472, and this account extends
    it: the same inversion of an informative speaker, widened from
    inferring a word's meaning given its referent to inferring the
    referent. LIT-824 is not added to the source, because its Experiment 1
    tests the neighbouring inference and not this one. A Connections
    section names both.
- version: 3
  date: '2026-10-20'
  note: >-
    Narrowed and promoted, carrying out the promotion audit's decision for
    THEORY-172 (batch 048, ADR-047 v3): two studies read in full, whose text
    states the results. "Listeners interpret an utterance by inverting a
    speaker model" becomes the measured match in those games, and "neither
    the prior nor the literal meaning alone" keeps only the prior, since no
    likelihood-only model was fitted. The promote_when moves to
    QUESTION-209.
- version: 4
  date: '2026-10-20'
  note: >-
    Note of 2026-10-20 added: the wider claim this entry's narrowing
    dropped is now filed as THEORY-tmp6lphc, Proposed, which extends
    this one (ADR-047 v4). The title and status are unchanged.
tags:
- pragmatics
- linguistics
- cognition
- probabilistic-modeling
date: '2026-10-09'
source:
- LIT-821
- LIT-809
- LIT-816
extends:
- THEORY-472
summary: >-
  Frank & Goodman (2012), [LIT-821](../literature.d/LIT-821.md), read in [NOTE-634](../notes.d/NOTE-634.md): a parameter-free
  Bayesian listener inverting a size-principle speaker, with a separately
  measured salience prior, matches mean listener bets over seven context
  types at r = .99 (.87 without the 0 and 100 predictions), while salience
  alone correlates at r = .19. Bergen, Goodman & Levy (2012), [LIT-809](../literature.d/LIT-809.md), read
  in [NOTE-613](../notes.d/NOTE-613.md): with novel signals and no conventions, listeners read the
  signal as the object its alternative did not name, and lexical
  uncertainty derives Horn's mapping. Goodman & Frank (2016), [LIT-816](../literature.d/LIT-816.md),
  states the framework. Shown for artificial games with given alternatives,
  by fits of condition means with no rival fitted; a test against named
  rivals on trial-level data is [QUESTION-209](../questions.d/QUESTION-209.md).
supports:
- CLAIM-111
- CLAIM-221
- CLAIM-236
- CLAIM-214
- CLAIM-242
extended_by:
- THEORY-tmp6lphc
---

<!-- inactive-ok-file: THEORY-tmp6lphc — Proposed; the wider claim this entry's narrowing dropped, cited as open -->
# THEORY-172: In Frank and Goodman's one-shot reference games, listeners' mean bets matched a parameter-free listener inverting a speaker who chooses among true utterances by informativeness, with a separately measured salience prior, and not salience alone; and in Bergen, Goodman and Levy's signalling games with novel symbols, listeners read a signal as excluding what the available alternative would have conveyed

## Source

- Frank & Goodman (2012), [LIT-821](../literature.d/LIT-821.md), read in [NOTE-634](../notes.d/NOTE-634.md): Eqs. 1–2,
  S1–S4, the three-group design and its correlations.
- Bergen, Goodman & Levy (2012), [LIT-809](../literature.d/LIT-809.md), read in [NOTE-613](../notes.d/NOTE-613.md):
  Eqs. 1–8, Experiments 1–2.
- Goodman & Frank (2016), [LIT-816](../literature.d/LIT-816.md), read in [NOTE-606](../notes.d/NOTE-606.md) from the
  authors' manuscript: the general form and its extensions.

## The claim

In one-shot reference and signalling games with a known set of
alternative utterances, listeners' interpretations match
P_L(m|u) ∝ P_S(u|m)P(m), where P_S chooses among the utterances true of m
in proportion to exp(α[log P_Lit(m|u) − c(u)]) and P_Lit conditions the
prior on literal truth. Two consequences follow and are observed: a
general utterance is read as excluding what a more specific available
utterance would have conveyed (specificity implicature), and, when the
agents are uncertain what the signals mean, a costlier signal is read as
the less likely meaning (Horn's principle). The measured prior alone
does not predict the interpretation; its combination with the speaker
model does. A literal-meaning-only listener was not fitted.

## What was actually shown

Frank and Goodman measured the prior and the listener in separate groups
of participants. Salience and listener bets were uncorrelated (r = .19);
the model combining measured salience with the parameter-free speaker
matched listener means at r = .99 (.87 without 0/100 points), and the
speaker model matched speaker bets at r = .98. This could have failed:
listeners could have followed salience, or literal meaning alone, or a
speaker who is not informative. Bergen, Goodman and Levy showed that
interpretations of signals with no prior meaning follow the contrast with
the available alternative (ceiling, Experiment 1) and the relative costs
of alternatives (Experiment 2); and they showed by derivation that the
basic recursion cannot produce the cost effect, so the observed Horn
mapping is evidence for something beyond it, which lexical uncertainty
supplies.

## What this does not say

- **Not that comprehension in natural conversation computes this
  recursion.** The games give the alternatives, use single features or
  novel symbols, and make costs explicit in money. How alternatives are
  fixed in real language is listed by the framework's authors as open.
- **Not that speakers are informative.** RSA models the listener's
  assumption about speakers; production is overspecified and egocentric
  in ways the authors acknowledge it does not capture.
- **Not that one depth of recursion is universal.** The evidence the
  review cites has most people at minimal depth and a minority deeper.
- **Not established beyond aggregated fits.** The 2012 correlations are
  over condition means, several fixed at 0 or 100; a 2021 reanalysis
  (Sikos et al., not held, not read) addresses how robust they are.
- **Not that a form's meaning is nothing but its contrasts.** The
  alternatives' literal meanings, iconic or conventional, are inputs; the
  contrast modulates them.

## Connections

- **The word-learning precursor ([THEORY-472](THEORY-472.md); [LIT-824](../literature.d/LIT-824.md), [NOTE-627](../notes.d/NOTE-627.md)).**
  Frank, Goodman, Lai and Tenenbaum (2009) derive the size-principle
  speaker this account's listener inverts from informative communication,
  and test the inversion in word learning: given the referent, learners
  bet on a novel word's meaning as the inverted speaker predicts. This
  account widens the same mechanism to inferring the referent. [NOTE-627](../notes.d/NOTE-627.md)
  finds that Experiment 1 adds support here in that neighbouring form,
  and that its evidence (r = .93 on condition means, one model, no
  competitor) is of the kind `promote_when` says cannot settle it.

## Note of 2026-10-20: what the promotion keeps

The account is held to what the two studies measured. Frank and
Goodman's listener condition is a match of condition means to one model
(r = .99) against a measured prior that does not predict the bets
(r = .19); a likelihood-only listener is not reported, so the title does
not claim that literal meaning alone fails. Bergen, Goodman and Levy's
Experiment 1 shows the dependence of a fixed form's reading on its
alternative at ceiling. Their Experiment 2, the Horn mapping, supports
lexical uncertainty, which goes beyond the basic inversion, and stays in
the body as such. Whether listeners compute the inversion, rather than
follow the alternatives by a simpler route, is [QUESTION-209](../questions.d/QUESTION-209.md).

## Note of 2026-10-20: the wider claim filed

The promotion audit narrowed this entry to what was shown. Under
[ADR-047](../decisions.d/ADR-047.md) v4 the claim the narrowing dropped, that listeners interpret utterances by inverting an informative speaker, as the mechanism and not only a fit to mean bets, is now filed as
[THEORY-tmp6lphc](THEORY-tmp6lphc.md), Proposed, which extends this entry and takes it as
evidence. This entry's title and status are unchanged.
