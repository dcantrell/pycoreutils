#
# pysleep.py - sleep(1) core functionality
# Copyright (C) 2007  Chris Lumens <clumens@redhat.com>
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

import re
import time

def pysleep(timespec):
	secs = 0
	suffix = 's'

	m = re.match("^([0-9]+(\.[0-9]+)?)([smhd])?$", timespec)

	if m is None:
		return 1

	secs = float(m.group(1))
	suffix = m.group(3)

	if suffix == 'm':
		secs *= 60
	elif suffix == 'h':
		secs *= 60*60
	elif suffix == 'd':
		secs *= 60*60*24

	try:
		time.sleep(secs)
	except KeyboardInterrupt:
		return 258

	return 0
