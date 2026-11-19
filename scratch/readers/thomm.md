# Reader notes: thomm (Thomm et al. 2024, arXiv 2402.05785)

## Copy
- arXiv PDF v5 (5 Nov 2024, NeurIPS 2024 camera-ready), fetched 2026-11-19 from arxiv.org/pdf/2402.05785; 43 pages. Lawful (arXiv). Text kept in reader scratchpad, not here.

## Read: main text (sec 1-7), appendix B.1, C (all tables), C.4, skimmed A, D
- Design: LLaMA 150M trained FROM SCRATCH on all sub-tasks CONCURRENTLY with the composed task ("train a LLaMA model from scratch on all sub-tasks concurrently (sampling from them uniformly at random)", sec 4.1). Not sub-tasks first, then the composition.
- Measured: accuracy at convergence of the composed task as a function of the number of composed-task samples, with vs without sub-task data in the mix (w/ sub-tasks vs w/o sub-tasks, Fig 3, Tables C.2-C.9). Sample counts of sub-tasks fixed (e.g. PEN: Cpy 20K, RCpy 20K, PE 60K, PEV 100K).
- Finding: no significant benefit from the sub-tasks; composed task needs more samples than the sum for all sub-tasks (H4).
- One run per row (C.3: "Each row ... corresponds to one run"); checklist: no error bars.
- Sequential design appears only in reverse (sec 4.2, decomposition): pretrain on PEN (1000K) then fine-tune on PEV; PERM (2000K) then PE.
- No matched first stage, no intervention on learned components.
