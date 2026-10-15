---
status: Proposed
title: 'Where reuse cannot be forecast, recurrence weighted by reconstruction cost is the filing criterion, not only evidence for one: filing once the reconstruction already paid for equals the cost of filing is within twice the hindsight optimum on every sequence of uses, and no rule without foresight does better, under fixed known costs and with staleness left out'
version: 1
role: counter
tags:
- design-rationale
- epistemology
date: '2026-10-15'
line: nucleating-argument
objects_to:
- CLAIM-303
grounds:
- THEORY-tmplx6hr
summary: >-
  Filed at the owner's request, from the rent-or-buy result of Karlin et al.
  1988 ([THEORY-tmplx6hr](../theory.d/THEORY-tmplx6hr.md)) set against [CLAIM-303](CLAIM-303.md)'s clause that recurrence is
  evidence of reuse, not the criterion. In [CLAIM-303](CLAIM-303.md)'s own terms the break-even
  rule needs no forecast and is worst-case optimal; [ADR-032](../decisions.d/ADR-032.md)'s second-occurrence
  rule is that rule when filing costs about one reconstruction. It does not
  reach staleness, which the theorem forbids rather than prices, or drifting
  costs, and where reuse can be forecast an expected-reuse rule can do better,
  so [CLAIM-303](CLAIM-303.md)'s criterion survives there.
---
<!-- inactive-ok-file: CLAIM-303 CLAIM-185 — Proposed; the claim objected to, and an open claim cited as open -->

# CLAIM-tmpc3sk7: Where reuse cannot be forecast, recurrence weighted by reconstruction cost is the filing criterion, not only evidence for one: filing once the reconstruction already paid for equals the cost of filing is within twice the hindsight optimum on every sequence of uses, and no rule without foresight does better, under fixed known costs and with staleness left out

## The claim

[CLAIM-303](CLAIM-303.md) prices filing as an upfront cost F against reconstruction c_r
per use, with access and verification c_a and upkeep u per use once
filed, and files when expected reuse n exceeds F/(c_r − c_a − u). Its
last clause keeps recurrence out of the criterion: recurrence is evidence
that reuse will come, and the criterion is the expected reuse itself.

That needs a forecast of n, and the record rarely has one. Without it,
the question becomes what rule does well whatever the sequence of uses
turns out to be. Karlin, Manasse, Rudolph and Sleator answer it for two
states with fixed prices ([THEORY-tmplx6hr](../theory.d/THEORY-tmplx6hr.md)): switch "when the cost of
making the change equals the extra cost incurred due to being in state A
instead of A'". Here state A is reconstructing each time, A' is having
filed, the extra cost of staying in A is c_r − c_a − u per use, and the
change costs F. The rule is to file at the use where the reconstruction
overpaid so far reaches F.

On every sequence that rule costs at most twice what filing with
hindsight would have cost. If reuse stops before the break-even point,
it paid exactly what hindsight pays. If reuse stops at the break-even
point, it paid about 2F plus upkeep against hindsight's F plus upkeep.
After that, both pay upkeep per use. No rule without foresight
guarantees better than 2: an adversary can stop reuse the moment the
argument is filed. The paper proves this for snoopy caching, whose
filed state costs nothing per use. The extension to a filed state with
per-use cost c_a + u is the record's, by the same accounting.

So where reuse cannot be forecast, the past recurrences, each weighted
by what it cost to redo, are the criterion. The decision is a function
of them, and it carries a guarantee that no forecast-based rule can
carry when there is no forecast.

## What it gives the record

[ADR-032](../decisions.d/ADR-032.md)'s second-occurrence rule is the break-even rule when F is about
one reconstruction's overpayment. The rule should file sooner when
filing is cheap, later when filing is dear, and at once when filing
costs nearly nothing, as with setting a found brick aside
([CASE-tmpd5exw](../cases.d/CASE-tmpd5exw.md)). A11's "rare, expensive-to-reconstruct
argument" is filed by the break-even rule after its first expensive
reconstruction. The unweighted count is what fails, not recurrence as
such.

## What it does not say

- **Anything about staleness.** The theorem forbids stale reads rather
  than pricing them. [CLAIM-303](CLAIM-303.md)'s added term, that reusing an obsolete
  argument may cost more than recomputing it, is outside the result. A
  filed argument that can go wrong unnoticed is not the paper's two
  fixed-price states.
- **That the guarantee holds with drifting or unknown costs.** F, c_r,
  c_a and u are fixed and known in the proof. The record's reconstruction
  costs are estimates, and reconstruction gets cheaper as related
  arguments are filed.
- **That worst-case rules beat expected-value rules.** Where reuse can be
  forecast, a rule using the forecast can do better on average. There
  [CLAIM-303](CLAIM-303.md)'s criterion stands, and this objection narrows the clause
  instead of defeating it.
- **That it covers more than two options.** With a third, such as
  filing a pointer instead of the argument, the deterministic bound rises
  to 3 ([THEORY-tmplx6hr](../theory.d/THEORY-tmplx6hr.md)).
- **That the paper says this.** Its case is when to stop maintaining a
  copy. Reading it as when to file is the record's mirror-image use of
  the same principle ([NOTE-tmp6n3s5](../notes.d/NOTE-tmp6n3s5.md)).
- **Anything about [ADR-032](../decisions.d/ADR-032.md)'s other reason.** The second-occurrence rule
  is also a throttle on capture by agents, and this objection says
  nothing about that.

## How [CLAIM-303](CLAIM-303.md) could answer

It could restrict "the criterion" to the case where reuse is forecastable
and concede the clause elsewhere. Or it could hold that the record always
has some forecast, such as the line an argument belongs to or the
question it answers, so that the worst case is the wrong standard.
[CLAIM-185](CLAIM-185.md)'s threshold would then need to say which case the record is in.
