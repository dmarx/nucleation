---
status: Proposed
title: 'Halpern and Moses''s result on unreliable channels applies to a record read asynchronously: publishing a standing does not make it common knowledge'
version: 1
form: formal-application
grounds:
- LIT-1213
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
  and Moses cited for the distinction. The inference from LIT-1213, as
  NOTE-1381 reads it, to the fourth row of CLAIM-tmpyp3u3. Proposed. The
  theorems apply once reading the record is modelled as receiving a
  message whose time of arrival is unbounded and unacknowledged, which is
  how the record is read; a record that every collaborator reads at a
  shared clock tick is outside it. LIT-1213 is a work cited, read in
  NOTE-1381, with no THEORY of its own yet, so the ground is the weakest
  kind. The citation is A's (ChatGPT's); the wording is the assistant's
  (Claude, in this session), and adopting it is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpyp3u3 — filed from the same exchange, Proposed; the claim this argument concludes -->

# ARG-tmpbuocw: Halpern and Moses's result on unreliable channels applies to a record read asynchronously: publishing a standing does not make it common knowledge

## The inference

1. NOTE-1381, reading LIT-1213: over a channel whose deliveries are not
   guaranteed, no fact becomes common knowledge that was not common
   knowledge at the start (Theorem 5); the same holds when delivery is
   guaranteed but its time is unbounded (Theorem 7); and asynchronous
   channels cannot give ε-common knowledge (Theorem 11).
2. A collaborator learns the record's current standing by reading it: a
   pull or a fresh session that happens at a time no one else observes,
   with no acknowledgement written back. A32: an agent "could have an
   outdated checkout, miss a notification, misunderstand a status, or fail
   to inspect a relevant objection".
3. So, between collaborators, the record's standing travels over a channel
   of the kind in 1: delivered, if at all, at unbounded and unobserved
   times.
4. So publishing a standing in the record does not make it common
   knowledge among the collaborators that the record endorses it, which is
   the fourth row of CLAIM-tmpyp3u3.

## Critical questions

- **Does the theorem's premise hold of the case?** Theorems 5 and 7
  concern messages between processors with no shared clock or bounded
  delay. A collaborator who reads the record at a time fixed in advance
  and known to all, against a shared clock, is outside them: Theorem 12
  gives eventual common knowledge if every clock reaches the time. The
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
- **Is LIT-1213 enough as a ground?** It is a work cited, though read in
  NOTE-1381. A THEORY drawn from that reading would be the stronger
  footing; until one is filed, the ground is NOTE-1381's statement of the
  theorems.
