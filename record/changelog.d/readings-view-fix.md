### Fixed

- The readings-by-line view counted no reading that a claim or argument grounds on, because it read the converse fields `supports` and `reports`, which are not stored. It now gathers those users from their own `grounds` and `reported_in`. ADR-090's figures are corrected (version 2): 406 of 856 readings in force serve a line, not 277.
