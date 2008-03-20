#
# pyprintenv.py - printenv(1) core functionality
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

import os

def pyprintenv(var=None):
	if var:
		if os.environ.has_key(var):
			return (os.environ[var], 0)
		else:
			return ("", 1)
	else:
		retval = ""

		for (key, val) in os.environ.items():
			retval += "%s=%s\n" % (key, val)

		return (retval.rstrip(), 0)
