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

## Second target (coordinator): code FIRST, natural language later
- Verified on arXiv API: Papadimitriou & Jurafsky 2004.14601 (2020-04-30); Aryabumi et al. 2408.10914 (2024-08-20); Ma et al. 2309.16298 (2023-09-28); Petty, van Steenkiste, Linzen 2409.04556 (2024-09-06).
- Aryabumi Sec 3.1 read: code->text (200B code, then 200B text with 10% code) vs text-only 400B: "The code→text model and balanced→text model beat the text-only baseline on NL reasoning tasks by 8.8% and 8.2% relative improvement". Knowledge: "initializing 100% code gives the same performance with text-only baseline". Strong fit.
- Ma et al. Sec 3.3.4 read: the stepwise code-decrease schedule is tested only at instruction tuning; "since experiments in the pre-training phase require a lot of resources, we leave the validation of this phase to later work." Weak-partial.
- Petty et al.: interleaved mixtures, no ordering; code helps compositional/maths, harms syntax/morphology/knowledge. Weak for ordering.
- Papadimitriou & Jurafsky: LSTM trained on Java/MIDI then tested on NL; "improves test performance on natural language". Partial (small LSTMs, transfer test, not cost of later learning at scale).
