#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# housekeeping.py - Thursday, November 21, 2019
""" This is modeled after the rsync get/put commands in Makefile """
__version__ = '1.0.1'

import os
from datetime import datetime, timezone
from glob import glob
from os.path import exists, getmtime, join

from tzlocal import get_localzone

source = '.'
target = join('local', 'backup')
pattern = '*~*'
days_old = 1


def main(source, target, pattern, days_old=1):
	if not exists(source):
		raise FileNotFoundError(source)
	os.makedirs(target, exist_ok=True)
	file_count = 0
	# Find backup files
	matches = glob("**/%s" % pattern, recursive=True)
	# Exclude files in 'local'
	matches = [ x for x in matches if not x.startswith(target) ]
	for match in matches:
		file_count += 1
		age = (_run_dt_naive - datetime.fromtimestamp(getmtime(match)))
		# print("%3d) %s %s" % (file_count, age, match))
		if age.days > days_old:
			new = join(target, match)
			os.renames(match, new)
	return


if __name__ == '__main__':
	_run_dt_naive = datetime.now().replace(microsecond=0)
	tz = get_localzone()
	_run_dt = _run_dt_naive.astimezone(tz)
	_run_utc = _run_dt.astimezone(timezone.utc)
	_fdate = _run_dt.strftime("%Y-%m-%d")

	main(source, target, pattern, days_old)
