# Reader notes: metastability-bovier (LIT-tmpl98s1)

## Step 1, 2026-11-21: copy located
- https://arxiv.org/pdf/math/0007160 (arXiv, author preprint): fetched 2026-11-21, PDF 44 pp, converted with pdftotext.

## Step 2, 2026-11-21: sections read
Read in full: abstract, §1 (Def 1.1, 1.2, Thm 1.3, remarks, BEGK example (1.15)-(1.18)), §2 (Lemma 2.5, Cor 2.6, e(x,y) almost-ultrametric (2.27)), §3 (Thm 3.1 Green's function, Thm 3.5 mean times), §5 (exclusion sets Σj, Thm 5.1, Cor 5.2, Lemma 5.3/5.4 using ultrametricity, ln T_{x,J} = e(x,J) − f(x)).
Skimmed: §4 (Laplace transforms; Thm 4.4 statement), §6 (Thm 6.1, Cor 6.2 statements). Skipped: proofs in §4, §5.5-5.7, §6.
Key: E(x,y)=Q(x)/T_{x,y} capacity; e=−ln E is ultrametric up to ln 3 on M_N; genericity (rate/time gaps ε_N) assumed throughout; mean exit time = Q(A(x))/cap; eigenvalue ≈ 1/mean exit time.

## Step 3, 2026-11-21: recheck and draft
- Recheck overturns CLAIM-tmpxi826's "the record holds neither": LIT-2035 (Freidlin–Wentzell, Active; front matter read, NOTE-1562), THEORY-1366 (Proposed), LIT-2037 / THEORY-1370 (Berglund, cites Bovier et al. 2004 capacities), NOTE-1590.
- Reader's observation (own check, python3 -I, not in the paper): log of ANY metric satisfies the strong triangle inequality up to ln 2; on 300 random metrics, four-point δ of log d stayed ≤ 0.63. So bounded δ of log commute time needs no rate gaps; what needs gaps is level spacing vs δ. Bears on QUESTION-tmpv6fxp and CLAIM-tmpxi826's hyperbolicity clause. Paper's Lemma 2.5 / Cor 2.6 (ln 3 slack) have the same character and their proofs do not use M_N.
- Draft verdict: characterization corrected (large-N, abstract metastable sets, capacity not barrier, genericity assumed, hierarchy = almost-ultrametric + nested exclusion sets).
