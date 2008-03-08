#
# pygroups.py - groups(1) core functionality
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
# Author: David Cantrell <dcantrell@redhat.com>
#

import pwd
from pycoreutils.pywhoami import pywhoami

def pygroups(userlist=None):
	header = False
	ret = []

	if userlist is None:
		userlist = [pywhoami()]

	if len(userlist) > 1:
		header = True

	for user in userlist:
		try:
			(
		except KeyError:
			ret.append("id: %s: No such user" % (user,))

id: 500: No such user


	return userlist
