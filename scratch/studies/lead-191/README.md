# LEAD-191: a signalling-allowing sheaf test against CbD 2.0 on LIT-844's data

## What is here

- `routes.py`: linear programs, by scipy's HiGHS, for the binary 3-cycle
  of LIT-844 (arXiv 2412.16806v1). They compute:
  - the contextual fraction CF and the signalling fraction SF, as LIT-844 §3a
    defines them;
  - the corrected sheaf criterion CF > 2|M|·SF that LIT-844 applies. It takes
    it from Vallée et al.; that paper was not read here;
  - two more sheaf-side readings of "contextual once signalling is allowed".
    Both are the assistant's own:
    - `ns_part_contextual`: the no-signalling part of a minimal-SF
      decomposition (LIT-844's eq. 3.3) is contextual;
    - `nearest_ns_contextual`: the model is farther from the noncontextual
      set than from the no-signalling set, so every nearest no-signalling
      model is contextual. The distance is the sum, or the max, of the
      total-variation distances over the contexts;
  - CbD 2.0 noncontextuality: an LP for whether the six variables R_q^c have
    a coupling whose bunches are the model's and whose connections are
    multimaximally coupled. With two binary variables per connection, that
    means maximally coupled.

  It also gives the closed forms: SF = max|ε_i|, and
  Δ = |ε1−ε2| + |ε2−ε3| + |ε3+ε1|.
- `test_routes.py`: 249 tests. The LPs agree with the closed forms
  (CF ≡ 1, SF = max|ε|, CbD contextual iff Δ < 2, ns-part contextual iff
  SF < 1). The sheaf region lies inside the CbD region. The uniform family
  ε = (p, p, p) diverges for 1/6 ≤ p < 1. Two control models are included.
- `study.py` → `results.json`, in four parts:
  1. LIT-844's published counts, checked arithmetically. The divergence
     count follows from them.
  2. The 25 instances printed in LIT-844's Tables 1 and 2, as (SF, Δ). For
     each: both verdicts, with rounding taken into account, and the
     nearest-NS readings over sampled ε triples consistent with the
     printed values.
  3. The uniform family.
  4. 3000 random PR-like models tallied by all five verdicts.

## Rerun

    cd scratch/studies/lead-191
    OPENBLAS_NUM_THREADS=1 python3 -I -m pytest -q -p no:cacheprovider test_routes.py
    OPENBLAS_NUM_THREADS=1 python3 -I study.py      # about 25 s on one core

## Why the full reanalysis was not possible

LIT-844 publishes only aggregate counts and the (SF, Δ) of 25 printed
instances. It does not publish the per-instance BERT probabilities.

- **The repository.** Its §9 points to github.com/kinianlo/Contextuality-in-LLM.
  On 2026-11-23 that repository held one commit ("initial commit",
  2024-05-28, tag v0.1.0) with a README and a .gitignore only. It had no
  code and no data, although the README says it "contains the code and
  data".
- **The release page.** github.com/kinianlo/contextuality-in-llm/releases/tag/v0.1.0
  returned HTTP 403 through the session proxy on 2026-11-23. It was not
  retried, and whether any release assets exist is not known.
- **Zenodo.** A Zenodo search found no deposit.

Both verdicts are functions of (SF, Δ) alone. So the published (SF, Δ)
values are enough to recompute the verdicts on the printed instances. With
the inclusion proved here, the published counts also give the exact
divergence count.
