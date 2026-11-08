---
status: Proposed
title: 'A SYNTHESIS is an account of a scope of the record''s argument and asserts nothing of its own, and whatever adds to its components is a CLAIM: the admitted syntheses return to the claims they were, the admission test becomes the test for filing a claim whose premises are claims, and a claim''s premises are claims again'
version: 1
tags:
- record
date: '2026-11-08'
summary: >-
  [ADR-076](ADR-076.md) gave syntheses a scheme. An entry earned a place in it by passing one of
  [ADR-075](ADR-075.md)'s admission routes. Asked what the admitted syntheses add, the
  record's answer was one proposition each, with a credence, a voice, a
  warrant and a defeater. Those are a CLAIM's fields. The owner observed
  that such an addition should be a claim, which is atomic however many
  premises it has. The owner also observed that the unadmitted accounts,
  which map a scope's components and add nothing, are what "synthesis"
  means. This decision makes SYNTHESIS the scheme of accounts only. Its
  status is whether the mapping is right. Its defeater is fidelity. It has
  no role, warrant, route or premises. Anything that adds to its components
  is a CLAIM, filed under [ADR-072](ADR-072.md)'s rule. [ADR-075](ADR-075.md)'s routes become the way
  such a claim shows it has content of its own. The nine claims moved into
  the scheme are restored under their own codes, and the two syntheses
  that were never claims become new claims. A claim's `rests_on` names
  claims only again, so the patches [ADR-077](ADR-077.md) and [ADR-080](ADR-080.md) made are undone.
  It supersedes [ADR-076](ADR-076.md), [ADR-077](ADR-077.md) and [ADR-080](ADR-080.md), and amends [ADR-075](ADR-075.md), [ADR-078](ADR-078.md)
  and [ADR-tmpyihxy](ADR-tmpyihxy.md). Rejected: a field telling the two kinds apart within
  one scheme; the status quo; moving the integrations to new claim codes;
  an `integrates` field on CLAIM; making accounts generated views.
---
<!-- inactive-ok-file: ADR-075 ADR-076 ADR-077 ADR-078 ADR-079 ADR-080 ADR-tmpyihxy ADR-tmpyb8vm — Proposed; the decisions this supersedes or amends -->
<!-- inactive-ok-file: SYNTHESIS-001 SYNTHESIS-002 SYNTHESIS-003 SYNTHESIS-004 SYNTHESIS-005 SYNTHESIS-006 SYNTHESIS-007 SYNTHESIS-008 SYNTHESIS-009 SYNTHESIS-010 SYNTHESIS-011 — Superseded by the claims they return to -->
<!-- inactive-ok-file: SYNTHESIS-tmpllsy7 SYNTHESIS-tmp7nvem SYNTHESIS-tmp5p7lm SYNTHESIS-tmp9cgig — Proposed; the accounts of the demonstration -->
<!-- inactive-ok-file: CLAIM-336 CLAIM-545 CLAIM-610 CLAIM-611 CLAIM-615 CLAIM-620 CLAIM-624 CLAIM-628 CLAIM-629 CLAIM-308 CLAIM-176 — Proposed; restored claims and the claims cited as instances -->

# ADR-tmp72iro: A SYNTHESIS is an account of a scope of the record's argument and asserts nothing of its own, and whatever adds to its components is a CLAIM: the admitted syntheses return to the claims they were, the admission test becomes the test for filing a claim whose premises are claims, and a claim's premises are claims again

## Context

[ADR-075](ADR-075.md) began from a gap in filing. An exchange's syntheses were filed as
recaps mapped to their turns, so the record "can't say what its current
account is", and later syntheses "can't be checked for drift". It added an
admission test, so that a source's broad summary would not gain standing as
one more claim. [ADR-076](ADR-076.md) gave syntheses a scheme. An admitted SYNTHESIS was
one that had passed a route, recorded in a `route` field:

- hypothesis: a case where every component holds and the integration fails;
- derived: a valid, nontrivial inference no claim holds;
- integration: a dependency, mechanism or prediction the components leave
  open.

[ADR-tmpyihxy](ADR-tmpyihxy.md) then used the scheme's unadmitted entries for accounts held in
parts.

The owner asked what the admitted syntheses add. Read one by one, each adds
one proposition:

- **[SYNTHESIS-008](../syntheses.d/SYNTHESIS-008.md), [SYNTHESIS-009](../syntheses.d/SYNTHESIS-009.md) and the nucleating-argument line's
  synthesis** ([SYNTHESIS-tmpllsy7](../syntheses.d/SYNTHESIS-tmpllsy7.md)) are short derivations: a third complex
  that decides frustration, bounds on readiness, and a regime where two
  filing rules part.
- **The other eight are hypotheses.** Each adds an identification, a
  generalization or a claim of joint sufficiency. Admission often narrowed
  them to one clause: [SYNTHESIS-004](../syntheses.d/SYNTHESIS-004.md) was admitted on one link of three.

