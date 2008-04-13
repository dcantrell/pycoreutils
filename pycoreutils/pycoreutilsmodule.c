/*
 * pycoreutilsmodule.c - Functionality that we cannot implement directly
 *                       in Python.
 * Copyright (C) 2007, 2008  David Cantrell <david.l.cantrell@gmail.com>
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public License
 * as published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software Foundation,
 * Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
 */

#include <Python.h>
#include <unistd.h>

static PyObject *hostid_cmd(PyObject *self, PyObject *args) {
	unsigned int id;
	char ret[9];

	id = gethostid();
	id &= 0xffffffff;
	if (sprintf(ret, "%08x", id) < 0)
		return NULL;

	return Py_BuildValue("s", ret);
}

static PyObject *sync_cmd(PyObject *self, PyObject *args) {
	sync();
	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef pycoreutilsMethods[] = {
	{ "hostid", (PyCFunction) hostid_cmd, METH_VARARGS, NULL },
	{ "sync", (PyCFunction) sync_cmd, METH_VARARGS, NULL },
	{ NULL, NULL, 0, NULL }
};

void initpycoreutils(void) {
	PyObject *m, *d;

	m = Py_InitModule("pycoreutils", pycoreutilsMethods);
	d = PyModule_GetDict(m);
}
