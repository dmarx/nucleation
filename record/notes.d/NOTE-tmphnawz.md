---
status: Read
paper: LIT-tmpo6res
title: 'Hong Kong Monetary Authority (2026) — Discussion Paper on Agentic A.I. Governance in the Banking Sector'
version: 1
history:
- version: 1
  date: '2026-11-16'
  note: >-
    Read on 2026-11-16 from the exchange "Assess Depp Heard Abuse", by a
    delegated reader whose draft the filer verified. Copy: the HKMA's own
    PDF, https://www.hkma.gov.hk/media/eng/doc/key-information/press-release/2026/20261102e3a1.pdf
    (57 pages, cover dated November 2026, file created 2 November 2026).
    Read in full: chapters 1–7 (executive summary, introduction,
    definition, risks, intent-anchored accountability, lifecycle, harness,
    oversight and intervention, traceability) and section 8.1
    (materiality). Skimmed: 8.2–8.4 (Registry notification), 9 (external
    agents, Know Your Agent) and 10 (way forward).
date: '2026-11-16'
summary: >-
  A non-binding discussion paper. The HKMA proposes that an agentic AI
  deployment act only for an approved business intent, within delegated
  authority that is defined in advance and technically enforced through an
  "agent harness" (permissions, deterministic checks, transaction and
  velocity limits, approval gates). Accountability stays with a named owner.
  Human oversight counts only where it is effective: a formal approval step
  is not oversight when volume or velocity outruns review, and intervention
  must be designed around detection, decision and stopping time, so that it
  comes before harm becomes irreversible. Where oversight cannot keep pace,
  the agent's authority, scope or velocity should be reduced.
---
<!-- inactive-ok-file: CLAIM-tmpfmmkt CLAIM-tmpkx7ct CLAIM-tmpuiaop CLAIM-tmpwpvbz TERM-tmp91lqy — Proposed or Deferred; filed from the exchange "Assess Depp Heard Abuse" or its readings, cited with its standing -->
# NOTE-tmphnawz: Hong Kong Monetary Authority (2026) — Discussion Paper on Agentic A.I. Governance in the Banking Sector

## Contribution

