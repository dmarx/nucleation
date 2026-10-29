---
status: Read
paper: 'LIT-1226'
title: 'Rose et al. — Zero trust architecture (NIST SP 800-207)'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in full on 2026-10-29 from NIST's own PDF
    (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207.pdf,
    59 pages, dated August 2020, the copy doi:10.6028/NIST.SP.800-207
    resolves to); text extracted with pdftotext. Read: the front matter,
    §§1–7 and Appendix B. Figures 1–12 are diagrams and were read from
    their captions and the text. Not read: the reference list and
    Appendix A (acronyms). It is a guideline with no data; nothing to
    recompute. The section numbering of Appendix B was checked against
    the table of contents.
date: '2026-10-29'
summary: >-
  NIST's abstract definition of zero trust: no implicit trust from network
  location or ownership, access to each resource granted per session by
  a policy engine and administrator and enforced at a policy enforcement
  point, on dynamic policy fed by asset state, identity, behaviour and
  threat intelligence. Seven tenets, three approaches, four deployment
  models, five use cases, seven threats and a migration path; its own
  survey judged the ecosystem not yet mature enough for widespread
  adoption.
---
<!-- inactive-ok-file: CLAIM-359 — Proposed; the claim this reading bears on, cited as open -->
<!-- inactive-ok-file: LIT-1206 — Deferred, read only in part; cited for the two controls that part covers -->


# NOTE-tmpd81mn: Rose et al. — Zero trust architecture (NIST SP 800-207)

## Contribution

It gives US federal agencies a vendor-neutral vocabulary for zero trust:
what the term means, which logical components an architecture has, how
they can be deployed, what new threats they bring, and how to migrate
from a perimeter network. It states the idea as tenets rather than as a
product, and says outright that zero trust "is not a single architecture
but a set of guiding principles".

## Key insight

Shrink the zone of implicit trust to the resource. In the document's
airport analogy, everything past the security checkpoint is trusted
alike; zero trust moves checkpoints next to each gate and checks every
boarding. Trust is then a per-request judgment by a policy engine that
"assume[s] an attacker is present", not a status a subject earns by
being inside.

## Assumptions

- The enterprise knows its assets, subjects, data flows and business
  processes; without that inventory "the PE denies requests due to
  insufficient information" (§7.3).
- It can observe all traffic, at least as metadata (§3.4.1).
- Identity, credential and access management and continuous diagnostics
  exist; ZTA rests on them (§§6.3, 6.6).
- The tenets apply to work within or between enterprises, "not to
  anonymous public or consumer-facing business processes" (§2.1).

## Key results

- **Definition (§2).** ZT "provides a collection of concepts and ideas
  designed to minimize uncertainty in enforcing accurate, least
  privilege per-request access decisions in information systems and
  services in the face of a network viewed as compromised".
- **Seven tenets (§2.1).** All data sources and services are resources;
  all communication is secured regardless of location; access is per
  session with least privilege; access is set by dynamic policy over
  identity, asset state and behaviour; the enterprise monitors the
  integrity of every asset and none is inherently trusted;
  authentication and authorization are dynamic and enforced before
  access; and the enterprise collects as much state as it can to
  improve policy.
- **Components (§3).** Policy engine (decides, logs), policy
  administrator (opens and closes paths), policy enforcement point
  (gates the session), fed by CDM, compliance, threat intelligence,
  activity logs, access policy, PKI, identity management and SIEM.
  Control plane separate from data plane.
- **Approaches and deployments (§§3.1–3.2).** Identity governance,
  micro-segmentation, software-defined perimeters; agent/gateway,
  enclave, resource portal and application sandbox models.
- **Trust algorithm (§3.3).** Criteria-based or score-based; singular or
  contextual. Contextual, which uses the subject's history, is
  preferred because it can catch "an attacker using subverted
  credentials ... in a pattern that is atypical" — an HR account
  reading 100 records in a day against a usual 20 to 30.
