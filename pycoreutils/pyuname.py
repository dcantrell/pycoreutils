#
# pyuname.py - uname(1) core functionality
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
