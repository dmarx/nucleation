---
status: Proposed
title: 'Syntheses get a scheme of their own, SYNTHESIS, with statuses about the integration, a closed admission route, components whose standing is derived, and a generated current-account view'
version: 1
tags:
- record
date: '2026-11-07'
summary: >-
  A synthesis filed as a CLAIM strains the CLAIM scheme four ways. Its
  components' voice and standing live in prose and drift. Its admission
  route has no field. CLAIM's status vocabulary has no word for "exhausted
  by its components", so the first synthesis that failed admission was
  marked Rejected, which says false. And nothing renders the record's
  current account, which the owner wants. This decision adds a SYNTHESIS
  scheme. It has its own statuses: Current, Proposed, Unadmitted, Rejected
  and Superseded. It has a required, closed `route`: hypothesis, derived
  or integration. It has `integrates` and `premises` relations, whose
  targets' standing a generated view derives. The view,
  docs/current-account.md, is a Jinja template that sets out every Current
  or Proposed synthesis by line, with each component's status read from
  the component when the page is built. The five syntheses filed from
  "Individuation, Possibility, and Disposition" are moved into it as the
  demonstration, and their CLAIMs are Superseded by the new entries.
  ARG's `concludes` accepts a synthesis.
  Rejected: a route field on CLAIM; a CLAIM-only status vocabulary; DP's
  document rendering; the status quo.
---
<!-- inactive-ok-file: ARG-tmp0fc4y — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-tmpvxtof — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: ADR-tmpe7y42 — Proposed; the admission protocol this scheme carries -->
<!-- inactive-ok-file: SYNTHESIS-tmpg2eh2 SYNTHESIS-tmpj2lnj SYNTHESIS-tmp46moy SYNTHESIS-tmprmcy0 SYNTHESIS-tmp73anp — Proposed; the demonstration -->
<!-- inactive-ok-file: CLAIM-tmp6xhn3 CLAIM-tmp2ka9y CLAIM-tmpcdshj CLAIM-tmpnjz70 CLAIM-tmptfuky — Superseded by the demonstration's entries -->
<!-- inactive-ok-file: CLAIM-545 — Proposed; the earlier synthesis filed as a CLAIM, for the sweep -->

# ADR-tmptu1vn: Syntheses get a scheme of their own, SYNTHESIS, with statuses about the integration, a closed admission route, components whose standing is derived, and a generated current-account view

## Context

[ADR-tmpe7y42](ADR-tmpe7y42.md) began filing a source's syntheses as CLAIMs, after an audit
and an admission test. It chose CLAIM over a scheme of its own, "until a
synthesis CLAIM strains". In the same pull request, dmarx/nucleation#422,
it strained four ways.

