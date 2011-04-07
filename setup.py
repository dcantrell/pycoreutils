# setup.py for pycoreutils
#
# Copyright (C) 2011  David Cantrell <david.l.cantrell@gmail.com>
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

import glob
import os
from distutils.core import setup
from distutils.core import Extension

setup(name='pycoreutils',
      version='0.1',
      author='David Cantrell',
      author_email='david.l.cantrell@gmail.com',
      url='https://github.com/dcantrell/pycoreutils',
      description='Python reimplementation of GNU coreutils',
      license='GPLv2+',
      ext_modules=[Extension('pycoreutils',
                             glob.glob(os.path.join('pycoreutils', '*.c')))],
      scripts=glob.glob(os.path.join('src', '*')))
