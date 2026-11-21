---
status: Proposed
title: 'Alternative A for the admission test of a synthesis: the test for a claim whose premises are claims decides whether a synthesis also yields a claim, not whether it is kept; a synthesis that organizes held components is filed as an account of its own scope whether or not it yields a claim, and only a recap, a synthesis that adds nothing but labels, stays in the curation entry'
version: 1
tags:
- record
date: '2026-11-21'
summary: >-
  One of three alternatives (with [ADR-tmpoxu5i](ADR-tmpoxu5i.md) and [ADR-tmpkiuac](ADR-tmpkiuac.md)) answering
  the owner's worry of 2026-11-20 that [ADR-075](ADR-075.md)'s language "might be
  discouraging us from documenting useful syntheses we may have already
  constructed", and their concern of 2026-11-21 about "potentially
  rejecting content we might want prematurely". Step 5's admission routes
  are kept as the test a claim whose premises are claims passes ([ADR-084](ADR-084.md)).
  What changes is what follows a failure. A synthesis that passes no
  route is filed as an account of its own scope, a line, a part of one or
  a theme, instead of being kept only in the curation entry. A recap stays
  in the curation entry. "Admit" becomes "file as a claim". The
  assistant's lean.
---
<!-- inactive-ok-file: ADR-tmpoxu5i ADR-tmpkiuac — Proposed; the alternatives filed with this one -->

# ADR-tmpi2grj: Alternative A for the admission test of a synthesis: the test for a claim whose premises are claims decides whether a synthesis also yields a claim, not whether it is kept; a synthesis that organizes held components is filed as an account of its own scope whether or not it yields a claim, and only a recap, a synthesis that adds nothing but labels, stays in the curation entry

*Filed with two alternatives, [ADR-tmpoxu5i](ADR-tmpoxu5i.md) (B) and [ADR-tmpkiuac](ADR-tmpkiuac.md) (C). The owner chooses. The context is shared and given in full here.*

## Context

[ADR-075](ADR-075.md) added a synthesis audit and, at step 5, three routes by which a synthesis earns an entry as a claim: a separating case, a derivation, a discriminating prediction. Its language is about admission. "Admit it, or don't." A synthesis that passes no route "is exhausted by its components. It is not filed. It and its audit stay in the curation entry". [ADR-084](ADR-084.md) later made SYNTHESIS the scheme of accounts and turned the routes into the test for a claim whose premises are claims. The `read-and-file` skill now says: "File what it adds as a claim, or nothing … If nothing passes, file no claim. Keep the synthesis and its audit in the curation entry." An account is filed only for "a synthesis of a line, or of a part of one".

So a synthesis that fails the test as a claim and is not of a line goes nowhere but a curation entry. On 2026-11-20 that was ten integrations the owner wanted on the record, the principles of the manuscript "From Obstruction to Reorganization". Eight of them were filed as accounts only at the owner's direction, and against the scope [ADR-083](ADR-083.md) names (workbench entry of 2026-11-20). The owner then raised two concerns:

- "I worry that [ADR-075](ADR-075.md)'s language might be discouraging us from documenting useful syntheses we may have already constructed" (2026-11-20).
- On the retrospective's recommendation to run the test when an integration is drafted: "my concern is potentially rejecting content we might want prematurely" (2026-11-21).

[ADR-075](ADR-075.md)'s guards remain good reasons: salience without work, a real integration lost to loose wording, a free parameter. They guard against filing a broad synthesis *as a claim*. They do not argue against giving it an address as an account, which earns no standing ([ADR-084](ADR-084.md)).

## Decision

1. **The test routes; it does not reject.** Step 5's three routes stay as they are. They decide whether a synthesis yields a claim: the narrowest integrating sentence that passes is filed as a CLAIM, as now. Wherever [ADR-075](ADR-075.md) and the skills say "admit", read "file as a claim".
2. **A synthesis that organizes held components is filed as an account**, whether or not it yields a claim. Its scope is a line, a part of one, or a theme that crosses lines (as the proposed decision on cross-line accounts in pull request 593 allows). If the scope has an account, the synthesis revises it as a new version; if not, it files one. The account maps every component, attributes every link, and lists under "Not stated on the record" each link the test failed, with the reason.
3. **A recap stays in the curation entry.** A synthesis that adds nothing but labels to components already mapped together in an account is recorded in the curation entry, as now.
4. **A link that contradicts a component is not mapped as held.** It goes under "Not stated on the record" with the component it contradicts, as the predicted cycle's sequence did against [CLAIM-474](../claims.d/CLAIM-474.md).

## Demonstration

**The skill wording.** In `read-and-file`, step 9, "File what it adds as a claim, or nothing" becomes "File what it adds as a claim, and its map as an account". "If nothing passes, file no claim. Keep the synthesis and its audit in the curation entry, linked to the components" becomes "If nothing passes, file no claim. The map still goes in its scope's account, and the audit in the curation entry." "A synthesis of a line, or of a part of one, revises that scope's account" becomes "A synthesis of a line, a part of one, or a theme across lines (as the proposed decision on cross-line accounts in pull request 593 allows) revises that scope's account". `synthesis-review`'s Arm B "the link fails for another reason" keeps its rule: the account names the link under "Not stated".

**The case of 2026-11-20 under this rule.** P1 and P3 are already stated. P2 and P4 to P10 are filed as eight accounts by the rule, with no direction needed. The cycle stated as a sequence contradicts [CLAIM-474](../claims.d/CLAIM-474.md) and [CLAIM-532](../claims.d/CLAIM-532.md), so it goes under "Not stated" in an account of the cycle's components. Its narrowed part passes and is filed as a claim, [CLAIM-794](../claims.d/CLAIM-794.md). The outcome is what the owner directed, reached by rule.

**The retrospective's concern.** Running the test at drafting time becomes harmless under this rule, since a failure loses nothing. It only says which sentences are claims.

## Alternatives

- **B, [ADR-tmpoxu5i](ADR-tmpoxu5i.md):** the same, for syntheses the owner constructs or asks for only. Syntheses found in a source keep [ADR-075](ADR-075.md)'s rule.
- **C, [ADR-tmpkiuac](ADR-tmpkiuac.md):** no test at filing. Every synthesis worth keeping is filed as an account, and the test for claims is run at the next synthesis review.
- **Change the wording only.** Rename "admit" and "not filed", and keep the outcome. Rejected because the outcome, not the word, is what left the ten principles with nowhere to go.

## Consequences

- [ADR-075](ADR-075.md) and [ADR-084](ADR-084.md) take history notes. The `read-and-file` and `synthesis-review` skills change as above.
- More accounts. The synthesis review's coverage and cross-line audit (as the proposed decision on cross-line accounts in pull request 593 allows) keep them in view.
