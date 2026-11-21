# Reader notes: mup-yanghu (Yang and Hu, TP IV, arXiv 2011.14522; LIT-tmp9tr5w)

## Step 1: copy located (2026-11-21)
- https://arxiv.org/pdf/2011.14522 : arXiv, lawful. Fetched 2026-11-21, 65 pages, PDF, converted with pdftotext.

## Step 2: sections read
Read: abstract, §1 (intro, abc def, dichotomy statement, µP), §2 related work, §3 (3.1 shallow NTK/MF, 3.2 stability Thm 3.3, nontriviality Thm 3.4, Def 3.5, Thm 3.6, Def 3.7, Thm 3.8, Cor 3.9, 3.10, Rem 3.11-3.12), §4 SP, §5 µP (5.1-5.3: r_l, Prop 5.3, Defs 5.2/5.4, Prop 5.5, Thm 5.6), App B, App C/C.1, App G (uniform body, UP_r edge from µP to NTP), App H.1 defs H.9-H.12, Thm H.13, Cor H.14, Rem H.15-H.16.
Skipped: §6-7 derivations (Tensor Programs, Master Theorem), §8-9 experiments (Omniglot, Word2Vec) except intro figures, App D-F, H.2-H.8 proofs.
Key: r = exponent with Delta x^L = Theta(n^-r) (Def 3.2); per-layer r_l = size of Delta W^l x^{l-1} (Prop 5.3); muP all r_l=0, unique (Thm 5.6). NTP = UP_{1/2}: body uniform r_l = 1/2, readout updated maximally (Theta(1)). SP(LR 1/n): r_1 = 3/2, r_l = 1/2 (my arithmetic). Only O(1) training time.
