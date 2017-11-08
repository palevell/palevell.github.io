---
layout: post
title:  "Disaster Recovery"
date:   2017-11-08 08:44:19 -0500
categories: sysadmin, linux, backups, apt-get
---
{: style="float: right"}
![IMAGE](/images/disaster-recovery-180.jpg)

It has been a crazy month.  I've been tracing the source of an intermittent issue that causes the hard drive on one of my laptops to go into **read-only** mode.  While tracing this, an Ubuntu distribution update saw fit to remove the GUI, and all software packages that explicity depended on it.

### Read-Only Filesystem
This seems to be a bug in the Ubuntu kernel, going back **nine (9) years**.  In recent years, it seems to affect solid-state drives (SSDs) more than traditional hard drives (ie. SATA, SCSI, etc.).  It makes me wonder if it is related to the size/capacity of the disk.  In other words, does it only affect bigger hard drives?  If so, could a work-around be using smaller disk partitions?

In the meantime, I have gotten used to entering `fsck -f -C /dev/sda1` at the `initramfs>` prompt, which appears after being forced to reboot, after Ubuntu remounts the boot partition  in read-only mode.

{: style="float: right"}
![IMAGE](/images/ubuntu-logo-small.png){:width="180px"}

### Ubuntu Dist-Update Removed GUI

My laptop automatically updates most of its software.  For operating system updates, the commands look like the following:

	`sudo apt-get update && sudo apt-get upgrade && sudo apt-get dist-upgrade`

The above command chain fetches the package index, installs updated packages, and then checks for kernel updates.  A few weeks ago, an error notification appeared from `dist-upgrade`.  When I investigated, it showed a bunch of packages were going to be removed (over 350).

I remembered reading that Ubuntu was retiring the *Unity* desktop, and returning to the `Gnome` desktop.  I expected the incoming update was doing this.

I was wrong.

Ubuntu's `dist-upgrade` command removed the GUI, and dependent programs (including my backup program).  This left me with a text-only operating system, from which I had to restore my system from my backups, **without** my backup program.

I was dumbfounded.  This was a hostile action by Ubuntu's update system.  Who is responsible for approving this update to be released?

{: style="float: right"}
![IMAGE](/images/button_restore2xipad.png){:width="180px"}

### Restoring my System
My backups are stored on a Network Area Storage device (NAS).  The first attempt at restoring my system did not go well.  It broke symlinks and wreaked havoc with file permissions.  

I ended-up using my Ubuntu installer DVD, and installing the backup program from there.  Because the symlinks and permissions were already in chaos, I had to devise a way to get them back.

##### Python to the Rescue

The backup program is written in Python and stores file permissions in a separate file.  I was able to piece together some Python scripts that restored the symlinks and permissions from the backup.  This took a few tries, because `dist-upgrade` installed a new Linux kernel which had to be rolled-back, and the broken symlinks made the laptop unbootable, to the point that I couldn't even install a fresh version of Ubuntu on a separate partition.

### Success!
I got my system back, without losing any files.

### Lessons Learned
- dist-upgrade
	- Canonical can no longer be trusted to release 'safe' distribution updates
	- Read the changelog when issues arise, before making changes
- read-only filesystem
	- Reducing the size of the boot partition doesn't seem to have resolved the issue
	- User data seems to no longer affected, because the `/home` directory now has a separate partition
	- This seems to occur most often at 7:00am, when either Ubuntu or Python updates are attempted