### Added

- CASE-tmpnti0m: an executed study (LEAD-016) that runs a reduced version of CASE-117 with identical linear operators, four contexts (one rare), and four influence rules: mixture-of-experts gating, gating with a balancing loss, gating with a usage bias, and a multiplicative contribution rule. Each rule was run with and without spare operators, testing recovery when rare, removal and suppression. Code, tests and results are in `scratch/studies/lead-016/`.
- CLAIM-tmp1u4m3: under softmax-gradient routing, the part of a rare operator's growth that depends on its own performance is proportional to its share, so its recovery exponent at rarity does not reflect its competence. A multiplicative contribution rule does not have this property (demonstrated, checked in CASE-tmpnti0m).
- CLAIM-tmp1jz5w: whether a suppressed rare-context specialist returns is decided by spare capacity, not by whether it kept its competence. It files two readings for the owner (empirical).

### Changed

- Dated notes of 2026-11-22 were added to LEAD-016, CASE-117, QUESTION-132, QUESTION-134, QUESTION-083, QUESTION-135, QUESTION-133 and QUESTION-125. LEAD-016 gains `operationalized_in` CASE-tmpnti0m. No status changed.
- The run-lead skill gains a step: on a shared machine, stop processes only by their PID, keep scratch files in a subdirectory named after the lead, and measure the pace under the real load.
