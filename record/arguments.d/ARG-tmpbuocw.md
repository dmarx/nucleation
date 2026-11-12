---
status: Proposed
title: 'Halpern and Moses''s result on unreliable channels applies to a record read asynchronously: publishing a standing does not make it common knowledge'
version: 1
form: formal-application
grounds:
- THEORY-tmp4cr0g
concludes:
- CLAIM-tmpyp3u3
tags:
- epistemology
- logic
date: '2026-11-12'
line:
- record-as-apparatus
- distributed-agency
summary: >-
  From the exchange "luria experiment design" (2026-11-10), A32 §1:
  "publishing a record does not establish common knowledge", with Halpern
  and Moses cited for the distinction. The inference from THEORY-tmp4cr0g, the reading of
  LIT-1213 in NOTE-1381, to the fourth row of CLAIM-tmpyp3u3. Proposed. The
  theorems apply once reading the record is modelled as receiving a
  message whose time of arrival is uncertain and unacknowledged, which is
  how the record is read; a record that every collaborator reads at a
  shared clock tick is outside it. First filed on LIT-1213 alone; moved to
  the THEORY, filed the same day at the owner's acceptance of the filer's
  ideas, so that the ground is a reading. The citation is A's (ChatGPT's); the wording is the assistant's
  (Claude, in this session), and adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpyp3u3 — filed from the same exchange, Proposed; the claim this argument concludes -->
<!-- inactive-ok-file: THEORY-tmp4cr0g — Proposed, filed the same day; the reading this argument starts from -->

# ARG-tmpbuocw: Halpern and Moses's result on unreliable channels applies to a record read asynchronously: publishing a standing does not make it common knowledge

## The inference

1. THEORY-tmp4cr0g, from NOTE-1381's reading of LIT-1213: over a channel
   whose deliveries are not guaranteed, no fact becomes common knowledge
   that was not common knowledge at the start (Theorem 5), and the same
   holds when start and delivery times are uncertain, even if every
   message arrives (Theorem 8). NOTE-1381 followed both proofs.
2. A collaborator learns the record's current standing by reading it: a
   pull or a fresh session that happens at a time no one else observes,
   with no acknowledgement written back. A32: an agent "could have an
   outdated checkout, miss a notification, misunderstand a status, or fail
   to inspect a relevant objection".
3. So, between collaborators, the record's standing travels over a channel
   of the kind in 1: delivered, if at all, at uncertain and unobserved
   times.
4. So publishing a standing in the record does not make it common
   knowledge among the collaborators that the record endorses it, which is
   the fourth row of CLAIM-tmpyp3u3.

## Critical questions

- **Does the theorem's premise hold of the case?** Theorems 5 and 8
  concern messages between processors that may be lost or whose timing is
  uncertain. A collaborator who reads the record at a time fixed in advance
  and known to all, against a shared clock, is outside them: the paper's
  timestamped common knowledge (Theorem 12, a statement NOTE-1381 did not
  check) is how such a team would get the eventual form. The
  record imposes no such reading schedule, and its sessions start when
  they start. Where a team does impose one, step 3 fails and the
  conclusion does not follow for that team.
- **Is the application exact or by analogy?** Exact for the model in step
  2, where reading is receiving a message. Whether any actual team reads
  that way is an empirical fact about the team, not about the record,
  which is why the claim speaks of what the record represents by itself.
- **Does the conclusion overreach?** It says common knowledge is not
  established, not that coordination fails. NOTE-1381 itself separates
  the impossibility of guaranteed simultaneous action from weaker
  coordination that remains possible.
- **Is the ground a reading?** Yes, since THEORY-tmp4cr0g. Its title
  is limited to the theorems NOTE-1381 checked; the claim needs no more
  than Theorem 8, which holds even if no reading is ever missed: uncertain
  timing suffices.
