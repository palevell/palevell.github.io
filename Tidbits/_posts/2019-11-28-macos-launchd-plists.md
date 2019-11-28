---
layout:     post
title:      Advanced Task Scheduling with launchd
subtitle:   with launchd & plists
date:       2019-11-28 7:33:25 -0500
modified:   2019-11-28 7:33:25 -0500
version:    0
categories: Tidbits
tags:       [osx, macos, launchd, plist, cron, scheduling]
excerpt:    Launchd day accepts arrays of date dictionaries in the 
            "StartCalendarInterval" tag of plist files
---

I recently finished a project that involved generating lists of top ten 
tweets.  It was scheduled to run twice a day, six days a week, and once 
on the day that the weekly top 40 list ran.  This was easy to do as a 
cron job, as shown below:

```
00  8	* * *	/path/to/topten.py 
00 20	* * 1-6	/path/to/topten.py 
```

Most of the examples of using `launchd` .plists only include jobs that 
occur once a day or on-demand, and the documentation doesn't make it 
clear how complex task schedules are set up.

As usual, [Stack Overflow](https://stackoverflow.com) provided a wealth 
of information, and I arrived at the following:

```xml
<key>StartCalendarInterval</key>
<array>
    <dict>
        <key>Weekday</key>
            <integer>123456</integer>
        <key>Hour</key>
            <integer>8</integer>
        <key>Minute</key>
            <integer>00</integer>
    </dict>
    <dict>
        <key>Weekday</key>
            <integer>123456</integer>
        <key>Hour</key>
            <integer>20</integer>
        <key>Minute</key>
            <integer>00</integer>
    </dict>
    <dict>
        <key>Weekday</key>
            <integer>0</integer>
        <key>Hour</key>
            <integer>8</integer>
        <key>Minute</key>
            <integer>00</integer>
    </dict>
</array>
```

As you can see, it is nowhere near as elegant as cron, but it works.  It 
reminds me of a project where we opted for CSV files over XML because 
the tags were bigger than the data.  These days, a JSON version of this 
would be nice.

The complete .plist file for scheduling this job is shown below:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>Label</key>
		<string>local.toptentweets</string>
	<key>ProgramArguments</key>
	<array>
		<string>/path/to/topten.py</string>
	</array>
	<key>StartCalendarInterval</key>
	<array>
		<dict>
			<key>Weekday</key>
				<integer>123456</integer>
			<key>Hour</key>
				<integer>8</integer>
			<key>Minute</key>
				<integer>00</integer>
		</dict>
		<dict>
			<key>Weekday</key>
				<integer>123456</integer>
			<key>Hour</key>
				<integer>20</integer>
			<key>Minute</key>
				<integer>00</integer>
		</dict>
		<dict>
			<key>Weekday</key>
				<integer>0</integer>
			<key>Hour</key>
				<integer>8</integer>
			<key>Minute</key>
				<integer>00</integer>
		</dict>
	</array>
	<key>StandardOutPath</key>
		<string>/path/to/topten.log</string>
	<key>StandardErrorPath</key>
		<string>/path/to/topten.err</string>
</dict>
</plist>
```

Hopefully, this will save somebody time trying to implement advanced 
scheduling with launchd.