Each has a credence (`status`), a voice (`role`), a warrant and a
`defeated_if`. Those are a CLAIM's fields ([ADR-032](ADR-032.md), [ADR-043](ADR-043.md)), and having many
premises does not make a claim less atomic. The owner put it so: adding a
result or a claim should still be a claim, and the unadmitted case is the
one true to the meaning of "synthesis".

The record already shows the confusion in three ways:

- **The same kind of thing is filed both ways.** [CLAIM-628](../claims.d/CLAIM-628.md) and [CLAIM-629](../claims.d/CLAIM-629.md),
  results derived and checked by script, are claims. [SYNTHESIS-008](../syntheses.d/SYNTHESIS-008.md) and 009
  are the same kind of result in another scheme. [CLAIM-592](../claims.d/CLAIM-592.md), "one theorem
  with its proof", was refused admission and stayed a claim.
- **The admission test repeats an existing rule.** "Valid, nontrivial, not
  held" is [ADR-072](ADR-072.md)'s rule for every idea: it gets a code when it has
  content of its own and is not already held.
- **The claim graph was cut in two and patched back together.**
  - Nine of the eleven admitted syntheses began as claims, and [ADR-077](ADR-077.md)
    had to design their move so that it changed nothing.
  - [ADR-080](ADR-080.md) let a claim's `rests_on` name a SYNTHESIS, and so the
    `argument` chain had to walk a pattern.
  - The third review found that a moved claim's objections would be
    stranded, since `objects_to` accepts only CLAIMs.

Meanwhile the scheme strained the accounts. An account "cannot be set
Current", is Proposed as though it were a credence, and is called
"unadmitted" as though it had been refused.

## Decision

- **A SYNTHESIS is an account of a scope.** A scope is a line or a part of
  one ([ADR-tmpyihxy](ADR-tmpyihxy.md)). The account:
  - names every component in `integrates`, with its voice and status in the
    body;
  - attributes each link it states to the entry that states it;
  - adds nothing.

  A link no component states goes under "Not stated on the record". If the
  link is worth stating, it is filed as a claim, and the account then
  integrates that claim.
- **Its fields are an account's.**
  - **Kept:** `status`, `defeated_if`, `tags`, `line`, `integrates`,
    `bears_on`, and supersession both ways.
  - **Removed:** `role`, `warrant`, `admission`, `route`, `premises`,
    `grounds`, `uses`, and the converses that served them, together with
    the vocabularies `synthesis-admission` and `synthesis-routes`.
  - **`defeated_if` is fidelity.** It names a component misstated or
    misattributed, an in-force component of the scope left out, or a link
    stated that no component states.
- **Its status is whether the mapping is right.** It is not a credence.
  - **Current:** the record's account of its scope, its mapping reviewed by
    the owner.
  - **Proposed:** drafted and offered, its mapping not yet reviewed.
  - **Superseded:** replaced by a revised account, or a claim that returned
    to CLAIM.

  Rejected leaves the vocabulary, since an unfaithful account is revised,
  not disbelieved. A Current account may integrate Proposed claims: its
  status vouches for the map, not for the territory.
- **What adds to its components is a CLAIM,** filed under [ADR-072](ADR-072.md)'s rule
  like any other.
  - **The routes become the test for such a claim.** [ADR-075](ADR-075.md)'s routes
    become the way a claim whose premises are claims shows it has content
    of its own: a separating case, a derivation or a discriminating
    prediction. The case or derivation goes in its body, under
    "Admission", as before.
  - **A realistic separating case is evidence against the claim.** A case
    that is not stipulated, and could plainly occur, is checked against the
    claim's own `defeated_if` before the claim is filed. Such a case shows
    the claim is separate from its premises, but it may also show the claim
    is false.
- **The admitted syntheses return.**
  - **The nine claims are restored.** The nine claims moved into the scheme
    take back their own codes. Each gets the synthesis's current title,
    body, defeater, role and warrant as a new version, and the synthesis's
    premises as its `rests_on`. Standing is kept: Current becomes Active,
    and Proposed stays Proposed.
  - **The two that were never claims are filed new.** [SYNTHESIS-008](../syntheses.d/SYNTHESIS-008.md) and
    [SYNTHESIS-009](../syntheses.d/SYNTHESIS-009.md) become new claims.
  - **Each synthesis is Superseded by its claim,** and the relations
    pointing at it are repointed to the claim: an ARG's `concludes`, a
    CASE's `illustrates`, a claim's `rests_on` and `corroborates`, and a
    reading's `corroborates`.
- **A claim's premises are claims again.**
  - **The [ADR-080](ADR-080.md) patch is undone.** `rests_on` and `corroborates` on CLAIM
    and THEORY name CLAIMs only. The `argument` chain walks `rests_on`
    directly, and the pattern `rests_on_claim` is removed.
  - **The objection gap closes.** A claim that adds to its premises can
    now have objections like any other claim.
