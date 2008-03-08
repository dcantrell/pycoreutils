#
# pytee.py - tee(1) core functionality
#
# This copyrighted material is made available to anyone wishing to use,
# modify, copy, or redistribute it subject to the terms and conditions of
# the GNU General Public License v.2.  This program is distributed in the
# hope that it will be useful, but WITHOUT ANY WARRANTY expressed or
# implied, including the implied warranties of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
# details.  You should have received a copy of the GNU General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA. Any Red Hat trademarks that are incorporated in the source code or
# documentation are not subject to the GNU General Public License and may
# only be used or replicated with the express permission of Red Hat, Inc.
#
# Author: David Hilley <davidhi@cc.gatech.edu>
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
