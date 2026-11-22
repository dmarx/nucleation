### Added

- [CASE-341](record/cases.d/CASE-341.md): an executed study ([LEAD-016](record/leads.d/LEAD-016.md)) that runs a reduced version of [CASE-117](record/cases.d/CASE-117.md) with identical linear operators, four contexts (one rare), and four influence rules: mixture-of-experts gating, gating with a balancing loss, gating with a usage bias, and a multiplicative contribution rule. Each rule was run with and without spare operators, testing recovery when rare, removal and suppression. Code, tests and results are in `scratch/studies/lead-016/`.
- [CLAIM-918](record/claims.d/CLAIM-918.md): under softmax-gradient routing, the part of a rare operator's growth that depends on its own performance is proportional to its share, so its recovery exponent at rarity does not reflect its competence. A multiplicative contribution rule does not have this property (demonstrated, checked in [CASE-341](record/cases.d/CASE-341.md)).
- [CLAIM-919](record/claims.d/CLAIM-919.md): whether a suppressed rare-context specialist returns is decided by spare capacity, not by whether it kept its competence. It files two readings for the owner (empirical).

### Changed

- Dated notes of 2026-11-22 were added to [LEAD-016](record/leads.d/LEAD-016.md), [CASE-117](record/cases.d/CASE-117.md), [QUESTION-132](record/questions.d/QUESTION-132.md), [QUESTION-134](record/questions.d/QUESTION-134.md), [QUESTION-083](record/questions.d/QUESTION-083.md), [QUESTION-135](record/questions.d/QUESTION-135.md), [QUESTION-133](record/questions.d/QUESTION-133.md) and [QUESTION-125](record/questions.d/QUESTION-125.md). [LEAD-016](record/leads.d/LEAD-016.md) gains `operationalized_in` [CASE-341](record/cases.d/CASE-341.md). No status changed.
- The run-lead skill gains a step: on a shared machine, stop processes only by their PID, keep scratch files in a subdirectory named after the lead, and measure the pace under the real load.
