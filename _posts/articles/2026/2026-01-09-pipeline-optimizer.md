---
title: "Startups I Didn't Start: Pipeline Optimizer"
main_image: wien/previews/6.jpeg
layout: post
category: articles
tags: [startups, technology, ai, programming]
description: Enterprise sales are chains of cross-team handoffs, but managers rarely have visibility outside their silo. The predictable outcome is local optimization. What if you zoom out?
---

<small>
<em>Between 2022 and 2023 I explored many startup ideas, seriously considering 8 partnerships before founding Inscope. Some died as simple prototypes, others first became decks or demos shared in user research calls. In this series, I'm sharing some of the ideas I rolled around at the time, and why I ultimately decided not to pursue them.
</em></small>

Enterprise sales are chains of cross-team handoffs, but managers rarely have visibility outside their silo. The predictable outcome is local optimization: each team improves its own metrics without asking where the system’s leverage points actually are. What if you zoom out? I learned [the concept in school](https://en.wikipedia.org/wiki/Theory_of_constraints), but was first exposed to this behavior in the wild at Vouch, building the data pipelines that fed our GTM motion.

If you are in insurance, lending, or investing, a key function is selecting which deals to turn away. In a sense, these companies sell money, so demand is usually not the bottleneck. That means, by definition, the bottleneck is inside the decision process, and it often isn’t obvious where. Even in the highest caliber teams, deals idle in queues at whatever desk is constrained, which varies over time. Working with RevOps, I realized I could apply queuing theory on top of my data engineering skill set to build an end-to-end optimization engine.

The core insight was that each decision point has staffing costs and accuracy tradeoffs, and that you can estimate them from prior deals. Sometimes a junior person can handle a case even if their error rates are higher: speed might matter more than precision if you'd lose the deal to a competitor otherwise anyway. Other times you pull in senior people because a deal is large and a mistake would be expensive. The decision [costs are asymmetric](https://web.archive.org/web/20160904174426/http://blog.mldb.ai/blog/posts/2016/01/ml-meets-economics) too. Declining a deal you should have accepted leaves money on the table, but accepting a bad deal might create costly future claims or defaults. Opportunity costs also change depending on where in the process you drop a deal. There's a lot of value to uncover if you can get sharper with your routing.

This is classic operations research: treat each step in the chain as a state with transition probabilities, and routing as a choice based on historical estimates. Given expected value, capacity, staffing costs, and error rates each way, you can compute the path that maximizes expected utility. The goal is not maximum accuracy at every step, but good enough decisions for each deal’s expected value. Even better, once you have a [Markov map](https://en.wikipedia.org/wiki/Markov_decision_process) of your team, you can understand where to invest next to maximize expected value across the whole system.

The cool thing about this idea in 2023 was that deeper AI decisioning felt imminent thanks to new capabilities to process unstructured data. It seemed plausible to run counterfactuals on what an LLM would have done as a node in the system. Would it make the same mistakes, and at what cost? There for sure would be points on the cost curve where it would make sense to pull the trigger on the LLM's choice without human review, to pay more for a premium model's answer, or to just wait for the senior underwriter without even showing them the LLM’s draft reasoning.

Ultimately, as excited as I was about the idea, I realized it wasn’t a standalone product. User research pointed to it being more a killer feature for Salesforce or HubSpot than a net new startup. CRMs and marketing automation tools already track ACV and handoffs, collecting the history you need to estimate the matrices. As an MVP at a startup it would have been brutal to set up, dealing with both integrations hell and a cold-start data problem. And there’s the most basic question of team politics: who do you sell to? 

<hr>

<small>
<em>Photo: Pipeline, by me. Previously posted on [Wien, 2025](/photos/2025/11/17/wien/).
</em></small>