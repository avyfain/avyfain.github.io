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
    {{ post.content }}
    <ul>
      {% for article in post.articles %}
        <li>
          <a href='{{ article.url }}' onclick="trackOutboundLink('{{ article.url }}'); return true;">
            {{ article.title }}
          </a></br>
        {% if article.author or article.source %}
        <small>
          {% if article.author %}
            {{article.author}}
          {% endif %}
          {% if article.author and article.source %}
          -
          {% endif %}
          {% if article.source %}
            {{article.source}}
          {% endif %}
        </small>
        {% endif %}
        </li>
    {% endfor %}
  </ul>
</div>

{% endfor %}