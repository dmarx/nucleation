### Changed

- [ADR-tmp1304r](record/decisions.d/ADR-tmp1304r.md) (Proposed): a claim's `rests_on` may name a SYNTHESIS, and SYNTHESIS gains the derived converse `supports`. The `argument` chain now walks the named pattern `rests_on_claim`, which keeps its claim-to-claim steps, since a chain stays within one scheme.
- [CLAIM-338](record/claims.d/CLAIM-338.md) now rests on [SYNTHESIS-011](record/syntheses.d/SYNTHESIS-011.md), and [CLAIM-544](record/claims.d/CLAIM-544.md) on [SYNTHESIS-007](record/syntheses.d/SYNTHESIS-007.md). Each had rested on the claim that moved into the scheme.
- The `synthesis-review` skill repoints a claim's `rests_on` when it moves the claim rested on.
