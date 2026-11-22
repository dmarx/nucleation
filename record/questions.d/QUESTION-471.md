---
number: 471
status: Open
formerly:
- QUESTION-tmp9n1ac
title: 'How can a record of inquiry that automates the incorporation of new material keep the speed of incorporation from outrunning its capacity to evaluate what it incorporates, and which of its checks are points at which an incorporation can still be stopped rather than reviewed after it has taken effect?'
version: 5
history:
- version: 2
  date: '2026-11-16'
  note: >-
    A dated note added: Hong Kong Monetary Authority (LIT-2696) read on 2026-11-16, NOTE-2018. No change of status or title.
- version: 3
  date: '2026-11-16'
  note: >-
    A dated note added: Natali et al. (LIT-2687) read on 2026-11-16, NOTE-2033. No change of status or title.
- version: 4
  date: '2026-11-16'
  note: >-
    A dated note added: Bovens and Zouridis (LIT-2661) read on 2026-11-16, NOTE-2030. No change of status or title.
- version: 5
  date: '2026-11-22'
  note: >-
    A dated note added: Frischmann and Benesch (LIT-3136) registered and read on 2026-11-22 for LEAD-152, NOTE-2359. No change of status or title.
tags:
- design-rationale
- epistemology
- software-engineering
date: '2026-11-15'
line:
- records-of-inquiry
summary: >-
  A's, from A30 §7 of the exchange "Assess Depp Heard Abuse" (2026-11-15),
  which reads this record itself as a small case of the exchange's
  argument: "Automation reduces the routine work of maintaining a coherent
  intellectual record. But checks, review stages, and explicit adoption
  decisions preserve opportunities to challenge what enters that record as
  authoritative." Its question: "How can an automated knowledge-production
  system increase its capacity to incorporate new material without
  allowing the speed of incorporation to outrun its capacity for critical
  evaluation?" The owner's procedural-friction claim, applied to the record.
  The wording is A's; adopting it is the owner's call.
---
<!-- inactive-ok-file: THEORY-1765 — Proposed or Deferred; filed from the exchange "Assess Depp Heard Abuse" or its readings, cited with its standing -->
<!-- inactive-ok-file: THEORY-1931 — Proposed or Deferred; filed from the exchange "Assess Depp Heard Abuse" or its readings, cited with its standing -->
<!-- inactive-ok-file: CLAIM-710 CLAIM-705 — filed from the same exchange, Proposed -->

# QUESTION-471: How can a record of inquiry that automates the incorporation of new material keep the speed of incorporation from outrunning its capacity to evaluate what it incorporates, and which of its checks are points at which an incorporation can still be stopped rather than reviewed after it has taken effect?

## Why it is open

A30 §7 of the exchange
(https://chatgpt.com/share/6afa2a8d-2598-83ea-8d1a-d9ceb992a99c) names the
record's own practices: claims with status, role and warrant kept apart,
defeaters, [DP-3](../../docs/design-principles.md#dp-3) (norms walked from prose to mechanism) and [DP-4](../../docs/design-principles.md#dp-4) (fire a
guard before trusting it), review, versioning, decision records and
automated checks. "So Nucleation is itself an interesting small-scale case
of the tension we've been examining." Then:

> **How can an automated knowledge-production system increase its capacity
> to incorporate new material without allowing the speed of incorporation
> to outrun its capacity for critical evaluation?**

"That is precisely the execution-versus-correction problem, applied to
intellectual inquiry."

In this record's terms: a filing of an exchange like this one produces
dozens of entries in a session, each Proposed, and the owner's review is
the corrective process. The owner's procedural-friction claim
([CLAIM-710](../claims.d/CLAIM-710.md)) asks where the points of intervention are; the
throughput claim ([CLAIM-705](../claims.d/CLAIM-705.md)), from the same exchange, says what
happens when entries needing review arrive faster than review resolves
them. Proposed status keeps an entry from counting as in force, so review
can come after filing without anything being foreclosed, unless later
entries come to rest on unreviewed ones.

## What would count as an answer

A description of which of the record's stages can stop an incorporation
(a pull request not merged, a lint that fails) and which only review it
after it is on the default branch (status reviews, synthesis reviews), with
the rates at which entries arrive and are reviewed, and a criterion for
when entries resting on unreviewed entries make later review remedial
rather than preventive.

## Note of 2026-11-16: Hong Kong Monetary Authority, read

An answer from banking supervision to this question's form. Place the points
at which a process can be stopped "before actions with significant customer,
financial, legal or operational implications take effect", timed by
detection, decision and stopping time (§7.2, p. 37). Set the rate of action by
the demonstrated capacity of review, not by technical throughput (§4.3,
p. 19). Do not count a formal review step that the volume has made
perfunctory. Relation: [THEORY-1931](../theory.d/THEORY-1931.md) bears_on.

## Note of 2026-11-16: Natali, read

The poster's problem, frictionless interfaces inviting uncritical acceptance of automated output, is this question's problem at the scale of one interaction: a filer accepting a reader's draft is a human accepting an automated recommendation. Its mechanisms are candidate checks: requiring the filer's own verification before the draft is shown as filed (a cognitive forcing function), or a step that challenges the draft rather than presenting it (an AI provocation). It offers no evidence that any of them works. The record's evidence is [THEORY-1765](../theory.d/THEORY-1765.md) (Buçinca et al.), which found such designs reduce over-reliance without eliminating it and are less liked.

## Note of 2026-11-16: Bovens and Zouridis, read

§7's observation that the move to system-level bureaucracy was insidious and never debated, and §6.1's
informatization review before new rules are digitized, are the institutional analogue of this question's
concern: automation of incorporation outrunning evaluation, and checks placed before it. Relation: bears_on.

## Note of 2026-11-22: Frischmann and Benesch, read
<!-- inactive-ok-file: THEORY-2267 — new of 2026-11-22, Proposed; the account filed from the reading for LEAD-152 -->

Frischmann and Benesch ([LIT-3136](../literature.d/LIT-3136.md), [NOTE-2359](../notes.d/NOTE-2359.md), [THEORY-2267](../theory.d/THEORY-2267.md)) report a distinction this question asks for: friction that only adds a cost to passage (a speed bump, a delay) against friction that blocks passage until a condition is shown (a checkpoint, a CAPTCHA), which alone creates a "governance seam" (p. 405 n. 89, quoting Frischmann and Ohm). In the question's terms, a check of the second kind is a point at which an incorporation can still be stopped; a delay is one only if someone uses the time to act. Their measures aim at one person's deliberation, so they say nothing on how a record's checks keep pace with its incorporation. Relation: [THEORY-2267](../theory.d/THEORY-2267.md) `bears_on` this question.
