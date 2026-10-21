### Changed

- [ADR-049](record/decisions.d/ADR-049.md) v2: how an Answered question is cited. An Open question may
  cite one, with an `inactive-ok` annotation; this is usually a parent
  citing its split-off child. Anywhere else, cite the CLAIM or THEORY
  that answers it. luria cannot allow the first case by configuration,
  because `active:` names one status word.

### Fixed

- The thirteen split parents acknowledge their Answered children.
  [THEORY-239](record/theory.d/THEORY-239.md)'s Connections bullet cites [QUESTION-052](record/questions.d/QUESTION-052.md) and its
  co-answerers instead of the Answered child. [QUESTION-241](record/questions.d/QUESTION-241.md) no longer
  cites [QUESTION-239](record/questions.d/QUESTION-239.md), and names [CLAIM-340](record/claims.d/CLAIM-340.md) alone.
