---
title: "Startups I Didn't Start: Synthetic A/B Traffic Agents"
main_image: wyoming/previews/37.jpeg
layout: post
category: articles
tags: [startups, technology, ai, programming, experimentation]
description: Anyone who's run experiments at scale knows it's slow, often political, and full of pitfalls. What if you could run "experiments" without real users?
---

<small>
<em>Between 2022 and 2023 I explored many startup ideas, seriously considering 8 partnerships before founding Inscope. Some died as simple prototypes, others first became decks or demos shared in user research calls. In this series, I'm sharing some of the ideas I rolled around at the time, and why I ultimately decided not to pursue them. You can find the previous post in the series [here](/articles/2026/01/09/pipeline-optimizer/).</em>
</small>

Anyone who's run experiments at scale knows it's slow, often political, and full of pitfalls. Simple UI changes break conversion for that one random browser version, or disproportionately affect people in one region. Tests that "should" take a week easily turn into three. Even when everything goes right, you're left waiting for more data to resolve arguments nobody wanted to have in the first place.

I got a close-up of this at Apple. I was the engineering manager building Siri Search's experimentation platform, and the team was rolling it out to the rest of Siri when I left. For ML features, experimentation *is* the product development loop, defining the experience and bottlenecking the rollout of new ideas. If results are unreliable or hard to interpret, you don’t just ship slower; millions of users face suboptimal experiences until you agree the stats are good enough to move forward.

Experimentation has a hidden cost most teams underweight: it’s not just eng setup and analyst time, it’s weeks of [knowingly burning cash *not* showing users the best known version of your product](https://en.wikipedia.org/wiki/Explore-exploit) while collecting results. And since running tests is expensive, teams cut corners. They peek early, slice and dice segments, and keep checking charts [until something looks convincing](https://en.wikipedia.org/wiki/Data_dredging). You don't need a stats PhD to read this [classic Airbnb blog post](https://medium.com/airbnb-engineering/experiments-at-airbnb-e2db3abf39e7), which explains that if you monitor results continuously and stop when you see a win, you’ll eventually “find” effects, which makes the whole exercise moot. 

What if you could run "experiments" without real users? We did it all the time with counterfactuals: fork a request, run a parallel path, and check how your system would have responded. Great, except only some kinds of features can be tested this way. You don't know what the user would have done if they’d seen the other answer. Could you simulate the user behavior, though? That would let you iterate on more ideas before exposing changes to the world, compressing that feedback loop. In early 2023, prompting an LLM “you’re an expert in X domain” was the hot new thing, so why not tell a bot “you’re a mom in Nebraska trying to buy shoes for your kids," followed by "Here’s a landing page. Where do you click?” An LLM-based simulator couldn't replace real experiments, but it could pre-test ideas in minutes, avoid a lot of these incentives traps, and cut down the number of long, costly tests.

The interface I imagined was almost childish. Users would specify a matrix of personas, intents, and page variations. From then on, it’s just a parallel grid search, time, and inserting coins for more tokens. You point your model at a combination, let it browse, and watch what happens. Where does it click? Does it get stuck? Bounce? Repeat across personas and variations, treating the model's behavior as synthetic traffic: fast, cheap flow comparison.

I built a crude prototype on top of Playwright with early open models. It could navigate pages and (mostly) followed simple instructions. But the limiting factor was model behavior. Even after upgrading to whatever the best ChatGPT model was then, results weren’t variable enough. Real users misread, get distracted, click the wrong thing confidently, and go down rabbit holes when confused. A synthetic user, especially one hyper-instructed for someone else's goal, doesn’t simulate the part of the world that matters.

I still think there's an opportunity here, and the buyer is obvious: growth and marketing teams will try anything that promises lift. They already measure conversion obsessively, and the value of faster iteration is legible across the board. Had another project not come along, I might have pursued this one, but the timing wasn’t right.

<hr>

<small><em>
Photo: Wyoming, by me. Previously posted on [Jackson Hole, Tetons, and Yellowstone, 2024](/photos/2024/10/27/wyoming/).
</em></small>