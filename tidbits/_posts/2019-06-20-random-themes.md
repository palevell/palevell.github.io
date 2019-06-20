---
layout:     post
title:      Pelican Themes Randomizer
date:       2019-06-20 08:22:22 -0400
modified:   2019-06-20 08:24:22 -0400
categories: programming
tags:       pelican, pelican-themes, 
permalink:	/tidbits/pelican-themes-randomizer
excerpt:    This script chooses a random theme from pelican-themes--great for testing!
---

To streamline testing operations, I opted to move the theme-picker out of the pelican settings file.

With this setup, this script `random_theme` can be executed before building the site, as shown in the following example:

```bash
./random_theme ; make clean devserver
```

-- Enjoy!

<script src="https://gist.github.com/palevell/111bad0abe970095746d1d85bdde20bf.js"></script>


