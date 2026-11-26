---
status: Open
title: "Pilot synthesis-mediated compaction on one mature argument cluster: a compact working representation of what its synthesis integrates, tested on understanding, applying, challenging and revising after a premise is withdrawn"
version: 1
history:
- version: 1
  date: '2026-11-26'
  note: >-
    Filed from A34's fifth pilot, with A33 §8 and A31 §§3 and 11, of the
    exchange "Alignment consequences brainstorm" (ChatGPT, 2026-11-26).
    The check of A31's declarations, the correction to the mediation
    ratio and the criteria are the assistant's (Claude, in this session).
stage: costed
method:
- empirical
tags:
- information-retrieval
- design-rationale
- epistemology
date: '2026-11-26'
line:
- record-as-apparatus
- nucleating-argument
advances:
- CLAIM-tmpyk9r5
presupposes:
- LEAD-tmpn6mi2
- LEAD-tmp14mq0
summary: >-
  A34: "Select a relatively mature argument cluster already represented by
  a synthesis. Construct a compact working representation, cool the
  constituent material, and retain its full justification for explicit
  recovery." It is tested against "understanding the result, applying it,
  challenging its grounds, and revising it after a premise is withdrawn",
  and followed by whether later work "increasingly uses the consolidated
  unit rather than its constituents" (A33 §8's mediation ratio). It tests
  CLAIM-tmpyk9r5 (H3) and would inform the condensed_into relation of A31
  §11 (CLAIM-tmpnf6q4). On this record
  the mediation ratio cannot be read off the relation fields, since no
  claim rests on a synthesis. The pilot is A's; the correction and
  criteria are the assistant's (Claude, in this session), and adopting
  them is the owner's call.
---
<!-- inactive-ok-file: CLAIM-tmpyk9r5 CLAIM-250 CLAIM-758 CLAIM-tmpnf6q4 — Proposed, or cited for what it holds; the hypothesis tested and the limits the test must respect, cited on 2026-11-26 -->

# LEAD-tmpd85zk: Pilot synthesis-mediated compaction on one mature argument cluster: a compact working representation of what its synthesis integrates, tested on understanding, applying, challenging and revising after a premise is withdrawn

## What A31 proposed, checked

Loaded into luria 1.11.0 with the record's `luria.yaml` as a stand-in, on
2026-11-26:

- A31 §11's `condensed_into` reference on CLAIM (to CLAIM or SYNTHESIS,
  optional, many) loads as written.
- Its companion field `condensation_scope`, declared with a `blurb` alone,
  does not load: luria refuses a field that "declares no type". Declaring it
  `many: true` (a list of the operations preserved) or giving it
  `required_when` on `condensed_into` would make it load.
- A31 §3's report of Active claims that a Current synthesis integrates
  matches none, since the record has no Current synthesis; counting
  Proposed ones it lists 451 of 474 Active claims. Integration alone does
  not pick out candidates; the cluster has to be chosen on other grounds.

## The design

1. **Choose the cluster.** A SYNTHESIS integrating at least ten components,
   most of them in LEAD-tmp14mq0's established-anchor or dormant regimes
   (stable for at least 14 days), on a line with open questions, so that
   the representation will be used.
2. **Write the capsule**: the cluster's conclusions, the conditions under
   which they stand, the codes of the premises each rests on, the open
   objections, and what would defeat each, A29's assumption-set form
   (LIT-2320). The components stay where
   they are and leave the working view (LEAD-tmpolbqp's mechanism).
3. **Test the four operations**, each on five tasks with a key written from
   the full material by someone who does not run the trial, in two arms at
   one token budget, capsule with recovery against full material:
   - *understand*: state the result and its scope;
   - *apply*: use it on a case not in the cluster;
   - *challenge*: name its weakest ground and what would defeat it;
   - *revise*: given a premise stipulated withdrawn, say which conclusions
     fall and which stand.
4. **Follow it** with LEAD-tmpn6mi2's log for a month: what later entries
   cite, the capsule or synthesis or the components.

## The mediation ratio, corrected

A33 §8 defines `M_t(C)` as new references to the abstraction over new
references to the abstraction or its constituents. In this record's
grammar a claim rests on claims only, and a SYNTHESIS asserts nothing of
its own (ADR-084), so no `rests_on` or `grounds` can point at one: counted
in relation fields the ratio is zero by construction. It has to be counted
in prose, as mentions of the synthesis's or capsule's code in new entries
against mentions of its components, from the text snapshots LEAD-tmpn6mi2
keeps; or through a CLAIM that the synthesis's audit filed for what it adds
(ADR-075), which can be rested on. A33's own caveat applies with force here:
"Agents might simply be instructed to cite the synthesis, even though they
still need the full underlying material." The read-and-file skill tells
agents to revise syntheses, so mentions of them are partly instructed.

## What would count

- **For CLAIM-tmpyk9r5 on this cluster:** the capsule arm matches the full
  arm on understanding, applying and challenging in at least 12 of 15
  tasks, and on revising names the conclusions that fall in at least 4 of
  5, at no more than half the tokens.
- **Against:** the capsule arm needs recovery of the full material on most
  revising tasks, so that no budget is freed where the fourth operation
  is concerned, which is the second limb of the claim's defeater.
- A failure on revising alone is the expected one, and is informative:
  CLAIM-664 holds that whether a dependant falls is a judgement, not a
  computation over the graph, so the capsule may need to carry more than
  the premises' codes. What it needed is what `condensation_scope` would
  have to declare.

## Risks to read against

CLAIM-758, overconsolidation: a representation that improves present use
while raising the cost of later acquisitions outside it. CLAIM-250: what
must survive is accountability, not propositions.

## Cost

Choosing the cluster and writing the capsule and the key: a day. The arms:
a few hours. The follow-up costs nothing beyond LEAD-tmpn6mi2.
