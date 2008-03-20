/*
 * pysync.c - sync(1) core functionality
 * Copyright (C) 2007  David Cantrell <david.l.cantrell@gmail.com>
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

static PyObject *dopysync(PyObject *self, PyObject *args) {
	sync();
	Py_INCREF(Py_None);
	return Py_None;
}

static PyMethodDef pysyncMethods[] = {
	{ "pysync", (PyCFunction) dopysync, METH_VARARGS, NULL },
	{ NULL, NULL, 0, NULL }
};

void initpysync(void) {
	PyObject *m, *d;

	m = Py_InitModule("pysync", pysyncMethods);
	d = PyModule_GetDict(m);
}
