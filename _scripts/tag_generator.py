#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tag_generator.py - Tuesday, November 19, 2019
"""
Generate tags in Jekyll blog hosted on GitHub Pages
(This was inspired by the article at http://longqian.me/2017/02/09/github-jekyll-tag/,
but it turned-out to be a real mess.  I deleted everything except this script.
"""
__version__ = '1.1.3'

from datetime import datetime, timedelta, timezone
from tzlocal import get_localzone
from glob import glob
from os.path import abspath, exists, expanduser, expandvars, join
from xdg import XDG_CACHE_HOME, XDG_CONFIG_HOME, XDG_DATA_HOME
import argparse, os, sys


def main(args):
	for arg in args.BLOG_DIRS:
		blog_dir = abspath(expandvars(expanduser(arg)))
		if not exists(blog_dir):
			raise IOError("Unable to locate '%s'" % args.BLOG_DIRS)
		os.chdir(blog_dir)
		# Find blog posts
		post_files = glob('**/_posts/*md', recursive=True)
		tags = []
		for p in post_files:
			print(' ', p)
			tags.extend(extract_tags(p))
		generate_tag_files(blog_dir, tags)
	return


def generate_tag_files(blog_dir, tags):
	tags = list(set(tags))
	tag_dir = join(blog_dir, 'tag')
	# Housekeeping
	os.makedirs(tag_dir, exist_ok=True)
	for match in glob(tag_dir + '*.md'):
		os.rename(match, match + '~.1')
	for tag in tags:
		filename = join(tag_dir, tag + '.md')
		lines = [
			'---',
			'layout: tagpage',
			'title: "Tag: %s"' % tag,
			'tag: %s' % tag,
			'robots: noindex',
			'---',
		]
		lines = [x + '\n' for x in lines]
		with open(filename, 'wt') as tagfile:
			tagfile.writelines(lines)
	print("Tags generated, count", len(tags))
	return


def _parse_args(args):
	parser = argparse.ArgumentParser(description=__doc__, add_help=False,
	                                 epilog='epilog')

	parser.add_argument('BLOG_DIRS', nargs='+')
	return parser.parse_args(args)


def _load_user_conf():
	if not XDG_CONFIG_HOME:
		raise FileNotFoundError("Unable to locate user config directory (This is for develpment use only")
	user_conf_filename = join(XDG_CONFIG_HOME, 'tag_generator.conf')
	with open(user_conf_filename, 'rt') as confile:
		user_args = [x.strip() for x in confile.readlines()]
	return user_args


def extract_tags(filename):
	tags = []
	with open(filename, 'rt') as blogfile:
		inside_header = False
		for line in blogfile.readlines()[:20]:
			line = line.strip()
			if line == '---':
				inside_header = not inside_header
			if inside_header:
				if not line.startswith('tags:'):
					continue
				tags = line.split()[1:]
				for tag in tags:
					if tag.endswith(','):
						print("Fix This:", tag)
			else:
				# print("Unable to locate Jekyll header in '%s'" % filename, file=sys.stderr)
				break
	print("    Tags:", tags)
	return tags


def init():
	print("Run Start: %s" % _run_dt)
	return


def eoj():
	print("Run Stop : %s" % datetime.now(tz).replace(microsecond=0))
	return


def local_to_utc(dt, naive=True):
	if dt.tzinfo is None:
		raise ValueError("Missing time zone")
	if type(dt) is not datetime:
		raise TypeError("Expected datetime value")
	dt = dt.astimezone(timezone.utc)
	if naive:
		dt = dt.replace(tzinfo=None)
	return dt


def debug_breakpoint():
	pass
	return


if __name__ == '__main__':
	tz = get_localzone()
	_run_dt = datetime.now(tz).replace(microsecond=0)
	_run_utc = local_to_utc(_run_dt)
	_fdate = _run_dt.strftime("%Y-%m-%d")

	# init()
	main(_parse_args(_load_user_conf() + sys.argv[1:]))
	# eoj()
