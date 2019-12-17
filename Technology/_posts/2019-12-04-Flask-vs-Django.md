---
layout:     post
title:      Flask-vs-Django
date:       2020-12-04 5:01:59 -0500
modified:   2020-12-17 6:34:00 -0500
published:  false
version:    0
categories: Technology
tags:       [django, flask, python, web frameworks, programming]
excerpt:    After working with Flask for over a year,
            I am finding Django to be much more to my liking.
---

**side note:**
I tried doing this in ReStructuredText, but the jekyll-rst plugin 
doesn't seem to work.  When published to the test server, the 
article link is to a `.rst` file, not HTML.  It looks like the 
repository is no longer maintained.  Maybe it's because there 
weren't many people using it (or, did Pelican come after that?)

### Outline

1.  I used [Flask][flask], first - [link][flask]
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


[flask]:        https://palletsprojects.com/p/flask
[flaskmega]:    https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
[vssearch]:     https://duckduckgo.com/?q=django+vs+flask+2019
[djangostart]:  https://docs.djangoproject.com/en/3.0/intro


**ToDo:** [Give Pelican another try](https://opensource.com/article/19/5/run-your-blog-github-pages-python)

