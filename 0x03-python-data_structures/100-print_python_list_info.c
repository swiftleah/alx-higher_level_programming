#include <Python.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	if (!PyList_Check(p))
	{
		fprintf(stderr, "Object is not a list.\n");
		return;
	}

	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", allocated);

	for (Py_ssize_t i = 0; i < size; ++i)
	{
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
