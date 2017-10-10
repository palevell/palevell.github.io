---
layout: post
title:  "Code Tidbit: PyLocalNow (Python)"
date:   2017-09-12 12:34:56 -0400
categories: programming timezones python
permalink: /tidbits/pylocalnow/
---

### **What is PyLocalNow?**

PyLocalNow is a [Python](https://www.python.org) module that returns a [PyTZ](http://pythonhosted.org/pytz) object containing the
local date/time and timezone, with or without nanoseconds,
using [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).(ie. **`2017-09-12 12:34:56-0400`**).

### **The Problem**

Generally speaking, support for timezone-aware applications is
inadequate.  This became painfuly obvious during my work on the
[**_iWarehouse_**](https://www.slideshare.net/slideshow/embed_code/key/iG8qiiUfafuQzU)&trade; project, while collecting data from vehicles
in over 60 countries.

In the IT world, it is common practice to store dates and times using
the Universal Time Code (UTC), often referred to as Greenwich
Mean Time, colloquially.  For user-facing applications, this isn't
always preferrable, or practical when using future dates and times.

Add to the mix that timezone support in design tools is
inconsistent across product offerings, and the need for better
"timezone-awareness" and interoperability becomes quite clear.

### **The Solution**

The ISO 8601 date/time format is a good place to start, since it is
supported my most date/time functions.  The weakness in many of them
is lack of support for "timezone awareness," by which I mean the ability
of an application to determine the timezone in which it is operating, or
that which the environment has been configured.

PyLocalNow combines the **`datetime`** and **`PyTZ`** modules into one, for
improved timezone awareness.

Development files for PyLocalNow can be viewed on GitHub at
[http://palevell.github.io/pylocalnow](http://palevell.github.io/pylocalnow).


