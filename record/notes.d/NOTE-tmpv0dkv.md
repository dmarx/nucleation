---
status: Skimmed
paper: 'LIT-2696'
title: 'Hong Kong Monetary Authority — Discussion Paper on Agentic A.I. Governance in the Banking Sector'
version: 1
history:
- version: 1
  date: '2026-11-18'
  note: >-
    Read in part on 2026-11-17 from the HKMA's own PDF,
    https://www.hkma.gov.hk/media/eng/doc/key-information/press-release/2026/20261102e3a1.pdf,
    57 pages, text by pdftotext; page numbers are the paper's. The first
    fetch was cut off by a connection reset (a transport failure, not a
    refusal); one retry succeeded. Read: §1 Executive Summary (pp. 4–9),
    §2 Introduction (pp. 10–11), §4.2–4.4 on risks (pp. 16–19), §5.4–5.5
    with questions 5A–5D (pp. 27–29), the end of §7.1, §7.2 on human
    oversight and the start of §7.3 (pp. 36–38). Not read: §3, §5.1–5.3,
    §6, the rest of §7.3, §§8–10. About 40% of the paper; hence Skimmed.
    The quotes below were rechecked by the filer against the same copy on
    2026-11-18.
date: '2026-11-18'
summary: >-
  The HKMA's preliminary, non-binding thinking on agentic A.I. at banks.
  Its organizing idea is "intent-anchored accountability": an agent acts
  only for an approved business intent within delegated authority, and
  accountability stays with named human owners and cannot pass to vendors
  or customers. A formal approval step is not meaningful oversight unless
  the approver sees the substance, can reject, treats rejection as
  legitimate and has time; velocity is to be limited by what oversight can
  review; a tested stop mechanism, logs, a registry and customer access to
  human review are proposed. "AIs" in the paper means Authorized
  Institutions (banks).
---
<!-- inactive-ok-file: CLAIM-tmp238zy CLAIM-707 CLAIM-tmpgh3v2 CLAIM-tmpohafo — Proposed; cited with their standing, entries this reading bears on or files -->

# NOTE-tmpv0dkv: Hong Kong Monetary Authority — Discussion Paper on Agentic A.I. Governance in the Banking Sector

## Contribution

A regulator's framework that keeps accountability fixed on the human
owners of an agent's mandate while granting that per-action human approval
can be a formality. It defines when approval is meaningful and treats the
capacity of oversight as a limit on how fast and far an agent may act.

## Key insight

The control that counts is authority over the mandate, kept by named
people and backed by a stop that works, not a signature on each output.

## Assumptions

- Accountability can and should stay with identified people as action is
  delegated to software.
- Controls enforced outside the model (the "agent harness") are more
  reliable than instructions to it.
- Governance intensity tracks materiality, autonomy, access, impact and
  reversibility (p. 4).
- Status (p. 9, p. 11): the paper "does not itself introduce binding
  supervisory requirements" and "is not a statement of supervisory
  expectations".

## Key results

- **Principle** (p. 5): "The Discussion Paper is centred on intent-anchored
  accountability."
- **In command** (p. 7): "human-in-command arrangements, under which
  identified persons retain authority to define, change, restrict,
  suspend or withdraw the deployment's mandate and operating boundaries."
- **Approval is not oversight** (p. 37): "A formal approval step is not,
  by itself, meaningful human oversight. Approval is meaningful only where
  the approver sees the substance of the action, has the authority and
  practical ability to challenge or reject it, regards rejection as a
  legitimate outcome, and has sufficient time to make an informed decision
  before the action takes effect."
- **Volume** (p. 37): "Where the volume, complexity or velocity of actions
  exceeds the reviewer's ability to assess them meaningfully, the AI
  should not regard the formal existence of an approval step as an
  effective control."
- **Speed against review** (p. 18): "Numerous individually minor actions
  may cause serious harm before review catches up"; "The last opportunity
  for human intervention may occur several steps before the harm becomes
  visible."
- **Velocity limited by oversight** (p. 19): "AIs may therefore need to
  consider the need for velocity limits that are commensurate not only
  with technical constraints, but also with the demonstrated effectiveness
  of oversight arrangements."
- **Timing** (p. 37): "Their design should take account of detection time,
  decision time and stopping time, so that intervention can occur before
  harm arises or becomes irreversible."
- **Stop in substance** (p. 38): "If an AI cannot stop or materially
  constrain a deployment without unacceptable disruption, the principle is
  not met in substance, regardless of how effective the mechanism appears
  on paper."
- **Reserved decisions** (p. 36): "Where applicable law, regulation, or
  internal policy reserves a decision for a person, an agentic A.I. system
  may inform but should not make that decision."
- **Accountability stays** (p. 27): "Second, the AI's accountability for
  its own deployment cannot be passed to customers."; "A move from
  individual human approval towards monitoring-based oversight should not
  reduce the AI's accountability."
- **Customers** (p. 27): "They should be able to request human review of a
  material action, outcome or decision, as appropriate to the use case."
- **Logs** (p. 38): "When software acts, the log replaces the memory and
  signature of a human actor."

## Concepts

Agentic A.I.; intent-anchored accountability; accountable, business,
technical and control owners; risk-integrated agent harness; velocity
limits; human-in-the-loop, on-the-loop and in-command; meaningful human
oversight; stop mechanism ("kill switch"); Registry of material A.I.
agents; Know Your Agent; risk Bands A–C.

## Bearing on the record

- **[CLAIM-tmpgh3v2](../claims.d/CLAIM-tmpgh3v2.md)** (a slow governing level over a fast process).
  Corroborates both halves. The harm: minor actions "may cause serious
  harm before review catches up", and the last chance to intervene "may
  occur several steps before the harm becomes visible". The remedy: limits
  set beforehand in the harness, velocity tied to "the demonstrated
  effectiveness of oversight arrangements", and in-command authority to
  "define, change, restrict, suspend or withdraw" the mandate. It is
  guidance, not evidence that the remedy works.
- **[CLAIM-tmp238zy](../claims.d/CLAIM-tmp238zy.md)** (friction that makes people think differs from
  friction that makes the institution answerable). Corroborates. Approval
  is meaningful only where the approver "has the authority and practical
  ability to challenge or reject it" and "regards rejection as a legitimate
  outcome": a regulator separating scrutiny from authority to act on it.
- **[CLAIM-410](../claims.d/CLAIM-410.md)**. Related, not filed as a relation: the paper splits
  execution (delegated to the agent) from rule-setting and revision (kept
  by named owners), and forbids accountability passing to vendors or
  customers.
- **[CLAIM-tmpohafo](../claims.d/CLAIM-tmpohafo.md)**. Customers get access to a person and review on
  request, but no power to suspend an agent's action: review without
  interruption.
- **[CLAIM-707](../claims.d/CLAIM-707.md)**. The rule that accountability stays with owners is an
  institutional guard against control and blame coming apart.
- **[LIT-2705](../literature.d/LIT-2705.md)** (meaningful human control) and **[LIT-2665](../literature.d/LIT-2665.md)** (moral
  crumple zones) are the held literature closest to §7.2.

## Verdict on the exchange's characterization

Faithful: A23 says only that the HKMA published a discussion paper on
agentic AI in banking. The LIT's gloss, control over outputs against
control over the process, is faithful in substance, not in wording: the
paper contrasts per-action approval with authority over the mandate.

## Limitations

A non-binding discussion paper, about 40% read. No evidence of
effectiveness. Its accountability is the bank's to the regulator and to
customers; affected customers get disclosure, human contact, review on
request and existing redress, not a right to suspend.
