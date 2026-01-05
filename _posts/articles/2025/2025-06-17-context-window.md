---
title: "Big Window, Small Vision"
main_image: cdmx25/previews/9.jpeg
layout: post
category: articles
tags: [tools, technology, ai, programming]
description: Stuffing the context window doesn't mean tradeoffs go away. They just get laundered through the model.
---

Over coffee a few days ago, a friend (YC founder, obviously building agents) told me most people in the space were thinking about it all wrong. His pitch was simple: pick the smartest model, give it the right tools, and call it a day. No RAG, no smart indexing, no embeddings. Just a good prompt and a fat token budget.

He referenced Anthropic's Boris Cherny, who took it further speaking about how for Claude Code they load context and memory [on Latent Space](https://www.latent.space/p/claude-code) (~45 minute mark):

> Early versions of Claude actually used RAG. So we, like, indexed the code base [...] just off-the-shelf RAG, and that worked pretty well. [...] eventually, we landed on just agentic search as the way to do stuff [...] it outperformed everything. By a lot. [...] Just using regular code searching, you know, glob, grep, just regular code search. [...] And then the second one was there was this whole, like, indexing step that you have to do for RAG. And there's a lot of complexity that comes with that because the code drifts out of sync. And then there's security issues because this index has to live somewhere. And then, you know, what if that provider gets hacked? And so it's just a lot of liability for a company to do that. [...] we don't want to upload it to a third-party thing. It could be a first-party thing. But then we still have this out-of-sync issue. And agentic search just sidesteps all of that. So essentially, at the cost of latency and tokens, you now have really awesome search without security downsides.

Agentic search is just `grep` in a loop with a marketing team. No preprocessing, no infra glue, no [composite systems](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/). Just stuff the context window, burn tokens, and sidestep the maintenance mess. The subtext is that models are getting bigger and windows are getting longer, so infrastructure doesn't matter. Just scale the model and let it figure it out.

But a bigger window doesn't fix bad inputs, so I pushed back. [I'd heard a version of this argument before](https://x.com/avyfain/status/1796281064891277646), but saying the models were getting _too_ good. Last year, in a different room, and with a politician's spin from Senator Scott Wiener.

Back in the ancient days of AI, in early 2024, Wiener proposed [SB 1047](https://en.wikipedia.org/wiki/Safe_and_Secure_Innovation_for_Frontier_Artificial_Intelligence_Models_Act), a bill to regulate large-scale AI systems: FLOP limits, training budget thresholds, etc. The idea was to contain dangerous models by putting boundaries around them.

At GitHub's office in SF, he pitched it to engineers as if 'the model' were the unit to regulate. The audience pushed back on him, too. Benchmarks sucked, science was moving fast, and 10^26 FLOPs or $100M wouldn't stay relevant for long. Fine-tuning was seen as adding to the model, so it was regulated. Tool calling and curated databases tacked-on were just SaaS that didn't need intervention. Afterward, I told him that was a broken abstraction. The model doesn't do anything alone. It lives inside a system: tools, data, memory, UI, and, fast forward a year, now MCP servers. Pretending otherwise is wishful thinking. He was implicitly proposing to separate 'the model' from the system that surrounds it. That line doesn't exist, even if the labs are organized in pre and post training teams.

Cherny's "just stuff the context window" strategy makes the same mistake. It pretends the model is the whole product. But preprocessing and curating data is product, too.

In theory, with infinite compute and infinite time, sure... let the model read the whole universe, raw! But that's not the world we live in. In the real world, we have budgets. Constraints. Latency targets. Tokens cost money. Inference isn't free, even if you're part of the Claude Code team. Shaping data into something clean, trustable, and useful lets you navigate this cost curve with fixed costs. Stuffing the context window doesn't mean tradeoffs go away. They just get laundered through the model. What you gain in flexibility, you lose in speed, cost, or interpretability at the margin. The 60s maxim _garbage in, garbage out_ still applies, now you're just paying more to process it.

The context window sounds like a silver bullet, but it's not. My friend's use cases are async. He doesn't care if inference takes 30 seconds. But if you're building a realtime interface, you have to care. Latency is product. Relying on the model alone also kills modularity. With structured systems, you can test components, trace errors, and swap parts without retraining the whole thing. You get observability and control.

Yes, model architectures are improving. Yes, context windows are expanding. But those shifts don't collapse the boundary between model and system. Massaging your data, whether via RAG, indexing, or structured retrieval, isn't wasted effort. It's what lets you pull just the slice you need. It's what makes a system fast, safe, and understandable, but most importantly allows you to evolve your product over time in a deliberate way instead of treating it like Sam or Dario's black box.

<small>Thanks to Hannah Doherty for her feedback on early drafts of this post, even though she's not the target audience.</small>

<hr>

<small>
<em>Photo: Out the window, by me. Previously posted on [CDMX '25](/photos/2025/06/12/cdmx25/).
</em></small>