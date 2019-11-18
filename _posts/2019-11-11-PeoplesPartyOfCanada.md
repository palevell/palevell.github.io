---
layout: post
title:  People's Party of Canada
date:   2019-11-11 11:11:11 -0500
categories: Tech
tags: [PPC, Python, Tweepy, Programming]
---

Back in February, I started a research project using the 
[Tweepy][tweepy] library in [Python][python].  Around that time, the 
leader of the [People's Party of Canada][ppc] (PPC), Maxime Bernier, 
asked people to follow the accounts that he followed, and retweet their 
tweets.

That was a big job, so I wrote a Python script to create a list to 
which others could subscribe.  The next task was to isolate PPC-related 
tweets.  This was the genesis of my twitter bot.  It listens for 
PPC-related tweets from the accounts followed by Maxime Bernier.

After a while, I wrote another Python script to generate Top Tweets 
lists.  It generates daily Top Ten and weekly Top 40 lists of the most 
popular PPC-related tweets.  It also served to help PPC supporters find 
each other and relevant information.

We built a solid community on Twitter, able to dominate most threads 
and get hashtags trending.  This was particularly useful in getting the 
attention of the debate organizers.

[tweepy]:   https://pypi.org/project/tweepy
[ppc]:      https://peoplespartyofcanada.ca/?recruiter_id=964689
[python]:   https://python.org


