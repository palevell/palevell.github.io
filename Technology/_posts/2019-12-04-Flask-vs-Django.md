---
layout:     post
title:      Flask-vs-Django
date:       2019-12-27 05:01:59 -0500
modified:   2019-12-29 08:35:00 -0500
published:  true
version:    0
categories: Technology
tags:       [django, flask, python, web frameworks, programming]
excerpt:    After working with Flask for over a year, I am finding 
            Django to be much more to my liking.
slug:       flask-vs-django
---

![IMAGE](/assets/img/flask-vs-django.png){: .center-image}

1.  I used the [Flask][flask] web framework, first.
    -   Miguel's [Flask Mega Tutorial][flaskmega] is a great way to learn Python
    -   A few quick [web searches][vssearch] for Django vs. Flask articles 
        indicated that Flask was the way to go.
    -   When I got to the data encryption part of my app, Flask was a 
        disaster.  I encountered abandoned modules and tutorials that 
        don't work--more so than usual for the Python community (I have 
        a separate rant on that).
2.  I am working through the Django [Getting Started][djangostart] tutorial, and 
    I love it.
    - The admin page is well-integrated into the database functionality
    - The admin shell is a handy tool for keyboard warriors
3.  I have worked through a few other Django tutorials, covering things like 
    the following:
    - Authentication Templates (login pages)
    - Social logins (ie. OAuth with Twitter, GitHub, Facebook, etc.)
    - HTML templates
    - [Bootstrap][bootstrap] (I have to mention this because 
      [one tutorial][authexample] covered this particularly well)
4.  Social login is central to my Twitter projects.  As such, it is something I have 
    researched extensively while comparing Flask and Django.  Offerings range from 
    home-brewed solutions to code libraries that are actively maintained.  Popular 
    Django libraries include the following:
    - [django-allauth][allauth]
    - [django-oauth-toolkit][toolkit]
    - [python-social-auth / social-auth-app-django][pysocialauth] (formerly [django-social-auth][socialauth])
5.  [Tweepy][tweepy] can also be used to authenticate, as can be seen in the following 
    tutorial and example:
    - [Tweepy Authentication & Authorization Tutorial][tweepyauth]
    - [DjangoTweepy][djangotweepy]

    These are fine for single-user applications, but need to be wrapped in extra code 
    for a multi-user application.

### Conclusion

What finally convinced me that Django was the better option was being able to get 
Tweepy working the way I wanted with Django, faster than in Flask.  I am sure I could 
get Flask to do what I wanted, but isn't the whole  point of these frameworks to make 
life easier?  From what I have seen, Django  handles sessions (*read: user data*) 
better than Flask.

Flask is okay for spinning up small or local servers that don't store sensitive 
information (aka. secrets).  For projects that handle secrets or have complex data 
models, Django seems to be the better option.  The [Django Project's][django] tagline 
of *"The Web framework for perfectionists with deadlines"* seems appropriate.


[allauth]:      https://django-allauth.readthedocs.io/en/latest
[authexample]:  https://youtu.be/60GTvKCuam8
[bootstrap]:    https://getbootstrap.com
[django]:       https://www.djangoproject.com
[djangostart]:  https://docs.djangoproject.com/en/3.0/intro
[djangotweepy]: https://github.com/martinjc/DjangoTweepy
[flask]:        https://palletsprojects.com/p/flask
[flaskmega]:    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
[toolkit]:      https://django-oauth-toolkit.readthedocs.io
[pysocialauth]: https://python-social-auth.readthedocs.io
[socialauth]:   https://github.com/omab/django-social-auth
[tweepy]:       http://www.tweepy.org
[tweepyauth]:   http://docs.tweepy.org/en/latest/auth_tutorial.html
[vssearch]:     https://duckduckgo.com/?q=django+vs+flask+2019


