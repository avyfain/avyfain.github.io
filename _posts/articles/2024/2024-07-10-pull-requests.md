---
title: "Effective Code Reviews: Align your team and ship better code"
main_image: cdmx2/previews/17.jpeg
layout: post
category: articles
tags: [management, startups, jobs, technology, software engineering, programming]
description: The pull request review process introduces a lot of friction in the development cycle but serves multiple purposes, including knowledge sharing, code quality, and team alignment. It is a worthwhile investment.
---

<small><em>Este ensayo también está disponible [en español](/articles/2024/07/10/pull-requests-es/).</em></small>

The essay below is a slightly edited version of a document I wrote for my team at Vouch back in 2021 as we scaled the data engineering function. It's a guide to writing good pull requests, and how to review them constructively. The patterns are general enough that they should fit any team, not just one focused on data efforts. The pull request review process introduces a lot of friction in the development cycle but serves multiple purposes, including knowledge sharing, code quality, and team alignment. It is a worthwhile investment.

<hr>

**First things first - what even is a PR, and what's the purpose of reviewing them?**

A PR is a "pull request." Opening a PR is a way to ask (request) that the maintainers of a project bring in (pull) a set of code changes into a project's repository. PRs are sometimes also called "[merge requests](https://stackoverflow.com/a/36666408)."

When an author opens a PR, one or multiple reviewers will go over the proposed changes and share their feedback on what should be updated before the code can be merged. The authoring developer can then respond to the critique, revise their work, and request another review. The cycle repeats a few times until the reviewer is comfortable with the proposal and approves the PR. This iterative review process is how we ensure we have shared understanding of our systems while keeping the bar high on code quality.

**What makes a good PR?**

A good pull request represents one logical piece of work. At times, especially in large projects the people reviewing PRs can have little context on how a proposed change will work, so including a concise summary of what is the intended effect is necessary. Discussion about the problem to be solved should happen in the ticketing sytem, and ideally should happen before any code is written. Discussion about the implementation that solves said problem should live in the PR. Your tickets should tell the "why" and the "what" while your PRs are the "how."

Ideally, the proposed changes are small, and the PR includes tests that prove the proposed fix is effective, or that the feature works as expected. If there are pieces of the proposed logic that you are unsure about as an author, or which can't easily be tested, make sure to call that out. This is a good opportunity for reviewers to help authors think through the problem.

Often, PRs clean up or fix other issues that were present in the files that they touch. This is ok, and in fact encouraged, but if those changes go past a few additional functions or class updates it might make sense to split the PR into two - one for the feature you were supposed to be working on, and another one for the clean up work, especially if the PR's scope creeps.

Reviewing other people's work takes time and effort. A good PR makes it easy on the reviewers to understand what you're changing.

**So what's my role and what's the reviewer's?**

As the author opening a PR, you are responsible for seeking out reviews and shepherding the PR to its merge. Reviewers are accountable for code quality and standards. Authors are responsible for ensuring changes work as intended.

It's important to balance quality and delivery, ensuring that we don't aim at perfection but instead ship code that's "good enough." The interaction between you and the reviewers keeps that balance. As the author, you should push back when it makes sense. If the reviewer's requested changes seem too large or unrelated, open new tickets in the backlog and avoid scope creep. If there's a disagreement over logic, find a second reviewer.

As a reviewer, it’s important to focus on the high level goals first. Avoid nitpicking. If you have many comments, be clear about what changes are absolutely necessary and what's "nice to have." Some teams might include prioritized lists on their PR checklists to guide this process.

Reviews normally take a couple of cycles. Don't expect to merge your code as it was on the first push. After you've addressed a round of comments, you should re-request review and explicitly ask for more feedback.

**Is your code ready for review and merge?**

Tools like Github or Bitbucket have features tailored to reviewing code changes, so often authors will open draft pull requests as a way to share their ideas before they are ready to merge into the shared repository. It is important that work that's half-baked is marked as such, and you can do that when opening a PR.

Similarly, if there are adjacent changes that need to happen in other systems (think PRs in other repositories, or configuration of upstream/downstream components) you should mention those so that reviewers understand the scope of your change. Often, teams will use labels, checklists, or other mechanisms in their version control service to denote this.

Most mature repos will have some level of continuous integration (CI) checks that run automatically when a PR is open. The fact that CI checks are green doesn't necessarily mean that your code is good – you might be introducing changes that CI can't catch yet. If CI goes red you could be hitting a false negative – maybe you have to update the tests, or potentially you're hitting an unrelated problem. As the developer, you're responsible for both types of errors.

It is possible to get approval before CI goes green. In this case, use your judgment and re-request reviews when updates needed to get CI to pass required significant changes.

If merging your PR leads to an expected positive change, great! If merging your PR leads to breaking the build or unexpected problems, you're on the hook to resolve those problems. If you merged something that didn't work as expected, and things get out of hand, you should work with your team to correct that. Generally, you should favor rolling forward with a fix rather than rolling back to a previous state.

**Anything else?**

Remember that reviews are great opportunities to learn from each other.

The critique we give and get in PR reviews are about people's work, not about people. We all have opinions about code and how things should work. Stay kind and respectful.

<hr>
<small><em>Photo: Déjalo Ir, by me. Previously posted on [CDMX, Dos](/photos/2022/12/16/cdmx2/).</em></small>
