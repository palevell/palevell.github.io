---
layout: 	post   
title:  	PATCH - Long Tweets in youtube-dl (updated)
date:   	2020-Jan-14 11:22:33 -0500
published:	true
categories: Technology
tags: 		development youtube-dl twitter 
---

I finally had a chance to dig into this a bit further, and devised a 
more permanent fix (see the gist, below).

If you have been experiencing *'Cannot write'* errors when trying to 
download [Twitter][twitter] videos with [youtube-dl][youtube-dl], it 
could be due to the number of characters in the tweet.  Twitter now 
allows 280 characters per tweet, while many file systems have a 
255-character limit for filenames.

There is a simple patch to fix this issue, as follows:

{% gist c9781f75ca482ab406514d068ad3e639 %}

[twitter]:    https://www.twitter.com
[youtube-dl]: https://pypi.org/project/youtube_dl

