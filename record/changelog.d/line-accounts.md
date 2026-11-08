### Added

- [ADR-tmpyihxy](record/decisions.d/ADR-tmpyihxy.md) (Proposed, version 2): an account the record holds only in parts, for a line or a part of one, gets an unadmitted SYNTHESIS that restates it, giving the account an address.
  - An unadmitted account adds nothing, has no admission route and cannot be set Current.
  - There is one account per scope, and a line's synthesis may be built over its parts' syntheses.
  - A line whose parts barely relate is reported as a candidate to split.
  - `docs/current-account.md` lists unadmitted accounts last, under "Accounts held in parts".
- [ADR-tmpyb8vm](record/decisions.d/ADR-tmpyb8vm.md) (Proposed): the nucleating-argument line is split in three, on the relations among its parts' components. Two lines are added, `records-of-inquiry` and `record-as-apparatus`, and 43 entries move to them, each with a history note. Five of them keep nucleating-argument beside the new line, because they answer, refine or object to one of its entries (version 2): [CLAIM-178](record/claims.d/CLAIM-178.md), [CLAIM-183](record/claims.d/CLAIM-183.md), [CLAIM-189](record/claims.d/CLAIM-189.md), [CLAIM-181](record/claims.d/CLAIM-181.md) and [QUESTION-108](record/questions.d/QUESTION-108.md).
- The demonstration, six syntheses:
  - **nucleating-argument:**
    - [SYNTHESIS-tmpllsy7](record/syntheses.d/SYNTHESIS-tmpllsy7.md), its synthesis over its three parts, admitted by derivation: when filing costs at least twice a reconstruction's overpayment, the break-even filing rule and the drift-catching second-occurrence rule part, and the competitive guarantee prices none of the drift between them;
    - three unadmitted part accounts: drift ([SYNTHESIS-tmp7nvem](record/syntheses.d/SYNTHESIS-tmp7nvem.md)), anchors ([SYNTHESIS-tmp5p7lm](record/syntheses.d/SYNTHESIS-tmp5p7lm.md)) and the costs of anchoring ([SYNTHESIS-tmp9cgig](record/syntheses.d/SYNTHESIS-tmp9cgig.md)).
  - **records-of-inquiry:** an unadmitted account, [SYNTHESIS-tmpnakke](record/syntheses.d/SYNTHESIS-tmpnakke.md).
  - **record-as-apparatus:** an unadmitted account, [SYNTHESIS-tmp4csi2](record/syntheses.d/SYNTHESIS-tmp4csi2.md).
- `scratch/formal/line_parts.py` counts the relations among a line's parts.

### Changed

- The `synthesis-review` skill:
  - files or revises an unadmitted account when an opportunity fails only because the record already holds it;
  - builds a line's synthesis over its parts;
  - reports lines whose parts barely relate.

  Readers' briefs now state the tests neutrally.
- The current-account template cites [ADR-075](record/decisions.d/ADR-075.md) by number.
