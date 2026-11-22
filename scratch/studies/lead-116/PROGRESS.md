# LEAD-116: Run stochastic and factorial assembly scored by committor

- Lead: LEAD-116 (Open, stage specified)
- Branch: claude/lead-116-committor-assembly (cut from origin/staging)

## Task as understood

Extend CASE-216's four-state annealing toy into the stochastic assembly study
CASE-219 and its factorial variant CASE-220, and score intermediates by the
committor q(s) = Pr_s(tau_F < tau_K) (chance of reaching the target F before a
designated failure set K). Build in numpy as continuous-time Markov chains;
committors are exact linear solves on the transient states. Vary allocation at
fixed total (QUESTION-400). Test with pytest.

Advances QUESTION-400, CLAIM-567, CLAIM-566, CLAIM-599. Operationalizes
CASE-219 (stochastic) and CASE-220 (factorial, committor-scored), extending
CASE-216.

Targets to demonstrate:
1. Committor orders intermediates by their future, not their progress
   (bond count): a more-assembled trap with lower q than a smaller nucleus
   (CLAIM-567 reachable != reliably reached; CASE-220 "progress not completion").
2. Delta q_N: productive nucleus (q up) vs trap (q down); TERM-117.
3. Two separately productive nuclei combine into a trap (V non-monotone):
   an assembly-dynamics instance of CLAIM-599, which so far has only a
   stipulated numerical example.
4. QUESTION-400: reallocating a fixed stock at fixed total changes which form
   nucleates/results while the attainable set is unchanged.
5. CLAIM-566: assembly vs persistence, F reversible.

Filing note: CASE's bears_on takes QUESTION codes only; case->claim by
illustrates/counterexample_to; executed case variant_of CASE-219/CASE-220/CASE-216.
Held entries (CASE-216/219/220, the cited claims, the lead) get only dated notes
and relation fields; no status/title/text changes.

## Done

- Read CLAUDE.md, design principles, ADR-001/048, run-lead skill.
- Read LEAD-116, CASE-216/219/220, CLAIM-567/566/599/184/185, QUESTION-400,
  TERM-117, THEORY-1398, existing scratch/formal/dna_origami_toys.py, record.md
  field reference.
- Step 1: confirmed target not already held (CASE-219/220 still Proposed
  proposed-studies; LEAD-095's committor work is a different lead).
- Cut branch, wrote this PROGRESS.md.

## Next

- Write the assembly CTMC engine + scenarios (assembly_committor.py).
- Write pytest (test_assembly_committor.py), run it.
- Produce results (results.txt/json), README.
- File executed-study CASE(s), a CLAIM for the finding, dated notes on held
  entries, changelog fragment.
