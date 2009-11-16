dnl configure.ac for pycoreutils
dnl
dnl Copyright (C) 2009  David Cantrell <david.l.cantrell@gmail.com>
dnl
dnl This program is free software; you can redistribute it and/or
dnl modify it under the terms of the GNU General Public License
dnl as published by the Free Software Foundation; either version 2
dnl of the License, or (at your option) any later version.
dnl
dnl This program is distributed in the hope that it will be useful,
dnl but WITHOUT ANY WARRANTY; without even the implied warranty of
dnl MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
dnl GNU General Public License for more details.
dnl
dnl You should have received a copy of the GNU General Public License
dnl along with this program; if not, write to the Free Software Foundation,
dnl Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

m4_define(python_required_version, 2.5)

AC_PREREQ(2.59)
AC_INIT([pycoreutils], [0.1], [david.l.cantrell@gmail.com])
AM_INIT_AUTOMAKE
AC_CONFIG_SRCDIR([src/basename])
AC_CONFIG_HEADER([config.h])
AC_CONFIG_FILES([Makefile pycoreutils/Makefile src/Makefile tests/Makefile])
AM_SILENT_RULES([yes])
AC_CONFIG_MACRO_DIR([m4])

AC_DEFINE_UNQUOTED([BUILD_DATE], ["`date +%m%d%Y`"], [Date of pycoreutils build])

AC_DISABLE_STATIC
AC_PROG_CPP
AC_PROG_CC

AC_HEADER_STDC

AC_PROG_LIBTOOL

dnl Check for Python
AM_PATH_PYTHON(python_required_version)
AM_CHECK_PYTHON_HEADERS(,[AC_MSG_ERROR(could not find Python headers or library)])

AC_OUTPUT
