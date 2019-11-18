---
layout: post   
title:  PATCH - Long Tweets in youtube-dl
date:   2019-11-18 09:34:56 -0500
categories: development
---

If you have been experiencing *'Cannot write'* errors when trying to 
download [Twitter][twitter] videos with [youtube-dl][youtube-dl], it 
could be due to the number of characters in the tweet.  Twitter now 
allows 280 characters per tweet, while many file systems have a 
255-character limit for filenames.

There is a simple patch to fix this issue, as follows:

{% gist add67ace898d7381c6e79b5d8fa56a69 %}

[twitter]:    https://www.twitter.com
[youtube-dl]: https://pypi.org/project/youtube_dl

