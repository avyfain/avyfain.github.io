---
title: Why should engineers care about insurance technology?
main_image: catch-up/previews/41.jpeg
layout: post
category: articles
description: "The insurance industry is known for its old-fashioned way of doing things: pen and paper, PDFs full of legalese, lots of regulation, and frustratingly long weeks of back and forth to get anything done."
tags: [insurance, startups, jobs, technology, software engineering, programming]
---

<small><em>This essay was originally posted on the [Vouch Engineering Blog](https://medium.com/vouch-engineering/why-should-engineers-care-about-insurance-technology-6ee8ab97b84d).</em></small>

The insurance industry is known for its old-fashioned way of doing things: pen and paper, PDFs full of legalese, lots of regulation, and frustratingly long weeks of back and forth to get anything done. Why would a talented engineer work in insurance technology when there are so many other fast-moving, innovative startups out there they could join? Don’t all insurance products boil down to just a form, anyway?

These were questions I asked myself in early 2021 as I considered making the jump from a cushy Engineering Manager role at Apple to this up and coming insurtech. However, as I realized how central data was to the product vision, and learned about the problems they were solving, I became intrigued and decided to come onboard. A year and a half later, I can share that yes, the problems are weird and awesome and this category matters even more than I thought.

At Vouch, we’re building key technologies that allow us to be fast, responsive and focused on our customers — high growth, innovative companies. In this blog post we’ll discuss some of those technologies we’re creating, as well as some of the industry dynamics that can make insurtech especially appealing to highly skilled software engineers.

Insuring a business is complex because there are no one-size fits all solutions. The price and shape of our policies must change in relation to each startup that applies for coverage. Some startups will be inherently risky and cost more to cover. Others will be in less risky business categories and have lower premiums. In a world of perfect information, this would be an easy problem, but reality isn’t that simple, especially since our clients are building products at the boundaries between conventional categories.

We ask our clients a series of questions to understand their operations, and feed those answers to an underwriting engine that algorithmically generates unique policies tailored for each applicant. The more questions we ask, the better we understand our clients. The less questions we ask the better our user experience becomes.

The software we’ve built models the relationships between our products, our underwriting rules, local regulations, and the knowledge gathered directly from questions to our clients, allowing us to dynamically ask only relevant questions. If a company’s operation is too complex our engine also knows to get a member of our [insurance advisory team](https://www.vouch.us/on-the-line) involved. Having a human in the loop for tough cases ensures clients are properly covered and creates new signals we can use to further improve our system over time.

As new companies get founded and our understanding of the world evolves, so must our products. When the average implementation and rollout of a new insurance product [takes incumbents more than 2 years](https://www.coretechinsight.com/blog/how-long-do-core-implementations-really-take), there is a clear opportunity in moving fast. Keeping our underwriting engine up to speed with our clients is a constantly moving target. This pace of innovation introduces the meta-problem of building the tools to safely build our policies. After launching and scaling our first generation of products, we realized that by introducing ideas of software engineering such as continuous integration and unit testing into the tools Vouch’s insurance operations team uses to configure and administer our policies, we can iterate fast while comfortably going to market with the resulting products.

We realized that having a clear model of the startup ecosystem at large would help us determine the risk profile of potential clients in our underwriting and sales motions. Building this model requires us to have robust data pipelines, a flexible entity resolution system, and exploratory tools to make sense of it all. Understanding individual companies is important, but given how young most of our potential clients are, and how thin the public data on their operations are, we also derive a lot of valuable information from the relationships between companies, founders, and investors in the ecosystem. At Vouch, we are using a knowledge graph to map these relationships and their evolution in time. This paradigm allows us to easily ingest new kinds of data from new data sources while keeping a full paper trail to where we learned each fact, making it easy for non-technical people to keep track of data provenance.

Making better insurance products more accessible to startups is a net positive for the world. The insurance business is rooted in a mutually beneficial market dynamic, where the insurer and the buyer of a policy get to share the risk of uncertain future outcomes. Buyers get an upper bound for their losses while sellers collect a premium. Unlike the buyer, for whom the risk can be existential, the insurer can treat a single policy’s risk as a small bet in a broader portfolio, lowering the volatility of the system as a whole, and thus creating value. Enabling entrepreneurs to take on more risk is one way to push out the frontier of what products are feasible to build, as it lowers the cost of failure for any one company, and that’s exactly what we’re aiming for at Vouch.

As the companies that founders start get more and more complex, the ability to understand the risks they take on becomes a problem that can only be solved with a great team and solid software. If the challenges described above sound interesting, join us in our mission to craft the best insurance for those building the future. [We’re hiring](http://vouch.us/careers)!

<hr>
<small><em>Photo: Fence, by me. Previously posted on [A year of memories, in film](/photos/2024/08/01/catch-up/).</em></small>
