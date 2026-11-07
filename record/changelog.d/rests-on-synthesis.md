### Changed

- ADR-tmp1304r (Proposed): a claim's `rests_on` may name a SYNTHESIS, and SYNTHESIS gains the derived converse `supports`. The `argument` chain now walks the named pattern `rests_on_claim`, which keeps its claim-to-claim steps, since a chain stays within one scheme.
- CLAIM-338 now rests on SYNTHESIS-tmprnoj1, and CLAIM-544 on SYNTHESIS-007. Each had rested on the claim that moved into the scheme.
- The `synthesis-review` skill repoints a claim's `rests_on` when it moves the claim rested on.
