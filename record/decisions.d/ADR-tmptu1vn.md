---
status: Proposed
title: 'Syntheses get a scheme of their own, SYNTHESIS, with statuses about the integration, a closed admission route, components whose standing is derived, and a generated current-account view'
version: 2
history:
- version: 2
  date: '2026-11-07'
  note: >-
    At A's joint review of #422 and #424, pasted by the owner. Admission
    is a field of its own, `admission`, and `Unadmitted` leaves the
    status vocabulary, so epistemic standing, admission and component
    dependency are separate axes. `route` is required only while
    admitted, and `role` is required. Five lint rules enforce what the
    fields cannot say: premises within integrates, a Current synthesis
    resting only on what is in force or adopted, and derived meaning
    demonstrated. The view shows each component's kind and only admitted
    syntheses. CASE's `illustrates` accepts a SYNTHESIS. Relations
    describing the current account are repointed, and `complements`
    waits on dmarx/luria#358. A fixture fires every rule.
tags:
- record
date: '2026-11-07'
summary: >-
  A synthesis filed as a CLAIM strains the CLAIM scheme four ways. Its
  components' voice and standing live in prose and drift. Its admission
  route has no field. CLAIM's status vocabulary has no word for
  "exhausted by its components", so the first synthesis that failed
  admission was marked Rejected, which says false. And nothing renders
  the record's current account, which the owner wants. This decision
  adds a SYNTHESIS scheme. It keeps three judgements apart: a status for
  the integrating account (Current, Proposed, Rejected, Superseded); an
  `admission` field (admitted or unadmitted), saying whether it earned
  an entry; and relations for its components. It has a closed `route`,
  required while admitted,: hypothesis, derived or integration. It has
  `integrates` and `premises` relations, whose targets' standing a
  generated view derives. The view, docs/current-account.md, is a Jinja
  template that sets out every Current or Proposed synthesis by line,
  with each component's status read from the component when the page is
  built. The five syntheses filed from "Individuation, Possibility, and
  Disposition" are moved into it as the demonstration, and their CLAIMs
  are Superseded by the new entries. ARG's `concludes` accepts a
  synthesis. Rejected: a route field on CLAIM; a CLAIM-only status
  vocabulary; DP's document rendering; the status quo.
---
<!-- inactive-ok-file: ARG-tmp4iu19 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-tmpdf15p — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-tmpdlr93 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-tmpgxas4 — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: ARG-tmpovvgn — filed from the same exchange, Rejected -->
<!-- inactive-ok-file: CASE-tmpnlf5c — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CLAIM-tmpagkxi — filed from the same exchange, Proposed -->
<!-- inactive-ok-file: CLAIM-tmplgp4k — filed from the same exchange, Proposed -->
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
  Three judgements are kept on separate axes (version 2):
  - **`status`, the epistemic standing of the integrating account**, from
    `synthesis-statuses`:
    - `Current`: the account the owner has adopted for its line; the
      scheme's in-force word;
    - `Proposed`: argued, not adopted;
    - `Rejected`: the integrating claim was tested and failed;
    - `Superseded`: a later synthesis covers the same integration.
  - **`admission`, whether it earned an entry of its own**, required,
    from `synthesis-admission`:
    - `admitted`: it passed a route;
    - `unadmitted`: it passed none, or lost the one it passed. It is
      kept, and it is not refuted.

    Admission is judged apart from belief. An unadmitted synthesis keeps
    whatever status it had, and leaves the current-account view.
  - **Component dependency, in its relations:**
    - `integrates`, required: every entry the synthesis puts together, of
      any scheme;
    - `premises`: the components it could not stand without, CLAIMs or
      syntheses;
    - `bears_on`: questions;
    - `argued_by`: the ARGs concluding it;
    - `illustrated_by`: the CASEs illustrating it;
    - `supersedes` and `superseded_by`: between syntheses, and from the
      CLAIMs a synthesis replaces.
- **`route`**, from `synthesis-routes`: `hypothesis`, `derived` or
  `integration`, the routes of ADR-tmpe7y42 step 5. It is required while
  `admission` is `admitted`. An unadmitted entry's former route, if it had
  one, is in its history.
