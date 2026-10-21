### Added

- [ADR-049](record/decisions.d/ADR-049.md): a QUESTION is Answered when Active CLAIMs or THEORYs answer it
  as posed and in full scope. An Active THEORY counts, so a CLAIM is not
  filed only to restate a reading. A partly answered question is split:
  the answered part becomes a child QUESTION that refines the parent and
  is marked Answered, and the parent is reworded to what is left and stays
  Open.

### Changed

- The Answered status blurb in `luria.yaml` now says "an Active CLAIM or
  THEORY" and cites [ADR-049](record/decisions.d/ADR-049.md).
