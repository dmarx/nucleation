---
status: Read
paper: LIT-tmpkmjuj
title: 'Bachas and Huberman — Complexity and ultradiffusion'
version: 1
history:
- version: 1
  date: '2026-11-21'
  note: >-
    Read on 2026-11-21 by a delegated reader, as a stand-in for Ogielski
    and Stein (LIT-tmpslg57), from SLAC-PUB-4077 on www.slac.stanford.edu
    (an institutional preprint): the abstract and §§1–3 including Theorem
    1; §§4–6 (random and unbalanced trees, temperature dependence)
    skipped. Equations partly garbled in extraction; eqs. 3.1–3.2
    reconstructed from the prose. Running notes on the branch
    claude/readers/ultrametric-ogielski. Quotations rechecked by the filer
    by script.
date: '2026-11-21'
summary: >-
  Ultradiffusion on an ultrametric tree solved as one exponential mode per
  branch point; power-law relaxation on infinite uniform trees, exponent
  ln b/(ln(1/g) − ln b) in per-pair terms, unstable when gb ≥ 1;
  exponential decay on any finite tree. Stands in for Ogielski and Stein,
  whose results it says it partly rederives.
---
<!-- inactive-ok-file: LIT-tmpslg57 CLAIM-tmp6q7ma CLAIM-tmpxi826 CLAIM-tmpy75jv — Proposed, Deferred, Unfetched or new; filed in this contribution of 2026-11-21 or the ones it builds on -->

# NOTE-tmp69i8d: Bachas and Huberman — Complexity and ultradiffusion

## Key results

1. **Lineage** (§1): Ogielski and Stein (1985) are among the first exact treatments of diffusion on a truly ultrametric space; "Some of the results of this section have already been derived in" Schreckenberg, Ogielski and Stein, Paladin and colleagues and Qiang.
2. **General solution** (§2): a walk with rates set by the height of the common ancestor relaxes as a weighted sum of exponentials, one mode per branch point.
3. **Uniform trees** (§3): with b offspring per node and height step Δh, the silhouette s = ln b/Δh gives an autocorrelation decaying as t^(−v), v = s/(1 − s), provided e^Δh > b. In per-pair terms, rates falling by g = e^(−Δh) per level, v = ln b/(ln(1/g) − ln b). Where s ≥ 1, "relaxation is unstable in part or all of the tree which can thus be collapsed to a single state".
4. **Finite trees** (§2): "for finite trees the decay of the autocorrelation function to its equilibrium value is always exponential".
5. **Shape** (§3): "fatter trees relax faster"; uniform trees saturate the bound on v; faster-growing heights give slower-than-power decay.

## Bearing on the record

- **[LEAD-tmp7rohc](../leads.d/LEAD-tmp7rohc.md)** (step 1 confirmed): the assistant's own check of 2026-11-21 fitted exponents to ln b/ln(1/(bg)), which equals ln b/(ln(1/g) − ln b); the lead's first guess, ln b/ln(1/g), holds only for g the ratio of total escape rates. A finite designed tree shows a power-law window that ends exponentially.
- **[CLAIM-tmp6q7ma](../claims.d/CLAIM-tmp6q7ma.md)** (grounds): a tree of rate differences seen from one state decays as a power of time.
- **[CLAIM-tmpxi826](../claims.d/CLAIM-tmpxi826.md)** (supports by setting): the metric tree here, rates e^(−h) at the common ancestor, is that claim's limit; this paper supplies the dynamics on it.
- **[CLAIM-tmpy75jv](../claims.d/CLAIM-tmpy75jv.md)** (qualifies): a level stays a level only while its rate ratio beats the branching; the number of states in a block matters, not only the spread of rates within it.

## Limitations

A 1987 preprint read from extracted text with garbled equations; §§4–6 not read; Ogielski and Stein's own exponent is not quoted.
