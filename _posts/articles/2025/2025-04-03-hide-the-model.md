---
title: "Hide the model: On shallow product thinking"
main_image: nyc2024/previews/36.jpeg
layout: post
category: articles
tags: [data, machine learning, ai, technology, literature]
description: Nobody wants to use your LLM-powered service. They want you to solve their problems. 
---

Nobody wants to use your LLM-powered service. They want you to solve their problems. 

Great products hide complexity. When a glucose monitor triggers an alert, or a CRM surfaces your next best lead—that's AI. Same with the ad targeting that caused your last impulse buy, the bank fraud notice sitting in your inbox, or the document parser that helped you get through tax season. We notice the results, so why do we ignore the methods? Simply put, these are problems solved. No one cares how, as long as it's fast, cheap, and reliable.

When things work we don't think about the tech behind them, and language models, the current iteration of AI, will be no different. The moving goalposts idea is not new. New technologies have quickly faded into the background for centuries. As Douglas Hofstadter noted in 1979:

> Ever since Pascal and Leibniz, people have dreamt of machines that could perform intellectual tasks \[…\] nowadays, practically no one feels that sense of awe any longer – even when computers perform operations that are incredibly more sophisticated than those which sent thrills down spines in the early days \[...\] intelligence is always in that next thing which hasn't yet been programmed.
>
> Douglas Hofstadter, **Gödel, Escher, Bach** (1979)

The AI success stories of the last decade have become invisible. The ones that we *still* call AI are those that pretend to be general purpose, but remain unreliable. What seems to go over people's heads is that these products are not a single "intelligences." Siri, Alexa, and co. are entry points, shallow veneers over highly curated ~~compound systems~~ [duct-taped pipelines](https://bair.berkeley.edu/blog/2024/02/18/compound-ai-systems/) that crunch datasets into models, which are in turn used to index other datasets, surfaced on all-encompassing interfaces. With those products, we learned which magic words route us to their definitive answers, and which knowledge is inaccessible, leading to frustration. Language models are no different. The aperture of prompting incantations has widened, and the answers now come wrapped in a wall of extraneous text, but they are also frustrating, and often wrong.

Today’s AI UX problem isn’t that models are dumb—it’s that builders are lazy. Telling me that your system is *agentic* or that you're using a *model context protocol server* doesn't make the experience of using your product more satisfying. You can be lazy and name your bot a cute name before you even know what it does, but that's not product thinking. Your product doesn't need to be anthropomorphized. Your users don't have to know –or care– that there's an LLM under the hood; don't have to think about what it works for or doesn't; don't have to think about how to prompt it with magic spells, nor whether it's doing *retrieval augmented generation*. If a user has to think of any of this you're asking too much of them.

Don't be lazy and ask users to figure it out by staring at a blank text box. Bake it into your product instead.

The best tools, AI or otherwise, don't masquerade as general-purpose. They solve specific problems. Our job as builders is not to tell users how a tool works, but to constrain what the user sees and the actions they can take so they can rely on our tool intuitively. While extremely powerful, assistants died in the uncanny valley, so we ended up just asking for the weather – one of the few places where we knew we'd have the "I'm feeling lucky" experience promised in the early days of Google. We learned not to ask questions that would land us in a "here's what I found on the web" response. Agents are the same - over a year using Cursor as my main IDE, I'm starting to get a sense for when `⌘+k` won't add enough context to work or when the ask is too tall so the agent will just get stuck.

While moats and sustainable business models are unclear, Silicon Valley's obsession with buzzwords and catchphrases persists: we've all been through the eras of "Uber for X" and blockchain for everything. And as money sloshes around Silicon Valley, many have meme'd their way into a funding round as "AI agents for insert-your-industry-here," like others did with NFTs, subscription boxes, and the business model du jour before that. Many engineering hours are going into channeling LLMs to be more resilient, and new [marketing buzzwords](https://twitter.com/HamelHusain/status/1798757828100047063) quickly materialize to explain to the user how the newest mousetrap will help them.

These models are powerful, enabling workflows that would have been prohibitively costly to automate in the past, but harnessing their power requires [deep product thinking](https://www.ben-evans.com/benedictevans/2024/6/8/building-ai-products). On the surface, the flexibility of a general purpose chat box with an agent's looping transcript seems freeing. In fact, what people want are constraints, not vibes.

The winners won't be those that talk about agents or tool use and push the thinking to the user. Instead it will be those that mindfully use this new technology to generate signals behind the scenes, shaping the user experience, and understand the problems their user is actually trying to solve. They’ll just feel like magic. And, eventually, no one will call them AI.

<hr>

<small>
<em>Photo: Guggenheim Staircase, by me. Previously posted on [New York, 2024](/photos/2025/02/17/nyc2024/).
</em></small>
