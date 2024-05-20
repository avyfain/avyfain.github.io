---
title: Reflections on my first startup attempt
main_image: tailandia/previews/40.jpeg
layout: post
category: articles
description: I started a startup, and I'm no longer part of it. Needless to say, this was not the exit I imagined.
tags: [startups, jobs, technology, software engineering, programming]
---

> "And so castles made of sand fall in the sea, eventually"
>
> -Jimi Hendrix

I started a startup, and I'm no longer part of it. Needless to say, this was not the exit I imagined.

Coming out of a strong fundraise, we had money in the bank, great investors on board, customers ready to pay to jump in, and had just closed the last candidate on our hiring plan for the year. We were in the midst of building a great product, but we had different ideas about where we stood, our velocity, and how to move forward. Rather than working through it together, my co-founders decided they wanted to part ways with me.

From the beginning, my biggest risk when we started the company was obvious: I was joining two people with similar backgrounds, in finance, who knew each other well. As the only technical one out of three co-founders, I was the odd one out on multiple counts. It was clear that I was stepping into a [well known founder dynamic](https://hn.algolia.com/?q=technical%20cofounder), but I convinced myself that the market pull and the specific people involved would offset that risk. In the end, it all boiled down to mismatched expectations.

Out of the lessons of this past year, my biggest learnings were about myself:
* The breadth of my abilities, stretching to build the v0 of everything, including teaching myself Typescript and React to build our first prototypes, or designing our logo and our first marketing site, not just the backend and data pipes that were closer to home. After years of managing teams of engineers, it felt good to be hands-on-keyboard again.

* The strength of the network I've built in San Francisco, which allowed me to bring in investors and friends who were excited to help and be part of what I was building.

* The persuasion skills needed to convince candidates to join us, and build a great engineering team at a no-name company. It was also my first time recruiting for roles I hadn't done myself before, where I had less experience to draw on. I had felt a step up in difficulty recruiting when I left [Apple for Vouch](/articles/2021/04/26/new-beginnings/) – in comparison this was playing at the hardest level.

I also learned a few lessons along the way that can hopefully help other aspiring founders, and not just my future self:
* **Choose the right place to start.**
Pick a product strategy that delivers tangible value early on. Focusing on a complex MVP that requires perfect execution for eventual payoff is an easy mistake.
Our original strategy required two components: data pipelines to ingest and aggregate transaction-level data into metrics[^1], and a generative AI UX to produce financial reports. Instead of focusing on the latter, which left more room for error, we chose to start with what I thought was the harder piece. It required perfection.
Defining the ways in which something needs to be "perfect," and identifying where users will tolerate failure is hard. Not [slicing the product](https://faingezicht.com/articles/2020/06/13/chunks/) into small enough, self-contained, useful deliverables can mean backing yourself into an all-or-nothing corner. Sequence your work incrementally, so your MVP is both minimum and viable.

* **Be deliberate.** 
Small ideas quickly balloon into full-fledged projects and technical debt if you're not paying attention. It's easy to spend time on tooling that could help you onboard customers, without being able to fully service the customers you already have. You should Wizard-of-Oz-it until it hurts. Investing in internal tooling and building for scale is tempting, but it's easy to pave the cow paths too soon, which ends up being counterproductive. Service your first customers with paperclips and duct tape and only build software for what you absolutely can't do without it.

* **Don’t take your competition's marketing at face value.**
It’s easy to panic when you see 10 well-funded startups pop up in your category. It’s harder to remember that if they're lucky their hair is also on fire with customer demand, trying to figure out their own problems. Websites display fancy logos and sleek animations. Press releases are designed to sound impressive and create apparent success. Keep the blinders on, focus on customer needs, and build.

* **Address your biggest risks early.**
When we wish for things to work out, it's easy to ignore the red flags and imagine the success path, and harder to foresee the million ways things could go wrong. You can [copy-paste](https://calteches.library.caltech.edu/51/2/CargoCult.htm) the same "biggest risks" on a shared doc every week, but that won't help if the real problems are simmering in the background. Be honest with yourself, and run pre-mortems periodically to figure out what are the most likely failure modes for your company. Talk about them. Then fix them.

* **Discuss the escape hatch before you need it.**
Whether or not two of every three[^2] startups actually fail because of co-founder conflict, break-ups are large risks to any company. You will probably download a template or work with a cookie-cutter service for your founders agreement and incorporation docs, but you should spend time discussing what a fair separation should look like, and write it in, in case you do get there. There will be a thousand things on your mind when you're getting started, so reading and customizing legalese won't be a top priority, but if you do end up with a break-up, having thought about what kind of golden parachute is fair while you are cold-headed and behind a veil of ignorance will benefit everyone.

I am convinced that my early departure was for the better. I wish my former team all the best. 

Eventually, I'll put this experience to good use and take another swing at the startup piñata. In the meantime I am open to fractional engineering roles while I find my next full-time opportunity at a more established startup. If you're looking for a software or data engineering leader to join you, or simply want to hear a founder's perspective, [hit me up](/contact).

 <hr>

<small><em>_Photo: Photo: "Peace Out," Bangkok, Thailand, by me. Previously posted on [Thailand, 2023.](/photos/2024/04/12/tailandia/)_</em></small>

[^1]: NetSuite replication is a notoriously hard problem. This is in part because of their clunky APIs, and in part because of how customization interacts with permissioning. This is why vendors like Merge and Rutter offer a limited set of objects, and drop out to a proxy instead of solving the full problem for their users. If you need a full ledger replica, and want to support custom objects, you're forced to build your own.

[^2]: This often misquoted fact comes from the opening pages of [Noam Wasserman's The Founder's Dilemmas](https://bookshop.org/p/books/the-founder-s-dilemmas-anticipating-and-avoiding-the-pitfalls-that-can-sink-a-startup-noam-wasserman/8964388?ean=9780691158303). He in turn cites 65% from [a 1989 paper by Gorman and Sahlman](https://www.sciencedirect.com/science/article/abs/pii/0883902689900141) which points to "senior management as the most important contributing factor" to company failure, but "senior management" is not necessarily the same as co-founder conflict. To make things worse, the paper is a survey of VCs in 1984! More recently, there's [anecdata from Elad Gil](https://blog.eladgil.com/p/how-to-fire-co-founder) in 2013 quoting a YC founder who blamed failure of ~20% of his batch to co-founder issues. In 2012, Paul Graham [wrote on HN](https://news.ycombinator.com/item?id=4833610) that ~1/4 of companies lose a co-founder, but that's also not failure. I find it odd that there aren't better sources for this.
