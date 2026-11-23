<!-- scratch/studies/lead-101/CODING.md: coding rules for LEAD-101, written 2026-11-23 before any case was coded -->
# LEAD-101: coding rules

Written after a scoping pass (one search, one quantitative study located)
and before the case table. Changes made while coding are listed at the end,
dated, with the reason.

## What is tested

CLAIM-432, part 5: "a corporation changed only by sanction reverts when the
sanction lifts, and one whose concerns were redesigned does not." CLAIM-431's
first answer: the two kinds of corporation differ once "the external sanction
that might have motivated the procedure is lifted". LEAD-101 adds: "with
reputation and benefit held fixed".

## Two arms of evidence

1. **Quantitative.** Open studies that compare firms' conduct during a
   sanction and after it ends. Coded at the level of the study: what the
   outcome measure is, whether it measures harm-weighing or only detected
   violation, whether the post-sanction window is estimated separately, and
   what is held fixed.
2. **Case histories.** A unit is one firm and one sanction with a fixed term
   that ended on a documented date. Coded from open documents only.

## Admitted sanctions

A deferred or non-prosecution agreement, a court-appointed or
agreement-appointed monitorship, an HHS-OIG corporate integrity agreement
(CIA), a consent decree or administrative consent order with a term, or court
probation. A sanction still running at the end of the study window
(2026-11-23) is coded `open`; one that ended less than two years before is
coded `unripe` (no post-lift window to trace).

## The arm (what changed the firm)

Coded from documents dated before the sanction ended where possible.

- **R, concern redesigned**: a documented procedure or role duty that makes
  harm of the sanctioned kind an input to decisions with authority over them
  (a gate that can stop a product, a sale or a payment on harm grounds; a
  board committee with that remit), either installed beyond what the
  sanction required or kept after it ended. The evidence must be an
  independent source (a court, an agency, a monitor's public report, a study)
  or the firm's own internal documents, not its promotional statements.
- **S, sanction only**: the documented changes are those the sanction
  required, and nothing meets R.
- **U**: not codable from what was read.

## The outcome (after the sanction ended)

The window runs from the documented end date to the earlier of five years
later and the start of a new sanction for the same kind of harm.

- **W+, harm weighed**: a documented decision in the window in which harm of
  the sanctioned kind was weighed against the firm's interest and restrained
  or repaired the firm's conduct at a cost to it.
- **W-, harm not weighed**: documented conduct in the window that does harm
  of the sanctioned kind, or a documented decision in which information about
  that harm reached decision-makers and did not restrain the conduct.
- **W0**: nothing traceable either way.

Each W- is also coded for timing: `reversion` if the conduct began after the
end date; `through` if it began or continued while the sanction ran.

Each outcome is coded for **source standing**: `finding` (a conviction, plea,
admitted statement of facts, agency or court finding), `allegation` (a
complaint, an indictment not resolved), `study` or `report`.

## What the lead says to hold fixed

- **Reputation**: `exposed` if, at the time of the post-lift decision, the
  conduct was publicly visible or a pending investigation or litigation made
  it likely to become so; `private` if the documents show it was not;
  `unknown` otherwise.
- **Benefit**: for W+, `opposed` if the weighing cost the firm net of what it
  gained, `aligned` if it also served the firm, `unknown`; for W-, whether the
  harmful course served the firm (`aligned`) or not.

## Meeting the lead's standard

A case meets the standard only if all of the following hold: the sanction
ended on a documented date with a post-lift window; the arm is coded R or S;
the outcome is W+ or W- from a `finding` or `study`; and neither reputation
nor benefit explains the outcome: for W+, reputation `private` and benefit
`opposed`; for W-, the case is paired with a case in the other arm whose
reputation and benefit codes are the same. A case short of this is listed
with each condition it lacks.

## What discriminates

Coded separately, since it decides what any outcome can show: which outcomes
CLAIM-432's part 5 and CLAIM-431's prudence reading predict alike. An S firm
that reverts is predicted by both. Only an R firm's conduct after the lift,
with reputation and benefit fixed, separates them.

## Frame

Purposive, and said so: the quantitative studies found by search; and the
cases the record itself names (CASE-151, Wells Fargo) plus those whose end
date and post-lift record are in open documents. A purposive frame can show
that the standard is or is not met by the cases looked at, not how often
firms revert.

## Changes while coding

(none: the rules were applied as written. Siemens's during-sanction outcome
is coded "W+ and W-" because both kinds of event are documented.)
