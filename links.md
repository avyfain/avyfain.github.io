---
layout: page
title: Links
---

{% for post in site.categories.links %}
<div class="post">
    <h2 class="post-title">
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
    </h2>
    {% for article in post.articles %}
    <ul>
      <li>
        <a href="{{ article.url }}">
          {{ article.title }}
        </a>
      </li>
    </ul>
  {% endfor %}
</div>

{% endfor %}