- **Supersession may cross the two schemes.**
  - **From claim to account:** a claim that turns out only to map its
    components is superseded by the account that holds the mapping.
  - **From account to claim:** a synthesis that turns out to be a claim is
    superseded by the claim.
  - **The `revisions` chain** walks claim-to-claim supersession through a
    pattern, `supersedes_claim`, because a luria chain stays within one
    scheme.
- **Lint.** The six rules on admission, routes and premises go. Two new
  rules take their place, and both fail the build:
  - a Current account integrating a Superseded claim;
  - a Current account integrating a Superseded account.

  An account that is in force must follow its components' revisions. This
  is the mechanical check that a map kept in prose otherwise lacks.
- **The current-account view** sets out each line's accounts, Current
  first, with each component's live standing. It lists the lines that have
  no account.
- **The review ([ADR-078](ADR-078.md)) changes arms.**
  - **Arm A** looks for claims that are accounts: claims that add nothing
    beyond their components. The account supersedes such a claim, and the
    claims resting on it are repointed to what it rested on.
  - **Arm B** looks for integrations held in parts. If one passes the test
    above, it is filed as a CLAIM. Either way, the scope's account records
    where the link is stated.
  - **Coverage** is [ADR-tmpyihxy](ADR-tmpyihxy.md)'s: one account per scope.
- **Supersedes and amends.**
  - **Superseded:** [ADR-076](ADR-076.md) (the scheme), [ADR-077](ADR-077.md) (moving a claim into it)
    and [ADR-080](ADR-080.md) (`rests_on` naming a SYNTHESIS). [ADR-079](ADR-079.md)'s derived
    converses are unaffected.
  - **Amended, [ADR-075](ADR-075.md):** its step 5 now applies to filing a claim, and
    steps 1 to 4 apply to accounts and to a source's syntheses as before.
  - **Amended, [ADR-078](ADR-078.md):** the review's arms, as above.
  - **Amended, [ADR-tmpyihxy](ADR-tmpyihxy.md):** an account is no longer "unadmitted", and it
    can be Current.
- **Demonstration ([ADR-071](ADR-071.md)).** This decision ships with its first
  application:
  - the eleven syntheses return to CLAIM;
  - the nucleating-argument line's synthesis, [SYNTHESIS-tmpllsy7](../syntheses.d/SYNTHESIS-tmpllsy7.md), is split
    in two. Its derivation becomes a claim. The synthesis itself becomes
    the line's account over its three part accounts and that claim.

## Alternatives considered

- **A field telling the two kinds apart within one scheme** (`form:
  integration | account`). This was proposed first. It keeps two kinds of
  entry in one scheme, with fields one kind requires and the other forbids,
  which is the admission and route arrangement over again. It also leaves
  the claim graph cut in two, so [ADR-080](ADR-080.md)'s patch and the objection gap
  stay.
- **The status quo.** Every move into the scheme needs repointing, every
  dependency needs a pattern, and the objection gap needs a `dialectic`
  pattern of its own. The accounts keep a status vocabulary written for
  credences.
- **Moving the integrations to new claim codes.** That gives one
  proposition three codes (for example [CLAIM-474](../claims.d/CLAIM-474.md), then [SYNTHESIS-006](../syntheses.d/SYNTHESIS-006.md), then
  a third). Restoring keeps the code that readers and other entries already
  cite, and the history notes record the round trip.
- **An `integrates` field on CLAIM,** so that claims which integrate can
  be listed. That duplicates the account's job. An integrating claim's
  dependencies are its `rests_on`, and its context is its scope's account.
  It can be added if a view needs it.
- **Accounts as generated views.** An account is written judgement: which
  components belong to a scope and who states each link. It cannot be
  derived from fields, and it needs an address and versions.

## Consequences

- **The view starts small.** No synthesis is admitted any more. The
  current-account view shows accounts only: the nucleating-argument line's
  three part accounts and its line account, and the accounts of
  records-of-inquiry and record-as-apparatus. Lines that admitted syntheses
  used to cover now show no account. Filing accounts for them is the next
  review's coverage work, and their integrating claims will be among the
  components.
- **The restored claims keep their "Admission" sections** as the record of
  how each showed it had content of its own.
- **Lint changes.** The restored claims' dependencies now show in the
  `argument` chain, and the existing claim checks (`inverted_premise` and
  the rest) apply to them.
- **Tooling follows.**
  - `scratch/formal/synthesis_fixture.py` is rewritten for the new rules.
  - The `synthesis-review` skill and step 9b of `read-and-file` are
    rewritten.
  - `scratch/formal/synthesis_candidates.py` keeps its ranking, which now
    feeds the new arms.
- **The cost** is one round trip for nine claims, and a scheme that is
  smaller and does one job.
