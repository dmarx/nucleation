### Added

- ADR-tmpyihxy (Proposed, version 2): an account the record holds only in parts, for a line or a part of one, gets an unadmitted SYNTHESIS that restates it, giving the account an address.
  - An unadmitted account adds nothing, has no admission route and cannot be set Current.
  - There is one account per scope, and a line's synthesis may be built over its parts' syntheses.
  - A line whose parts barely relate is reported as a candidate to split.
  - `docs/current-account.md` lists unadmitted accounts last, under "Accounts held in parts".
- ADR-tmpyb8vm (Proposed): the nucleating-argument line is split in three, on the relations among its parts' components. Two lines are added, `records-of-inquiry` and `record-as-apparatus`, and 43 entries move to them, each with a history note.
- The demonstration, six syntheses:
  - **nucleating-argument:**
    - SYNTHESIS-tmpllsy7, its synthesis over its three parts, admitted by derivation: when filing costs at least twice a reconstruction's overpayment, the break-even filing rule and the drift-catching second-occurrence rule part, and the competitive guarantee prices none of the drift between them;
    - three unadmitted part accounts: drift (SYNTHESIS-tmp7nvem), anchors (SYNTHESIS-tmp5p7lm) and the costs of anchoring (SYNTHESIS-tmp9cgig).
  - **records-of-inquiry:** an unadmitted account, SYNTHESIS-tmpnakke.
  - **record-as-apparatus:** an unadmitted account, SYNTHESIS-tmp4csi2.
- `scratch/formal/line_parts.py` counts the relations among a line's parts.

### Changed

- The `synthesis-review` skill:
  - files or revises an unadmitted account when an opportunity fails only because the record already holds it;
  - builds a line's synthesis over its parts;
  - reports lines whose parts barely relate.

  Readers' briefs now state the tests neutrally.
- The current-account template cites ADR-075 by number.
