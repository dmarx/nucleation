# Reader notes: search (data scheduling / "conversational first, domain later")

Brief: find LM-training work showing generic conversational text early helps later learning of harder domain text; also null results on ordering.
Excluded (planned elsewhere): Skill-it! (2023), Don't Stop Pretraining (2020), Bengio et al. Curriculum learning (2009).

## Log
- Started; worktree on claude/readers/data-scheduling.
- Web searches (conversational-first, dialogue-then-domain, BabyLM speech-then-text, staged general-then-domain): no paper found that tests a conversational-first then domain-text schedule directly. Neighbours only so far.
- Verified on arXiv API (id, date, abstract): 2510.14865 (Midtraining bridges, Liu/Neubig/Xiong, 2025-10-16); 2510.03264 (Front-loading reasoning, Akter et al., 2025-09-26); 2406.03476 (Does your data spark joy, Blakeney et al., 2024-06-05); 2408.03617 (Child-directed speech, Feng/Goodman/Frank, 2024-08-07: "global properties do not" matter -- ordering null); 2502.19249 (Pre-pretraining on formal languages, Hu et al., 2025-02-26: "33% smaller token budget"); 2102.01293 (Scaling laws for transfer, Hernandez et al., 2021-02-02); 2412.15285 (Two-phase pretraining, Feng et al., 2024-12-18); 2506.11300 (Beyond random sampling, Zhang et al., 2025-06-12); 2509.24356 (Text simplification curriculum, 2025-09-29).
- Doubt: owner's "generic conversational text" phrasing not matched by any abstract yet.
- Added 2402.17400 (Yildiz et al., 2024-02-27): domain order in continual pretraining; similar-order specializes, random order transfers better.
- Conclusion: the specific "conversational first, harder domain later" result not found; best neighbours are Midtraining Bridges (2510.14865), Front-Loading Reasoning (2510.03264), Pre-pretraining on formal languages (2502.19249). Ordering-null: 2408.03617.