- **Threats (§5).** Subversion of the decision process by anyone "with
  configuration access to the PE's rules"; denial of service against
  the PE/PA; stolen credentials and insiders, which ZTA confines to
  their account's purview but does not stop within it; limited
  visibility into encrypted traffic; the stored monitoring data and
  policy store as reconnaissance targets; vendor lock-in; and
  non-person entities (AI agents) administering policy, which an
  attacker may "induce or coerce" to act for it.
- **Maturity (Appendix B).** "The current state of the ZTA ecosystem is
  not mature enough for widespread adoption"; no vendor supplies every
  component, interfaces are proprietary, and attacker response, user
  experience and resilience are open research.

## Claims

| id | claim | strength | support |
|---|---|---|---|
| C1 | Removing implicit trust from network location limits lateral movement after a breach | moderate | argued from the design; no measurement |
| C2 | A contextual trust algorithm is more likely than a singular one to catch misuse of valid credentials | weak | worked examples, no evaluation |
| C3 | ZTA concentrates risk in the policy engine and administrator | moderate | §5.1–5.2, follows from the design |
| C4 | The vendor ecosystem in 2020 could not supply a complete ZTA | moderate | NIST's technology survey, Appendix B, method not described |

## Concepts

- **Zero trust / zero trust architecture / zero trust enterprise**: the
  principles, the enterprise's plan using them, and the infrastructure
  and policies that result (§2).
- **Implicit trust zone**: the area past the last PDP/PEP in which all
  entities share one level of trust.
- **Policy decision point**: the policy engine and policy administrator
  together.
- **Trust algorithm**: the policy engine's process for granting or
  denying a request.
- **Non-person entity**: software agents, AI among them, acting as
  subjects or administrators.

## Connections

It descends, by its own history (§1.1), from DISA's "black core" and the
Jericho Forum's de-perimeterization (2004), named "zero trust" by John
Kindervag at Forrester. It builds on SP 800-53's least privilege and
separation of duties (LIT-1206, NOTE-tmpgdnkh) and on SP 800-63's identity
assurance levels.

## Bearing on the record

- **CLAIM-359.** A41 cited zero trust as governance that does not assume
  any constituent is sound. The document bears that out for subjects
  and devices and then shows where the assumption stops: the policy
  engine and administrator are trusted absolutely, and the document's
  only answer to their subversion is that they "must be properly
  configured and monitored, and any configuration changes must be
  logged and subject to audit" (§5.1). That is the claim's thesis that
  robustness lives in the processes that allocate and audit authority:
  zero trust relocates trust to the authority-allocating process and
  makes that process the target. Two further points bear on the claim's
  trade-off. Contextual trust algorithms, which flag deviation from a
  subject's usual pattern, treat an unusual but legitimate act as
  suspect, and the document's remedy is a "tuning" phase and lenient
  "reporting-only" operation (§§3.3.1, 7.3.6), which is the claim's
  cost of safeguards to disagreement in operational form. And §5.7
  names AI agents with weaker authentication as a route by which an
  attacker can borrow privilege, an instance of authority capture
  through a constituent.
- **CASE-108.** The case's "reliability-weighted influence" arm, with its
  failure "self-reinforcing capture or unfair suppression", is close to
  a score-based contextual trust algorithm, whose confidence rises with
  a history of normal behaviour. The document does not consider that
  such a score can be farmed.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- It is a guideline: no deployment is evaluated and no effect measured.
  The technology survey in Appendix B is reported without method or
  participants.
- It treats insiders with valid credentials as largely outside its
  reach: "an attacker with valid credentials (or a malicious insider)
  may still be able to access resources for which the account has been
  granted access" (§5.3).
- **Errors and slips.** Appendix B's numbering skips: B.3 is followed by
  B.3.3 and B.3.4 with no B.3.1 or B.3.2, and B.4 by B.4.5 to B.4.7. The
  policy administrator "would generate any session-specific
  authentication and authentication token" (§3) repeats a word where
  "authorization" is probably meant. "[SP8900-160v1]" (§7.1) is a typo
  for SP 800-160v1, and "Significate changes" (§7.3.7) for
  "significant".

## Open questions

- How should the policy engine itself be governed, and by whom, when
  it is the one component everything trusts?
- Does a contextual trust score reward an insider who behaves normally
  for long enough, and how would one test that?
