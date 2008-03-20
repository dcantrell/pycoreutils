#!/usr/bin/env python
#
# uname.py - uname(1) command written in Python
# Copyright (C) 2007  David Cantrell <david.l.cantrell@gmail.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

pyunamever = (1, 0)

import getopt, sys
from pycoreutils.common import *
from pycoreutils.pyuname import pyuname
from pycoreutils.pybasename import pybasename

def main():
	prog = pybasename(sys.argv[0])
	opts, args = [], []
	all, help, version, unknown = False, False, False, False
	s, n, r, v, m, pr, pl, os = False, False, False, False, False, False, False, False
	num = 0

	val = pyuname()

	if len(sys.argv) == 1:
		print val['sysname']
		sys.exit(0)

	try:
		opts, args = getopt.getopt(sys.argv[1:], 'asnrvmpio',
		                           ['all', 'kernel-name',
		                            'nodename', 'kernel-release',
		                            'kernel-version', 'machine',
		                            'processor', 'hardware-platform',
		                            'operating-system', 'help',
		                            'version'])
	except getopt.GetoptError:
		help = True

	for o, a in opts:
		if o in ('-a', '--all'):
			all = True
		elif o in ('-s', '--kernel-name'):
			s = True
			num += 1
		elif o in ('-n', '--nodename'):
			n = True
			num += 1
		elif o in ('-r', '--kernel-release'):
			r = True
			num += 1
		elif o in ('-v', '--kernel-version'):
			v = True
			num += 1
		elif o in ('-m', '--machine'):
			m = True
			num += 1
		elif o in ('-p', '--processor'):
			pr = True
			num += 1
		elif o in ('-i', '--hardware-platform'):
			pl = True
			num += 1
		elif o in ('-o', '--operating-system'):
			os = True
			num += 1
		elif o in ('--help'):
			help = True
		elif o in ('--version'):
			version = True
		else:
			unknown = True

	if help:
		try:
			from pycoreutils.usage import pyuname_usage
			pyuname_usage(prog)
		except:
			print "Help screen is not available."

		sys.exit(0)
	elif version:
		showversion(prog, pyunamever)
	elif unknown:
		print "%s: extra operand `%s'" % (prog, sys.argv[1],)
		print "Try `%s --help' for more information." % (prog,)
		sys.exit(1)

	if all:
		print "%s %s %s %s %s %s %s %s" % (val['sysname'], val['nodename'], val['release'], val['version'], val['machine'], val['processor'], val['platform'], val['opsys'],)
		sys.exit(0)

	if s:
		sys.stdout.write(val['sysname'])

	if n:
		sys.stdout.write(val['nodename'])
		if num > 1:
			sys.stdout.write(' ')

	if r:
		sys.stdout.write(val['release'])
		if num > 1:
			sys.stdout.write(' ')

	if v:
		sys.stdout.write(val['version'])
		if num > 1:
			sys.stdout.write(' ')

	if m:
		sys.stdout.write(val['machine'])
		if num > 1:
			sys.stdout.write(' ')

	if pr:
		sys.stdout.write(val['processor'])
		if num > 1:
			sys.stdout.write(' ')

	if pl:
		sys.stdout.write(val['platform'])
		if num > 1:
			sys.stdout.write(' ')

	if os:
		sys.stdout.write(val['opsys'])

	sys.stdout.write('\n')
	sys.stdout.flush()

if __name__ == "__main__":
	main()
