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

## Numbers read off Tables C.2-C.9 (single runs)
- PEN, composed-task samples 100/500/750/1000K: with sub-tasks 0.00/0.93/0.95/0.97; without 300K 0.00, 500K 0.74, 750K 0.98, 1000K 0.98. So at 500K the mix is ahead, at 750-1000K behind; one run each, no statistics.
- PERM 1000/1500/2000K: with 0.74/0.91/0.91; without 0.68/0.65/0.98.
- HSS 25/50/100/200K: with 0.68/0.85/0.95/0.99; without 0.67/0.84/0.95/0.99.
- MUL 200/400/800/1600K: with 0.65/0.68/0.74/0.77; without 0.56/0.63/0.78/0.77.
- H3 threshold = sum of fixed sub-task set sizes (PEN 20+20+60K = 100K without PEV; PERM 40+40+150K = 230K). Sub-task sizes are chosen, not measured minima.
- "No significant benefit" is the authors' reading of single runs without tests; the with-arm also sees more total data.

## Bearings searched
- Record holds no LIT for this work. Closest: THEORY-tmpd6l4a (Chen et al., Skill-it: mixing prerequisite skills helps at equal steps) is in tension; THEORY-253 parallel; THEORY-tmpk9cmk / tmpmy98s / tmpq9sev / tmpf6s7m are staged-transfer designs this one lacks.
- Lead design: (a) only joint-mixture vs composed-only, not sequential; reverse sequential (decomposition) in 4.2; (b) no; (c) no.
