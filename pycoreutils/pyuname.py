#
# pyuname.py - uname(1) core functionality
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

import posix

def pyuname():
	ret = {}
	(sysname, nodename, release, version, machine,) = posix.uname()

	if machine == 'i686':
		processor = machine

		try:
			f = open('/proc/cpuinfo', 'r')
			for l in f.readlines():
				if l.startswith('vendor_id'):
					if l.find('AuthenticAMD') != -1:
						processor = 'athlon'
						break
			f.close()
		except:
			pass

	platform = machine
	if platform.startswith('i') and platform.endswith('86'):
		platform = 'i386'

	# FIXME: does not support anything other than Linux right now
	opsys = sysname
	if opsys == 'Linux':
		opsys = 'GNU/Linux'

	ret['sysname'] = sysname
	ret['nodename'] = nodename
	ret['release'] = release
	ret['version'] = version
	ret['machine'] = machine
	ret['processor'] = processor
	ret['platform'] = platform
	ret['opsys'] = opsys

	return ret
