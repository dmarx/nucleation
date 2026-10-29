---
status: Skimmed
paper: 'LIT-1206'
title: 'Joint Task Force — NIST SP 800-53 Revision 5'
version: 1
history:
- version: 1
  date: '2026-10-29'
  note: >-
    Read in part on 2026-10-29 from NIST's own PDF
    (https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf,
    492 pages, "September 2020 / includes updates as of 12-10-2020");
    text extracted with pdftotext. Read: the abstract, the errata page,
    Chapter One (introduction) and Chapter Two (fundamentals) in full;
    from the Chapter Three catalogue, AC-3(2), AC-5, AC-6 with its ten
    enhancements, AC-7, AU-9 with enhancements (1), (2) and (5), CM-5(4),
    MP-6(7) and PM-12. Not read: the rest of the roughly 450 pages of
    controls, the references, glossary, acronyms and the control summary
    tables of Appendix C, except as a search index. A catalogue is not
    read for an argument, so this is a skim by design.
date: '2026-10-29'
summary: >-
  A catalogue of security and privacy controls in 20 families, each a
  control statement with organization-defined parameters, a discussion,
  related controls and enhancements, chosen by a separate risk process.
  The controls the record cites, separation of duties (AC-5), least
  privilege (AC-6) and dual authorization, are short, parameterized and
  name collusion as the residual risk.
---
<!-- inactive-ok-file: CLAIM-359 — Proposed; the claim this reading bears on, cited as open -->
<!-- inactive-ok-file: LIT-1216 — Deferred, read only in part; cited for its mapping to these controls -->

# NOTE-tmpgdnkh: Joint Task Force — NIST SP 800-53 Revision 5

## Contribution

A consolidated, outcome-neutral catalogue of safeguards for any system
that processes information, mandatory for US federal systems under FISMA
and OMB A-130 and offered to others. It holds security and privacy
controls in one catalogue of 20 families, 17 aligned with FIPS 200's
minimum requirements and three (Program Management, PII Processing and
Transparency, Supply Chain Risk Management) for later federal mandates,
and keeps the catalogue separate from the process that selects controls
(§§1.1, 2.2).

## Key insight

A control is a template, not a rule: "[Assignment: organization-defined
...]" and "[Selection: ...]" slots are filled by the adopting
organization's risk process, and "an inheriting entity cannot assume
that controls are the same ... just because the control identifiers ...
are the same" (§2.3). The catalogue says what kinds of safeguard exist;
it does not say how much of each an organization needs.

## Key results

From the parts read.

- **AC-5, separation of duties.** "Identify and document [duties of
  individuals requiring separation]; and define system access
  authorizations to support separation of duties." Discussion: it
  "addresses the potential for abuse of authorized privileges and helps
  to reduce the risk of malevolent activity without collusion", and
  includes "ensuring that security personnel who administer access
  control functions do not also administer audit functions". No
  enhancements.
- **AC-6, least privilege.** "Allowing only authorized accesses ... that
  are necessary to accomplish assigned organizational tasks." Ten
  enhancements, among them separate non-privileged accounts for
  privileged users (2), periodic review of privileges (7), logging of
  privileged functions "to mitigate the risk from insider threats" (9).
- **Dual authorization.** AC-3(2), AU-9(5), CM-5(4) and MP-6(7) require
  two-person control for named actions; each discussion says "to reduce
  the risk of collusion, organizations consider rotating dual
  authorization duties".
- **AU-9(2).** Audit records stored on a physically separate system, so
  "a compromise of the system being audited does not also result in a
  compromise of the audit records".
- **PM-12, insider threat program.** A cross-discipline incident team;
  HR records are useful because some insider crimes are preceded by
  "ongoing patterns of disgruntled behavior", but their use "could
  raise significant concerns for privacy".
- **§2.3.** Common (inheritable) controls "can introduce the risk of a
  single point of failure".

## Concepts

- **Control / control enhancement**: a base safeguard and an addition
  that strengthens it; an enhancement is never selected without its
  base.
- **Organization-defined parameter**: the assignment or selection slot.
- **Assurance**: "the measure of confidence that the system
  functionality is implemented correctly, operating as intended, and
  producing the desired outcome" (§2.5).

## Connections

SP 800-207 ([LIT-1226](../literature.d/LIT-1226.md), [NOTE-tmpd81mn](NOTE-tmpd81mn.md)) builds its least-privilege,
per-request access on these controls. The CERT guide ([LIT-1216](../literature.d/LIT-1216.md),
[NOTE-tmp3wx9h](NOTE-tmp3wx9h.md)) maps each of its best practices to controls here; its
separation-of-duties practice maps to AC-5 and AC-6.

## Bearing on the record

- **[CLAIM-359](../claims.d/CLAIM-359.md).** The controls A41 read as will-organization relations
  are here in their own words, and they confirm one half of the claim
  and leave the other open. They locate robustness in how authority is
  allocated and audited: who may act, who may audit, who may change the
  configuration, and that the auditor is not the access administrator.
  They name collusion as what they do not stop, and their remedy for it
  is rotation, a further allocation process. They say nothing about the
  claim's cost to disagreement and self-revision; the only costs the
  parts read mention are availability ("when immediate responses are
  necessary") and privacy (PM-12). A reading of the catalogue would not
  find the trade-off the claim asserts stated anywhere, as far as these
  parts go.
- No instruction for machine-learning practice; nothing for the
  anthology.

## Limitations

- What was read is about a tenth of the document. Nothing here should be
  taken as a reading of any control not listed in the history.
- A catalogue gives no evidence that any control works; assessment is a
  separate publication (SP 800-53A).
- **A slip.** The dual-authorization discussions disagree on the safety
  exception: AC-3(2) says organizations "consider the risk associated
  with implementing dual authorization mechanisms when immediate
  responses are necessary", AU-9(5) that they "do not require dual
  authorization mechanisms when immediate responses are necessary".

## Open questions

- Does any control in the catalogue protect dissent, or the capacity of
  a constituent to challenge the controls themselves? The parts read do
  not; a search of the full text would settle it.
