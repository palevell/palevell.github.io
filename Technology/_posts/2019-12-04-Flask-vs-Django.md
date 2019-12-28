---
layout:     post
title:      Flask-vs-Django
date:       2019-12-04 05:01:59 -0500
modified:   2019-12-28 17:06:00 -0500
published:  true
version:    0
categories: Technology
tags:       [django, flask, python, web frameworks, programming]
excerpt:    After working with Flask for over a year,
            I am finding Django to be much more to my liking.
slug:       flask-vs-django
---

<img src="/assets/img/flask-vs-django.png" alt="IMAGE" width="350"/>

### Outline

1.  I used [Flask][flask] first - [link][flask]
    a.  Miguel's [Flask Mega Tutorial][flaskmega] is a great way to learn Python
    b.  A few quick [web searches][vssearch] for Django vs. Flask articles 
        indicated that Flask was the way to go.
    c.  When I got to the data encryption part of my app, Flask was a 
        disaster.  I encountered abandoned modules and tutorials that 
        don't work--more so than usual for the Python community (I have 
        a separate rant on that).
2.  I am working through the Django [Getting Started][djangostart] tutorial, and 
    I love it.  [link][djangostart]
    a. The admin page is well-integrated into the database functionality
    b. The admin shell is a handy tool for keyboard warriors
3.  I have worked through a few other Django tutorials, covering things like 
    the following:
    a. Authentication Templates (login pages)
    b. Social logins (ie. OAuth with Twitter, GitHub, Facebook, etc.)
    c. HTML templates
    d. Bootstrap (I have to mention this because one tutorial covered this well)
4.  What finally convinced me that Django was the better option was being able to get 
    Tweepy working the way I wanted with Django, and not Flask, in the shortest period 
    of time.  I am sure I could get Flask to do what I wanted, but isn't the whole point 
    of these frameworks to make life easier?  From what I have seen, Django handles 
    sessions (read: user data) better than Flask.  And if it comes down to how the apps 
    work, Flask loses, simply based on my experiences with pgAdmin IV.  I spent hours 
    trying to get it to work.  I scoured StackOverflow.com, looking for solutions.  
    Nothing worked.  Even today, pgAdmin IV still bombs-out.  I am pretty sure it is a 
    dependency issue--somebody forgot to list all the packages that need to be installed.  
    It doesn't matter--Adminer works, period.


[flask]:        https://palletsprojects.com/p/flask
[flaskmega]:    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
[vssearch]:     https://duckduckgo.com/?q=django+vs+flask+2019
[djangostart]:  https://docs.djangoproject.com/en/3.0/intro


**ToDo:** [Give Pelican another try](https://opensource.com/article/19/5/run-your-blog-github-pages-python)

