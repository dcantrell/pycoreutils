#
# pytee.py - tee(1) core functionality
# Copyright (C) 2007  David Hilley <davidhi@cc.gatech.edu>
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

import os, sys

def openfile((fname, append)):
	mode = ("wb", "ab")[append]
		
	if fname == "-":
		return sys.stdout
	else:
		f = None
		try:
			f = file(fname, mode, 0)
		except IOError, ioe:
			sys.stderr.write("tee: %s: %s\n" % (fname, ioe.strerror))
		return f

def pytee(files, append=False):
	files = [(f, append) for f in files]

	sys.stdin = os.fdopen(sys.stdin.fileno(), "rb", 0)
	sys.stdout = os.fdopen(sys.stdout.fileno(), "wb", 0)
	
	openfiles = filter(None, map(openfile, files))

	stdin_fd = sys.stdin.fileno()

	while True:
		s = os.read(stdin_fd, 1024)
		if s == "":
			break
		for f in openfiles:
			f.write(s)

	return 0