- **Standing in prose.** A synthesis puts together entries in several
  voices (the owner's, A's, the record's) and at several standings. As a
  CLAIM it can list them only in `rests_on`, `grounds` and `uses`, and say
  their status in its body. The body was written once, and the components'
  statuses move.
- **The route has no field.** [ADR-tmpe7y42](ADR-tmpe7y42.md)'s third version admits a
  synthesis by one of three routes: independent hypothesis, derived result
  or explanatory integration. Each has its own test and kind of defeat. On
  a CLAIM the route is a sentence in the body, so nothing can check that a
  derived synthesis has warrant `demonstrated`, or list syntheses by route.
- **No status says what admission found.** CLAIM shares THEORY's status
  vocabulary, whose `Rejected` "means the reason is wrong". The first
  synthesis to fail admission, the dispositional reframing, was first
  marked Rejected, and A's second review pointed out that this told
  readers it was false. It was withdrawn before merge, which works only
  while a code is unmerged.
- **No current account.** The owner asked where the synthesis is tracked
  and wants a current-account view. Each synthesis CLAIM renders on the
  claims index beside six hundred atomic claims, and no page says what the
  record now holds about how its claims fit together.

## Decision

- **A SYNTHESIS scheme** in `record/syntheses.d/`, allocated at merge.
  - **`status`, from `synthesis-statuses`.** These say where the
    integration stands, not whether its components are believed:
    - `Current`: the account the owner has adopted for its line; the
      scheme's in-force word;
    - `Proposed`: admitted and argued, not adopted;
    - `Unadmitted`: passed no route after it was filed; kept, and not
      refuted;
    - `Rejected`: the integrating claim was tested and failed;
    - `Superseded`: a later synthesis covers the same integration.
  - **`route`, required, from `synthesis-routes`:** `hypothesis`,
    `derived` or `integration`, the routes of [ADR-tmpe7y42](ADR-tmpe7y42.md) step 5.
  - **`role`, `warrant`, `defeated_if`, `tags` and `line`**, as on CLAIM.
    `defeated_if` is required, and states the defeat by the route.
  - **`integrates`, required:** every entry the synthesis puts together,
    of any scheme. **`premises`:** the components it could not stand
    without, CLAIMs or other syntheses. **`bears_on`:** questions.
    **`supersedes` and `superseded_by`:** between syntheses, and from the
    CLAIMs a synthesis replaces. CLAIM's `superseded_by` accepts SYNTHESIS.
  - **`argued_by`:** the ARGs concluding it. ARG's `concludes` accepts a
    SYNTHESIS, so an argument for or against an integration is filed
    against the integration, under step 10's rule for load-bearing or
    contested support.
- **Components' standing is derived, never copied ([DP-2](../../docs/design-principles.md#dp-2)).** The voice of
  each component, which no field records, stays in the body. Its status is
  read from the component.
- **A current-account view**, `docs/current-account.md`, rendered by
  `luria index` from `record/views.d/current-account.md.j2`.
  - It sets out every Current or Proposed synthesis, grouped by line.
  - A synthesis spanning lines is set out under its first line and
    pointed to from the others.
  - Each synthesis shows its route, role, warrant and version, its
    summary, and a table of its components. Each component row shows that
    component's status, read when the page is built, and whether it is a
    premise.
  - The page ends each entry with what would defeat the integration.
- **Filing.** The read-and-file skill's step 9b files an admitted
  synthesis as a SYNTHESIS, not a CLAIM. A synthesis found exhausted after
  merge becomes `Unadmitted`, which removes the gap [ADR-tmpe7y42](ADR-tmpe7y42.md) version 4
  left open.
- **The demonstration ([ADR-071](ADR-071.md)).** The five syntheses admitted in [#422](https://github.com/dmarx/nucleation/issues/422)
  are moved into the scheme. Each SYNTHESIS entry carries the claim's
  title, route, defeater and body unchanged. Each CLAIM becomes Superseded
  by its entry, so that what cites it still resolves:
  - [CLAIM-tmp6xhn3](../claims.d/CLAIM-tmp6xhn3.md) becomes [SYNTHESIS-tmpg2eh2](../syntheses.d/SYNTHESIS-tmpg2eh2.md);
  - [CLAIM-tmp2ka9y](../claims.d/CLAIM-tmp2ka9y.md) becomes [SYNTHESIS-tmpj2lnj](../syntheses.d/SYNTHESIS-tmpj2lnj.md);
  - [CLAIM-tmpcdshj](../claims.d/CLAIM-tmpcdshj.md) becomes [SYNTHESIS-tmp46moy](../syntheses.d/SYNTHESIS-tmp46moy.md);
  - [CLAIM-tmpnjz70](../claims.d/CLAIM-tmpnjz70.md) becomes [SYNTHESIS-tmprmcy0](../syntheses.d/SYNTHESIS-tmprmcy0.md);
  - [CLAIM-tmptfuky](../claims.d/CLAIM-tmptfuky.md) becomes [SYNTHESIS-tmp73anp](../syntheses.d/SYNTHESIS-tmp73anp.md).

  The view renders them under four lines.

## Alternatives considered

- **A route field on CLAIM.** It is the smallest change, and it records
  the route on its own axis. It leaves the other three strains standing:
  standing in prose, no status for an exhausted synthesis, and no
  current account short of a filtered index. The owner asked for the view.
- **A CLAIM-only status vocabulary with a word for "withdrawn".** It puts a
  fact about the filing into a credence vocabulary, the same category
  error as `Rejected`, only better labelled. The two vocabularies would
  drift.
- **DP's document rendering.** It assembles one page, but only as bodies
  concatenated in number order. It cannot group by line or derive a
  component's status. A view template can do both, and stays a pure
  function of the tree, so `luria index --check` can call it stale.
- **Status quo.** Syntheses stay CLAIMs, standing goes on drifting in
  prose, and the current account is reconstructed by whoever is asked for
  it, which is how this began.

## Consequences

- **ARGs about syntheses.** The two ARGs from [#422](https://github.com/dmarx/nucleation/issues/422) that concluded
  synthesis claims now conclude the syntheses: [ARG-tmpvxtof](../arguments.d/ARG-tmpvxtof.md) concludes
  [SYNTHESIS-tmp46moy](../syntheses.d/SYNTHESIS-tmp46moy.md), and [ARG-tmp0fc4y](../arguments.d/ARG-tmp0fc4y.md) concludes [SYNTHESIS-tmp73anp](../syntheses.d/SYNTHESIS-tmp73anp.md). ARG's
  `rests_on` still takes only CLAIMs. An argument resting on a synthesis
  as a premise has not been needed yet.
- **The sweep.** [CLAIM-545](../claims.d/CLAIM-545.md) and the syntheses left unaudited in earlier
  filings ([ADR-tmpe7y42](ADR-tmpe7y42.md)'s Context) are audited and, where admitted, moved
  into the scheme in a contribution of their own.
- **Adoption is the owner's.** No synthesis is Current until the owner
  makes it so. Until then the view says what is offered, not what is held.
- **The view is only as good as `integrates`.** A component left out of
  that field is invisible on the page, though the body may name it.
  [ADR-tmpe7y42](ADR-tmpe7y42.md)'s coverage check is where it is caught.
- **This pull request is stacked on [#422](https://github.com/dmarx/nucleation/issues/422).** It needs [#422](https://github.com/dmarx/nucleation/issues/422)'s syntheses and
  its temporary ADR codes. It merges after [#422](https://github.com/dmarx/nucleation/issues/422), or with it.
