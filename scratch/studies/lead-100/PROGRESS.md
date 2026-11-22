# LEAD-100 progress

- Lead: LEAD-100 (receiver-restricted informativeness order, with its own results)
- Branch: claude/lead-100-receiver-order (from origin/staging)
- Task: define an order on experiments that compares them only for receivers
  whose decision rules lie in a stated class, and prove its basic results
  without Blackwell's garbling theorem; check numerically; file as claims /
  cases / term. Settles ARG-019's open point if it has results.

## Done

- Step 1: checked the record. No receiver-restricted order is held
  (grep: receiver-restricted, restricted order, V-informative). NOTE-1048
  asks for one as an open question; CLAIM-199 says it does not supply one.

- Step 2: formal results worked out and checked numerically
  (rorder.py, run_checks.py, results.json, tests pass). All checks agree.

- Step 3: filed TERM-tmpjv1xh (definition), CLAIM-tmp03h8w (six results,
  demonstrated), CASE-tmphabte (executed study of the checks).
- Step 4: dated notes on LEAD-100, ARG-019 (readings (a) narrowed / (b)
  settled for the owner), CLAIM-199, CLAIM-225, CLAIM-050; changelog
  fragment record/changelog.d/lead-100.md.

## Next

- Report to the lead. Nothing else remains on this branch.

## Choices

- Definition: receivers on one fixed medium X (a disjoint union covers
  cross-modal chains); a receiver is a class of rules per action set;
  order = usable risk no worse for every bounded loss. Chosen because the
  record's cases (CLAIM-199, CLAIM-087) compare renderings for one reader.
- The lead's second branch (argue judged access tracks ideal
  informativeness) is not attempted: it is empirical and CLAIM-199's
  defeat condition already holds it.
