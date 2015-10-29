---
layout: page
title: Projects
---

<ul>
{% for post in site.categories.projects %}
<div class="post">
    <h2 class="post-title">
      <a href="{{ post.url }}">
        {{ post.title }}
      </a>
    </h2>

    <span class="post-date">{{ post.date | date: "%B %-d, %Y" }}</span>
    {% if post.main_image %}
      <img src="{{ site.image_path}}{{ post.main_image }}" alt="{{post.title}}"/>
    {% endif %}
    <p>{{ post.description }} 
    <a href="{{ post.url }}">
      ...continue reading.
    </a></p>
  </div>
{% endfor %}
</ul>