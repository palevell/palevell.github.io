---
layout:     post
title:      Pelican Themes
date:       2019-06-19 11:44:55 -0400
categories: gist programming python
permalink:  /tidbits/testing-pelican-themes/
excerpt:    Sample Pelican config file for testing pelican-themes
---

I have been investigating [Pelican][pelican] as a static web site generator for [Python][python].
During that time, I came across a plethora of themes in the [pelican-themes][pelicanthemes] project,
which contains over 100 themes--many of them using [Bootstrap][bootstrap].

To test them out, I modified the Pelican config file, `pelicanconf.py` to pick a random theme 
every time the site is generated, as follows: 
<script src="https://gist.github.com/palevell/6e297554f1389971988813ddd69724ef.js"></script>

The file containing the list of [pelican-themes][pelicanthemes] looks like the following:
<script src="https://gist.github.com/palevell/711a8393bde6a6462df9050b564bda09.js"></script>

[pelican]: https://blog.getpelican.com
[pelicanthemes]: http://www.pelicanthemes.com
[python]: https://www.python.org
[bootstrap]: https://getbootstrap.com



