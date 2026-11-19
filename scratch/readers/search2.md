# search2: Reddit/social-media data early in pretraining

Brief: find work showing generic conversational (Reddit / forum) data helps most at the START of LM training and eases learning of harder domain text later.
Skipping neighbours already found by `search`.

## Log
- Started. Angles: Reddit in data mixtures/ablations, data ordering by source, forum-first curricula.
- Web searches (Reddit early / conversational first / BabyLM dialogue-first): no direct hit yet.
- Candidate: Wang, Mittal, Song, Jia, "Data Shapley in One Training Run", arXiv 2406.11011 (v1 2024-06-16, verified on arXiv API). Sec 5.3.2 read: "in the early stages of training, general corpora tend to have a relatively large contribution regardless of the downstream tasks ... in the later stages of training, the contribution from domain-specific corpora becomes dominant". The general corpus is Pile-CC (web crawl), not Reddit; attribution, not an ordering intervention. Partial fit.
- Candidate: Opper, Morrison, Siddharth, 2311.00128 (2023-10-31): BabyLM, speech/dialogue corpora (AO-Childes, OpenSubtitles) drive grammar acquisition; "proportion of training steps assigned to such data". Weak-partial: no later-domain effect.
- Candidate: Nishida et al., "Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining", arXiv 2608.13515 (2026-08-13, COLM 2026). Abstract: "Early in training, literature-related data are more strongly aligned with the trajectory toward the final parameters, whereas STEM data become more strongly aligned in later stages." App. B.1: early high-contribution example "is conversational and closer to natural discourse". Attribution on Pythia, not an ordering intervention; no Reddit. Partial fit.
- Checked and set aside: Albalak ODM 2312.02406, ADO 2410.11820, Sweeney Lie-bracket transfer order 2606.24993 (ordering method, no Reddit finding).
