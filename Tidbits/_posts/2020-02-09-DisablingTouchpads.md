---
layout:     post
title:      Disabling Laptop Touch Devices
date:       2020-02-09 10:25:01 -0500
modified:   2020-02-09 10:25:01 -0500
version:    0
categories: Tidbits
tags:       [howto, bash, touchpad, laptop, linux, macos, osx, unix, bashrc]
excerpt:    Script to toggle laptop touch devices ON/OFF
---

When I set up a new laptop, I add commands to toggle the on-board touchpad ON/OFF.  I don't permanently disable it 
because there are times when a mouse is not available.

The laptop I just setup has a touchpad and a "touch stick."  This presented a challenge--how to put multiple commands in 
a single BASH alias, to disable both at the same time.

My solution is as follows:

{% gist 9b1952153c7e59f20296e5aaa6880a90 %}

