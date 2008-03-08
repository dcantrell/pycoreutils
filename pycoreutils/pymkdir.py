#
# pymkdir.py - mkdir(1) core functionality
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

import os
import re
import sys
import stat
from stat import *

try:
	import selinux
except:
	print "SELinux support is not available on this system."
	sys.exit(1)

usermasks = {	'a' : 07777,
		'u' : S_ISUID | S_IRWXU,
		'g' : S_ISGID | S_IRWXG,
		'o' : S_ISVTX | S_IRWXO,}

permmods = {	'x' : S_IXUSR | S_IXGRP | S_IXOTH,
		'w' : S_IWUSR | S_IWGRP | S_IWOTH,
		'r' : S_IRUSR | S_IRGRP | S_IROTH,
		's' : S_ISUID | S_ISGID,
		't' : S_ISVTX, }

usermods = {	'u' : (S_IRWXU, 6),
		'g' : (S_IRWXG, 3),
		'o' : (S_IRWXO, 0),}

def mask_and_extend(startmode, mask, shift):
	t = (startmode & mask) >> shift
	return t << 6 | t << 3 | t

def apply_permmod(app, mask, startmode, c):
	if c in permmods:
		app |= mask & permmods[c]
	elif c == 'X' and (startmode & permmods['x']):
		app |= mask & permmods['x']
	elif c in usermods:
		app |= mask & mask_and_extend(startmode, *usermods[c])
	else:
		raise ValueError
	return app

def apply_mod(s, startmode, umask):
	m = re.compile("[+-=]").search(s)
	users, ops = s[0:m.start()], s[m.start():]
	mods = re.compile("[+-=][rwxXstugo]*").findall(ops)
	um = [usermasks[c] for c in list(users)]
	# this mask defines the scope of the series of operations
	mask = reduce(lambda x, y: x | y, um, 0)
	if um == []:
		mask = 07777 & ~umask

	result = startmode
	for m in mods:
		app = 0
		for c in m[1:]:
			app = apply_permmod(app, mask, startmode, c)
		if m[0] == '+':
			result |= app  
		elif m[0] == '-':
			result &= ~app
		else:
			result &= ~mask
                        result |= app
	
	return result

def parse_symbolic_mode(mode, umask):
	mlist = mode.split(',')
	try:
		mask = reduce(lambda x, y: apply_mod(y, x, umask), mlist, 0777)
	except:
		raise

	print mask
	return mask

def parse_mode(mode, mask):
	raw_mode = None
	try:
		raw_mode = int(mode, 8)
	except ValueError:
		# not numeric, try symbolic
		raw_mode = parse_symbolic_mode(mode, mask)

	if not raw_mode:
		sys.stderr.write("mkdir: invalid mode `%s'\n" % mode)
		sys.exit(1)

	return raw_mode

# the majority of this is taken from os.makedirs, but we can't simply
# call os.makedirs, because GNU mkdir permission semantics are
# different in two ways: 1) GNU mkdir -p makes non-leaf directories
# with a different set of permissions than leaf directories; and 2)
# GNU mkdir has the --verbose option to print out the name of each
# newly created directory
def makewithparents(name, mode, mask, verbose=False, innercall=False):
	rv = 0
	if not innercall:
		leaf_mode = mode
		mode = 0777 & ~mask | S_IWUSR | S_IXUSR
	head, tail = os.path.split(name)
	if not tail:
		head, tail = os.path.split(head)
	if head and tail and not os.path.exists(head):
		rv = makewithparents(head, mode, mask, verbose, True)
		if tail == os.curdir:		
			return 0
	if not innercall:
		mode = leaf_mode
	rv |= makeonedir(name, mode, mask, verbose, True)
	return rv

def makeonedir(d, mode, mask, verbose=False, parent=False):
	try:
		if parent and os.path.exists(d):
			if os.path.isdir(d):
				return 0
			elif os.path.isfile(d):
				sys.stderr.write("mkdir: `%s' exists "
						 "but is not a directory\n" % d)
				return 1
		os.mkdir(d, mode)
		if verbose:
			print "mkdir: created directory `%s'" % d
		return 0
	except OSError, o:
		sys.stderr.write("mkdir: cannot create directory `%s': %s\n"
				 % (d, o.strerror))
		return 1

def pymkdir(dirlist, mode, parents=False, verbose=False, con=None):
	ret = 0

	if con is not None:
		selinux.setcon(con)

	mask = os.umask(0)
	if not mode:
		mode = 0777 & ~mask
	else:
		mode = parse_mode(mode, mask)

	for d in dirlist:
		rv = (makeonedir, makewithparents)[parents](d, mode, mask, verbose)
		ret |= rv

	return ret
