<!-- scratch/studies/record-history/handcheck/README.md: LEAD-tmpn6mi2's checks 2 and 4, done blind -->
# Hand-check, 2026-11-26

A reader given the rules and each commit's diff, and not the class the
extraction gave, labelled every change to the entry. An item is correct when
the sampled class is among the reader's labels (for mechanical: when it is
the only one).

- Round 1 (`key.tsv`, `partA.txt`; seed 2026): revised 10/10, status 10/10,
  note 10/10, mechanical 10/10, relation_add 2/10. The eight misses were all
  relations added in the commit that created the entry, which the brief told
  the reader to label "created": a fault of the sheet, not of the extraction.
  The sampler no longer draws them.
- Round 2 (`round2/`; seed 2027, relation adds only, same reader, same rules):
  10/10.
- Check 2, so: 50/50 by the letter. The reader's ambiguities, each a limit
  the counts carry: a retitle that moves the old title into `statement` is a
  statement event (8 of round 1's revised items came from the claim-titles
  sweep, which profiles exclude as a sweep); a sweep writing the other side
  of a symmetric relation by hand is a relation add; an edge re-typed from
  `answers` to `bears_on` (ADR-060) is an add and a removal.
- Check 4 (`profiles_key.tsv`, the profile's values before the fix): the
  reader's date of last revision and inbound count agreed on 10 of 10; the
  revision count disagreed on 3, because a commit changing title and body
  counted twice. Fixed (revisions count commits); after the fix all three
  agree. The reader's table: CLAIM-1130 2 0 1, CLAIM-308 26 2 5, CLAIM-683
  10 1 2, CLAIM-702 7 1 4, CLAIM-979 3 0 1, CLAIM-1100 2 0 0, CLAIM-1325 0 0 3,
  CLAIM-884 3 0 0, CLAIM-926 3 0 0, CLAIM-793 4 1 1 (days, revisions, inbound).
