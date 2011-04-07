# Makefile for pycoreutils
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

PYTHON    ?= python
DESTDIR   ?= /
TESTSUITE = tests/baseclass.py

default: all

all:
	$(PYTHON) setup.py build

test: all
	PYTHONPATH=$$(find $$(pwd) -name "*.so" | head -n 1 | xargs dirname):. \
	$(PYTHON) $(TESTSUITE) -v

clean:
	$(PYTHON) setup.py -q clean --all
	[ -d .git ] && git clean -d -x -f

install: all
	$(PYTHON) setup.py install --root=$(DESTDIR)

ChangeLog:
	git log > ChangeLog

release: ChangeLog
	$(PYTHON) setup.py sdist
