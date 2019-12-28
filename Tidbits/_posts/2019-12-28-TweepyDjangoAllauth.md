---
layout:     post
title:      Tweepy with Django-Allauth
date:       2019-12-28 16:17:08 -0500
modified:   2019-12-28 16:17:08 -0500
version:    0
categories: Tidbits
tags:       [howto, python, tweepy, django, allauth, web frameworks, programming]
excerpt:    I have been experimenting to see which web framework would make the better 
            wrapper for Tweepy.  I decided on Django, with the Allauth package.
slug:       howto-tweepy-django-allauth
---

<img src="/assets/img/tweepy.org.png" alt="IMAGE" width="350"/>
<img src="/assets/img/djangoallauth.jpg" alt="IMAGE" width="350"/>

I have spent a good portion of this year developing Twitter software.  Some of it is 
for research, account maintenance, and retweeting.  Now, I am ready to put some of 
what I developed online, for public use.

I had been learning the Flask web framework, but it seemed inadequate for what I 
wanted to do--namely keep user data private (including API keys).  For the last month 
or so, I have been banging-out Django code, mostly from tutorials.  In fact, it prompted 
me to write a utility script for customizing Django's `settings.py` file to my 
preferences.

Anyway, after much research and reading of code, I have grown to like the [Django-Allauth 
package][djangoallauth].  It handles the cration of user accounts and managing sessions quite nicely, and
should I decide to deploy APIs on any of other social networks that it handles, I suspect 
integrating them will be quite similar.

Once I figured-out what it was that I needed to do to get what I want, it was relatively 
simple, as can be seen in the the `utils.py` file that I added to the [Django-Allauth 
Tutorial][allauthtut].  And giving credit where due, I borrowed some of the code from 
the [DjangoTweepy][djangotweepy] repository on GitHub.

Here is the code:
{% gist 0014a2fff7d8d5d08d9f8679df3d6131 %}


The utility script that I wrote for updating the Django `settings.py` file can be found 
here:
{% gist 3264ab36209c149d15e63fc8816fcdd6 %}


[allauthtut]:       https://wsvincent.com/django-allauth-tutorial/
[djangoallauth]:    https://django-allauth.readthedocs.io/en/latest/
[djangotweepy]:     https://github.com/martinjc/DjangoTweepy/blob/master/src/twitter_auth/utils.py

