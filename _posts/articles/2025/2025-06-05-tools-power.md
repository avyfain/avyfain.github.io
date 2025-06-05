---
title: "The best tools take power away"
main_image: h123-variety-pack/previews/21.jpeg
layout: post
category: articles
tags: [tools, startups, technology, entrepreneurship, business, programming]
description: Good tools give users agency; the best tools take it away and prevent mistakes.
---

Good tools give users agency; the best tools take it away and prevent mistakes.

This idea, from a decade-old [blog post](http://tagide.com/blog/research/constraints) by UC Irvine professor Crista Lopes, has stuck with me. Lopes argues that the real work of programming language design is to constrain. As computers' abilities expand, guardrails become more important. Constraints aren’t limitations, they’re high leverage product decisions that help us avoid [footguns](https://en.wiktionary.org/wiki/footgun), and give us just enough rope.

Most engineers today write Python and Javascript, not Assembly or C, because those languages eliminate dangerous choices and wrap power in safer, higher-level defaults. The same thing is true of B2B software. Excel’s blank grid feels empowering, but it's full of opportunities for a junior analyst or accountant to mess up the numbers for your board meeting. Although financial professionals love Excel's flexibility, their bosses prefer it when they don't make mistakes, so they pick narrow tools with guardrails:

* **Opinionated GUIs.** The next button is either enabled or it isn’t. Users literally can’t click on-to the wrong step.  
* **Customer and vendor names aren’t text, they’re objects.** No “Acme,” “Acme Inc.,” and “Acme LLC.” Dropdowns keyed on IDs means joins never break.  
* **Journal entries can’t freestyle.** Pipe everything through a ledger service that refuses to post unless debits match credits.  
* **Metrics live in semantic layers.** Define once in code; every dashboard inherits it. No ad-hoc SQL, no divergent truths.

In the past year there's been a lot of talk about how AI changes the cost structure of build vs. buy decisions, and how selling B2B SaaS will get harder as companies will build something perfectly customized to their use cases. 

I don't buy that. A tool that works for hundreds of companies will likely work for yours too, and the team building it likely has already seen someone blunder into the pothole you don't know you're about to hit. They're much more incentivized to get the workflows right than you are. When choosing great tools, users trade a little agency for a lot of peace-of-mind, an easy sell to anyone who signs a P&L. You should only build when it's a strategic core competency.

When I first read Lopes' post in 2016 [I wrote](/links/2016/06/13/links/):  
> Taking away an engineer’s ability to do *X* also removes a concern from the picture. Thinking about less things at once means you can focus more on what’s left. 

I’ve internalized this outside of work, too. In my photography, I shoot film, mostly with prime lenses. The limits are the point. Fewer knobs to tweak means I pay more attention to composition and light, and get those right. I have a limited number of shots, so I slow down. Ironically, the constraints make the creative process feel freer and produce better outcomes.

Constraints are not handcuffs, they're clarifying. 

<small>Thanks to Hannah Doherty for her feedback on early drafts of this post.</small>

<hr>

<small>
<em>Photo: On Rails, by me. Previously posted on [H1 '23 Variety Pack](/photos/2023/06/14/h123-variety-pack/).
</em></small>