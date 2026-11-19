---
status: Read
paper: LIT-tmpuv25r
title: 'Marx — Mapping reddit''s active communities'
version: 1
history:
- version: 1
  date: '2026-11-19'
  note: >-
    Read in full by the filer on 2026-11-19 from the owner's site; the
    interactive map and the static figures were not viewed. Quotations
    checked by script against the downloaded text.
date: '2026-11-19'
summary: >-
  A map of Reddit's subreddits by shared active users, built so that the
  direction and weight of each edge read as the share of the target's
  active users also active in the source. A small community nested in a
  large one then shows as an edge into the small one, which the post
  reads as a specialization forked from the larger community. Monthly
  graphs are flattened by the maximum weight, filtered and clustered; the
  post shows clusters for sports, gaming, fashion and others, and names
  communities that grew around April Fools pranks and then went quiet.
---
<!-- inactive-ok-file: CASE-tmp6idy5 — Proposed; the case this reading is filed with -->

# NOTE-tmpbivmm: Marx — Mapping reddit's active communities

## Contribution

A practical method for showing nested communities in a bipartite
user–community network, and a map made with it, meant for users to find
communities.

## Key results

1. **The weighting.** Mutual active users between two subreddits are
   divided by the active users of the target, so each edge reads as
   "what is the proportion of members of the target community who also
   participate in the source?" With one large and one small subreddit,
   "we can construct an edge whose direction suggests that the smaller
   subreddit is a specialization forked from the larger community".
2. **Activity, by month.** "A user is defined as “active” in a subreddit
   if they commented in at least 3 separate submissions in a given
   month"; ratios below 0.1 are dropped. Relationships "were then
   aggregated by taking the max of the observed mutual user ratio across
   all months to flatten the time dimension."
3. **Joke communities.** The post names "the surprisingly sprawling,
   albeit currently inactive, communities that have sprung up around April
   fools jokes" (/r/TheButton, /r/Periwinkle, /r/Orangered), dropped from
   the map as no longer active.
4. **Clusters shown.** Among them "a very large community focused on
   American Sports", and a "microcommunity embedded in the larger
   high-performance computing community" around /r/buildapc.
5. **Against a significance filter.** A backbone extraction by edge
   significance is "deceptively aggressive": it drops strong edges between
   low-degree nodes, so small tightly knit communities disappear.

## Assumptions

Activity read from public comments (January 2015 to November 2016); a
user active at three or more submissions a month; thresholds chosen by
judgment; Gephi's modularity clustering.

## Concepts

Bipartite projection; directed mutual-user ratio; specialization edge;
community clusters labelled by prototype subreddits.

## Bearing on the record

The owner named it at U37 of the follow-up turns of "Topological
protection explained" as where communities forming subcommunities can be
seen. The directed weight is a candidate signal for a parent and a
specialization; flattening the months by their maximum removes the order
in which communities formed, which a study of formation would need
(CASE-tmp6idy5). The April Fools communities are joke distinctions that
became communities, and then lapsed.

## Limitations

Read from the text; the map itself not viewed. Built for discovery, not
for inference about formation; the thresholds are judgment calls.
