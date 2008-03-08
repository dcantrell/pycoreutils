/*
 * pyhostid.c - hostid(1) core functionality
 *
 * This copyrighted material is made available to anyone wishing to use,
 * modify, copy, or redistribute it subject to the terms and conditions of
 * the GNU General Public License v.2.  This program is distributed in the
 * hope that it will be useful, but WITHOUT ANY WARRANTY expressed or
 * implied, including the implied warranties of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
 * details.  You should have received a copy of the GNU General Public
 * License along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
 * USA. Any Red Hat trademarks that are incorporated in the source code or
 * documentation are not subject to the GNU General Public License and may
 * only be used or replicated with the express permission of Red Hat, Inc.
 *
 * Author: David Cantrell <dcantrell@redhat.com>
 */

#include <Python.h>
#include <unistd.h>

static PyObject *dopyhostid(PyObject *self, PyObject *args) {
	unsigned int id;
	char ret[9];

	id = gethostid();
	id &= 0xffffffff;
	if (sprintf(ret, "%08x", id) < 0)
		return NULL;

	return Py_BuildValue("s", ret);
}

static PyMethodDef pyhostidMethods[] = {
	{ "pyhostid", (PyCFunction) dopyhostid, METH_VARARGS, NULL },
	{ NULL, NULL, 0, NULL }
};

void initpyhostid(void) {
	PyObject *m, *d;

	m = Py_InitModule("pyhostid", pyhostidMethods);
	d = PyModule_GetDict(m);
}