- **`role`, required, `warrant`, `defeated_if`, required, `tags` and
  `line`**, as on CLAIM. `defeated_if` states the defeat by the route.
- **Relations into the scheme.** CLAIM's `superseded_by`, ARG's
  `concludes` and CASE's `illustrates` accept a SYNTHESIS.
- **What the fields cannot say is linted** (`luria.yaml`, `lint.fail_on`):
  - `premise_outside_integrates` and
    `synthesis_premise_outside_integrates`: `premises` ⊆ `integrates`;
  - `current_on_premise_not_in_force`: a Current synthesis resting on a
    claim that is not Active;
  - `current_on_synthesis_not_current`: a Current synthesis resting on a
    synthesis that is not Current;
  - `derived_not_demonstrated`: a derived synthesis whose warrant is not
    `demonstrated`.
- **Components' standing is derived, never copied (DP-2).** The voice of
  each component, which no field records, stays in the body. Its status is
  read from the component.
- **A current-account view**, `docs/current-account.md`, rendered by
  `luria index` from `record/views.d/current-account.md.j2`.
  - It sets out every admitted synthesis that is Current or Proposed,
    grouped by line.
  - A synthesis spanning lines is set out under its first line and
    pointed to from the others.
  - Each entry shows its route, role, warrant and version, its summary,
    and a table of its components. Each row gives the component's kind
    (its scheme), its status read when the page is built, and whether it
    is a premise. An Open QUESTION, an Active TERM and a Proposed CLAIM
    are different kinds of standing.
  - Each entry ends with what would defeat the integration.
- **Filing.** The read-and-file skill's step 9b files an admitted
  synthesis as a SYNTHESIS, with `admission`, `route` and `role`. A merged
  SYNTHESIS that loses its admission becomes `unadmitted`, with the reason
  in its history. A synthesis held only as a legacy CLAIM is revised by
  filing a SYNTHESIS that supersedes it.
- **The demonstration (ADR-071).**
  - **The five syntheses admitted in #422 move into the scheme.** Each
    SYNTHESIS entry carries the claim's title, route, defeater and body
    unchanged, and each CLAIM becomes Superseded by its entry:
    - CLAIM-tmp6xhn3 becomes SYNTHESIS-tmpg2eh2;
    - CLAIM-tmp2ka9y becomes SYNTHESIS-tmpj2lnj;
    - CLAIM-tmpcdshj becomes SYNTHESIS-tmp46moy;
    - CLAIM-tmpnjz70 becomes SYNTHESIS-tmprmcy0;
    - CLAIM-tmptfuky becomes SYNTHESIS-tmp73anp.
  - **Relations describing the current account are repointed.** Seven
    ARGs and one CASE pointed at the moved claims. ARG-tmpvxtof now
    concludes SYNTHESIS-tmp46moy. ARG-tmp0fc4y, ARG-tmp4iu19,
    ARG-tmpdf15p, ARG-tmpdlr93, ARG-tmpgxas4 and ARG-tmpovvgn now
    conclude, and CASE-tmpnlf5c illustrates, SYNTHESIS-tmp73anp.
    Historical relations stay: the claims' own `superseded_by`, and the
    history notes.
  - **The fixture.** `scratch/formal/synthesis_fixture.py` builds a
    throwaway record from this `luria.yaml`, with eight syntheses: a
    derived result, an explanatory integration, an unadmitted synthesis,
    and one case for each lint rule. It checks that each rule fires on its
    case and nowhere else. It checks that the view shows the admitted
    syntheses and hides the unadmitted one, shows each component's kind,
    and shows a component's status change on the next render. All checks
    pass (DP-4).

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

- **`complements` does not cross into the scheme yet.** It is symmetric,
  and luria mishandles a symmetric relation across schemes
  (dmarx/luria#358, which CLAIM's `complements` already cites). The two
  CLAIMs that complement moved syntheses keep pointing at the superseded
  CLAIMs until that is fixed. CLAIM-tmpagkxi complements CLAIM-tmpnjz70,
  and CLAIM-tmplgp4k complements CLAIM-tmptfuky. The links resolve, and
  the superseded CLAIMs name their successors.
- **ARG's `rests_on`** still takes only CLAIMs. An argument resting on a
  synthesis as a premise has not been needed yet.
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