A regulator's proposal for governing AI agents that act through tools in
banks, anchored in an approved business intent ("intent-anchored
accountability"). It does three things the record can use. It makes
effectiveness, not the presence of a human step, the test of oversight. It
sets the speed at which an agent may act by what oversight can handle,
through velocity limits. And it locates intervention in time: intervention
points come before consequential actions take effect, designed around
detection, decision and stopping time.

## Key results

1. §4.1, p. 16: oversight "is not established merely by adding a formal
   approval" step. Where agents act at machine speed, institutions may need
   to define in advance permitted actions, limits, thresholds "and the
   maximum velocity at which / oversight and intervention arrangements can
   remain effective."
2. §4.3, pp. 18–19, speed and scale: "Numerous individually minor actions may
   cause serious harm before / review catches up". Hence the "need for
   velocity limits that are commensurate" not only with technical capacity
   but "with the demonstrated effectiveness of oversight", and, where
   stress tests fail, "the deployment’s / authority, scope or velocity may
   need to be constrained."
3. §4.3, p. 18, compounding errors: "The last opportunity for human
   intervention may occur" several steps before harm is visible.
4. §4.4, p. 20, approval fatigue: a perfunctory approval "creates a practical
   limit on the speed and volume at which an agent can" operate safely.
   Irreversibility: "An agent may complete an irreversible action before
   anyone notices". Contextual failures: an action within authority and
   rules may still be inappropriate, so transaction-specific validation may
   be needed.
5. §3.2, p. 13, drift: "A deployment may also move along this spectrum without
   a deliberate decision." Authority creep (§4.4, p. 20) is the same risk at
   the level of permissions.
6. §7.1, p. 35, the harness: boundaries "should be defined in advance,
   technically enforced and changed only through the AI’s" change
   management, translated into "practical, testable and enforceable
   operating constraints." The agent may not alter its own boundaries
   unless the institution has explicitly approved an arrangement for it (p. 36).
   A failed deterministic check "should be prevented, escalated or routed
   for human review." (p. 36).
7. §7.2, p. 37, three forms of oversight: in the loop, on the loop, and
   "human-in-command arrangements, under which identified persons retain
   authority to / define, change, restrict, suspend or withdraw the
   deployment’s mandate and operating" boundaries. "A formal approval step
   is not, by itself, meaningful human oversight." Approval is meaningful
   only where the approver sees the substance, can reject, "regards
   rejection as a legitimate outcome", and has time.
8. §7.2, p. 37, timing: intervention design "should take account of detection
   time, decision time and stopping time, so that / intervention can occur
   before harm arises or becomes irreversible." Intervention measures
   include "reducing transaction, exposure, operational or velocity
   limits;", restricting tools, pausing (a "kill switch") and fallback.
9. §7.2, p. 38, the test in substance: "If an AI cannot stop or materially
   constrain a" deployment without unacceptable disruption, the principle
   is not met, "regardless of / how effective the mechanism appears on
   paper."
10. §8.1, p. 43, materiality: genuine per-action approval can make a
   deployment non-material unless the action is irreversible, because "a
   failed gate on a reversible action still / allows correction, but a
   failed gate on an irreversible action does not." Payment finality is the
   standard example.
11. Status, §2.3, p. 11: "This Discussion Paper presents preliminary views and
   invites comment." It "creates no new obligations".

## Assumptions

That an institution can say in advance what an agent is for (the business
intent) and turn its risk appetite into enforceable, testable limits. That
accountability can be kept with named people however many vendors and
components are involved. That effective oversight can be shown by testing
and rehearsal at stressed volumes. Evidence is admitted to be thin:
deployment "is still at an early stage and practical evidence remains
limited" (§4.1).

## Concepts

Agentic AI (acts through tools, chooses its steps); intent-anchored
accountability; agent harness; deterministic validation checks; velocity
limits; human-in-the-loop, on-the-loop and in-command; approval fatigue;
authority creep; stop mechanism ("kill switch") and fallback; detection,
decision and stopping time; irreversibility and payment finality;
materiality; Registry of material agents; Know Your Agent.

## Bearing on the record

- **CLAIM-tmpwpvbz**: the paper is where the exchange found this objection's
  architecture: A23 §3 cites it, and A33 and A35 develop it. It specifies
  standing limits set in advance and technically enforced (result 6), fast
  actuators with tested stopping time (results 8 and 9), and revision kept
  with people in command (result 7). It also confirms the objection's own
  caveats: rules cannot catch contextual failures (result 4), and
  boundaries drift (result 5). It does not say that standing limits make
  friction unnecessary. Its answer to speed is to slow the agent to what
  oversight can handle (results 1 and 2) and to keep approval gates for
  consequential actions. Not an independent corroboration; a documentary
  source for the claim's architecture.
- **TERM-tmp91lqy**: the harness is the term's "friction without delay": the
  agent cannot pass a deterministic check or change its limits; the
  institution's change control and independent control owner hold them.
  Result 7 adds a case the term does not separate out: an approval step on
  which the process waits but which is perfunctory. That is friction by
  dependence that opens no real opportunity to intervene. Dependence is
  necessary for an opportunity on the term's reading, not sufficient.
- **CLAIM-tmpuiaop**: partly supports the "exposes" reading. Velocity limits
  deliberately restore delay so that review can keep up, and the
  perfunctory-approval case shows friction can be present while the
  opportunity is not.
- **CLAIM-tmpkx7ct**: who counts as the "executor" matters. The limits bind
  the agent, but the deploying institution sets and enforces them (with an
  independent control owner, and the HKMA's own suspension powers above it).
  If the executor is the institution, this is the defeater's case of a
  limit the executor controls. If it is the agent, the reply holds.
- **CLAIM-tmpfmmkt**: a regulator's qualitative statement of its point. When
  actions outrun review, the formal approval step stays and its effect does
  not (results 4 and 7). No arithmetic.
- **QUESTION-tmp9n1ac**: an answer from another domain. Put the stopping
  points before consequential actions take effect, and set the rate of
  action by the demonstrated capacity of review (results 2 and 8).
- **CLAIM-464**: result 10 is its logic in miniature: an irreversible action
  removes the correction a failed gate would have allowed.

## Limitations

A discussion paper. It presents preliminary views, invites comment, and
creates no obligations. It is a design proposal, not evidence that the
controls work; the HKMA says practical evidence is limited. Its scope is
banking agents under one supervisor. The A.I.-versus-A.I. oversight it
floats is only mentioned.
