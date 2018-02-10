---
layout: post
title: Decision Tree Implementation in Python
description: A simple implementation of the ID3/C4.5 algorithm in vanilla Python.
main_image: DT/DT.jpg
tags: [programming, python, machine learning, nu project]
category: articles
permalink: projects/:year/:month/:day/:title/
---

Decision trees are an amzingly simple way to model data classification. This is an implementation of a [ID3](https://en.wikipedia.org/wiki/ID3_algorithm)/[C4.5](https://en.wikipedia.org/wiki/C4.5_algorithm) hybrid algorithm. The basic idea behind the model is to recursively cut the available data into two parts, maximizing information gain on each iteration.

Built for professor Doug Downey's [Machine Learning course](http://www.cs.northwestern.edu/~ddowney/courses/349_Winter2014/) at Northwestern University. More info on the assignment can be found [here](http://www.cs.northwestern.edu/~ddowney/courses/349_Winter2014/pset2.html).

This was one of the first complex CS projects I worked on, which is evident by reading my sloppy code. You can find the implemantation [here](https://github.com/avyfain/decisionTree).