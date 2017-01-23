---
title: "The Descriptor Protocol, and Python Black Magic"
main_image: Witch.jpg
tags: [programming, python]
layout: post
category: articles
description: Trying to make sense of what is perhaps the most basic behavior of objects and classes in Python.
permalink: /projects/2016/04/26/python-black-magic/
---

Late last night, I saw a very confusing tweet:

<blockquote>
    {% highlight python %}
    class A:
        def b(self):
            pass

    if A.b is A.b:
        print("Python 3")
    else:
        print("Python 2")
    {% endhighlight %}
    &mdash; Jake VanderPlas (@jakevdp) <a href="https://twitter.com/jakevdp/status/724827419132178433">April 26, 2016</a>
</blockquote>

Like any self-respecting programmer, the first thing I did was copy paste that into a terminal, even though I knew exactly what to expect. My response was simple:

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr"><a href="https://twitter.com/jakevdp">@jakevdp</a> what is this black magic!?!?</p>&mdash; Avy Faingezicht (@avyfain) <a href="https://twitter.com/avyfain/status/724832373678952449">April 26, 2016</a></blockquote>

Since I graduated last summer, I have been writing lots of both Python 2 and 3. This snippet seemed like something I should understand well. However, I did not, so this post is an attempt to solve that. I was inspired by [Julia Evans](http://jvns.ca), and her campaign to share the things she learns, however incomplete her understanding might be.

This post assumes you have at least a basic understanding of Python and OOP. For a good overview of OOP in Python, I recommend Leonardo Giordani's [series](http://blog.thedigitalcatonline.com/blog/2014/08/20/python-3-oop-part-1-objects-and-types/) which builds up nicely from simple concepts to the internals of Python classes (he also has one [on Python 2.x](http://blog.thedigitalcatonline.com/blog/2014/03/05/oop-concepts-in-python-2-dot-x-part-1/), although I haven't read it closely).


## So, what is this black magic?
My first instinct was to check the behavior of the comparison itself. While `==` delegates to an object's `__eq__` method to check **equality**, the `is` keyword checks **identity**, so those objects can't be the same in memory!

{% highlight python %}
# Python 2
>>> A.b
<unbound method A.b>
>>> hex(id(A.b))
'0x1006ebc80'
>>> hex(id(A.b))
'0x1006beb90'

# Python 3
>>> A.b
<function A.b at 0x101b75158>
>>> hex(id(A.b))
'0x101b75158'
>>> hex(id(A.b))
'0x101b75158'
{% endhighlight %}

As expected! The memory locations (as given by `id`) in Python 2 are different, causing the identity check to fail. Not so in `3`. So far so good. But why do we get `unbound method` on one end and `function` on another? How are these objects even stored internally? In most cases, Python uses a dictionary, accessible under `__dict__` to store the local variables, or _namespace_ of an object (Note that not all objects have a `__dict__`, but that is a different story). Let's look up `b` in `A`:

{% highlight python %}
# Python 2
>>> A.__dict__['b']
<function b at 0x1007a8398>
>>> type(A.__dict__['b'])
<type 'function'>
>>> type(A.b)
<type 'instancemethod'>

# Python 3
>>> A.__dict__['b']
<function A.b at 0x101b75158>
>>> type(A.__dict__['b'])
<class 'function'>
>>> type(A.b)
<class 'function'>
{% endhighlight %}

Huh? In `2` we get an `instancemethod`, while `3` spits out a function, but if we check the `type` inside the enclosing `__dict__` we see they are *both functions*? How does this work? This is caused by the design of the [Descriptor Protocol](https://docs.Python.org/2/howto/descriptor.html), which defines how data in an object is reached through a series of attribute accesses. In Python 2, the protocol sets in place a `type` distinction based on _how_ the function object is accessed. In the doc, Raymond Hettinger explains:

{% highlight python %}
# Python 2
>>> class D(object):
...      def f(self, x):
...           return x

>>> d = D()
>>> D.__dict__['f'] # Stored internally as a function
<function f at 0x00C45070>
>>> D.f             # Get from a class becomes an unbound method
<unbound method D.f>
>>> d.f             # Get from an instance becomes a bound method
<bound method D.f of <__main__.D object at 0x00B18C90>>
{% endhighlight %}

In 3, this distinction between `bound` and `unbound` doesn't exist, but strangely, the [docs for Python 3](https://docs.python.org/3/howto/descriptor.html) are not up to date, so I can't tell what the underlying behavior is. The same code clearly has a different output:

{% highlight python %}
# Python 3
>>> class D(object):
...     def f(self, x):
...           return x

>>> d = D()
>>> D.__dict__['f'] # Stored internally as a function
<function D.f at 0x1014021e0>
>>> D.f             # Get from a class becomes an unbound method... NOT!
<function D.f at 0x1014021e0>
>>> d.f             # Get from an instance becomes a bound method
<bound method D.f of <__main__.D object at 0x10123cf28>>
{% endhighlight %}

Also explained in the documentation is the fact that both `bound` and `unbound` methods are backed by the same C implementation, except for the value of their `im_self` attribute, which is _NULL_ when unbound. So I am guessing that`instancemethod` is creating a new instance of the function object at runtime in `2` regardless of whether it is bound or unbound, while in `3` the instantiation only happens when `bound`, given that the `unbound`s don't exist. This would make sense, as the function must be executed each time you access it.

If that were the case, we would expect that calling `b` on an instance on A would always return a different object, regardless of which Python runtime we're on, as they are always bound:

{% highlight python %}
# Python 2&3
>>> a = A()
>>> a.b is a.b
False
>>> hex(id(a.b))
'0x1003bf988'
>>> hex(id(a.b))
'0x1003f1448'
{% endhighlight %}

So, the reason why `A.b is A.b` in Python 3, and not Python 2 is this whole bound/unbound story. Seems like the Descriptor Protocol is responsible for this sorcery! Magic is just technology we don't understand, [yet](https://en.wikipedia.org/wiki/Clarke%27s_three_laws).

If you have more insight into the inner workings of this, I'd love to [hear about it](/contact/).

**Update (4/26/16):**
Jake VanderPlas replied to my tweet, and pointed to a 2009 <a href="http://python-history.blogspot.in/2009/02/first-class-everything.html">post by Guido</a> describing the behavior. Apparently, the bound/unbound distinction was introduced as a way to achieve "first-class everything," which methods didn't quite fit into. Python 3's undoing of unbound methods is just a further expression of the idea.

**Update 2 (4/29/16):**
Today I received an email from Todd Jennings, who pointed me to [the bug](https://bugs.python.org/issue23702) that tracks the out-of-date documentation for Python 3. Sadly, it is marked as still waiting.

**Update 3 (8/22/16):**
After attending PyBay, Wesley Chun [pointed out](https://twitter.com/wescpy/status/767588995727437824) that the definition of `A` was that of a classic 2.x class, while the rest of the article used new-style classes. Changing the class definition to inherit from object (as in, `class A(object):`) doesn't change the behavior that I describe above, for either Python 2.x or 3.x. To remain true to the original tweet, I have kept the class definition without explicit inheritance, but [the distinction](https://stackoverflow.com/questions/4015417/python-class-inherits-object/9448136#9448136) is important.

<hr>
*Image: "The Witch No. 1" by Baker, Joseph E. - Licensed under Public Domain, via [Wikimedia Commons](https://commons.wikimedia.org/wiki/File%3ATheWitch-no1.jpg")*