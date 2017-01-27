---
layout: post
title: 'Wikitropolis: The Link Structure of Wikipedia'
description: Investigating the hyperlink architecture of Wikipedia by displaying the links from five major cities as three-dimensional structures.
main_image: wikitropolis/main.jpg
tags: [programming, complexity, visualization, wikipedia, nu project]
category: articles
permalink: projects/:year/:month/:day/:title
---

This past fall I had the chance to take a course called **Data as Art**, which paired up Northwestern University engineering students with artists from the School of the Art Institute of Chicago (SAIC) to pursue a data-driven art project. I saw the class as an opportunity to work on an interdisciplinary team and tackle a subject generally experienced in the abstract digital world, but expressing it in a physical form instead. The course did not only accomplish this, but in the process it also allowed me to better understand and overcome the obstacles that appear when bringing people from diverse academic backgrounds together for a common goal.

During one of the first class sessions, the faculty members told us about their research, and suggested data sets we could work with. We were given ideas to play with at the intersections of computer science with [music](http://music.cs.northwestern.edu/research.php'), [communication](http://collablab.northwestern.edu/), but the projects we would work on were completely open ended, and students were allowed to form groups based on their interests. I knew I wanted to work with Wikipedia data, and those interested in the subject gravitated towards each other as we brainstormed: how can you visualize this huge system? It had been tried [many]('http://seealso.org/) [times](http://infodisiac.com/Wikimedia/Visualizations/) before, and we wanted to do something different.

My group was particularly interested in the structure of Wikipedia, and how by using only the network formed by its hyperlinks, we could derive a proxy to explain the underlying content, and how its readers experienced it. At first, the task seemed daunting. To ground the concept in a way that most observers could relate to it, we decided to focus on the idea of the city, **as represented in Wikipedia**. Specifically, we decided to study global cities, and show what was unique about each one, as inferred by a computer algorithm from their articles' hyperlinks. The choice was arbitrary, as the same procedure could give us insights across domains if applied to different data sets (i.e., the same algorithm could have revealed patterns in any other category: books, animals, universities, etc.)

Once we established our end goal, we scraped the Wikipedia articles for over fifty global cities ranked in the "alpha" and "beta" categories of the [Globalization and World Cities Research Network Study](http://en.wikipedia.org/wiki/Global_city#Studies), and developed software to analyze them. The full article text was fed to our program, which extracted the hyperlinks in each article, and processed each one by giving them a numeric *relatedness* value, utilizing an information retrieval method called [tf-idf weighting](http://en.wikipedia.org/wiki/Tf%E2%80%93idf) (term-frequency/inverse-document-frequency).

With these scores in hand, we quickly honed in on a visual that would allow us to communicate the importance of each hyperlink to its parent article: screenshots of the Wikipedia articles for each of the selected cities, but with the text whited out, and its images blurred, putting all the attention on the links. To accentuate the idea of uniqueness, we mapped each link’s score to a palette of blue hues in the printout. Darker colors meant higher tf-idf values. For example "Millenium Park" or "The L" are uniquely relevant to Chicago, so they are dark blue, but the links to "Park" or "Transportation System" appear in many different cities, and they would appear in the lighter colored blue tones.

![tokyo]({{ site.image_path}}wikitropolis/tokyo.png)
<small>Partial renderings of the prints for the Tokyo tower.</small>

With the visual representation of the data defined, we had to decide on the form in which we would present it, and the team was set on the idea of having very well defined physical objects. Our final result was a collection of **four-sided pillars**, with printouts of the whited-out Wikipedia articles for **New York, Chicago, London, Tokyo and Paris** attached on their front and back, and a different layout on their two sides, showing the links sorted by their scores, and forming a color gradient, which provided a non-didactic explanation of the content of our pieces. The skyline shape of the towers inspired the project's name: **Wikitropolis**.

![ford]({{ site.image_path}}wikitropolis/ford.jpg)
<small>The exhibit opening at the Ford Engineering Design Center.</small>

For someone who is used to working in the digital medium, building the pillars was quite a challenge. The cost of iteration when working in the digital world is minimal (you refresh your browser and things have changed) but this was not the case for the physical towers we built. Everything, from choosing the materials, deciding on sizes, and even printing the designs, required tremendous attention to detail. Even though we had ups and downs, as we learned to measure twice and cut once during the design process, our project was a success and our piece caught a lot of attention.

Our artwork, together with the other three teams' pieces, was exhibited at a gallery at SAIC for two weeks at the beginning of December, and this Friday marks the end of its month long stint at the Ford Engineering Design Center at Northwestern. I couldn’t be more proud of my team’s achievement.

<img src="{{site.image_path}}wikitropolis/team.jpg" />
<small>The team at the SAIC exhibit. From left to rigth: Kevin, Leon, myself, Paola and Ryan.</small>

The projects were covered by the McCormick School of Engineering's magazine, [here](http://www.mccormick.northwestern.edu/news/articles/2014/12/schools-collaborate-to-turn-information-into-art.html). The high resolution prints can be downloaded [here](https://www.dropbox.com/sh/zaiq6fsl2xpgiw1/AACh95rF_ChOx0scBIb7uhcpa?lst).
