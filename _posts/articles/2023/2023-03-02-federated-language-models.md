---
title: Federated language models, or the future of universal computing
main_image: oaxaca/previews/84.jpeg
layout: post
category: articles
description: As Wolfram implies, building "one model to rule them all" is a stupid goal
tags: [data, machine learning, technology, software engineering, programming]
---

A few weeks ago, Stephen Wolfram [wrote a piece](https://writings.stephenwolfram.com/2023/01/wolframalpha-as-the-way-to-bring-computational-knowledge-superpowers-to-chatgpt/) on the failure modes of generalized language models, focusing on ChatGPT, and contrasting them to Wolfram\|Alpha's narrow and curated computational engine. You might remember Wolfram\|Alpha as the website that helped you get through calculus more than a decade ago. Unlike ChatGPT, Wolfram's AI tool has not been featured non-stop in the news recently, but it made a splash when first launched and the technology behind it is still popular in scientific circles. Wolfram's critique was just another rant on language model [hallucination](https://en.wikipedia.org/wiki/Hallucination_(artificial_intelligence)), but there was a kernel of insight buried in his post: for a certain class of problems "if ChatGPT 'consulted' Wolfram\|Alpha it’d of course be able to get it right." Wolfram's main point is that there could be a feedback loop in which large language models (LLMs, or simply LMs) improve their performance by acting as interfaces to specialized tools like his, which lie outside of the model's understanding of the world.

Humans change the way they ask questions in order to be understood by Siri or Alexa. Unlike the Google or Bing search box, which return N options for you to sift through, the user experience when interacting with an assistant is, by definition, narrower. The assistants pretend to be universal, but drop out to a web search [with a shrug](https://www.ben-evans.com/benedictevans/2017/2/22/voice-and-the-uncanny-valley-of-ai) if we don't ask things the way they expect. GPT, on the other hand, seems to understand your question and spits out what sounds like a correct answer, but often fails on the specifics. Efforts to get around this have led to full time jobs consisting of [clever prompting and tinkering](https://archive.is/20230301052905/https://www.washingtonpost.com/technology/2023/02/25/prompt-engineers-techs-next-big-job/) with query parameters. The kind of "consulting" suggested by Wolfram could give users of LMs the best of both worlds — the richness of a seemingly universal human language interface when asking questions, and correct answers which happen to be articulate and essay-like, just like GPT's.

Behind the scenes, assistants and search engines often implement an information retrieval technique called [federated search](https://en.wikipedia.org/wiki/Federated_search). A single user interface forwards queries to other subsystems which might have answers and quickly decides which responses are viable. It seems inevitable that someone will build a set of federated models where a GPT-like front end "understands" that the user has a problem best forwarded to one of N downstream systems. Those downstream systems execute behind the scenes, and return to the federator model to recompose its answer in a human-friendly format.

I imagine a near future where N specialized LMs spring up from different creators, some built from scratch and others on top of GPT, along with a federator model that can decide which of those LMs are the best candidates to route questions to. If the federator thinks the question is answerable with basic math, it might [drop to a calculator or a python interpreter](https://arxiv.org/abs/2302.04761); if the question requires a more complex computational answer, it might send it to Wolfram's model. A query asking for a cryptic short story about corgis could be sent to a model trained on internet memes, but fine-tuned on Borges or Calvino[^1].

Federated search is a very well understood problem, already at the core of Google, Bing, Siri, and many other services. Today, both the federator and the specialized indices are owned by the same company, and the internal services are not exposed to end-users. These companies are likely rebuilding their internal services to use more LMs as we speak. But that's where [Coase's theorem](https://www.investopedia.com/terms/c/coase-theorem.asp) kicks in, and the lower transaction costs can lead to unbundling. Building those indices and exposing them via APIs will continue to get cheaper, and as soon as the cost isn't prohibitive an opportunity opens up.

The best federator might win by virtue of their UX when re-assembling answers and presenting them to the user, or by figuring out how to deal with privacy, masking your data while still getting you good answers. Maybe, their ranking model will take your preferences into account, ranking higher those services and websites which you have configured to trust more. This is reminiscent of [Albert Wenger's idea of bot representation](https://continuations.com/post/172413445510/we-need-mandatory-enduser-apis-for-social-and), but in the version laid out here users take control of their search engine’s personalization strategies instead of that of their news feed.

As Wolfram implies, building "one model to rule them all" is a stupid goal, so why not let a thousand flowers bloom and create a unifying view that knows when it is best to ask each one? Whoever builds such a system will become a front-end router with market power, analogous to app stores for the previous wave of technological innovation: a front-end to specialized compute experiences. The business model is unclear, but it could work by taking fees on a per call basis, setting up a pay-to-play model, or even decentralizing and skimming off a protocol. All of these imply tradeoffs to the user experience, but ultimately the quality of the information surfaced should crown a winner.

_Thanks to Hannah Doherty, Max Faingezicht, Pete Huang and Perry Wang for their feedback on early drafts of this post._

<hr>
<small><em>Photo: Clay Ornaments, by me. Previously posted on [Oaxaca](/photos/2023/02/13/oaxaca/).</em></small>

[^1]: Of course, I asked ChatGPT to write this for me. Enjoy:

	> In a small town nestled among rolling hills and misty moors, there existed a pack of corgis that captivated the imagination of all who beheld them. Some whispered that the corgis were descendants of a long-lost tribe, while others speculated that they were a product of some peculiar experiment gone awry.
	> One day, as the sun began to set over the fields, the corgis gathered in a circle and began to bark in unison. At first, their barks were random and chaotic, but as the minutes ticked by, they fell into a rhythm that seemed almost musical.
	>
	> A passerby who stumbled upon the scene could not believe his eyes. Was he witnessing a sacred ritual, or some sort of secret language only known to the corgis themselves?
	>
	> Suddenly, a single corgi leapt into the center of the circle and began to dance. Its movements were like a kaleidoscope, each twist and turn revealing a new facet of its being. The other corgis watched in awe as the dance continued, each movement more intricate and beautiful than the last.
	>
	> In that moment, the pack of corgis had transcended the boundaries of mere canine existence. They had become something greater, something mystical and profound. And when it was over, the corgi collapsed to the ground, panting but triumphant.
	>
	> The passerby, unable to shake the image from his mind, later wrote a treatise on the nature of reality, weaving in the corgis as a central theme. For in that brief moment, the corgis had unlocked a secret truth that eluded even the greatest philosophers and sages.
